import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D

#df = pd.read_csv(r"C:\Users\usui0\Google ドライブ\プログラミング\PCA\0126_usui_5jes.csv") #notePC

df = pd.read_csv("all.csv") #desktopPC

df.columns=['1ch', '2ch', '3ch', '4ch', '5ch', '6ch', '7ch', '8ch', 'class']

X = df.iloc[:,0:8].values
y = df.iloc[:,8].values

#-1 - 1の範囲にする
X_std = StandardScaler().fit_transform(X)

pca = PCA(n_components=8) 

principalComponents = pca.fit_transform(X_std) 

principalDf = pd.DataFrame(data = principalComponents, columns = ['principal component 1', 'principal component 2','principal component 3','principal component 4','principal component 5','principal component 5','principal component 7','principal component 8']) 



print("主成分の分散説明率")
print(pca.explained_variance_ratio_)
print("固有ベクトル")
print(pca.components_)

finalDf = pd.concat([principalDf, df[['class']]], axis = 1)


# plt.figure(figsize = (8,6))

# plt.xlabel('Principal Component 1', fontsize = 15)
# plt.ylabel('Principal Component 2', fontsize = 15)


# targets = ['oya', 'hito', 'naka','kusuri','ko']
# colors = ['b', 'g', 'r','c','m']

# for target, color in zip(targets,colors):
#     indicesToKeep = finalDf['class'] == target
#     plt.scatter(finalDf.loc[indicesToKeep, 'principal component 1']
#                , finalDf.loc[indicesToKeep, 'principal component 2']
#                , c = color
#                , s = 50)

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

targets = ['oya', 'hito', 'naka','kusuri','ko']
colors = ['b', 'g', 'r','c','m']
for target, color in zip(targets,colors):
    indicesToKeep = finalDf['class'] == target
    ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1']
               , finalDf.loc[indicesToKeep, 'principal component 2']
               , finalDf.loc[indicesToKeep, 'principal component 3']
               , c = color
               , s = 50)


pc1 = pca.explained_variance_ratio_[0]
pc2 = pca.explained_variance_ratio_[1]
pc3 = pca.explained_variance_ratio_[1]
ans = (pc1+pc2+pc3)*100
plt.title('contribution ratio: %i percent'%ans,fontsize = 20)

plt.legend(targets)
plt.grid()

plt.show()

import seaborn as sns
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111)
sns.heatmap(pca.components_,
           cmap='Blues',
           annot=True,
           annot_kws={'size': 14},
           fmt='.2f',
           xticklabels=['ch1', 'ch2', 'ch3', 'ch4','ch5','ch6','ch7','ch8'],
           yticklabels=['PC1', 'PC2', 'PC3', 'PC4', 'PC5', 'PC6', 'PC7', 'PC8'],
           ax=ax)
plt.show()