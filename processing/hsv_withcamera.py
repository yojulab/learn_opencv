import numpy as np
import cv2

def tracking_hsv():
    try:
        cap = cv2.VideoCapture(0)
    except :
        return
    
    while True:
        ret, frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        lower_blue = np.array([110, 100, 100])
        uppper_blue = np.array([130, 255, 255])

        lower_green = np.array([50, 100, 100])
        uppper_green = np.array([70, 255, 255])

        lower_red = np.array([-10, 100, 100])
        uppper_red = np.array([10, 255, 255])

        mask_blue = cv2.inRange(hsv, lower_blue, uppper_blue)
        mask_green = cv2.inRange(hsv, lower_green, uppper_green)
        mask_red = cv2.inRange(hsv, lower_red, uppper_red)

        bit_blue = cv2.bitwise_and(frame, frame, mask=mask_blue)
        bit_green = cv2.bitwise_and(frame, frame, mask=mask_green)
        bit_red = cv2.bitwise_and(frame, frame, mask=mask_red)

        cv2.imshow('original', frame)
        cv2.imshow('blue', bit_blue)
        cv2.imshow('green', bit_green)
        cv2.imshow('red', bit_red)

        key = cv2.waitKey(1)
        if key == 27:
            break
    cv2.destroyAllWindows()

tracking_hsv()    