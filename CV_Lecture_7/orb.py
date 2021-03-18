import cv2

image =cv2.imread('resources\\morshu_good.png')

orb = cv2.ORB_create()
keypoints = orb.detect(image, None)
keypoints, des = orb.compute(image, keypoints)

image_kp = cv2.drawKeypoints(image, keypoints, None, (0,0,255), flags = 0)
cv2.imshow('original', image)
cv2.imshow('result', image_kp)
cv2.waitKey()
cv2.destroyAllWindows()