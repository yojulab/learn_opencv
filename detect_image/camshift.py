from cv2 import cv2 as cv
import numpy as np

# Define a class to handle object tracking related functionality
class ObjectTracker(object):
    def __init__(self, scaling_factor=0.5):
        # Initialize the video capture object
        self.cap = cv.VideoCapture(0)

        # Capture the frame from the webcam
        _, self.frame = self.cap.read()

        # Scaling factor for the captured frame
        self.scaling_factor = scaling_factor

        # Resize the frame
        self.frame = cv.resize(self.frame, None, 
                fx=self.scaling_factor, fy=self.scaling_factor, 
                interpolation=cv.INTER_AREA)

        # Create a window to display the frame
        cv.namedWindow('Object Tracker')

        # Set the mouse callback function to track the mouse
        cv.setMouseCallback('Object Tracker', self.mouse_event)

        # Initialize variable related to rectangular region selection
        self.selection = None

        # Initialize variable related to starting position 
        self.drag_start = None

        # Initialize variable related to the state of tracking 
        self.tracking_state = 0

    # Define a method to track the mouse events
    def mouse_event(self, event, x, y, flags, param):
        # Convert x and y coordinates into 16-bit numpy integers
        x, y = np.int16([x, y]) 

        # Check if a mouse button down event has occurred
        if event == cv.EVENT_LBUTTONDOWN:
            self.drag_start = (x, y)
            self.tracking_state = 0

        # Check if the user has started selecting the region
        if self.drag_start:
            if flags & cv.EVENT_FLAG_LBUTTON:
                # Extract the dimensions of the frame
                h, w = self.frame.shape[:2]

                # Get the initial position
                xi, yi = self.drag_start

                # Get the max and min values
                x0, y0 = np.maximum(0, np.minimum([xi, yi], [x, y]))
                x1, y1 = np.minimum([w, h], np.maximum([xi, yi], [x, y]))

                # Reset the selection variable
                self.selection = None

                # Finalize the rectangular selection
                if x1-x0 > 0 and y1-y0 > 0:
                    self.selection = (x0, y0, x1, y1)

            else:
                # If the selection is done, start tracking  
                self.drag_start = None
                if self.selection is not None:
                    self.tracking_state = 1

    # Method to start tracking the object
    def start_tracking(self):
        # Iterate until the user presses the Esc key
        while True:
            # Capture the frame from webcam
            _, self.frame = self.cap.read()
            
            # Resize the input frame
            self.frame = cv.resize(self.frame, None, 
                    fx=self.scaling_factor, fy=self.scaling_factor, 
                    interpolation=cv.INTER_AREA)

            # Create a copy of the frame
            vis = self.frame.copy()

            # Convert the frame to HSV colorspace
            hsv = cv.cvtColor(self.frame, cv.COLOR_BGR2HSV)

            # Create the mask based on predefined thresholds
            mask = cv.inRange(hsv, np.array((0., 60., 32.)), 
                        np.array((180., 255., 255.)))

            # Check if the user has selected the region
            if self.selection:
                # Extract the coordinates of the selected rectangle
                x0, y0, x1, y1 = self.selection

                # Extract the tracking window
                self.track_window = (x0, y0, x1-x0, y1-y0)

                # Extract the regions of interest 
                hsv_roi = hsv[y0:y1, x0:x1]
                mask_roi = mask[y0:y1, x0:x1]

                # Compute the histogram of the region of 
                # interest in the HSV image using the mask
                hist = cv.calcHist( [hsv_roi], [0], mask_roi, 
                        [16], [0, 180] )

                # Normalize and reshape the histogram
                cv.normalize(hist, hist, 0, 255, cv.NORM_MINMAX);
                self.hist = hist.reshape(-1)

                # Extract the region of interest from the frame
                vis_roi = vis[y0:y1, x0:x1]

                # Compute the image negative (for display only)
                cv.bitwise_not(vis_roi, vis_roi)
                vis[mask == 0] = 0

            # Check if the system in the "tracking" mode
            if self.tracking_state == 1:
                # Reset the selection variable
                self.selection = None
                
                # Compute the histogram back projection
                hsv_backproj = cv.calcBackProject([hsv], [0], 
                        self.hist, [0, 180], 1)

                # Compute bitwise AND between histogram 
                # backprojection and the mask
                hsv_backproj &= mask

                # Define termination criteria for the tracker
                term_crit = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 
                        10, 1)

                # Apply CAMShift on 'hsv_backproj'
                track_box, self.track_window = cv.CamShift(hsv_backproj, 
                        self.track_window, term_crit)

                # Draw an ellipse around the object
                cv.ellipse(vis, track_box, (0, 255, 0), 2)

            # Show the output live video
            cv.imshow('Object Tracker', vis)

            # Stop if the user hits the 'Esc' key
            c = cv.waitKey(5)
            if c == 27:
                break

        # Close all the windows
        cv.destroyAllWindows()

if __name__ == '__main__':
	# Start the tracker
    ObjectTracker().start_tracking()

