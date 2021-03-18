import cv2
import numpy as np

image = cv2.imread('resources\\hand.png', 0)
image = cv2.resize(image, None, fx=0.2, fy=0.2)
image = cv2.GaussianBlur(image, (9, 9), None)
image_sobel_x = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=7)
image_sobel_y = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=7)

cv2.imshow('Original', image)
cv2.imshow('Sobel X', image_sobel_x)
cv2.imshow('Sobel Y', image_sobel_y)
image_sobel_xy = cv2.bitwise_or(image_sobel_x, image_sobel_y)
cv2.imshow('result', image_sobel_xy)

cv2.waitKey()
cv2.destroyAllWindows()
