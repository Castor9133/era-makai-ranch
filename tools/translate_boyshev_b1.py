#!/usr/bin/env python3
"""ボーイッシュ口上1_イベント・魔界入り.ERB — 完整翻译"""
import sys
sys.stdout = open(1, 'w', encoding='utf-8', closefd=False)

FPATH = r"C:\Cursor local\era-makai-ranch\ERB\○口上\汎用口上\ボーイッシュ口上1_イベント・魔界入り.ERB"

R = {
    # === 进入魔界的 (lines 31-71) ===
    r'CALL MESSAGE_BOX,@"「ここが魔界か……もっと荒れ放題なトコだと思ってたんだけどな」"':
    r'CALL MESSAGE_BOX,@"「这里就是魔界吗……我还以为会是更荒凉的地方呢」"',
    r'CALL MESSAGE_BOX,@"「近くの【魔界水晶】は採り尽くされてるみたいだな…」\n「まあそう簡単にはいかないか……気ぃ付けていかないと」"':
    r'CALL MESSAGE_BOX,@"「附近的【魔界水晶】好像被采光了…」\n「嘛，没那么简单吧……得小心点才行」"',
    r'CALL MESSAGE_BOX,@"「ここが魔界か……思ってたより草木が多いんだな…」"':
    r'CALL MESSAGE_BOX,@"「这里就是魔界吗……比想象中草木要多啊…」"',
    r'CALL MESSAGE_BOX,@"「近くの【魔界植物】は採り尽くされてるみたいだな…」\n「まあそう簡単にはいかないか……気ぃ付けていかないと」"':
    r'CALL MESSAGE_BOX,@"「附近的【魔界植物】好像被采光了…」\n「嘛，没那么简单吧……得小心点才行」"',
    r'CALL MESSAGE_BOX,@"「ここが魔界か……バケモンがうろついてるトコにしちゃ平和な感じだな…」"':
    r'CALL MESSAGE_BOX,@"「这里就是魔界吗……作为怪物出没的地方来说还挺和平的…」"',
    r'CALL MESSAGE_BOX,@"（死んでも助けてやるからな…っ）\n「頼むから無事でいてくれよ……！」"':
    r'CALL MESSAGE_BOX,@"（就算拼了命也会救你的…っ）\n「拜托了请平安无事啊……！」"',
    r'CALL MESSAGE_BOX,@"「ここが魔界か……思ったより落ち着いたトコなんだな…」"':
    r'CALL MESSAGE_BOX,@"「这里就是魔界吗……比想象中要安分的地方啊…」"',
    r'CALL MESSAGE_BOX,@"「つっても魔界には違いないし、名を上げるのに不足なし…だな」\n（城の向こうの『あれ』には絶対に近寄りたくねえけど…）"':
    r'CALL MESSAGE_BOX,@"「不过说到底还是魔界，用来扬名立万足够了…」\n（但城堡那边的『那个』我绝对不想靠近…）"',
    r'CALL MESSAGE_BOX,@"「……っ！ ……ここは…？ %SELF_CALL()%、もしかして魔界に……！？」"':
    r'CALL MESSAGE_BOX,@"「……っ！ ……这里是…？ %SELF_CALL()%、难道说在魔界……！？」"',
    r'CALL MESSAGE_BOX,@"「どうしたもんかな…… まさか頼れるトコなんかあるはずないし……」"':
    r'CALL MESSAGE_BOX,@"「怎么办才好……反正也不可能有能依靠的地方……」"',
    r'CALL MESSAGE_BOX,@"「それでも街っぽい所はあるみたいだ…」\n「話せばなんとかなるかも……いや、それは甘いかぁ…？ でもなぁ…」"':
    r'CALL MESSAGE_BOX,@"「不过好像有像是城镇的地方…」\n「说不定说说话就能解决……不，那也太天真了…？ 不过嘛…」"',
    r'CALL MESSAGE_BOX,@"「ここが魔界か……とうとう魔族どもの土地に着いたな…」"':
    r'CALL MESSAGE_BOX,@"「这里就是魔界吗……终于踏上魔族的土地了…」"',
    r'CALL MESSAGE_BOX,@"「ヤツらの親玉はあの城にいるんだろうな……うし、行くか…！」"':
    r'CALL MESSAGE_BOX,@"「他们的老大应该在那座城堡里吧……好，走吧…！」"',
    r'CALL MESSAGE_BOX,@"「ここが魔界か……瘴気に満ちた土地とかって噂はデタラメじゃねえか」"':
    r'CALL MESSAGE_BOX,@"「这里就是魔界吗……说什么瘴气弥漫的土地，果然是谣言吧」"',
    r'CALL MESSAGE_BOX,@"「うっし、%SELF_CALL()%の力を見せつけてやるぜ…！」"':
    r'CALL MESSAGE_BOX,@"「好嘞，让%SELF_CALL()%展示一下实力…！」"',
    r'CALL MESSAGE_BOX,@"（ちっ…正直ナメてたぜ… 精鋭連中はザコとは段違いじゃんかよ…っ）"':
    r'CALL MESSAGE_BOX,@"（切…说实话我小看他们了…精英和杂鱼根本不是一个级别啊…っ）"',
    r'CALL MESSAGE_BOX,@"（期待してなかった【処女結界】に、結局守られちまった…）\n「でも、そしたらなんでコイツら%SELF_CALL()%を殺さないんだ…？」"':
    r'CALL MESSAGE_BOX,@"（没想到被不抱期待的【处女结界】保护了…）\n「可是，那他们为什么不杀%SELF_CALL()%呢…？」"',
    r'CALL MESSAGE_BOX,@"（ニンゲンを売り買いするなんてよ……やっぱ魔界の連中は許せねえ…）"':
    r'CALL MESSAGE_BOX,@"（竟然买卖人类……果然魔界的家伙不可原谅…）"',
    r'CALL MESSAGE_BOX,@"「……ん？…ここドコだ…？」"':
    r'CALL MESSAGE_BOX,@"「……嗯？…这里是哪儿…？」"',
    r'CALL MESSAGE_BOX,@"「見たことない景色……ていうか映画のセットみたいだな…」"':
    r'CALL MESSAGE_BOX,@"「没见过的景色……倒像是电影布景啊…」"',
    r'CALL MESSAGE_BOX,@"「あっちに見えるのは街…？ 話通じるんだろうな…」"':
    r'CALL MESSAGE_BOX,@"「那边能看到的是城镇…？ 能沟通吧…」"',

    # === 事件/领取奴隶 (lines 86-90) ===
    r'CALL MESSAGE_BOX,@"「ひっ……あ、あんな目にあわせて…今度は奴隷…？」"':
    r'CALL MESSAGE_BOX,@"「咿……让、让我经历那种遭遇……这次是奴隶…？」"',
    r'CALL MESSAGE_BOX,@"「…こ、ここは牧場…？」"':
    r'CALL MESSAGE_BOX,@"「…这、这里是牧场…？」"',
    r'CALL MESSAGE_BOX,@"「…こんなトコまで連れてきて何させるつもりだよ…」"':
    r'CALL MESSAGE_BOX,@"「…把我带到这种地方来想让我干什么啊…」"',
    r'CALL MESSAGE_BOX,@"「…今すぐ解放しろって言ってるだろ……っ」"':
    r'CALL MESSAGE_BOX,@"「…我说了快放了我……っ」"',

    # === 事件/母乳体质化 (lines 95-97) ===
    r'CALL MESSAGE_BOX,@"「へへ…♥ これからは%MASTER_CALL()%のために母乳が出せんだな…♥」"':
    r'CALL MESSAGE_BOX,@"「嘿嘿…♥ 以后就能为%MASTER_CALL()%出奶了啊…♥」"',
    r'CALL MESSAGE_BOX,@"「あ、あぁ… こんなこと、あってたまるか…」"':
    r'CALL MESSAGE_BOX,@"「啊、啊啊… 这种事，怎么可能发生…」"',

    # === 事件/魔力母乳体质化 (lines 102-104) ===
    r'CALL MESSAGE_BOX,@"「んぁ…魔力が流れ出してく……さてはとことん搾取するつもりだな…♥」"':
    r'CALL MESSAGE_BOX,@"「嗯啊…魔力在往外流……你这是打算彻底榨取啊…♥」"',
    r'CALL MESSAGE_BOX,@"「っ！？ 魔力が抜けて…っ %SELF_CALL()%の胸に何したんだよ……！？」"':
    r'CALL MESSAGE_BOX,@"「っ！？ 魔力在流失…っ 你对%SELF_CALL()%的胸做了什么……！？」"',

    # === 事件/超乳化 (lines 109-113) ===
    r'CALL MESSAGE_BOX,@"「啊♥ こんな乳牛らしい身体にしてもらえて感動だ…♥♥」\n「これからは『おっぱい家畜』として一生飼ってくれるんだよな♥♥」"':
    r'CALL MESSAGE_BOX,@"「啊♥ 能被赐予这么像奶牛的身体太感动了…♥♥」\n「以后会作为『奶子家畜』养我一辈子的对吧♥♥」"',
    r'CALL MESSAGE_BOX,@"「ふあぁ…♥ こんなどうしようもない胸にされちまったぁ♥♥」\n「もう%MASTER_CALL()%のおっぱい奴隷としてしか生きらんねぇ…♥♥」"':
    r'CALL MESSAGE_BOX,@"「呼啊…♥ 被弄成了这么无可救药的胸部♥♥」\n「已经只能作为%MASTER_CALL()%的奶子奴隶活下去了…♥♥」"',
    r'CALL MESSAGE_BOX,@"「なっ…あぁ……こんな…う、嘘だ……っ」\n「%SELF_CALL()%の身体、元に戻してくれよぉ…！」"':
    r'CALL MESSAGE_BOX,@"「什么…啊啊……这种…骗、骗人的吧……っ」\n「把%SELF_CALL()%的身体、变回来啊…！」"',

    # === 事件/崩坏 (lines 120-128) ===
    r'CALL MESSAGE_BOX,@"（あ…あ…%MASTER_CALL()%に……こわされ……）"':
    r'CALL MESSAGE_BOX,@"（啊…啊…被%MASTER_CALL()%……弄坏……）"',
    r'CALL MESSAGE_BOX,@"（もう……なにもかも…どうでも……ひひっ……）"':
    r'CALL MESSAGE_BOX,@"（已经……一切都…无所谓了……嘻嘻……）"',
    r'CALL MESSAGE_BOX,@"「あっ…が……%MASTER_CALL()%……ゆ、許し……ぃ…」"':
    r'CALL MESSAGE_BOX,@"「啊っ…咳……%MASTER_CALL()%……饶、饶了我……」"',
    r'CALL MESSAGE_BOX,@"「あぁ……あ…ぁ……っ…？」"':
    r'CALL MESSAGE_BOX,@"「啊啊……啊…啊……っ…？」"',

    # === 事件/反抗消除 (lines 135-137) ===
    r'CALL MESSAGE_BOX,@"（ここには誰も助けになんか来ない…っ 怖い…苦しい…っ）\n（反抗しないから…許してくれ…いや、許してください…っ！）"':
    r'CALL MESSAGE_BOX,@"（这里谁都不会来救我…っ 好可怕…好痛苦…っ）\n（我不会反抗了…饶了我吧…不、请饶了我…っ！）"',
    r'CALL MESSAGE_BOX,@"（怖い……こんなのが続くと、そのうち壊される…）\n「に、二度と逆らったりしないから…お願いです…許してください…」"':
    r'CALL MESSAGE_BOX,@"（好可怕……这样继续下去的话，迟早会被弄坏…）\n「我、我再也不敢反抗了…求您了…请饶了我…」"',

    # === 事件/屈服 (lines 143-145) ===
    r'CALL MESSAGE_BOX,@"（どんな命令でも聞くからっ…ここから出してくれ…っ）"':
    r'CALL MESSAGE_BOX,@"（我什么命令都会听的…放我出去吧…っ）"',
    r'CALL MESSAGE_BOX,@"「はっ…ぐ…%SELF_CALL()%齿%MASTER_CALL()%のドレイです…」\n「……っ どんなことでも、言うこと聞きます…」"':
    r'CALL MESSAGE_BOX,@"「哈…呜…%SELF_CALL()%是%MASTER_CALL()%的奴隶…」\n「……っ 什么事我都会照办的…」"',

    # === 事件/陷落 (lines 151-153) ===
    r'CALL MESSAGE_BOX,@"（あぁ…地獄みたいな思いをしてようやく分かったよ…）\n（%SELF_CALL()%はコイツには逆らったり出来ないんだな…）"':
    r'CALL MESSAGE_BOX,@"（啊啊…经历了地狱般的遭遇终于明白了…）\n（%SELF_CALL()%是没办法违抗这家伙的啊…）"',
    r'CALL MESSAGE_BOX,@"「なあ…%MASTER_CALL()%のこととか、いろいろ教えてくれよ…」\n「べ、別に少しは上手く立ち回ろうってだけだっての……」"':
    r'CALL MESSAGE_BOX,@"「喂…%MASTER_CALL()%的事情什么的，多教教我吧…」\n「又、又不是别的意思，只是想稍微好好相处而已……」"',

    # === 事件/恋慕告白 (lines 159-161) ===
    r'CALL MESSAGE_BOX,@"「な、なぁ…%MASTER_CALL()%は…誰かを好きになったこととか、あんのか…？」\n「いや、なんつーのかな……ちょっと気になってるヤツがいて……その…」"':
    r'CALL MESSAGE_BOX,@"「那、那个…%MASTER_CALL()%有…喜欢过谁吗…？」\n「不、该怎么说呢……有个在意的人……那个…」"',
    r'CALL MESSAGE_BOX,@"「そ、その…%MASTER_CALL()%に…ほ、ほ、惚れちまったみたいなんだ…っ♥」\n「迷惑かけたりはしないから……ただ、そばにさせてほしい…♥」"':
    r'CALL MESSAGE_BOX,@"「那、那个…我好像…喜、喜、喜欢上%MASTER_CALL()%了…っ♥」\n「我不会给你添麻烦的……只、只是让我待在你身边…♥」"',

    # === 事件/隶属告白 (lines 167-169) ===
    r'CALL MESSAGE_BOX,@"「%SWEET_MASTER_CALL()%…♥ %SELF_CALL()%さ、こんなに幸せにしてもらって、ほんと感謝してるんだ…♥♥」\n「それで%MASTER_CALL()%にどうやってお礼すればいいか考えたんだけど…♥♥」"':
    r'CALL MESSAGE_BOX,@"「%SWEET_MASTER_CALL()%…♥ %SELF_CALL()%啊，被你弄得这么幸福，真的很感谢…♥♥」\n「所以我想着该怎么报答%MASTER_CALL()%才好…♥♥」"',
    r'CALL MESSAGE_BOX,@"「%SELF_CALL()%にはこの身体くらいしかなくて……だったら『全部』あげちゃえばいいなって♥♥」\n「なるべく壊れないようにがんばるから…♥♥ いっぱい使ってくれよなっ♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「%SELF_CALL()%也只有这副身体了……那不如把『全部』都给你♥♥」\n「我会尽量不让自己坏掉的…♥♥ 好好多用用我吧っ♥♥♥」"',

    # === 事件/乳牛堕落 (lines 175-177) ===
    r'CALL MESSAGE_BOX,@"（あぁ♥ きもちいい…しあわせ…♥ 今までの人生でこんな幸せなことなかった…♥）\n（もう『人生』なんていらない…♥♥ これからは乳牛として幸せに生きてく…♥♥）"':
    r'CALL MESSAGE_BOX,@"（啊啊♥ 好舒服…好幸福…♥ 以前的人生从没有这么幸福过…♥）\n（已经不想要『人生』了…♥♥ 以后要作为奶牛幸福地活下去…♥♥）"',
    r'CALL MESSAGE_BOX,@"「あぁ～…♥♥ きもちいい♥ きもちいい♥ おっぱいきもちいいっ…！♥」\n「搾乳アクメの気持ちよさを、身体の芯まで刻み込まれちまった…♥」\n「乳牛として飼われる幸せを知っちまったら、もう人間になんて戻れない…♥♥」"':
    r'CALL MESSAGE_BOX,@"「啊啊～…♥♥ 好舒服♥ 好舒服♥ 奶子好舒服っ…！♥」\n「挤奶绝顶的舒服，被刻进了身体深处…♥」\n「一旦知道了被当作奶牛饲养的幸福，就再也回不去人类了…♥♥」"',

    # === 事件/处女结界破坏 (lines 184-186) ===
    r'CALL MESSAGE_BOX,@"「これまで%SELF_CALL()%を守ってくれた結界も、もう要らなくなったなぁ…♥♥」\n\d"':
    r'CALL MESSAGE_BOX,@"「至今为止保护%SELF_CALL()%的结界，也已经不需要了啊…♥♥」\n\d"',
    r'CALL MESSAGE_BOX,@"「…っ！ 結界が壊れる……なんでだ…！？」"':
    r'CALL MESSAGE_BOX,@"「…っ！ 结界在崩溃……为什么…！？」"',

    # === 事件/处女丧失前 (lines 193-231) ===
    r'CALL MESSAGE_BOX,@"「あぅ…拘束されたまま初体験なんて♥ ちょっと怖いけど、それ以上に興奮してきた…♥」"':
    r'CALL MESSAGE_BOX,@"「啊呜…被束缚着初体验什么的♥ 虽然有点害怕，但更兴奋了…♥」"',
    r'CALL MESSAGE_BOX,@"「あぅ…目隠しされたまま初体験なんて♥ ちょっと怖いけど、それ以上に興奮してきた…♥」"':
    r'CALL MESSAGE_BOX,@"「啊呜…被蒙着眼初体验什么的♥ 虽然有点害怕，但更兴奋了…♥」"',
    r'CALL MESSAGE_BOX,@"「あぁ…♥ %SELF_CALL()%の処女、%MASTER_CALL()%が貰ってくれるんだな…♥♥」"':
    r'CALL MESSAGE_BOX,@"「啊啊…♥ %SELF_CALL()%的处女，%MASTER_CALL()%会收下啊…♥♥」"',
    r'CALL MESSAGE_BOX,@"「%MASTER_CALL()%…？ 目隠しでよくわかんねぇけど…も、もしかして…♥」"':
    r'CALL MESSAGE_BOX,@"「%MASTER_CALL()%…？ 蒙着眼看不太清…难、难道说…♥」"',
    r'CALL MESSAGE_BOX,@"「啊咿嘻…♥ %SELF_CALL()%の処女、こんなモンに奪われるのかよ…♥♥」"':
    r'CALL MESSAGE_BOX,@"「啊咿嘻…♥ %SELF_CALL()%的处女，要被这种东西夺走吗…♥♥」"',
    r'CALL MESSAGE_BOX,@"「あぁ…♥ 初めての相手は絶対に%MASTER_CALL()%だって決めてた…♥♥」"':
    r'CALL MESSAGE_BOX,@"「啊啊…♥ 我早就决定了第一次一定要给%MASTER_CALL()%…♥♥」"',
    r'CALL MESSAGE_BOX,@"「あぁ…♥ 目隠しするなら、せめて抱きしめながらシてくれ…♥♥\n　%MASTER_CALL()%の存在を感じてたいよ…♥♥」"':
    r'CALL MESSAGE_BOX,@"「啊啊…♥ 要蒙眼的话，至少抱着我做吧…♥♥\n　我想感受%MASTER_CALL()%的存在…♥♥」"',
    r'CALL MESSAGE_BOX,@"「啊♥ %MASTER_CALL()%…♥ この時が来たんだな…♥♥」"':
    r'CALL MESSAGE_BOX,@"「啊♥ %MASTER_CALL()%…♥ 这一刻终于来了啊…♥♥」"',
    r'CALL MESSAGE_BOX,@"「そんな……初めては%MASTER_CALL()%が貰ってくれるんじゃ……っ」"':
    r'CALL MESSAGE_BOX,@"「怎么会……第一次不是应该由%MASTER_CALL()%来收下的吗……っ」"',
    r'CALL MESSAGE_BOX,@"「あぁ…てっきり初めては%MASTER_CALL()%が貰ってくれるって……\n　い、いや…%MASTER_CALL()%がしたいならそれで……」"':
    r'CALL MESSAGE_BOX,@"「啊啊…我还以为第一次一定是由%MASTER_CALL()%来收下……\n　不、不过…%MASTER_CALL()%想的话那就这样吧……」"',
    r'CALL MESSAGE_BOX,@"「い、嫌だ…っ それだけは…頼むからぁ…っ！ やめろぉっ！」"':
    r'CALL MESSAGE_BOX,@"「不、不要…っ 只有那个…求你了…っ！ 住手啊っ！」"',
    r'CALL MESSAGE_BOX,@"「う……いつかはこんな時が来るとは思ってたけどよ……」"':
    r'CALL MESSAGE_BOX,@"「呜……虽然早知道会有这么一天……」"',
    r'CALL MESSAGE_BOX,@"「いぃっ…！？ は、初めての相手が触手…！？ そんな…ひでえよ……っ」"':
    r'CALL MESSAGE_BOX,@"「咿っ…！？ 第、第一次的对象是触手…！？ 怎么这样…太残忍了……っ」"',
    r'CALL MESSAGE_BOX,@"「うぁぁっ！ ゴブリンなんかにっ……ぁぁあああああっ！」"':
    r'CALL MESSAGE_BOX,@"「呜啊啊っ！ 被哥布林什么的……啊啊啊啊啊っ！」"',
    r'CALL MESSAGE_BOX,@"「は、離せっ！ なに入れようとしてんだ…っ うぁぁっ！」"':
    r'CALL MESSAGE_BOX,@"「放、放开っ！ 你想塞什么东西进来…っ 呜啊啊っ！」"',

    # === 事件/处女丧失后 (lines 238-276) ===
    r'CALL MESSAGE_BOX,@"「はぅっ♥ ……初めてがコレで、ヘンタイになっちまったら…♥♥\n　%MASTER_CALL()%に責任とってもらわないと…♥♥」"':
    r'CALL MESSAGE_BOX,@"「哈呜っ♥ ……第一次就这样，要是变成变态了…♥♥\n　可得让%MASTER_CALL()%负责才行…♥♥」"',
    r'CALL MESSAGE_BOX,@"「ん…%MASTER_CALL()%に抱かれるのがこんなに幸せだなんてな…♥♥」"':
    r'CALL MESSAGE_BOX,@"「嗯…被%MASTER_CALL()%抱居然这么幸福啊…♥♥」"',
    r'CALL MESSAGE_BOX,@"「ふぐぅっ♥…や、やっぱりぃ♥……なんてひでえヤツ…♥♥」"':
    r'CALL MESSAGE_BOX,@"「呼咕っ♥…果、果然♥……真是过分的家伙…♥♥」"',
    r'CALL MESSAGE_BOX,@"「はぐぅぅ♥……あ、あれ…涙？……きっと痛みのせい、だ…♥♥」"':
    r'CALL MESSAGE_BOX,@"「哈咕呜♥……啊、啊咧…眼泪？……一定是太痛了…♥♥」"',
    r'CALL MESSAGE_BOX,@"「惚れた相手とひとつに結ばれて、嬉しすぎて怖いくらいだ…♥♥\n　%SELF_CALL()%、初めてがこんなに幸せでいいのかな…♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「和喜欢的人结合在一起，开心得让人害怕…♥♥\n　%SELF_CALL()%、第一次这么幸福真的可以吗…♥♥♥」"',
    r'CALL MESSAGE_BOX,@"「%MASTER_CALL()%♥♥ %SWEET_MASTER_CALL()%…♥♥ 愛してるぅ♥♥」"':
    r'CALL MESSAGE_BOX,@"「%MASTER_CALL()%♥♥ %SWEET_MASTER_CALL()%…♥♥ 爱你♥♥」"',
    r'CALL MESSAGE_BOX,@"「惚れた相手と結ばれるのがこんなに幸せだなんて…♥♥」"':
    r'CALL MESSAGE_BOX,@"「和喜欢的人结合居然这么幸福…♥♥」"',
    r'CALL MESSAGE_BOX,@"「%SELF_CALL()%の想いを知っといて……%MASTER_CALL()%はヒドいやつだ……ぐすっ…」"':
    r'CALL MESSAGE_BOX,@"「明明知道%SELF_CALL()%的心意……%MASTER_CALL()%真是过分……呜咽…」"',
    r'CALL MESSAGE_BOX,@"「うぅぅ……こんな…こんな形で処女を捨てることに……」"':
    r'CALL MESSAGE_BOX,@"「呜呜……竟然…竟然以这种形式失去处女……」"',
    r'CALL MESSAGE_BOX,@"「…こ、これは…きっと夢なんだ……そう、ただの悪い…夢…」"':
    r'CALL MESSAGE_BOX,@"「…这、这一定是梦……对，只是个噩梦…」"',
    r'CALL MESSAGE_BOX,@"「…初体験に理想なんかなかったけど…ゴブリン相手ってのは…流石に堪えるぜ……」"':
    r'CALL MESSAGE_BOX,@"「…虽然对初体验没什么幻想…但对象是哥布林的话…还是有点受不了……」"',
    r'CALL MESSAGE_BOX,@"「んっ……思ったほどは辛くないな…」"':
    r'CALL MESSAGE_BOX,@"「嗯っ……比想象中没那么难受…」"',
    r'CALL MESSAGE_BOX,@"「ぐぅ…い、痛いに決まってんだろ…っ！\n　き、気遣うくらいなら早く抜いてくれ…っ」"':
    r'CALL MESSAGE_BOX,@"「咕…当、当然很痛啊…っ！\n　与、与其假惺惺关心不如快拔出来…っ」"',
    r'CALL MESSAGE_BOX,@"「あぐっ……ぐっ…ひぅ…」"':
    r'CALL MESSAGE_BOX,@"「啊咕っ……咕っ…咿呜…」"',

    # === 事件/Ａ处女丧失前 (lines 281-309) ===
    r'CALL MESSAGE_BOX,@"「……？ 一体%ANAL_CALL()%に何をするつもりだ…？\n　…っ！？ %ANAL_CALL()%にっ…捻じ込まれてっ…！？」"':
    r'CALL MESSAGE_BOX,@"「……？ 到底要对%ANAL_CALL()%做什么…？\n　…っ！？ %ANAL_CALL()%被…拧进去了…！？」"',
    r'CALL MESSAGE_BOX,@"「いてっ…！？　なのに…%ANAL_CALL()%の奥がジンジンして…変なの混ざってんじゃねえか…♥」"':
    r'CALL MESSAGE_BOX,@"「好痛っ…！？　可是…%ANAL_CALL()%深处在发麻…混进去了什么奇怪的东西吧…♥」"',
    r'CALL MESSAGE_BOX,@"「%MASTER_CALL()%…尻まで好きにしていいって言ったのに…こんなの聞いてねえ…っ♥」"':
    r'CALL MESSAGE_BOX,@"「%MASTER_CALL()%…虽然说了连屁股也可以随便，但没听说过这个…っ♥」"',
    r'CALL MESSAGE_BOX,@"「%MASTER_CALL()%♥ 新品の%ANAL_CALL()%…自由に使っていいからな♥♥」"':
    r'CALL MESSAGE_BOX,@"「%MASTER_CALL()%♥ 崭新的%ANAL_CALL()%…随便用吧♥♥」"',
    r'CALL MESSAGE_BOX,@"「痛っ…！？　でも…押し広げられながら…奥がムズムズ…気持ち悪…っ♥」"':
    r'CALL MESSAGE_BOX,@"「好痛っ…！？　可是…被撑开的同时…深处痒痒的…好奇怪…っ♥」"',
    r'CALL MESSAGE_BOX,@"「触手が%ANAL_CALL()%に入ってくるのは…やっぱちょっと怖い……っ」"':
    r'CALL MESSAGE_BOX,@"「触手进入%ANAL_CALL()%…果然还是有点害怕……っ」"',
    r'CALL MESSAGE_BOX,@"「痛ぇ…！？　なのに…%ANAL_CALL()%が勝手に…吸い付いてんの感じる…マジかよ…♥」"':
    r'CALL MESSAGE_BOX,@"「好痛…！？　可是…能感觉到%ANAL_CALL()%自己…吸住了…真的假的…♥」"',
    r'CALL MESSAGE_BOX,@"「啊哈哈♥ %SELF_CALL()%的%ANAL_CALL()%でいっぱい遊んでくれよなぁ♥♥」"':
    r'CALL MESSAGE_BOX,@"「啊哈哈♥ 用%SELF_CALL()%的%ANAL_CALL()%好好玩玩吧♥♥」"',
    r'CALL MESSAGE_BOX,@"「……っ！？ %ANAL_CALL()%に触んじゃねえ…っ！？」"':
    r'CALL MESSAGE_BOX,@"「……っ！？ 别碰%ANAL_CALL()%…っ！？」"',
    r'CALL MESSAGE_BOX,@"「そっちは違…っ！？　痛っ…！？　なのに…奥がぞわぞわ…っ、気持ち悪…！」"':
    r'CALL MESSAGE_BOX,@"「那边不是…っ！？　好痛…！？　可是…深处麻麻的…っ、好奇怪…！」"',
    r'CALL MESSAGE_BOX,@"「そ、そっちは違っ…… っ～～～！」"':
    r'CALL MESSAGE_BOX,@"「那、那边不对…… っ～～～！」"',

    # === 事件/Ａ处女丧失后 (lines 315-340) ===
    r'CALL MESSAGE_BOX,@"「かひっ…%ANAL_CALL()%は…なんかを入れたりするトコじゃ……んぐっ…」"':
    r'CALL MESSAGE_BOX,@"「咔咿…%ANAL_CALL()%不是…用来放东西的地方……嗯咕…」"',
    r'CALL MESSAGE_BOX,@"「…まだヒリヒリ…。でも…奥がうずいて…もっとって言ってんのかよ…嫌な予感だ…♥」"':
    r'CALL MESSAGE_BOX,@"「…还在火辣辣地疼…。可是…深处在发痒…像在说要更多…不妙的预感…♥」"',
    r'CALL MESSAGE_BOX,@"「%MASTER_CALL()%のせいだ…尻まで変な癖つく…♥」"':
    r'CALL MESSAGE_BOX,@"「都是%MASTER_CALL()%的错…连屁股都养成了奇怪的癖好…♥」"',
    r'CALL MESSAGE_BOX,@"「…んおぉっ！？ ひ、一突きで…♥ %ANAL_CALL()%が%PENIS_CALL()%に屈服させられたぁ…♥♥」"':
    r'CALL MESSAGE_BOX,@"「…嗯哦っ！？ 一、一击就…♥ %ANAL_CALL()%被%PENIS_CALL()%征服了…♥♥」"',
    r'CALL MESSAGE_BOX,@"「痛みの奥に…妙な火種みたいなの残ってんじゃん…マジで最悪…♥」"':
    r'CALL MESSAGE_BOX,@"「疼痛深处…留下了一种奇怪的火种…真是糟透了…♥」"',
    r'CALL MESSAGE_BOX,@"「お、おぉ…っ♥ 腹が押し広げられて……っ♥」"':
    r'CALL MESSAGE_BOX,@"「哦、哦哦…っ♥ 肚子被撑开了……っ♥」"',
    r'CALL MESSAGE_BOX,@"「ぎっ……うぐぅ……いてえっ！…やめ…っ！」"':
    r'CALL MESSAGE_BOX,@"「咯……呜咕……好痛っ！…住手…っ！」"',
    r'CALL MESSAGE_BOX,@"「はぐぅっ……結界があるからって、%ANAL_CALL()%に入れるとか…っ」"':
    r'CALL MESSAGE_BOX,@"「哈咕っ……有结界就能放进%ANAL_CALL()%吗…っ」"',
    r'CALL MESSAGE_BOX,@"「痛っ…！？　なのに…腸の奥が妙に熱い…気持ち悪…っ」"':
    r'CALL MESSAGE_BOX,@"「好痛っ…！？　可是…肠子深处莫名发热…好奇怪…っ」"',
    r'CALL MESSAGE_BOX,@"「ふぐぅ…っ こんな%ANAL_CALL()%を無理やり……」"':
    r'CALL MESSAGE_BOX,@"「呼咕…っ 竟然这样强行弄%ANAL_CALL()%……」"',

    # === 事件/初吻 (lines 348-369) ===
    r'CALL MESSAGE_BOX,@"「%MASTER_CALL()%♥♥ %SELF_CALL()%のファーストキス、受け取ってくれるか♥♥」"':
    r'CALL MESSAGE_BOX,@"「%MASTER_CALL()%♥♥ %SELF_CALL()%的初吻，愿意收下吗♥♥」"',
    r'CALL MESSAGE_BOX,@"「あぁ…♥ 初めてのキスを好きな相手にやれるなんてなぁ…♥♥\n　こんなでも女だからさ、すげーうれしいよ…♥♥」"':
    r'CALL MESSAGE_BOX,@"「啊啊…♥ 能把初吻给喜欢的人…♥♥\n　再怎么说我也是女生嘛，真的超开心…♥♥」"',
    r'CALL MESSAGE_BOX,@"「あぁ…本当のキス…♥ ようやく味わえるんだな…♥♥」"':
    r'CALL MESSAGE_BOX,@"「啊啊…真正的吻…♥ 终于能尝到了啊…♥♥」"',
    r'CALL MESSAGE_BOX,@"「うぶぅっ！？…ぶふぅっ！……ぐぅぇぇっ！」"':
    r'CALL MESSAGE_BOX,@"「呜噗っ！？…噗呼っ！……咕呃呃っ！」"',
    r'CALL MESSAGE_BOX,@"「あ、ぁ…%SELF_CALL()%の唇……こ、こんな…いきなり……」"':
    r'CALL MESSAGE_BOX,@"「啊、啊…%SELF_CALL()%的嘴唇……这、这样…太突然了……」"',
    r'CALL MESSAGE_BOX,@"「……一応、これが初めてのキスだったんだけどな…」"':
    r'CALL MESSAGE_BOX,@"「……说起来，这还是我的初吻呢…」"',
    r'CALL MESSAGE_BOX,@"「ぐぅ…っ こんなヤツに…初めてだってのに…」"':
    r'CALL MESSAGE_BOX,@"「咕…っ 被这种家伙…明明是我的第一次…」"',

    # === 事件/初次乳交 (lines 375-390) ===
    r'CALL MESSAGE_BOX,@"「あー…ぬるぬるして…何とも言えない感触だな…」"':
    r'CALL MESSAGE_BOX,@"「啊——…滑溜溜的…说不出的感觉啊…」"',
    r'CALL MESSAGE_BOX,@"「はぁ♥ %MASTER_CALL()%的%PENIS_CALL()%♥♥ 胸の中ですっげぇ熱い…♥♥」"':
    r'CALL MESSAGE_BOX,@"「哈啊♥ %MASTER_CALL()%的%PENIS_CALL()%♥♥ 在胸口里好烫…♥♥」"',
    r'CALL MESSAGE_BOX,@"「はぁ♥ %MASTER_CALL()%的%PENIS_CALL()%♥♥ すっげぇ熱い…♥♥」"':
    r'CALL MESSAGE_BOX,@"「哈啊♥ %MASTER_CALL()%的%PENIS_CALL()%♥♥ 好烫…♥♥」"',
    r'CALL MESSAGE_BOX,@"「ひうぅ…ぬるぬるして…動いてる…」"':
    r'CALL MESSAGE_BOX,@"「咿呜…滑溜溜的…在动…」"',
    r'CALL MESSAGE_BOX,@"「うぅ…なんでこんなこと…」"':
    r'CALL MESSAGE_BOX,@"「呜…为什么要这样…」"',
    r'CALL MESSAGE_BOX,@"「ひぃっ…汚いっ……うぁぁっ…！」"':
    r'CALL MESSAGE_BOX,@"「咿っ…好脏……呜啊啊っ…！」"',
    r'CALL MESSAGE_BOX,@"「うぅっ……この……はなせ…っ」"':
    r'CALL MESSAGE_BOX,@"「呜呜っ……你这……放开我…っ」"',

    # === 事件/主人公童贞毕业 (lines 400-424) ===
    r'CALL MESSAGE_BOX,@"「……？ %MASTER_CALL()%も初めて…？ まるで夢みたいだ…♥♥\n　っ……うっ…ぐすっ♥ 運命とか…信じていいのかも…♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「……？ %MASTER_CALL()%也是第一次…？ 简直像做梦一样…♥♥\n　呜……呜…啜泣♥ 说不定可以相信命运了呢…♥♥♥」"',
    r'CALL MESSAGE_BOX,@"「……？ %MASTER_CALL()%も初めて…？ まるで夢みたいだ…♥♥\n　%SELF_CALL()%、%MASTER_CALL()%の初めての相手に選んでもらえたんだな…♥♥」"':
    r'CALL MESSAGE_BOX,@"「……？ %MASTER_CALL()%也是第一次…？ 简直像做梦一样…♥♥\n　%SELF_CALL()%、被选为%MASTER_CALL()%的第一次对象了啊…♥♥」"',
    r'CALL MESSAGE_BOX,@"「うぅ…ほんとなら%SELF_CALL()%だってきれいな身体で抱かれたかったよ…」"':
    r'CALL MESSAGE_BOX,@"「呜…说实话%SELF_CALL()%也想用干净的身体被抱啊…」"',
    r'CALL MESSAGE_BOX,@"「なぁ…初めてだったのに、相手が%SELF_CALL()%でよかったのか…？\n　ん、んん…っ♥ 口ばっか上手いんだからよ…♥♥」"':
    r'CALL MESSAGE_BOX,@"「喂…明明是第一次，对象是%SELF_CALL()%真的好吗…？\n　唔、嗯嗯…っ♥ 就嘴上会说…♥♥」"',
    r'CALL MESSAGE_BOX,@"「へへ♥♥ お互い初めての相手になれるなんてさ…♥♥\n　%SELF_CALL()%、世界で一番幸せな家畜だろうな…♥♥」"':
    r'CALL MESSAGE_BOX,@"「嘿嘿♥♥ 能成为彼此的第一次对象…♥♥\n　%SELF_CALL()%、应该是世界上最幸福的家畜了吧…♥♥」"',
    r'CALL MESSAGE_BOX,@"「へへっ♥♥ %MASTER_CALL()%の初めてに選ばれて嬉しいよ…♥♥\n　本番で恥かかないように家畜の%VAGINA_CALL()%で練習しとこうな♥♥」"':
    r'CALL MESSAGE_BOX,@"「嘿嘿♥♥ 被选为%MASTER_CALL()%的第一次好开心…♥♥\n　为了实战不丢脸，用家畜的%VAGINA_CALL()%练习一下吧♥♥」"',
    r'CALL MESSAGE_BOX,@"「自分が初めてだとか…それがなんだってんだ……うっ、うっ…」"':
    r'CALL MESSAGE_BOX,@"「自己是第一次…那又怎么样……呜、呜…」"',
    r'CALL MESSAGE_BOX,@"「初めて…？ 他にいい相手がいなかったのか…？」"':
    r'CALL MESSAGE_BOX,@"「第一次…？ 没有其他合适的人了吗…？」"',
    r'CALL MESSAGE_BOX,@"「初めてだった…？ はぁ…よかったな…？」"':
    r'CALL MESSAGE_BOX,@"「是第一次…？ 哈…那还真是恭喜啊…？」"',
    r'CALL MESSAGE_BOX,@"「初めてだった…？ 抵抗できない相手に、さぞ楽しいことだろうよ…っ」"':
    r'CALL MESSAGE_BOX,@"「是第一次…？ 对无力抵抗的对象，一定很开心吧…っ」"',

    # === 事件/主人公初吻 (lines 430-449) ===
    r'CALL MESSAGE_BOX,@"「%MASTER_CALL()%とお互い初めてのキスなんてさ…♥♥\n　%SELF_CALL()%、自分が家畜の中でも特別だと勘違いしそうだ…♥♥」"':
    r'CALL MESSAGE_BOX,@"「和%MASTER_CALL()%互相都是初吻什么的…♥♥\n　%SELF_CALL()%、差点以为自己在家畜中也很特别了…♥♥」"',
    r'CALL MESSAGE_BOX,@"「%MASTER_CALL()%の初めてのキスがもらえるなんてさ…♥♥\n　%SELF_CALL()%、自分が家畜の中でも特別だと勘違いしそうだ…♥♥」"':
    r'CALL MESSAGE_BOX,@"「能得到%MASTER_CALL()%的初吻什么的…♥♥\n　%SELF_CALL()%、差点以为自己在家畜中也很特别了…♥♥」"',
    r'CALL MESSAGE_BOX,@"「それもお互いに初めてのキスとかさ……勘違いしてもいいのか…？♥♥」"':
    r'CALL MESSAGE_BOX,@"「而且还是彼此初吻什么的……我可以误会了吗…？♥♥」"',
    r'CALL MESSAGE_BOX,@"「%MASTER_CALL()%の初めてのキス…♥ もらっちまったぜ♥♥」"':
    r'CALL MESSAGE_BOX,@"「%MASTER_CALL()%的初吻…♥ 我收下了♥♥」"',
    r'CALL MESSAGE_BOX,@"「%MASTER_CALL()%も初めてのキス…？ その、悪い気はしねーな…」"':
    r'CALL MESSAGE_BOX,@"「%MASTER_CALL()%也是初吻…？ 那个，感觉还不坏…」"',
    r'CALL MESSAGE_BOX,@"「キスは初めて…？ 他にいい相手がいなかったのか…？」"':
    r'CALL MESSAGE_BOX,@"「初吻…？ 没有其他合适的人了吗…？」"',
    r'CALL MESSAGE_BOX,@"「初めてだった…？ だったら何してもいいってのか…っ」"':
    r'CALL MESSAGE_BOX,@"「是第一次…？ 那就可以为所欲为了吗…っ」"',

    # === 事件/处女结界解除 (lines 477-479) ===
    r'CALL MESSAGE_BOX,@"「全部ってんなら、一番最初に『アレ』…やっとかないとな♥♥」\n「今まで護ってくれてた結界も、ついにお役御免ってワケだ…♥」"':
    r'CALL MESSAGE_BOX,@"「要全部的话，得先做『那个』才行呢♥♥」\n「一直以来保护着我的结界，也终于要退休了…♥」"',
    r'CALL MESSAGE_BOX,@"「ほら…%SELF_CALL()%の大事な初めてを…奪ってほしい♥♥」"':
    r'CALL MESSAGE_BOX,@"「来吧…%SELF_CALL()%重要的第一次…来夺走吧♥♥」"',
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

    print(f"Batch 1 (事件) 替换: {total}/{len(R)}")
    for nf in not_found:
        print(f"  ⚠️  {nf}")

if __name__ == "__main__":
    main()
