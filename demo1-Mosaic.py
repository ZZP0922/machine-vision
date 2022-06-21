import cv2
import numpy as np

if __name__ == '__main__':
    img = cv2.imread("I:/tmp/cat0005.jpg")
    print(img.shape)
    cv2.imshow("cat_src",img)
    # Mosaic方式1
    # img2 = cv2.resize(img,(60,43))
    # img3 = cv2.resize(img2,(600,437))

    # Mosaic方式2
    # img2 = cv2.resize(img,(60,43))
    # img3 = np.repeat(img2,10,axis=0)
    # img4 = np.repeat(img3,10,axis=1)

    # Mosaic方式3
    img2 = img[::10,::10] # 每10个中取出一个像素
    cv2.namedWindow("cat",cv2.WINDOW_NORMAL)
    cv2.resizeWindow("cat",600,437)

    cv2.imshow("cat",img2)
    cv2.waitKey(0)
    cv2.destroyWindow()