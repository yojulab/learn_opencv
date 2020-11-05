from cv2 import cv2 as cv

videoFile = 'datas/videos/Armbot.mp4'
cap = cv.VideoCapture(videoFile)
while not cap.isOpened():
    cap = cv.VideoCapture(videoFile)
    cv.waitKey(1000)
    print ("Wait for the header")

pos_frame = cap.get(cv.CAP_PROP_POS_FRAMES)
while True:
    flag, frame = cap.read()
    if flag:
        # The frame is ready and already captured
        cv.imshow('video', frame)
        pos_frame = cap.get(cv.CAP_PROP_POS_FRAMES)
        print (str(pos_frame)," frames")
    else:
        # The next frame is not ready, so we try to read it again
        cap.set(cv.CAP_PROP_POS_FRAMES, pos_frame-1)
        print ("frame is not ready")
        # It is better to wait for a while for the next frame to be ready
        cv.waitKey(1000)

    if cv.waitKey(10) == 27:
        break
    if pos_frame == cap.get(cv.CAP_PROP_FRAME_COUNT):
        # If the number of captured frames is equal to the total number of frames,
        # we stop
        break