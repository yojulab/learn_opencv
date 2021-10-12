import cv2 as cv
import numpy as np
import Tracking_Framedifferencing
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

smtp_server = "smtp.gmail.com"
port = 587
portssl = 465
userid = "mahau.master@gmail.com"
passwd = "************"

def sendmail(image):
    to=[userid]
    imageByte=cv.imencode(".jpeg", image)[1].tostring()
    msg = MIMEMultipart()
    imageMime=MIMEImage(imageByte)
    msg.attach(imageMime)
    msg["From"] = 'Me'
    msg["To"] = to[0]
    msg["Subject"] = "Invader is coming!"

    #server = smtplib.SMTP_SSL(smtp_server, portssl)
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo_or_helo_if_needed()
    server.starttls()
    server.ehlo_or_helo_if_needed()
    ret, m = server.login(userid, passwd)
    if ret != 235:
        print("login fail")
        return
    server.sendmail('me', to, msg.as_string())
    server.quit()

if __name__ == "__main__":
    thresh = 16
    cam = cv.VideoCapture(0)
    cam.set(cv.CAP_PROP_FRAME_WIDTH, 320)
    cam.set(cv.CAP_PROP_FRAME_HEIGHT, 240)
    if cam.isOpened() == False:
        print("Cam isn't opened")
        exit()
    i = [None, None, None]
    for n in range(3):
        i[n] = Tracking_Framedifferencing.getGrayCameraImage(cam)
    flag = False
    checkFlag = 0
    while True:
        diff = Tracking_Framedifferencing.diffImage(i)
        ret,thrimg=cv.threshold(diff, thresh, 1, cv.THRESH_BINARY)
        count = cv.countNonZero(thrimg)
        # if invader is checked
        if (count > 1):
            checkFlag += 1
        if checkFlag >= 10 and flag == False:
#             sendmail(i[2])
            flag = True
            print ("Invader is coming!")
        elif count == 0 and flag == True:
            flag = False
            checkFlag = 0

        # process next image
        Tracking_Framedifferencing.updateCameraImage(cam, i)

        key = cv.waitKey(10)
        if key == 27:
            break
