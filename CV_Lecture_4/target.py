import cv2
import numpy as np

img = cv2.imread('resources\\target.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)

img_ranged = cv2.inRange(gray, 60, 140)
cv2.imshow('thrashed', img_ranged)
kernel = np.ones((9, 9), np.uint8)
img_opened = cv2.morphologyEx(img_ranged, cv2.MORPH_OPEN, kernel)
cv2.imshow('open', img_opened)

cv2.waitKey()
cv2.destroyAllWindows()
