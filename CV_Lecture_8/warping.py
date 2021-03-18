import cv2
import numpy as np

pts = []
points_count = 0


def transform(image, pts):
    tl, tr, br, bl = pts
    widthA = np.sqrt((tr[0] - tl[0]) ** 2 + (tr[1] - tl[1]) ** 2)
    widthB = np.sqrt((br[0] - bl[0]) ** 2 + (br[1] - bl[1]) ** 2)
    maxWidth = max(widthA, widthB)
    heightA = np.sqrt((tl[0] - bl[0]) ** 2 + (tl[1] - bl[1]) ** 2)
    heightB = np.sqrt((tr[0] - br[0]) ** 2 + (tr[1] - br[1]) ** 2)
    maxHeight = max(heightA, heightB)

    src = np.array([[tl[0], tl[1]],
                    [tr[0], tr[1]],
                    [br[0], br[1]],
                    [bl[0], bl[1]]], dtype='float32')     # np.float32 подсказка не вываливается

    dst = np.array([[0, 0],
                    [maxWidth - 1, 0],
                    [maxWidth - 1, maxHeight - 1],
                    [0, maxHeight - 1]], dtype='float32')

    M = cv2.getPerspectiveTransform(src, dst)
    wraped = cv2.warpPerspective(image, M, (int(maxWidth), int(maxHeight)))
    cv2.imshow('wraped', wraped)


def onMouse(event, x, y, flags, param):
    global points_count
    global pts
    global image
    if event == cv2.EVENT_LBUTTONDOWN:
        pts.append((x, y))
        points_count += 1
    if points_count == 4:
        transform(image, pts)


image = cv2.imread('resources\\parking.jpg')
cv2.imshow('original', image)
cv2.setMouseCallback('original', onMouse)

cv2.waitKey()
cv2.destroyAllWindows()
