# -*- coding: utf-8 -*-
"""Rewrite 绝顶 TEQUIP:深喉 MESSAGE_BOX pairs: no intelligible speech in 「」, meaning in （）."""
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1] / "ERB" / "○口上" / "汎用口上"

# Two universal lines (personality nuance lives in 进阶调教 / train; climax here = blocked throat)
LINE1 = (
    '\tSIF TEQUIP:深喉\n'
    '\t\tCALL MESSAGE_BOX,@"「……唔咕……！……咳咳……♥」\\n（喉咙被堵死，高潮从窒闷里顶上来，声带挤不出整句……）"'
)
LINE2 = (
    '\tSIF TEQUIP:深喉\n'
    '\t\tCALL MESSAGE_BOX,@"「……噜……嗯呃……♥」\\n（只剩鼻腔与喉间的水声、呛咳在替身体尖叫……）"'
)

BLOCK_PATTERN = re.compile(
    r"\tSIF TEQUIP:深喉\n\t\tCALL MESSAGE_BOX,@\"[^\"]+\"\n"
    r"\tSIF TEQUIP:深喉\n\t\tCALL MESSAGE_BOX,@\"[^\"]+\"",
    re.MULTILINE,
)


def main():
    fixed = []
    for p in sorted(ROOT.glob("*口上1.ERB")):
        if "_調教" in p.name or "_イベント" in p.name:
            continue
        t = p.read_text(encoding="utf-8")
        if "CASE \"绝顶\"" not in t or "TEQUIP:深喉" not in t:
            continue
        nt, n = BLOCK_PATTERN.subn(LINE1 + "\n" + LINE2, t, count=1)
        if n:
            p.write_text(nt, encoding="utf-8")
            fixed.append(p.name)
        else:
            print("skip no match:", p.name)
    print("fixed", len(fixed), "files")


if __name__ == "__main__":
    main()
