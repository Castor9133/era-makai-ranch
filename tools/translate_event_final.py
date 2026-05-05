#!/usr/bin/env python3
"""Final batch: translate remaining lines in event ERB - non-raw strings with \\n"""
import sys
sys.stdout = open(1, 'w', encoding='utf-8', closefd=False)

FPATH = r"C:\Cursor local\era-makai-ranch\ERB\○口上\汎用口上\慇懃口上1_イベント・魔界入り.ERB"

# Non-raw strings: \\n = literal backslash+n (as in ERB source files)
# 　= U+3000 ideographic space, pasted directly
R = {
    # L637
    'CALL MESSAGE_BOX,@"「んっ！ んんっ！……」\\n（痛……！？\u3000可是……被撑开的同时……深处……发酥……♥）"':
    'CALL MESSAGE_BOX,@"「嗯っ！ 嗯嗯っ！……」\\n（痛……！？\u3000可是……被撑开的同时……深处……发酥……♥）"',

    # L639
    'CALL MESSAGE_BOX,@"「んっ！ んんっ！ 嗯嗯~~……」\\n（触手进入%ANAL_CALL()%时……还是有些害怕……）"':
    'CALL MESSAGE_BOX,@"「嗯っ！ 嗯嗯っ！ 嗯嗯~~……」\\n（触手进入%ANAL_CALL()%时……还是有些害怕……）"',

    # L643
    'CALL MESSAGE_BOX,@"「んん～～♥…んむぅ♥……」\\n（痛……！？\u3000可是……%ANAL_CALL()%……像有自己的想法……♥）"':
    'CALL MESSAGE_BOX,@"「嗯嗯～～♥…嗯呜♥……」\\n（痛……！？\u3000可是……%ANAL_CALL()%……像有自己的想法……♥）"',

    # L645
    'CALL MESSAGE_BOX,@"「んん～～♥♥ んむぅ♥ 嗯呼…♥♥」\\n（请尽情玩弄%SELF_CALL()%的%ANAL_CALL()%吧♥♥）"':
    'CALL MESSAGE_BOX,@"「嗯嗯～～♥♥ 嗯呜♥ 嗯呼…♥♥」\\n（请尽情玩弄%SELF_CALL()%的%ANAL_CALL()%吧♥♥）"',

    # L650
    'CALL MESSAGE_BOX,@"「んっ！ んんっ！……」\\n（那边……不行……！？\u3000痛……！？\u3000可是……深处……好奇怪……）"':
    'CALL MESSAGE_BOX,@"「嗯っ！ 嗯嗯っ！……」\\n（那边……不行……！？\u3000痛……！？\u3000可是……深处……好奇怪……）"',

    # L652
    'CALL MESSAGE_BOX,@"「んっ！ んんっ！ ……嗯咕~~！！」\\n（那、那里不对…… っ～～～！）"':
    'CALL MESSAGE_BOX,@"「嗯っ！ 嗯嗯っ！ ……嗯咕~~！！」\\n（那、那里不对…… 唔～～～！）"',

    # L662
    'CALL MESSAGE_BOX,@"「んぐぅっ！？♥……ぐふっ♥……」\\n（还火辣辣地疼……可是……深处……像被点燃……忍不住想夹紧……♥）"':
    'CALL MESSAGE_BOX,@"「嗯咕っ！？♥……咕呼っ♥……」\\n（还火辣辣地疼……可是……深处……像被点燃……忍不住想夹紧……♥）"',

    # L665
    'CALL MESSAGE_BOX,@"「んぐぅっ！？♥♥……ぐふっ♥……んむぅぅ♥♥♥」\\n（ひ、一突きで…♥ %ANAL_CALL()%已经屈服于%PENIS_CALL()%了…♥♥）"':
    'CALL MESSAGE_BOX,@"「嗯咕っ！？♥♥……咕呼っ♥……嗯呜呜♥♥♥」\\n（一、一击就…♥ %ANAL_CALL()%已经屈服于%PENIS_CALL()%了…♥♥）"',

    # L669
    'CALL MESSAGE_BOX,@"「んぐぅっ！？♥……ぐふっ♥……」\\n（痛……又……深处……好麻……像会上瘾……♥）"':
    'CALL MESSAGE_BOX,@"「嗯咕っ！？♥……咕呼っ♥……」\\n（痛……又……深处……好麻……像会上瘾……♥）"',

    # L671
    'CALL MESSAGE_BOX,@"「んぐぅっ！？♥♥……ぐふっ♥……んむぅぅ♥♥♥」\\n（お、おぉ…っ♥ 肚子被撑开了……♥）"':
    'CALL MESSAGE_BOX,@"「嗯咕っ！？♥♥……咕呼っ♥……嗯呜呜♥♥♥」\\n（哦、哦哦…っ♥ 肚子被撑开了……♥）"',

    # L685
    'CALL MESSAGE_BOX,@"「ふぐぅ…っ！……」\\n（痛……！？\u3000可是……肠子里……像有火在爬……）"':
    'CALL MESSAGE_BOX,@"「呼咕…っ！……」\\n（痛……！？\u3000可是……肠子里……像有火在爬……）"',

    # L687
    'CALL MESSAGE_BOX,@"「ふぐぅ…っ！……うぅ…ぐっ……」\\n（竟然这样强行使用%ANAL_CALL()%……）"':
    'CALL MESSAGE_BOX,@"「呼咕…っ！……呜…咕っ……」\\n（竟然这样强行使用%ANAL_CALL()%……）"',

    # L695
    'CALL MESSAGE_BOX,@"「んん♥…ん♥…むふー♥…んふ♥」\\n（はぁ♥ %MASTER_CALL()%的%PENIS_CALL()%♥♥ 好烫…♥♥）"':
    'CALL MESSAGE_BOX,@"「嗯嗯♥…嗯♥…呜呼——♥…嗯呼♥」\\n（哈啊♥ %MASTER_CALL()%的%PENIS_CALL()%♥♥ 好烫…♥♥）"',

    # L736
    'CALL MESSAGE_BOX,@"「ぐっ♥…んぐ♥……ぉぐ♥……」\\n（啊啊♥ %SELF_CALL()%能好好地用喉咙夹紧%PENIS_CALL()%吗……♥）"':
    'CALL MESSAGE_BOX,@"「咕っ♥…嗯咕♥……哦咕♥……」\\n（啊啊♥ %SELF_CALL()%能好好地用喉咙夹紧%PENIS_CALL()%吗……♥）"',

    # L744
    'CALL MESSAGE_BOX,@"「んぐぅっ！ ……～～～～っ！」\\n（啊…啊……%SELF_CALL()%还没接过吻，就……被迫含住了……啊……啊……啊……）"':
    'CALL MESSAGE_BOX,@"「嗯咕っ！ ……～～～～っ！」\\n（啊…啊……%SELF_CALL()%还没接过吻，就……被迫含住了……啊……啊……啊……）"',

    # L746
    'CALL MESSAGE_BOX,@"「ぉごっ！…がほっ……んぐぅ…っ」\\n（好、好痛苦……っ！ 喉咙被堵住了，无法呼吸……っ！）"':
    'CALL MESSAGE_BOX,@"「哦咯っ！…嘎咳っ……嗯咕…っ」\\n（好、好痛苦……っ！ 喉咙被堵住了，无法呼吸……っ！）"',
}

def main():
    with open(FPATH, 'r', encoding='utf-8') as f:
        content = f.read()

    total = 0
    not_found = []
    for old, new in R.items():
        if old in content:
            content = content.replace(old, new)
            total += 1
            print(f"  ✅ L{list(R.keys()).index(old)+1}")
        else:
            not_found.append(old[:60])

    with open(FPATH, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"\n替换: {total}/{len(R)}")
    for nf in not_found:
        print(f"  ⚠️  {nf}")

if __name__ == "__main__":
    main()
