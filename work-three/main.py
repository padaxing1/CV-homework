# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
import cv2
import matplotlib.pyplot as plt
def gaussian(original_image,down_times=5):
    temp = original_image.copy()
    gaussian_pyramid = [temp]
    for i in range(down_times):
        temp = cv2.pyrDown(temp)
        gaussian_pyramid.append(temp)
    return gaussian_pyramid


img = cv2.imread("C:\\Users\\86158\\Pictures\\R-C.jfif", -1)
gaussian_pyramid = gaussian(img, down_times=5)
plt.subplot(2, 3, 1), plt.imshow(img, cmap='gray')
plt.subplot(2, 3, 2), plt.imshow(gaussian_pyramid[1], cmap='gray')
plt.subplot(2, 3, 3), plt.imshow(gaussian_pyramid[2], cmap='gray')
plt.subplot(2, 3, 4), plt.imshow(gaussian_pyramid[3], cmap='gray')
plt.subplot(2, 3, 5), plt.imshow(gaussian_pyramid[4], cmap='gray')
plt.subplot(2, 3, 6), plt.imshow(gaussian_pyramid[5], cmap='gray')
plt.show()
print(gaussian_pyramid[0].shape, gaussian_pyramid[1].shape, gaussian_pyramid[2].shape,
      gaussian_pyramid[3].shape,
      gaussian_pyramid[4].shape,gaussian_pyramid[5].shape)

