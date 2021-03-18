import cv2

capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()
    frame_grey = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
    frame_grey_blur = cv2.GaussianBlur(frame_grey, (7, 7), None)
    frame_canny = cv2.Canny(frame_grey_blur, 10, 100)
    ret, frame_trashed = cv2.threshold(frame_canny, 127, 255, cv2.THRESH_BINARY_INV)

    cv2.imshow('result', frame_trashed)
    k = cv2.waitKey(1) # В цикле и не пустой, для того чтобы программа не ушла в себя, и хоть что-то показала
    if k == ord('q'): # Выходим из цикла при нажатии
        break

cv2.destroyAllWindows()