"""a"""
from getkey import getkey
import random
import time
import os

hiragana_kana = {
    "あ": ["a"],
    "え": ["e"],
    "い": ["i"],
    "お": ["o"],
    "う": ["u"],
    "か": ["ka"],
    "け": ["ke"],
    "き": ["ki"],
    "こ": ["ko"],
    "く": ["ku"],
    "さ": ["sa"],
    "せ": ["se"],
    "し": ["shi"],
    "そ": ["so"],
    "す": ["su"],
    "た": ["ta"],
    "て": ["te"],
    "ち": ["chi"],
    "と": ["to"],
    "つ": ["tsu"],
    "な": ["na"],
    "ね": ["ne"],
    "に": ["ni"],
    "の": ["no"],
    "ぬ": ["nu"],
    "は": ["ha"],
    "へ": ["he"],
    "ひ": ["hi"],
    "ほ": ["ho"],
    "ふ": ["fu", "hu"],
    "ま": ["ma"],
    "め": ["me"],
    "み": ["mi"],
    "も": ["mo"],
    "む": ["mu"],
    "や": ["ya"],
    "よ": ["yo"],
    "ゆ": ["yu"],
    "ら": ["ra"],
    "れ": ["re"],
    "り": ["ri"],
    "ろ": ["ro"],
    "る": ["ru"],
    "わ": ["wa"],
    "を": ["wo"],
    "ん": ["n"],
    "が": ["ga"],
    "げ": ["ge"],
    "ぎ": ["gi"],
    "ご": ["go"],
    "ぐ": ["gu"],
    "ざ": ["za"],
    "ぜ": ["ze"],
    "じ": ["ji"],
    "ぞ": ["zo"],
    "ず": ["zu"],
    "だ": ["da"],
    "で": ["de"],
    "ぢ": ["di", "dzi"],
    "ど": ["do"],
    "づ": ["du", "dzu"],
    "ば": ["ba"],
    "べ": ["be"],
    "び": ["bi"],
    "ぼ": ["bo"],
    "ぶ": ["bu"],
    "ぱ": ["pa"],
    "ぺ": ["pe"],
    "ぴ": ["pi"],
    "ぽ": ["po"],
    "ぷ": ["pu"],
    "きゃ": ["kya"],
    "きょ": ["kyo"],
    "きゅ": ["kyu"],
    "ぎゃ": ["gya"],
    "ぎょ": ["gyo"],
    "ぎゅ": ["gyu"],
    "しゃ": ["sha", "shya"],
    "しょ": ["sho", "shyo"],
    "しゅ": ["shu", "shyu"],
    "じゃ": ["ja", "jya"],
    "じょ": ["jo", "jyo"],
    "じゅ": ["ju", "jyu"],
    "ちゃ": ["cha", "chya"],
    "ちょ": ["cho", "chyo"],
    "ちゅ": ["chu", "chyu"],
    "ぢゃ": ["dya"],
    "ぢょ": ["dyo"],
    "ぢゅ": ["dyu"],
    "にゃ": ["nya"],
    "にょ": ["nyo"],
    "にゅ": ["nyu"],
    "ひゃ": ["hya"],
    "ひょ": ["hyo"],
    "ひゅ": ["hyu"],
    "びゃ": ["bya"],
    "びょ": ["byo"],
    "びゅ": ["byu"],
    "ぴゃ": ["pya"],
    "ぴょ": ["pyo"],
    "ぴゅ": ["pyu"],
    "みゃ": ["mya"],
    "みょ": ["myo"],
    "みゅ": ["myu"],
    "りゃ": ["rya"],
    "りょ": ["ryo"],
    "りゅ": ["ryu"],
}

