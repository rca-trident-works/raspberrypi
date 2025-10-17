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
# GPIO4のピンを出力に設定
GPIO.setup(4, GPIO.OUT)
 
 
# 無限ループにする
while True:
    # スイッチが押されているか判定
    if GPIO.input(9) == 0:
         # GPIO4をHIGHにする
         GPIO.output(4, GPIO.HIGH)
    else:
        # GPIO4をLOWにする
        GPIO.output(4, GPIO.LOW)
    time.sleep(0.5)  # 0.5秒待機する
