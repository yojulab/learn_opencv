from cv2 import cv2 as cv
import time
import numpy as np


def current_milli_time(): 
    return int(round(time.time() * 1000))

# Camera feed
cap_cam = cv.VideoCapture(0)
if not cap_cam.isOpened():
    print('Cannot open camera')
    exit()
ret, frame_cam = cap_cam.read()
if not ret:
    print('Cannot open camera stream')
    cap_cam.release()
    exit()

# Video feed
filename = 'datas/videos/Armbot.mp4'
cap_vid = cv.VideoCapture(filename)
if not cap_cam.isOpened():
    print('Cannot open video: ' + filename)
    cap_cam.release()
    exit()
ret, frame_vid = cap_vid.read()
if not ret:
    print('Cannot open video stream: ' + filename)
    cap_cam.release()
    cap_vid.release()
    exit()

# Specify maximum video time in milliseconds
max_time = 1000 * cap_vid.get(cv.CAP_PROP_FRAME_COUNT) / \
    cap_vid.get(cv.CAP_PROP_FPS)

# Resize the camera frame to the size of the video
height = int(cap_vid.get(cv.CAP_PROP_FRAME_HEIGHT))
width = int(cap_vid.get(cv.CAP_PROP_FRAME_WIDTH))

# Starting from now, syncronize the videos
start = current_milli_time()

while True:
    # Capture the next frame from camera
    ret, frame_cam = cap_cam.read()
    if not ret:
        print('Cannot receive frame from camera')
        break
    frame_cam = cv.resize(frame_cam, (width, height),
                           interpolation=cv.INTER_AREA)

    # Capture the frame at the current time point
    time_passed = current_milli_time() - start
    if time_passed > max_time:
        print('Video time exceeded. Quitting...')
        break
    ret = cap_vid.set(cv.CAP_PROP_POS_MSEC, time_passed)
    if not ret:
        print('An error occured while setting video time')
        break
    ret, frame_vid = cap_vid.read()
    if not ret:
        print('Cannot read from video stream')
        break

    # Blend the two images and show the result
    tr = 0.3  # transparency between 0-1, show camera if 0
    frame = ((1-tr) * frame_cam.astype(np.float) + tr *
             frame_vid.astype(np.float)).astype(np.uint8)
    cv.imshow('Transparent result', frame)
    if cv.waitKey(1) == 27:  # ESC is pressed
        break

cap_cam.release()
cap_vid.release()
cv.destroyAllWindows()
