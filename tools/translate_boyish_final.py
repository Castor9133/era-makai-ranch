#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ボーイッシュ口上1_調教コマンド.ERB 完整翻译脚本。
从 boyish_translations.json 读取翻译数据并应用。
"""
import sys, pathlib, json
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ROOT = pathlib.Path(r'C:\Cursor local\era-makai-ranch')
FNAME = 'ボーイッシュ口上1_調教コマンド.ERB'
FPATH = ROOT / 'ERB' / '○口上' / '汎用口上' / FNAME
TJSON = pathlib.Path(__file__).parent / 'boyish_translations.json'

def apply():
    text = FPATH.read_text(encoding='utf-8-sig')
    data = json.loads(TJSON.read_text(encoding='utf-8'))
    count = 0
    missed = []
    for item in data:
        source = item['source']
        target = item['target']
        old_str = f'CALL MESSAGE_BOX,@\"{source}\"'
        new_str = f'CALL MESSAGE_BOX,@\"{target}\"'
        if old_str not in text:
            missed.append(source[:60])
            continue
        n = text.count(old_str)
        text = text.replace(old_str, new_str)
        count += n

    FPATH.write_text(text, encoding='utf-8')
    print(f'OK: {count} replacements')
    if missed:
        print(f'MISSED ({len(missed)}):')
        for m in missed[:15]:
            print(f'  {m}')

if __name__ == '__main__':
    apply()
