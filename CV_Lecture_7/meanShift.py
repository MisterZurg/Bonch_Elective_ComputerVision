import cv2
import numpy as np


def onMouse(event, x, y, flags, param):
    # По нажатию ЛКМ
    if event == cv2.EVENT_LBUTTONDOWN:
        global points_count
        global x1, x2, y1, y2
        global frame
        if points_count == 0:
            x1 = x
            y1 = y
            points_count += 1
        else:
            x2 = x
            y2 = y
            frame_rect = frame.copy()
            cv2.rectangle(frame_rect, (x1, y1), (x2, y2), (0, 0, 255), 2)
            cv2.imshow('first', frame_rect)
            points_count = 0


capture = cv2.VideoCapture('resources\\flow.mp4')
ret, frame = capture.read()
cv2.imshow('first', frame)
cv2.setMouseCallback('first', onMouse)
x1, x2, y1, y2, points_count = 0, 0, 0, 0, 0

cv2.waitKey()
cv2.destroyAllWindows()

#
print(x1, y1, x2, y2)
roi = frame[y1:y2, x1:x2]
roi_hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
# Создадим ДИОпазон, для маски
hsv_begin = np.array((0, 60, 32))  # , dtype=np.uint)
hsv_end = np.array((180, 255, 255))  # , dtype=np.uint)

roi_mask = cv2.inRange(roi_hsv, hsv_begin, hsv_end)
cv2.imshow('mask', roi_mask)
cv2.waitKey()
roi_hist = cv2.calcHist([roi_hsv], [0], roi_mask, [180], [0, 180])  # Гистограмма для выделенной области
cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)
# Критерий для мейнШифта
criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)
# Проходимся по кадрам
while True:
    ret, frame = capture.read()
    if not ret:
        break
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Используем ф-ию для создания маски, на основании гистограммы
    dst = cv2.calcBackProject([frame_hsv], [0], roi_hist, [0, 180], 1)
    track_window = (x1, y1, abs(x2 - x1), abs(y2 - y1))
    # То ради чего была проделана работа :3
    ret, track_window = cv2.meanShift(dst, track_window, criteria)
    x, y, w, h = track_window
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
    # camShift
    cv2.CamShift(dst, track_window)
    cv2.imshow('result', frame)
    key = cv2.waitKey(50)
    if key == 27:
        break

cv2.destroyAllWindows()
capture.release()
