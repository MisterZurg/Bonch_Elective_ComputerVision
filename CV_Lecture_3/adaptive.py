import cv2
import numpy as np

image_paper = cv2.imread('resources\\contrast.png', 0)
ret, bin_thresh = cv2.threshold(image_paper, 77, 255, cv2.THRESH_BINARY)

adap_thresh = cv2.adaptiveThreshold(image_paper, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                    cv2.THRESH_BINARY, 71, 5)

cv2.imshow('adaptive', adap_thresh)
cv2.imshow('binery', bin_thresh)
cv2.waitKey()
cv2.destroyAllWindows()
