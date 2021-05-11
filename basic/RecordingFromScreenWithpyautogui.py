from cv2 import cv2 as cv
import numpy as np
import os
import pyautogui

start_x=0
start_y=10
end_x=400
end_y=300

# get info from image
# width, height = pyautogui.size()
width = end_x - start_x
height = end_y - start_y

view_img = cv.imread('datas/images/load_image.jpg',1)
cv.imshow('image',view_img)

# Define the codec and create VideoWriter object
output = "./datas/videos/screencapwithpyautogui.mp4"
fourcc = cv.VideoWriter_fourcc(*'MP4V')
out = cv.VideoWriter(output, fourcc, 20.0, (width, height))

while(True):
    try:
        img = pyautogui.screenshot(region=(start_x, start_y, end_x, end_y))
        frame = cv.cvtColor(np.array(img), cv.COLOR_RGB2BGR)
        out.write(frame)
        # cv.imshow('image',frame)

        # StopIteration(0.5)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    except KeyboardInterrupt:
        break

out.release()
cv.destroyAllWindows()
