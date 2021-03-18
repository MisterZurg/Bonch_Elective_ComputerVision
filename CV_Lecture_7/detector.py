import cv2
import numpy as np

image_template = cv2.imread('resources\\template1.jpg')
capture = cv2.VideoCapture('resources\\template_video1.mp4')

image_template_gray = cv2.cvtColor(image_template, cv2.COLOR_BGR2GRAY)
orb = cv2.ORB_create()
kp_template = orb.detect(image_template_gray, None)
kp_template, des_template = orb.compute(image_template_gray, kp_template)
bf_matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)  # Произошел Шумаков

while (True):
    ret, frame = capture.read()
    if ret == False:
        break
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    kp_frame = orb.detect(frame_gray, None)
    kp_frame, des_frame = orb.compute(frame_gray, kp_frame)
    matches = bf_matcher.match(des_frame, des_template)
    goods = []
    for m in matches:
        # if m.distance < 0:
        goods.append(m)
    print(len(goods))
    # image_result = cv2.drawMatches(image_template, kp_template, frame, kp_frame,
    #                               goods, None, flags= 2)
    image_result = np.zeros((frame.shape[0], frame.shape[1] + image_template.shape[1], 3),
                            dtype=np.uint8)

    # Поместим на изображение образца
    image_result[0:image_template.shape[0], 0:image_template.shape[1]] = image_template
    image_result[:, image_template.shape[1]:] = frame
    for i in range(len(goods)):
        pt_a = (int(kp_template[matches[i].trainIdx].pt[0]),
                int(kp_template[matches[i].trainIdx].pt[1]))
        pt_b = (int(kp_frame[matches[i].trainIdx].pt[0] + image_template.shape[1]),
                int(kp_frame[matches[i].trainIdx].pt[1]))
        cv2.line(image_result, pt_a, pt_b, (0, 255, 0), 1)
    cv2.imshow('result', image_result)
    key = cv2.waitKey(50)
    if key == 27:
        break

cv2.destroyAllWindows()
capture.release()
