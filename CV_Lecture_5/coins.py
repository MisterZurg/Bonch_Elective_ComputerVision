import cv2

image = cv2.imread('resources\\coins.jpeg')
cv2.imshow('default', image)
image_blur = cv2.GaussianBlur(image, (17, 17), None)  # Размер ядра размытия

image_canny = cv2.Canny(image_blur, 50, 110)
cv2.imshow('canny', image_canny)

contours, hierarchy = cv2.findContours(image_canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
image_result = image.copy()
for contour in contours:
    (x, y), radius = cv2.minEnclosingCircle(contour)
    if (10 < radius < 100):
        cv2.circle(image_result, (int(x), int(y)), int(radius), (255, 255, 0), 3)
cv2.drawContours(image_result, contours, -1, (255, 0, 0), 3)

image_hsv = cv2.cvtColor(image_blur, cv2.COLOR_BGR2BGRA)
# В учебных целях: (для определения пространства внутри монеток) повторим тоже самое
for contour in contours:
    # Получаем координаты монет
    (x, y), radius = cv2.minEnclosingCircle(contour)
    if (10 < radius < 100):
        # Ширина стороны квадрата
        l = int(radius * 2 ** 0, 5)
        # roi (region of interest) - интересующая область
        roi = image_hsv[int(y - l // 2):int(y + l / 2), int(x - l // 2):int(x + l / 2)]
        h, s, v = cv2.mean(roi)
        print(f"h={h} | s = {s}")
        if (s > 70):
            cv2.circle(image_result, (int(x), int(y)), int(radius), (0, 0, 255), 3)

cv2.imshow('countrs', image_result)
# По стандарту
cv2.waitKey()
cv2.destroyAllWindows()
