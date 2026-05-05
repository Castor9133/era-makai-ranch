#!/usr/bin/env python3
"""
Patch remaining kana in small files (生真面目, 無口ERB, 無口txt, 非敬語幼め).
Dictionary-based replacement for simple kana → Chinese.
"""
import os, sys, re
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BASE = r"C:\Cursor local\era-makai-ranch\ERB\○口上\汎用口上"

FILES = [
    "生真面目口上1.ERB",
    "無口口上1.ERB",
    "無口口上1.txt",
    "非敬語幼め口上1.ERB",
]

REPLACEMENTS = [
    # 無口/非敬語幼め common moans
    ("おっ♥", "哦♥"),
    ("おっ", "哦"),
    ("はぅぅ", "哈呜"),
    ("くぅっ♥", "咕呜♥"),
    ("くぅっ", "咕呜"),
    ("あぁ…♥", "啊啊……♥"),
    ("あ…っ♥", "啊…っ♥"),
    ("ん…♥", "嗯……♥"),
    ("はひぃっ♥", "哈咿♥"),
    ("はひぃっ", "哈咿"),
    ("あひぃ…♥♥", "啊咿……♥♥"),
    ("あひぃ…♥", "啊咿……♥"),
    ("ひぃ♥♥", "咿♥♥"),
    ("ひぃ♥", "咿♥"),
    ("ひぃ", "咿"),
    ("ひいっ！？", "咿——！？"),
    ("ひいっ", "咿——"),
    ("ひっ…", "咿……"),
    ("ひっ！？", "咿！？"),
    ("あっ♥♥", "啊♥♥"),
    ("はぁっ…♥", "哈啊……♥"),
    ("はぁっ♥", "哈啊♥"),
    ("あ♥♥♥", "啊♥♥♥"),
    ("あ♥♥", "啊♥♥"),
    ("触手にぃ♥", "触手啊♥"),
    ("嗯ひぃ♥♥", "嗯咿♥♥"),
    ("しぼられてるっ", "被吸得"),
]

def count_kana(text):
    return sum(1 for c in text if '\u3040' <= c <= '\u30ff')

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_kana = count_kana(content)
    if original_kana == 0:
        return None

    new_content = content
    total_repl = 0
    for old, new in REPLACEMENTS:
        cnt = new_content.count(old)
        if cnt > 0:
            new_content = new_content.replace(old, new)
            total_repl += cnt

    new_kana = count_kana(new_content)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

    return {
        'file': os.path.basename(filepath),
        'kana_before': original_kana,
        'kana_after': new_kana,
        'removed': original_kana - new_kana,
        'replacements': total_repl,
    }

def main():
    results = []
    for fname in FILES:
        fpath = os.path.join(BASE, fname)
        if not os.path.exists(fpath):
            print(f"MISSING: {fname}")
            continue
        result = process_file(fpath)
        if result:
            results.append(result)
            print(f"{result['file'][:30]:30s} kana: {result['kana_before']:4d} → {result['kana_after']:4d}  (-{result['removed']:3d}, {result['replacements']:3d} replacements)")
        else:
            print(f"{fname[:30]:30s} already clean")

    total_b = sum(r['kana_before'] for r in results)
    total_a = sum(r['kana_after'] for r in results)
    print(f"\nTotal: {total_b} → {total_a} kana chars remaining")

if __name__ == "__main__":
    main()
