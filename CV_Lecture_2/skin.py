import numpy as np
import cv2

# define the upper and lower boundaries of the HSV pixel
# intensities to be considered 'skin'
lower = np.array([0, 48, 80], dtype = "uint8")
upper = np.array([20, 255, 255], dtype = "uint8")

skinMask = cv2.inRange(converted, lower, upper)
cv2.imshow('Mask', skinMask);
cv2.waitKey()
skin = cv2.bitwise_and(frame, frame, mask = skinMask)
cv2.imshow('Skin masked', skin);
cv2.waitKey()
cv2.destroyAllWindows()
