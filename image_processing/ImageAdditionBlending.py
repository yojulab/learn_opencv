from cv2 import cv2 as cv

img = cv.imread('datas/images/load_image.jpg')
img2 = cv.imread('datas/images/window_image.jpg')
cv.imshow('load image',img)
cv.imshow('window image',img2)

cv.imshow('load + window image',img+img2)
cv.imshow('add (load,window) image',cv.add(img,img2))

def nothing(x):
    pass

cv.namedWindow('Blending image')
cv.createTrackbar('blending','Blending image',0,100,nothing)
mix = 1
while(True):
    blending_img = cv.addWeighted(img2, float(100-mix)/100, img, float(mix)/100,0)
    cv.imshow('Blending image',blending_img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
    mix = cv.getTrackbarPos('blending', 'Blending image')
    
cv.destroyAllWindows()