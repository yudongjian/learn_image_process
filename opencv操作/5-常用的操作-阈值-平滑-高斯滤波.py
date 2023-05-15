import cv2


# todo 1 阈值处理
# binary 二进制
# thresh 脱粒，翻滚--旧时谷物利用翻滚进行脱粒

'''
THRESH_BINARY         二值化
THRESH_BINARY_INV    反二值化
THRESH_TRUNC        截断阈值化处理
                    图像中大于阈值的像素点的值设定为阈值，小于或等于该阈值的像素点保持不变
THRESH_TOZERO       低阈值处理
                    将小于或等于阈值的像素点的值处理为0，大于阈值的像素点的值保持不变。
THRESH_TOZERO_INV       超阈值处理
                    将图像大于阈值的像素点设置为0，小于或等于该阈值的像素点的值保持不变。       
'''
img_dog = cv2.imread('../234.jpg')
img_dog.copy()
# 返回两个参数， 一个是阈值，一个是图像[[]]
yuzhi, img2 = cv2.threshold(img_dog, 147,255,cv2.THRESH_BINARY)
print(yuzhi)

cv2.imshow('img2', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()



# todo 2 平滑处理   卷积

# 类型1 均值滤波  使得图像更加平滑了
img_zs = cv2.imread('zaosheng.png',1)
img_zs = cv2.blur(img_zs,(3,3))
# cv2.medianBlur(img_zs)
cv2.imshow('img_zs', img_zs)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 类型2 方框滤波
img_zs = cv2.imread('zaosheng.png',1)
# true 此时表现和均值一致， false 则不一样，省去了除以 (3*3)的操作
img_zs = cv2.boxFilter(img_zs,-1,(3,3), normalize=True)
cv2.imshow('img_zs', img_zs)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 高斯函数