import cv2

'''
step1 读出 0-9的十张图片， 进行0-9的数字映射
'''
def get_nums_map():
    img_nums = cv2.imread('ocr_a_reference.png')
    img_nums_gary = cv2.cvtColor(img_nums,cv2.COLOR_BGR2GRAY)
    yuzhi, img_nums_inv = cv2.threshold(img_nums_gary,127,250, cv2.THRESH_BINARY)


    cnt, hie = cv2.findContours(img_nums_inv,cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    # cv2.drawContours(img_nums, cnt, -1, (0,0,255),2)


    num_map = {}
    num = 9
    for i in cnt:
        x,y,w,h = cv2.boundingRect(i)
        if y == 19:
            # print(x,y,w,h) # 649,19,w=57,h=88

            cv2.rectangle(img_nums, (x,y),(x+w,y+h),(255,0,0),1)
            num_map[x] = num

            num_map[x+1] = num
            num_map[x-1] = num

            num_map[x + 2] = num
            num_map[x - 2] = num
            num_map[x + 3] = num
            num_map[x - 3] = num
            num_map[x + 4] = num
            num_map[x - 4] = num
            num_map[x + 5] = num
            num_map[x - 5] = num

            num -=1
            # cv2.imshow('img_nums_inv1', img_nums)
    print(num_map)
    # cv2.imshow('img_nums_inv1', img_nums)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return num_map



# 轮廓的匹配
def match(img,template,my_dict):
    res = cv2.matchTemplate(img, template, cv2.TM_SQDIFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    try:
        res = my_dict[min_loc[0]]
        return res
    except Exception as e:
        print(e)
        print('not find num')

# 拿到图片 进行匹配
def xx():
    img1 = cv2.imread('images/credit_card_03.png')
    print(img1.shape)
    img1 = cv2.resize(img1,(583, 368))
    # 截取图片，反转,保存
    img_part = img1[190:250,]
    img_gray = cv2.cvtColor(img_part,cv2.COLOR_BGR2GRAY)
    yuzhi, img_gray = cv2.threshold(img_gray,127,255,cv2.THRESH_BINARY_INV)
    cv2.imwrite('img_temp.png', img_gray)

    new_img = cv2.imread('img_temp.png')
    new_img2 = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)
    yuzhi, img_cnt = cv2.threshold(new_img2, 127, 255, cv2.THRESH_BINARY)

    cnt, his = cv2.findContours(img_cnt,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    z_img = cv2.imread('ocr_a_reference.png')
    my_dict = get_nums_map()
    res_str = ''
    for i in cnt:
        x,y,w,h = cv2.boundingRect(i)
        if y == 27:
            print(x, y,w,h)
            cv2.rectangle(new_img,(x,y),(x+w,y+h),(255,0,0),1)
            img_temp = new_img[y:y+h, x:x+w,:]
            img_temp = cv2.resize(img_temp,(57,88))

            a = match(z_img,img_temp, my_dict)
            res_str +=str(a)

    print(res_str[::-1])
    cv2.imshow('new_img', new_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    xx()

    # {(729, 19): 9, (649, 19): 8, (570, 19): 7, (490, 19): 6, (410, 19): 5, (337, 19): 4, (251, 19): 3, (172, 19): 2,
    #  (92, 19): 1, (13, 19): 0}