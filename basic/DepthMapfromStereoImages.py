import numpy as np
from cv2 import cv2 as cv
from matplotlib import pyplot as plt

imgL = cv.imread('datas/images/tsukuba_L.png',0)
imgR = cv.imread('datas/images/tsukuba_R.png',0)
stereo = cv.StereoBM_create(numDisparities=16, blockSize=15)
disparity = stereo.compute(imgL,imgR)
plt.imshow(disparity,'gray')
plt.show()