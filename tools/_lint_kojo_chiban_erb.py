# -*- coding: utf-8 -*-
"""Structural lint for 口上 + 地の文 ERB (line-start IF/ENDIF, SELECTCASE, FOR/NEXT, REPEAT/REND, WHILE/WEND)."""
from __future__ import annotations

import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
ERB = ROOT / "ERB"
# ○口上 vs ◯地の文（Unicode 圆圈不同）
SUBDIRS = ("○口上", "◯地の文")


def _strip_semicolon_comment(line: str) -> str:
    if ";" in line:
        return line.split(";", 1)[0]
    return line


def _line_starts_keywords(full_text: str) -> dict[str, int]:
    """行首（去分号注释后 strip）统计，避免 MESSAGE_BOX 里的英文 IF/SELECTCASE 误报。"""
    keys = (
        "IF",
        "ELSEIF",
        "ENDIF",
        "SIF",
        "SELECTCASE",
        "ENDSELECT",
        "FOR",
        "NEXT",
        "REPEAT",
        "REND",
        "WHILE",
        "WEND",
    )
    counts = {k: 0 for k in keys}
    for raw in full_text.splitlines():
        line = _strip_semicolon_comment(raw).strip()
        if not line:
            continue
        up = line.split(None, 1)[0].upper()
        for k in keys:
            if up == k:
                counts[k] += 1
                break
    return counts


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    issues: list[tuple[str, str]] = []
    scanned = 0

    for sub in SUBDIRS:
        base = ERB / sub
        if not base.is_dir():
            print(f"[skip] missing: {base}", file=sys.stderr)
            continue
        for p in sorted(base.rglob("*")):
            if not p.is_file() or p.suffix.lower() != ".erb":
                continue
            scanned += 1
            t = p.read_text(encoding="utf-8", errors="replace")
            ls = _line_starts_keywords(t)

            n_if, n_endif = ls["IF"], ls["ENDIF"]
            n_sel, n_es = ls["SELECTCASE"], ls["ENDSELECT"]
            n_for, n_next = ls["FOR"], ls["NEXT"]
            n_rep, n_rend = ls["REPEAT"], ls["REND"]
            n_while, n_wend = ls["WHILE"], ls["WEND"]

            bad: list[str] = []
            if n_if != n_endif:
                bad.append(f"IF={n_if} ENDIF={n_endif} (line-start)")
            if n_sel != n_es:
                bad.append(f"SELECTCASE={n_sel} ENDSELECT={n_es} (line-start)")
            if n_for != n_next:
                bad.append(f"FOR={n_for} NEXT={n_next} (line-start)")
            if n_rep != n_rend:
                bad.append(f"REPEAT={n_rep} REND={n_rend} (line-start)")
            if n_while != n_wend:
                bad.append(f"WHILE={n_while} WEND={n_wend} (line-start)")

            if bad:
                rel = p.relative_to(ROOT)
                issues.append((str(rel), "; ".join(bad)))

    print(f"[struct] scanned={scanned} mismatch_files={len(issues)}")
    for path, msg in issues[:100]:
        print(f"  {path} | {msg}")
    if len(issues) > 100:
        print(f"  ... +{len(issues) - 100} more")
    return 1 if issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
