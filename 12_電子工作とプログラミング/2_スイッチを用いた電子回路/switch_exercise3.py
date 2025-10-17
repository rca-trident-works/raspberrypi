# encoding: utf-8

# TODO: テスト(パーツ不足のため)

#LED電球５個（赤x2・黄・緑x2）を使用する
#タクトスイッチ１個を使用する
#GPIOのピンは好きなものを使用してよい
#プログラム起動直後に、「歩行者信号」側の赤色のLED電球を点灯させ、「自動車信号」側の緑色のLED電球を点灯させる
#スイッチが押された場合、⑥～⑫の順に動作する（押されない場合は④の状態を継続）
#その5秒後に「自動車信号」側の緑色のLED電球を消灯し、黄色のLED電球を点灯させる
#その2秒後に「自動車信号」側の黄色のLED電球を消灯し、赤色のLED電球を点灯させる
#その1秒後に「歩行者信号」側の赤色のLED電球を消灯し、緑色のLED電球を点灯させる
#その10秒後に「歩行者信号」側の緑色のLED電球を0.5秒間隔で点滅させる
#その5秒後に「歩行者信号」側の緑色のLED電球を消灯し、赤色のLED電球を点灯させる
#その1秒後に「自動車信号」側の赤色のLED電球を消灯し、緑色のLED電球を点灯させる
#⑤へ戻る
#⑥～⑫動作中にスイッチが押されても動作に影響がないようにする

import RPi.GPIO as GPIO
import time

# Helper function to set up multiple output pins
def setup_out_pins(pin_list):
    for pin in pin_list:
        GPIO.setup(pin, GPIO.OUT)

LED_PIN_RED_1 = 23
LED_PIN_RED_2 = 24
LED_PIN_YELLOW = 25
LED_PIN_GREEN_1 = 8
LED_PIN_GREEN_2 = 7
SWITCH_PIN = 3

GPIO.setwarnings(False)
GPIO.cleanup()

GPIO.setmode(GPIO.BCM)
setup_out_pins([LED_PIN_RED_1, LED_PIN_RED_2, LED_PIN_YELLOW, LED_PIN_GREEN_1, LED_PIN_GREEN_2])
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    # Initial state
    GPIO.output(LED_PIN_RED_1, GPIO.HIGH)
    GPIO.output(LED_PIN_GREEN_2, GPIO.HIGH)
    # Wait for switch press
    while GPIO.input(SWITCH_PIN) == 1:
        pass
    # Sequence of light changes
    time.sleep(5)
    GPIO.output(LED_PIN_GREEN_2, GPIO.LOW)
    GPIO.output(LED_PIN_YELLOW, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(LED_PIN_YELLOW, GPIO.LOW)
    GPIO.output(LED_PIN_RED_2, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(LED_PIN_RED_1, GPIO.LOW)
    GPIO.output(LED_PIN_GREEN_1, GPIO.HIGH)
    time.sleep(10)
    for _ in range(10):
        GPIO.output(LED_PIN_GREEN_1, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(LED_PIN_GREEN_1, GPIO.HIGH)
        time.sleep(0.5)
    time.sleep(5)
    GPIO.output(LED_PIN_GREEN_1, GPIO.LOW)
    GPIO.output(LED_PIN_RED_1, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(LED_PIN_RED_2, GPIO.LOW)
    GPIO.output(LED_PIN_GREEN_2, GPIO.HIGH)
