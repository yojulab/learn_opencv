# sudo sysctl -w net.inet.udp.maxdgram=65535    for mac
# sudo sysctl -w net.core.rmem_max=65535    for linux
import socket
import cv2 as cv
# print(cv.__version__)
UDP_IP = '127.0.0.1'        # receiver ip
UDP_PORT = 1234

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

width=640   #1280
height=480  #720
cam_id = 0
flip=0
camSet='nvarguscamerasrc sensor-id='+str(cam_id)+' ! video/x-raw(memory:NVMM), width=3264, height=2464, framerate=21/1,format=NV12 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(width)+', height='+str(height)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
#camSet ='v4l2src device=/dev/video1 ! video/x-raw,width='+str(width)+',height='+str(height)+',framerate=24/1 ! videoconvert ! appsink'
cap = cv.VideoCapture(camSet)
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
