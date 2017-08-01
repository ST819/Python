# coding: utf-8
from time import sleep
import datetime
import locale
cmd = input(">>>")
if cmd == '起動':
    print("起動中...")
    sleep(3)
    print("起動完了")
    print("あなたの名前を教えて下さい")
    name = input(">>>")
    print ("よろしくお願いします",name)
    print("次に、私の名前を決めてください")
    namae=input(">>>")
    print(namae,"でよろしいですか？")
    yes=input(">>>")
    if yes =='はい':
        print("今日から私は",namae,"です")
    elif yes =='いいえ':
        print("名前をもう一度決めるため、再起動してください")
    else:
        print("コマンドを認識できません")
    cmd1 = input(">>>")
    if cmd1 == 'こんにちは': #helloに対する答え
        print("こんにちは！",name)
        print("あなたは何か今日予定がありますか？")
        plans=input(">>>")
        print("あなたは今日",plans,"をする予定なのですね")
    elif cmd1 == 'よろしくお願いします': #nice to meet you に対する答え
        print ("私もよろしくお願いします",name)
        sleep(2)
        print("今の天気を教えて下さい")
        weather=input(">>>")
        print("今日の天気は",weather,"ですか")
    elif cmd1 == "あなたの名前を教えて下さい": #What's your name?　に対する答え
        print("私の名前はまだありません")
        sleep(2)
        print("私はあなたのコンサルタントです")
        print("何かわたしにできることはありますか？")
        kotae=input(">>>")
        if kotae == 'はい':
            print("何をしましょう？")
        elif kotae == 'いいえ':
            print("分かりました")
    elif cmd1 == "頼みがあるんだけど": #To be trusted に対する答え
        print("何をしましょう？")
        tanomi=input(">>>")
        if tanomi == '買い物をして':#買い物を頼む
            print("私には手がないので買い物ができません")
        elif tanomi == '今の時間を教えて':#時間を聞く
            d = datetime.datetime.today()
            print("今の時間は %s:%s　です" % (d.hour, d.minute))
    else:
        print("すみません言葉の意味がわかりません")
elif cmd == '終了':
    print("さようなら")
    sleep(3)
    print("完了")
elif cmd == 'セーフモード':
    print("セーフモードで起動します")
    sleep(3)
    print("起動完了")
else:
    print("エラー")
    print("このコマンドを認識できません")