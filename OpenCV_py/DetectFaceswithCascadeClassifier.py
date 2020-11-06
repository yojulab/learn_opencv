from cv2 import cv2 as cv

cascade = cv.CascadeClassifier(
    "datas/haar_cascade_files/haarcascade_frontalface_default.xml")
img = cv.imread('datas/images/lena.png')
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

faces = cascade.detectMultiScale(imgGray, 1.1, 4)

for (x, y, w, h) in faces:
    cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)


cv.imshow("Result", img)
cv.waitKey(0)
cv.destroyAllWindows()
