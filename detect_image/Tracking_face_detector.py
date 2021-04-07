from cv2 import cv2 as cv
import numpy as np

# Load the Haar cascade file
face_cascade = cv.CascadeClassifier(
        'datas/haar_cascade_files/haarcascade_frontalface_default.xml')

# Check if the cascade file has been loaded correctly
if face_cascade.empty():
	raise IOError('Unable to load the face cascade classifier xml file')

# Initialize the video capture object
cap = cv.VideoCapture(1)

# Define the scaling factor
scaling_factor = 0.5

# Iterate until the user hits the 'Esc' key
while True:
    # Capture the current frame
    _, frame = cap.read()

    # Resize the frame
    frame = cv.resize(frame, None, 
            fx=scaling_factor, fy=scaling_factor, 
            interpolation=cv.INTER_AREA)

    # Convert to grayscale
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Run the face detector on the grayscale image
    face_rects = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    # Draw a rectangle around the face
    for (x,y,w,h) in face_rects:
        cv.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3)

    # Display the output
    cv.imshow('Face Detector', frame)

    # Check if the user hit the 'Esc' key
    c = cv.waitKey(1)
    if c == 27:
        break

# Release the video capture object
cap.release()

# Close all the windows
cv.destroyAllWindows()
