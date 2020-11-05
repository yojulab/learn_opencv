from cv2 import cv2 as cv
import numpy as np
import time

def diffImage(i):
    diff0 = cv.absdiff(i[0], i[1])
    diff1 = cv.absdiff(i[1], i[2])
    return cv.bitwise_and(diff0, diff1)

def getGrayCameraImage(cam):
    img=cam.read()[1]
    gimg=cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    return gimg

def updateCameraImage(cam, i):
    i[0] = i[1]
    i[1] = i[2]
    i[2] = getGrayCameraImage(cam)

# setup video capture
if __name__ == "__main__":
    thresh = 32
    cam = cv.VideoCapture(0)
    i = [None, None, None]
    for n in range(3):
        i[n] = getGrayCameraImage(cam)

    while True:
        diff = diffImage(i)
        ret,thrimg=cv.threshold(diff, thresh, 1, cv.THRESH_BINARY)
        count = cv.countNonZero(thrimg)
        if (count > 20):
            nz = np.nonzero(thrimg)
            cv.rectangle(diff,(min(nz[1]),min(nz[0])),(max(nz[1]),max(nz[0])),(255,0,0),2)
            cv.rectangle(i[0],(min(nz[1]),min(nz[0])),(max(nz[1]),max(nz[0])),(0,0,255),2)
            cv.imwrite('detect'+str(time.time())+'.jpg',i[0])

        cv.imshow('Detecting Motion', diff)

        # process next image
        updateCameraImage(cam, i)

        key = cv.waitKey(10)
        if key == 27:
            break
