import cv2
import numpy as np

img = cv2.imread('images/window_image.jpg')
cv2.imshow('Original Image',img)

res = cv2.resize(img,dsize=None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
cv2.imshow('Scaling Image',res)

rows,cols,tmp = img.shape

M = np.float32([[1,0,100],[0,1,50]])
dst = cv2.warpAffine(img,M,(cols,rows))
cv2.imshow('Shifting Image',dst)

M2 = cv2.getRotationMatrix2D((cols/2,rows/2),90,scale=1)
dst2 = cv2.warpAffine(img,M2,(cols,rows))
cv2.imshow('Rotating Image',dst2)

cv2.waitKey(0)
cv2.destroyAllWindows()