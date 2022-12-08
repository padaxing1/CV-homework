import cv2
import numpy as np


def RMSE(img1,img2):
    m = np.sqrt(np.mean((img1-img2)**2))
    return m

img = cv2.imread("C:\\Users\\86158\\Pictures\\R-C.jfif")
gaisi_img = cv2.imread("C:\\Users\\86158\\Pictures\\gaosi_R-C.jfif.jpg")
jiaoyan_img = cv2.imread("C:\\Users\\86158\\Pictures\\salt_R-C.jfif.jpg")
finished_gaosi_img = cv2.imread("C:\\Users\\86158\\Pictures\\gaosi_finished_R-C.jfif.jpg")
finished_jiaoyan_img = cv2.imread("C:\\Users\\86158\\Pictures\\jiaoyan_finished_R-C.jfif.jpg")
m1 = RMSE(jiaoyan_img,img)
m2 = RMSE(gaisi_img,img)
m3 = RMSE(finished_gaosi_img,img)
m4 = RMSE(finished_jiaoyan_img,img)
print("1.经过添加椒盐噪声的图片与原来图像之间的RMSE为：")
print(m1)
print("2.经过添加高斯噪声的图片与原来图像之间的RMSE为：")
print(m2)
print("3.添加高斯噪声后经过高斯平滑处理的图片与原图片之间的RMSE为：")
print(m3)
print("4.添加椒盐噪声后经过中值滤波处理的图片与原图片之间的RMSE为：")
print(m4)






