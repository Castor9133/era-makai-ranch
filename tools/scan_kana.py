#!/usr/bin/env python3
"""
扫描口上文件中的日文假名残留并输出统计。
保留中文部分，只标记需要翻译的日文片段。
"""

import os
import re
import sys

# 修复终端编码
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

BASE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                    "ERB", "○口上", "汎用口上")

files = sorted(f for f in os.listdir(BASE)
               if f.endswith((".ERB", ".txt")) and not f.endswith(".bak"))

total_files = 0
total_lines = 0

# 日文假名（不含中文常用字和标点）
KANA_RE = re.compile(r'[\u3040-\u309F\u30A0-\u30FF]')
# 中日混杂行：含有日文假名 + 中文
CN_RE = re.compile(r'[\u4e00-\u9fff]')

print(f"{'文件':40s} {'日文行数':>8s} {'混杂行':>8s} {'样本'}")
print("=" * 100)

for fname in files:
    fpath = os.path.join(BASE, fname)
    with open(fpath, "r", encoding="utf-8-sig") as f:
        lines = f.readlines()

    kana_lines = 0
    mixed_lines = 0
    samples = []

    for i, line in enumerate(lines):
        # 只关注 MESSAGE_BOX 行
        if 'MESSAGE_BOX' not in line:
            continue

        # 提取引号内内容
        m = re.search(r'@"(.+?)"\)', line)
        if not m:
            continue
        content = m.group(1)

        if KANA_RE.search(content):
            kana_lines += 1
            has_cn = bool(CN_RE.search(content))
            if has_cn:
                mixed_lines += 1

            if len(samples) < 2:
                snippet = content.strip()[:60]
                flag = " [中日混杂]" if has_cn else " [纯日文]"
                samples.append(f"  L{i+1}: {snippet}{flag}")

    if kana_lines > 0:
        total_files += 1
        total_lines += kana_lines
        print(f"{fname:40s} {kana_lines:>8d} {mixed_lines:>8d}")
        for s in samples:
            print(s)

print("=" * 100)
print(f"总计: {total_files} 个文件, {total_lines} 行日文残留")
