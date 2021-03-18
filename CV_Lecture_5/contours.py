import cv2

image = cv2.imread('resources\\shapes.png')
image = cv2.resize(image, None, fx=.5, fy=.5)
image_contours = image.copy()
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image_canny = cv2.Canny(image_gray, 20, 80)
cv2.imshow('canny', image_canny)
contours, hierarchy = cv2.findContours(image_canny, cv2.RETR_EXTERNAL,
                                       cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(image_contours, contours, -1, (255, 0, 0), 3)
print(contours)

cv2.imshow('contours', image_contours)
cv2.waitKey()
cv2.destroyAllWindows()
