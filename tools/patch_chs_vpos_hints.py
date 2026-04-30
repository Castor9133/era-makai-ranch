# -*- coding: utf-8 -*-
"""Insert KOJO_JP_VPOS_HINT calls into KOJO_CHS_VPOS_* in ○泛用口上_V体位九_分岐台詞.ERB."""
from __future__ import annotations

from pathlib import Path

root = Path(__file__).resolve().parents[1]
path = root / "ERB" / "○口上" / "汎用口上" / "○泛用口上_V体位九_分岐台詞.ERB"

# CHS function suffix -> KOJO_JP_VPOS_HINT_* name (Emuera CALL target)
PAIRS: list[tuple[str, str]] = [
    ("温柔大姐姐1", "KOJO_JP_VPOS_HINT_温柔大姐姐1"),
    ("闷骚小姐姐1", "KOJO_JP_VPOS_HINT_闷骚小姐姐1"),
    ("人妻口上1", "KOJO_JP_VPOS_HINT_人妻1"),
    ("妹系口上1", "KOJO_JP_VPOS_HINT_妹系1"),
    ("天然口上1", "KOJO_JP_VPOS_HINT_天然1"),
    ("女仆口上1", "KOJO_JP_VPOS_HINT_女仆1"),
    ("大和抚子口上1", "KOJO_JP_VPOS_HINT_大和抚子1"),
    ("虔诚口上1", "KOJO_JP_VPOS_HINT_虔诚1"),
    ("知心口上1", "KOJO_JP_VPOS_HINT_知心1"),
    ("仇恨口上1", "KOJO_JP_VPOS_HINT_仇恨1"),
    ("懦弱口上1", "KOJO_JP_VPOS_HINT_懦弱1"),
]

INSERT = """\tSIF CFLAG:乳牛 || CFLAG:洗脑 || ＃陷落状态／恋慕以上＃ || ＃陷落状态／隶属＃
\t\tSIF STRLENS(ARGS:0) > 0
\t\t\tCALL {hint}(ARGS:0)
"""


def main() -> int:
    text = path.read_text(encoding="utf-8")
    orig = text
    for suffix, hint in PAIRS:
        head = f"@KOJO_CHS_VPOS_{suffix}(ARGS:0, ARGS:1)\nSELECTCASE ARGS:1\n"
        for branch in ('CASE "执行":', 'CASE "继续":'):
            needle = head + branch + "\n\tSELECTCASE ARGS:0"
            if needle not in text:
                raise SystemExit(f"missing needle for {suffix} {branch}")
            repl = head + branch + "\n" + INSERT.format(hint=hint) + "\tSELECTCASE ARGS:0"
            text = text.replace(needle, repl, 1)
    if text == orig:
        raise SystemExit("no changes")
    path.write_text(text, encoding="utf-8")
    print("patched", path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
