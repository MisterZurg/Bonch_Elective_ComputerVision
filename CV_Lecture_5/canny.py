import cv2

image = cv2.imread('resources\\GladValakas.jpg', 0)
image_canny = cv2.Canny(image,100, 200)

cv2.imshow('canny_result', image_canny)

cv2.waitKey()
cv2.destroyAllWindows()