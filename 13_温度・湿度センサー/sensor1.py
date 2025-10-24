# coding: utf-8
 
import Adafruit_DHT as DHT
import time
 
 
while True:
    try:
        # GPIO14で温度と湿度を取得
        h, t = DHT.read_retry(DHT.DHT22, 14)
 
        # 結果出力
        print("温度={0:0.1f}℃, 湿度={1:0.1f}％".format(t, h))
 
        # 1秒間待機
        time.sleep(1)
    except KeyboardInterrupt:
        print("計測を終了しました")
        break
