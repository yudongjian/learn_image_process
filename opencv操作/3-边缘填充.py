import cv2

# borderType：边界的类型
# BORDER_REPLICATE：复制法，即复制最边缘的像素。例如：aaaa|abcdefg|ggggg
# BORDER_REFLECT：反射法,即以最边缘的像素为对称轴。例如：fedcba|abcdefg|gfedec
# BORDER_REFLECT_101：反射法,也是最边缘的像素为对称轴，但与BORDER_REFLECT有区别。例如：fedcb|abcdefg|fedec
# BORDER_WRAP：外包装法，即以图像的左边界与右边界相连，上下边界相连。例如：cdefgh|abcdefgh|abcdefg
# BORDER_CONSTANT：常量法。

# 复制法
# 反射法 （以边缘外的空白为轴对称）
# 反射法 （以边缘线为轴对称）
# 常量法
# 外包装法

img = cv2.imread('./../123.png')
top, bottom, left, right = (50,50,50,50)
wrap = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_WRAP)
wrap = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_CONSTANT, value=0)

cv2.imshow('123',wrap)
cv2.waitKey(0)
cv2.destroyAllWindows()