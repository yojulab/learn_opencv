from cv2 import cv2 as cv
import numpy as np
from os import listdir
from os.path import isfile, join

data_path = 'faces/'
onlyfiles = [f for f in listdir(data_path) if isfile(join(data_path,f))]

Training_Data, Labels = [], []

for i, files in enumerate(onlyfiles):
    image_path = data_path + onlyfiles[i]
    images = cv.imread(image_path, cv.IMREAD_GRAYSCALE)
    Training_Data.append(np.asarray(images, dtype=np.uint8))
    Labels.append(i)

Labels = np.asarray(Labels, dtype=np.int32)

model = cv.face.LBPHFaceRecognizer_create()

model.train(np.asarray(Training_Data), np.asarray(Labels))

print("Model Training Complete!!!!!")

face_classifier = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

def face_detector(img, size = 0.5):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray,1.3,5)

    if faces is():
        return img,[]

    for(x,y,w,h) in faces:
        cv.rectangle(img, (x,y),(x+w,y+h),(0,255,255),2)
        roi = img[y:y+h, x:x+w]
        roi = cv.resize(roi, (200,200))

    return img,roi

cap = cv.VideoCapture(0)
while True:

    ret, frame = cap.read()

    image, face = face_detector(frame)

    try:
        face = cv.cvtColor(face, cv.COLOR_BGR2GRAY)
        result = model.predict(face)

        if result[1] < 500:
            confidence = int(100*(1-(result[1])/300))
            display_string = str(confidence)+'% Confidence it is user'
        cv.putText(image,display_string,(100,120), cv.FONT_HERSHEY_COMPLEX,1,(250,120,255),2)


        if confidence > 75:
            cv.putText(image, "Unlocked", (250, 450), cv.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
            cv.imshow('Face Cropper', image)

        else:
            cv.putText(image, "Locked", (250, 450), cv.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
            cv.imshow('Face Cropper', image)


    except:
        cv.putText(image, "Face Not Found", (250, 450), cv.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
        cv.imshow('Face Cropper', image)
        pass

    if cv.waitKey(1)==13:
        break


cap.release()
cv.destroyAllWindows()
