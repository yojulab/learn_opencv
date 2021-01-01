from cv2 import cv2 as cv

# Test Previous(Singlecast, Not Multicast)
# Server (ip : 192.168.0.12), Client (ip : 192.168.0.6)
# ~$ ffmpeg -v verbose -f v4l2 -i /dev/video0 -s 100x70 -f mpegts udp://192.168.0.6:20001		# Server to Client
# ~$ ffplay udp://127.0.0.1:20001
addr = 'udp://:20001'
cap = cv.VideoCapture(addr, cv.CAP_FFMPEG)
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
