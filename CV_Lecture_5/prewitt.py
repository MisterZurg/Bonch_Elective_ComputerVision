import cv2
import numpy as np

kernel_x = np.array([[-1, -1, -1],
                     [0, 0, 0],
                     [1, 1, 1]])
kernel_y = np.array(
    [
        [1, 0, -1],
        [1, 0, -1],
        [1, 0, -1]
    ]
)

image = cv2.imread('resources\\GladValakas.jpg', 0)
image_prewitt_x = cv2.filter2D(image, -1, kernel_x)
image_prewitt_y = cv2.filter2D(image, -1, kernel_y)

cv2.imshow('default', image)
cv2.imshow('prewitt x', image_prewitt_x)
cv2.imshow('prewitt y', image_prewitt_y)
cv2.imshow('prewitt', cv2.bitwise_or(image_prewitt_x, image_prewitt_y))

# Цитата преподавателя, вот у Дениса хорошо получилось
cv2.waitKey()
cv2.destroyAllWindows()
