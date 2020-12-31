from cv2 import cv2 as cv
# Test Previous
# Server (ip : 192.168.0.12)
# ~$ ffmpeg -f v4l2 -i /dev/video0 -preset ultrafast -vcodec libx264 -vsync 2 -tune zerolatency -b 900k -f h264 udp://0.0.0.:5000
# ffmpeg -re -i /dev/video0 -f rtsp -rtsp_transport udp rtsp://localhost:5000/live.sdp
# ~$ ffmpeg -i /dev/video0 -vsync 2 -f h264 udp://0.0.0.0:5000 
# Client (ip : 192.168.0.6)
# ~$ ffplay udp://127.0.0.1:5000
# ffmpeg -i udp://192.168.0.12:5000 -vcodec copy output.h264
addr = 'udp://:1234'
cap = cv.VideoCapture(addr, cv.CAP_FFMPEG)
if not cap.isOpened():
    print('VideoCapture not opened')
    exit(-1)

import socket
serverAddressPort = ("192.168.0.12", 20001)
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
keys = [ord('x'),ord('y'),ord('z')]
while True:
    ret, frame = cap.read()

    if not ret:
        print('frame empty')
        break

    cv.imshow('image', frame)

    pressKey = cv.waitKey(1)
    if pressKey > 0:
        if pressKey in keys:
            bytesToSend = str.encode(str(pressKey))
            UDPClientSocket.sendto(bytesToSend, serverAddressPort)
        if pressKey == ord('q'):
            break

cap.release()
cv.destroyAllWindows()
