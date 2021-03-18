import cv2
import numpy as np

template = cv2.imread('resources\\box.png')
image = cv2.imread('resources\\box_in_scene.png')

sift = cv2.SIFT_create()
#
kp_template, des_template = sift.detectAndCompute(template, None)
kp_image, des_image = sift.detectAndCompute(image, None)

# Поиск с помощью аппарата сопостовления
matcher = cv2.BFMatcher()
matches = matcher.knnMatch(des_template, des_image, k=2)  # сопоставление по отдаленности точек
good = []
for m, n in matches:
    if m.distance < 0.5*n.distance:
        good.append([m])
result = cv2.drawMatchesKnn(template, kp_template, image, kp_image, good, None,
                         flags = cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS )

cv2.imshow('matches', result)
cv2.waitKey()
cv2.destroyAllWindows()
