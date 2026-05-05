#!/usr/bin/env python3
"""ボーイッシュ口上1_スケジュール.ERB — Batch 2: 搾乳+抽出+体内凌辱+调教+探索+追踪"""
import sys
sys.stdout = open(1, 'w', encoding='utf-8', closefd=False)

FPATH = r"C:\Cursor local\era-makai-ranch\ERB\○口上\汎用口上\ボーイッシュ口上1_スケジュール.ERB"

R = {
    # === 搾乳/执行前/初次 ===
    r'CALL MESSAGE_BOX,@"「はーっ♥ はーっ♥ 搾乳されたい…♥ もう待ちきれない…♥♥」"':
    r'CALL MESSAGE_BOX,@"「哈啊♥ 哈啊♥ 好想被挤奶…♥ 已经等不及了…♥♥」"',

    r'CALL MESSAGE_BOX,@"「おぉ…♥ %MASTER_CALL()%の手で搾乳してもらえるなんてな…♥♥」"':
    r'CALL MESSAGE_BOX,@"「哦哦…♥ 竟然能被%MASTER_CALL()%亲手挤奶…♥♥」"',

    r'CALL MESSAGE_BOX,@"「その道具……%SELF_CALL()%も一人前の家畜に認められた、ってことか…♥♥」"':
    r'CALL MESSAGE_BOX,@"「那个道具……也就是说%SELF_CALL()%也被承认为合格的家畜了…♥♥」"',

    r'CALL MESSAGE_BOX,@"「ふふ♥♥ 乳搾り奴隷としての役目を果たすよ…♥♥」"':
    r'CALL MESSAGE_BOX,@"「呼呼♥♥ 我会尽到挤奶奴隶的职责的…♥♥」"',

    r'CALL MESSAGE_BOX,@"「その器具はまるで…♥ %SELF_CALL()%を本当の家畜みたいにするのか…？♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「那个器具简直…♥ 是要把%SELF_CALL()%变成真正的家畜吗…？♥♥♥」"',

    r'CALL MESSAGE_BOX,@"「%MASTER_CALL()%の乳搾り…♥ 心待ちにしてたよ…♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「%MASTER_CALL()%的挤奶…♥ 我一直期待着哦…♥♥♥」"',

    r'CALL MESSAGE_BOX,@"「その器具はまさか… あぁ、これからもっと役に立てるんだな……♥♥」"':
    r'CALL MESSAGE_BOX,@"「那个器具难道… 啊，这样就能更多地派上用场了……♥♥」"',

    r'CALL MESSAGE_BOX,@"「牧場の役に立てるようにいっぱい搾ってくれよな♥」"':
    r'CALL MESSAGE_BOX,@"「为了牧场的贡献，多挤点吧♥」"',

    r'CALL MESSAGE_BOX,@"「これからは日常的に搾乳される、ってことか…」"':
    r'CALL MESSAGE_BOX,@"「也就是说，以后每天都要被挤奶了…」"',

    r'CALL MESSAGE_BOX,@"「それは牛用の…？ うっ……%SELF_CALL()%も１頭の家畜ってことか…」"':
    r'CALL MESSAGE_BOX,@"「那是给牛用的…？ 唔……%SELF_CALL()%也是一头家畜了…」"',

    r'CALL MESSAGE_BOX,@"「嫌だ……%SELF_CALL()%は家畜なんかじゃない……」"':
    r'CALL MESSAGE_BOX,@"「不要……%SELF_CALL()%才不是什么家畜……」"',

    r'CALL MESSAGE_BOX,@"「それは牛用じゃねえか……？ まさか%SELF_CALL()%に……！？」"':
    r'CALL MESSAGE_BOX,@"「那不是给牛用的吗……？ 难道要对%SELF_CALL()%……！？」"',

    # === 搾乳/执行前/普通 (超乳) ===
    r'CALL MESSAGE_BOX,@"「こんなにデカパイだと、ミルクを搾りきれないかもしれないな…♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「这么大的奶子，说不定奶都挤不完呢…♥♥♥」"',

    r'CALL MESSAGE_BOX,@"「せっかく搾乳にうってつけの身体になれたんだしさ…♥♥\n　情け容赦なく搾ってくれよな…♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「好不容易变成了适合挤奶的身体…♥♥\n　可别手下留情，尽管挤吧…♥♥♥」"',

    r'CALL MESSAGE_BOX,@"「%SWEET_MASTER_CALL()%♥♥ どっさりミルク作れるようにしてくれた牝牛おっぱい…♥\n　%MASTER_CALL()%の乳搾りが待ち遠しくて今にも噴き出そうなくらいだ…♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「%SWEET_MASTER_CALL()%♥♥ 为了多产奶而给我的母牛乳房…♥\n　等%MASTER_CALL()%的挤奶等得快要喷出来了…♥♥♥」"',

    r'CALL MESSAGE_BOX,@"「他に仕事なんて出来ないワケだからさ…♥ せめていっぱい母乳を出して貢献しないとな…♥♥」"':
    r'CALL MESSAGE_BOX,@"「反正也干不了别的活了…♥ 至少得多出点母乳做贡献才行…♥♥」"',

    r'CALL MESSAGE_BOX,@"「あぁ…♥ %MASTER_CALL()%に搾乳して頂けるなんて…♥♥ 沢山母乳をお出ししますからね…♥♥」"':
    r'CALL MESSAGE_BOX,@"「啊啊…♥ 能被%MASTER_CALL()%亲自挤奶…♥♥ 我会出很多母乳的…♥♥」"',

    r'CALL MESSAGE_BOX,@"「こんな身体じゃ…もう搾乳されることしか……」"':
    r'CALL MESSAGE_BOX,@"「这副身体…只能被挤奶了……」"',

    r'CALL MESSAGE_BOX,@"「ひぐ……こんな身体にされちゃ、もう抵抗することだって……うぅっ…」"':
    r'CALL MESSAGE_BOX,@"「呜……变成这副身体，连反抗都……呜呜…」"',

    r'CALL MESSAGE_BOX,@"「…………」\n\d%CALLNAME%は虚ろな目で、されるがままになっている…"':
    r'CALL MESSAGE_BOX,@"「…………」\n\d%CALLNAME%眼神空洞，任凭摆布…"',

    # === 搾乳/执行前/普通 (非超乳) ===
    r'CALL MESSAGE_BOX,@"「あひぃ♥♥ 美味しい家畜ミルク…♥♥ いっぱい出しゅぅ…♥♥」"':
    r'CALL MESSAGE_BOX,@"「啊咿♥♥ 美味的家畜奶汁…♥♥ 要出好多好多…♥♥」"',

    r'CALL MESSAGE_BOX,@"「ふあぁ…♥ %MASTER_CALL()%に搾乳してもらえるなんてぇ…♥♥」"':
    r'CALL MESSAGE_BOX,@"「呼啊…♥ 竟然能被%MASTER_CALL()%挤奶…♥♥」"',

    r'CALL MESSAGE_BOX,@"「%SWEET_MASTER_CALL()%♥♥ 搾乳狂いの牝牛ミルク♥ 搾り尽くしてほしいぃ♥♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「%SWEET_MASTER_CALL()%♥♥ 挤奶狂魔的母牛奶汁♥ 请全部挤干净吧♥♥♥♥」"',

    r'CALL MESSAGE_BOX,@"「%MASTER_CALL()%に搾ってもらえるんだし、きっとミルクがもっと美味くなるよ♥♥」"':
    r'CALL MESSAGE_BOX,@"「能被%MASTER_CALL()%挤奶，牛奶一定会变得更美味哦♥♥」"',

    r'CALL MESSAGE_BOX,@"「…本当は%MASTER_CALL()%に…… いや、我儘言いっこなしだよな……」"':
    r'CALL MESSAGE_BOX,@"「…其实想让%MASTER_CALL()%…… 不，不能太任性啊……」"',

    r'CALL MESSAGE_BOX,@"「はぅ… また搾乳されちまう…」"':
    r'CALL MESSAGE_BOX,@"「哈呜… 又要被挤奶了…」"',

    r'CALL MESSAGE_BOX,@"「っ……！ こんなマネ、許さねえからな……！」"':
    r'CALL MESSAGE_BOX,@"「っ……！ 这种事，我可饶不了你……！」"',

    # === 搾乳/执行后 ===
    r'CALL MESSAGE_BOX,@"「はひぃぃ…♥ こんなに…だしちゃったぁ…♥♥♥ あぅ……♥♥」"':
    r'CALL MESSAGE_BOX,@"「哈咿咿…♥ 这么多…都出来了…♥♥♥ 啊呜……♥♥」"',

    r'CALL MESSAGE_BOX,@"「かひっ…♥♥ ちちしぼり…こんなに……しあわせぇ…っ♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「咔咿…♥♥ 挤奶…这么……幸福…っ♥♥♥」"',

    r'CALL MESSAGE_BOX,@"「は、はへっ…♥ おっぱいからっぽ…♥♥ もうらせない……♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「哈、哈欸…♥ 乳房空了…♥♥ 再也出不来了……♥♥♥」"',

    r'CALL MESSAGE_BOX,@"「ふあぁ…♥♥ はぁ…はぁ…♥♥」"':
    r'CALL MESSAGE_BOX,@"「呼啊…♥♥ 哈啊…哈啊…♥♥」"',

    r'CALL MESSAGE_BOX,@"「あひぃ…♥♥ こんなに…しぼられるなんて……♥♥」"':
    r'CALL MESSAGE_BOX,@"「啊咿…♥♥ 居然被挤了这么多……♥♥」"',

    r'CALL MESSAGE_BOX,@"「ふ、ふひっ……♥ かんじすぎて…くるいそう……♥♥」"':
    r'CALL MESSAGE_BOX,@"「呼、呼咿…♥ 感觉太强烈…要疯掉了……♥♥」"',

    r'CALL MESSAGE_BOX,@"「む、むりっ…♥ もうおっぱいのこってにゃい…♥♥」"':
    r'CALL MESSAGE_BOX,@"「不、不行了…♥ 乳房里已经不剩了…♥♥」"',

    r'CALL MESSAGE_BOX,@"「はぁ…はぁ… お、おわったか……」"':
    r'CALL MESSAGE_BOX,@"「哈啊…哈啊… 结、结束了吗……」"',

    # === 抽出/执行前/初次 ===
    r'CALL MESSAGE_BOX,@"「なんだこの機械…？ とりあえず入ればいいのか…？」"':
    r'CALL MESSAGE_BOX,@"「这机器是什么…？ 总之进去就行了吗…？」"',

    r'CALL MESSAGE_BOX,@"「この大げさな機械は……なんか嫌な予感が……」"':
    r'CALL MESSAGE_BOX,@"「这台夸张的机器……总有种不好的预感……」"',

    r'CALL MESSAGE_BOX,@"「くっ……こんな機械まで用意して何するつもりなんだよ…！」"':
    r'CALL MESSAGE_BOX,@"「切……连这种机器都准备好了，到底想干什么啊…！」"',

    # === 抽出/执行前/普通 (继续抽出) ===
    r'CALL MESSAGE_BOX,@"「んおぉ…♥♥ また動き出して…♥ 霊力が吸われていくぅ…♥♥」"':
    r'CALL MESSAGE_BOX,@"「唔哦…♥♥ 又动起来了…♥ 灵力在被吸走…♥♥」"',

    r'CALL MESSAGE_BOX,@"「また霊力が奪われて……頼むからやめてくれ……」"':
    r'CALL MESSAGE_BOX,@"「灵力又被夺走了……拜托了饶了我吧……」"',

    r'CALL MESSAGE_BOX,@"「ひっ…また動き始めて……もしかして力を全部奪うつもりなんじゃ…」"':
    r'CALL MESSAGE_BOX,@"「咿…又动起来了……该不会想把我的力量全部夺走吧…」"',

    # === 抽出/执行前/普通 (非继续) ===
    r'CALL MESSAGE_BOX,@"「な、なぁ…%SELF_CALL()%は反抗なんかしないし、やめとかないか…？」"':
    r'CALL MESSAGE_BOX,@"「那、那个…%SELF_CALL()%不会反抗的，不如就算了吧…？」"',

    r'CALL MESSAGE_BOX,@"「あ、あぁ…っ……またこの機械ン中に……っ！？」"':
    r'CALL MESSAGE_BOX,@"「啊、啊啊…っ……又要进这台机器里面了……っ！？」"',

    # === 抽出/执行后 ===
    r'CALL MESSAGE_BOX,@"「いっぱいぃ…♥♥ みるくとちからがいっぱいしぼられたぁ…♥♥」"':
    r'CALL MESSAGE_BOX,@"「满满的…♥♥ 奶和力量都被榨干了…♥♥」"',

    r'CALL MESSAGE_BOX,@"「あ、あひぃ…♥♥ もうおしまいなのかぁ…♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「啊、啊咿…♥♥ 已经结束了吗…♥♥♥」"',

    r'CALL MESSAGE_BOX,@"「はっ…はひっ…♥♥ お、お哈…おぉ……♥♥」\n（さくにゅうされて、ちからすわれて、かちくいっちょくせん…♥♥♥）"':
    r'CALL MESSAGE_BOX,@"「哈…哈咿…♥♥ 哦、哦哈…哦哦……♥♥」\n（被挤了奶、被吸了灵力、家畜一条路走到黑…♥♥♥）"',

    r'CALL MESSAGE_BOX,@"「あぁ…ぁ…♥ お、おわったぞぉ…♥ 出してくれぇ…♥♥」"':
    r'CALL MESSAGE_BOX,@"「啊啊…啊…♥ 结、结束了…♥ 放我出去吧…♥♥」"',

    r'CALL MESSAGE_BOX,@"「かひっ♥ は、はひ…♥♥ たえられにゃい…♥♥ イきくるう…♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「咔咿♥ 哈、哈咿…♥♥ 受不鸟了…♥♥ 要高潮至死…♥♥♥」"',

    r'CALL MESSAGE_BOX,@"「おっ♥ おっ♥ おわった…♥♥ は、はやくここから出してくれぇ…♥」"':
    r'CALL MESSAGE_BOX,@"「哦♥ 哦♥ 结束了…♥♥ 快、快点放我出去…♥」"',

    r'CALL MESSAGE_BOX,@"「ふ…あぁ…♥ こ、これ以上力を奪われたら……あぅ…♥」"':
    r'CALL MESSAGE_BOX,@"「呼…啊啊…♥ 再、再被夺走力量的话……啊呜…♥」"',

    # === 体内凌辱/开始捕获/初次 ===
    r'CALL MESSAGE_BOX,@"「啊哈哈…♥ %SELF_CALL()%齿%MASTER_CALL()%に食べられちまうんだな…♥\n　いいぜ…%MASTER_CALL()%と本当のひとつになれるなら幸せだ…♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「啊哈哈…♥ %SELF_CALL()%要被%MASTER_CALL()%吃掉了啊…♥\n　好啊…能成为%MASTER_CALL()%真正的部分一体的话，我很幸福…♥♥♥」"',

    r'CALL MESSAGE_BOX,@"「あ…あぁ…%MASTER_CALL()%…？ %SELF_CALL()%は用済みだってのか…？\n　ま、まだまだ役に立てるからぁっ！ ゆ、許し……ひぃっ…！」"':
    r'CALL MESSAGE_BOX,@"「啊…啊啊…%MASTER_CALL()%…？ %SELF_CALL()%已经没用了吗…？\n　我、我还能继续效力的！ 饶、饶了我……咿…！」"',

    r'CALL MESSAGE_BOX,@"「ば、化け物っ！？ うあぁっ！ た、助け……っ！」"':
    r'CALL MESSAGE_BOX,@"「怪、怪物！？ 呜啊っ！ 救、救命……っ！」"',

    # === 体内凌辱/开始捕获/普通 ===
    r'CALL MESSAGE_BOX,@"「あぁ……♥♥ %SWEET_MASTER_CALL()%♥♥ %SELF_CALL()%をまたあの極楽に連れてってくれ…♥♥」"':
    r'CALL MESSAGE_BOX,@"「啊啊……♥♥ %SWEET_MASTER_CALL()%♥♥ 把%SELF_CALL()%再带去那个极乐世界吧…♥♥」"',

    r'CALL MESSAGE_BOX,@"「はぅ…分かってても身構えちまって…… あ…もう逃げらんね……♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「哈呜…明明知道还是紧张了…… 啊…已经逃不掉了……♥♥♥」"',

    r'CALL MESSAGE_BOX,@"「あ…あぁ… そんな、また『あっち』に…！？ 今度こそ心が壊れちまう……っ！」"':
    r'CALL MESSAGE_BOX,@"「啊…啊啊… 不会吧，又要去『那边』了…！？ 这次真的会坏掉的……っ！」"',

    # === 体内凌辱/执行前/初次 ===
    r'CALL MESSAGE_BOX,@"「んあ…？ %SELF_CALL()%齿%MASTER_CALL()%に美味しく頂かれたんじゃ……\n　もしかして、生きたまま消化される…とか？♥」"':
    r'CALL MESSAGE_BOX,@"「嗯啊…？ %SELF_CALL()%不是被%MASTER_CALL()%美味地吃掉了……\n　难道说，会被活着消化…之类的？♥」"',

    r'CALL MESSAGE_BOX,@"「～～～～っ！……んあ…？ %SELF_CALL()%、まだ生きてる……\n　んで、ここは…まさか体ン中ってことか…？」"':
    r'CALL MESSAGE_BOX,@"「～～～～っ！……嗯啊…？ %SELF_CALL()%、还活着……\n　那这里是…难道是身体里面…？」"',

    # === 体内凌辱/执行前/普通 (继续) ===
    r'CALL MESSAGE_BOX,@"「～～～っ♥♥♥ ……かひッ♥♥ はひィっ♥♥♥ ッ！ ッ！ ～～～～ッ♥♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「～～～っ♥♥♥ ……咔咿♥♥ 哈咿♥♥♥ 噫！ 噫！ ～～～～ッ♥♥♥♥」"',

    r'CALL MESSAGE_BOX,@"「お゛ーっ♥ おっ♥ おっ♥ おっ♥ んぐっ♥ おお゛ぉぉ～～♥♥」"':
    r'CALL MESSAGE_BOX,@"「啊呜——♥ 哦♥ 哦♥ 哦♥ 嗯呜♥ 哦哦呜哦哦～～♥♥」"',

    r'CALL MESSAGE_BOX,@"「哦♥ 哦♥ お゛おぉっ♥♥♥ ア、アタマ灼き切れるっ♥♥♥ んぎぃぃぃ♥♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「哦♥ 哦♥ 啊呜哦哦♥♥♥ 头、脑袋要烧断了♥♥♥ 嗯咿咿咿♥♥♥♥」"',

    r'CALL MESSAGE_BOX,@"（これいじょうは♥♥ つぶれるっ♥ 快楽におしつぶされるっ♥♥♥）"':
    r'CALL MESSAGE_BOX,@"（再也撑不住了♥♥ 要坏掉了♥ 要被快感压垮了♥♥♥）"',

    r'CALL MESSAGE_BOX,@"「あ゛っ♥♥ あひっ♥♥ %MASTER_CALL()%っ♥♥ た、たすっ……んぎゅぅぅぅぅ♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「啊呜♥♥ 啊咿♥♥ %MASTER_CALL()%♥♥ 救、救命……嗯呜唔唔唔唔♥♥♥」"',

    r'CALL MESSAGE_BOX,@"「ひぐっ♥♥ こ、こわれる…♥♥ ゆるしてっ♥♥ ゆるし――いぎぃぃぃ♥♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「咿咕♥♥ 要、要坏掉了…♥♥ 饶了我♥♥ 饶了——去了咿咿咿♥♥♥♥」"',

    r'CALL MESSAGE_BOX,@"「啊ー♥ 啊ー♥ かはっ♥ んぎっ♥ …んお゛お゛ぉぉぉ♥♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「啊ー♥ 啊ー♥ 咔哈♥ 嗯咿♥ ……唔哦呜哦哦哦♥♥♥♥」"',

    # === 体内凌辱/执行前/普通 (非继续) ===
    r'CALL MESSAGE_BOX,@"「アハハハハハ…♥♥ またココに来るのが愉しみだったんだよ♥♥\n　気絶すらさせてもらえない快楽地獄に帰ってきたってワケだ…♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「阿哈哈哈…♥♥ 我一直期待着再来这里呢♥♥\n　也就是说我回到了连晕过去都不被允许的快乐地狱…♥♥♥」"',

    r'CALL MESSAGE_BOX,@"「あぁ…休みのない触手責めは絶対無茶なんだって…♥」"':
    r'CALL MESSAGE_BOX,@"「啊啊…无休止的触手责罚绝对是乱来啊…♥」"',

    r'CALL MESSAGE_BOX,@"「ひっ… 離してくれっ…！ あ、あんな目は二度とゴメンだっ……」"':
    r'CALL MESSAGE_BOX,@"「咿… 放开我…！ 那、那种经历我可不想再来一次了……」"',

    # === 体内凌辱/执行后/初次 ===
    r'CALL MESSAGE_BOX,@"（こんなの味わっちまったら…%SELF_CALL()%はもうこの快楽なしで生きていけねえ…♥♥）"':
    r'CALL MESSAGE_BOX,@"（尝到了这个…%SELF_CALL()%已经没办法没有这份快感活下去了…♥♥）"',

    r'CALL MESSAGE_BOX,@"（からだが痙攣して動かない…♥♥ あんな快楽、受け止めきれる筈がない…♥♥♥）"':
    r'CALL MESSAGE_BOX,@"（身体痉挛着动弹不得…♥♥ 那种快感，根本不可能承受得住…♥♥♥）"',

    r'CALL MESSAGE_BOX,@"（なんとか生きてるけど……一息に食われた方がましだったかもしれねえ…♥）"':
    r'CALL MESSAGE_BOX,@"（虽然勉强活着……但也许一口气被吃掉反而更好…♥）"',

    # === 体内凌辱/执行后/普通 ===
    r'CALL MESSAGE_BOX,@"「あ、あぁ…♥♥ まってぇ…これでおしまいなんてやらぁ…♥♥」"':
    r'CALL MESSAGE_BOX,@"「啊、啊啊…♥♥ 等等…就这样结束我可不要…♥♥」"',

    r'CALL MESSAGE_BOX,@"「ひぁ…♥ ひぅぅ…♥♥ からだ痙攣して…♥ う、うごけない…♥♥」"':
    r'CALL MESSAGE_BOX,@"「咿啊…♥ 咿呜呜…♥♥ 身体痉挛着…♥ 动、动不了…♥♥」"',

    r'CALL MESSAGE_BOX,@"（きもちいい…きもちいい…なにもかんがえらんねぇ…♥♥）"':
    r'CALL MESSAGE_BOX,@"（好舒服…好舒服…什么都无法思考了…♥♥）"',

    # === 调教/开始调教 ===
    r'CALL MESSAGE_BOX,@"「%MASTER_CALL()%♥ 家畜の躾け♥♥ しっかり頼むぜ♥♥」"':
    r'CALL MESSAGE_BOX,@"「%MASTER_CALL()%♥ 家畜的调教♥♥ 拜托你了哦♥♥」"',

    r'CALL MESSAGE_BOX,@"「%MASTER_CALL()%に忠実な愛玩ペットをたっぷり可愛がってくれよな…♥♥」"':
    r'CALL MESSAGE_BOX,@"「对%MASTER_CALL()%忠诚的爱宠，好好宠爱我吧…♥♥」"',

    r'CALL MESSAGE_BOX,@"「%SELF_CALL()%でいっぱい愉しんでくれよ♥ %MASTER_CALL()%♥♥」"':
    r'CALL MESSAGE_BOX,@"「用%SELF_CALL()%好好享受吧♥ %MASTER_CALL()%♥♥」"',

    r'CALL MESSAGE_BOX,@"「へへ…待ち遠しかったよ♥ %SWEET_MASTER_CALL()%♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「嘿嘿…等你好久了♥ %SWEET_MASTER_CALL()%♥♥♥」"',

    r'CALL MESSAGE_BOX,@"「%SWEET_MASTER_CALL()%…♥ %SELF_CALL()%嬉しいよ…♥♥」"':
    r'CALL MESSAGE_BOX,@"「%SWEET_MASTER_CALL()%…♥ %SELF_CALL()%好开心…♥♥」"',

    r'CALL MESSAGE_BOX,@"「あぁ…%MASTER_CALL()%が恋しくて堪らなかったんだ…♥」"':
    r'CALL MESSAGE_BOX,@"「啊啊…想%MASTER_CALL()%想得受不了了…♥」"',

    r'CALL MESSAGE_BOX,@"「優しくされても手荒にされても良い声で鳴くからさ…たっぷり愉しんでくれよ♥♥」"':
    r'CALL MESSAGE_BOX,@"「不管温柔还是粗暴我都会叫得很好听的…好好享受吧♥♥」"',

    r'CALL MESSAGE_BOX,@"「%MASTER_CALL()%の好きにしてくれ……」"':
    r'CALL MESSAGE_BOX,@"「随%MASTER_CALL()%的便吧……」"',

    r'CALL MESSAGE_BOX,@"「ん……命令通りすればいいんだな……」"':
    r'CALL MESSAGE_BOX,@"「嗯……按命令做就行了吧……」"',

    r'CALL MESSAGE_BOX,@"「抵抗なんかしないから、乱暴はやめてくれ……」"':
    r'CALL MESSAGE_BOX,@"「我不会反抗的，别太粗暴……」"',

    r'CALL MESSAGE_BOX,@"「はぁ…… 抵抗しても無意味なら、せめて手短にしてくれ……」"':
    r'CALL MESSAGE_BOX,@"「哈啊…… 反正反抗也没用，至少快点结束吧……」"',

    r'CALL MESSAGE_BOX,@"「やめろっ…！ 近寄んじゃねえっ…！」"':
    r'CALL MESSAGE_BOX,@"「住手…！ 别靠近我…！」"',

    r'CALL MESSAGE_BOX,@"「へ、へへ…%SWEET_MASTER_CALL()%…く、苦しいのとかはちょっと……\n　咿唔……な、なんでもない……っ」"':
    r'CALL MESSAGE_BOX,@"「嘿、嘿嘿…%SWEET_MASTER_CALL()%…痛、痛苦的什么的我有点……\n　咿唔……没、没什么……っ」"',

    # === 调教/调教结束 ===
    r'CALL MESSAGE_BOX,@"「あー…%SELF_CALL()%、なんかやっちまったか…？」"':
    r'CALL MESSAGE_BOX,@"「啊——…%SELF_CALL()%、是不是搞砸了什么…？」"',

    r'CALL MESSAGE_BOX,@"「お……もう満足したんだな…」"':
    r'CALL MESSAGE_BOX,@"「哦……已经满足了啊…」"',

    r'CALL MESSAGE_BOX,@"「時間の無駄だろ、こんなの……」"':
    r'CALL MESSAGE_BOX,@"「浪费时间罢了，这种……」"',

    r'CALL MESSAGE_BOX,@"「ふぁあ…♥ こんなにしてくれるなんてぇ…♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「呼啊…♥ 居然能这样对我…♥♥♥」"',

    r'CALL MESSAGE_BOX,@"「はぁ…はぁ…♥♥ と、とっくに体力の限界だっての…♥♥」"':
    r'CALL MESSAGE_BOX,@"「哈啊…哈啊…♥♥ 早、早就体力不支了啊…♥♥」"',

    r'CALL MESSAGE_BOX,@"「は、はひっ…♥ ど、どんだけ時間かけんだよ…♥」"':
    r'CALL MESSAGE_BOX,@"「哈、哈咿…♥ 要、要花多少时间啊…♥」"',

    r'CALL MESSAGE_BOX,@"「ぜぇ…ぜぇ……もう…限界……」"':
    r'CALL MESSAGE_BOX,@"「呼…呼……已经…到极限了……」"',

    r'CALL MESSAGE_BOX,@"「%SWEET_MASTER_CALL()%…♥ %SELF_CALL()%幸せだぞぉ…♥♥」"':
    r'CALL MESSAGE_BOX,@"「%SWEET_MASTER_CALL()%…♥ %SELF_CALL()%好幸福…♥♥」"',

    r'CALL MESSAGE_BOX,@"「%MASTER_CALL()%…♥ 満足してもらえたか…？♥♥」"':
    r'CALL MESSAGE_BOX,@"「%MASTER_CALL()%…♥ 您满意了吗…？♥♥」"',

    r'CALL MESSAGE_BOX,@"「%MASTER_CALL()%…♥♥ 一生そばにいさせろよな…♥♥」"':
    r'CALL MESSAGE_BOX,@"「%MASTER_CALL()%…♥♥ 让我一辈子待在你身边吧…♥♥」"',

    r'CALL MESSAGE_BOX,@"「はぅ……こんなに責められちゃ、チカラ入らねえよ…♥♥」"':
    r'CALL MESSAGE_BOX,@"「哈呜……被这样折磨，使不上力气了…♥♥」"',

    r'CALL MESSAGE_BOX,@"「はぁ♥ 噗啊♥ ……満足してもらえたみたいだな…」"':
    r'CALL MESSAGE_BOX,@"「哈啊♥ 噗啊♥ ……看来你已经满足了呢…」"',

    r'CALL MESSAGE_BOX,@"「はぁ…はぁ……こんなに消耗させられるなんてよ……」"':
    r'CALL MESSAGE_BOX,@"「哈啊…哈啊……竟然被消耗成这样……」"',

    r'CALL MESSAGE_BOX,@"「…もう十分だろ……」"':
    r'CALL MESSAGE_BOX,@"「…已经够了吧……」"',

    r'CALL MESSAGE_BOX,@"「ぜぇ…ぜぇ……体力が…限界…」"':
    r'CALL MESSAGE_BOX,@"「呼…呼……体力…到极限了…」"',

    r'CALL MESSAGE_BOX,@"「なんでこんな目に…うぅ…」"':
    r'CALL MESSAGE_BOX,@"「为什么我要受这种罪…呜呜…」"',

    r'CALL MESSAGE_BOX,@"「ぜぇ…ぜぇ…こんなに消耗させられちゃ、逃げることも……」"':
    r'CALL MESSAGE_BOX,@"「呼…呼…被消耗成这样，连逃跑都……」"',

    # === 调教/晚上调教后回自室 ===
    r'CALL MESSAGE_BOX,@"「じゃあ、おやすみ…%MASTER_CALL()%♥♥\n　一緒に寝たいのは山々だけど、明日も早いからさ♥♥」"':
    r'CALL MESSAGE_BOX,@"「那么，晚安…%MASTER_CALL()%♥♥\n　虽然很想一起睡，但明天还要早起呢♥♥」"',

    r'CALL MESSAGE_BOX,@"「%MASTER_CALL()%が部屋まで運んでくれるなんてさ♥\n　へへ…♥ 今夜は幸せな夢が見れそうだぜ♥♥」"':
    r'CALL MESSAGE_BOX,@"「%MASTER_CALL()%居然把我送到房间♥\n　嘿嘿…♥ 今晚一定能做个幸福的梦♥♥」"',

    r'CALL MESSAGE_BOX,@"「じゃあ、おやすみ…%MASTER_CALL()%♥」\n（ほんとは一緒に寝たいんだけど…口にするのは恥ずかしいんだよなぁ……）"':
    r'CALL MESSAGE_BOX,@"「那么，晚安…%MASTER_CALL()%♥」\n（其实想和你一起睡…但说出来太难为情了……）」"',

    r'CALL MESSAGE_BOX,@"「じゃあ、%SELF_CALL()%は戻るぜ……あとどれくらい寝れっかな…」"':
    r'CALL MESSAGE_BOX,@"「那么，%SELF_CALL()%回去了……还能睡多久呢…」"',

    r'CALL MESSAGE_BOX,@"「うぅ…自力で部屋に戻ることもできないなんて……」"':
    r'CALL MESSAGE_BOX,@"「呜呜…连自己回房间都做不到了……」"',

    r'CALL MESSAGE_BOX,@"「ちっ…昼も夜もねえな…」"':
    r'CALL MESSAGE_BOX,@"「切…没日没夜了呢…」"',

    # === 探索魔界 ===
    r'CALL MESSAGE_BOX,@"「さて、そろそろ身体を休めないとな…」"':
    r'CALL MESSAGE_BOX,@"「好了，差不多该让身体休息一下了…」"',

    r'CALL MESSAGE_BOX,@"「地形を把握して、現在地を見失わないようにしないと…」"':
    r'CALL MESSAGE_BOX,@"「得掌握地形，不能迷失方向…」"',

    r'CALL MESSAGE_BOX,@"「おぉ…！ 結構可愛い動物とかもいるじゃん…！」"':
    r'CALL MESSAGE_BOX,@"「哦哦…！ 还挺有可爱的动物嘛…！」"',

    r'CALL MESSAGE_BOX,@"「うぅ…さっきも同じ道を通ったような……いや、そんな筈は…」"':
    r'CALL MESSAGE_BOX,@"「呜呜…刚才好像也走过同样的路……不，不可能…」"',

    # === 追踪 ===
    r'CALL MESSAGE_BOX,@"「……っ！」（嫌だ……怖えぇ…っ）"':
    r'CALL MESSAGE_BOX,@"「……っ！」（不要……好可怕…っ）"',

    r'CALL MESSAGE_BOX,@"「……っ！」（ここで見つかる訳には…っ）"':
    r'CALL MESSAGE_BOX,@"「……っ！」（绝不能在这里被发现…っ）"',

    r'CALL MESSAGE_BOX,@"「うぅっ…見つかっちまった…っ」"':
    r'CALL MESSAGE_BOX,@"「呜呜…被发现了…っ」"',

    r'CALL MESSAGE_BOX,@"「くっ…こうなったら…っ！」"':
    r'CALL MESSAGE_BOX,@"「切…事到如今…っ！」"',

    r'CALL MESSAGE_BOX,@"「ふぅ……なんとかやり過ごせたみたいだな……」"':
    r'CALL MESSAGE_BOX,@"「呼……好像总算蒙混过去了……」"',

    r'CALL MESSAGE_BOX,@"「あ、あぁ…っ！ いつのまに…っ！」"':
    r'CALL MESSAGE_BOX,@"「啊、啊啊…っ！ 什么时候…っ！」"',

    r'CALL MESSAGE_BOX,@"「くっ…！ 油断した…っ！」"':
    r'CALL MESSAGE_BOX,@"「切…！ 大意了…っ！」"',
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
