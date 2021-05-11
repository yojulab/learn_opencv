from cv2 import cv2 as cv

#############################################
frameWidth = 640
frameHeight = 480
nPlateCascade = cv.CascadeClassifier("datas/haar_cascade_files/haarcascade_russian_plate_number.xml")
minArea = 200
color = (255,0,255)
###############################################
cap = cv.VideoCapture("datas/videos/licenseplate_01.mp4")
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)
count = 0

while True:
    success, img = cap.read()
    imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    numberPlates = nPlateCascade.detectMultiScale(imgGray, 1.1, 10)
    for (x, y, w, h) in numberPlates:
        area = w*h
        if area >minArea:
            cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
            cv.putText(img,"Number Plate",(x,y-5),
                        cv.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)
            imgRoi = img[y:y+h,x:x+w]
            cv.imshow("ROI", imgRoi)

    cv.imshow("Result", img)

    if cv.waitKey(1) == ord('s'):
        cv.imwrite("datas/output/NoPlate_"+str(count)+".jpg",imgRoi)
        cv.rectangle(img,(0,200),(640,300),(0,255,0),cv.FILLED)
        cv.putText(img,"Scan Saved",(150,265),cv.FONT_HERSHEY_DUPLEX,
                    2,(0,0,255),2)
        cv.imshow("Result",img)
        cv.waitKey(500)
        count +=1

cv.destroyAllWindows()            