# -*- coding: utf-8 -*-
import sys
from pathlib import Path

name = sys.argv[1] if len(sys.argv) > 1 else "無口口上1.ERB"
p = Path(__file__).resolve().parents[1] / "ERB" / "○口上" / "汎用口上" / name
t = p.read_text(encoding="utf-8")
for i, line in enumerate(t.splitlines(), 1):
    if "CALL MESSAGE_BOX" not in line:
        continue
    if "「" in line and "」" not in line:
        print(i, line.strip()[:120])
