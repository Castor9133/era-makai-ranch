# -*- coding: utf-8 -*-
"""
用 DeepSeek OpenAI 兼容接口润色中文口上/文案（model: deepseek-v4-pro）。

前置：设置环境变量 DEEPSEEK_API_KEY（不要把 key 写进仓库或聊天）。

示例（PowerShell）：
  $env:DEEPSEEK_API_KEY = "sk-..."
  python scripts/kojo_deepseek_polish.py --file "ERB/○口上/汎用口上/知心口上1_調教コマンド.ERB"

仅打印润色结果到 stdout，不自动回写文件，便于 diff。
可选：--expand 略扩短句；--stdin-json 从 stdin 读 JSON 字符串数组，输出等长 JSON（UTF-8 管道勿经错误编码页）。
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

DEFAULT_BASE = "https://api.deepseek.com"
DEFAULT_MODEL = "deepseek-v4-pro"

SYSTEM_KOJO = """你是中文润色编辑，润色游戏口上/地文台词。
要求：
1. 保持主奴位阶与原文情绪（恳求、委屈、嘴硬等）不变；奴隶台词不得写成指导、训诫主人（除非原文明确是照顾事后乏力等情境）。
2. 所有形如 %...()% 或 %CALLNAME:...% 的占位符必须原样保留，一字不改、不拆开、不翻译。
3. 不添加注释或 Markdown，只输出润色后的正文（若输入是多段 MESSAGE_BOX 内文，保持段落结构相近）。"""

SYSTEM_KOJO_EXPAND = (
    SYSTEM_KOJO
    + "\n4. 若某句偏短，可在不改变含义的前提下略扩半句到一句，使口癖更饱满；总长度不要翻倍。"
)


def chat_complete(
    api_key: str, user_text: str, *, base: str, model: str, system: str | None = None
) -> str:
    url = base.rstrip("/") + "/v1/chat/completions"
    sys_msg = system if system is not None else SYSTEM_KOJO
    body = {
        "model": model,
        "messages": [
            {"role": "system", "content": sys_msg},
            {"role": "user", "content": user_text},
        ],
        "temperature": 0.35,
    }
    data = json.dumps(body, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            raw = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {e.code}: {err_body}") from e
    choices = raw.get("choices") or []
    if not choices:
        raise RuntimeError(f"Unexpected response: {raw!r}")
    msg = choices[0].get("message") or {}
    content = msg.get("content")
    if not isinstance(content, str):
        raise RuntimeError(f"No content in choices[0]: {raw!r}")
    return content.strip()


def main() -> int:
    p = argparse.ArgumentParser(description="DeepSeek v4-pro 中文润色（stdout）")
    p.add_argument("--file", type=Path, help="UTF-8 文本路径，整文件作为 user 内容")
    p.add_argument(
        "--text",
        help="直接传入要润色的字符串（短片段测试）",
    )
    p.add_argument(
        "--expand",
        action="store_true",
        help="在润色基础上允许适度扩写短句（仍遵守占位符与位阶）",
    )
    p.add_argument(
        "--stdin-json",
        action="store_true",
        help="从 stdin 读入 JSON 数组（字符串列表），向 stdout 输出等长 JSON 数组（仅润色后字符串）",
    )
    p.add_argument("--base", default=os.environ.get("DEEPSEEK_BASE_URL", DEFAULT_BASE))
    p.add_argument("--model", default=os.environ.get("DEEPSEEK_MODEL", DEFAULT_MODEL))
    args = p.parse_args()

    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass

    api_key = os.environ.get("DEEPSEEK_API_KEY", "").strip()
    if not api_key:
        print("错误：请设置环境变量 DEEPSEEK_API_KEY。", file=sys.stderr)
        return 2

    if args.stdin_json:
        raw_in = sys.stdin.read()
        try:
            arr_in = json.loads(raw_in)
        except json.JSONDecodeError as e:
            print(f"stdin JSON 解析失败: {e}", file=sys.stderr)
            return 2
        if not isinstance(arr_in, list) or not all(isinstance(x, str) for x in arr_in):
            print("stdin 须为 JSON 字符串数组。", file=sys.stderr)
            return 2
        user_text = (
            "输入为 JSON 字符串数组（口上对白原文）。\n"
            "请只输出**等长**的 JSON 数组（仅字符串元素），顺序一一对应；"
            "润色中文并保持所有 %…% 占位符原样；勿用 markdown 围栏；勿加解释。\n"
            + json.dumps(arr_in, ensure_ascii=False)
        )
    elif args.text is not None:
        user_text = args.text
    elif args.file is not None:
        user_text = args.file.read_text(encoding="utf-8")
    else:
        print("请指定 --file 或 --text 或 --stdin-json。", file=sys.stderr)
        return 2

    system = SYSTEM_KOJO_EXPAND if args.expand else SYSTEM_KOJO
    out = chat_complete(
        api_key, user_text, base=args.base, model=args.model, system=system
    )
    if args.stdin_json:
        out_stripped = out.strip()
        if out_stripped.startswith("```"):
            # 去掉偶发围栏
            lines = out_stripped.split("\n")
            if lines and lines[0].startswith("```"):
                lines = lines[1:]
            if lines and lines[-1].strip() == "```":
                lines = lines[:-1]
            out_stripped = "\n".join(lines).strip()
        try:
            arr_out = json.loads(out_stripped)
        except json.JSONDecodeError:
            print("模型未返回合法 JSON，原文如下：", file=sys.stderr)
            sys.stderr.write(out_stripped[:4000])
            sys.stderr.write("\n")
            return 3
        if not isinstance(arr_out, list) or len(arr_out) != len(arr_in):
            print(
                f"返回数组长度不符：输入 {len(arr_in)} 输出 {len(arr_out) if isinstance(arr_out, list) else type(arr_out)}",
                file=sys.stderr,
            )
            return 3
        sys.stdout.write(json.dumps(arr_out, ensure_ascii=False))
        sys.stdout.write("\n")
        return 0

    sys.stdout.write(out)
    if not out.endswith("\n"):
        sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
