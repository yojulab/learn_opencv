from cv2 import cv2 as cv
import numpy as np

# Define a function to get the current frame from the webcam
def get_frame(cap, scaling_factor):
    # Read the current frame from the video capture object
    _, frame = cap.read()

    # Resize the image
    frame = cv.resize(frame, None, fx=scaling_factor, 
            fy=scaling_factor, interpolation=cv.INTER_AREA)

    return frame

if __name__=='__main__':
    # Define the video capture object
    cap = cv.VideoCapture(1)

    # Define the scaling factor for the images
    scaling_factor = 0.5

    # Keep reading the frames from the webcam 
    # until the user hits the 'Esc' key
    while True:
        # Grab the current frame
        frame = get_frame(cap, scaling_factor) 

        # Convert the image to HSV colorspace
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

        # Define range of skin color in HSV
        lower = np.array([0, 70, 60])
        upper = np.array([50, 150, 255])

        # Threshold the HSV image to get only skin color
        mask = cv.inRange(hsv, lower, upper)

        # Bitwise-AND between the mask and original image
        img_bitwise_and = cv.bitwise_and(frame, frame, mask=mask)

        # Run median blurring
        img_median_blurred = cv.medianBlur(img_bitwise_and, 5)

        # Display the input and output
        cv.imshow('Input', frame)
        cv.imshow('Output', img_median_blurred)

        # Check if the user hit the 'Esc' key
        c = cv.waitKey(5) 
        if c == 27:
            break

    # Close all the windows
    cv.destroyAllWindows()
