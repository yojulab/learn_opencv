######################## READ IMAGE ############################
import cv2
# LOAD AN IMAGE USING 'IMREAD'
img = cv2.imread("datas/images/lena.png")
# DISPLAY
cv2.imshow("Lena Soderberg",img)
cv2.waitKey(0)

######################### READ VIDEO #############################
import cv2
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture("datas/videos/Armbot.mp4")
while True:
    success, img = cap.read()
    img = cv2.resize(img, (frameWidth, frameHeight))
    cv2.imshow("Result", img)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()

######################### READ WEBCAM  ############################
import cv2
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(1)

cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(cv2.CAP_PROP_BRIGHTNESS,150)
while cap.isOpened():
    success, img = cap.read()
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()