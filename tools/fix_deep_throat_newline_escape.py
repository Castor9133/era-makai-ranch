# -*- coding: utf-8 -*-
"""Fix broken MESSAGE_BOX newlines in TEQUIP:深喉 blocks (\\n was lost)."""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1] / "ERB" / "○口上" / "汎用口上"

FIXES = [
    (
        '\t\tCALL MESSAGE_BOX,@"「……唔咕……！……咳咳……♥」\n（喉咙被堵死，高潮从窒闷里顶上来，声带挤不出整句……）"',
        '\t\tCALL MESSAGE_BOX,@"「……唔咕……！……咳咳……♥」\\n（喉咙被堵死，高潮从窒闷里顶上来，声带挤不出整句……）"',
    ),
    (
        '\t\tCALL MESSAGE_BOX,@"「……噜……嗯呃……♥」\n（只剩鼻腔与喉间的水声、呛咳在替身体尖叫……）"',
        '\t\tCALL MESSAGE_BOX,@"「……噜……嗯呃……♥」\\n（只剩鼻腔与喉间的水声、呛咳在替身体尖叫……）"',
    ),
]

def main():
    nfiles = 0
    for p in sorted(ROOT.glob("*口上1.ERB")):
        if "_調教" in p.name or "_イベント" in p.name:
            continue
        t = p.read_text(encoding="utf-8")
        ot = t
        for a, b in FIXES:
            t = t.replace(a, b)
        if t != ot:
            p.write_text(t, encoding="utf-8")
            nfiles += 1
    print("repaired", nfiles)

if __name__ == "__main__":
    main()
