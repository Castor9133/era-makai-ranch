# -*- coding: utf-8 -*-
import pathlib

d = pathlib.Path(__file__).resolve().parents[1] / "ERB" / "○口上" / "汎用口上"
key = "CASE " + '"' + "\uff36\u6027\u4ea4" + '"'
for p in sorted(d.glob("*_調教コマンド.ERB")):
    t = p.read_text(encoding="utf-8", errors="ignore")
    if key in t:
        print(p.name)
