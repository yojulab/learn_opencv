from cv2 import cv2 as cv
import sys
import os
import numpy as np

root_path = os.getcwd()

# filename = '/datas/images/cashreceipt.png'
filename = '/datas/images/cashreceipt_kor.jpg'

img = cv.imread(root_path+filename)

if img is None: 
    print("Error opening video stream or file")
    sys.exit()

img_thresholding = img.copy()
import pytesseract
from pytesseract import Output

# custom_config = r'--oem 3 --psm 6'
custom_config = r'--oem 3 --psm 6 -l kor+kor_vert+eng'      # korean + english

words_string = pytesseract.image_to_string(img)
words = pytesseract.image_to_data(img, config=custom_config, output_type=Output.DICT)
print(words.keys())
n_boxes = len(words['text'])
for i in range(n_boxes):
    if int(words['conf'][i]) > 60:
        (x, y, w, h) = (words['left'][i], words['top'][i], words['width'][i], words['height'][i])
        img = cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv.imshow('Resource', img)

#thresholding
def thresholding(image):
    return cv.threshold(image, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)[1]

img_gray = cv.cvtColor(img_thresholding, cv.COLOR_BGR2GRAY)
img_thresh = thresholding(img_gray)
cv.imshow('threshold', img_thresh)

words_string = pytesseract.image_to_string(img_thresh)
words = pytesseract.image_to_data(img_thresh, config=custom_config, output_type=Output.DICT)
print(words.keys())
n_boxes = len(words['text'])
for i in range(n_boxes):
    if int(words['conf'][i]) > 60:
        (x, y, w, h) = (words['left'][i], words['top'][i], words['width'][i], words['height'][i])
        img_thresh = cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv.imshow('Resource with threshold', img_thresh)

cv.waitKey(0)

