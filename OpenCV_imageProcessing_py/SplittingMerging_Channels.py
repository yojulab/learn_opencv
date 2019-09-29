import cv2

img = cv2.imread('images/load_image.jpg')
img_tmp = img

b,g,r = cv2.split(img)  #is a costly operation
cv2.imshow('blue image Channel',b)
cv2.imshow('green image Channel',g)
cv2.imshow('red image Channel',r)

merge_img = cv2.merge((b,g,r))
cv2.imshow('merge image',merge_img)

img_tmp[:,:,2]=0    #isn't a costly operation
cv2.imshow('blue image Channel by Numpy',img_tmp) 

roi = img[180:340, 330:490]     # region of images
img_tmp[173:333, 100:260] = roi
cv2.imshow('Image ROI',img_tmp)

img_tmp[:,:,1]=0
img_black = img_tmp[:,:,1]
cv2.imshow('Green image Channel by Numpy',img_tmp) 

k = cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()