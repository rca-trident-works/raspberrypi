# encoding: utf-8

#LED電球１個を使用する
#タクトスイッチ２個を使用する
#GPIOのピンは好きなものを使用してよい
#スイッチが押されていない間は、LED電球を消灯させる
#スイッチが片方だけ押されている間は、LED電球を0.1秒間隔で点滅させる
#スイッチが両方とも押されている間は、LED電球を点灯させる

import RPi.GPIO as GPIO
import time

SWITCH_PIN_1 = 23
SWITCH_PIN_2 = 24
LED_PIN = 3

GPIO.setwarnings(False)
GPIO.cleanup()

GPIO.setmode(GPIO.BCM)
GPIO.setup(SWITCH_PIN_1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SWITCH_PIN_2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(LED_PIN, GPIO.OUT)

while True:
    if GPIO.input(SWITCH_PIN_1) == 1 and GPIO.input(SWITCH_PIN_2) == 1:
        GPIO.output(LED_PIN, GPIO.LOW)
    elif GPIO.input(SWITCH_PIN_1) == 0 and GPIO.input(SWITCH_PIN_2) == 0:
        GPIO.output(LED_PIN, GPIO.HIGH)
    else:
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(0.1)
