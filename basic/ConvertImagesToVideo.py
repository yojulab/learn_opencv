import cv2 as cv
import os

directory_name = os.getcwd() + '/temps'
def hasdir():
    hasdir = False
    if not os.path.exists(directory_name):
        os.mkdir(directory_name)
    hasdir = os.path.exists(directory_name)
    return hasdir

files = list()
if hasdir():
    files = os.listdir(directory_name)

# Once get shape information 
filename = directory_name+"/image_0.png"
img = cv.imread(filename)
height, width, layers = img.shape
size = (width, height)
filename_output = directory_name + '/output_video.mp3'
fps = 0.5
out_avi = cv.VideoWriter(filename_output, cv.VideoWriter_fourcc(*'MP4V'), fps, size)

# reading each files
for count in range(len(files)):
    filename = directory_name+"/image_"+str(count)+".png"
    # reading each files
    img = cv.imread(filename)
    if img is not None:
        cv.imshow('image_'+str(count), img) # same title if you want one window.
        out_avi.write(img)
    cv.waitKey(50)

out_avi.release()    
cv.waitKey(0)
