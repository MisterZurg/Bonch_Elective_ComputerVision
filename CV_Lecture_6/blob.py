import cv2
import numpy as np

image = cv2.imread('resources\\sunflower_header.png')
# image = cv2.resize(image, None, fx = 0.3,fy=0.3)
params = cv2.SimpleBlobDetector_Params()
params.maxArea = 10000
params.minArea = 10
params.filterByCircularity = True
params.minCircularity = 0.3
# По оболочке, как мало вогнутустей
params.filterByConvexity = True
params.minConvexity = 0.1

blob_detector = cv2.SimpleBlobDetector_create()
keypoints = blob_detector.detect(image)
image_zero = np.zeros((1, 1))
blobs = cv2.drawKeypoints(image, keypoints, image_zero, (0, 0, 255),
                          cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)  # Флаг делает бррр
cv2.imshow('result', blobs)

cv2.waitKey()
cv2.destroyAllWindows()
