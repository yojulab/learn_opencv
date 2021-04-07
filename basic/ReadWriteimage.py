from cv2 import cv2 as cv

# read gray color from images
img = cv.imread('datas/images/load_image.jpg',1)
cv.imshow('image',img)
k = cv.waitKey(0) & 0xFF   # 64bit
if k == 27:         # wait for ESC key to exit
    cv.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv.imwrite('datas/images/load_gray.png',img)
    cv.destroyAllWindows()
