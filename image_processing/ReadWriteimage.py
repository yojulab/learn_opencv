import cv2

# read gray color from images
img = cv2.imread('image_processing/images/load_image.jpg',1)
cv2.imshow('image',img)
k = cv2.waitKey(0) & 0xFF   # 64bit
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('image_processing/images/load_gray.png',img)
    cv2.destroyAllWindows()
