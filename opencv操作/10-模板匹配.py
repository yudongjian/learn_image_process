'''
模板匹配：
    滑动窗口，一个个的匹配， 类似卷积

    多种匹配模式:  可以参考官网 https://docs.opencv.org/3.4/de/da9/tutorial_template_matching.html
        TM_SQDIFF: 计算平方不同，计算出来的值越小，越相关
        TM_CCORR: 计算相关性，计算出来的值越大，越相关
        TM_CCOEFF: 计算相关系数，计算出来的值越大，越相关

        TM_SQDIFF NORMED: 计算归一化平方不同，计算出来的值越接近0，越相关
        TM_CCORR NORMED: 计算归一化相关性，计算出来的值越接近1，越相关
        TM_CCOEFF_NORMED: 计算归一化相关系数，计算出来的值越接近1，越相关
'''

import cv2
img = cv2.imread('lina.jpg')
img_part = cv2.imread('lina_part.jpg')
h,w = img_part.shape[:2]

# 匹配模式有多种
res = cv2.matchTemplate(img, img_part, cv2.TM_SQDIFF_NORMED)
print(res)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

cv2.rectangle(img, min_loc,(min_loc[0]+w, min_loc[1]+h), (0,0,255),2)

cv2.imshow('img_part', img_part)
cv2.imshow('img', img)


cv2.waitKey(0)
cv2.destroyAllWindows()
