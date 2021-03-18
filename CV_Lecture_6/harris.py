import cv2

image = cv2.imread('resources\\chessb.png')
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
harris = cv2.cornerHarris(image_gray, 5, 3, 0.04)
image[harris > 0.05 * harris.max()] = [0, 0, 255]
cv2.imshow('harris', image)

cv2.waitKey()
cv2.destroyAllWindows()
