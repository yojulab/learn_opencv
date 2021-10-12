import cv2 as cv
import numpy as np

# mouse callback function
def draw_shape(event,x,y,flags,param):
    if event == cv.EVENT_FLAG_LBUTTON:
        cv.circle(img,(x,y),10,(255,0,0),-1)

# Create a black image, a window and bind the function to window
img = np.zeros((512,512,3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image',draw_shape)

while(1):
    cv.imshow('image',img)
    if cv.waitKey(20) & 0xFF == ord('q'):
        break
cv.destroyAllWindows()