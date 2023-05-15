'''

cv2.findContours(img,mode,method)
mode:  轮廓检索模式
RETR_EXTERNAL : 只检索最外面的轮廓。
RETR_LIST: 检索所有的轮廓，并将其保存到一条链表当中。
RETR_CCOMP: 检索所有的轮廓，并将他们组织为两层: 顶层是各部分的外部边界，第二层是空洞的边界。
RETR_TREE: 检索所有的轮廓，并重构嵌套轮廓的整个层次。

method:轮廓逼近方法
    CHAIN_APPROX_NONE: 以Freeman链码的方式输出轮廓，所有其他方法输出多边形(顶点的序列)。
    CHAIN_APPROX_SIMPLE:  压缩水平的、垂直的和斜的部分，也就是，函数只保留他们的终点部分。

'''

import cv2

img1 = cv2.imread('cfx.png')

# step1 将图片进行二值化处理
img2 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
yuzhi, img3 = cv2.threshold(img2,127,255, cv2.THRESH_BINARY)

# step2 找到轮廓 返回1：轮廓特征
contours, hierarchy = cv2.findContours(img3, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# step3 在原始图像上 画出轮廓
cv2.drawContours(img1, contours, -1, (0, 0, 255),2)

cv2.imshow('img1', img1)



'''
轮廓特征
'''
a1 = contours[0]
print(cv2.contourArea(a1))
print(cv2.arcLength(a1, True)) # 周长， True表示闭合的面积

'''
轮廓近似--多边形逼近
    取值越小：近似越精确
    
'''
img1 = cv2.imread('jihe.png')

# 二值处理
gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
yuzhi, img3 = cv2.threshold(gray, 127,255, cv2.THRESH_BINARY)


con, hie = cv2.findContours(img3, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# 近似处理
epsilon = 0.09 * cv2.arcLength(con[0], True)
eps_con = cv2.approxPolyDP(con[0], epsilon, True)

# 画
cv2.drawContours(img1, [eps_con], -1, (255,0,0),2)

cv2.imshow('img_jisi', img1)



'''
外接矩形、外接圆
'''
x, y, w, h = cv2.boundingRect(con[0])
cv2.rectangle(img1,(x, y), (x + w, y + h), (0, 0, 255), 2)

cv2.imshow('img_wjjx', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
