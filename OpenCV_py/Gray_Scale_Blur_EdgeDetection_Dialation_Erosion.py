from cv2 import cv2 as cv

img = cv.imread("datas/images/lena.png")

imgGray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray Image",imgGray)

imgBlur = cv.GaussianBlur(imgGray,(7,7),0)
cv.imshow("Blur Image",imgBlur)

imgCanny = cv.Canny(img,150,200)
cv.imshow("Canny Image",imgCanny)

import numpy as np
kernel = np.ones((5,5),np.uint8)

imgDialation = cv.dilate(imgCanny,kernel,iterations=1)
cv.imshow("Dialation Image",imgDialation)

imgEroded = cv.erode(imgDialation,kernel,iterations=1)
cv.imshow("Eroded Image",imgEroded)

cv.waitKey(0)
cv.destroyAllWindows()