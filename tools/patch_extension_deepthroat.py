# -*- coding: utf-8 -*-
import pathlib
import re

p = pathlib.Path(__file__).resolve().parents[1] / "ERB" / "○口上" / "汎用口上" / "○調教_性行为扩展前缀.ERB"
t = p.read_text(encoding="utf-8")

def repl_deep(m: re.Match) -> str:
    return (
        'CASE "深喉"\n'
        '\t\tCALL MESSAGE_BOX,@"「……唔咕……！……噜……♥」\\n（喉被占满，整句只能烂在舌根后……）"'
    )


def repl_tent(m: re.Match) -> str:
    return (
        'CASE "触手深喉"\n'
        '\t\tCALL MESSAGE_BOX,@"「……咕噜……！……呜……♥」\\n（触手堵死声道，只剩呛咳与吸盘扯的含糊声……）"'
    )

t2, n1 = re.subn(
    r'CASE "深喉"\s*\n\s*CALL MESSAGE_BOX,@"[^"]+"',
    repl_deep,
    t,
)
t2, n2 = re.subn(
    r'CASE "触手深喉"\s*\n\s*CALL MESSAGE_BOX,@"[^"]+"',
    repl_tent,
    t2,
)
t2, n3 = re.subn(
    r'CASE "触手口交","触手深喉"\s*\n\s*CALL MESSAGE_BOX,@"[^"]+"',
    'CASE "触手口交","触手深喉"\n'
    '\t\tCALL MESSAGE_BOX,@"「……唔……！……咕噜……♥」\\n（嘴或喉被触手塞死，说不清，只有闷哼与吞咽……）"',
    t2,
)
p.write_text(t2, encoding="utf-8")
print("深喉", n1, "触手深喉", n2, "合并触手", n3)
