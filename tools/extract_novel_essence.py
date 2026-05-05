#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Optimized extraction of key passages from R18 novels.
Uses single-pass text scanning per file.
"""
import sys, pathlib, re
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

SRC = pathlib.Path(r'C:\Users\范振宁\Downloads\txt')
OUT = pathlib.Path(r'C:\Cursor local\era-makai-ranch\docs\novel_extracts')
OUT.mkdir(parents=True, exist_ok=True)

# Theme → keywords mapping
THEMES = [
    ('性描写_前戏', ['抚摸', '揉捏', '亲吻', '吸吮', '舔舐', '爱抚', '揉搓', '捻弄', '拨弄', '含住', '轻咬']),
    ('性描写_插入', ['插进', '插入', '进入', '挺进', '刺入', '顶入', '送入', '塞进', '抽插', '律动', '耸动', '挺动']),
    ('调教_命令', ['跪下', '趴下', '张开', '分开', '命令你', '不准动', '不许动', '规矩', '惩罚你', '责罚', '管教']),
    ('调教_羞辱', ['母狗', '骚货', '贱货', '性奴', '肉便器', '母畜', '母猪', '母牛', '奶牛', '肉玩具']),
    ('调教_标记', ['烙印', '刻字', '刺青', '项圈', '奴隶纹', '编号', '刻印', '标记']),
    ('调情_勾引', ['勾引', '诱惑', '魅惑', '挑逗', '调情', '引诱', '撩拨', '抛媚眼', '诱惑']),
    ('日常互动', ['吃饭', '洗澡', '起床', '穿衣', '散步', '做饭', '喂食', '梳头', '按摩', '拥抱', '聊天']),
    ('高潮', ['高潮', '泄了', '去了', '丢了', '绝顶', '痉挛', '抽搐', '弓起', '绷紧', '失禁', '喷出']),
    ('口交', ['口交', '深喉', '含住', '吞吐', '口活', '吹箫', '口爆', '颜射']),
    ('肛交', ['肛门', '后庭', '屁眼', '菊穴', '后穴', '肛', '直肠', '旱道', '谷道']),
    ('乳交_哺乳', ['乳交', '挤奶', '哺乳', '乳汁', '奶水', '奶子', '乳头', '乳晕', '乳夹']),
    ('捆绑_拘束', ['捆绑', '绑住', '束缚', '拘束', '绳索', '绳子', '铁链', '锁链', '镣铐']),
    ('暴力_强制', ['强制', '按住', '压制', '禁锢', '囚禁', '凌辱', '蹂躏', '侵犯', '虐待']),
    ('心理_沦陷', ['羞耻', '屈辱', '恐惧', '矛盾', '纠结', '挣扎', '沦陷', '堕落', '快感', '快乐']),
    ('狗奴_兽化', ['美女犬', '狗奴', '爬行', '狗碗', '摇尾', '汪汪', '学狗', '四肢着地']),
]

def read_file(filepath):
    raw = filepath.read_bytes()
    for enc in ['utf-8', 'utf-16-le', 'gbk', 'gb18030']:
        try:
            return raw.decode(enc)
        except:
            continue
    return None

def extract_all_in_one_pass(text, themes, context=60):
    """Single-pass: scan text once, find all keyword matches."""
    # Build a combined regex
    kw_to_theme = {}
    all_kws = []
    for theme, kws in themes:
        for kw in kws:
            if kw not in kw_to_theme:
                kw_to_theme[kw] = []
            kw_to_theme[kw].append(theme)
            all_kws.append(kw)

    # Sort keywords by length (longer first to avoid partial matches)
    all_kws.sort(key=len, reverse=True)
    # Escape for regex
    pattern = '|'.join(re.escape(kw) for kw in all_kws)
    regex = re.compile(pattern)

    results = {t: [] for t, _ in themes}

    for m in regex.finditer(text):
        kw = m.group()
        idx = m.start()
        start = max(0, idx - context)
        end = min(len(text), idx + len(kw) + context)

        # Extend to sentence boundaries
        for sep in '\n。！？':
            p = text.rfind(sep, start, idx)
            if p >= 0:
                start = p + 1
                break
        for sep in '\n。！？':
            p = text.find(sep, end)
            if p >= 0 and p - end < 200:
                end = p + 1
                break

        passage = text[start:end].strip()
        if len(passage) < 20:
            continue

        # Assign to themes
        for theme in kw_to_theme.get(kw, ['其他']):
            if len(results[theme]) < 50:  # limit per theme
                if passage not in results[theme]:  # dedup
                    results[theme].append(passage)

    return results

# Process all files
all_file_results = []
summary = []

for f in sorted(SRC.glob('*.txt')):
    fname = f.name
    print(f'  {fname}...', end=' ', flush=True)
    text = read_file(f)
    if text is None:
        print('ENCODING FAIL')
        continue

    lines = text.splitlines()
    fsize = len(text)

    results = extract_all_in_one_pass(text, THEMES, context=50)

    total = sum(len(v) for v in results.values())
    print(f'{total} passages')
    all_file_results.append((fname, fsize, len(lines), results))
    summary.append((fname, fsize, len(lines), total))

# Write report
print(f'\nWriting report...')

opath = OUT / 'novel_extracts.md'
with open(opath, 'w', encoding='utf-8') as f:
    f.write('# 小说精华提取 — 写作参考\n\n')
    f.write(f'提取自 {len(all_file_results)} 篇R18小说，共15个主题分类。\n\n')
    f.write('---\n\n')

    for theme, _ in THEMES:
        f.write(f'\n## {theme}\n\n')
        for fname, fsize, flines, results in all_file_results:
            passages = results.get(theme, [])
            if passages:
                short_name = fname.replace('【精校】', '').replace('【长篇】', '').replace('副本', '').strip()
                f.write(f'### ▶ {short_name} ({len(passages)}条)\n\n')
                for p in passages[:10]:
                    clean = p.replace('\r', '')
                    if len(clean) > 400:
                        clean = clean[:400] + '…'
                    f.write(f'> {clean}\n\n')
                f.write('---\n\n')

print(f'Written: {opath}')

# Print summary
print(f'\n{"="*60}')
print(f'SUMMARY:')
print(f'{"="*60}')
print(f'{"File":45s} {"Size":8s} {"Lines":8s} {"Total":8s}')
print('-' * 69)
for fname, fsize, flines, npass in sorted(summary, key=lambda x: -x[3]):
    print(f'{fname[:43]:45s} {fsize//1024:4d}KB {flines:6d}行 {npass:4d}个')
print(f'{"="*60}')