katakana_kana = {
    "ア": ["a"],
    "エ": ["e"],
    "イ": ["i"],
    "オ": ["o"],
    "ウ": ["u"],
    "カ": ["ka"],
    "ケ": ["ke"],
    "キ": ["ki"],
    "コ": ["ko"],
    "ク": ["ku"],
    "サ": ["sa"],
    "セ": ["se"],
    "シ": ["shi"],
    "ソ": ["so"],
    "ス": ["su"],
    "タ": ["ta"],
    "テ": ["te"],
    "チ": ["chi"],
    "ト": ["to"],
    "ツ": ["tsu"],
    "ナ": ["na"],
    "ネ": ["ne"],
    "ニ": ["ni"],
    "ノ": ["no"],
    "ヌ": ["nu"],
    "ハ": ["ha"],
    "へ": ["he"],
    "ヒ": ["hi"],
    "ホ": ["ho"],
    "ふ": ["fu", "hu"],
    "マ": ["ma"],
    "メ": ["me"],
    "ミ": ["mi"],
    "モ": ["mo"],
    "ム": ["mu"],
    "ヤ": ["ya"],
    "ヨ": ["yo"],
    "ユ": ["yu"],
    "ラ": ["ra"],
    "レ": ["re"],
    "リ": ["ri"],
    "ロ": ["ro"],
    "ル": ["ru"],
    "ワ": ["wa"],
    "ヲ": ["wo"],
    "ン": ["n"],
    "ガ": ["ga"],
    "ゲ": ["ge"],
    "ギ": ["gi"],
    "ゴ": ["go"],
    "グ": ["gu"],
    "ザ": ["za"],
    "ゼ": ["ze"],
    "ジ": ["ji"],
    "ゾ": ["zo"],
    "ズ": ["zu"],
    "ダ": ["da"],
    "デ": ["de"],
    "ヂ": ["di", "dzi"],
    "ド": ["do"],
    "ヅ": ["du", "dzu"],
    "バ": ["ba"],
    "ベ": ["be"],
    "ビ": ["bi"],
    "ボ": ["bo"],
    "ブ": ["bu"],
    "パ": ["pa"],
    "ぺ": ["pe"],
    "ピ": ["pi"],
    "ポ": ["po"],
    "プ": ["pu"],
    "キャ": ["kya"],
    "キョ": ["kyo"],
    "キュ": ["kyu"],
    "ギャ": ["gya"],
    "ギョ": ["gyo"],
    "ギュ": ["gyu"],
    "シャ": ["sha", "shya"],
    "ショ": ["sho", "shyo"],
    "シュ": ["shu", "shyu"],
    "ジャ": ["ja", "jya"],
    "ジョ": ["jo", "jyo"],
    "ジュ": ["ju", "jyu"],
    "チャ": ["cha", "chya"],
    "チョ": ["cho", "chyo"],
    "チュ": ["chu", "chyu"],
    "ヂャ": ["dya"],
    "ヂョ": ["dyo"],
    "ヂュ": ["dyu"],
    "ニャ": ["nya"],
    "ニョ": ["nyo"],
    "ニュ": ["nyu"],
    "ヒャ": ["hya"],
    "ヒョ": ["hyo"],
    "ヒュ": ["hyu"],
    "ビャ": ["bya"],
    "ビョ": ["byo"],
    "ビュ": ["byu"],
    "ピャ": ["pya"],
    "ピョ": ["pyo"],
    "ピュ": ["pyu"],
    "ミャ": ["mya"],
    "ミョ": ["myo"],
    "ミュ": ["myu"],
    "リャ": ["rya"],
    "リョ": ["ryo"],
    "リュ": ["ryu"],
    "ヴァ": ["va"],
    "ヴェ": ["ve"],
    "ヴィ": ["vi"],
    "ヴォ": ["vo"],
    "ウェ": ["we"],
    "ウィ": ["wi"],
    "ウォ": ["uxo", "wo"],
    "ファ": ["fa"],
    "フェ": ["fe"],
    "フィ": ["fi"],
    "フォ": ["fo"],
    "ツァ": ["tsa"],
    "ツェ": ["tse"],
    "ツィ": ["tsi"],
    "ツォ": ["tso"],
    "シェ": ["she"],
    "ジェ": ["je"],
    "チェ": ["che"],
    "ティ": ["thi"],
    "ディ": ["dhi"],
    "トゥ": ["twu"],
    "ドゥ": ["dwu"],
}
os.system("clear")
print("KANA TEST\n")
while True:
    hiragana_or_katakana = input("Hiragana (1) or Katakana (2): ")
    if hiragana_or_katakana in ["1","2"]:
        break

def hiragana_test():
    # hiragana test
    os.system("clear")
    test_info = {i:[0.0, 0] for i in hiragana_kana}
    questions = list(hiragana_kana.keys()).copy()
    random.shuffle(questions)
    for q in questions:
        os.system("clear")
        print("TESTING HIRAGANA ({} left)\n".format(len(questions)-questions.index(q)))
        print("KANA:", q)
        start_time = time.time()
        while True:
            answer = input("Romaji: ")
            if answer != '':
                break
        if answer == "babababa":
            break
        if answer in ["bababababa", "babababara"]:
            if answer == 'bababababa':
                for j in test_info:
                    test_info[j][1] = 1
                    test_info[j][0] = 0.5
            else:
                for j in test_info:
                    test_info[j][1] = random.choice([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0])
                    test_info[j][0] = random.random()*5
            break
        if answer in hiragana_kana[q]:
            test_info[q][1] = 1
            print("Correct!")
        elif answer not in hiragana_kana[q]:
            print("Incorrect. The correct answer was '" + hiragana_kana[q][0] + "'.")
        test_info[q][0] = time.time() - start_time
        key = ""
        while True:
            key = getkey()
            if key == '\n':
                break
    
    score = 0

    for kana in test_info:
        print(kana + ": Answered in", str(test_info[kana][0])[:str(test_info[kana][0]).index(".")+2] + "s. ", end='')
        if test_info[kana][1] == 1:
            print("You got it right!")
            score += 1
        elif test_info[kana][1] == 0:
            print("You got it wrong.")
    print('\nYour grade:', str(score/len(hiragana_kana)*100)[:5] + '%')


def katakana_test():
    # katakana test
    os.system("clear")
    test_info = {i:[0.0, 0] for i in katakana_kana}
    questions = list(katakana_kana.keys()).copy()
    random.shuffle(questions)
    for q in questions:
        os.system("clear")
        print("TESTING KATAKANA ({} left)\n".format(len(questions)-questions.index(q)))
        print("KANA:", q)
        start_time = time.time()
        while True:
            answer = input("Romaji: ")
            if answer != '':
                break
        if answer == "babababa":
            break
        if answer in katakana_kana[q]:
            test_info[q][1] = 1
            print("Correct!")
        elif answer not in katakana_kana[q]:
            print("Incorrect. The correct answer was '" + katakana_kana[q][0] + "'.")
        test_info[q][0] = time.time() - start_time
        key = ""
        while True:
            key = getkey()
            if key == '\n':
                break
    
    score = 0

    for kana in test_info:
        print(kana + ": Answered in", str(test_info[kana][0])[:str(test_info[kana][0]).index(".")+2] + "s. ", end='')
        if test_info[kana][1] == 1:
            print("You got it right!")
            score += 1
        elif test_info[kana][1] == 0:
            print("You got it wrong.")
    print('\nYour grade:', str(score/len(katakana_kana)*100)[:5] + '%')
if hiragana_or_katakana == "1":
    hiragana_test()
elif hiragana_or_katakana == "2":
    katakana_test()
# elif hiragana_or_katakana == "2":
#     # katakana test
