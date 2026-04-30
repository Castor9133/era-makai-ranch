#!/usr/bin/env python3
"""Simple fix: insert CASE "叫早" blocks into files that lost them."""

import sys

BASE = r"C:\Cursor local\era-makai-ranch\ERB\○口上\汎用口上"

# Content for each personality's 叫早 block (correctly indented)
WAKEUP_BLOCKS = {
    "仇恨口上1.ERB": """	CASE "叫早"
		SELECTCASE ARGS:2
		CASE "开始"
			IF CFLAG:乳牛 || CFLAG:洗脑 || ＃陷落状态／恋慕以上＃
				CALL MESSAGE_BOX,@"「……早上了。我恨你，但……（含入）……唔……别以为我会温柔……」"
				CALL MESSAGE_BOX,@"「……快点硬起来……虽然是恨你，但既然要做就做到位……」"
			ELSEIF ＃陷落状态／屈服以上＃
				CALL MESSAGE_BOX,@"「……一大早就要做这种事……你是不是有病……」"
				CALL MESSAGE_BOX,@"「……行了，别催……我做就是了……（咬牙切齿地张开嘴）……」"
			ELSE
				CALL MESSAGE_BOX,@"「……滚。我为什么要用嘴碰你……」"
				CALL MESSAGE_BOX,@"「……不做的话你要罚？哈……来吧，我会一口咬下去……」"
			ENDIF
		CASE "射精"
			IF CFLAG:乳牛 || CFLAG:洗脑 || ＃陷落状态／恋慕以上＃
				CALL MESSAGE_BOX,@"「……要出来了吗……哈……射吧……反正我也习惯了……♥」"
				CALL MESSAGE_BOX,@"「……别用那种得意的眼神看我……我恨你……♥」"
			ELSEIF ＃陷落状态／屈服以上＃
				CALL MESSAGE_BOX,@"「……快射……别磨蹭……我不想含太久……」"
			ELSE
				CALL MESSAGE_BOX,@"「……你敢射在我嘴里……我绝对杀了你……」"
			ENDIF
		CASE "继续"
			IF CFLAG:乳牛 || CFLAG:洗脑 || ＃陷落状态／恋慕以上＃
				CALL MESSAGE_BOX,@"「……咽下去了……恶心死了……但身体却习惯了……♥」"
				CALL MESSAGE_BOX,@"「……不许笑……我真想在你脸上留个印子……」"
			ELSEIF ＃陷落状态／屈服以上＃
				CALL MESSAGE_BOX,@"「……结束了是吧。我去漱口……别跟过来。」"
			ELSE
				CALL MESSAGE_BOX,@"「……咳……哈……我会记住这份屈辱的……你等着……」"
			ENDIF
		CASE "结束"
			IF CFLAG:乳牛 || CFLAG:洗脑 || ＃陷落状态／恋慕以上＃
				CALL MESSAGE_BOX,@"「……不射？你是在逗我吗……（嘴上这么说，眼里却闪过一丝不舍）」"
				CALL MESSAGE_BOX,@"「……随你便。反正下次还是得叫我起来的……」"
			ELSEIF ＃陷落状态／屈服以上＃
				CALL MESSAGE_BOX,@"「……不做了？算你识相……我走了。（迅速转身离开）」"
			ELSE
				CALL MESSAGE_BOX,@"「……不射了吗……算你还有半分人性……（狠狠瞪你一眼，快步离开）……」"
			ENDIF
		ENDSELECT""",

    "堅物口上1.ERB": """	CASE "叫早"
		SELECTCASE ARGS:2
		CASE "开始"
			IF CFLAG:乳牛 || CFLAG:洗脑 || ＃陷落状态／恋慕以上＃
				CALL MESSAGE_BOX,@"「晨间唤醒任务——用口腔执行。请勿乱动，确保作业效率。」"
				CALL MESSAGE_BOX,@"「（含入，抬眼看你）……温度正常。继续执行。」"
			ELSEIF ＃陷落状态／屈服以上＃
				CALL MESSAGE_BOX,@"「……口唇程序启动。别乱动，我会按规程完成。」"
			ELSE
				CALL MESSAGE_BOX,@"「……这不合规矩。用嘴叫你起床？我没签这份勤务。」"
			ENDIF
		CASE "射精"
			IF CFLAG:乳牛 || CFLAG:洗脑 || ＃陷落状态／恋慕以上＃
				CALL MESSAGE_BOX,@"「排出确认。接收完毕——数据记录：浓度偏高，建议增加饮水。」"
				CALL MESSAGE_BOX,@"「……不是刻意殷勤，只是例行汇报。」"
			ELSEIF ＃陷落状态／屈服以上＃
				CALL MESSAGE_BOX,@"「……排出确认。我去漱口，继续下一个勤务。」"
			ELSE
				CALL MESSAGE_BOX,@"「……咳……这种体液管理方式，严重违规……！」"
			ENDIF
		CASE "继续"
			IF CFLAG:乳牛 || CFLAG:洗脑 || ＃陷落状态／恋慕以上＃
				CALL MESSAGE_BOX,@"「吞咽完毕。口腔清洁度维持标准以上。希望这个报告让你满意。」"
				CALL MESSAGE_BOX,@"「……若有追加操作需求，随时提。」"
			ELSEIF ＃陷落状态／屈服以上＃
				CALL MESSAGE_BOX,@"「作业终了。我去做口腔清理，三分钟后恢复常规勤务。」"
			ELSE
				CALL MESSAGE_BOX,@"「……完毕。这份勤务……我不计入日志。（转身离开）」"
			ENDIF
		CASE "结束"
			IF CFLAG:乳牛 || CFLAG:洗脑 || ＃陷落状态／恋慕以上＃
				CALL MESSAGE_BOX,@"「未达排出标准。作业中止。是否需要切换其他唤醒方式？」"
				CALL MESSAGE_BOX,@"「……不是关心你。只是确保系统效率。」"
			ELSEIF ＃陷落状态／屈服以上＃
				CALL MESSAGE_BOX,@"「中止确认。我去处理下一个流程了。」"
			ELSE
				CALL MESSAGE_BOX,@"「……谢了。这活儿我干不来。下次用闹钟吧。」"
			ENDIF
		ENDSELECT""",

    "元気っ子口上1.ERB": """	CASE "叫早"
		SELECTCASE ARGS:2
		CASE "开始"
			IF CFLAG:乳牛 || CFLAG:洗脑 || ＃陷落状态／恋慕以上＃
				CALL MESSAGE_BOX,@"「早安——！叫醒服务上线！今天也使出全力让你舒服醒！」"
				CALL MESSAGE_BOX,@"「来，张嘴——哇，今天状态不错哦！我开动啦！」"
			ELSEIF ＃陷落状态／屈服以上＃
				CALL MESSAGE_BOX,@"「早、早上好……用嘴是吧，明白了……我做好觉悟了！」"
			ELSE
				CALL MESSAGE_BOX,@"「一大早就要？不是吧你——好啦好啦，我做还不行吗！」"
			ENDIF
		CASE "射精"
			IF CFLAG:乳牛 || CFLAG:洗脑 || ＃陷落状态／恋慕以上＃
				CALL MESSAGE_BOX,@"「来了来了！全部给我——唔唔！♥ 一大早就这么有精神，不愧是你！」"
				CALL MESSAGE_BOX,@"「咽下去啦！五星好评！明天也叫我！」"
			ELSEIF ＃陷落状态／屈服以上＃
				CALL MESSAGE_BOX,@"「快射吧！我快没气啦——唔……吞下去了。呼……搞定！」"
			ELSE
				CALL MESSAGE_BOX,@"「呜哇——别突然就……！嘴里全是……咳咳……坏死了！」"
			ENDIF
		CASE "继续"
			IF CFLAG:乳牛 || CFLAG:洗脑 || ＃陷落状态／恋慕以上＃
				CALL MESSAGE_BOX,@"「全部咽干净了！怎么样，今天的叫醒服务还满意不？再来一轮也行哦！」"
				CALL MESSAGE_BOX,@"「你要是还困，我就再含一会儿——反正我也没事做。」"
			ELSEIF ＃陷落状态／屈服以上＃
				CALL MESSAGE_BOX,@"「呼……任务完成！我去漱口啦，你自己也准备起床吧！」"
			ELSE
				CALL MESSAGE_BOX,@"「嘴里好奇怪……我去刷牙了！下次能不能换个正常方式叫我帮你啊！」"
			ENDIF
		CASE "结束"
			IF CFLAG:乳牛 || CFLAG:洗脑 || ＃陷落状态／恋慕以上＃
				CALL MESSAGE_BOX,@"「诶——不射吗？我嘴巴都准备好了的说……好吧好吧。」"
				CALL MESSAGE_BOX,@"「那抱一下总行吧？一大早就想黏着你。」"
			ELSEIF ＃陷落状态／屈服以上＃
				CALL MESSAGE_BOX,@"「哦，不做了？也好也好——我去准备早饭啦！」"
			ELSE
				CALL MESSAGE_BOX,@"「哇，不做了！好耶！我去洗脸了——你自己赖床吧！」"
			ENDIF
		ENDSELECT""",

    "天然口上1.ERB": """	CASE "叫早"
		SELECTCASE ARGS:2
		CASE "开始"
			IF CFLAG:乳牛 || CFLAG:洗脑 || ＃陷落状态／恋慕以上＃
				CALL MESSAGE_BOX,@"「……早安。用嘴叫你起来是吗？我看看……这样对吗？（歪头含入）」"
				CALL MESSAGE_BOX,@"「……那个，用不用先刷牙？顺序没搞错吧……？」"
			ELSEIF ＃陷落状态／屈服以上＃
				CALL MESSAGE_BOX,@"「……早上好。要做那个对吧……我、我记着步骤呢，一、二、三……」"
			ELSE
				CALL MESSAGE_BOX,@"「……诶？现在？可是天刚亮……好吧。张嘴是吗？……唔。」"
			ENDIF
		CASE "射精"
			IF CFLAG:乳牛 || CFLAG:洗脑 || ＃陷落状态／恋慕以上＃
				CALL MESSAGE_BOX,@"「唔……来了……咽下去……咕嘟。步骤完成了对不对？♥」"
				CALL MESSAGE_BOX,@"「那个味道……是今天的第一个记忆呢。」"
			ELSEIF ＃陷落状态／屈服以上＃
				CALL MESSAGE_BOX,@"「唔唔……咽下去了。这个步骤也记下了。」"
			ELSE
				CALL MESSAGE_BOX,@"「咳咳……好多……步骤里没写这个量……嘴里好烫……」"
			ENDIF
		CASE "继续"
			IF CFLAG:乳牛 || CFLAG:洗脑 || ＃陷落状态／恋慕以上＃
				CALL MESSAGE_BOX,@"「咽下去了。暖暖的。接下来是……洗脸？还是先抱一会儿？」"
				CALL MESSAGE_BOX,@"「今天的步骤表，你帮我看看有没有漏掉什么。」"
			ELSEIF ＃陷落状态／屈服以上＃
				CALL MESSAGE_BOX,@"「做完了。步骤打勾。还有别的吗？」"
			ELSE
				CALL MESSAGE_BOX,@"「嘴里还有味道……不过没事。接下来做什么？顺序我一搞混就慌。」"
			ENDIF
		CASE "结束"
			IF CFLAG:乳牛 || CFLAG:洗脑 || ＃陷落状态／恋慕以上＃
				CALL MESSAGE_BOX,@"「咦，没射？那我是不是步骤做错了……但你说停的话，我就停。」"
				CALL MESSAGE_BOX,@"「下次我再好好学一遍步骤。今天先这样——起来吧？」"
			ELSEIF ＃陷落状态／屈服以上＃
				CALL MESSAGE_BOX,@"「不做了？好……步骤中止。我去看看早饭好了没。」"
			ELSE
				CALL MESSAGE_BOX,@"「结束了？太好了……步骤太长了我会忘。（松了口气）」"
			ENDIF
		ENDSELECT""",

    "大和抚子口上1.ERB": """	CASE "叫早"
		SELECTCASE ARGS:2
		CASE "开始"
			IF CFLAG:乳牛 || CFLAG:洗脑 || ＃陷落状态／恋慕以上＃
				CALL MESSAGE_BOX,@"「……早安，夫君大人。妾身用这副样子来唤您……若能让您心情好些，便不算辱没了礼数。请别嫌妾身笨拙……」"
			ELSEIF ＃陷落状态／屈服以上＃
				CALL MESSAGE_BOX,@"「……晨安。妾身明白今日的差事了……请、请容妾身……领受。」"
			ELSE
				CALL MESSAGE_BOX,@"「请、请不要这样……晨起便行此事……实在不合礼法……妾身不能……」"
			ENDIF
		CASE "射精"
			IF CFLAG:乳牛 || CFLAG:洗脑 || ＃陷落状态／恋慕以上＃
				CALL MESSAGE_BOX,@"「……唔……嗯……♥ 请尽数交付于妾身……妾身会一滴不剩地咽下……这是身为侍女的荣幸……♥」"
			ELSEIF ＃陷落状态／屈服以上＃
				CALL MESSAGE_BOX,@"「……呜……恳请您……快些结束……妾身……有些撑不住了……」"
			ELSE
				CALL MESSAGE_BOX,@"「咳……不……不要……呜呜……求您……住手……」"
			ENDIF
		CASE "继续"
			IF CFLAG:乳牛 || CFLAG:洗脑 || ＃陷落状态／恋慕以上＃
				CALL MESSAGE_BOX,@"「……哈……夫君大人的气味……妾身会铭记于心。今日也请让妾身侍奉左右……只愿您眉间舒展。」"
			ELSEIF ＃陷落状态／屈服以上＃
				CALL MESSAGE_BOX,@"「……既然已了……妾身可以退下了么。请容我整理仪容。」"
			ELSE
				CALL MESSAGE_BOX,@"「……太过了……请、请不要再施这等羞辱……妾身至少想留些体面。」"
			ENDIF
		CASE "结束"
			IF CFLAG:乳牛 || CFLAG:洗脑 || ＃陷落状态／恋慕以上＃
				CALL MESSAGE_BOX,@"「……没能让您尽兴么。妾身修行不足，深感惭愧……明日定当加倍用心，请再给妾身机会。」"
			ELSEIF ＃陷落状态／屈服以上＃
				CALL MESSAGE_BOX,@"「……呼……万幸。妾身告退……请您好生歇息。」"
			ELSE
				CALL MESSAGE_BOX,@"「……总算……谢您手下留情。妾身……先行告退。」"
			ENDIF
		ENDSELECT""",

    "懦弱口上1.ERB": """	CASE "叫早"
		SELECTCASE ARGS:2
		CASE "开始"
			IF CFLAG:乳牛 || CFLAG:洗脑 || ＃陷落状态／恋慕以上＃
				CALL MESSAGE_BOX,@"「……%MASTER_CALL()%、早安……。%SELF_CALL()%、会用嘴……叫醒您的……请、请别嫌弃……」"
				CALL MESSAGE_BOX,@"「……%SELF_CALL()%、轻轻地……含进去……别、别嫌%SELF_CALL()%笨……」"
			ELSEIF ＃陷落状态／屈服以上＃
				CALL MESSAGE_BOX,@"「……要、要用嘴吗……。%SELF_CALL()%、会做的……求您……别太用力……」"
				CALL MESSAGE_BOX,@"「……知道了……%SELF_CALL()%张嘴就是……别、别催……」"
			ELSE
				CALL MESSAGE_BOX,@"「……不、不要……。一大早就……求您、放过%SELF_CALL()%吧……」"
				CALL MESSAGE_BOX,@"「……呜……%SELF_CALL()%还没准备好……好怕……」"
			ENDIF
		CASE "射精"
			IF CFLAG:乳牛 || CFLAG:洗脑 || ＃陷落状态／恋慕以上＃
				CALL MESSAGE_BOX,@"「……呜……♥ 请、请射在%SELF_CALL()%嘴里……%SELF_CALL()%、会全部接住的……♥」"
				CALL MESSAGE_BOX,@"「……是、是%MASTER_CALL()%的味道……%SELF_CALL()%、好幸福……♥」"
			ELSEIF ＃陷落状态／屈服以上＃
				CALL MESSAGE_BOX,@"「……快、快点……。%SELF_CALL()%、快撑不住了……求您快点……」"
				CALL MESSAGE_BOX,@"「……呜……喉咙好酸……%SELF_CALL()%快……」"
			ELSE
				CALL MESSAGE_BOX,@"「……呜……别、别射在嘴里……求您……好脏……」"
				CALL MESSAGE_BOX,@"「……不要……%SELF_CALL()%、想吐……喉咙好难受……」"
			ENDIF
		CASE "继续"
			IF CFLAG:乳牛 || CFLAG:洗脑 || ＃陷落状态／恋慕以上＃
				CALL MESSAGE_BOX,@"「……还、还在颤……♥ %SELF_CALL()%、嘴里全都是……好幸福……♥」"
				CALL MESSAGE_BOX,@"「……可以、再含一会儿吗……%SELF_CALL()%、不想松开……♥」"
			ELSEIF ＃陷落状态／屈服以上＃
				CALL MESSAGE_BOX,@"「……已经、射完了……可以……让%SELF_CALL()%停下了吗……」"
				CALL MESSAGE_BOX,@"「……嘴里黏糊糊的……%SELF_CALL()%、想去漱口……」"
			ELSE
				CALL MESSAGE_BOX,@"「……恶心……%SELF_CALL()%、想吐……嘴里全是那个味道……」"
				CALL MESSAGE_BOX,@"「……别、别看了……%SELF_CALL()%这样子……好丢脸……」"
			ENDIF
		CASE "结束"
			IF CFLAG:乳牛 || CFLAG:洗脑 || ＃陷落状态／恋慕以上＃
				CALL MESSAGE_BOX,@"「……没、没射吗……？%SELF_CALL()%、哪里做得不好……？下次一定更乖……」"
				CALL MESSAGE_BOX,@"「……%MASTER_CALL()%是不是、嫌弃%SELF_CALL()%了……？%SELF_CALL()%会改的……别丢下%SELF_CALL()%……」"
			ELSEIF ＃陷落状态／屈服以上＃
				CALL MESSAGE_BOX,@"「……没射、就……太好了……%SELF_CALL()%、可以走了吗……」"
				CALL MESSAGE_BOX,@"「……呼……幸好……%SELF_CALL()%、还以为又要……」"
			ELSE
				CALL MESSAGE_BOX,@"「……没、没射……？谢、谢谢……%SELF_CALL()%……得救了……」"
				CALL MESSAGE_BOX,@"「……赶紧走、赶紧走……不然又要反悔的……」"
			ENDIF
		ENDSELECT""",
}


