import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


list0=np.loadtxt('MRMSdata0.csv', delimiter=',')
list1=np.loadtxt('MRMSdata1.csv', delimiter=',')
list2=np.loadtxt('MRMSdata2.csv', delimiter=',')
list3=np.loadtxt('MRMSdata3.csv', delimiter=',')
# list4=np.loadtxt('MRMSdata4.csv', delimiter=',')

L0 = np.sum(list0,axis=0)
L1 = np.sum(list1,axis=0)
L2 = np.sum(list2,axis=0)
L3 = np.sum(list3,axis=0)
# L4 = np.sum(list4,axis=0)

List0 = L0/50
List1 = L1/50
List2 = L2/50
List3 = L3/50
# List4 = L4/50


# Lista = np.vstack((List0,List1,List2,List3,List4))
# 3D散布図でプロットするデータを生成する為にnumpyを使用
145
X0 = list0 [:,0]
Y0 = list0 [:,3]
Z0 = list0 [:,4]

X1 = list1 [:,0]
Y1 = list1 [:,3]
Z1 = list1 [:,4]

X2 = list2 [:,0]
Y2 = list2 [:,3]
Z2 = list2 [:,4]

X3 = list3 [:,0]
Y3 = list3 [:,3]
Z3 = list3 [:,4]

# X4 = list4 [:,0]
# Y4 = list4 [:,3]
# Z4 = list4 [:,4]
#重心用
ZX0 = List0 [0]
ZY0 = List0 [3]
ZZ0 = List0 [4]

ZX1 = List1 [0]
ZY1 = List1 [3]
ZZ1 = List1 [4]

ZX2 = List2 [0]
ZY2 = List2 [3]
ZZ2 = List2 [4]

ZX3 = List3 [0]
ZY3 = List3 [3]
ZZ3 = List3 [4]

# ZX4 = List4 [0]
# ZY4 = List4 [3]
# ZZ4 = List4 [4]

# 245
# X0 = list0 [:,1]
# Y0 = list0 [:,3]
# Z0 = list0 [:,4]

# X1 = list1 [:,1]
# Y1 = list1 [:,3]
# Z1 = list1 [:,4]

# X2 = list2 [:,1]
# Y2 = list2 [:,3]
# Z2 = list2 [:,4]

# X3 = list3 [:,1]
# Y3 = list3 [:,3]
# Z3 = list3 [:,4]

# X4 = list4 [:,1]
# Y4 = list4 [:,3]
# Z4 = list4 [:,4]

#重心用
# ZX0 = List0 [1]
# ZY0 = List0 [3]
# ZZ0 = List0 [4]

# ZX1 = List1 [1]
# ZY1 = List1 [3]
# ZZ1 = List1 [4]

# ZX2 = List2 [1]
# ZY2 = List2 [3]
# ZZ2 = List2 [4]

# ZX3 = List3 [1]
# ZY3 = List3 [3]
# ZZ3 = List3 [4]

# ZX4 = List4 [1]
# ZY4 = List4 [3]
# ZZ4 = List4 [4]


#817
# X0 = List0 [:,7]
# Y0 = List0 [:,0]
# Z0 = List0 [:,6]

# X1 = List1 [:,7]
# Y1 = List1 [:,0]
# Z1 = List1 [:,6]

# X2 = List2 [:,7]
# Y2 = List2 [:,0]
# Z2 = List2 [:,6]

# X3 = List3 [:,7]
# Y3 = List3 [:,0]
# Z3 = List3 [:,6]

# X4 = List4 [:,7]
# Y4 = List4 [:,0]
# Z4 = List4 [:,6]
# グラフの枠を作成
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# X,Y,Z軸にラベルを設定
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

# .plotで描画
#重心
ax.plot([ZX0],[ZY0],[ZZ0],ms=30,marker="^",color='blue')
ax.plot([ZX1],[ZY1],[ZZ1],ms=30,marker="^",color='green')
ax.plot([ZX2],[ZY2],[ZZ2],ms=30,marker="^",color='red')
ax.plot([ZX3],[ZY3],[ZZ3],ms=30,marker="^",color='cyan')
# ax.plot([ZX4],[ZY4],[ZZ4],ms=30,marker="^",color='magenta')
#全体
ax.plot(X0,Y0,Z0,"o",color='blue')
ax.plot(X1,Y1,Z1,"o",color='green')
ax.plot(X2,Y2,Z2,"o",color='red')
ax.plot(X3,Y3,Z3,"o",color='cyan')
# ax.plot(X4,Y4,Z4,"o",color='magenta')


# np.set_printoptions(threshold=np.inf)
# print(Lista)

# 最後に.show()を書いてグラフ表示
plt.show()