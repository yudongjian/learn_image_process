import cv2


# todo 1 读取图片
# t1 = cv2.imread('123.png',1)
# cv2.imshow('image',t1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# todo 2 保存图片
# img = cv2.imread('123.png',0)
# cv2.imshow('img',img)
# cv2.waitKey(5*1000)
# cv2.destroyWindow('img')
# cv2.imwrite('234.jpg', img)


# todo 3 读取图片后 一些简单的属性
img1 = cv2.imread('../123.png', 0)
img2 = cv2.imread('../123.png', 1)
print(img1)
print(img2)
print(type(img1))
v,w = img1.shape
print(v)
print(img1.shape)  # 形状 h w c
print(img2.shape)

print(img1.size)   # 像素点格式 ： h * w
print(img2.size)

print(img1.dtype)  # 数据类型



# todo 4 读取视频
video = cv2.VideoCapture('123.mp4')
if video.isOpened():
    res, frame = video.read()
else:
    res = False

while res:
    res, frame = video.read()
    if frame is None:
        break
    if res == True:
        img = cv2.cvtColor(frame,1)
        cv2.imshow('视频', img)
        if cv2.waitKey(10) & 0xFF==27:
            break

video.release()
cv2.destroyAllWindows()


