import cv2
import numpy as np

image_houses = cv2.imread('resources\\houses.png')
image = cv2.imread('resources\\lena_noise.png')
image_salt = cv2.imread('resources\\salt-n-pepper.png')
kernel = np.ones((7, 7), np.float32) / 49
# image_blurred = cv2.filter2D(image,None, kernel)
image_blurred = cv2.blur(image, (7, 7))
image_gauss = cv2.GaussianBlur(image, (13, 13), 0)
image_median = cv2.medianBlur(image_salt, 5)
image_houses_median = cv2.medianBlur(image_houses, 11)
image_cont = np.concatenate((image_salt, image_median), 1)
cv2.imshow('original', image)
cv2.imshow('blurred', image_blurred)
cv2.imshow('gauss', image_gauss)
cv2.imshow('median_houses', image_houses_median)

cv2.imshow('median ', image_cont)
cv2.waitKey()
cv2.destroyAllWindows()
