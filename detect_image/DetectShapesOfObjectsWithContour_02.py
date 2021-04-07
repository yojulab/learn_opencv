from cv2 import cv2 as cv

# path = 'datas/images/shapes_canny.png'
# imgCanny = cv.imread(path, cv.IMREAD_GRAYSCALE)
# cv.imshow('image canny', imgCanny)
# # imgray = cv.cvtColor(im,cv.COLOR_BGR2GRAY)
# # ret,thresh = cv.threshold(imgray,127,255,0)
# contours, hierarchy = cv.findContours(imgCanny,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
# print(contours)
# cnt = contours[4]
# img = cv.drawContours(imgCanny, [cnt], 0, (0,255,0), 3)

# cv.waitKey(0)

path = 'datas/images/shapes.png'
img_color = cv.imread(path)
img_color_approx = img_color.copy()

img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)
# imgBlur = cv.GaussianBlur(img_gray, (7, 7), 1)
# img_binary = cv.Canny(imgBlur, 50, 55)
ret, img_binary = cv.threshold(img_gray, 127, 255, 0)   # Try it otherwise

method = cv.CHAIN_APPROX_NONE
method = cv.CHAIN_APPROX_TC89_L1
method = cv.CHAIN_APPROX_TC89_KCOS
method = cv.CHAIN_APPROX_SIMPLE

contours, hierarchy = cv.findContours(img_binary, cv.RETR_LIST, method)

for cnt in contours:
    area = cv.contourArea(cnt)
    cv.drawContours(img_color, [cnt], 0, (255, 0, 0), 2)  # blue
    # cv.drawContours(img_color, [cnt], 0, (255, 0, 0), 2, -1)  # blue

cv.imshow("result", img_color)
# cv.waitKey(0)

for cnt in contours:
    x, y, w, h = cv.boundingRect(cnt)
    print(x, y, w, h)
    epsilon = 0.02 * cv.arcLength(cnt, True)            # Try 0.05, 0.1
    approx = cv.approxPolyDP(cnt, epsilon, True)
    print( len(approx))

    cv.drawContours(img_color_approx,[approx],0,(0,255,255),2)

cv.imshow("result approx", img_color_approx)

cv.waitKey(0)


