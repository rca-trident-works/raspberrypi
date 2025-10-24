# coding: utf-8
 
# Matplotlib関連のライブラリのインポート
import matplotlib.pyplot as plt
import numpy as np

# xの変域を-10 < x < 10とし、刻みを0.1とする
# x座標の描画範囲を指定
x = np.arange(-10,  10,  0.1)

# 関数 y = x^2 + 5x + 1 を定義
y = x**2 + 5*x + 1
 
plt.plot(x,  y)   # 関数をグラフにプロット
plt.show()        # グラフを描画する
