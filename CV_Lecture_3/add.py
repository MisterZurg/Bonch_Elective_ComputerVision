import cv2
import numpy as np

image = cv2.imread('resources\\arsenal.jpg')
#h,w,c = image.shape
fill = np.ones(image.shape,dtype= np.uint8)*100
white = np.ones(image.shape,dtype= np.uint8)*255

#added = image+fill  # 130+126 = 256 uint8 [0..255] 1
#BGR B=B+100 G= G+100 R= R+100
added = cv2.add(image,fill)
subtracted = cv2.subtract(white,image)
cv2.imshow('added', added)
cv2.imshow('subtracted', subtracted)

cv2.waitKey()

