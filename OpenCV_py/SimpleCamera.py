from cv2 import cv2 as cv

cap = cv.VideoCapture(1)
  
# Read until video is completed
while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the resulting frame
    cv.imshow('frame',frame)
    if cv.waitKey(1) == 27:
        break

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
print('End....')
