from cv2 import cv2 as cv
import sys
import os
import numpy as np

root_path = os.getcwd()

filename = '/datas/images/namecard_korea.png'

img = cv.imread(root_path+filename)

if img is None: 
    print("Error opening video stream or file")
    sys.exit()

import pytesseract

print(pytesseract.image_to_string(img, lang='Hangul+Hangul_vert+eng+eng_vert'))

cv.imshow('Resource', img)
cv.waitKey(0)

