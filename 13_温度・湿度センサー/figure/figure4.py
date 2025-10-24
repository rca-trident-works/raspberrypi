# coding: utf-8
 
# Matplotlib関連のライブラリのインポート
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
 
# グラフに描画するデータ
df = pd.DataFrame(
  {
    'x': [10, 20, 30],     # x軸の刻み
    'a': [150, 300, 250],  # a系列のデータ
    'b': [250, 100, 200]   # b系列のデータ
  }
)
 
# プロットの構成要素（レイアウト・オブジェクト）を取得
# 変数figはウィンドウ
# 変数axはグラフの描画領域
fig, ax = plt.subplots(figsize=(7, 5))
 
# x軸のオブジェクトを設定
df.set_index('x').plot(
  ax = ax,        # 取得したグラフ領域を使用
  kind='line',    # 折れ線グラフとして表示
  legend = True,  # 凡例を表示
)
 
ax.set_title('Sample Figure')  # タイトル
ax.set_ylabel('y')             # y軸のラベル
 
# グラフを描画する
plt.show()
 
 
# プロットの構成要素（レイアウト・オブジェクト）を取得
fig, ax = plt.subplots(figsize=(7, 5))
 
ax.plot(df.x, df.a)   # a系列をグラフにプロット
ax.plot(df.x, df.b)   # b系列をグラフにプロット
 
ax.legend()                    # 凡例を表示
ax.set_title('Sample Figure')  # タイトル
ax.set_xlabel('x')             # x軸のラベル
ax.set_ylabel('y')             # y軸のラベル
 
# 既に描画したグラフに重ねてさらにグラフを描画する
plt.show()
