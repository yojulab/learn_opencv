#/usr/bin/env python

import numpy as np
from cv2 import cv2 as cv
from cv2 import cv2 as cv.cv as cv

def clock():
    return cv.getTickCount() / cv.getTickFrequency()

def draw_str(dst, (x, y), s):
    cv.putText(dst, s, (x+1, y+1), cv.FONT_HERSHEY_PLAIN, 1.0, (0, 0, 0), thickness = 2, lineType=cv.CV_AA)
    cv.putText(dst, s, (x, y), cv.FONT_HERSHEY_PLAIN, 1.0, (255, 255, 255), lineType=cv.CV_AA)

def detect(img, cascade):
    #rects = cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=4, minSize=(30, 30), flags = cv.CV_HAAR_SCALE_IMAGE)
    #rects = cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=4, minSize=(80, 80), flags = cv.CV_HAAR_SCALE_IMAGE)
    rects = cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=3, minSize=(80, 80), flags = cv.CV_HAAR_SCALE_IMAGE)
    if len(rects) == 0:
        return []
    rects[:,2:] += rects[:,:2]
    return rects

def draw_rects(img, rects, color):
    for x1, y1, x2, y2 in rects:
        cv.rectangle(img, (x1, y1), (x2, y2), color, 2)

if __name__ == '__main__':

    #cascade_fn = "/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml"
    cascade_fn = "/usr/local/share/OpenCV/lbpcascades/lbpcascade_frontalface.xml"
    #nested_fn  = "/usr/local/share/OpenCV//haarcascades/haarcascade_eye.xml"

    cascade = cv.CascadeClassifier(cascade_fn)
    #nested = cv.CascadeClassifier(nested_fn)

    cam = cv.VideoCapture(0)
    cam.set(cv.cv.CV_CAP_PROP_FRAME_WIDTH, 320)
    cam.set(cv.cv.CV_CAP_PROP_FRAME_HEIGHT, 240)

    while True:
        ret, img = cam.read()
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        gray = cv.equalizeHist(gray)

        t = clock()
        rects = detect(gray, cascade)
        vis = img.copy()
        draw_rects(vis, rects, (0, 255, 0))
        #for x1, y1, x2, y2 in rects:
        #    roi = gray[y1:y2, x1:x2]
        #    vis_roi = vis[y1:y2, x1:x2]
        #    subrects = detect(roi.copy(), nested)
        #    draw_rects(vis_roi, subrects, (255, 0, 0))
        dt = clock() - t

        draw_str(vis, (20, 20), 'time: %.1f ms' % (dt*1000))
        cv.imshow('facedetect', vis)

        if 0xFF & cv.waitKey(5) == 27:
            break
    cv.destroyAllWindows()

