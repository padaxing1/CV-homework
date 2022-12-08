import cv2 as cv
import matplotlib.pyplot as plt


img = cv.imread("C:\\Users\\86158\\Pictures\\R-C.jfif", 0)

#sobel算子边缘提取
x = cv.Sobel(img, cv.CV_64F, 1, 0)
y = cv.Sobel(img, cv.CV_64F, 0, 1)

Scale_absX = cv.convertScaleAbs(x)  # 格式转换函数
Scale_absY = cv.convertScaleAbs(y)
Sobel = cv.addWeighted(Scale_absX, 0.5, Scale_absY, 0.5, 0)

cv.imshow('origion',img)
cv.imshow('Sobel',Sobel)

#拉普拉斯边缘提取
dst = cv.Laplacian(img,cv.CV_16S,ksize=3)
dst = cv.convertScaleAbs(dst)
cv.imshow("res",dst)
cv.waitKey(0)

#canny边缘提取
Canny = cv.Canny(img,100,200,apertureSize=3)
cv.imshow('img_Canny',Canny)
cv.waitKey()

#热力图
mag, ang = cv.cartToPolar(x, y)
plt.figure()

plt.subplot(2,2,1)
plt.imshow(Scale_absX,cmap=plt.cm.hot)
plt.title("X")

plt.subplot(2,2,2)
plt.imshow(Scale_absY,cmap=plt.cm.hot)
plt.title("Y")

plt.subplot(2,2,3)
plt.imshow(mag,cmap=plt.cm.hot)
plt.title("幅度")

plt.subplot(2,2,4)
plt.imshow(ang,cmap=plt.cm.hot)
plt.title("角度")

plt.show()

#合并
merge = cv.addWeighted(img, 0.5, dst, 0.5, 0)
cv.imshow('origion',img)
cv.imshow('merge',merge)
cv.waitKey()

