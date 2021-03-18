import cv2
import numpy as np


# Произойдет центроид

# Посчитаем координаты по ОХ
# Вернет все моменты до II-го порядка
def x_coord(contours):
    moment = cv2.moments(contours)
    return int(moment['m10'] / moment['m00']), int(moment['m01'] / moment['m10'])


image = cv2.imread('resources\\shapes.png')
# image = cv2.resize(image, None, fx=0.5, fy=0.5,interpolation=cv2.INTER_CUBIC) # Интерполяция средней тяжести
image = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LANCZOS4)  # Интерполяция тяжелая, но точная
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

image_canny = cv2.Canny(image_gray, 70, 150)
contours, h = cv2.findContours(image_canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
for contour in contours:
    x, y = x_coord(contour)
    poly = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
    print(x, y)
    cv2.circle(image, (x, y), 2, (255, 0, 0), 2)
    cv2.imshow('result', image)
    cv2.waitKey()
    
cv2.destroyAllWindows()
