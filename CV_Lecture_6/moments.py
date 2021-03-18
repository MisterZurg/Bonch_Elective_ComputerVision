import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('resources\\shapes.png')
image = cv2.resize(image, None, fx=.5, fy=.5)
image_contours = image.copy()
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image_canny = cv2.Canny(image_gray, 20, 80)
cv2.imshow('canny', image_canny)
contours, hierarchy = cv2.findContours(image_canny, cv2.RETR_EXTERNAL,
                                       cv2.CHAIN_APPROX_NONE)
sorted_contours = sorted(contours,key=cv2.contourArea)
for contour in sorted_contours:
    area = cv2.contourArea(contour)
    print(area)
    cv2.drawContours(image_gray, [contour],-1,(255,0,0),2)
    cv2.imshow('areas', image_gray)
    cv2.waitKey()
cv2.destroyAllWindows()

#  Определить форму фигуры и вывести на ней.