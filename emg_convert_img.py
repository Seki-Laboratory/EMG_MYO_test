import numpy as np
import cv2
import matplotlib.pyplot as plt

# for i in range(1,11):

#RMSList=np.loadtxt('jes/nigiru_test/'+str(1)+'.csv', delimiter=',')
RMSList=np.loadtxt('MRMSdata0.csv', delimiter=',')

img_gray = np.array(RMSList [1:400,0:8], dtype = np.uint8)

# #画像の表示
plt.imshow(img_gray, cmap = 'gray', vmin = 0, vmax = 20, interpolation = 'none')
plt.show()

    #cv2.imwrite('img/shoukutu_test'+ str(i) +'.jpg', img_gray)
# cv2.imwrite('test1.jpg', img_gray)
# print(RMSList)