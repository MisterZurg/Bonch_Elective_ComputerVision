import cv2
import numpy as np

percent = 0.1  # Коэффициент matches
# img_template = cv2.imread('resources\\gmischenko_valeri.png')
# image = cv2.imread('resources\\family.jpg')

img_template = cv2.imread('resources\\template1.jpg')
video = cv2.VideoCapture('resources\\template_video1.mp4')

img_template_gray = cv2.cvtColor(img_template, cv2.COLOR_BGR2GRAY)
orb = cv2.ORB_create(500)
kp_template, des_template = orb.detectAndCompute(img_template_gray, None)
matcher = cv2.DescriptorMatcher_create(cv2.DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING)

# Цикл считывающий кадры
while True:
    ret, frame = video.read()
    if ret == False:
        break
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    kp_frame, des_frame = orb.detectAndCompute(frame_gray, None)

    matches = matcher.match(des_template, des_frame, None)
    matches.sort(key=lambda x: x.distance, reverse=False)
    good_matches = matches[0:int(len(matches) * percent)]
    # img_matches = cv2.drawMatches(img_template, kp_template, frame, kp_frame, good_matches, None)
    # cv2.imshow('matches',img_matches)

    pts_template = np.zeros((len(matches), 2), dtype=np.float32)  # .reshape(-1, 1, 2)
    pts_frame = np.zeros((len(matches), 2), dtype=np.float32)  # .reshape(-1, 1, 2)

    # Помещаем реальные значения
    for i, match in enumerate(matches):
        pts_template[i, :] = kp_template[match.queryIdx].pt
        pts_frame[i, :] = kp_frame[match.queryIdx].pt
    #
    M, mask = cv2.findHomography(pts_template, pts_frame, cv2.RANSAC)
    # Отрисовка контура
    height, width = frame.shape[:2]

    pst = np.float32([[0, 0],
                      [0, height - 1],
                      [width - 1, height - 1],
                      [width - 1, 0]]).reshape(-1, 1, 2)

    # print(pts)
    dts = cv2.perspectiveTransform(pst, M)

    frame_contour = frame.copy()
    cv2.polylines(frame_contour, [np.int(dts)], True, (0, 0, 255), 2)
    cv2.imshow('contour', frame_contour)

    key = cv2.waitKey(20)
    if key == 29:
        break

cv2.destroyAllWindows()
