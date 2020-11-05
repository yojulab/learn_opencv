import numpy as np
from cv2 import cv2 as cv

cap = cv.VideoCapture(1)
#fourcc = cv.VideoWriter_fourcc(*'XVID')
#out = cv.VideoWriter('datas/videos/output.avi',fourcc, 20.0, (640,480))
fourcc = cv.VideoWriter_fourcc(*'MP4V')
out = cv.VideoWriter('datas/videos/output.mp4',fourcc, 20.0, (640,480))

while(True):
    ret, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    out.write(frame)
    cv.imshow('frame',gray)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv.destroyAllWindows()
