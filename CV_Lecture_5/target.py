import cv2
import numpy as np

img = cv2.imread('resources\\target.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)

img_ranged = cv2.inRange(gray, 60, 140)
cv2.imshow('thrashed', img_ranged)
kernel = np.ones((9,9),np.uint8)
img_opened = cv2.morphologyEx(img_ranged, cv2.MORPH_OPEN, kernel)
cv2.imshow('open', img_opened)

contours, hierarchy = cv2.findContours(img_opened, cv2.RETR_EXTERNAL, 
                cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours,-1, (0,255,0), 3)

for contour in contours:
    (x,y),radius = cv2.minEnclosingCircle(contour)
    cv2.circle(img,(int(x),int(y)),int(radius), (0,0,255),3)
    position = (int(x)-20,int(y)-20)
    cv2.putText(img, str(100), position, cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)
cv2.imshow('contours', img)
cv2.waitKey()
cv2.destroyAllWindows()