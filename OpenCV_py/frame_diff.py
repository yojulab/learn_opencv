from cv2 import cv2 as cv

# Compute the frame differences
def frame_diff(prev_frame, cur_frame, next_frame):
    # Difference between the current frame and the next frame
    diff_frames_1 = cv.absdiff(next_frame, cur_frame)

    # Difference between the current frame and the previous frame
    diff_frames_2 = cv.absdiff(cur_frame, prev_frame)

    return cv.bitwise_and(diff_frames_1, diff_frames_2)

# Define a function to get the current frame from the webcam
def get_frame(cap, scaling_factor):
    # Read the current frame from the video capture object
    _, frame = cap.read()

    # Resize the image
    frame = cv.resize(frame, None, fx=scaling_factor, 
            fy=scaling_factor, interpolation=cv.INTER_AREA)

    # Convert to grayscale
    gray = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)

    return gray 

if __name__=='__main__':
    # Define the video capture object
    cap = cv.VideoCapture(0)

    # Define the scaling factor for the images
    scaling_factor = 0.5
    
    # Grab the current frame
    prev_frame = get_frame(cap, scaling_factor) 

    # Grab the next frame
    cur_frame = get_frame(cap, scaling_factor) 

    # Grab the frame after that
    next_frame = get_frame(cap, scaling_factor) 

    # Keep reading the frames from the webcam 
    # until the user hits the 'Esc' key
    while True:
        # Display the frame difference
        cv.imshow('Object Movement', frame_diff(prev_frame, 
                cur_frame, next_frame))

        # Update the variables
        prev_frame = cur_frame
        cur_frame = next_frame 

        # Grab the next frame
        next_frame = get_frame(cap, scaling_factor)

        # Check if the user hit the 'Esc' key
        key = cv.waitKey(10)
        if key == 27:
            break

    # Close all the windows
    cv.destroyAllWindows()
