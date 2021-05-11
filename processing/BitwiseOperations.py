from cv2 import cv2 as cv

img = cv.imread('datas/images/load_image.jpg')
img2 = cv.imread('datas/images/opencv_logo.png')

# cv.imshow('source image',img)
# cv.imshow('logo',img2)
# I want to put logo on top-left corner, So I create a ROI
rows,cols,channels = img2.shape
roi = img[0:rows, 0:cols ]

cv.imshow('roi source',roi)
# Now create a mask of logo and create its inverse mask also
img2gray = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)
# cv.imshow('img2gray',img2gray)
ret, mask = cv.threshold(img2gray, 10, 255, cv.THRESH_BINARY)
mask_inv = cv.bitwise_not(mask)
cv.imshow('mask',mask)
cv.imshow('mask_inv',mask_inv)

# Now black-out the area of logo in ROI
img1_bg = cv.bitwise_and(roi,roi,mask = mask_inv)
cv.imshow('img1_bg',img1_bg)

# Take only region of logo from logo image.
img2_fg = cv.bitwise_and(img2,img2,mask = mask)
cv.imshow('img2_fg',img2_fg)

# Put logo in ROI and modify the main image
dst = cv.add(img1_bg,img2_fg)
cv.imshow('add(img1_bg,img2_fg)',dst)

img[0:rows, 0:cols ] = dst
cv.imshow('result image',img)
cv.waitKey(0)
cv.destroyAllWindows()
