from cv2 import cv2 as cv
import numpy as np

frameWidth = 640
frameHeight = 480
cap = cv.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)

def empty(a):
    pass

title = "HSV"
cv.namedWindow(title)
cv.resizeWindow(title,640,240)
cv.createTrackbar("HUE Min",title,0,179,empty)
cv.createTrackbar("SAT Min",title,0,255,empty)
cv.createTrackbar("VALUE Min",title,0,255,empty)
cv.createTrackbar("HUE Max",title,179,179,empty)
cv.createTrackbar("SAT Max",title,255,255,empty)
cv.createTrackbar("VALUE Max",title,255,255,empty)

while True:

    _, img = cap.read()
    imgHsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)

    h_min = cv.getTrackbarPos("HUE Min",title)
    h_max = cv.getTrackbarPos("HUE Max", title)
    s_min = cv.getTrackbarPos("SAT Min", title)
    s_max = cv.getTrackbarPos("SAT Max", title)
    v_min = cv.getTrackbarPos("VALUE Min", title)
    v_max = cv.getTrackbarPos("VALUE Max", title)
    # print(h_min)

    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv.inRange(imgHsv,lower,upper)
    result = cv.bitwise_and(img,img, mask = mask)

    mask = cv.cvtColor(mask, cv.COLOR_GRAY2BGR)
    hStack = np.hstack([img,mask,result])
    # cv.imshow('Original', img)
    # cv.imshow('HSV Color Space', imgHsv)
    # cv.imshow('Mask', mask)
    # cv.imshow('Result', result)
    cv.imshow(title, hStack)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()