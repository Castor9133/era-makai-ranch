# -*- coding: utf-8 -*-
"""口上 i18n 流水线入口：extract | export-batches | import-batches | validate | apply"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def py(*args: str) -> int:
    cmd = [sys.executable, str(ROOT / args[0])] + list(args[1:])
    return subprocess.call(cmd)


def main() -> None:
    ap = argparse.ArgumentParser(description="Kojo MESSAGE_BOX i18n pipeline helper")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p1 = sub.add_parser("extract", help="抽取 MESSAGE_BOX -> out/kojo_messagebox_strings.jsonl")
    p1.add_argument("--root", type=Path, default=None)
    p1.add_argument("--out", type=Path, default=None)

    p2 = sub.add_parser("export-batches", help="切分 JSONL")
    p2.add_argument("--in", dest="inp", type=Path, required=True)
    p2.add_argument("--out-dir", type=Path, default=None)
    p2.add_argument("--size", type=int, default=500)

    p3 = sub.add_parser("import-batches", help="合并已翻译 batch")
    p3.add_argument("--dir", type=Path, required=True)
    p3.add_argument("--out", type=Path, default=None)

    p4 = sub.add_parser("validate", help="校验占位符")
    p4.add_argument("--translations", type=Path, required=True)

    p5 = sub.add_parser("apply", help="回写 ERB")
    p5.add_argument("--translations", type=Path, required=True)
    p5.add_argument("--repo", type=Path, default=None)

    args = ap.parse_args()

    if args.cmd == "extract":
        cmd = ["kojo_extract_translatables.py"]
        if args.root:
            cmd += ["--root", str(args.root)]
        if args.out:
            cmd += ["--out", str(args.out)]
        raise SystemExit(py(*cmd))

    if args.cmd == "export-batches":
        cmd = ["kojo_export_batches.py", "--in", str(args.inp), "--size", str(args.size)]
        if args.out_dir:
            cmd += ["--out-dir", str(args.out_dir)]
        raise SystemExit(py(*cmd))

    if args.cmd == "import-batches":
        cmd = ["kojo_import_batches.py", "--dir", str(args.dir)]
        if args.out:
            cmd += ["--out", str(args.out)]
        raise SystemExit(py(*cmd))

    if args.cmd == "validate":
        raise SystemExit(py("kojo_validate_translations.py", "--translations", str(args.translations)))

    if args.cmd == "apply":
        cmd = ["kojo_apply_translations.py", "--translations", str(args.translations)]
        if args.repo:
            cmd += ["--repo", str(args.repo)]
        raise SystemExit(py(*cmd))


if __name__ == "__main__":
    main()
