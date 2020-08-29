import cv2
import sys
import os
import numpy as np

def reorderPts(pts):
    idx = np.lexsort((pts[:,1], pts[:,0]))
    pts = pts[idx]
    if pts[0,1] > pts[1,1]:
        pts[[0,1]] = pts[[1,0]]
    if pts[2,1] < pts[3,1]:
        pts[[2,3]] = pts[[3,2]]
    return np.float32(pts)

root_path = os.getcwd()

img = cv2.imread(root_path+'/image_processing/images/namecard.png')

if img is None: 
    print("Error opening video stream or file")
    sys.exit()

img = cv2.resize(img, (0,0), fx=0.3, fy=0.3)    
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, img_binary = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
contours, _ = cv2.findContours(img_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

dw, dh = 900, 500
import pytesseract
for pts in contours:
    if cv2.contourArea(pts) > 5000:
        approx = cv2.approxPolyDP(pts, cv2.arcLength(pts, True)*0.02, True)
        if len(approx) == 4 and cv2.isContourConvex(approx):
            cv2.polylines(img, pts, True, (0,0,255))
            srcQuad = reorderPts(approx.reshape(4,2))
            dstQuad = np.array([[0,dh], [dw,dh], [dw,0], [0,0]], dtype=np.float32)

            pers = cv2.getPerspectiveTransform(srcQuad, dstQuad)
            img_dst = cv2.warpPerspective(img, pers, (dw, dh), flags=cv2.INTER_CUBIC)

            dst_rgb = cv2.cvtColor(img_dst, cv2.COLOR_BGR2RGB)
            print(pytesseract.image_to_string(dst_rgb, lang='Hangul+Hangul_vert+eng+eng_vert'))

cv2.imshow('Resource', img)
cv2.imshow('Grayscale', img_gray)
cv2.imshow('Convert Binary', img_binary)
cv2.imshow('dst', img_dst)
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()

