# coding: utf-8
 
# Adafruit_DHTライブラリのインポート
import Adafruit_DHT as DHT
 
# numpyライブラリのインポート
import numpy as np
# pandasライブラリのインポート
import pandas as pd
 
# matplotlibライブラリのインポート
from matplotlib import pyplot as plt
from matplotlib import animation
 
 
# グラフの描画を更新する関数
def update_fig(frame, figdata, sensor_pin):
    # GPIO14のピンで温度と湿度を取得
    h, t = DHT.read_retry(DHT.DHT22, sensor_pin)
 
    # グラフデータにそれぞれの値を追加する
    figdata['x'].append(frame)   # 現在のフレーム数（X座標）
    figdata['t'].append(int(t))  # 温度のデータ追加
    figdata['h'].append(int(h))  # 湿度のデータ追加
 
    plt.cla()    # 現在描画しているグラフを消去
 
    # グラフデータからグラフ領域を定義
    df = pd.DataFrame(figdata) 
 
 
    # ----------------------------- #
    # 1行2列のグラフを定義する
    # ----------------------------- #   
 
    # 温度の情報に関するグラフ（1行2列の左側に描画）
    plt.subplot(1, 2, 1)
    plt.plot(
        df.x, df.t, color='red',
        linestyle='solid', linewidth = 2.0
    )
    # タイトル
    plt.title('Temperature(C)')
 
    # 湿度の情報に関するグラフ（1行2列の右側に描画）
    plt.subplot(1, 2, 2)
    plt.plot(
        df.x, df.h, color='blue',
        linestyle='dashed', linewidth = 2.0
    )
    # タイトル
    plt.title('Humidity(%)')
 
 
 
# ----------------------------- #
# グラフに関する変数を定義する
# ----------------------------- #
 
# グラフの描画領域（幅、高さ）
FIG = plt.figure(figsize=(10, 5))
 
# 温湿度センサーのGPIOピン
SENSOR_PIN = 14
 
# グラフデータ（初期状態）
FIGDATA = {
    'x': [],    # X座標
    't': [],    # 温度
    'h': []     # 湿度
}
 
# グラフのアニメーション用のパラメータ
params = {
    'fig': FIG,         # グラフの描画領域
    'interval': 10,     # 10ミリ秒間隔で関数を呼び出す
    'func': update_fig, # グラフの描画を更新する関数を指定する
    'fargs': (FIGDATA, SENSOR_PIN),  # 関数へ渡す引数
 
    # フレーム番号を生成するイテレータ
    # x座標の0～100の範囲でグラフを描画する（増減値：0.1）
    'frames': np.arange(0, 100, 0.1),  
    'repeat': False,    # 繰り返し実行を禁止する
}
 
# グラフのアニメーションを開始する
# update_fig関数を連続で呼び出す
anime = animation.FuncAnimation(**params)
 
# グラフを描画する
plt.show()
