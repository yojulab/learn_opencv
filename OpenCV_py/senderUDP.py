
# UDP Message too long
# https://stackoverflow.com/questions/22819214/udp-message-too-long
# sudo sysctl -w net.inet.udp.maxdgram=65535
import socket
from cv2 import cv2 as cv

UDP_IP = '127.0.0.1'        # receiver ip
UDP_PORT = 9505

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

cap = cv.VideoCapture(0)

print('Start....')
try : 
    while cap.isOpened():
        ret, frame = cap.read()
        d = frame.flatten()
        s = d.tostring()

        for i in range(20):
            sock.sendto(bytes([i]) + s[i*46080:(i+1)*46080], (UDP_IP, UDP_PORT))

            if cv.waitKey(1) & 0xFF == ord('q'):
                break
except :
    pass
finally:
    # When everything done, release the capture
    cap.release()
    cv.destroyAllWindows()

print('End....')
