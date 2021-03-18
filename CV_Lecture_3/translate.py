import cv2
import numpy as np

image = cv2.imread('resources\\arsenal.jpg')
h, w = image.shape[:2]
tx = 100
ty = 200

M = np.float32([[1, 0, tx], [0, 1, ty]])
M_rotate = cv2.getRotationMatrix2D((w // 2, h // 2), 45, 0.5)

image_translated = cv2.warpAffine(image, M, (w, h))
image_rotated = cv2.warpAffine(image, M_rotate, (w, h))
iamge_transposed = cv2.transpose(image)
image_flipped = cv2.flip(image, 1)  # 1 - vertical, 0 - horizontal
image_resized_koef = cv2.resize(image, None, fx=0.75, fy=0.75)
image_resized_precise = cv2.resize(image, (800, 600), interpolation=cv2.INTER_AREA)
image_smalled = cv2.pyrDown(image)
image_larger = cv2.pyrUp(image_smalled)

cv2.imshow('original', image)
cv2.imshow('after pyrdown', image_larger)
cv2.imshow('translated', image_translated)
cv2.imshow('rotated', image_translated)
cv2.imshow('transposed', iamge_transposed)
cv2.imshow('flipped', image_flipped)
cv2.imshow('resized koef', image_resized_koef)
cv2.imshow('resized precise', image_resized_precise)
cv2.waitKey()
cv2.destroyAllWindows()
