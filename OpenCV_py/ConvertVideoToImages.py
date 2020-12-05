from cv2 import cv2 as cv
import os

directoryname = os.getcwd() + '/datas/images/imagesframes'
def hasdir():
    hasdir = False
    if not os.path.exists(directoryname):
        os.mkdir(directoryname)
        hasdir = os.path.exists(directoryname)
    return hasdir

def getFrame(sec):
    cap.set(cv.CAP_PROP_POS_MSEC, sec*1000)
    hasFrames, image = cap.read()
    if hasFrames:
        # save frame as JPG file
        cv.imwrite(directoryname+"/image_"+str(count)+".jpg", image)
    return hasFrames

filename = 'datas/videos/Armbot.mp4'
cap = cv.VideoCapture(filename)
sec = 0
frameRate = 0.5  # //it will capture image in each 0.5 second
count = 1
success = (cap.isOpened() and hasdir())

while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)
