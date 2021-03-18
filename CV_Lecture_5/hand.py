import cv2
import numpy as np
import math

image = cv2.imread('resources\\hand.png', 0)
image = cv2.resize(image, None, fx=.75, fy=.75)
# Мылим руку XD
image_blur = cv2.GaussianBlur(image, (15, 15), None)
h, w = image.shape
image_color = np.zeros((h, w, 3), dtype=np.uint8)

_, image_tresh = cv2.threshold(image, 100, 255, cv2.THRESH_BINARY)
cv2.imshow('thresh hold', image_tresh)

contours, hierarchy = cv2.findContours(image_tresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
cnt = max(contours, key=cv2.contourArea)
cv2.drawContours(image_color, contours, 0, (0, 0, 255), 3)
hull = cv2.convexHull(cnt)
cv2.drawContours(image_color, [hull], 0, (255, 0, 0), 3)
hull = cv2.convexHull(cnt, returnPoints=False)
defects = cv2.convexityDefects(contours[0], hull)

count = 0
for i in range(len(defects)):
    s, e, f, d = defects[i, 0]
    start = tuple(cnt[s][0])
    end = tuple(cnt[e][0])
    far = tuple(cnt[f][0])
    a = math.sqrt(
        (end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2
    )
    b = math.sqrt(
        (far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2
    )
    c = math.sqrt(
        (end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2
    )
    angle = math.acos(
        (b ** 2 + c ** 2 - a ** 2) / (2 * b * c)
    ) * 57
    if angle <= 90:
        count += 1
        cv2.line(image_color, start, end, (255, 255, 0), 2)

# Дз сделать все тоже самое с фильтром кожи
print(f"We've detected, {count + 1} fingers")
cv2.imshow('contours', image_color)
cv2.waitKey()
cv2.destroyAllWindows()
