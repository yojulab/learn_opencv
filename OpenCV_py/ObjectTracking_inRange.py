from cv2 import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while(True):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    lower_red = np.array([-10,100,100])
    upper_red = np.array([10,255,255])

    # Threshold the HSV image to get only blue colors
    mask_blue = cv.inRange(hsv, lower_blue, upper_blue)
    mask_red = cv.inRange(hsv, lower_red, upper_red)

    # Bitwise-AND mask and original image
#     result = cv.bitwise_and(frame,frame, mask= mask_blue)
    result = cv.bitwise_and(frame,frame, mask= mask_red)

    cv.imshow('frame',frame)
    cv.imshow('mask',mask_red)
    cv.imshow('result',result)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break

cv.destroyAllWindows()