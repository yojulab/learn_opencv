from cv2 import cv2 as cv
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

img = cv.imread(root_path+'/image_processing/datas/images/namecard.png')

if img is None: 
    print("Error opening video stream or file")
    sys.exit()

img = cv.resize(img, (0,0), fx=0.3, fy=0.3)    
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

_, img_binary = cv.threshold(img_gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
contours, _ = cv.findContours(img_binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

dw, dh = 900, 500
import pytesseract
for pts in contours:
    if cv.contourArea(pts) > 5000:
        approx = cv.approxPolyDP(pts, cv.arcLength(pts, True)*0.02, True)
        if len(approx) == 4 and cv.isContourConvex(approx):
            cv.polylines(img, pts, True, (0,0,255))
            srcQuad = reorderPts(approx.reshape(4,2))
            dstQuad = np.array([[0,dh], [dw,dh], [dw,0], [0,0]], dtype=np.float32)

            pers = cv.getPerspectiveTransform(srcQuad, dstQuad)
            img_dst = cv.warpPerspective(img, pers, (dw, dh), flags=cv.INTER_CUBIC)

            dst_rgb = cv.cvtColor(img_dst, cv.COLOR_BGR2RGB)
            print(pytesseract.image_to_string(dst_rgb, lang='Hangul+Hangul_vert+eng+eng_vert'))

cv.imshow('Resource', img)
cv.imshow('Grayscale', img_gray)
cv.imshow('Convert Binary', img_binary)
cv.imshow('dst', img_dst)
if cv.waitKey(0) == 27:
    cv.destroyAllWindows()

