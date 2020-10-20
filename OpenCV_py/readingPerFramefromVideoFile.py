import cv2

videoFile = 'OpenCV_py/datas/videos/Armbot.mp4'
# videoFile = 'OpenCV_py/datas/videos/output.avi'
cap = cv2.VideoCapture(videoFile)

break_key = True
count = 0
while cap.isOpened() & break_key:
    flag, frame = cap.read()
    if flag:
        # The frame is ready and already captured
        count += 1   
        # cv2.imshow('video', frame)
        cv2.imshow('video '+str(count)+' frame', frame)
    if cv2.waitKey(9000) == ord('q'):
        break_key = False
        
cap.release()
cv2.destroyAllWindows()