# encoding: utf-8

#LED電球２個を使用する
#タクトスイッチ１個を使用する
#GPIOのピンは好きなものを使用してよい
#スイッチが押されるたびに、LED電球を交互に点灯させる

import RPi.GPIO as GPIO

SWITCH_PIN = 3
LED_PIN_1 = 23
LED_PIN_2 = 24

GPIO.setwarnings(False)
GPIO.cleanup()

GPIO.setmode(GPIO.BCM)
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED_PIN_1, GPIO.OUT)
GPIO.setup(LED_PIN_2, GPIO.OUT)

while True:
    if GPIO.input(SWITCH_PIN) == 0:
        if GPIO.input(LED_PIN_1) == GPIO.HIGH:
            GPIO.output(LED_PIN_1, GPIO.LOW)
            GPIO.output(LED_PIN_2, GPIO.HIGH)
        else:
            GPIO.output(LED_PIN_1, GPIO.HIGH)
            GPIO.output(LED_PIN_2, GPIO.LOW)

        while GPIO.input(SWITCH_PIN) == 0:
            pass
