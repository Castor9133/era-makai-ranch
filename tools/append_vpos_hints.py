# -*- coding: utf-8 -*-
from pathlib import Path

root = Path(__file__).resolve().parents[1]
main = root / "ERB" / "○口上" / "汎用口上" / "○調教_V体位_日语前缀.ERB"
snippet = Path(__file__).resolve().parent / "_vpos_hint_append.txt"
a = main.read_text(encoding="utf-8").rstrip()
b = snippet.read_text(encoding="utf-8").strip()
main.write_text(a + "\n" + b + "\n", encoding="utf-8")
print("ok", main)
