import cv2
import numpy as np

square = np.zeros((300, 300), dtype=np.uint8)
cv2.rectangle(square, (50, 50), (250, 250), 255, -1)
ellipse = np.zeros((300, 300), dtype=np.uint8)
cv2.ellipse(ellipse, (150, 150), (150, 150), 30, 0, 180, 255, -1)

image_and = cv2.bitwise_and(square, ellipse)
image_or = cv2.bitwise_or(square, ellipse)
image_xor = cv2.bitwise_xor(square, ellipse)
image_not = cv2.bitwise_not(ellipse)

cv2.imshow('not', image_not)
cv2.imshow('xor', image_xor)
cv2.imshow('or', image_or)
cv2.imshow('and', image_and)
cv2.imshow('square', square)
cv2.imshow('ellipse', ellipse)

cv2.waitKey()
cv2.destroyAllWindows()
