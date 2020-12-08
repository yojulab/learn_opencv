# import the necessary packages
import numpy as np
import pyautogui
import imutils
from cv2 import cv2 as cv

image = pyautogui.screenshot()
image = cv.cvtColor(np.array(image), cv.COLOR_RGB2BGR)
cv.imwrite("in_memory_to_disk.png", image)

pyautogui.screenshot("straight_to_disk.png")

image = cv.imread("straight_to_disk.png")
cv.imshow("Screenshot", imutils.resize(image, width=600))
cv.waitKey(0)