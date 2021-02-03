
# UDP Message too long
# https://stackoverflow.com/questions/22819214/udp-message-too-long
# sudo sysctl -w net.inet.udp.maxdgram=65535    for mac
# sudo sysctl -w net.core.rmem_max=65535    for linux
import socket
from cv2 import cv2 as cv

UDP_SERVER_IP = '127.0.0.1'        # sender ip
UDP_SERVER_IP = '192.168.0.173'
# UDP_CLIENT_IP = '127.0.0.1'
UDP_CLIENT_IP = '192.168.0.151'        # receiver ip
UDP_PORT = 20001

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.setblocking(0)     # Non-Blocking
# Bind to address and ip
UDPServerSocket.bind((UDP_SERVER_IP, UDP_PORT))

# width, height = 640, 480
width, height = 160, 120
# width, height = 128, 96
deeps = 3
total_length = width * height * deeps
# divide = 20
divide = 3
# divide = 4      
perlength = int(total_length / divide)
reallength = perlength + 1


cap = cv.VideoCapture(0)
# CSI Camera ~$ ls /dev/video*
# cam_id = 0
# camSet ='nvarguscamerasrc sensor-id='+str(cam_id)+' ! video/x-raw(memory:NVMM), width=3264, height=2464, framerate=21/1,format=NV12 ! nvvidconv flip-method=0 ! video/x-raw, width=640, height=480, format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
# cap = cv.VideoCapture(camSet)


print('Start....')
# net.inet.udp.maxdgram=65535
from jetbot import Robot
import time
robot = Robot()

try : 
    while cap.isOpened():
        ret, frame = cap.read()     # frame (480, 640, 3)
        frame = cv.resize(frame, (width, height))
        d = frame.flatten()
        s = d.tostring()

        for i in range(divide):         # ((480*640*3)/20=46080) < 65535
            UDPServerSocket.sendto(bytes([i]) + s[i*perlength:(i+1)*perlength], (UDP_CLIENT_IP, UDP_PORT))

            # Receive     
            bytesAddressPair = None
            try:
                bytesAddressPair = UDPServerSocket.recvfrom(1024)
            except BlockingIOError:
                pass

            if bytesAddressPair:
                message = bytesAddressPair[0]
                address = bytesAddressPair[1]

                clientMsg = "Message from Client:{}".format(message)
                clientIP = "Client IP Address:{}".format(address)

                print(clientMsg, clientIP)

                x = int(message)
                if x <= width/2:
                    robot.left(0.3)
                else :
                    robot.right(0.3)
                time.sleep(0.5)
                robot.stop()
except :
    pass
finally:
    # When everything done, release the capture
    cap.release()
    cv.destroyAllWindows()

print('End....')
