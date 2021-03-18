import cv2
import numpy as np

image = cv2.imread('resources\\arsenal.jpg')
h, w = image.shape[:2]

start_row, start_col = h // 4, w // 4
end_row, end_col = int(h * 0.75), int(w * .75)

image_cropped = image[start_row:end_row, start_col:end_col]
image_cropped = image[h // 2:h, 0:w]

cv2.imshow('cropped', image_cropped)
cv2.waitKey()
cv2.destroyAllWindows()
