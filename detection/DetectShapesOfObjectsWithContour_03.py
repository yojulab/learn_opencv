from cv2 import cv2 as cv
from skimage.data import horse
import numpy as np

img_raw = horse().astype('uint8')
img_raw = np.ones(img_raw.shape) - img_raw

img = img_raw.copy().astype('uint8')

contours, hierachy = cv.findContours(img, cv.RETR_TREE, cv.CHAIN_APPROX_TC89_KCOS)
image = cv.drawContours(img, contours, 0, 2)

cv.imshow('horse', image)
cv.waitKey(0)

