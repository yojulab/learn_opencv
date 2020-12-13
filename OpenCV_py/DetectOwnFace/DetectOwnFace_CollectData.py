from cv2 import cv2 as cv
import numpy as np

face_classifier = cv.CascadeClassifier("datas/haar_cascade_files/haarcascade_frontalface_default.xml")


def face_extractor(img):

    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray,1.3,5)

    if faces is():
        return None

    for(x,y,w,h) in faces:
        cropped_face = img[y:y+h, x:x+w]

    return cropped_face


cap = cv.VideoCapture(0)
count = 0

import os
directory_name = 'datas/images/faces/'

if not os.path.exists(directory_name):
    os.mkdir(directory_name)

while cap.isOpened():
    ret, frame = cap.read()
    cropped_area = face_extractor(frame)
    put_text = ''
    if cropped_area is not None:
        count+=1
        area = cv.resize(cropped_area,(200,200))
        area = cv.cvtColor(area, cv.COLOR_BGR2GRAY)

        file_name = directory_name + 'user'+str(count)+'.jpg'
        cv.imwrite(file_name,area)

        put_text = "Face Found!, imwrite() count" + str(count)
    else:
        put_text = "Face not Found"

    cv.putText(area,put_text,(50,50),cv.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
    cv.imshow('Face Cropper',area)

    if cv.waitKey(1)==ord('q') or count==1000:     # Try adjust count 50, 100, 200
        break

cap.release()
cv.destroyAllWindows()
print('Colleting Samples Complete!!!')
