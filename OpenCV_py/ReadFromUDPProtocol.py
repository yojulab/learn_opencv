from cv2 import cv2 as cv

# Test Previous
# Server (ip : 192.168.0.12)
# ~$ ffmpeg -f v4l2 -i /dev/video0 -preset ultrafast -vcodec libx264 -vsync 2 -tune zerolatency -b 900k -f h264 udp://0.0.0.:5000
# ffmpeg -re -i /dev/video0 -f rtsp -rtsp_transport udp rtsp://localhost:5000/live.sdp
# ~$ ffmpeg -i /dev/video0 -vsync 2 -f h264 udp://0.0.0.0:5000 
# Client (ip : 192.168.0.6)
# ~$ ffplay udp://127.0.0.1:5000
# ffmpeg -i udp://192.168.0.12:5000 -vcodec copy output.h264
cap = cv.VideoCapture('udp://192.168.0.12:5000', cv.CAP_FFMPEG)
if not cap.isOpened():
    print('VideoCapture not opened')
    exit(-1)

while True:
    ret, frame = cap.read()

    if not ret:
        print('frame empty')
        break

    cv.imshow('image', frame)

    if cv.waitKey(1) & 0XFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
