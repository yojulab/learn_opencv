
# UDP Message too long
# https://stackoverflow.com/questions/22819214/udp-message-too-long
# sudo sysctl -w net.inet.udp.maxdgram=65535    for mac
# sudo sysctl -w net.core.rmem_max=65535    for linux
import socket
from cv2 import cv2 as cv

UDP_IP = '127.0.0.1'        # receiver ip
# UDP_IP = '192.168.0.151'        # receiver ip
UDP_PORT = 1234

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

cap = cv.VideoCapture(0)
# CSI Camera ~$ ls /dev/video*
# cam_id = 0
# camSet ='nvarguscamerasrc sensor-id='+str(cam_id)+' ! video/x-raw(memory:NVMM), width=3264, height=2464, framerate=21/1,format=NV12 ! nvvidconv flip-method=0 ! video/x-raw, width=640, height=480, format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
# cap = cv.VideoCapture(camSet)


print('Start....')
# net.inet.udp.maxdgram=65535

# width, height = 640, 480
width, height = 128, 96
deeps = 3
total_length = width * height * deeps
# divide = 20
divide = 4      
perlength = int(total_length / divide)
reallength = perlength + 1

try : 
    while cap.isOpened():
        ret, frame = cap.read()     # frame (480, 640, 3)
        frame = cv.resize(frame, (width, height))
        d = frame.flatten()
        s = d.tostring()

        for i in range(divide):         # ((480*640*3)/20=46080) < 65535
            sock.sendto(bytes([i]) + s[i*perlength:(i+1)*perlength], (UDP_IP, UDP_PORT))
except :
    pass
finally:
    # When everything done, release the capture
    cap.release()
    cv.destroyAllWindows()

print('End....')
