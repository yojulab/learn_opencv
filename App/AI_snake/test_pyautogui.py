import cv2
import numpy as np
import os
import pyautogui

start_x=0
start_y=10
end_x=300
end_y=400

# get info from image
# width, height = pyautogui.size()
width = end_x - start_x
height = end_y - start_y

view_img = cv2.imread('image_processing/datas/images/load_image.jpg',1)
cv2.imshow('image',view_img)

# Define the codec and create VideoWriter object
output = "datas/videos/screencapwithpyautogui.mp4"
fourcc = cv2.VideoWriter_fourcc(*'MP4V')
out = cv2.VideoWriter(output, fourcc, 20.0, (width, height))

while(True):
    try:
        img = pyautogui.screenshot(region=(start_x, start_y, end_x, end_y))
        frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        out.write(frame)
        # cv2.imshow('image',frame)

        # StopIteration(0.5)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    except KeyboardInterrupt:
        break

out.release()
cv2.destroyAllWindows()
