#!/usr/bin/env python3
"""
批量翻译 □上文件中的日文 MESSAGE_BOX 内容为中文。

读取 data/translations.jsonl 中的翻译条目，应用到对应的 ERB 文件。
每一条目格式: {"file": "相对路径", "line": 行号, "source": "日文原文", "target": "中文译文"}
"""

import json
import os
import re
import sys

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TRANSLATIONS_FILE = os.path.join(os.path.dirname(__file__), "translations.jsonl")

if not os.path.exists(TRANSLATIONS_FILE):
    print(f"[ERROR] 翻译条目文件不存在: {TRANSLATIONS_FILE}")
    sys.exit(1)

# 读取所有翻译条目
entries = []
with open(TRANSLATIONS_FILE, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line:
            entries.append(json.loads(line))

print(f"[INFO] 读取到 {len(entries)} 条翻译条目")

# 按文件分组
by_file = {}
for entry in entries:
    fpath = entry["file"]
    by_file.setdefault(fpath, []).append(entry)

total_replaced = 0
total_files = 0
failed_lines = []

for fpath, fentries in by_file.items():
    abspath = os.path.join(PROJECT_ROOT, fpath)
    if not os.path.exists(abspath):
        print(f"[WARN] 文件不存在: {abspath}")
        continue

    with open(abspath, "r", encoding="utf-8-sig") as f:
        lines = f.readlines()

    file_replaced = 0
    file_fail = 0

    for entry in fentries:
        lineno = entry["line"]
        source = entry["source"]
        target = entry["target"]

        if lineno > len(lines):
            failed_lines.append(f"{fpath}:{lineno} — 行号超出范围 (文件共{len(lines)}行)")
            file_fail += 1
            continue

        line = lines[lineno - 1]  # 0-based

        # 安全替换：只替换 MESSAGE_BOX 引号内的精确 source
        # 构造正则：(CALL MESSAGE_BOX,@"...) 中的 source 部分
        pattern = re.escape(source)
        if re.search(pattern, line):
            newline = line.replace(source, target, 1)
            if newline != line:
                lines[lineno - 1] = newline
                file_replaced += 1
            else:
                failed_lines.append(f"{fpath}:{lineno} — 替换失败（source匹配但replace无变化）")
                file_fail += 1
        else:
            failed_lines.append(f"{fpath}:{lineno} — 未找到原文:\n    {source.strip()}")
            file_fail += 1

    if file_replaced > 0 or file_fail > 0:
        with open(abspath, "w", encoding="utf-8") as f:
            f.writelines(lines)
        total_files += 1
        print(f"[OK] {fpath}: 替换 {file_replaced} 处, 失败 {file_fail} 处")
    else:
        print(f"[--] {fpath}: 无改动")

    total_replaced += file_replaced

print(f"\n{'='*50}")
print(f"完成！涉及 {total_files} 个文件")
print(f"成功替换: {total_replaced} 处")

if failed_lines:
    print(f"失败: {len(failed_lines)} 处")
    print("\n失败详情（前20条）:")
    for fl in failed_lines[:20]:
        print(f"  {fl}")
    if len(failed_lines) > 20:
        print(f"  ... 还有 {len(failed_lines) - 20} 条")
else:
    print("全部成功，无失败！")
