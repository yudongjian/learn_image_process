import cv2
import numpy as np


# 多张尺度不同个图片显示在一起
def show_images(image_name, *key):
    max_w = 0
    max_h = 0
    # 得到最大的宽，高
    for img in key:
        if img.shape[0] > max_w:
            max_w = img.shape[0]

        if img.shape[1] > max_h:
            max_h = img.shape[1]

    # 统一宽高
    image_list = []
    for img in key:
        temp_w, temp_h, c = img.shape
        top = (max_w - temp_w)//2
        bottom = top
        left = (max_h - temp_h)//2
        right = left
        temp_image = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_CONSTANT, value=0)
        image_list.append(temp_image)


    # 最后统一输出: 500 * 800 即可
    print(image_list)
    res = np.hstack(tuple(image_list))
    cv2.namedWindow(image_name, 0)
    cv2.resizeWindow(image_name, 1000,500)
    cv2.imshow(image_name, res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    img1 = cv2.imread('dj.png')
    img2 = cv2.imread('demo.png')
    show_images('123',img1, img2)

