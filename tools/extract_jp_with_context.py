#!/usr/bin/env python3
"""
提取所有口上文件中 MESSAGE_BOX 内的日文假名，附带上文（场景/条件分支）。
输出 JSONL，每行包含：
  - file: 文件名
  - line: 行号
  - jp_text: 日文原文(引号内)
  - context: 上文(CASE/IF/ELSEIF 等，最近3层)
  - full_line: 完整行内容（定位用）
"""
import os, re, sys, json
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ROOT = r"C:\Cursor local\era-makai-ranch\ERB\○口上\汎用口上"
KANA = re.compile(r'[\u3041-\u3096\u30A1-\u30FA]')

def extract_context(lines, current_idx, depth=3):
    """向上提取最近 depth 层的 SELECTCASE/CASE/IF/ELSEIF 分支上下文"""
    ctx = []
    for i in range(current_idx - 1, max(current_idx - 30, -1), -1):
        if i < 0:
            break
        line = lines[i].strip()
        if line.startswith(('CASE ', 'CASE"', "CASE '")):
            ctx.append(line)
            if len(ctx) >= depth:
                break
        elif line.startswith(('SELECTCASE', 'IF ', 'ELSEIF ', 'ELSE', 'ENDIF', 'ENDSELECT')):
            ctx.append(line)
            if len(ctx) >= depth:
                break
    ctx.reverse()
    return ' | '.join(ctx) if ctx else '(无分支)'

def main():
    files = sorted(f for f in os.listdir(ROOT) if f.endswith(('.ERB','.txt')) and not f.endswith('.bak'))
    entries = []

    for fname in files:
        fpath = os.path.join(ROOT, fname)
        with open(fpath, 'r', encoding='utf-8-sig') as f:
            lines = f.readlines()

        for i, line in enumerate(lines, 1):
            if 'MESSAGE_BOX' not in line or '@"' not in line:
                continue
            idx = line.find('@"')
            rest = line[idx+2:]
            lq = rest.rfind('"')
            if lq < 0:
                continue
            inner = rest[:lq]
            if not KANA.search(inner):
                continue
            # 去掉纯っ/ッ/ー/～/♥ 类的才计为需要翻译
            cleaned = re.sub(r'[っッ～♥\u0300-\u036f]', '', inner)
            cleaned = re.sub(r'[ー]', '', cleaned)
            if not KANA.search(cleaned):
                continue

            context = extract_context(lines, i-1)
            entries.append({
                "file": fname,
                "line": i,
                "jp_text": inner.strip(),
                "context": context,
                "full_line": line.rstrip()
            })

    out_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                            "tools", "_translations_to_do.jsonl")
    with open(out_path, 'w', encoding='utf-8') as f:
        for e in entries:
            f.write(json.dumps(e, ensure_ascii=False) + '\n')

    # 汇总
    by_file = {}
    for e in entries:
        by_file.setdefault(e['file'], 0)
        by_file[e['file']] += 1

    print(f"提取完成！共 {len(entries)} 条日文行，输出到 {out_path}")
    print(f"\n按文件分布：")
    for fname, count in sorted(by_file.items(), key=lambda x: -x[1]):
        print(f"  {fname}: {count} 行")

if __name__ == "__main__":
    main()
