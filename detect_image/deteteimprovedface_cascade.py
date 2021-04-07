import numpy as np
import pyautogui
from cv2 import cv2 as cv
from PIL import ImageGrab

fourcc = cv.VideoWriter_fourcc(*'XVID')

face_csc = cv.CascadeClassifier('improved_cascade.xml')

out = cv.VideoWriter("output.avi", fourcc, 5.0, (1366, 768))

while True:

    img = ImageGrab.grab(bbox=None)
    # convert image to numpy array
    img_np = np.array(img)
    # convert color space from BGR to RGB
    frame = cv.cvtColor(img_np, cv.COLOR_BGR2RGB)
    # show image on OpenCV frame
    faces = face_csc.detectMultiScale(frame, 1.1 , 15)

    for (x,y,w,h) in faces:
        detected_icon = cv.rectangle(frame,(x,y),(x+w,y+h), (255,0,0), 2)
        roi_gray = frame[y:y+h, x:x+w]
        roi_color = img_np[y:y+h,x:x+w]
        cv.putText(frame,'icon',(x,y),cv.FONT_HERSHEY_TRIPLEX,0.8,(0,0,255),1)
        cv.imshow("stream", frame)
    # write frame to video writer
    out.write(frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

out.release() 
cv.destroyAllWindows()