# -*- coding: utf-8 -*-
"""汎用口上 *_調教コマンド*.ERB 与 CSV/Train.csv 第二列指令名对照。"""
from __future__ import annotations

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
CSV_TRAIN = ROOT / "CSV" / "Train.csv"
KOJO_DIR = ROOT / "ERB" / "○口上" / "汎用口上"


def parse_train_names() -> dict[int, str]:
    out: dict[int, str] = {}
    for raw in CSV_TRAIN.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw.strip()
        if not line or line.startswith(";"):
            continue
        m = re.match(r"^(\d+)\s*,\s*(.+?)\s*$", line)
        if not m:
            continue
        out[int(m.group(1))] = m.group(2)
    return out


def extract_top_args1_cases_and_groupmatch(text: str) -> set[str]:
    names: set[str] = set()
    for m in re.finditer(
        r"GROUPMATCH\s*\(\s*ARGS:1\s*,\s*((?:\s*\"[^\"]*\"\s*,?)+\s*\"[^\"]*\"\s*)\)",
        text,
    ):
        chunk = m.group(1)
        for s in re.findall(r'"([^"]*)"', chunk):
            names.add(s)

    lines = text.splitlines()
    stack: list[str] = []

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if stripped.startswith(";"):
            i += 1
            continue

        msel = re.search(r"SELECTCASE\s+ARGS:(\d+)", line)
        if msel:
            n = int(msel.group(1))
            stack.append("A1" if n == 1 else f"A{n}")
            i += 1
            continue

        if stripped == "ENDSELECT" or stripped.startswith("ENDSELECT "):
            if stack:
                stack.pop()
            i += 1
            continue

        # 汉化分册常见：SELECTCASE ARGS:2 → CASE "执行" → SELECTCASE ARGS:1 → CASE "揉胸"
        if stack and stack[-1] == "A1" and re.match(r"^\s*CASE\s+", line) and "CASEELSE" not in line:
            for s in re.findall(r'"([^"]*)"', line):
                names.add(s)

        i += 1

    return names


def main() -> int:
    if not CSV_TRAIN.exists():
        print("missing", CSV_TRAIN, file=sys.stderr)
        return 1
    train = parse_train_names()
    train_names = set(train.values())

    train_files = sorted(KOJO_DIR.glob("*_調教コマンド*.ERB"))
    if not train_files:
        print("no train erb under", KOJO_DIR, file=sys.stderr)
        return 1

    per_file: list[tuple[str, set[str]]] = []
    union: set[str] = set()
    for p in train_files:
        t = p.read_text(encoding="utf-8", errors="replace")
        s = extract_top_args1_cases_and_groupmatch(t)
        per_file.append((p.name, s))
        union |= s

    noise = {"", "执行", "移除", "初次", "普通"}
    union_cmd = union - noise
    extra = sorted(union_cmd - train_names)
    missing = sorted(train_names - union_cmd)

    out_path = ROOT / "docs" / "汎用調教分册_Train欠番表.md"
    md: list[str] = []
    md.append("# 汎用調教分册 × Train.csv 欠番对照\n")
    md.append(
        "> 由 `tools/diff_train_kojo_generic.py` 生成：在 "
        "`ERB/○口上/汎用口上/*_調教コマンド*.ERB` 中收集 "
        "「当前嵌套层级最内为 `SELECTCASE ARGS:1`」时的所有 `CASE \"…\"` 字面量，"
        "并合并全文件中的 `GROUPMATCH(ARGS:1,…)` 字面量。"
        "（兼容先 `SELECTCASE ARGS:2` → `执行` 再 `ARGS:1` 的汉化分册结构。）"
        "仅靠 `CASEELSE` 兜底的指令**不会**出现在并集中。\n"
    )
    md.append(f"- Train 有效指令条目: **{len(train_names)}**\n")
    md.append(f"- 汎用調教分册文件数: **{len(train_files)}**\n")
    md.append(f"- 并集指令字符串数: **{len(union_cmd)}**\n")

    md.append("\n## 一、Train 有、并集中无\n\n")
    if not missing:
        md.append("（无）\n")
    else:
        for name in missing:
            num = next((n for n, v in train.items() if v == name), None)
            line = f"- COM{num}, `{name}`\n" if num is not None else f"- `{name}`\n"
            md.append(line)

    md.append("\n## 二、并集有、Train 无（别名 / 拼写差异 / 非 COM 字符串）\n\n")
    if not extra:
        md.append("（无）\n")
    else:
        for name in extra:
            md.append(f"- `{name}`\n")

    md.append("\n## 三、各分册覆盖 Train 条数\n\n")
    md.append("| 文件 | 显式覆盖数 | 未在 CASE/GROUPMATCH 出现数 |\n")
    md.append("| --- | ---: | ---: |\n")
    for fname, s in per_file:
        cov = train_names & (s - noise)
        miss_n = len(train_names - (s - noise))
        md.append(f"| {fname} | {len(cov)} | {miss_n} |\n")
    md.append(
        "\n## 四、说明\n\n"
        "- 「并集有、Train 无」中的 `Ｖ性交` / `Ｖ注射` 等多为共用转发或魔改内部分组字符串，"
        "与 `Train.csv` 第二列并非一一对应，需人工对照，不能直接当缺行删除。\n"
        "- 曾用错误文件名 `元気っ子口上1_調教コマンド .ERB`（扩展名前多余空格）已更名为 "
        "`元気っ子口上1_調教コマンド.ERB`。\n"
        "- 重新生成本表：`python tools/diff_train_kojo_generic.py`（在仓库根目录执行）。\n"
    )

    out_path.write_text("".join(md), encoding="utf-8")

    for line in md:
        print(line, end="")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
