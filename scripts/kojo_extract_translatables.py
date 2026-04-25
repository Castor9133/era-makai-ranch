# -*- coding: utf-8 -*-
"""扫描 ERB 中 CALL MESSAGE_BOX,@"…" 并导出 JSONL（供机翻/人工翻译 pipeline）。"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

_SCRIPTS = Path(__file__).resolve().parent
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

from kojo_i18n_lib import (
    find_message_box_string_spans,
    iter_erb_files,
    repo_root_from_scripts,
    stable_id,
    write_jsonl,
)


def main() -> None:
    ap = argparse.ArgumentParser(description="Extract MESSAGE_BOX @\"…\" strings from kojo ERB files.")
    ap.add_argument(
        "--root",
        type=Path,
        default=None,
        help="ERB 子目录，默认 repo/ERB/○口上",
    )
    ap.add_argument(
        "--out",
        type=Path,
        default=None,
        help="输出 JSONL，默认 out/kojo_messagebox_strings.jsonl",
    )
    args = ap.parse_args()
    root = args.root or (repo_root_from_scripts() / "ERB" / "○口上")
    out = args.out or (repo_root_from_scripts() / "out" / "kojo_messagebox_strings.jsonl")

    repo = repo_root_from_scripts()
    rows: list[dict] = []

    for path in iter_erb_files(root):
        try:
            data = path.read_bytes()
        except OSError:
            continue
        rel = path.relative_to(repo).as_posix()
        lines = data.splitlines(keepends=True)
        for line_no, line in enumerate(lines, start=1):
            spans = find_message_box_string_spans(line)
            for _q, _end, inner_b in spans:
                inner_text = inner_b.decode("utf-8", errors="replace")
                sid = stable_id(rel, line_no, inner_text)
                rows.append(
                    {
                        "id": sid,
                        "path": rel,
                        "line": line_no,
                        "source": inner_text,
                    }
                )

    write_jsonl(out, rows)
    stats_path = out.with_suffix(out.suffix + ".stats.txt")
    stats_path.parent.mkdir(parents=True, exist_ok=True)
    stats_path.write_text(
        f"files_scanned_under: {root.as_posix()}\n"
        f"entries: {len(rows)}\n",
        encoding="utf-8",
    )
    print("written:", out)
    print("entries:", len(rows))


if __name__ == "__main__":
    main()
