import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 3D散布図でプロットするデータを生成する為にnumpyを使用
X = np.array([i for i in range(1,100)]) # 自然数の配列
Y = np.sin(X) # 特に意味のない正弦
Z = np.sin(Y) # 特に意味のない正弦

# グラフの枠を作成
fig = plt.figure()
ax = Axes3D(fig)

# X,Y,Z軸にラベルを設定
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

# .plotで描画
ax.plot(X,Y,Z,marker="o",linestyle='None')

# 最後に.show()を書いてグラフ表示
plt.show()