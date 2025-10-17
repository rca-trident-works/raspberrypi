# coding: utf-8
# 2球のLEDを2秒間隔で交互に点滅

import RPi.GPIO as GPIO
import time

LED_PIN_1 = 23
LED_PIN_2 = 24

GPIO.setwarnings(False)
GPIO.cleanup()

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN_1, GPIO.OUT)
GPIO.setup(LED_PIN_2, GPIO.OUT)

while True:
    GPIO.output(LED_PIN_1, GPIO.HIGH)
    GPIO.output(LED_PIN_2, GPIO.LOW)
    time.sleep(2)
    GPIO.output(LED_PIN_1, GPIO.LOW)
    GPIO.output(LED_PIN_2, GPIO.HIGH)
    time.sleep(2)
