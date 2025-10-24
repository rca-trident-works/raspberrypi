# coding: utf-8
 
import Adafruit_DHT as DHT
import time
 
import scratch
 
# Scratchと通信をするための情報を定義
sc = scratch.Scratch(host='localhost')
# Scratchとの通信を開始
sc.connect()
 
while True:
    try:
        # GPIO14で温度と湿度を取得
        h, t = DHT.read_retry(DHT.DHT22, 14)
        
        # 温度の情報をScratchに送信する
        sc.sensorupdate({'t' : t})
        # 湿度の情報をScratchに送信する
        sc.sensorupdate({'h' : h})
 
        # 0.5秒間待機
        time.sleep(0.5)
    except KeyboardInterrupt:
        print("計測を終了しました")
        break
 
# Scratchとの通信を切断
sc.disconnect()
