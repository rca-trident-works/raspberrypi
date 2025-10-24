# coding: utf-8
 
# Matplotlib関連のライブラリのインポート
import matplotlib.pyplot as plt
import numpy as np
 
# xの変域を0 < x < 10とし、刻みを0.1とする
# x座標の描画範囲を指定
x = np.arange(0, 10, 0.1)
 
# 関数 y = 2x を定義
y = 2  *  x
 
plt.plot(x,  y)   # 関数をグラフにプロット
plt.show()        # グラフを描画する
