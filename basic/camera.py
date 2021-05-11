from cv2 import cv2 as cv
#import numpy

cam = cv.VideoCapture(0)
cam.set(cv.CAP_PROP_FRAME_WIDTH, 640)
cam.set(cv.CAP_PROP_FRAME_HEIGHT, 480)
cam.set(cv.CAP_PROP_FPS, 7)
#cv2mat = numpy.array([])

while True:
    ret,img = cam.read()
    #ret1=cv.imencode(".jpeg",im,cv2mat)
    #JpegData=cv2mat.tostring()
    #print JpegData
    cv.imshow('video test',img)
    key = cv.waitKey(10)
    if key == 27:
        break
    if key == ord('s'):
        cv.imwrite('capture.jpg',img)

