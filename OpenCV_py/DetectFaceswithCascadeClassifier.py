from cv2 import cv2 as cv

cascadefile = "datas/haar_cascade_files/haarcascade_frontalface_default.xml"
# cascadefile = "datas/haar_cascade_files/haarcascade_eye.xml"
# cascadefile = "datas/haar_cascade_files/haarcascade_mcs_nose.xml"
cascade = cv.CascadeClassifier(cascadefile)

# filepath = 'datas/images/lena.png'    # sigle human
# filepath = 'datas/images/faces.jpg'      # few human -> one missing
filepath = 'datas/images/people.jpg'    # a lot human -> can't detect little bit
img = cv.imread(filepath)
# faces = cascade.detectMultiScale(img, 1.1, 4)

imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
faces = cascade.detectMultiScale(imgGray, 1.1, 4)

for (x, y, w, h) in faces:
    cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv.imshow("Result", img)
cv.waitKey(0)
cv.destroyAllWindows()
