
# UDP Message too long
# https://stackoverflow.com/questions/22819214/udp-message-too-long
# sudo sysctl -w net.inet.udp.maxdgram=65535
import socket
from cv2 import cv2 as cv

UDP_IP = '127.0.0.1'        # receiver ip
UDP_PORT = 1234

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

cap = cv.VideoCapture(0)

print('Start....')
# net.inet.udp.maxdgram=65535
try : 
    while cap.isOpened():
        ret, frame = cap.read()     # frame (480, 640, 3)
        d = frame.flatten()
        s = d.tostring()

        for i in range(20):         # ((480*640*3)/20=46080) < 65535
            sock.sendto(bytes([i]) + s[i*46080:(i+1)*46080], (UDP_IP, UDP_PORT))
except :
    pass
finally:
    # When everything done, release the capture
    cap.release()
    cv.destroyAllWindows()

print('End....')
