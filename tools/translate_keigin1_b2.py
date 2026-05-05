#!/usr/bin/env python3
"""慇懃口上1.ERB — Batch 2: 射精/乳内+精饮+手淫+搾乳 sections"""
import sys
sys.stdout = open(1, 'w', encoding='utf-8', closefd=False)

FPATH = r"C:\Cursor local\era-makai-ranch\ERB\○口上\汎用口上\慇懃口上1.ERB"

R = {
    # === 射精/乳内 (lines ~256-260) ===
    r'CALL MESSAGE_BOX,@"「啊啊♥  为什么呢♥♥ せーえききもちいいっ♥♥ 最喜欢乳内射精了呀♥♥」"':
    r'CALL MESSAGE_BOX,@"「啊啊♥  为什么呢♥♥ 精液好舒服っ♥♥ 最喜欢乳内射精了呀♥♥」"',

    r'CALL MESSAGE_BOX,@"「はひぃ…♥ 每次乳内射精时，胸部都屈服于%PENIS_CALL()%了呀♥♥」"':
    r'CALL MESSAGE_BOX,@"「哈咿…♥ 每次乳内射精时，胸部都屈服于%PENIS_CALL()%了呀♥♥」"',

    r'CALL MESSAGE_BOX,@"「啊哈哈…♥ 精液でぐちゃぐちゃのどろどろ…♥」"':
    r'CALL MESSAGE_BOX,@"「啊哈哈…♥ 被精液弄得黏糊糊乱七八糟…♥」"',

    r'CALL MESSAGE_BOX,@"「はふぅ♥♥ 感谢使用乳交自慰器呀♥♥」"':
    r'CALL MESSAGE_BOX,@"「哈呼♥♥ 感谢使用乳交自慰器呀♥♥」"',

    r'CALL MESSAGE_BOX,@"「はぁ♥ 浓厚的精液从乳沟中源源不断地溢出……令人陶醉呀……♥」"':
    r'CALL MESSAGE_BOX,@"「哈啊♥ 浓厚的精液从乳沟中源源不断地溢出……令人陶醉呀……♥」"',

    # === 射精/精饮 口交 (lines ~302-322) ===
    r'CALL MESSAGE_BOX,@"「ん～～～♥ ぢゅるるるるる……♥ ぷはぁ…♥♥♥\n　我会把%PENIS_CALL()%里剩下的也全部吸出来的哦……♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「嗯～～～♥ 啾噜噜噜噜噜……♥ 噗哈…♥♥♥\n　我会把%PENIS_CALL()%里剩下的也全部吸出来的哦……♥♥♥」"',

    r'CALL MESSAGE_BOX,@"「あぁ♥♥ %MASTER_CALL()%的%PENIS_CALL()%太棒了呀……♥♥\n　我想一直为您口交……♥♥」"':
    r'CALL MESSAGE_BOX,@"「啊啊♥♥ %MASTER_CALL()%的%PENIS_CALL()%太棒了呀……♥♥\n　我想一直为您口交……♥♥」"',

    r'CALL MESSAGE_BOX,@"「～～っ♥♥ %MASTER_CALL()%的浓厚精液呀♥♥ 让我的脑袋深处都麻痹了……♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「～～っ♥♥ %MASTER_CALL()%的浓厚精液呀♥♥ 让我的脑袋深处都麻痹了……♥♥♥」"',

    r'CALL MESSAGE_BOX,@"「喂，♥ ん～～♥ …んくっ…んくっ……ぷはぁ♥\n　はぁ…♥♥ 感谢在我的嘴便器中排泄精液呀♥♥」"':
    r'CALL MESSAGE_BOX,@"「喂，♥ 嗯～～♥ …嗯咕っ…嗯咕っ……噗哈♥\n　哈啊…♥♥ 感谢在我的嘴便器中排泄精液呀♥♥」"',

    r'CALL MESSAGE_BOX,@"「んくっ♥ んくっ♥ ふぅ……♥ 您射了这么多呀……♥」"':
    r'CALL MESSAGE_BOX,@"「嗯咕っ♥ 嗯咕っ♥ 呼……♥ 您射了这么多呀……♥」"',

    r'CALL MESSAGE_BOX,@"「嗯♥ 咳…♥ 嗯～，啧啧……♥\n　我最喜欢口交服务了，感觉是在最尽心地伺候您……♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「嗯♥ 咳…♥ 嗯～，啧啧……♥\n　我最喜欢口交服务了，感觉是在最尽心地伺候您……♥♥♥」"',

    r'CALL MESSAGE_BOX,@"「んくっ♥ んくっ♥ ふぅ……♥ %MASTER_CALL()%的味道……♥ 已经彻底上瘾了呢……♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「嗯咕っ♥ 嗯咕っ♥ 呼……♥ %MASTER_CALL()%的味道……♥ 已经彻底上瘾了呢……♥♥♥」"',

    r'CALL MESSAGE_BOX,@"「んぐ…♥ んん……♥ こ哈…♥♥ 浓浓的精液缠绕在喉咙深处……♥ 已经忍不住了……♥♥」"':
    r'CALL MESSAGE_BOX,@"「嗯咕…♥ 嗯嗯……♥ 咔哈…♥♥ 浓浓的精液缠绕在喉咙深处……♥ 已经忍不住了……♥♥」"',

    r'CALL MESSAGE_BOX,@"「うぅ…生臭い……はぁ…はぁ……」"':
    r'CALL MESSAGE_BOX,@"「呜…好腥臭……哈啊…哈啊……」"',

    r'CALL MESSAGE_BOX,@"「～～～～っ！ ご哈！……ぉぇぇ…」"':
    r'CALL MESSAGE_BOX,@"「～～～～っ！ 咔哈！……呕呃…」"',

    # === 射精/深喉 (lines ~327-338) ===
    r'CALL MESSAGE_BOX,@"「ぐっ！♥……んぐ♥…ぅぐ♥…んぐ♥……かふっ♥\n　直接射在喉咙深处……♥ 谢谢您……♥♥」"':
    r'CALL MESSAGE_BOX,@"「咕っ！♥……嗯咕♥…呜咕♥…嗯咕♥……咔呼っ♥\n　直接射在喉咙深处……♥ 谢谢您……♥♥」"',

    r'CALL MESSAGE_BOX,@"「んぶっ！♥……ごきゅっ♥…ごきゅっ♥……はふぅ♥♥\n　嗯嗯……精液的热量顺着喉咙传到肚子里……♥♥」"':
    r'CALL MESSAGE_BOX,@"「嗯噗っ！♥……咕噜っ♥…咕噜っ♥……哈呼♥♥\n　嗯嗯……精液的热量顺着喉咙传到肚子里……♥♥」"',

    r'CALL MESSAGE_BOX,@"「んん゛っ♥……ぐっ♥…んぐ♥………かはぁっ♥♥\n　我的喉咙自慰器，您感到满意吗……♥♥」"':
    r'CALL MESSAGE_BOX,@"「嗯嗯゛っ♥……咕っ♥…嗯咕♥………咔哈っ♥♥\n　我的喉咙自慰器，您感到满意吗……♥♥」"',

    r'CALL MESSAGE_BOX,@"「ごっ♥ おごぉ♥♥…んん゛♥……げ哈♥…げ哈♥……\n　ふぅ…♥ 精液撞击喉咙深处的感觉真是受不了……♥♥」"':
    r'CALL MESSAGE_BOX,@"「咯っ♥ 哦咯♥♥…嗯嗯゛♥……咳哈♥…咳哈♥……\n　呼…♥ 精液撞击喉咙深处的感觉真是受不了……♥♥」"',

    r'CALL MESSAGE_BOX,@"「んぶっ♥♥ ぐっ……んむ゛っ♥ ん゛嗯………ごふ…♥♥♥\n　……如果还没射够的话……请继续使用我吧……♥♥」"':
    r'CALL MESSAGE_BOX,@"「嗯噗っ♥♥ 咕っ……嗯呜゛っ♥ 嗯゛嗯………咯呼…♥♥♥\n　……如果还没射够的话……请继续使用我吧……♥♥」"',

    r'CALL MESSAGE_BOX,@"「～～～～っ！？ げ哈！ ご哈！ く、くるし……かはっ…！」"':
    r'CALL MESSAGE_BOX,@"「～～～～っ！？ 咳哈！ 咯哈！ 好、好痛苦……咔哈っ…！」"',

    r'CALL MESSAGE_BOX,@"「ぐぶぅっ！？ ぐっ…ぶふっ……ぅえ゛ぇぇっ！」"':
    r'CALL MESSAGE_BOX,@"「咕噗っ！？ 咕っ…噗呼……呕呃呃っ！」"',

    # === 射精/股间+颜面 (lines ~346-391) ===
    r'CALL MESSAGE_BOX,@"「あぁ…♥ 接下来，请射在我的膣内吧……♥♥」"':
    r'CALL MESSAGE_BOX,@"「啊啊…♥ 接下来，请射在我的膣内吧……♥♥」"',

    r'CALL MESSAGE_BOX,@"「うぅ…… 虽然比直接射在里面好一点……」"':
    r'CALL MESSAGE_BOX,@"「呜…… 虽然比直接射在里面好一点……」"',

    r'CALL MESSAGE_BOX,@"「あ…もったいない…♥ …ん……ちゅる…♥」"':
    r'CALL MESSAGE_BOX,@"「啊…好浪费…♥ …嗯……啾噜…♥」"',

    r'CALL MESSAGE_BOX,@"「あぁ…♥ 喜欢用%PENIS_CALL()%把精液涂满我的脸……♥♥」"':
    r'CALL MESSAGE_BOX,@"「啊啊…♥ 喜欢用%PENIS_CALL()%把精液涂满我的脸……♥♥」"',

    r'CALL MESSAGE_BOX,@"「っ！……わざわざ顔に……うぅ……」"':
    r'CALL MESSAGE_BOX,@"「っ！……特意射在脸上……呜呜……」"',

    # === 射精/手淫 (lines ~401-404) ===
    r'CALL MESSAGE_BOX,@"「呀……！ %PENIS_CALL()%が暴れて……」"':
    r'CALL MESSAGE_BOX,@"「呀……！ %PENIS_CALL()%在乱动……」"',

    r'CALL MESSAGE_BOX,@"「ひっ…！ 手の中で脈打って…ビクビクして……」"':
    r'CALL MESSAGE_BOX,@"「咿っ…！ 在手里跳动着…一抖一抖的……」"',

    # === 射精/授乳手交 (lines ~419, 429) ===
    r'CALL MESSAGE_BOX,@"「呼嗬……♥♥ %SELF_CALL()%もぉ♥ 在胸部射奶精了呀……♥♥」"':
    r'CALL MESSAGE_BOX,@"「呼嗬……♥♥ %SELF_CALL()%也哦♥ 在胸部射奶精了呀……♥♥」"',

    # === 搾乳 section (lines ~444-642) ===
    r'CALL MESSAGE_BOX,@"「哎呀♥ 母乳が勝手に漏れてきて…♥♥\n　%SWEET_MASTER_CALL()%♥ 请原谅我这个不争气的家畜吧……♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「哎呀♥ 母乳擅自漏出来了…♥♥\n　%SWEET_MASTER_CALL()%♥ 请原谅我这个不争气的家畜吧……♥♥♥」"',

    r'CALL MESSAGE_BOX,@"「そんなぁ…♥ ミルクがぁ♥♥ 停不下来呢……♥♥」"':
    r'CALL MESSAGE_BOX,@"「不要啊…♥ 奶汁啊♥♥ 停不下来呢……♥♥」"',

    r'CALL MESSAGE_BOX,@"「はぁ♥♥ 已经空了呀……♥♥ 还在噗噗地流出来呢……♥♥」"':
    r'CALL MESSAGE_BOX,@"「哈啊♥♥ 已经空了呀……♥♥ 还在噗噗地流出来呢……♥♥」"',

    r'CALL MESSAGE_BOX,@"「あうぅ♥ 剩下的母乳正在噗噗地流出来……♥」"':
    r'CALL MESSAGE_BOX,@"「啊呜♥ 剩下的母乳正在噗噗地流出来……♥」"',

    r'CALL MESSAGE_BOX,@"「はうぅぅぅ♥♥ もっと強くぅ♥♥ ぼにゅう吸い尽くしてぇ♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「哈呜呜呜♥♥ 再用力点♥♥ 母乳吸干吧♥♥♥」"',

    r'CALL MESSAGE_BOX,@"「はふぅ…♥♥ 在给%MASTER_CALL()%哺乳时，会让我感到平静……♥♥」"':
    r'CALL MESSAGE_BOX,@"「哈呼…♥♥ 在给%MASTER_CALL()%哺乳时，会让我感到平静……♥♥」"',

    r'CALL MESSAGE_BOX,@"「ふぎぃっ♥♥ 搾乳狂いの淫乱おっぱい♥♥ ちゅぱちゅぱされてイぐぅっ♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「唔咿っ♥♥ 挤奶狂魔的淫乱奶子♥♥ 被啾啾吸着要去っ♥♥♥」"',

    r'CALL MESSAGE_BOX,@"「啊♥ あひぃっ♥ 挤奶真是太棒了……♥♥ んひいいぃぃぃっっっ♥♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「啊♥ 啊咿っ♥ 挤奶真是太棒了……♥♥ 嗯咿咿咿咿っっっ♥♥♥♥」"',

    r'CALL MESSAGE_BOX,@"「ほーっ♥ ほーっ♥ みるく搾りだされてぇ♥♥ 好舒服呀……♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「嚯ーっ♥ 嚯ーっ♥ 奶被挤出来了♥♥ 好舒服呀……♥♥♥」"',

    r'CALL MESSAGE_BOX,@"「おおぉぉっ♥♥ もうからっぽなのにぃ♥♥ ちくびアクメでミルク噴き出るぅっ♥♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「哦哦哦っ♥♥ 明明已经空了♥♥ 乳头绝顶又喷出奶了っ♥♥♥♥」"',

    r'CALL MESSAGE_BOX,@"「んひぃっ♥♥♥ もう限界ぃ♥♥ おっぱい絶頂させられて無理やり搾られるぅ♥♥」"':
    r'CALL MESSAGE_BOX,@"「嗯咿っ♥♥♥ 已经到极限了♥♥ 被弄到奶子绝顶又被强行挤奶♥♥」"',

    r'CALL MESSAGE_BOX,@"「ふあぁっ♥♥ もう全部吸い尽くされたのにぃ♥♥ 気持ち良すぎてまた出るぅっ♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「呼啊っ♥♥ 明明全被吸干了♥♥ 太舒服了又出来了っ♥♥♥」"',

    r'CALL MESSAGE_BOX,@"「らめっ♥ おっぱい絶頂しすぎてっ♥♥ 止まらな――んおぉぉっ♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「不要っ♥ 奶子绝顶过头了っ♥♥ 停不下来——唔哦哦っ♥♥♥」"',

    r'CALL MESSAGE_BOX,@"「ふおおぉぉっ♥♥ 機械で搾乳されてイっぐぅぅっ♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「呼哦哦哦っ♥♥ 被机器挤奶去去去っ♥♥♥」"',

    r'CALL MESSAGE_BOX,@"「あぁん♥♥ 被啾啾地吸着，真的太舒服了……♥♥」"':
    r'CALL MESSAGE_BOX,@"「啊嗯♥♥ 被啾啾地吸着，真的太舒服了……♥♥」"',

    r'CALL MESSAGE_BOX,@"「おっ♥ おっ♥ 搾乳でイくっ♥ %SELF_CALL()%は幸せな家畜でしゅうぅ♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「哦っ♥ 哦っ♥ 挤奶要去っ♥ %SELF_CALL()%是幸福的家畜呜呜♥♥♥」"',

    r'CALL MESSAGE_BOX,@"「んひぃぃぃいい♥♥ 乳首責められながら乳搾りなんてぇ♥♥ おっぱい馬鹿になるぅぅ♥」"':
    r'CALL MESSAGE_BOX,@"「嗯咿咿咿咿♥♥ 一边被责乳头一边挤奶什么的♥♥ 奶子要坏掉了♥」"',

    r'CALL MESSAGE_BOX,@"「あ゛っ♥ あ゛っ♥ おっぱいがぁっ♥ 触手に支配されてっ♥♥ んほおおおぉぉぉ♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「啊っ♥ 啊っ♥ 奶子啊っ♥ 被触手支配了っ♥♥ 唔嚯哦哦哦哦♥♥♥」"',

    r'CALL MESSAGE_BOX,@"「ひぐぅ♥ 交尾しながら搾乳しゅごいぃぃ♥♥ 自己是家畜的事实已经深深刻在脑海里了……♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「咿咕♥ 一边交尾一边挤奶好厉害♥♥ 自己是家畜的事实已经深深刻在脑海里了……♥♥♥」"',

    r'CALL MESSAGE_BOX,@"「おっ♥ おっ♥ 被%ANAL_CALL()%深入贯穿着……♥♥ 家畜的奶水被吸出来了……♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「哦っ♥ 哦っ♥ 被%ANAL_CALL()%深入贯穿着……♥♥ 家畜的奶水被吸出来了……♥♥♥」"',

    r'CALL MESSAGE_BOX,@"「んひぃ♥♥ おっぱいと%ANAL_CALL()%、両方でイくぅっ♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「嗯咿♥♥ 奶子和%ANAL_CALL()%、两边都要去っ♥♥♥」"',

    r'CALL MESSAGE_BOX,@"「はっ♥ 哈♥ おっぱいがぁ♥ 触手に凌辱されて母乳止まらないぃぃ♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「哈っ♥ 哈♥ 奶子啊♥ 被触手凌辱母乳停不下来♥♥♥」"',

    r'CALL MESSAGE_BOX,@"「あぁ…♥♥ 能直接成为%MASTER_CALL()%的魔力，真是……♥♥\n　这真是意外的喜悦……♥♥」"':
    r'CALL MESSAGE_BOX,@"「啊啊…♥♥ 能直接成为%MASTER_CALL()%的魔力，真是……♥♥\n　这真是意外的喜悦……♥♥」"',

    r'CALL MESSAGE_BOX,@"「ふわぁ♥ %SELF_CALL()%の魔力が溶けたミルク♥♥ 被夺走了呢……♥♥」"':
    r'CALL MESSAGE_BOX,@"「呼哇♥ %SELF_CALL()%的魔力融化的奶汁♥♥ 被夺走了呢……♥♥」"',

    r'CALL MESSAGE_BOX,@"「あぁ♥♥ 被啾啾地吸着，真的太舒服了……♥♥」"':
    r'CALL MESSAGE_BOX,@"「啊♥♥ 被啾啾地吸着，真的太舒服了……♥♥」"',

    r'CALL MESSAGE_BOX,@"「はぁ♥ 噗啊♥ %SELF_CALL()%の母乳♥ 被吸出来好多呢……♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「哈啊♥ 噗啊♥ %SELF_CALL()%的母乳♥ 被吸出来好多呢……♥♥♥」"',

    r'CALL MESSAGE_BOX,@"「あぁっ♥ %SWEET_MASTER_CALL()%っ♥♥ 情感溢出来了……♥♥ 哺乳高潮来了呢……♥♥」"':
    r'CALL MESSAGE_BOX,@"「啊っ♥ %SWEET_MASTER_CALL()%っ♥♥ 情感溢出来了……♥♥ 哺乳高潮来了呢……♥♥」"',

    r'CALL MESSAGE_BOX,@"「あ゛あぁ……♥♥ 勃起的乳头被吮吸着，真是忍受不了了……♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「啊啊啊……♥♥ 勃起的乳头被吮吸着，真是忍受不了了……♥♥♥」"',

    r'CALL MESSAGE_BOX,@"「啊♥ 啊♥ %MASTER_CALL()%に敏感ロリちくび吸われて絶頂しますぅぅ♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「啊♥ 啊♥ 被%MASTER_CALL()%吸着敏感的萝莉乳头要绝顶了♥♥♥」"',

    r'CALL MESSAGE_BOX,@"「はひぃっ…♥♥ 未成熟こどもおっぱいのくせに母乳吸われてイきますっ♥♥\n　ロリちくび勃起させて授乳アクメきめちゃいますぅっ♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「哈咿っ…♥♥ 明明是不成熟的儿童奶子却被吸母乳去っ♥♥\n　让萝莉乳头勃起来个哺乳绝顶っ♥♥♥」"',

    r'CALL MESSAGE_BOX,@"「はぁ♥ 噗啊♥ %SELF_CALL()%の母乳♥ 我被搾得很多呢♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「哈啊♥ 噗啊♥ %SELF_CALL()%的母乳♥ 我被搾得很多呢♥♥♥」"',

    r'CALL MESSAGE_BOX,@"「あぁぁぁ♥♥♥ 母乳が噴水みたいに♥♥ 明明很害羞却停不下来呢♥♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「啊啊啊♥♥♥ 母乳像喷泉一样♥♥ 明明很害羞却停不下来呢♥♥♥♥」"',

    r'CALL MESSAGE_BOX,@"「～～～っ♥♥♥ %MASTER_CALL()%强行搾奶真是太好了♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「～～～っ♥♥♥ %MASTER_CALL()%强行搾奶真是太好了♥♥♥」"',

    r'CALL MESSAGE_BOX,@"「啊♥ 你好♥ おっぱいみるくがぁ♥ 被吸得好舒服呢♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「啊♥ 你好♥ 奶子乳汁啊♥ 被吸得好舒服呢♥♥♥」"',

    r'CALL MESSAGE_BOX,@"「ああ♥♥ 機械とまんない♥ 搾奶永远不会结束呢♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「啊啊♥♥ 机器停不下来♥ 搾奶永远不会结束呢♥♥♥」"',

    r'CALL MESSAGE_BOX,@"「嗯啊♥ 搾乳と乳首責めを同時にされてぇ♥ 耐えられるわけにゃいぃぃ♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「嗯啊♥ 挤奶和乳首责同时进行♥ 怎么可能受得了♥♥♥」"',

    r'CALL MESSAGE_BOX,@"「ひぎぃ♥♥ おっぱい吸引と乳首ねぶりが一緒にぃぃ♥♥ ひああぁぁっ♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「咿咿♥♥ 奶子吸引和乳头舔弄一起来♥♥ 呼啊啊っ♥♥♥」"',

    r'CALL MESSAGE_BOX,@"「こ、こんなっ♥ 触手の搾乳乳首責めっ♥♥ 刺激つよすぎ、たえられなっ…ひっ……♥♥」"':
    r'CALL MESSAGE_BOX,@"「这、这样的っ♥ 触手的挤奶乳头责っ♥♥ 刺激太强了、受不了…咿っ……♥♥」"',

    r'CALL MESSAGE_BOX,@"「啊♥ 啊♥ %VAGINA_CALL()%も乳首もどっちもイって…♥♥\n　真是个不堪的母兽，抱歉……啊♥ 啊♥ あぁぁ～～っ♥」"':
    r'CALL MESSAGE_BOX,@"「啊♥ 啊♥ %VAGINA_CALL()%和乳头两边都去了…♥♥\n　真是个不堪的母兽，抱歉……啊♥ 啊♥ 啊啊～～っ♥」"',

    r'CALL MESSAGE_BOX,@"「んひぃ♥♥ おっぱいと%ANAL_CALL()%、両方でイくぅっ♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「嗯咿♥♥ 奶子和%ANAL_CALL()%、两边都要去っ♥♥♥」"',

    r'CALL MESSAGE_BOX,@"「あぁ…♥♥ %SELF_CALL()%的魔力成为了我爱%MASTER_CALL()%的养分…♥♥」"':
    r'CALL MESSAGE_BOX,@"「啊啊…♥♥ %SELF_CALL()%的魔力成为了我爱%MASTER_CALL()%的养分…♥♥」"',

    r'CALL MESSAGE_BOX,@"「あぁ…♥♥ %SELF_CALL()%的魔力与母乳一起被搾取了……♥♥」"':
    r'CALL MESSAGE_BOX,@"「啊啊…♥♥ %SELF_CALL()%的魔力与母乳一起被搾取了……♥♥」"',

    r'CALL MESSAGE_BOX,@"「あぅ…♥ 胸部的尖端开始麻麻的了……」"':
    r'CALL MESSAGE_BOX,@"「啊呜…♥ 胸部的尖端开始麻麻的了……」"',

    r'CALL MESSAGE_BOX,@"「あぁっ♥ そんなにしつこく吸われたら…♥♥ イ、イくっ♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「啊っ♥ 被那么执拗地吸的话…♥♥ 要、要去っ♥♥♥」"',

    r'CALL MESSAGE_BOX,@"「啊♥ 母乳がぁ♥ 我被挤了呢…♥」"':
    r'CALL MESSAGE_BOX,@"「啊♥ 母乳啊♥ 我被挤了呢…♥」"',

    r'CALL MESSAGE_BOX,@"「うぅぅ… 機械で搾乳されるなんてイヤなはずなのに…♥」"':
    r'CALL MESSAGE_BOX,@"「呜呜… 被机器挤奶明明应该讨厌的…♥」"',

    r'CALL MESSAGE_BOX,@"「あぁっ…出る……出るっ……んあぁぁ♥」"':
    r'CALL MESSAGE_BOX,@"「啊っ…出来……出来っ……嗯啊啊♥」"',

    r'CALL MESSAGE_BOX,@"「んやぁ♥♥ 胸部和%VAGINA_CALL()%都被随意玩弄到高潮了……♥」"':
    r'CALL MESSAGE_BOX,@"「咿呀♥♥ 胸部和%VAGINA_CALL()%都被随意玩弄到高潮了……♥」"',

    r'CALL MESSAGE_BOX,@"「んぅぅ…♥ むりやり母乳搾られて… とま…な…い……♥」"':
    r'CALL MESSAGE_BOX,@"「嗯呜…♥ 被强行挤奶… 停不下……来了……♥」"',

    r'CALL MESSAGE_BOX,@"「うあぁ♥ 挿入しながら搾乳なんて卑きょ、ものぉ♥♥」"':
    r'CALL MESSAGE_BOX,@"「呜啊♥ 一边插入一边挤奶什么的卑、卑鄙哦♥♥」"',

    r'CALL MESSAGE_BOX,@"「ひぎぃっ…♥ 竟然用触手强行给予快感……真是卑鄙……っ♥」"':
    r'CALL MESSAGE_BOX,@"「咿咿っ…♥ 竟然用触手强行给予快感……真是卑鄙……っ♥」"',

    r'CALL MESSAGE_BOX,@"「ぐうぅ… %SELF_CALL()%的魔力竟然在这种地方失去……」"':
    r'CALL MESSAGE_BOX,@"「咕呜… %SELF_CALL()%的魔力竟然在这种地方失去……」"',

    # === 抽出 (lines ~650-682) ===
    r'CALL MESSAGE_BOX,@"「んぎぃ♥ ひぎっ♥♥ イ、イくときにぃ♥♥ 从胸部喷涌而出的灵力……♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「嗯咿♥ 咿咿っ♥♥ 去、去的时候♥♥ 从胸部喷涌而出的灵力……♥♥♥」"',

    r'CALL MESSAGE_BOX,@"「んほぉ♥♥ %SWEET_MASTER_CALL()%♥♥ 请把我全部夺走……♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「嗯嚯♥♥ %SWEET_MASTER_CALL()%♥♥ 请把我全部夺走……♥♥♥」"',

    r'CALL MESSAGE_BOX,@"「ふぎぃっ♥♥ 请把%SELF_CALL()%变成适合家畜的无力母牛吧♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「唔咿っ♥♥ 请把%SELF_CALL()%变成适合家畜的无力母牛吧♥♥♥」"',

    r'CALL MESSAGE_BOX,@"「おぉっ♥♥ 对家畜来说灵力是无用的呢♥♥ 请尽情吸取我的资源吧♥♥」"':
    r'CALL MESSAGE_BOX,@"「哦っ♥♥ 对家畜来说灵力是无用的呢♥♥ 请尽情吸取我的资源吧♥♥」"',

    r'CALL MESSAGE_BOX,@"「あっ♥♥ あっ♥♥ %SELF_CALL()%和%MASTER_CALL()%の霊力が溶け合って…♥♥\n　あぁぁあっ♥ 幸せすぎてイっ……く……～～～～っ♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「啊っ♥♥ 啊っ♥♥ %SELF_CALL()%和%MASTER_CALL()%的灵力融合在一起…♥♥\n　啊啊啊っ♥ 太幸福了去……去……～～～～っ♥♥♥」"',

    r'CALL MESSAGE_BOX,@"「んあ゛ぁっ♥♥ 喷出来了♥ 一边喷涌灵力一边高潮呢♥♥」"':
    r'CALL MESSAGE_BOX,@"「嗯啊っ♥♥ 喷出来了♥ 一边喷涌灵力一边高潮呢♥♥」"',

    r'CALL MESSAGE_BOX,@"「嗯♥ ふぅ…♥ 请把%SELF_CALL()%的灵力全部夺走……♥」"':
    r'CALL MESSAGE_BOX,@"「嗯♥ 呼…♥ 请把%SELF_CALL()%的灵力全部夺走……♥」"',

    r'CALL MESSAGE_BOX,@"「くっ 停下……っ 霊力が奪われ……嗯♥」"':
    r'CALL MESSAGE_BOX,@"「切 停下……っ 灵力被夺走……嗯♥」"',

    # === 吸欧派 / 开始 (lines ~691-691) ===
    r'CALL MESSAGE_BOX,@"「さあ%MASTER_CALL()%♥ 请尽情饮用……♥♥」"':
    r'CALL MESSAGE_BOX,@"「来吧%MASTER_CALL()%♥ 请尽情饮用……♥♥」"',
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
        else:
            not_found.append(old[:60])

    with open(FPATH, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Batch 2 替换: {total}/{len(R)}")
    for nf in not_found:
        print(f"  ⚠️  {nf}")

if __name__ == "__main__":
    main()
