# -*- coding: utf-8 -*-

from PIL import Image
from pylab import *
from numpy import *
import random
import  cv2

path = 'C:/Users/86158/Pictures/'
im = array(Image.open(path + 'R-C.jfif'))
means = 10
sigma = 40


def normal(pixel):
    if pixel > 255:
        pixel = 255
    elif pixel < 0:
        pixel = 0
    return pixel


# r通道
r = im[:, :, 0].flatten()
# g通道
g = im[:, :, 1].flatten()
# b通道
b = im[:, :, 2].flatten()
for i in range(im.shape[0] * im.shape[1]):
    pr = normal(int(r[i]) + random.gauss(0, sigma))
    pg = normal(int(g[i]) + random.gauss(0, sigma))
    pb = normal(int(b[i]) + random.gauss(0, sigma))
    r[i] = pr
    g[i] = pg
    b[i] = pb
im[:, :, 0] = r.reshape([im.shape[0], im.shape[1]])
im[:, :, 1] = g.reshape([im.shape[0], im.shape[1]])
im[:, :, 2] = b.reshape([im.shape[0], im.shape[1]])

# 显示图像
imshow(im)
cv2.imwrite(path + "gaosi_R-c.jfif.jpg", im)
show()