from cv2 import cv2 as cv

videoFile = 'datas/videos/Armbot.mp4'
# videoFile = 'datas/videos/output.avi'
cap = cv.VideoCapture(videoFile)

break_key = True
count = 0
while cap.isOpened() & break_key:
    flag, frame = cap.read()
    if flag:
        # The frame is ready and already captured
        count += 1   
        # cv.imshow('video', frame)
        cv.imshow('video '+str(count)+' frame', frame)
    if cv.waitKey(9000) == ord('q'):
        break_key = False
        
cap.release()
cv.destroyAllWindows()