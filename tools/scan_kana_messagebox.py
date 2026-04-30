# -*- coding: utf-8 -*-
"""Scan 汎用口上 main files for hiragana/katakana inside MESSAGE_BOX strings."""
from __future__ import annotations

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
KOJO = ROOT / "ERB" / "○口上" / "汎用口上"

# Hiragana + katakana + prolonged sound mark (ー)
KANA = re.compile(r"[\u3041-\u3096\u30A1-\u30FA\u30FC]")

FILES = [
    "人妻口上1.ERB",
    "仇恨口上1.ERB",
    "堅物口上1.ERB",
    "女仆口上1.ERB",
    "妹系口上1.ERB",
    "愚忠口上1.ERB",
    "懦弱口上1.ERB",
    "知心口上1.ERB",
    "虔诚口上1.ERB",
    "闷骚小姐姐口上1.ERB",
    "大和抚子口上1.ERB",
    "天然口上1.ERB",
    "強気口上1.ERB",
    "元気っ子口上1.ERB",
    "温柔大姐姐口上1.ERB",
    "無口口上1.ERB",
    "気品口上1.ERB",
    "非敬語幼め口上1.ERB",
]


def main() -> int:
    out_lines: list[str] = []
    for name in FILES:
        p = KOJO / name
        if not p.exists():
            out_lines.append(f"MISSING {name}\n")
            continue
        text = p.read_text(encoding="utf-8", errors="replace")
        hits: list[tuple[int, str]] = []
        for i, line in enumerate(text.splitlines(), 1):
            if "MESSAGE_BOX" not in line:
                continue
            if KANA.search(line):
                hits.append((i, line.rstrip()))
        out_lines.append(f"## {name}  (MESSAGE_BOX lines with kana: {len(hits)})\n")
        for ln, content in hits:
            out_lines.append(f"L{ln}: {content}\n")
        out_lines.append("\n")
    out_path = ROOT / "tools" / "_kana_messagebox_hits.txt"
    out_path.write_text("".join(out_lines), encoding="utf-8")
    print(out_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
