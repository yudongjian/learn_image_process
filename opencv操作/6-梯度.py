import cv2

'''
Sobel 算子
    x  右 --减去--左  [-1, 0, 1]
                     [-2, 0, 2]
                     [-1, 0, 1]
    Y  下--减去--上   [-1, -2,  -1]
                     [ 0,  0,  0]
                     [ 1,  2,  1]
    为什么分别计算 乘以 权重，然后求和 效果好于 直接计算：
        个人理解，因为边界是一条 粗线！
        求出的梯度线是一些存在小格子。
        直接相加，导致面积变大，出现重影
        乘以权重，

Scharr算子
    在sobel核的基础上，使得卷积核的数值变大一些，使得效果明显一下,效果是更加敏感
           [-3, 0, 3]
     x     [-9, 0, 9]    y 同理
           [-3, 0, 3]

lapalas  二阶算子  周围的减去中间的
           [0,  1, 0]
     x     [1, -4, 1]    
           [0,  1, 0]
'''
# todo 1 sobel 算子
img1 = cv2.imread('yuan.png')

#  直接计算，不建议  包含重影
img_yuan = cv2.Sobel(img1, cv2.CV_64F, 1, 1, ksize=3)
img_yuan = cv2.convertScaleAbs(img_yuan)
cv2.imshow('img_yuan', img_yuan)

# 建议 分别计算*权重，再相加
img_x = cv2.Sobel(img1, cv2.CV_64F, 1, 0, ksize=3)
img_x = cv2.convertScaleAbs(img_x)

img_y = cv2.Sobel(img1, cv2.CV_64F, 0, 1, ksize=3)
img_y = cv2.convertScaleAbs(img_y)
img_z = cv2.addWeighted(img_x, 0.5, img_y, 0.5, 0)
cv2.imshow('img_z', img_z)

# todo 2 scharr 算子   注意：x,y 不能同时指定为1
img_scharr_x = cv2.Scharr(img1, cv2.CV_64F, 0, 1)
img_scharr_y = cv2.Scharr(img1, cv2.CV_64F, 1, 0)

img_scharr_x = cv2.convertScaleAbs(img_scharr_x)
img_scharr_y = cv2.convertScaleAbs(img_scharr_y)

img_scharr = cv2.addWeighted(img_scharr_x, 0.5, img_scharr_y, 0.5, 0)
cv2.imshow('img_scharr', img_scharr)

# todo 3

img_lapalas = cv2.Laplacian(img1, cv2.CV_64F)
img_lapalas = cv2.convertScaleAbs(img_lapalas)
cv2.imshow('img_lapalas', img_lapalas)

# import numpy as np
# res = np.hstack((img_z, img_scharr, img_lapalas))
# cv2.imshow('res', res)

cv2.waitKey(0)
cv2.destroyAllWindows()