import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('datas/images/noisy.jpg', cv.IMREAD_GRAYSCALE)
# img = cv.imread('datas/images/radial_gradient.png', cv.IMREAD_GRAYSCALE)
# img = cv.imread('datas/images/opencv_logo.png', cv.IMREAD_GRAYSCALE)
# img = cv.imread('datas/images/load_image.jpg', cv.IMREAD_GRAYSCALE)

# global thresholding
ret1,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)

# Otsu's thresholding
ret2,th2 = cv.threshold(img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

# Otsu's thresholding after Gaussian filtering
# blur = cv.GaussianBlur(img,(5,5),0)
ret3,th3 = cv.threshold(img,0,255,cv.THRESH_BINARY+cv.ADAPTIVE_THRESH_GAUSSIAN_C)

# plot all the images and their histograms
images = [img, 0, th1,
          img, 0, th2,
          img, 0, th3]
titles = ['Original Noisy Image','Histogram','Global Thresholding (v=127)',
          'Original Noisy Image','Histogram',"Otsu's Thresholding",
          'Gaussian filtered Image','Histogram',"Otsu's Thresholding"]


for i in range(3):
    plt.subplot(3,3,i*3+1),plt.imshow(images[i*3],'gray')
    plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
    plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256)
    plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
    plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2],'gray')
    plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])
plt.show()