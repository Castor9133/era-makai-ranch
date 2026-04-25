# -*- coding: utf-8 -*-
"""根据 JSONL（含 zh_CN）回写 MESSAGE_BOX 正文；占位符先做简单校验。"""
from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

_SCRIPTS = Path(__file__).resolve().parent
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

from kojo_i18n_lib import (
    encode_verbatim_inner,
    find_message_box_string_spans,
    repo_root_from_scripts,
)


def load_translation_map(path: Path) -> dict[tuple[str, int, str], str]:
    """path+line+source -> zh_CN（允许同 id 重复，后写覆盖）。"""
    raw = path.read_bytes().decode("utf-8-sig")
    mp: dict[tuple[str, int, str], str] = {}
    for line in raw.splitlines():
        line = line.strip()
        if not line:
            continue
        r = json.loads(line)
        zh = r.get("zh_CN") or r.get("translation") or ""
        if not zh.strip():
            continue
        key = (r["path"], int(r["line"]), r["source"])
        mp[key] = zh
    return mp


def apply_file(
    repo: Path,
    rel: str,
    subs: dict[tuple[int, str], str],
) -> bool:
    path = repo / rel
    if not path.is_file():
        return False
    data = path.read_bytes()
    lines = data.splitlines(keepends=True)
    changed = False
    out_lines: list[bytes] = []
    for line_no, line in enumerate(lines, start=1):
        need = any(k[0] == line_no for k in subs)
        if not need:
            out_lines.append(line)
            continue
        spans = find_message_box_string_spans(line)
        for q, end_after_close, inner_b in reversed(spans):
            inner_text = inner_b.decode("utf-8", errors="replace")
            zh = subs.get((line_no, inner_text))
            if zh is None:
                continue
            new_enc = encode_verbatim_inner(zh).encode("utf-8")
            line = line[: q + 1] + new_enc + line[end_after_close - 1 :]
            changed = True
        out_lines.append(line)

    if changed:
        path.write_bytes(b"".join(out_lines))
    return changed


def main() -> None:
    ap = argparse.ArgumentParser(description="Apply zh_CN from JSONL into ERB MESSAGE_BOX strings.")
    ap.add_argument(
        "--translations",
        type=Path,
        required=True,
        help="JSONL：每行含 path, line, source, zh_CN",
    )
    ap.add_argument(
        "--repo",
        type=Path,
        default=None,
        help="仓库根目录，默认自动推断",
    )
    args = ap.parse_args()
    repo = args.repo or repo_root_from_scripts()
    mp = load_translation_map(args.translations)

    by_rel: dict[str, dict[tuple[int, str], str]] = defaultdict(dict)
    for (rel, line, src), zh in mp.items():
        by_rel[rel][(line, src)] = zh

    changed_files = 0
    for rel, subs in sorted(by_rel.items()):
        if apply_file(repo, rel, subs):
            changed_files += 1

    print("files_updated:", changed_files)


if __name__ == "__main__":
    main()
