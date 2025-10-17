# coding: utf-8
 
# timeライブラリのインポート
import time
 
# GPIOのライブラリのインポート
import RPi.GPIO as GPIO
 
# GPIO初期化時の警告メッセージを非表示にする
GPIO.setwarnings(False)
# GPIOの初期化
GPIO.cleanup()
# GPIOの番号でピンを指定する
GPIO.setmode(GPIO.BCM)
# GPIO9のピンを入力に設定
GPIO.setup(9, GPIO.IN, pull_up_down=GPIO.PUD_UP)
 
# スイッチを押した回数
count = 0
 
 
# 無限ループにする
while True:
    # スイッチが押されてか判定する
    if GPIO.input(9) == 0:
         # スイッチを押した回数を増やす
         count = count + 1
         print("スイッチが" + str(count) + "回押されました")
 
         # スイッチが離されるまで無限に待機する
         while GPIO.input(9) == 0:
             time.sleep(0.1)  # 0.1秒待機する
