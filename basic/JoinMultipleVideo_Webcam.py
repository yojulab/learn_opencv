import cv2 as cv
import numpy as np

import cv2 as cv
frameWidth = 640
frameHeight = 480
# cap = cv.VideoCapture("datas/videos/Armbot.mp4")
cap = cv.VideoCapture(0)
while True:
    success, img = cap.read()
    if img is None:
        break
    img = cv.resize(img, (frameWidth, frameHeight))
    imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    grayToBGR = cv.cvtColor(imgGray,cv.COLOR_GRAY2BGR)  # without Error dimension
    # frameWidth = frameWidth + 20
    # frameHeight = frameHeight + 20
    imgVer = np.hstack((grayToBGR,img))
    cv.imshow("Vertical",imgVer)
    # cv.imshow("Result", img)
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
