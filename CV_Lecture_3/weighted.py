import cv2
import numpy as np

image_sand = cv2.imread('resources\\road_add.jpg')
image_car = cv2.imread('resources\\car_add.jpg')

image_weighted = cv2.addWeighted(image_sand, 0.5, image_car, 0.7, 0)
cv2.imshow('weighted', image_weighted)

cv2.waitKey()