#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Focused extraction: SM/training/abuse content from 7 novels.
Expanded keyword set for 调教虐待SM.
"""
import sys, pathlib, re
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

SRC = pathlib.Path(r'C:\Users\范振宁\Downloads\txt')
OUT = pathlib.Path(r'C:\Cursor local\era-makai-ranch\docs\novel_extracts')
OUT.mkdir(parents=True, exist_ok=True)

FILES = [
    '【精校】《清军大营中的女犯》（全本）作者：曾九副本.txt',
    '【长篇】A级乳牛最终章-最后的激情副本.txt',
    '【精校】异世界魔物娘收容 作者：kof_boss副本.txt',
    '【长篇】在充满魔物娘的大陆上的生存法则副本.txt',
    '【长篇】田岫和他的奴隶们副本.txt',
    '【长篇】《渔港春夜（真血亲修改加料）》_soushu555_net_搜书吧网址副本.txt',
    '【长篇】《完全摧花手册之地狱天使》.TXT',
]

# SM/调教/虐待 定向关键词（大幅扩充）
THEMES = [
    ('SM_调教_命令服从', [
        '跪下', '趴下', '张开腿', '命令你', '不准动', '不许',
        '规矩', '惩罚', '管教', '调教', '训诫', '训练', '驯服',
        '服从', '听话', '乖', '学乖', '教教你',
    ]),
    ('SM_羞辱_贬低', [
        '母狗', '骚货', '贱货', '婊子', '母畜', '母猪', '母牛',
        '肉便器', '性奴', '奴隶', '贱奴', '贱婢', '狗奴',
        '奶牛', '肉玩具', '公共', '公用',
    ]),
    ('SM_体罚_鞭打', [
        '鞭', '鞭打', '鞭笞', '抽打', '抽', '皮鞭',
        '打屁股', '掌掴', '打耳光', '罚跪', '杖',
        '杀威棒', '棒子', '藤条', '戒尺',
    ]),
    ('SM_拘束_捆绑', [
        '绑', '捆绑', '绑住', '捆', '捆住', '束缚', '拘束',
        '手铐', '脚镣', '铁链', '锁链', '绳索', '绳子',
        '固定', '大字', '悬吊', '吊起', '绑在',
    ]),
    ('SM_道具_器具', [
        '项圈', '口塞', '口球', '肛塞', '尾塞', '乳夹',
        '跳蛋', '假阳具', '按摩棒', '震动棒', '拉珠',
        '贞操带', '尿道', '扩张器', '振动',
    ]),
    ('SM_强制_暴力侵入', [
        '按住', '按倒', '压住', '压制', '制服',
        '强迫', '强行', '强制', '硬塞', '捅入',
        '撕裂', '撑开', '拉开', '扒开',
    ]),
    ('SM_痛苦_身体反应', [
        '惨叫', '哭喊', '求饶', '哀嚎', '呻吟', '闷哼',
        '痉挛', '抽搐', '颤抖', '发抖', '僵硬',
        '流泪', '哭泣', '哭', '眼泪', '泪水',
    ]),
    ('SM_心理_崩溃', [
        '绝望', '崩溃', '麻木', '放弃', '认命',
        '眼神空洞', '失神', '呆滞', '机械地',
        '羞辱', '屈辱', '羞耻',
    ]),
    ('SM_标记_烙印', [
        '烙印', '刻字', '刺青', '编号', '刻印',
        '标记', '毁容', '烫伤', '烧伤',
    ]),
    ('SM_放置_冷落', [
        '关', '关禁闭', '关起来', '锁起来', '锁住',
        '关进', '关在', '关押', '囚禁',
    ]),
    ('SM_精液_体液控制', [
        '灌精', '内射', '中出', '吞精', '饮精',
        '颜射', '口爆', '射在', '精液', '白浊',
    ]),
    ('SM_调教_言语洗脑', [
        '你是谁', '你是谁的东西', '属于谁',
        '说你是', '承认', '记住', '回答我',
        '知错', '以后还敢', '是什么',
    ]),
]

def read_file(filepath):
    raw = filepath.read_bytes()
    for enc in ['utf-8', 'utf-16-le', 'gbk', 'gb18030']:
        try:
            return raw.decode(enc)
        except:
            continue
    return None

def extract(text, themes, context=80):
    kw_to_theme = {}
    all_kws = []
    for theme, kws in themes:
        for kw in kws:
            if kw not in kw_to_theme:
                kw_to_theme[kw] = []
            kw_to_theme[kw].append(theme)
            all_kws.append(kw)
    all_kws.sort(key=len, reverse=True)
    pattern = '|'.join(re.escape(kw) for kw in all_kws)
    regex = re.compile(pattern)

    results = {t: [] for t, _ in themes}
    seen = set()

    for m in regex.finditer(text):
        kw = m.group()
        idx = m.start()
        start = max(0, idx - context)
        end = min(len(text), idx + len(kw) + context)

        for sep in '\n。！？':
            p = text.rfind(sep, start, idx)
            if p >= 0:
                start = p + 1
                break
        for sep in '\n。！？':
            p = text.find(sep, end)
            if p >= 0 and p - end < 300:
                end = p + 1
                break

        passage = text[start:end].strip()
        if len(passage) < 25:
            continue

        for theme in kw_to_theme.get(kw, ['其他']):
            key = (theme, passage[:100])
            if len(results[theme]) >= 80 or key in seen:
                continue
            seen.add(key)
            results[theme].append(passage)
    return results

all_results = []
summary = []

for fname in FILES:
    f = SRC / fname
    if not f.exists():
        print(f'  {fname} — NOT FOUND')
        continue
    print(f'  {fname}...', end=' ', flush=True)
    text = read_file(f)
    if text is None:
        print('ENCODING FAIL')
        continue
    lines = len(text.splitlines())
    fsize = len(text)
    results = extract(text, THEMES, context=80)
    total = sum(len(v) for v in results.values())
    print(f'{total} passages ({fsize//1024}KB, {lines}行)')
    all_results.append((fname, fsize, lines, results))
    summary.append((fname, fsize, lines, total))

# Write report
opath = OUT / 'sm_extracts.md'
with open(opath, 'w', encoding='utf-8') as f:
    f.write('# SM/调教/虐待 精华提取 — 7篇重点小说\n\n')
    f.write(f'提取自 {len(all_results)} 篇，共 {len(THEMES)} 个SM专项主题，上下文窗口80字。\n\n')
    f.write('> 注意：原文某些字可能被替换，如"性"→"铯""色"，"操"→"C""c"等，提取时保留了原文写法。\n\n')
    f.write('---\n\n')

    for theme, _ in THEMES:
        f.write(f'\n## {theme}\n\n')
        for fname, fsize, flines, results in all_results:
            passages = results.get(theme, [])
            if not passages:
                continue
            short = fname.replace('【精校】', '').replace('【长篇】', '').replace('副本', '').replace('（全本）', '').replace('作者：曾九', '').replace('作者：kof_boss', '').strip()
            short = short[:40]
            f.write(f'### ▶ {short} ({len(passages)}条)\n\n')
            for p in passages:
                clean = p.replace('\r', '')
                if len(clean) > 600:
                    clean = clean[:600] + '…'
                f.write(f'> {clean}\n\n')
            f.write('---\n\n')

print(f'\nWritten: {opath}')

# Summary
print(f'\n{"="*60}')
print(f'SM EXTRACTION SUMMARY:')
print(f'{"="*60}')
for fname, fsize, flines, npass in sorted(summary, key=lambda x: -x[3]):
    short = fname[:50]
    print(f'{short:50s} {fsize//1024:4d}KB {npass:4d}个')
print(f'{"="*60}')
