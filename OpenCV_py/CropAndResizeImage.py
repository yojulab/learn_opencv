from cv2 import cv2 as cv
import numpy as np

# img = cv.imread("datas/images/shapes.png")
img = cv.imread("datas/images/lambo.png")
print(img.shape)
# (462, 623, 3)

imgResize = cv.resize(img,(1000,500))
print(imgResize.shape)
# (500, 1000, 3)
cv.imshow("Image Resize",imgResize)

imgCropped = img[46:219,152:495] # image numpy matrix

cv.imshow("Image",img)
cv.imshow("Image Cropped",imgCropped)

cv.waitKey(0)
cv.destroyAllWindows()