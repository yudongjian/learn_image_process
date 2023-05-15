import cv2

# Region of interest
img1 = cv2.imread('../123.png', 1)

# 切片操作
img_part = img1[0:400,0:400]

cv2.imshow('img_part', img_part)
cv2.waitKey(0)
cv2.destroyAllWindows()

b,g,r = cv2.split(img1)  # 颜色通道提取
img3 = cv2.merge((b,g,r))

# 只保留特定 颜色通道
# 1 只保留 b通道颜色  （实现逻辑：将不需要保留的 颜色通道设置为 0 即可）
img3[:,:,1] = 0
img3[:,:,2] = 0

cv2.imshow('img3', img3)
cv2.waitKey(0)
cv2.destroyAllWindows()