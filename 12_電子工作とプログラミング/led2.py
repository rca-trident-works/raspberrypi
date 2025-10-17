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
# GPIO4のピンを出力に設定 
GPIO.setup(4, GPIO.OUT)
 
 
# 無限ループにする
while True:
    # GPIO4をHIGHにする
    GPIO.output(4, GPIO.HIGH)
    time.sleep(1)  # 1秒待機する
    # GPIO4をLOWにする
    GPIO.output(4, GPIO.LOW)
    time.sleep(1)  # 1秒待機する
