# Optimal_Order_Calculator
アサルトリリィラストバレットにおいて，レギオン内で"最適"なオーダーの組み合わせを求めよう！！

# 開発環境
WSL Ubuntu 18.04.5 LTS
Python 3.6.9

## 外部モジュール
- discord.py
- Pillow
- gspread
- oauth2client

# 実行について

$ python ./main.py

※実行するには、botディレクトリにtoken.txtを配置し、中にbotのトークンを記述してください。

※現時点で、bot/Sourcesディレクトリ内で実行しないとtoken.txtを見つけられずerrorになります（修正方法要検討）

# 現在使えるコマンド

.もゆさまおるかー

テキストチャットに百由様を呼ぶ。

最初にこれを実行しないと他のコマンドを使えない。


.picture

botに画像を送信するテスト。


.じゃあの

botを終了


.add player

自身をプレイヤーとして登録


.remove player

自身の登録データを削除