#!/usr/bin/env python3
"""慇懃口上1.ERB — Batch 1: 绝顶 + 射精/膣内 + 射精/尻穴 sections"""
import sys
sys.stdout = open(1, 'w', encoding='utf-8', closefd=False)

FPATH = r"C:\Cursor local\era-makai-ranch\ERB\○口上\汎用口上\慇懃口上1.ERB"

R = {
    # === 绝顶 (lines 90-100) ===
    r'CALL MESSAGE_BOX,@"「嗯呜♥ 嗯呜呜♥ 嗯呜嗯呜イぎゅ嗯呜呜呜呜♥♥♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「嗯呜♥ 嗯呜呜♥ 嗯呜嗯呜咿呜嗯呜呜呜呜♥♥♥♥♥」"',

    r'CALL MESSAGE_BOX,@"「唔哦哦哦っ♥♥♥ アクメっ♥ 深っ♥♥ とっ♥ とまらっ♥♥\n　哦♥ 啊呜♥♥ 哦♥♥♥ 哦哦哦オ゛オ゛っ♥♥♥♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「唔哦哦哦っ♥♥♥ 绝顶っ♥ 好深っ♥♥ 停っ♥ 停不下来っ♥♥\n　哦♥ 啊呜♥♥ 哦♥♥♥ 哦哦哦哦哦っ♥♥♥♥♥♥」"',

    r'CALL MESSAGE_BOX,@"「哈♥ 哈啊♥ め、目の前がチカチカして♥ またイ、イぐっっ♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「哈♥ 哈啊♥ 眼、眼前在闪烁♥ 又要去、去去了っっ♥♥♥」"',

    r'CALL MESSAGE_BOX,@"「啊♥ 啊♥ 啊♥ たっ♥ たえられなっ♥♥ こんなのっ♥♥」"':
    r'CALL MESSAGE_BOX,@"「啊♥ 啊♥ 啊♥ 受っ♥ 受不了っ♥♥ 这样的っ♥♥」"',

    r'CALL MESSAGE_BOX,@"「んあっ♥♥ こんなぁ…♥ らめ…♥♥ んんん♥♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「嗯啊っ♥♥ 这样的…♥ 不要…♥♥ 嗯嗯嗯♥♥♥♥」"',

    r'CALL MESSAGE_BOX,@"「啊♥ んぅっ♥ 啊♥ 啊♥ んあぁっ♥」"':
    r'CALL MESSAGE_BOX,@"「啊♥ 嗯呜っ♥ 啊♥ 啊♥ 嗯啊っ♥」"',

    # === 射精/膣内 (lines 131-168) ===
    r'CALL MESSAGE_BOX,@"「啊♥ あぁ…♥ 多么强烈的高潮呀♥♥ 子宫都屈服了呀♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「啊♥ 啊啊…♥ 多么强烈的高潮呀♥♥ 子宫都屈服了呀♥♥♥」"',

    r'CALL MESSAGE_BOX,@"「んやぁ♥♥ %SELF_CALL()%的%VAGINA_CALL()%♥♥ 被精液驯服了呀♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「咿呀♥♥ %SELF_CALL()%的%VAGINA_CALL()%♥♥ 被精液驯服了呀♥♥♥」"',

    r'CALL MESSAGE_BOX,@"「んひぃぃ♥♥♥ 感谢您赐予精液牛奶的奖励呀♥♥ あひぃぃ♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「嗯咿咿♥♥♥ 感谢您赐予精液牛奶的奖励呀♥♥ 啊咿咿♥♥♥」"',

    r'CALL MESSAGE_BOX,@"「はひっ♥ %MASTER_CALL()%专用的性处理便器，请尽情使用吧♥♥」"':
    r'CALL MESSAGE_BOX,@"「哈咿っ♥ %MASTER_CALL()%专用的性处理便器，请尽情使用吧♥♥」"',

    r'CALL MESSAGE_BOX,@"「んあぁっ♥♥ 因为膣内射精而高潮的家畜的丑态呀♥♥ 请尽情观赏吧♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「嗯啊っ♥♥ 因为膣内射精而高潮的家畜的丑态呀♥♥ 请尽情观赏吧♥♥♥」"',

    r'CALL MESSAGE_BOX,@"「キたっ♥ キたっ♥ 種付けご褒美っ♥♥ 非常感谢呀♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「来っ♥ 来っ♥ 配种奖赏っ♥♥ 非常感谢呀♥♥♥」"',

    r'CALL MESSAGE_BOX,@"「んおぉっ♥♥♥ 即使怀孕了，还是因精液而快乐到高潮呀♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「唔哦っ♥♥♥ 即使怀孕了，还是因精液而快乐到高潮呀♥♥♥」"',

    r'CALL MESSAGE_BOX,@"「ふわぁ♥♥ 肚子里扩散开了热流……好舒服呀……♥♥」"':
    r'CALL MESSAGE_BOX,@"「呼哇♥♥ 肚子里扩散开了热流……好舒服呀……♥♥」"',

    r'CALL MESSAGE_BOX,@"「%SWEET_MASTER_CALL()%っ♥♥ すきっ♥♥ すきぃぃっ♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「%SWEET_MASTER_CALL()%っ♥♥ 喜欢っ♥♥ 好喜欢っ♥♥♥」"',

    r'CALL MESSAGE_BOX,@"「んあぁ♥♥ いっしょにっ♥ 和%MASTER_CALL()%一起到达高潮呀♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「嗯啊♥♥ 一起っ♥ 和%MASTER_CALL()%一起到达高潮呀♥♥♥」"',

    r'CALL MESSAGE_BOX,@"「ほぁぁ♥ 精液中毒的%VAGINA_CALL()%不想让%PENIS_CALL()%离开呀……♥♥」"':
    r'CALL MESSAGE_BOX,@"「嚯啊♥ 精液中毒的%VAGINA_CALL()%不想让%PENIS_CALL()%离开呀……♥♥」"',

    r'CALL MESSAGE_BOX,@"「っ～～～～♥♥ 種付け同時絶頂ぉぉ♥♥♥ 幸せすぎゆぅぅぅ♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「っ～～～～♥♥ 配种同时绝顶哦哦♥♥♥ 幸福得不得了呜呜呜♥♥♥」"',

    r'CALL MESSAGE_BOX,@"「おごッ…！？ %PENIS_CALL()%で子宮口こじ開けられてっ…じ、直に注がれてるっ♥♥\n　こんなのぉっ♥♥ 因太过幸福而必定高潮呀！♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「哦咯ッ…！？ %PENIS_CALL()%把子宫口撬开っ…直、直接注射进来了っ♥♥\n　这样的哦っ♥♥ 因太过幸福而必定高潮呀！♥♥♥」"',

    r'CALL MESSAGE_BOX,@"「あぁ…♥♥ 如果再怀孕的话，希望是个女孩呀…♥\n　那样母女俩就可以一起侍奉%MASTER_CALL()%了呀…♥♥」"':
    r'CALL MESSAGE_BOX,@"「啊啊…♥♥ 如果再怀孕的话，希望是个女孩呀…♥\n　那样母女俩就可以一起侍奉%MASTER_CALL()%了呀…♥♥」"',

    r'CALL MESSAGE_BOX,@"「ぐぅぅ♥ 被随心所欲地玩弄到高潮……」"':
    r'CALL MESSAGE_BOX,@"「咕呜♥ 被随心所欲地玩弄到高潮……」"',

    r'CALL MESSAGE_BOX,@"「あ、あぁ…ナカに…出され……うぅ…っ」"':
    r'CALL MESSAGE_BOX,@"「啊、啊啊…里面…被射了……呜呜…っ」"',

    # === 射精/尻穴 (lines 207-251) ===
    r'CALL MESSAGE_BOX,@"「んおぉぉ♥♥ 感谢使用肛门自慰器呀♥♥」"':
    r'CALL MESSAGE_BOX,@"「嗯哦哦♥♥ 感谢使用肛门自慰器呀♥♥」"',

    r'CALL MESSAGE_BOX,@"「んふぅ♥♥ 很高兴能完美履行肛门精液便所的职责呀♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「嗯呼♥♥ 很高兴能完美履行肛门精液便所的职责呀♥♥♥」"',

    r'CALL MESSAGE_BOX,@"「哼啊♥♥ あ゛っ♥ %SELF_CALL()%はぁ…♥ 哦♥ 哦♥ お゛ぉっ♥\n　ザーメン浣腸されて…んぐっ♥…アクメする変態れす…っ♥♥」"':
    r'CALL MESSAGE_BOX,@"「哼啊♥♥ 啊っ♥ %SELF_CALL()%哈…♥ 哦♥ 哦♥ 哦っ♥\n　被精液灌肠…嗯咕っ♥…绝顶的变态…っ♥♥」"',

    r'CALL MESSAGE_BOX,@"「はひぃ…♥♥ 因%MASTER_CALL()%的精液，肚子感觉好热呀……♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「哈咿…♥♥ 因%MASTER_CALL()%的精液，肚子感觉好热呀……♥♥♥」"',

    r'CALL MESSAGE_BOX,@"「あぅぅっ♥♥ 在%ANAL_CALL()%中射精后就要高潮了……嗯呃呀♥♥」"':
    r'CALL MESSAGE_BOX,@"「啊呜呜っ♥♥ 在%ANAL_CALL()%中射精后就要高潮了……嗯呃呀♥♥」"',

    r'CALL MESSAGE_BOX,@"「うれしい…♥ 在%ANAL_CALL()%中射出这么多，溢出来了呀……♥♥」"':
    r'CALL MESSAGE_BOX,@"「好开心…♥ 在%ANAL_CALL()%中射出这么多，溢出来了呀……♥♥」"',

    r'CALL MESSAGE_BOX,@"「あぁ、もっとぉ…♥♥ 好想让%MASTER_CALL()%把%ANAL_CALL()%浸满精液呀……♥♥」"':
    r'CALL MESSAGE_BOX,@"「啊啊、更多…♥♥ 好想让%MASTER_CALL()%把%ANAL_CALL()%浸满精液呀……♥♥」"',

    r'CALL MESSAGE_BOX,@"「…かっ、かんじしゅぎてっ……ッ♥♥\n　いきっ できな ……ひっ……ぎッッッッ♥♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「…感、感觉太强烈了っ……ッ♥♥\n　去 去不了……咿っ……咿ッッッッ♥♥♥♥」"',

    r'CALL MESSAGE_BOX,@"「おぉぉ～～♥♥ 精液中毒の%ANAL_CALL()%にザーメン塗りたくられてイぐぅっっっ！♥♥♥」"':
    r'CALL MESSAGE_BOX,@"「哦哦～～♥♥ 精液中毒的%ANAL_CALL()%被涂满精液要去っっっ！♥♥♥」"',

    r'CALL MESSAGE_BOX,@"「あぁ…♥ 知道精液被射出来了呀♥♥ %ANAL_CALL()%…♥ 好多呀……♥♥」"':
    r'CALL MESSAGE_BOX,@"「啊啊…♥ 知道精液被射出来了呀♥♥ %ANAL_CALL()%…♥ 好多呀……♥♥」"',

    r'CALL MESSAGE_BOX,@"「はふぅ♥ 请随时吩咐让%ANAL_CALL()%为您服务……♥♥」"':
    r'CALL MESSAGE_BOX,@"「哈呼♥ 请随时吩咐让%ANAL_CALL()%为您服务……♥♥」"',

    r'CALL MESSAGE_BOX,@"「あっ…嗯嗯……♥♥ 因在%ANAL_CALL()%中的射精而失去了理智……♥♥」"':
    r'CALL MESSAGE_BOX,@"「啊っ…嗯嗯……♥♥ 因在%ANAL_CALL()%中的射精而失去了理智……♥♥」"',

    r'CALL MESSAGE_BOX,@"「あ、あひぃっ♥♥ 因精液灌肠而肛门高潮了呀♥♥」"':
    r'CALL MESSAGE_BOX,@"「啊、啊咿っ♥♥ 因精液灌肠而肛门高潮了呀♥♥」"',

    r'CALL MESSAGE_BOX,@"「くぅ… こんなところに出されるなんて……」"':
    r'CALL MESSAGE_BOX,@"「呜… 竟然被射在这种地方……」"',

    r'CALL MESSAGE_BOX,@"「はぐぅっ♥ 在%ANAL_CALL()%中被射精后达到高潮……好变态的事情呀……♥♥」"':
    r'CALL MESSAGE_BOX,@"「哈咕っ♥ 在%ANAL_CALL()%中被射精后达到高潮……好变态的事情呀……♥♥」"',

    r'CALL MESSAGE_BOX,@"「呃……好不干净…… こんな……」"':
    r'CALL MESSAGE_BOX,@"「呃……好不干净…… 这样的……」"',

    r'CALL MESSAGE_BOX,@"「うぁあ♥ 居然在%ANAL_CALL()%中感觉到了……为什么会这样……♥」"':
    r'CALL MESSAGE_BOX,@"「呜啊♥ 居然在%ANAL_CALL()%中感觉到了……为什么会这样……♥」"',
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
