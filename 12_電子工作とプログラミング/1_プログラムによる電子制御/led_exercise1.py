# coding: utf-8
# 1球のLEDを0.5秒間隔で点滅(GPIO 24)

import RPi.GPIO as GPIO
import time

LED_PIN = 24

GPIO.setwarnings(False)
GPIO.cleanup()

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

while True:
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(0.5)
