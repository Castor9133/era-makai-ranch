#!/usr/bin/env python3
"""ボーイッシュ口上1_スケジュール.ERB — Batch 1: 奶农+事务+调剂"""
import sys
sys.stdout = open(1, 'w', encoding='utf-8', closefd=False)

FPATH = r"C:\Cursor local\era-makai-ranch\ERB\○口上\汎用口上\ボーイッシュ口上1_スケジュール.ERB"

R = {
    # === 奶农/初次 ===
    r'CALL MESSAGE_BOX,@"「%SELF_CALL()%も乳牛だし、家畜同士、通じ合える気がするぜ♥♥」"':
    r'CALL MESSAGE_BOX,@"「%SELF_CALL()%也是奶牛，家畜之间说不定能心意相通呢♥♥」"',

    r'CALL MESSAGE_BOX,@"「必ず%MASTER_CALL()%の役に立ってみせるから…♥」"':
    r'CALL MESSAGE_BOX,@"「我一定会为%MASTER_CALL()%效劳的…♥」"',

    r'CALL MESSAGE_BOX,@"「家畜の世話か……普通の方だよな…？」"':
    r'CALL MESSAGE_BOX,@"「照顾家畜吗……是普通的活儿吧…？」"',

    r'CALL MESSAGE_BOX,@"「家畜の世話…？ いくらか経験したことあるぜ」"':
    r'CALL MESSAGE_BOX,@"「照顾家畜…？ 我多少有点经验哦」"',

    r'CALL MESSAGE_BOX,@"「家畜の世話…？ とりあえずやってはみるけど…」"':
    r'CALL MESSAGE_BOX,@"「照顾家畜…？ 总之先试试看吧…」"',

    # === 奶农/普通 ===
    r'CALL MESSAGE_BOX,@"「いっぱいミルクを搾って%MASTER_CALL()%の役に立たないとな…♥♥」"':
    r'CALL MESSAGE_BOX,@"「得多挤点奶为%MASTER_CALL()%做贡献才行啊…♥♥」"',

    r'CALL MESSAGE_BOX,@"「へへ♥ 上手に世話したら%MASTER_CALL()%に褒めてもらえっかな…♥」"':
    r'CALL MESSAGE_BOX,@"「嘿嘿♥ 好好照顾的话，%MASTER_CALL()%会夸我吗…♥」"',

    r'CALL MESSAGE_BOX,@"「あ、いや…別に搾乳されている牛たちが羨ましいとか…思ってないし……」"':
    r'CALL MESSAGE_BOX,@"「啊、不…我才没有羡慕那些被挤奶的牛呢…绝对没有……」"',

    r'CALL MESSAGE_BOX,@"「ちゃんと世話して、美味しい牛乳を沢山出してもらわねえとな…」"':
    r'CALL MESSAGE_BOX,@"「得好好照顾，让它们产出更多美味的牛奶才行啊…」"',

    r'CALL MESSAGE_BOX,@"「ニンゲンに手を出さなくても、こうしてちゃんと仕事があんだからよー……」\n\d%CALLNAME%はぶつくさ言いながら仕事をこなしている…"':
    r'CALL MESSAGE_BOX,@"「不对人类出手，也有正经的工作可做啊……」\n\d%CALLNAME%嘀嘀咕咕地完成了工作…"',

    r'CALL MESSAGE_BOX,@"「さぁ牛たち、外でのんびり過ごすよーに！」"':
    r'CALL MESSAGE_BOX,@"「来吧牛儿们，去外面悠闲地度过时光吧！」"',

    r'CALL MESSAGE_BOX,@"「よし牛たち、健康のためには食事に睡眠、運動だっ！」"':
    r'CALL MESSAGE_BOX,@"「好了牛儿们，为了健康要吃饭、睡觉、运动！」"',

    r'CALL MESSAGE_BOX,@"「あぁっ…待てっ……柵の外はだめだぁっ…」"':
    r'CALL MESSAGE_BOX,@"「啊っ…等等っ……栅栏外面不行啊っ…」"',

    r'CALL MESSAGE_BOX,@"「牛たちみんな元気がいいな…！ %SELF_CALL()%も見習わないとな」"':
    r'CALL MESSAGE_BOX,@"「牛儿们都好有精神…！ %SELF_CALL()%也得学着点」"',

    r'CALL MESSAGE_BOX,@"「牛たちもおだやかで…平和で何事もないのが一番だなぁ」"':
    r'CALL MESSAGE_BOX,@"「牛儿们也很平静…和平无事才是最好的啊」"',

    r'CALL MESSAGE_BOX,@"「なんか牛たちの元気がないような… %SELF_CALL()%がちゃんとしねえと…」"':
    r'CALL MESSAGE_BOX,@"「总觉得牛儿们没什么精神… %SELF_CALL()%不好好干可不行啊…」"',

    # === 事务/初次 ===
    r'CALL MESSAGE_BOX,@"「事務作業……、こう見えて得意中の得意だぜ！」"':
    r'CALL MESSAGE_BOX,@"「事务工作……别看我这样，可是最拿手的！」"',

    r'CALL MESSAGE_BOX,@"「事務作業……、まぁいくらかやってみればコツも掴めるだろ」"':
    r'CALL MESSAGE_BOX,@"「事务工作……嘛，多干干就能掌握窍门了吧」"',

    r'CALL MESSAGE_BOX,@"「事務作業…… %MASTER_CALL()%、頼む相手を間違えてるぞ」"':
    r'CALL MESSAGE_BOX,@"「事务工作…… %MASTER_CALL()%，你找错人了吧」"',

    # === 事务/普通 ===
    r'CALL MESSAGE_BOX,@"「事務処理だったら、この%SELF_CALL()%に任せときな！」"':
    r'CALL MESSAGE_BOX,@"「事务处理的话，就交给%SELF_CALL()%吧！」"',

    r'CALL MESSAGE_BOX,@"「得意ってほどじゃないけど……ちゃんと仕事はやるって」"':
    r'CALL MESSAGE_BOX,@"「虽说不算擅长……但活儿会好好干的」"',

    r'CALL MESSAGE_BOX,@"「おいおい、どう考えても人選ミスだろ……」"':
    r'CALL MESSAGE_BOX,@"「喂喂，怎么看都是选错人了吧……」"',

    r'CALL MESSAGE_BOX,@"「よくもまあ、こんなにため込んだもんだ……」"':
    r'CALL MESSAGE_BOX,@"「可真行啊，竟然积了这么多文件……」"',

    r'CALL MESSAGE_BOX,@"「せっかくだし、先の分まで済ましとくか」"':
    r'CALL MESSAGE_BOX,@"「难得有机会，把之后的份也一并处理了吧」"',

    r'CALL MESSAGE_BOX,@"「地上のアレコレと共通点もあるし、なんとかやれるもんだな」"':
    r'CALL MESSAGE_BOX,@"「和地上那些活儿也有共通之处，总归还能应付」"',

    r'CALL MESSAGE_BOX,@"「まだ続けてやれって？ 目、節穴か？」"':
    r'CALL MESSAGE_BOX,@"「还要继续干？ 你眼睛是瞎了吗？」"',

    # === 调剂/初次 ===
    r'CALL MESSAGE_BOX,@"「調合の経験はそれなりに積んでるつもりだぜ」"':
    r'CALL MESSAGE_BOX,@"「调配的经验我自认为积累了不少」"',

    r'CALL MESSAGE_BOX,@"「んー……細かい作業だけど、手順通りでいいならなんとか」"':
    r'CALL MESSAGE_BOX,@"「嗯——……虽然是细致活，但按步骤来的话还行」"',

    r'CALL MESSAGE_BOX,@"「へへ…自慢じゃねえが、%SELF_CALL()%にやらせると人災が起きるぜ！」"':
    r'CALL MESSAGE_BOX,@"「嘿嘿…不是自夸，让%SELF_CALL()%干这个会出人命的！」"',

    # === 调剂/普通 ===
    r'CALL MESSAGE_BOX,@"「いっぱい薬を作って%MASTER_CALL()%の力になんねえとな」"':
    r'CALL MESSAGE_BOX,@"「得多做点药来帮%MASTER_CALL()%才行啊」"',

    r'CALL MESSAGE_BOX,@"「せっかく%MASTER_CALL()%が任せてくれたんだし、失敗出来ねえな…」"':
    r'CALL MESSAGE_BOX,@"「难得%MASTER_CALL()%交给我，可不能失败啊…」"',

    r'CALL MESSAGE_BOX,@"「よっと、完璧な調剤……、へへ…褒めてもらえるかも♥」"':
    r'CALL MESSAGE_BOX,@"「哟呵，完美的调剂……嘿嘿…说不定会被夸呢♥」"',

    r'CALL MESSAGE_BOX,@"「せめてヒトを殺さない程度に失敗を抑えねえと……」"':
    r'CALL MESSAGE_BOX,@"「至少得控制在不把人毒死的程度……」"',

    r'CALL MESSAGE_BOX,@"「まあ、やれって言うならやるさ」"':
    r'CALL MESSAGE_BOX,@"「嘛，说让我干我就干呗」"',

    r'CALL MESSAGE_BOX,@"「まあ、適材適所ってやつだな」"':
    r'CALL MESSAGE_BOX,@"「嘛，这就是人尽其才吧」"',

    r'CALL MESSAGE_BOX,@"「まさか地上の技術が目当てだったのか…？」"':
    r'CALL MESSAGE_BOX,@"「难不成是看上了地上的制药技术…？」"',

    r'CALL MESSAGE_BOX,@"「もしかして%SELF_CALL()%の薬で他のニンゲンが苦しむんじゃ…？」"':
    r'CALL MESSAGE_BOX,@"「该不会%SELF_CALL()%的药会让其他人受苦吧…？」"',

    r'CALL MESSAGE_BOX,@"「さっきの惨状……もう忘れたのか…？」"':
    r'CALL MESSAGE_BOX,@"「刚才的惨状……你已经忘了吗…？」"',

    r'CALL MESSAGE_BOX,@"「また調合かよ……今度こそ死人が出るだろうな」"':
    r'CALL MESSAGE_BOX,@"「又搞调配……这次肯定会出人命的吧」"',
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

    print(f"Batch 1 替换: {total}/{len(R)}")
    for nf in not_found:
        print(f"  ⚠️  {nf}")

if __name__ == "__main__":
    main()
