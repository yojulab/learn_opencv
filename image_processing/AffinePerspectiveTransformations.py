import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('image_processing/images/sudoku.jpg')
rows,cols,ch = img.shape

pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])
M = cv2.getAffineTransform(pts1,pts2)
dst = cv2.warpAffine(img,M,(cols,rows))
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')

# pts3 = np.float32([[56,65],[368,52],[28,387],[389,390]])
# pts4 = np.float32([[0,0],[300,0],[0,300],[300,300]])
# M2 = cv2.getPerspectiveTransform(pts3,pts4)
# dst2 = cv2.warpPerspective(img,M2,(300,300))
# # plt.subplot(123),plt.imshow(img),plt.title('Input Affine')
# plt.subplot(124),plt.imshow(dst2),plt.title('Output Perspective')

plt.show()