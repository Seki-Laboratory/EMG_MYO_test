import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


List0=np.loadtxt('MRMSdata0.csv', delimiter=',')
List1=np.loadtxt('MRMSdata1.csv', delimiter=',')
List2=np.loadtxt('MRMSdata2.csv', delimiter=',')
List3=np.loadtxt('MRMSdata3.csv', delimiter=',')
List4=np.loadtxt('MRMSdata4.csv', delimiter=',')

# 3D散布図でプロットするデータを生成する為にnumpyを使用
#145
# X0 = List0 [:,0]
# Y0 = List0 [:,3]
# Z0 = List0 [:,4]

# X1 = List1 [:,0]
# Y1 = List1 [:,3]
# Z1 = List1 [:,4]

# X2 = List2 [:,0]
# Y2 = List2 [:,3]
# Z2 = List2 [:,4]

# X3 = List3 [:,0]
# Y3 = List3 [:,3]
# Z3 = List3 [:,4]

# X4 = List4 [:,0]
# Y4 = List4 [:,3]
# Z4 = List4 [:,4]

#245
# X0 = List0 [:,1]
# Y0 = List0 [:,3]
# Z0 = List0 [:,4]

# X1 = List1 [:,1]
# Y1 = List1 [:,3]
# Z1 = List1 [:,4]

# X2 = List2 [:,1]
# Y2 = List2 [:,3]
# Z2 = List2 [:,4]

# X3 = List3 [:,1]
# Y3 = List3 [:,3]
# Z3 = List3 [:,4]

# X4 = List4 [:,1]
# Y4 = List4 [:,3]
# Z4 = List4 [:,4]


#817
X0 = List0 [:,7]
Y0 = List0 [:,0]
Z0 = List0 [:,6]

X1 = List1 [:,7]
Y1 = List1 [:,0]
Z1 = List1 [:,6]

X2 = List2 [:,7]
Y2 = List2 [:,0]
Z2 = List2 [:,6]

X3 = List3 [:,7]
Y3 = List3 [:,0]
Z3 = List3 [:,6]

X4 = List4 [:,7]
Y4 = List4 [:,0]
Z4 = List4 [:,6]
# グラフの枠を作成
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# X,Y,Z軸にラベルを設定
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

# .plotで描画
ax.plot(X0,Y0,Z0,"o",color='blue')
ax.plot(X1,Y1,Z1,"o",color='green')
ax.plot(X2,Y2,Z2,"o",color='red')
ax.plot(X3,Y3,Z3,"o",color='cyan')
ax.plot(X4,Y4,Z4,"o",color='magenta')

# 最後に.show()を書いてグラフ表示
plt.show()