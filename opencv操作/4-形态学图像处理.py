import cv2
import numpy as np


img1 = cv2.imread('demo.png', 0)
# 白色为255  即：越亮数值越大
# 黑色为0
print(img1)

# 设置卷积核
ke = np.ones((5,5), np.uint8)

# 腐蚀  （消除毛刺）
img_fs = cv2.erode(img1, ke, iterations=1)
cv2.imshow('img_fs', img_fs)

# 膨胀  (扩大细节)
img_pz = cv2.dilate(img1, ke, iterations=5)
cv2.imshow('img_pz', img_pz)

# todo  morphology 形态学
# 开运算  先腐蚀--再膨胀   （消除毛刺）
img_k = cv2.morphologyEx(img1, cv2.MORPH_OPEN,ke)
cv2.imshow('img_k', img_k)

# 闭运算  先膨胀-再腐蚀  (扩大毛刺)
img_b = cv2.morphologyEx(img1, cv2.MORPH_CLOSE, ke)
cv2.imshow('img_b', img_b)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 梯度运算  --》  获取边界
# 逻辑：  进行膨胀（图像变大）--减去-- 腐蚀图像(图像变小)
img_yuan = cv2.imread('yuan.png')
img_tidu = cv2.morphologyEx(img_yuan, cv2.MORPH_GRADIENT, ke)
cv2.imshow('img_tidu', img_tidu)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# 礼帽  原图像--减去--开运算 == 得到毛刺  top_hat
img_top = cv2.imread('demo.png')
ke = np.ones((5,5), np.uint8)
img_top = cv2.morphologyEx(img_top, cv2.MORPH_TOPHAT, ke)
cv2.imshow('img_top', img_top)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 黑帽  闭元素 --减去-- 原图像 == 大致的模糊的轮廓 black_hat
img_back = cv2.imread('demo.png')
ke = np.ones((5,5), np.uint8)
img_back = cv2.morphologyEx(img_back, cv2.MORPH_BLACKHAT, ke)
cv2.imshow('img_back', img_back)
cv2.waitKey(0)
cv2.destroyAllWindows()