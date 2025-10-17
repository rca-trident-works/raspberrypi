# coding: utf-8
# 応用問題

#LED電球３個（赤・黄・緑）を使用する
#GPIOのピンは好きなものを使用してよい
#プログラム起動直後に、赤色のLED電球を点灯させる
#その3秒後に、赤色のLED電球を消灯し、緑色のLED電球を点灯させる
#その5秒後に、緑色のLED電球を0.5秒間隔で点滅させる
#その5秒後に、緑色のLED電球を消灯し、黄色のLED電球を点灯させる
#その2秒後に、黄色のLED電球を消灯し、赤色のLED電球を点灯させる（④へ戻る）


import RPi.GPIO as GPIO
import time

LED_PIN_R = 23 # Red
LED_PIN_G = 24 # Green
LED_PIN_Y = 25 # Yellow

GPIO.setwarnings(False)
GPIO.cleanup()

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN_R, GPIO.OUT)
GPIO.setup(LED_PIN_G, GPIO.OUT)
GPIO.setup(LED_PIN_Y, GPIO.OUT)

while True:
    # 赤色LED点灯
    GPIO.output(LED_PIN_R, GPIO.HIGH)
    time.sleep(3)
    # 赤色LED消灯、緑色LED点灯
    GPIO.output(LED_PIN_R, GPIO.LOW)
    GPIO.output(LED_PIN_G, GPIO.HIGH)
    time.sleep(5)
    # 緑色LED点滅
    end_time = time.time() + 5
    while time.time() < end_time:
        GPIO.output(LED_PIN_G, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(LED_PIN_G, GPIO.HIGH)
        time.sleep(0.5)
    # 緑色LED消灯、黄色LED点灯
    GPIO.output(LED_PIN_G, GPIO.LOW)
    GPIO.output(LED_PIN_Y, GPIO.HIGH)
    time.sleep(2)
    # 黄色LED消灯、赤色LED点灯へ戻る
    GPIO.output(LED_PIN_Y, GPIO.LOW)

