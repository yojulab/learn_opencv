from cv2 import cv2 as cv
import os

directoryname = os.getcwd() + '/datas/images/imageframes'
def hasdir():
    hasdir = False
    if not os.path.exists(directoryname):
        os.mkdir(directoryname)
    hasdir = os.path.exists(directoryname)
    return hasdir

files = list()
if hasdir():
    files = os.listdir(directoryname)
# frame_array = []

# reading each files
# Once get shape information 
filename = directoryname+"/image_0.png"
img = cv.imread(filename)
height, width, layers = img.shape
size = (height, width)
filename_output = directoryname + '/output_video.avi'
fps = 0.5
write_video = cv.VideoWriter(filename_output, cv.VideoWriter_fourcc(*'DIVX'), fps, size)

for count in range(len(files)):
    filename = directoryname+"/image_"+str(count)+".png"
    # reading each files
    img = cv.imread(filename)
    cv.imshow('image_'+str(count), img)
    cv.waitKey(50)
    write_video.write(img)

    # inserting the frames into an image array
    # frame_array.append(img)
cv.waitKey(0)
# out = cv.VideoWriter(pathOut, cv.VideoWriter_fourcc(*'DIVX'), fps, size)
# for i in range(len(frame_array)):
#     # writing to a image array
#     out.write(frame_array[i])
# out.release()
