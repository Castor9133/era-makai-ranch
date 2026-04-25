# -*- coding: utf-8 -*-
"""合并已翻译的分批 JSONL（每行含 zh_CN）为单一 kojo_messagebox_translations.jsonl。"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

_SCRIPTS = Path(__file__).resolve().parent
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

from kojo_i18n_lib import repo_root_from_scripts, write_jsonl


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", type=Path, required=True, help="out/batches")
    ap.add_argument(
        "--out",
        type=Path,
        default=None,
        help="默认 out/kojo_messagebox_translations.jsonl",
    )
    args = ap.parse_args()
    out = args.out or (repo_root_from_scripts() / "out" / "kojo_messagebox_translations.jsonl")
    parts = sorted(args.dir.glob("part_*.jsonl"))
    if not parts:
        raise SystemExit("no part_*.jsonl found")
    merged: list[dict] = []
    seen: set[str] = set()
    dup = 0
    for p in parts:
        raw = p.read_bytes().decode("utf-8-sig")
        for line in raw.splitlines():
            line = line.strip()
            if not line:
                continue
            r = json.loads(line)
            rid = r.get("id", "")
            if rid in seen:
                dup += 1
                continue
            seen.add(rid)
            merged.append(r)

    write_jsonl(out, merged)
    print("merged_entries:", len(merged), "dup_skipped:", dup)
    print("written:", out)


if __name__ == "__main__":
    main()
