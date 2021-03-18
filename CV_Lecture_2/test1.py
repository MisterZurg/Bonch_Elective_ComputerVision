import numpy as np
import cv2

img = np.ones((600, 800, 3), dtype=np.uint8) * np.random.randint(10, 255)


def randColor():
    c = np.random.uniform(0, 255, 3)
    return (int(c[0]), int(c[1]), int(c[2]))


def randCoord(image):
    h, w = image.shape[:2]
    return (np.random.randint(0, w), np.random.randint(0, h))


def drawLines(image, iterations):
    for i in range(iterations):
        cv2.line(image, randCoord(image), randCoord(image), randColor(),
                 np.random.randint(1, 6))


def drawTriangels(image, iterations):
    vertices = np.zeros((3, 2), np.int)
    for i in range(iterations):
        for j in range(3):
            vertices[j, 0] = randCoord(image)[0]
            vertices[j, 1] = randCoord(image)[1]
        cv2.fillPoly(image, [vertices], randColor())


def drawCicles(image, iterations):
    for i in range(iterations):
        cv2.circle(image, randCoord(image), np.random.randint(20, 170),
                   randColor(), np.random.randint(-10, 15))


drawLines(img, 100)
drawTriangels(img, 100)
drawCicles(img, 105)

cv2.imshow('ellipse', img)
cv2.waitKey()
cv2.destroyAllWindows()
