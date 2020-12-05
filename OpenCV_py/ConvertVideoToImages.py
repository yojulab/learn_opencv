from cv2 import cv2 as cv
import os

directoryname = os.getcwd() + '/datas/images/imageframes'
def hasdir():
    hasdir = False
    if not os.path.exists(directoryname):
        os.mkdir(directoryname)
    hasdir = os.path.exists(directoryname)
    return hasdir

def writeFrame(videocapture, second, cnt):
    videocapture.set(cv.CAP_PROP_POS_MSEC, second*1000)
    hasFrames, image = videocapture.read()
    if hasFrames:
        # save frame as PNG file
        cv.imwrite(directoryname+"/image_"+str(cnt)+".png", image)
    return hasFrames

filename = 'datas/videos/Armbot.mp4'
cap = cv.VideoCapture(filename)
sec = 0
count = 0
frameRate = 0.5  # it will capture image in each 0.5 second
success = (cap.isOpened() and hasdir())

while success:
    sec = sec + frameRate
    success = writeFrame(cap, sec, count)
    count = count + 1
