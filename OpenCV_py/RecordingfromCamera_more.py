import numpy as np
from cv2 import cv2 as cv

cap = cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('datas/videos/output.avi',fourcc, 20.0, (640,480))

while (True):
    ret, frame = cap.read()
    if ret:
        frame = cv.flip(frame, 0)    # 이미지 반전,  0:상하, 1 : 좌우
        out.write(frame)
        cv.imshow('frame', frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv.destroyAllWindows()