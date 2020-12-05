from cv2 import cv2 as cv
import numpy as np

img = cv.imread('datas/images/window_image.jpg')
cv.imshow('Original Image',img)

res = cv.resize(img,dsize=None,fx=2, fy=2, interpolation = cv.INTER_CUBIC)
cv.imshow('Scaling Image',res)

rows,cols,tmp = img.shape

M = np.float32([[1,0,100],[0,1,50]])
dst = cv.warpAffine(img,M,(cols,rows))
cv.imshow('Shifting Image',dst)

M2 = cv.getRotationMatrix2D((cols/2,rows/2),90,scale=1)
dst2 = cv.warpAffine(img,M2,(cols,rows))
cv.imshow('Rotating Image',dst2)

cv.waitKey(0)
cv.destroyAllWindows()