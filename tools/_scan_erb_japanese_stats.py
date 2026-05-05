# -*- coding: utf-8 -*-
"""One-off scan: count ERB files with kana / MESSAGE_BOX kana lines."""
import pathlib
import re
import sys

def main() -> int:
    root = pathlib.Path(__file__).resolve().parents[1] / "ERB"
    if not root.is_dir():
        print("ERB not found", root, file=sys.stderr)
        return 1
    kana_re = re.compile(r"[\u3041-\u3096\u30a1-\u30fa\u30fc]")
    msg_re = re.compile(r"CALL\s+MESSAGE_BOX", re.I)
    # Emuera: PRINTFORMW / PRINTFORML / PRINTW …
    print_re = re.compile(
        r"\bPRINT(FORMW|FORML|FORM|W|L|V|PLAIN)\b",
        re.I,
    )
    # Windows 路径大小写/双 glob 会去重，避免同一文件计两次
    files = []
    seen: set[pathlib.Path] = set()
    for f in root.rglob("*"):
        if not f.is_file() or f.suffix.lower() != ".erb":
            continue
        key = f.resolve()
        if key in seen:
            continue
        seen.add(key)
        files.append(f)
    files.sort(key=lambda p: str(p).lower())
    rows_kana: list[tuple[int, pathlib.Path]] = []
    rows_msg: list[tuple[int, int, pathlib.Path]] = []
    rows_print: list[tuple[int, int, pathlib.Path]] = []

    for f in files:
        try:
            t = f.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        nk = len(kana_re.findall(t))
        msg_hits = 0
        print_hits = 0
        for line in t.splitlines():
            if msg_re.search(line) and kana_re.search(line):
                msg_hits += 1
            if print_re.search(line) and kana_re.search(line):
                print_hits += 1
        rel = f.relative_to(root)
        rows_kana.append((nk, rel))
        if msg_hits:
            rows_msg.append((msg_hits, nk, rel))
        if print_hits:
            rows_print.append((print_hits, nk, rel))

    thresholds = [1, 20, 50, 100, 200, 500, 1000]
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    print("=== ERB kana chars (per file) ===")
    print("total_files:", len(files))
    for th in thresholds:
        c = sum(1 for nk, _ in rows_kana if nk >= th)
        print(f"  kana_count >= {th:4d}: {c} files")

    print()
    print("=== CALL MESSAGE_BOX lines still containing kana ===")
    print("files_with_msg_kana:", len(rows_msg))
    rows_msg.sort(key=lambda x: (-x[0], -x[1], str(x[2])))
    print("top 30 (msg_lines_kana, total_kana, path):")
    for a, b, c in rows_msg[:30]:
        print(f"  {a:4d}  {b:6d}  {c}")

    uni_msg = {p for _, _, p in rows_msg}
    uni_print = {p for _, _, p in rows_print}
    union = len(uni_msg | uni_print)
    both = len(uni_msg & uni_print)
    print()
    print("=== PRINT* lines containing kana (narrative-style) ===")
    print("files_with_print_kana:", len(rows_print))
    rows_print.sort(key=lambda x: (-x[0], -x[1], str(x[2])))
    print("top 15 (print_lines_kana, total_kana, path):")
    for a, b, c in rows_print[:15]:
        print(f"  {a:4d}  {b:6d}  {c}")
    print()
    print("union(files with MSG_LINE kana OR PRINT_LINE kana):", union)
    print("intersection(both):", both)

    print()
    print("=== top 25 files by total kana ===")
    rows_kana.sort(key=lambda x: -x[0])
    for nk, p in rows_kana[:25]:
        if nk == 0:
            break
        print(f"  {nk:7d}  {p}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
