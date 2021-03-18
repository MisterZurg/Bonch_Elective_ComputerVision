import cv2
from matplotlib import pyplot as plt

beach = cv2.imread('resources\\Where_is_Waldo.png', 0)
beach_color = cv2.imread('resources\\Where_is_Waldo.png')
template = cv2.imread('resources\\Waldo.png', 0)

matched = cv2.matchTemplate(beach, template, cv2.TM_CCOEFF)
plt.imshow(matched)
plt.show()

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(matched)
cv2.rectangle(beach_color,
              (max_loc[0] + 20, max_loc[1]),
              (max_loc[0] + 50, max_loc[1] + 60),
              (255, 0, 0), 2)

cv2.imshow("result", beach_color)

cv2.waitKey()
cv2.destroyAllWindows()
