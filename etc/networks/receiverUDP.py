
# sudo sysctl -w net.inet.udp.maxdgram=65535    for mac
# sudo sysctl -w net.core.rmem_max=65535    for linux

import socket
import numpy
from cv2 import cv2 as cv

UDP_IP = '127.0.0.1'        # receiver ip
# UDP_IP = '192.168.0.151'        # receiver ip
UDP_PORT = 1234

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

width, height = 640, 480
width, height = 160, 120
# width, height = 128, 96
deeps = 3
total_length = width * height * deeps
divide = 20
divide = 3      
# divide = 4      
perlength = int(total_length / divide)
reallength = perlength + 1

s = [b'\xff' * perlength for x in range(divide)]

fourcc = cv.VideoWriter_fourcc(*'DIVX')
# out = cv.VideoWriter('datas/videos/receiver_out.avi', fourcc, 25.0, (width, height))

while True:
    picture = b''

    data, addr = sock.recvfrom(reallength)
    s[data[0]] = data[1:reallength]

    if data[0] == (divide-1):
        for i in range(divide):
            picture += s[i]

        frame = numpy.fromstring(picture, dtype=numpy.uint8)
        frame = frame.reshape(height, width, deeps)
        cv.imshow("frame", frame)
        # out.write(frame)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break
cv.destroyAllWindows()
