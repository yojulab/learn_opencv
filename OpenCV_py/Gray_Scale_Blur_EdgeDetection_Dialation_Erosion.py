import cv2

img = cv2.imread("datas/images/lena.png")

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image",imgGray)

imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
cv2.imshow("Blur Image",imgBlur)

imgCanny = cv2.Canny(img,150,200)
cv2.imshow("Canny Image",imgCanny)

import numpy as np
kernel = np.ones((5,5),np.uint8)

imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
cv2.imshow("Dialation Image",imgDialation)

imgEroded = cv2.erode(imgDialation,kernel,iterations=1)
cv2.imshow("Eroded Image",imgEroded)

cv2.waitKey(0)
cv2.destroyAllWindows()