def fix_file(filename):
    filepath = BASE + "\\" + filename
    block = WAKEUP_BLOCKS[filename]

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find insertion point: after 调教's ENDSELECT, before CASE "探索魔界"
    # Pattern: \t\tENDSELECT\n\tCASE "探索魔界"
    target = '\t\tENDSELECT\n\tCASE "探索魔界"'
    replacement = '\t\tENDSELECT\n' + block + '\n\tCASE "探索魔界"'

    if target not in content:
        print(f"  ERROR: {filename}: pattern not found")
        # Try alternative: ENDSELECT followed by CASEELSE or ENDSELECT
        for alt_pattern in ['\t\tENDSELECT\n\tCASEELSE', '\t\tENDSELECT\n\tENDSELECT']:
            if alt_pattern in content:
                alt_replacement = '\t\tENDSELECT\n' + block + '\n\t' + alt_pattern.split('\n\t')[1]
                content = content.replace(alt_pattern, alt_replacement, 1)
                print(f"  FIXED (alt): {filename}")
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                return True
        return False

    content = content.replace(target, replacement, 1)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  FIXED: {filename}")
    return True


def fix_renqi():
    """Remove duplicate CASE "叫早" from 人妻口上1.ERB - keep the one at correct level."""
    filepath = BASE + "\\人妻口上1.ERB"
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Count occurrences
    count = content.count('CASE "叫早"')
    if count <= 1:
        print(f"  SKIP: 人妻口上1.ERB has {count} 叫早, no fix needed")
        return

    # The correct叫早 is at the right level (after ENDSELECT, before 探索魔界)
    # Find the one that's nested (preceded by another CASE inside 调教) and remove it
    lines = content.split('\n')
    new_lines = []
    skip_until_ends = False
    skip_depth = 0
    found_nested = False

    for i, line in enumerate(lines):
        if not found_nested and line.strip().startswith('CASE "叫早"') and line.startswith('\t\tCASE'):
            # This is the nested one (2-tab indent, inside 调教)
            found_nested = True
            skip_until_ends = True
            skip_depth = 0
            continue

        if skip_until_ends:
            if line.lstrip('\t').startswith('ENDSELECT'):
                if skip_depth == 0:
                    skip_until_ends = False
                    continue
                else:
                    skip_depth -= 1
                    continue
            elif line.lstrip('\t').startswith('SELECTCASE'):
                skip_depth += 1
                continue
            continue

        new_lines.append(line)

    if found_nested:
        content = '\n'.join(new_lines)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  FIXED: 人妻口上1.ERB - removed duplicate 叫早")
    else:
        print(f"  ERROR: 人妻口上1.ERB - couldn't find nested 叫早")


def main():
    print("=== Fixing missing 叫早 blocks ===")
    for filename in WAKEUP_BLOCKS:
        fix_file(filename)

    print("\n=== Fixing duplicate 叫早 in 人妻 ===")
    fix_renqi()

    print("\nDone!")

if __name__ == "__main__":
    main()
