import cv2
import numpy as np

spoons_noise = cv2.imread('resources\\spoons_2.png', 0) # spoons_noise
spoons_gaps = cv2.imread('resources\\spoons_1.png', 0) # spoons_gaps

kernel = np.ones((5, 5), np.uint8)
dilation = cv2.dilate(spoons_gaps, kernel, iterations=2)
erode = cv2.erode(spoons_noise, kernel, iterations=2)
open = cv2.morphologyEx(spoons_noise, cv2.MORPH_OPEN, kernel, iterations=2)
close = cv2.morphologyEx(spoons_gaps, cv2.MORPH_CLOSE, kernel, iterations=2)
cv2.imshow('open', open)
cv2.imshow('close', close)
cv2.imshow('gaps', spoons_gaps)
cv2.imshow('noise', spoons_noise)
cv2.imshow('dilation', dilation)
cv2.imshow('erose', erode)
cv2.waitKey()
cv2.destroyAllWindows()
