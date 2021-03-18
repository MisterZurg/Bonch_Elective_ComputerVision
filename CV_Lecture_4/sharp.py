import cv2
import numpy as np

image = cv2.imread('resources/houses.png')

kernel = np.array([[0, 0, 0],
                   [0, 2, 0],
                   [0, 0, 0]])
kernel_sub = np.ones((3, 3), np.float) / 9

#image_sharped = cv2.filter2D(image, cv2.CV_8U, kernel) - \
#                cv2.filter2D(image, None, kernel_sub)
image_sharped = cv2.filter2D(image, None, kernel - kernel_sub)

cv2.imshow('sharped', image_sharped)
cv2.waitKey()
cv2.destroyAllWindows()
