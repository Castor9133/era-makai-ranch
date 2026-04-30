#!/usr/bin/env python3
"""
Batch-replace Japanese onomatopoeia/moans in personality files.
Mechanical replacements that don't depend on personality context.
"""

import os, glob, re

BASE = r"C:\Cursor local\era-makai-ranch\ERB\○口上\汎用口上"

# Replacement map: Japanese moan → Chinese equivalent
# Ordered from longest to shortest to avoid partial matches
REPLACEMENTS = [
    # イぎゅ family → 嗯呜
    ("イぎゅう゛ぅぅぅぅ", "嗯呜呜呜呜"),
    ("イぎゅイぎゅイぎゅイぎゅ", "嗯呜嗯呜嗯呜嗯呜"),
    ("イぎゅイぎゅ", "嗯呜嗯呜"),
    ("イぎゅぅっ", "嗯呜呜"),
    ("イぎゅっ", "嗯呜"),

    # んぉおお family → 唔哦哦
    ("んぉおおオ゛", "唔哦哦哦"),
    ("んぉおお", "唔哦哦"),

    # お゛ family → 啊呜
    ("お゛っ♥♥", "啊呜♥♥"),
    ("お゛っ♥", "啊呜♥"),
    ("お゛っ", "啊呜"),

    # ふぅぅ → 呼呼
    ("ふぅぅっ", "呼呼"),

    # ひぅっ → 咿唔
    ("ひぅっ♥♥", "咿唔♥♥"),
    ("ひぅっ", "咿唔"),

    # ほっ/ほあっ → 哈啊
    ("ほあっ", "哈啊"),
    ("ほっ", "哈"),

    # んんっ → 嗯嗯
    ("んんっ…", "嗯嗯……"),
    ("んんっ", "嗯嗯"),

    # ああっ → 啊啊
    ("ああっ…♥", "啊啊……♥"),
    ("ああっ", "啊啊"),

    # あーっ → 啊—！
    ("あーっ♥", "啊—！♥"),
    ("あーっ", "啊—！"),

    # んっ → 嗯
    ("んっ…", "嗯……"),
    ("んっ♥", "嗯♥"),
    ("んっ", "嗯"),

    # ぉおお → 哦哦
    ("ぉおおオ゛", "哦哦哦"),
    ("ぉおお", "哦哦"),
]

def get_main_files():
    """Get all main personality and schedule files."""
    files = glob.glob(os.path.join(BASE, '*口上*.ERB'))
    targets = []
    for f in files:
        basename = os.path.basename(f)
        if '_調教コマンド' in basename or '_イベント' in basename or 'V体位' in basename:
            continue
        targets.append(f)
    return targets

def count_japanese(text):
    """Count characters in Japanese kana range."""
    return sum(1 for c in text if '\u3040' <= c <= '\u30ff')

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_jp = count_japanese(content)
    if original_jp == 0:
        return None

    # Apply replacements
    new_content = content
    replacements_done = 0
    for old, new in REPLACEMENTS:
        count = new_content.count(old)
        if count > 0:
            new_content = new_content.replace(old, new)
            replacements_done += count

    new_jp = count_japanese(new_content)
    removed = original_jp - new_jp

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

    return {
        'file': os.path.basename(filepath),
        'jp_before': original_jp,
        'jp_after': new_jp,
        'removed': removed,
        'replacements': replacements_done,
    }

def main():
    files = get_main_files()
    results = []

    for filepath in sorted(files):
        result = process_file(filepath)
        if result:
            results.append(result)

    print("File                               JP_before  JP_after  Removed  Replacements")
    print("-" * 75)
    total_before = 0
    total_after = 0
    total_repl = 0
    for r in sorted(results, key=lambda x: -x['removed']):
        print("%-35s %5d     %5d     %5d     %5d" % (
            r['file'][:35], r['jp_before'], r['jp_after'], r['removed'], r['replacements']))
        total_before += r['jp_before']
        total_after += r['jp_after']
        total_repl += r['replacements']

    print("-" * 75)
    print("%-35s %5d     %5d     %5d     %5d" % (
        'TOTAL', total_before, total_after, total_before - total_after, total_repl))

    print("\nRemaining JP chars after mechanized pass: %d" % total_after)
    print("These require manual translation (mixed sentences, etc.)")

if __name__ == "__main__":
    main()
