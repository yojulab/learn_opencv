import cv2 as cv
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
print(img)
img[:] = 255, 0, 0     # Try 0,255,0
print(img.shape)

cv.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)
cv.rectangle(img, (0, 0), (250, 350), (0, 0, 255), 2)
cv.imshow("Image", img)

cv.circle(img, (400, 50), 30, (255, 255, 0), 5)
cv.putText(img, " OPENCV  ", (300, 200),
           cv.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 3)
cv.imshow("Image", img)

x, y, w, h = 310, 320, 150, 160
cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
cv.putText(img, "Bounding Box",
           (x-10, y-10), cv.FONT_HERSHEY_COMPLEX, 0.5,
           (0, 0, 255), 1)
cv.imshow("Image", img)

cv.waitKey(0)
cv.destroyAllWindows()
