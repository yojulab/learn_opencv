import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)
(width, height) = (640,480)
fps = 20.0
# fps = 29.97                                         # 초당 프레임 수
delay = round(1000/ fps)                            # 프레임 간 지연 시간
cap.set(cv.CAP_PROP_ZOOM, 1)                   # 카메라 속성 지정
cap.set(cv.CAP_PROP_FOCUS, 0)
cap.set(cv.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, height)
cap.set(cv.CAP_PROP_FPS, fps)

fourcc = cv.VideoWriter_fourcc(*'XVID')
out_avi = cv.VideoWriter('datas/videos/output.avi',fourcc, fps, (width, height))
fourcc = cv.VideoWriter_fourcc(*'MP4V')
# fourcc = cv.VideoWriter_fourcc(*'DX50')            # 압축 코덱 설정
out_mp4 = cv.VideoWriter('datas/videos/output.mp4',fourcc, fps, (width, height))

# 카메라 속성 콘솔창에 출력
print("압축코덱 숫자:", fourcc)
print("delay: %2d ms" % delay)
print("fps: %.2f" % fps)


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
