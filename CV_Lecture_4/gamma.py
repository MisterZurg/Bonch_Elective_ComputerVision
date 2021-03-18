import cv2
import numpy as np


def gamma_correction(image, gamma=1.0):
    table = np.zeros((256), dtype=np.uint8)
    for i in range(256):
        table[i] = int(((i / 255.0) ** gamma) * 255)
    image_corrected = cv2.LUT(image, table)
    return image_corrected


img = cv2.imread('resources\\contrast.png', 0)
img_corrected = gamma_correction(img, 0.7)
cv2.imshow('orig', img)
cv2.imshow('gamma', img_corrected)
cv2.waitKey()
cv2.destroyAllWindows()
