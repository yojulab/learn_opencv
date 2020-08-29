import cv2

img = cv2.imread('image_processing/images/load_image.jpg')
img2 = cv2.imread('image_processing/images/window_image.jpg')
cv2.imshow('load image',img)
cv2.imshow('window image',img2)

cv2.imshow('load + window image',img+img2)
cv2.imshow('add (load,window) image',cv2.add(img,img2))

def nothing(x):
    pass

cv2.namedWindow('Blending image')
cv2.createTrackbar('blending','Blending image',0,100,nothing)
mix = 1
while(True):
    blending_img = cv2.addWeighted(img2, float(100-mix)/100, img, float(mix)/100,0)
    cv2.imshow('Blending image',blending_img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    mix = cv2.getTrackbarPos('blending', 'Blending image')
    
cv2.destroyAllWindows()