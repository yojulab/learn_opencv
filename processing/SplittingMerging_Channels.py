from cv2 import cv2 as cv

img = cv.imread('datas/images/load_image.jpg')
img_tmp = img

b,g,r = cv.split(img)  #is a costly operation
cv.imshow('blue image Channel',b)
cv.imshow('green image Channel',g)
cv.imshow('red image Channel',r)

merge_img = cv.merge((b,g,r))
cv.imshow('merge image',merge_img)

img_tmp[:,:,2]=0    #isn't a costly operation
cv.imshow('blue image Channel by Numpy',img_tmp) 

roi = img[180:340, 330:490]     # region of images
img_tmp[173:333, 100:260] = roi
cv.imshow('Image ROI',img_tmp)

img_tmp[:,:,1]=0
img_black = img_tmp[:,:,1]
cv.imshow('Green image Channel by Numpy',img_tmp) 

k = cv.waitKey(0) & 0xFF
cv.destroyAllWindows()