import cv2

image = cv2.imread('resources\\building.jpg')
image_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

sift = cv2.SIFT_create()
keypoints = sift.detect(image_grey, None)

cv2.drawKeypoints(image, keypoints, image_grey)
cv2.imshow('result', image_grey)
cv2.waitKey()
cv2.destroyAllWindows()
