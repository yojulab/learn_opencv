from cv2 import cv2 as cv
import numpy as np

img = cv.imread("datas/images/cards.jpg")

width,height = 250,350
pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]])  # bottom card
# pts1 = np.float32([[280,120],[450,130],[280,340],[454,369]])    # right card
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv.getPerspectiveTransform(pts1,pts2)
imgOutput = cv.warpPerspective(img,matrix,(width,height))


cv.imshow("Image",img)
cv.imshow("Output",imgOutput)

import matplotlib.pyplot as plt
plt.imshow(img)
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()