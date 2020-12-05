from cv2 import cv2 as cv
import os

directoryname = os.getcwd() + '/datas/image/imagesframes'

from cv2 import cv2 as cv
img = cv.imread("datas/imageslena.png")
# DISPLAY
cv.imshow("Lena Soderberg",img)
cv.waitKey(0)

