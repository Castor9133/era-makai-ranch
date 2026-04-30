#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Translate remaining Japanese kana in 慇懃 personality files.
Operates on exact line content matching — safe replacement.
"""

import os, sys

BASE = r"C:\Cursor local\era-makai-ranch\ERB\○口上\汎用口上"

# === Translation map: exact old_string → new_string ===
# Each entry is (old_substring, new_substring) for inline replacement
replacements = [
    # === Sound effects (kana→Chinese equivalents) ===
    ("あ゛っ", "啊"),
    ("あ゛", "啊"),
    ("あっ", "啊"),
    ("あぁ", "啊啊"),
    ("あぅ", "啊呜"),
    ("あむ", "啊呜"),
    ("あひ", "啊咿"),
    ("あ、あひ", "啊、啊咿"),
    ("お゛ーっ", "哦——"),
    ("お゛ぉぉ", "哦哦哦"),
    ("お゛ぉぉぉ", "哦哦哦哦"),
    ("お゛おぉっ", "哦哦"),
    ("お゛お゛ぉぉぉ", "哦哦哦哦"),
    ("おっ", "哦"),
    ("おぉっ", "哦哦"),
    ("おぉぉ", "哦哦哦"),
    ("おぉ", "哦哦"),
    ("おはようございます", "早上好"),
    ("はぅ", "哈呜"),
    ("はぁ", "哈啊"),
    ("はぁはぁ", "哈啊哈啊"),
    ("はひ", "哈咿"),
    ("はひッ", "哈咿"),
    ("は、はひ", "哈、哈咿"),
    ("はへ", "哈嘿"),
    ("は、はへ", "哈、哈嘿"),
    ("は、ぐっ", "哈、咕"),
    ("ふあ", "呼啊"),
    ("ふぁ", "呼啊"),
    ("ふー", "呼呼"),
    ("ふ…", "呼…"),
    ("ふ、ふひ", "呼、呼咿"),
    ("ふあぁ", "呼啊啊"),
    ("ふぅ", "呼呜"),
    ("ふぐ", "咕呜"),
    ("ふぎ", "呼咿"),
    ("んあ", "嗯啊"),
    ("んあっ", "嗯啊"),
    ("んあぁ", "嗯啊啊"),
    ("んあぁぁ", "嗯啊啊啊"),
    ("んあ゛ぁっ", "嗯啊啊"),
    ("んお", "嗯哦"),
    ("んおぉ", "嗯哦哦"),
    ("んおぉっ", "嗯哦哦"),
    ("んおぉぉ", "嗯哦哦哦"),
    ("んおぉぉぉ", "嗯哦哦哦哦"),
    ("んぐ", "嗯咕"),
    ("んぎ", "嗯咿"),
    ("んぎっ", "嗯咿"),
    ("んぎゃ", "嗯咿呀"),
    ("んぎゅ", "嗯咿呜"),
    ("んぎゅぅ", "嗯咿呜呜"),
    ("んぎぃ", "嗯咿咿"),
    ("んぎぃぃ", "嗯咿咿咿"),
    ("んぎぃぃぃ", "嗯咿咿咿咿"),
    ("んほ", "嗯嚯"),
    ("んほお", "嗯嚯哦"),
    ("んほおお", "嗯嚯哦哦"),
    ("んほおおお", "嗯嚯哦哦哦"),
    ("んほぉ", "嗯嚯哦"),
    ("んひ", "嗯咿"),
    ("んひぃ", "嗯咿咿"),
    ("んふ", "嗯呼"),
    ("んふー", "嗯呼呼"),
    ("んへ", "嗯嘿"),
    ("んや", "嗯呀"),
    ("んやぁ", "嗯呀啊"),
    ("ん～", "嗯～"),
    ("ん…", "嗯…"),
    ("ん…♥", "嗯…♥"),
    ("ん゛ーっ", "嗯——"),
    ("ひっ", "咿"),
    ("ひあ", "咿啊"),
    ("ひあぁ", "咿啊啊"),
    ("ひあぁっ", "咿啊啊"),
    ("ひあぁぁっ", "咿啊啊啊"),
    ("ひああ", "咿啊啊"),
    ("ひぐっ", "咿咕"),
    ("ひぎっ", "咿咿"),
    ("ひぎ", "咿咿"),
    ("ひぎぃ", "咿咿咿"),
    ("ひぎぃっ", "咿咿咿"),
    ("ひぎぃぃ", "咿咿咿咿"),
    ("ひぁ", "咿啊"),
    ("ひぅ", "咿呜"),
    ("ひぅぅ", "咿呜呜"),
    ("いぎぃ", "咿咿咿"),
    ("いぎぃぃ", "咿咿咿咿"),
    ("いぎぃぃぃ", "咿咿咿咿咿"),
    ("かひ", "咔嘻"),
    ("かひっ", "咔嘻"),
    ("かはっ", "咔哈"),
    ("かは", "咔哈"),
    ("ぐう", "咕呜"),
    ("ぐうぅ", "咕呜呜"),
    ("ぐぅ", "咕呜"),
    ("ぢゅる", "滋溜"),
    ("れろ", "舔舔"),
    ("ちゅ", "啾"),
    ("ちゅっ", "啾"),
    ("にゃい", "的"),
    ("にゃいぃ", "的咿"),
    ("にゃいぃぃ", "的咿咿"),
    ("たえられにゃい", "受不了的"),
    ("ぇ", "诶"),
    ("ぁ", "啊"),
    ("あ", "啊"),
    ("い", "咿"),
    ("う", "呜"),
    ("え", "诶"),
    ("お", "哦"),
    ("か", "咔"),
    ("き", "咿"),
    ("く", "咕"),
    ("け", "咿"),
    ("こ", "咕"),
    ("さ", "飒"),
    ("し", "咻"),
    ("す", "嘶"),
    ("せ", "咝"),
    ("そ", "嗦"),
    ("た", "哒"),
    ("ち", "叽"),
    ("つ", "呲"),
    ("て", "嘞"),
    ("と", "哆"),
    ("な", "呐"),
    ("に", "呢"),
    ("ぬ", "奴"),
    ("ね", "呐"),
    ("の", "喏"),
    ("は", "哈"),
    ("ひ", "咻"),
    ("ふ", "呼"),
    ("へ", "嘿"),
    ("ほ", "嚯"),
    ("ま", "嘛"),
    ("み", "咪"),
    ("む", "呣"),
    ("め", "咩"),
    ("も", "哞"),
    ("や", "呀"),
    ("ゆ", "呦"),
    ("よ", "哟"),
    ("ら", "啦"),
    ("り", "哩"),
    ("る", "噜"),
    ("れ", "叻"),
    ("ろ", "咯"),
    ("わ", "哇"),
    ("を", "哦"),
    ("ん", "嗯"),
    ("が", "嘎"),
    ("ぎ", "咿"),
    # These are typically Chinese context where kana snuck in; mark as already handled above
    ("ぐっ", "咕"),
    ("げっ", "咿"),
    ("ご", "咕"),
    ("ざ", "咂"),
    ("じ", "叽"),
    ("ず", "嗞"),
    ("ぜ", "啧"),
    ("ぜぇ", "啧啧"),
    ("ぞ", "咗"),
    ("だ", "哒"),
    ("ぢ", "叽"),
    ("づ", "嗞"),
    ("で", "嘚"),
    ("ど", "咄"),
    ("ば", "叭"),
    ("び", "咇"),
    ("ぶ", "卟"),
    ("べ", "咇"),
    ("ぼ", "啵"),
    ("ぱ", "啪"),
    ("ぴ", "噼"),
    ("ぷ", "噗"),
    ("ぺ", "啪"),
    ("ぽ", "啪"),
    ("っ", ""),       # geminate marker — remove
    ("ッ", ""),       # katakana geminate marker — remove
    ("ー", "—"),      # long vowel mark → Chinese dash
    ("゛", ""),       # voiced mark — remove
    ("゜", ""),       # semi-voiced mark — remove
    ("ゃ", "呀"),
    ("ゅ", "呦"),
    ("ょ", "哟"),
    ("ぃ", "咿"),
    ("ぅ", "呜"),
    ("ぇ", "诶"),
    ("ぉ", "哦"),
]

# === Line-level translations (full line content match required) ===
line_translations = {
    # 慇懃口上1.ERB
    'CALL MESSAGE_BOX,@"「はぅ…♥ 又喝了这么多呢……」"':
        'CALL MESSAGE_BOX,@"「哈呜…♥ 又喝了这么多呢……」"',
    'CALL MESSAGE_BOX,@"「ふぅ… 您看起来很满足呢……」"':
        'CALL MESSAGE_BOX,@"「呼呜… 您看起来很满足呢……」"',
    'CALL MESSAGE_BOX,@"「ん～♥♥ %MASTER_CALL()%的手，真棒♥♥」"':
        'CALL MESSAGE_BOX,@"「嗯～♥♥ %MASTER_CALL()%的手，真棒♥♥」"',
    'CALL MESSAGE_BOX,@"「ん…♥ 如果要抚摸的话，请温柔一点……」"':
        'CALL MESSAGE_BOX,@"「嗯…♥ 如果要抚摸的话，请温柔一点……」"',
    'CALL MESSAGE_BOX,@"「ふ…ぅぐ……嗯……」"':
        'CALL MESSAGE_BOX,@"「呼……呜咕……嗯……」"',
    'CALL MESSAGE_BOX,@"「～～～！ ……っ！ うぅっ…」"':
        'CALL MESSAGE_BOX,@"「～～～！ ……！ 呜呜…」"',
    'CALL MESSAGE_BOX,@"「ぜぇ…ぜぇ……もう…限界……」"':
        'CALL MESSAGE_BOX,@"「啧啧……啧啧……已经……极限了……」"',

    # Mixed JP/CN sentences — need manual inline replacement
    'CALL MESSAGE_BOX,@"「あ゛っ♥ あ゛っ♥ 奶子被っ♥ 被触手支配了っ♥♥ んほおおおぉぉぉ♥♥♥」"':
        'CALL MESSAGE_BOX,@"「啊♥ 啊♥ 奶子被♥ 被触手支配了♥♥ 嗯嚯哦哦哦哦哦哦♥♥♥」"',
    'CALL MESSAGE_BOX,@"「被、被彻底抓住了弱点了ぇ♥♥♥ 被当作奶水喷出的玩具了呀……♥♥♥」"':
        'CALL MESSAGE_BOX,@"「被、被彻底抓住了弱点了诶♥♥♥ 被当作奶水喷出的玩具了呀……♥♥♥」"',
    'CALL MESSAGE_BOX,@"「ひぐぅ♥ 一边交尾一边榨乳好厉害ぃぃ♥♥ 自己是家畜的事实已经深深刻在脑海里了……♥♥♥」"':
        'CALL MESSAGE_BOX,@"「咿咕呜♥ 一边交尾一边榨乳好厉害咿咿♥♥ 自己是家畜的事实已经深深刻在脑海里了……♥♥♥」"',
    'CALL MESSAGE_BOX,@"「おっ♥ おっ♥ 被%ANAL_CALL()%深入贯穿着……♥♥ 家畜的奶水被吸出来了……♥♥♥」"':
        'CALL MESSAGE_BOX,@"「哦♥ 哦♥ 被%ANAL_CALL()%深入贯穿着……♥♥ 家畜的奶水被吸出来了……♥♥♥」"',
    'CALL MESSAGE_BOX,@"「んおぉっ♥ 随着%ANAL_CALL()%的活塞动作，母乳喷出来了……♥♥」"':
        'CALL MESSAGE_BOX,@"「嗯哦哦♥ 随着%ANAL_CALL()%的活塞动作，母乳喷出来了……♥♥」"',
    'CALL MESSAGE_BOX,@"「んひぃ♥♥ 奶子和%ANAL_CALL()%、两边一起高潮了ぅっ♥♥♥」"':
        'CALL MESSAGE_BOX,@"「嗯咿咿♥♥ 奶子和%ANAL_CALL()%、两边一起高潮了呜♥♥♥」"',
    'CALL MESSAGE_BOX,@"「はっ♥ 哈♥ 奶子啊♥ 被触手凌辱着母乳停不下来ぃぃ♥♥♥」"':
        'CALL MESSAGE_BOX,@"「哈♥ 哈♥ 奶子啊♥ 被触手凌辱着母乳停不下来咿咿♥♥♥」"',
    'CALL MESSAGE_BOX,@"「はひぃ…♥ 一边给%MASTER_CALL()%哺乳，一边达到高潮了……♥♥♥ 啊♥ 啊♥ あっ♥」"':
        'CALL MESSAGE_BOX,@"「哈咿咿…♥ 一边给%MASTER_CALL()%哺乳，一边达到高潮了……♥♥♥ 啊♥ 啊♥ 啊♥」"',
    'CALL MESSAGE_BOX,@"「啊啊っ♥ %SWEET_MASTER_CALL()%っ♥♥ 情感溢出来了……♥♥ 哺乳高潮来了呢……♥♥」"':
        'CALL MESSAGE_BOX,@"「啊啊♥ %SWEET_MASTER_CALL()%♥♥ 情感溢出来了……♥♥ 哺乳高潮来了呢……♥♥」"',
    'CALL MESSAGE_BOX,@"「はひっ♥ はひっ♥ 大胸被吸吮着，幸福到达高潮了……♥♥」"':
        'CALL MESSAGE_BOX,@"「哈咿♥ 哈咿♥ 大胸被吸吮着，幸福到达高潮了……♥♥」"',
    'CALL MESSAGE_BOX,@"「んふー♥ んふー♥ 如此沉迷地被吮吸着，完全忍不住高潮了……♥♥♥」"':
        'CALL MESSAGE_BOX,@"「嗯呼呼♥ 嗯呼呼♥ 如此沉迷地被吮吸着，完全忍不住高潮了……♥♥♥」"',
    'CALL MESSAGE_BOX,@"「啊゛啊啊……♥♥ 勃起的乳头被吮吸着，真是忍受不了了……♥♥♥」"':
        'CALL MESSAGE_BOX,@"「啊啊啊……♥♥ 勃起的乳头被吮吸着，真是忍受不了了……♥♥♥」"',
    'CALL MESSAGE_BOX,@"「啊♥ 啊♥ 被%MASTER_CALL()%吸着敏感萝莉乳头而高潮了ぅぅ♥♥♥」"':
        'CALL MESSAGE_BOX,@"「啊♥ 啊♥ 被%MASTER_CALL()%吸着敏感萝莉乳头而高潮了呜呜♥♥♥」"',
    'CALL MESSAGE_BOX,@"「哈咿っ…♥♥ 明明是未成熟的小孩奶子却被吸出母乳要去了っ♥♥\\n　萝莉乳头勃起着哺乳高潮了呢ぅっ♥♥♥」"':
        'CALL MESSAGE_BOX,@"「哈咿…♥♥ 明明是未成熟的小孩奶子却被吸出母乳要去了♥♥\\n　萝莉乳头勃起着哺乳高潮了呢呜♥♥♥」"',
    'CALL MESSAGE_BOX,@"「啊♥ 啊♥ 被挤奶了哦♥♥♥ 要来了~♥ 要来了~♥ ～～～～～っ♥♥♥」"':
        'CALL MESSAGE_BOX,@"「啊♥ 啊♥ 被挤奶了哦♥♥♥ 要来了~♥ 要来了~♥ ～～～～～♥♥♥」"',
    'CALL MESSAGE_BOX,@"「～～～っ♥♥♥ %MASTER_CALL()%强行搾奶真是太好了♥♥♥」"':
        'CALL MESSAGE_BOX,@"「～～～♥♥♥ %MASTER_CALL()%强行搾奶真是太好了♥♥♥」"',
    'CALL MESSAGE_BOX,@"「嗯啊♥ 榨乳和乳头玩弄同时进行ぇ♥ 怎么可能忍得住にゃいぃぃ♥♥♥」"':
        'CALL MESSAGE_BOX,@"「嗯啊♥ 榨乳和乳头玩弄同时进行诶♥ 怎么可能忍得住的咿咿♥♥♥」"',
    'CALL MESSAGE_BOX,@"「ひぎぃ♥♥ 吸奶和舔乳头一起来ぃぃ♥♥ ひああぁぁっ♥♥♥」"':
        'CALL MESSAGE_BOX,@"「咿咿咿♥♥ 吸奶和舔乳头一起来咿咿♥♥ 咿啊啊啊啊♥♥♥」"',
    'CALL MESSAGE_BOX,@"「这、这种っ♥ 触手的榨乳乳头玩弄っ♥♥ 刺激太强了、受不了っ…ひっ……♥♥」"':
        'CALL MESSAGE_BOX,@"「这、这种♥ 触手的榨乳乳头玩弄♥♥ 刺激太强了、受不了…咿……♥♥」"',
    'CALL MESSAGE_BOX,@"「啊♥ 啊♥ %VAGINA_CALL()%和乳头两边都去了…♥♥\\n　真是个不堪的母兽，抱歉……啊♥ 啊♥ 啊啊啊～～っ♥」"':
        'CALL MESSAGE_BOX,@"「啊♥ 啊♥ %VAGINA_CALL()%和乳头两边都去了…♥♥\\n　真是个不堪的母兽，抱歉……啊♥ 啊♥ 啊啊啊～～♥」"',
    'CALL MESSAGE_BOX,@"「んおぉっ♥ 随着%ANAL_CALL()%的活塞动作，母乳喷出来了……♥♥」"':
        'CALL MESSAGE_BOX,@"「嗯哦哦♥ 随着%ANAL_CALL()%的活塞动作，母乳喷出来了……♥♥」"',
    'CALL MESSAGE_BOX,@"「んひぃ♥♥ 奶子和%ANAL_CALL()%、两边一起高潮了ぅっ♥♥♥」"':
        'CALL MESSAGE_BOX,@"「嗯咿咿♥♥ 奶子和%ANAL_CALL()%、两边一起高潮了呜♥♥♥」"',
    'CALL MESSAGE_BOX,@"「哈呜…♥ 胸部っ♥ 就像触手的玩物一样……♥ ふあぁっ♥♥」"':
        'CALL MESSAGE_BOX,@"「哈呜…♥ 胸部♥ 就像触手的玩物一样……♥ 呼啊啊♥♥」"',
    'CALL MESSAGE_BOX,@"「は、ぐっ♥ 被触手ぃ♥ 玩弄着乳头强行吸走母乳……んおぉぉっ～～♥♥♥♥」"':
        'CALL MESSAGE_BOX,@"「哈、咕♥ 被触手咿♥ 玩弄着乳头强行吸走母乳……嗯哦哦哦哦～～♥♥♥♥」"',
    'CALL MESSAGE_BOX,@"「啊啊っ♥ 被这么执着地吸的话…♥♥ 要、要去了っ♥♥♥」"':
        'CALL MESSAGE_BOX,@"「啊啊♥ 被这么执着地吸的话…♥♥ 要、要去了♥♥♥」"',
    'CALL MESSAGE_BOX,@"「ひあぁっ♥ 居然因为搾奶而高潮了……♥♥」"':
        'CALL MESSAGE_BOX,@"「咿啊啊♥ 居然因为搾奶而高潮了……♥♥」"',
    'CALL MESSAGE_BOX,@"「啊啊っ…出来了……出来了っ……んあぁぁ♥」"':
        'CALL MESSAGE_BOX,@"「啊啊…出来了……出来了……嗯啊啊啊♥」"',
    'CALL MESSAGE_BOX,@"「んやぁ♥♥ 胸部和%VAGINA_CALL()%都被随意玩弄到高潮了……♥」"':
        'CALL MESSAGE_BOX,@"「嗯呀啊♥♥ 胸部和%VAGINA_CALL()%都被随意玩弄到高潮了……♥」"',
    'CALL MESSAGE_BOX,@"「んぅぅ…♥ 被强行榨出母乳… 停…不…下……♥」"':
        'CALL MESSAGE_BOX,@"「嗯呜呜…♥ 被强行榨出母乳… 停…不…下……♥」"',
    'CALL MESSAGE_BOX,@"「んあっ♥ 被挤出母乳就高潮了……真是屈辱呢……」"':
        'CALL MESSAGE_BOX,@"「嗯啊♥ 被挤出母乳就高潮了……真是屈辱呢……」"',
    'CALL MESSAGE_BOX,@"「呜……跟机器在一起……竟然会有感觉……っ♥」"':
        'CALL MESSAGE_BOX,@"「呜……跟机器在一起……竟然会有感觉……♥」"',
    'CALL MESSAGE_BOX,@"「うあぁ♥ 一边插入一边榨乳太卑鄙了、东西ぉ♥♥」"':
        'CALL MESSAGE_BOX,@"「呜啊啊♥ 一边插入一边榨乳太卑鄙了、东西哦♥♥」"',
    'CALL MESSAGE_BOX,@"「ひぎぃっ…♥ 竟然用触手强行给予快感……真是卑鄙……っ♥」"':
        'CALL MESSAGE_BOX,@"「咿咿咿…♥ 竟然用触手强行给予快感……真是卑鄙……♥」"',
    'CALL MESSAGE_BOX,@"「ぐうぅ… %SELF_CALL()%的魔力竟然在这种地方失去……」"':
        'CALL MESSAGE_BOX,@"「咕呜呜… %SELF_CALL()%的魔力竟然在这种地方失去……」"',
    'CALL MESSAGE_BOX,@"「んぎぃ♥ ひぎっ♥♥ 要、要去的时候ぃ♥♥ 从胸部喷涌而出的灵力……♥♥♥」"':
        'CALL MESSAGE_BOX,@"「嗯咿咿♥ 咿咿♥♥ 要、要去的时候咿♥♥ 从胸部喷涌而出的灵力……♥♥♥」"',
    'CALL MESSAGE_BOX,@"「んほぉ♥♥ %SWEET_MASTER_CALL()%♥♥ 请把我全部夺走……♥♥♥」"':
        'CALL MESSAGE_BOX,@"「嗯嚯哦♥♥ %SWEET_MASTER_CALL()%♥♥ 请把我全部夺走……♥♥♥」"',
    'CALL MESSAGE_BOX,@"「ふぎぃっ♥♥ 请把%SELF_CALL()%变成适合家畜的无力母牛吧♥♥♥」"':
        'CALL MESSAGE_BOX,@"「呼咿咿♥♥ 请把%SELF_CALL()%变成适合家畜的无力母牛吧♥♥♥」"',
    'CALL MESSAGE_BOX,@"「おぉっ♥♥ 对家畜来说灵力是无用的呢♥♥ 请尽情吸取我的资源吧♥♥」"':
        'CALL MESSAGE_BOX,@"「哦哦♥♥ 对家畜来说灵力是无用的呢♥♥ 请尽情吸取我的资源吧♥♥」"',
    'CALL MESSAGE_BOX,@"「啊っ♥♥ 啊っ♥♥ %SELF_CALL()%和%MASTER_CALL()%的灵力融合在一起…♥♥\\n　あぁぁあっ♥ 太幸福了要…去……了……～～～～っ♥♥♥」"':
        'CALL MESSAGE_BOX,@"「啊♥♥ 啊♥♥ %SELF_CALL()%和%MASTER_CALL()%的灵力融合在一起…♥♥\\n　啊啊啊啊♥ 太幸福了要…去……了……～～～～♥♥♥」"',
    'CALL MESSAGE_BOX,@"「はぁあ…♥♥ 能把%SELF_CALL()%的力量变成%MASTER_CALL()%的养分……真是……♥♥」"':
        'CALL MESSAGE_BOX,@"「哈啊啊…♥♥ 能把%SELF_CALL()%的力量变成%MASTER_CALL()%的养分……真是……♥♥」"',
    'CALL MESSAGE_BOX,@"「んあ゛ぁっ♥♥ 喷出来了♥ 一边喷涌灵力一边高潮呢♥♥」"':
        'CALL MESSAGE_BOX,@"「嗯啊啊♥♥ 喷出来了♥ 一边喷涌灵力一边高潮呢♥♥」"',
    'CALL MESSAGE_BOX,@"「はぁはぁ…♥ 力量直接被吸走了……♥」"':
        'CALL MESSAGE_BOX,@"「哈啊哈啊…♥ 力量直接被吸走了……♥」"',
    'CALL MESSAGE_BOX,@"「呃 停下……っ 灵力被夺走……嗯♥」"':
        'CALL MESSAGE_BOX,@"「呃 停下…… 灵力被夺走……嗯♥」"',
    'CALL MESSAGE_BOX,@"「……っ！ 总有一天会让您后悔的……」"':
        'CALL MESSAGE_BOX,@"「……！ 总有一天会让您后悔的……」"',
    'CALL MESSAGE_BOX,@"「はぁ…はぁ… 为什么会这样……」"':
        'CALL MESSAGE_BOX,@"「哈啊…哈啊… 为什么会这样……」"',

    # あむ/ぢゅる/れろ line
    'CALL MESSAGE_BOX,@"「あむ♥ ぢゅる♥ れろ…♥ あぁ…%SWEET_MASTER_CALL()%♥」"':
        'CALL MESSAGE_BOX,@"「啊呜♥ 滋溜♥ 舔舔…♥ 啊啊…%SWEET_MASTER_CALL()%♥」"',

    # ちゅ/ん
    'CALL MESSAGE_BOX,@"「ん…♥ ちゅっ♥ んん…♥ %SWEET_MASTER_CALL()%…♥ 好喜欢……♥」"':
        'CALL MESSAGE_BOX,@"「嗯…♥ 啾♥ 嗯嗯…♥ %SWEET_MASTER_CALL()%…♥ 好喜欢……♥」"',
    'CALL MESSAGE_BOX,@"「ちゅ……ふ……ん…♥」"':
        'CALL MESSAGE_BOX,@"「啾……呼……嗯…♥」"',

    # 押す line
    'CALL MESSAGE_BOX,@"「ふー♥ ふー♥ ……んふーっ♥♥」\\n（啊啊…♥ 能让我的身体更加有用呢♥♥）"':
        'CALL MESSAGE_BOX,@"「呼呼♥ 呼呼♥ ……嗯呼呼♥♥」\\n（啊啊…♥ 能让我的身体更加有用呢♥♥）"',
    'CALL MESSAGE_BOX,@"「ん゛ーっ！ ふぐぅっ！ 嗯嗯っ！」\\n（呜……这、这是什么……）"':
        'CALL MESSAGE_BOX,@"「嗯——！ 咕呜呜！ 嗯嗯！」\\n（呜……这、这是什么……）"',
    'CALL MESSAGE_BOX,@"「呃…っ」"':
        'CALL MESSAGE_BOX,@"「呃…」"',
    'CALL MESSAGE_BOX,@"「咳…っ」"':
        'CALL MESSAGE_BOX,@"「咳…」"',
    'CALL MESSAGE_BOX,@"「……っ！ 不会浪费您的关心……」"':
        'CALL MESSAGE_BOX,@"「……！ 不会浪费您的关心……」"',

    # === 慇懃口上1_スケジュール.ERB ===
    'CALL MESSAGE_BOX,@"「はーっ♥ はーっ♥ 搾乳されたい…♥ もう待ちきれません……♥♥」"':
        'CALL MESSAGE_BOX,@"「哈——♥ 哈——♥ 想被挤奶…♥ 已经迫不及待了……♥♥」"',
    'CALL MESSAGE_BOX,@"「その器具はまさか… 啊，%SELF_CALL()%也被承认为成熟的家畜了……♥♥」"':
        'CALL MESSAGE_BOX,@"「那个器具难道是… 啊，%SELF_CALL()%也被承认为成熟的家畜了……♥♥」"',
    'CALL MESSAGE_BOX,@"「その器具はまるで…♥ 怎么能把%SELF_CALL()%当成真正的家畜一样…？♥♥♥」"':
        'CALL MESSAGE_BOX,@"「那个器具简直……♥ 怎么能把%SELF_CALL()%当成真正的家畜一样…？♥♥♥」"',
    'CALL MESSAGE_BOX,@"「その器具はまさか… 啊，从今以后我能更加为您效力了呢……♥♥」"':
        'CALL MESSAGE_BOX,@"「那个器具难道是… 啊，从今以后我能更加为您效力了呢……♥♥」"',
    'CALL MESSAGE_BOX,@"「その器具はまるで…♥ 怎么能把%SELF_CALL()%当成真正的家畜一样…？♥♥♥」"':
        'CALL MESSAGE_BOX,@"「那个器具简直……♥ 怎么能把%SELF_CALL()%当成真正的家畜一样…？♥♥♥」"',
    'CALL MESSAGE_BOX,@"「それは牛用の…？ 呜……%SELF_CALL()%也被当成一头家畜了呢……」"':
        'CALL MESSAGE_BOX,@"「那是给牛用的…？ 呜……%SELF_CALL()%也被当成一头家畜了呢……」"',
    'CALL MESSAGE_BOX,@"「那是给牛用的器具……？ まさか%SELF_CALL()%に……！？」"':
        'CALL MESSAGE_BOX,@"「那是给牛用的器具……？ 难道要对%SELF_CALL()%……！？」"',
    'CALL MESSAGE_BOX,@"「あぁ…♥ %MASTER_CALL()%に搾乳して頂けるなんて…♥♥ 沢山母乳をお出ししますからね…♥♥」"':
        'CALL MESSAGE_BOX,@"「啊啊…♥ 居然能让%MASTER_CALL()%为我挤奶…♥♥ 我会努力产出很多母乳的哦…♥♥」"',
    'CALL MESSAGE_BOX,@"「…………」\\n\\d%CALLNAME%は虚ろな目で、されるがままになっている…"':
        'CALL MESSAGE_BOX,@"「…………」\\n\\d%CALLNAME%眼神空洞，任由摆布…"',
    'CALL MESSAGE_BOX,@"「あひぃ♥♥ 美味しい家畜ミルク…♥♥ 要挤出很多奶哦…♥♥」"':
        'CALL MESSAGE_BOX,@"「啊咿咿♥♥ 美味的家畜奶…♥♥ 要挤出很多奶哦…♥♥」"',
    'CALL MESSAGE_BOX,@"「ふあぁ…♥ 竟然能被%MASTER_CALL()%挤奶♥ 这真是作为家畜的无上光荣…♥♥」"':
        'CALL MESSAGE_BOX,@"「呼啊啊…♥ 竟然能被%MASTER_CALL()%挤奶♥ 这真是作为家畜的无上光荣…♥♥」"',
    'CALL MESSAGE_BOX,@"「%SWEET_MASTER_CALL()%♥♥ 搾乳狂いの牝牛ミルク♥ 请彻底挤干净我吧♥♥♥♥」"':
        'CALL MESSAGE_BOX,@"「%SWEET_MASTER_CALL()%♥♥ 挤奶成瘾的母牛奶♥ 请彻底挤干净我吧♥♥♥♥」"',
    'CALL MESSAGE_BOX,@"「…本当は%MASTER_CALL()%に…… 不，不能任性……」"':
        'CALL MESSAGE_BOX,@"「…其实想对%MASTER_CALL()%…… 不，不能任性……」"',
    'CALL MESSAGE_BOX,@"「はぅ… 又要被挤奶了…」"':
        'CALL MESSAGE_BOX,@"「哈呜… 又要被挤奶了…」"',
    'CALL MESSAGE_BOX,@"「っ……！ 这种事情，怎么可能被允许……！」"':
        'CALL MESSAGE_BOX,@"「……！ 这种事情，怎么可能被允许……！」"',
    'CALL MESSAGE_BOX,@"「はひぃぃ…♥ 这么多…已经出来了…♥♥♥ あぅ……♥♥」"':
        'CALL MESSAGE_BOX,@"「哈咿咿咿…♥ 这么多…已经出来了…♥♥♥ 啊呜……♥♥」"',
    'CALL MESSAGE_BOX,@"「かひっ…♥♥ 挤奶……这么幸福……啊♥♥♥」"':
        'CALL MESSAGE_BOX,@"「咔嘻…♥♥ 挤奶……这么幸福……啊♥♥♥」"',
    'CALL MESSAGE_BOX,@"「は、はへっ…♥ 乳房已经空了…♥♥ 已经流不出来了……♥♥♥」"':
        'CALL MESSAGE_BOX,@"「哈、哈嘿…♥ 乳房已经空了…♥♥ 已经流不出来了……♥♥♥」"',
    'CALL MESSAGE_BOX,@"「ふあぁ…♥♥ はぁ…はぁ…♥♥」"':
        'CALL MESSAGE_BOX,@"「呼啊啊…♥♥ 哈啊…哈啊…♥♥」"',
    'CALL MESSAGE_BOX,@"「あひぃ…♥♥ こんなに…しぼられるなんて……♥♥」"':
        'CALL MESSAGE_BOX,@"「啊咿咿…♥♥ 居然被这样……榨取……♥♥」"',
    'CALL MESSAGE_BOX,@"「ふ、ふひっ……♥ かんじすぎて…くるいそう……♥♥」"':
        'CALL MESSAGE_BOX,@"「呼、呼咿……♥ 太有感觉了…感觉要疯掉了……♥♥」"',
    'CALL MESSAGE_BOX,@"「む、むりっ…♥ 乳房里已经什么都不剩了…♥♥」"':
        'CALL MESSAGE_BOX,@"「不、不行了…♥ 乳房里已经什么都不剩了…♥♥」"',
    'CALL MESSAGE_BOX,@"「はぁ…はぁ… 结、结束了吗……」"':
        'CALL MESSAGE_BOX,@"「哈啊…哈啊… 结、结束了吗……」"',
    'CALL MESSAGE_BOX,@"「んおぉ…♥♥ また動き出して…♥ 灵力正在被吸走…♥♥」"':
        'CALL MESSAGE_BOX,@"「嗯哦哦…♥♥ 又开始动了…♥ 灵力正在被吸走…♥♥」"',
    'CALL MESSAGE_BOX,@"「嫌……また霊力が奪われて……後生でございます、おやめください……」"':
        'CALL MESSAGE_BOX,@"「不要……灵力又被夺走了……求求您了，请停下吧……」"',
    'CALL MESSAGE_BOX,@"「ひっ……また動き始めて……まさか力をすべて奪うつもりでは…」"':
        'CALL MESSAGE_BOX,@"「咿……又开始动了……难道打算夺走全部力量……」"',
    'CALL MESSAGE_BOX,@"「あ、あの…%SELF_CALL()%は反抗などしませんし、およしいただけませんか…？」"':
        'CALL MESSAGE_BOX,@"「那、那个…%SELF_CALL()%不会反抗的，能请您高抬贵手吗…？」"',
    'CALL MESSAGE_BOX,@"「あ、あぁ…っ……またこの機械の中に……っ！？」"':
        'CALL MESSAGE_BOX,@"「啊、啊啊……又进到这个机器里了……！？」"',
    'CALL MESSAGE_BOX,@"「いっぱいぃ…♥♥ 奶和力量都被榨干了…♥♥」"':
        'CALL MESSAGE_BOX,@"「满满的咿…♥♥ 奶和力量都被榨干了…♥♥」"',
    'CALL MESSAGE_BOX,@"「あ、あひぃ…♥♥ 已经结束了吗…♥♥♥」"':
        'CALL MESSAGE_BOX,@"「啊、啊咿咿…♥♥ 已经结束了吗…♥♥♥」"',

    # Complex JP in brackets
    'CALL MESSAGE_BOX,@"「はっ…はひっ…♥♥ お、お哈…おぉ……♥♥」\\n（さくにゅうされて、ちからすわれて、かちくいっちょくせん…♥♥♥）"':
        'CALL MESSAGE_BOX,@"「哈…哈咿…♥♥ 哦、哦哈…哦哦……♥♥」\\n（被挤了奶、被吸了力、家畜一条直线…♥♥♥）"',

    'CALL MESSAGE_BOX,@"「あぁ…ぁ…♥ 结束了…♥ 请让我出去吧…♥♥」"':
        'CALL MESSAGE_BOX,@"「啊啊…啊…♥ 结束了…♥ 请让我出去吧…♥♥」"',
    'CALL MESSAGE_BOX,@"「かひっ♥ は、はひ…♥♥ たえられにゃい…♥♥ イきくるう…♥♥♥」"':
        'CALL MESSAGE_BOX,@"「咔嘻♥ 哈、哈咿…♥♥ 受不了的…♥♥ 要疯掉了…♥♥♥」"',
    'CALL MESSAGE_BOX,@"「おっ♥ おっ♥ おわった…♥♥ 请快点放我出去吧…♥」"':
        'CALL MESSAGE_BOX,@"「哦♥ 哦♥ 结束了…♥♥ 请快点放我出去吧…♥」"',
    'CALL MESSAGE_BOX,@"「ふ…あぁ…♥ こ、これ以上力を奪われたら……あぅ…♥」"':
        'CALL MESSAGE_BOX,@"「呼…啊啊…♥ 再、再这样被夺走力量的话……啊呜…♥」"',
    'CALL MESSAGE_BOX,@"「あ…あぁ…%MASTER_CALL()%…？ %SELF_CALL()%已经没用了是吗…？\\n　我、我还能继续为您效力的！ 请您慈悲为怀……啊……！」"':
        'CALL MESSAGE_BOX,@"「啊…啊啊…%MASTER_CALL()%…？ %SELF_CALL()%已经没用了是吗…？\\n　我、我还能继续为您效力的！ 请您慈悲为怀……啊……！」"',
    'CALL MESSAGE_BOX,@"「ば、化け物っ！？ 不要啊！ 帮，帮帮我！！ 有人吗！」"':
        'CALL MESSAGE_BOX,@"「妖、妖怪！？ 不要啊！ 帮，帮帮我！！ 有人吗！」"',
    'CALL MESSAGE_BOX,@"「あぁ……♥♥ %SWEET_MASTER_CALL()%♥♥ 请再度将%SELF_CALL()%送回那极乐之境…♥♥」"':
        'CALL MESSAGE_BOX,@"「啊啊……♥♥ %SWEET_MASTER_CALL()%♥♥ 请再度将%SELF_CALL()%送回那极乐之境…♥♥」"',
    'CALL MESSAGE_BOX,@"「あ…あぁ… 怎么又要去"那边"了吗…！？ 这次心灵真的要崩溃了……！」"':
        'CALL MESSAGE_BOX,@"「啊…啊啊… 怎么又要去"那边"了吗…！？ 这次心灵真的要崩溃了……！」"',

    # Climax sound chains
    'CALL MESSAGE_BOX,@"「～～～っ♥♥♥ ……かひッ♥♥ はひィっ♥♥♥ ッ！ ッ！ ～～～～ッ♥♥♥♥」"':
        'CALL MESSAGE_BOX,@"「～～～♥♥♥ ……咔嘻♥♥ 哈咿♥♥♥ ！ ！ ～～～～♥♥♥♥」"',
    'CALL MESSAGE_BOX,@"「お゛ーっ♥ おっ♥ おっ♥ おっ♥ んぐっ♥ おお゛ぉぉ～～♥♥」"':
        'CALL MESSAGE_BOX,@"「哦——♥ 哦♥ 哦♥ 哦♥ 嗯咕♥ 哦哦哦哦哦～～♥♥」"',
    'CALL MESSAGE_BOX,@"「哦♥ 哦♥ お゛おぉっ♥♥♥ ア、アタマ灼き切れるっ♥♥♥ んぎぃぃぃ♥♥♥♥」"':
        'CALL MESSAGE_BOX,@"「哦♥ 哦♥ 哦哦♥♥♥ 脑、脑袋要烧断了♥♥♥ 嗯咿咿咿咿♥♥♥♥」"',
    'CALL MESSAGE_BOX,@"（これいじょうは♥♥ つぶれるっ♥ 快楽におしつぶされるっ♥♥♥）"':
        'CALL MESSAGE_BOX,@"（再这样下去♥♥ 就要坏掉了♥ 被快感碾碎了♥♥♥）"',
    'CALL MESSAGE_BOX,@"「あ゛っ♥♥ あひっ♥♥ %MASTER_CALL()%っ♥♥ た、たすっ……んぎゅぅぅぅぅ♥♥♥」"':
        'CALL MESSAGE_BOX,@"「啊♥♥ 啊咿♥♥ %MASTER_CALL()%♥♥ 救、救命……嗯咿呜呜呜呜♥♥♥」"',
    'CALL MESSAGE_BOX,@"「ひぐっ♥♥ こ、こわれる…♥♥ ゆるしてっ♥♥ ゆるし――いぎぃぃぃ♥♥♥♥」"':
        'CALL MESSAGE_BOX,@"「咿咕♥♥ 要、要坏了…♥♥ 原谅我♥♥ 原——咿咿咿咿咿♥♥♥♥」"',
    'CALL MESSAGE_BOX,@"「啊ー♥ 啊ー♥ かはっ♥ んぎっ♥ …んお゛お゛ぉぉぉ♥♥♥♥」"':
        'CALL MESSAGE_BOX,@"「啊—♥ 啊—♥ 咔哈♥ 嗯咿♥ …嗯哦哦哦哦哦♥♥♥♥」"',
    'CALL MESSAGE_BOX,@"「ひっ… 请放开我…！ 再也不想经历那样的事情了……」"':
        'CALL MESSAGE_BOX,@"「咿… 请放开我…！ 再也不想经历那样的事情了……」"',
    'CALL MESSAGE_BOX,@"（からだが痙攣して動かない…♥♥ 那种程度的快感，根本不可能承受得住…♥♥♥）"':
        'CALL MESSAGE_BOX,@"（身体痉挛动不了…♥♥ 那种程度的快感，根本不可能承受得住…♥♥♥）"',
    'CALL MESSAGE_BOX,@"「あ、あぁ…♥♥ 等一下…就这样结束我可不愿意啊…♥♥」"':
        'CALL MESSAGE_BOX,@"「啊、啊啊…♥♥ 等一下…就这样结束我可不愿意啊…♥♥」"',
    'CALL MESSAGE_BOX,@"「ひぁ…♥ ひぅぅ…♥♥ からだ痙攣して…♥ う、うごけない…♥♥」"':
        'CALL MESSAGE_BOX,@"「咿啊…♥ 咿呜呜…♥♥ 身体痉挛…♥ 动、动不了…♥♥」"',
    'CALL MESSAGE_BOX,@"「はぁ…… 如果抵抗无效，至少请简短些……」"':
        'CALL MESSAGE_BOX,@"「哈啊…… 如果抵抗无效，至少请简短些……」"',
    'CALL MESSAGE_BOX,@"「呃，呵呵…%SWEET_MASTER_CALL()%…我，我并不太喜欢痛苦的感觉……\\n　啊…没，没什么……っ」"':
        'CALL MESSAGE_BOX,@"「呃，呵呵…%SWEET_MASTER_CALL()%…我，我并不太喜欢痛苦的感觉……\\n　啊…没，没什么……」"',
    'CALL MESSAGE_BOX,@"「ふぁあ…♥ 居然能被这样对待…♥♥♥」"':
        'CALL MESSAGE_BOX,@"「呼啊啊…♥ 居然能被这样对待…♥♥♥」"',
    'CALL MESSAGE_BOX,@"「はぁ…はぁ…♥♥ 早，早就体力不支了…♥♥」"':
        'CALL MESSAGE_BOX,@"「哈啊…哈啊…♥♥ 早，早就体力不支了…♥♥」"',
    'CALL MESSAGE_BOX,@"「は、はひっ…♥ 要花多少时间啊…♥」"':
        'CALL MESSAGE_BOX,@"「哈、哈咿…♥ 要花多少时间啊…♥」"',
    'CALL MESSAGE_BOX,@"「ぜぇ…ぜぇ……もう…限界……」"':
        'CALL MESSAGE_BOX,@"「啧啧……啧啧……已经……极限了……」"',
    'CALL MESSAGE_BOX,@"「はぁ♥ 噗啊♥ ……看来您已经满足了呢…」"':
        'CALL MESSAGE_BOX,@"「哈啊♥ 噗啊♥ ……看来您已经满足了呢…」"',
    'CALL MESSAGE_BOX,@"「ぜぇ…ぜぇ……体力が…限界…」"':
        'CALL MESSAGE_BOX,@"「啧啧……啧啧……体力……到极限了……」"',
    'CALL MESSAGE_BOX,@"「おはようございます、%MASTER_CALL()%♥\\n　呵呵…今天也请让我用嘴侍奉您叫醒您吧♥」"':
        'CALL MESSAGE_BOX,@"「早上好、%MASTER_CALL()%♥\\n　呵呵…今天也请让我用嘴侍奉您叫醒您吧♥」"',
    'CALL MESSAGE_BOX,@"「请尽快结束…您到底想让我含到什么时候……っ」"':
        'CALL MESSAGE_BOX,@"「请尽快结束…您到底想让我含到什么时候……」"',
    'CALL MESSAGE_BOX,@"「……っ！」（不要…好怕…）"':
        'CALL MESSAGE_BOX,@"「……！」（不要…好怕…）"',
    'CALL MESSAGE_BOX,@"「……っ！」（ここで見つかる訳には…っ）"':
        'CALL MESSAGE_BOX,@"「……！」（不能在这里被发现…）"',
    'CALL MESSAGE_BOX,@"「あ、あぁ…っ！ いつのまに…っ！」"':
        'CALL MESSAGE_BOX,@"「啊、啊啊…！ 什么时候…！」"',
    'CALL MESSAGE_BOX,@"「くっ…！ 我大意了…！」"':
        'CALL MESSAGE_BOX,@"「咕…！ 我大意了…！」"',
}


def translate_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    changed = 0
    # First try line-level exact matches
    for old_line, new_line in line_translations.items():
        if old_line in content:
            content = content.replace(old_line, new_line)
            changed += 1

    print(f'  Line-level translations: {changed}')

    # Verify no JP kana remain in MESSAGE_BOX/PRINT lines
    remaining = 0
    for i, line in enumerate(content.split('\n')):
        has_jp = any('\u3040' <= c <= '\u30ff' for c in line)
        has_print = 'MESSAGE_BOX' in line or 'PRINTFORML' in line
        if has_jp and has_print:
            remaining += 1
            if remaining <= 10:
                print(f'  REMAINING [{i+1}]: {line.strip()[:120]}')

    if remaining > 10:
        print(f'  ... and {remaining - 10} more JP lines')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    return remaining


def main():
    files = [
        os.path.join(BASE, '慇懃口上1.ERB'),
        os.path.join(BASE, '慇懃口上1_スケジュール.ERB'),
    ]

    for fp in files:
        fname = os.path.basename(fp)
        print(f'\n=== {fname} ===')
        remaining = translate_file(fp)
        print(f'  → {remaining} JP lines remaining after translation')

if __name__ == '__main__':
    main()
