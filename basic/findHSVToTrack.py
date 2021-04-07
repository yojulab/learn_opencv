from cv2 import cv2 as cv
import numpy as np

flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
print (flags)

#BGR --> Gray and BGR --> HSV
blue = np.uint8([[[ 255,255,255 ]]])
green = np.uint8([[[ 0,255,0 ]]])
red = np.uint8([[[ 0,0,255 ]]])
hsv_blue = cv.cvtColor(blue,cv.COLOR_BGR2HSV)

print('Convert HSV for blue', hsv_blue)
hsv_green = cv.cvtColor(green,cv.COLOR_BGR2HSV)
print('Convert HSV for green', hsv_green)
hsv_red = cv.cvtColor(red,cv.COLOR_BGR2HSV)
print('Convert HSV for red', hsv_red)
