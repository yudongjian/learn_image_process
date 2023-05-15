import cv2

# 相加操作
# cv2.add  超过255 显示为255

img1 = cv2.imread('../123.png',1)
# 设置w h
img2 = cv2.resize(img1, (500,500))
cv2.imshow('img2', img2)

# 放缩
img3 = cv2.resize(img1, (0,0), fx=3, fy=3)
cv2.imshow('img3', img3)

# 直接融合
img4 = cv2.resize(img1,(500,500))
img5 = cv2.add(img2,img4)
cv2.imshow('img5', img5)

# 先放缩一致  然后加权融合，可以添加偏置
img_dog = cv2.imread('../4.jpg')
img_cat = cv2.imread('../2.jpg')
print(img_dog)
w,h,c= img_dog.shape
print(h)
print(w)
print(c)

img_cat = cv2.resize(img_cat, (w,h))
img_add = cv2.addWeighted(img_cat,0.6, img_dog,0.4,-20)
cv2.imshow('img_add', img_add)



cv2.waitKey(0)
cv2.destroyAllWindows()