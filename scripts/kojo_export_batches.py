# -*- coding: utf-8 -*-
"""将抽取结果 JSONL 切成多份 batch（便于分批机翻），写 out/batches/part_XXXXX.jsonl。"""
from __future__ import annotations

import argparse
import math
import sys
from pathlib import Path

_SCRIPTS = Path(__file__).resolve().parent
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

from kojo_i18n_lib import load_jsonl, repo_root_from_scripts, write_jsonl


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="inp", type=Path, required=True, help="kojo_messagebox_strings.jsonl")
    ap.add_argument(
        "--out-dir",
        type=Path,
        default=None,
        help="默认 repo/out/batches",
    )
    ap.add_argument("--size", type=int, default=500, help="每条 batch 最多行数")
    args = ap.parse_args()
    out_dir = args.out_dir or (repo_root_from_scripts() / "out" / "batches")
    rows = load_jsonl(args.inp)
    out_dir.mkdir(parents=True, exist_ok=True)
    readme = out_dir / "README.txt"
    readme.write_text(
        "分批 JSONL：可直接送机翻 API；翻译完成后在每行补上 zh_CN，再 kojo_import_batches。\n",
        encoding="utf-8",
    )

    n = len(rows)
    chunks = max(1, math.ceil(n / args.size))
    width = max(5, len(str(chunks)))
    for i in range(chunks):
        part = rows[i * args.size : (i + 1) * args.size]
        name = f"part_{i+1:0{width}d}.jsonl"
        write_jsonl(out_dir / name, part)

    prog = out_dir.parent / "BATCH_PROGRESS.md"
    prog.write_text(
        f"- source: `{args.inp.as_posix()}`\n"
        f"- total_entries: {n}\n"
        f"- batch_size: {args.size}\n"
        f"- batch_files: {chunks}\n",
        encoding="utf-8",
    )
    print("batches:", chunks, "dir:", out_dir)


if __name__ == "__main__":
    main()
