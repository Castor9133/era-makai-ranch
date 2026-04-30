#!/usr/bin/env python3
"""Rename 叫早 → 早安咬 across entire project."""

import os

BASE = r"C:\Cursor local\era-makai-ranch"

def main():
    exts = ('.ERB', '.ERH', '.CSV', '.md', '.txt', '.json')
    all_files = []
    for root, dirs, files in os.walk(BASE):
        if '.git' in root.split(os.sep):
            continue
        for f in files:
            if f.endswith(exts):
                all_files.append(os.path.join(root, f))

    print("=== Scanning %d files ===" % len(all_files))

    changes = {}
    for filepath in sorted(all_files):
        try:
            with open(filepath, 'r', encoding='utf-8') as fh:
                content = fh.read()
        except:
            continue

        if '叫早' not in content:
            continue

        new_content = content.replace('叫早', '早安咬')
        with open(filepath, 'w', encoding='utf-8') as fh:
            fh.write(new_content)

        count = content.count('叫早')
        changes[filepath] = count
        rel = os.path.relpath(filepath, BASE)
        print("  %3d  %s" % (count, rel))

    # Rename the main dispatch file
    old_name = os.path.join(BASE, "ERB", "○MAIN_PHAZE", "●叫早.ERB")
    new_name = os.path.join(BASE, "ERB", "○MAIN_PHAZE", "●早安咬.ERB")
    if os.path.exists(old_name):
        os.rename(old_name, new_name)
        print("\nRenamed: ●叫早.ERB → ●早安咬.ERB")
    elif os.path.exists(new_name):
        print("\nFile already renamed: ●早安咬.ERB")
    else:
        print("\nWARNING: Neither old nor new file found")

    print("\n=== Done: %d files, %d replacements ===" % (len(changes), sum(changes.values())))

if __name__ == "__main__":
    main()
