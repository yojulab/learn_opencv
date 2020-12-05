######################## READ IMAGE ############################
from cv2 import cv2 as cv
# LOAD AN IMAGE USING 'IMREAD'
img = cv.imread("datas/images/lena.png")
# DISPLAY
cv.imshow("Lena Soderberg",img)
cv.waitKey(0)

######################### READ VIDEO #############################
from cv2 import cv2 as cv
frameWidth = 640
frameHeight = 480
cap = cv.VideoCapture("datas/videos/Armbot.mp4")
while True:
    success, img = cap.read()
    img = cv.resize(img, (frameWidth, frameHeight))
    # frameWidth = frameWidth + 20
    # frameHeight = frameHeight + 20
    cv.imshow("Result", img)
    if cv.waitKey(1) == ord('q'):
        break
cap.release()

######################### READ WEBCAM  ############################
from cv2 import cv2 as cv
frameWidth = 640
frameHeight = 480
cap = cv.VideoCapture(1)

cap.set(cv.CAP_PROP_FRAME_WIDTH, frameWidth)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, frameHeight)
cap.set(cv.CAP_PROP_BRIGHTNESS,150)
while cap.isOpened():
    success, img = cap.read()
    cv.imshow("Result", img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv.destroyAllWindows()