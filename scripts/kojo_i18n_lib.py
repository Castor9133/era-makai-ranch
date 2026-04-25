# -*- coding: utf-8 -*-
"""口上 MESSAGE_BOX 提取/回写共用：解析 @" 逐字串（"" 表示 "）。"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Iterator

# CALL MESSAGE_BOX,@"…" ；允许逗号周围空白
MESSAGE_BOX_HEAD = re.compile(
    rb"CALL\s+MESSAGE_BOX\s*,\s*@\"",
    re.IGNORECASE,
)


def repo_root_from_scripts() -> Path:
    return Path(__file__).resolve().parent.parent


def parse_verbatim_after_atquote(data: bytes, open_quote_at: int) -> tuple[bytes, int] | None:
    """
    data[open_quote_at] 必须为双引号 "（开启 @" 之后第一个引号位置）。
    返回 (内部原文的 UTF-8 字节，不含外层引号；若把 "" 解为单 " 则解码后文本)，以及结束位置（闭合 " 的下一字节索引）。
    """
    if open_quote_at >= len(data) or data[open_quote_at : open_quote_at + 1] != b'"':
        return None
    i = open_quote_at + 1
    out = bytearray()
    while i < len(data):
        if data[i] == ord('"'):
            if i + 1 < len(data) and data[i + 1] == ord('"'):
                out.append(ord('"'))
                i += 2
                continue
            return bytes(out), i + 1
        out.append(data[i])
        i += 1
    return None


def find_message_box_string_spans(line_bytes: bytes) -> list[tuple[int, int, bytes]]:
    """
    一行内可能有多个 CALL MESSAGE_BOX（少见），全部找出。
    每项：(open_quote_index, end_after_closing_quote, inner_decoded_bytes)
    open_quote_index 为 @" 之后起始 " 的下标；end_after_closing_quote 为闭合 " 的下一字节下标。
    """
    spans: list[tuple[int, int, bytes]] = []
    for m in MESSAGE_BOX_HEAD.finditer(line_bytes):
        q = m.end() - 1  # 指向 @" 的起始 "
        parsed = parse_verbatim_after_atquote(line_bytes, q)
        if not parsed:
            continue
        inner, end_after_close = parsed
        spans.append((q, end_after_close, inner))
    return spans


def stable_id(rel_path: str, line_no: int, inner_text: str) -> str:
    h = hashlib.sha256(f"{rel_path}\n{line_no}\n{inner_text}".encode("utf-8")).hexdigest()
    return h[:16]


def encode_verbatim_inner(text: str) -> str:
    """逻辑文本 → 写入 @" 内部（" → ""）。"""
    return text.replace('"', '""')


def iter_erb_files(root: Path) -> Iterator[Path]:
    for p in sorted(root.rglob("*.ERB")):
        if p.is_file():
            yield p


def load_jsonl(path: Path) -> list[dict]:
    rows: list[dict] = []
    raw = path.read_bytes()
    text = raw.decode("utf-8-sig")
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        rows.append(json.loads(line))
    return rows


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


def extract_placeholders(text: str) -> list[str]:
    return re.findall(r"%[^%]+%", text)
