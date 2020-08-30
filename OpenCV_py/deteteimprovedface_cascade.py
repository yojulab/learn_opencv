import numpy as np
import pyautogui
import cv2
from PIL import ImageGrab

fourcc = cv2.VideoWriter_fourcc(*'XVID')

face_csc = cv2.CascadeClassifier('improved_cascade.xml')

out = cv2.VideoWriter("output.avi", fourcc, 5.0, (1366, 768))

while True:

    img = ImageGrab.grab(bbox=None)
    # convert image to numpy array
    img_np = np.array(img)
    # convert color space from BGR to RGB
    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    # show image on OpenCV frame
    faces = face_csc.detectMultiScale(frame, 1.1 , 15)

    for (x,y,w,h) in faces:
        detected_icon = cv2.rectangle(frame,(x,y),(x+w,y+h), (255,0,0), 2)
        roi_gray = frame[y:y+h, x:x+w]
        roi_color = img_np[y:y+h,x:x+w]
        cv2.putText(frame,'icon',(x,y),cv2.FONT_HERSHEY_TRIPLEX,0.8,(0,0,255),1)
        cv2.imshow("stream", frame)
    # write frame to video writer
    out.write(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

out.release() 
cv2.destroyAllWindows()