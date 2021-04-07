
# sudo sysctl -w net.inet.udp.maxdgram=65535    for mac
# sudo sysctl -w net.core.rmem_max=65535    for linux

import socket
import numpy
from cv2 import cv2 as cv

UDP_SERVER_IP = '127.0.0.1'        # sender ip
UDP_SERVER_IP = '192.168.0.151'
# UDP_CLIENT_IP = '127.0.0.1'
UDP_CLIENT_IP = '192.168.0.173'        # receiver ip
UDP_PORT = 20001

UDPServerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
UDPServerSocket.setblocking(0)     # Non-Blocking
# Bind to address and ip
UDPServerSocket.bind((UDP_SERVER_IP, UDP_PORT))

# width, height = 640, 480
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
# out = cv.VideoWriter('temps/receiver_out.avi', fourcc, 25.0, (width, height))

drawing = False
ix, iy = -1, -1
show_frame_name = "cam with mouse"
def draw_shape(event, x, y, flags, param):			# mouse callback function
    if event == cv.EVENT_LBUTTONDOWN:
        global ix, iy, drawing									# Need to define global
        ix, iy = x, y
        drawing = True

cv.namedWindow(show_frame_name);		
cv.setMouseCallback(show_frame_name, draw_shape)

while True:
    picture = b''
    data, addr = None, None
    try:
        data, addr = UDPServerSocket.recvfrom(reallength)
    except BlockingIOError:
        pass

    if data:
        s[data[0]] = data[1:reallength]

        if data[0] == (divide-1):
            for i in range(divide):
                picture += s[i]

            frame = numpy.fromstring(picture, dtype=numpy.uint8)
            frame = frame.reshape(height, width, deeps)
            cv.imshow(show_frame_name, frame)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break

        if drawing:
            bytesToSend = str.encode(str(ix))

            UDPServerSocket.sendto(bytesToSend, (UDP_CLIENT_IP, UDP_PORT))
            drawing = False

cv.destroyAllWindows()
