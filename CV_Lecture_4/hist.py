import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread('resources\\high_contrast.png',0)

#hist = cv2.calcHist([img],None,None,[256],[0,256])
img_ravel = img.ravel()
print(img_ravel)
plt.hist(img_ravel,256,[0,256])
#plt.plot(hist)
plt.show()
img_eq = cv2.equalizeHist(img)
cv2.imshow('equalized', img_eq)
cv2.waitKey()
cv2.destroyAllWindows()

