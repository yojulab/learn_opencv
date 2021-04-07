import numpy as np
from cv2 import cv2 as cv

cap = cv.VideoCapture(0)
(width, height) = (640,480)
fps = 20.0
cap.set(cv.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, height)
cap.set(cv.CAP_PROP_FPS, fps)

fourcc = cv.VideoWriter_fourcc(*'XVID')
out_avi = cv.VideoWriter('datas/videos/output.avi',fourcc, fps, (width, height))
fourcc = cv.VideoWriter_fourcc(*'MP4V')
out_mp4 = cv.VideoWriter('datas/videos/output.mp4',fourcc, fps, (width, height))

while(True):
    ret, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    out_avi.write(frame)
    out_mp4.write(frame)
    cv.imshow('frame',frame)
    # cv.imshow('frame',gray)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out_avi.release()
out_mp4.release()
cv.destroyAllWindows()
