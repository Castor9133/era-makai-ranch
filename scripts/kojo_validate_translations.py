# -*- coding: utf-8 -*-
"""校验翻译 JSONL：占位符（%…%）数量须与 source 一致。"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

_SCRIPTS = Path(__file__).resolve().parent
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

from kojo_i18n_lib import extract_placeholders


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--translations", type=Path, required=True)
    args = ap.parse_args()
    raw = args.translations.read_bytes().decode("utf-8-sig")
    errors = 0
    checked = 0
    for line in raw.splitlines():
        line = line.strip()
        if not line:
            continue
        r = json.loads(line)
        zh = r.get("zh_CN") or r.get("translation") or ""
        if not zh.strip():
            continue
        checked += 1
        s = r.get("source") or ""
        ps = extract_placeholders(s)
        pz = extract_placeholders(zh)
        if len(ps) != len(pz):
            errors += 1
            print(f"[count] id={r.get('id')} line={r.get('line')} path={r.get('path')}")
            print(f"  source placeholders: {ps}")
            print(f"  zh_CN placeholders: {pz}")
            continue
        sm = sorted(ps)
        zm = sorted(pz)
        if sm != zm:
            errors += 1
            print(f"[set] id={r.get('id')} line={r.get('line')} path={r.get('path')}")
            print(f"  source: {sm}")
            print(f"  zh_CN: {zm}")

    print("checked_records:", checked)
    print("errors:", errors)


if __name__ == "__main__":
    main()
