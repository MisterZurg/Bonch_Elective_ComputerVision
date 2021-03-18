# Must have libs
import numpy as np
import cv2

# Sum of Arrays
a = np.zeros(8, dtype=np.uint8)
b = np.ones(8, dtype=np.uint8)

c = a + b
# print("a + b is:",c)

# For loop

# for i in range(7):
#    print(a[i])

# Our custom img
# Height 4 : Width 3
# img = np.zeros((4,3),dtype='uint8')
img = np.ones((4, 3), dtype='uint8') * 100  # 1 * 100
# print(img)
# cv2.namedWindow('image')
cv2.imshow('First_Facult', img)
cv2.waitKey()  # Delay of clothing picture
img1 = np.ones((300, 400), dtype='uint8')  # 1 * 100
cv2.imshow('First_Facult', img1)
cv2.waitKey()  # Delay of clothing picture
cv2.destroyAllWindows()  # Free memory

# Loading from a file
# Path, Flag
image = cv2.imread('resources\\MZ_Head.jpg', cv2.IMREAD_GRAYSCALE)  # Flag 0 or cv2.IMREAD_GRAYSCALE
cv2.imshow('First but Sec', image)
cv2.waitKey()  # Delay of clothing picture
cv2.destroyAllWindows()  # Free memory
print(image.shape)
height, width = image.shape
for y in range(height):
    for x in range(width):
        image[y, x] += 160
        cv2.imshow('First but Sec', image)
        cv2.waitKey(5)
cv2.destroyAllWindows()  # Free memory