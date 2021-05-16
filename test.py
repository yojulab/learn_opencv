
import numpy as np
import cv2

image = cv2.imread("datas/images/bright.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일 읽기 오류 발생")

image4 = cv2.subtract(255, image)

cv2.imshow('test01', image)

cv2.imshow('test', image4)
cv2.waitKey(0)