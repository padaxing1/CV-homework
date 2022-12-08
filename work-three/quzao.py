import cv2
import numpy as np

a = cv2.imread('C:\\Users\\86158\\Pictures\\gaosi_R-c.jfif.jpg',cv2.IMREAD_UNCHANGED)
b = cv2.GaussianBlur(a, (5,5), 0 )
c = cv2.imread('c:\\Users\\86158\\Pictures\\salt_R-c.jfif.jpg',cv2.IMREAD_UNCHANGED)
d = cv2.medianBlur(c,5)
cv2.namedWindow('a',cv2.WINDOW_GUI_NORMAL)
cv2.namedWindow('b',cv2.WINDOW_GUI_NORMAL)
cv2.namedWindow('c',cv2.WINDOW_GUI_NORMAL)
cv2.namedWindow('d',cv2.WINDOW_GUI_NORMAL)
cv2.imshow('a',a)
cv2.imshow('b',b)
cv2.imshow('c',c)
cv2.imshow('d',d)
cv2.imwrite('C:\\Users\\86158\\Pictures\\gaosi_finished_R-C.jfif.jpg',b)
cv2.imwrite('C:\\Users\\86158\\Pictures\\jiaoyan_finished_R-C.jfif.jpg',d)
cv2.waitKey(0)
cv2.destroyAllWindows()