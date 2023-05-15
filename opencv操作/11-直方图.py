
'''
掩膜、掩码  [指定特定的区域]

cv2.calcHist
'''
import cv2

import matplotlib.pyplot as plt
img = cv2.imread('dog.jpg',0)


# img, 通道  掩膜（某个部分，none 指的是全图）
img1 = cv2.calcHist([img],[0],None,[256],[0,256])
print(img1.shape)
# cv2.imshow('img', img1)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()


plt.figure(figsize=(10,8))
plt.plot(img1, color='b')

plt.xlim([0,256])
plt.show()