import cv2
import numpy as np

# Готовый классификатор из OpenCV
# Обученный как на лицах и глазах, так и не только :3
face_classifier = cv2.CascadeClassifier('resources\\haarcascade_frontalface_default.xml')
eye_classifier = cv2.CascadeClassifier('resources\\haarcascade_eye.xml')

img = cv2.imread('resources\\family.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_classifier.detectMultiScale(img_gray, 1.2, 5)
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    eyes = eye_classifier.detectMultiScale(img_gray[y:y + h, x:x + w])
    for e_x, e_y, e_h, e_w in eyes:
        cv2.rectangle(img, (x + e_x, y + e_y), (x + w + e_x + e_w))

# Поиск людей можно реализовывать с помощью
# Гистограммы направленных градиентов, ну тупа HOG 's
# Метод устойчив к изменению яркости
