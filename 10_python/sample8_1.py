# coding: utf-8

# randomライブラリのインポート
import random

# おみくじを引く
omikuji = random.randint(1, 3)

# おみくじの結果
if omikuji == 1:
    print("大吉")
elif omikuji == 2:
    print("吉")
elif omikuji == 3:
    print("凶")
