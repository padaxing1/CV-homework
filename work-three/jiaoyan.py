import cv2
import numpy as np


def salt(img, n):
    for k in range(n):
        i = int(np.random.random() * img.shape[1])
        j = int(np.random.random() * img.shape[0])
        if img.ndim == 2:
            img[j, i] = 255
        elif img.ndim == 3:
            img[j, i, 0] = 255
            img[j, i, 1] = 255
            img[j, i, 2] = 255
    return img


def nosalt(img, n):
    for k in range(n):
        i = int(np.random.random() * img.shape[1])
        j = int(np.random.random() * img.shape[0])
        if img.ndim == 2:
            img[j, i] = 0
        elif img.ndim == 3:
            img[j, i, 0] = 0
            img[j, i, 1] = 0
            img[j, i, 2] = 0
    return img

path = 'C:/Users/86158/Pictures/'
img = cv2.imread(path + "R-C.jfif", 0)
SNR = 0.9
noiseNum = int((1 - SNR) * img.shape[0] * img.shape[1])
saltImg = salt(img, noiseNum)
saltImg = nosalt(saltImg, noiseNum)
cv2.imshow("salt", saltImg)
cv2.imwrite(path + "salt_R-c.jfif.jpg", saltImg)
cv2.waitKey(0)
cv2.destroyAllWindows()




