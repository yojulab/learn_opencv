import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('datas/images/sudoku.jpg',cv.IMREAD_GRAYSCALE)
# img = cv.imread('datas/images/radial_gradient.png',0)
# img = cv.imread('datas/images/opencv_logo.png',0)
# img = cv.imread('datas/images/load_image.jpg', cv.IMREAD_GRAYSCALE)
# img = cv.medianBlur(img,5)

ret,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,\
            cv.THRESH_BINARY,11,4)
th3 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv.THRESH_BINARY,11,4)

titles = ['Original Image', 'Global Thresholding (v = 127)',
            'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2, th3]

for i in range(4):
    plt.subplot(1,4,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()