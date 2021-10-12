import cv2 as cv

# read from images
img = cv.imread('datas/images/load_image.jpg')
# read gray color from images
# img = cv.imread('datas/images/load_image.jpg',1)
cv.imshow('image',img)
while True:
    k = cv.waitKey(0) & 0xFF   # 64bit
    if k == 27:         # wait for ESC key to exit
        break
    elif k == ord('s'): # wait for 's' key to save and exit
        output = "datas/images/output.png'
        # save image with lower compression - bigger file size but faster decoding
        cv.imwrite(output, img, [cv.IMWRITE_PNG_COMPRESSION, 0]) # 0~9

        # check that image saved and loaded again image is the same as original one
        saved_img = cv.imread(output)
        assert saved_img.all() == img.all()

        # save image with lower quality - smaller file size
        cv.imwrite("datas/images/output.jpg', img, [cv.IMWRITE_JPEG_QUALITY, 90]) # 0~100
        break
    
cv.destroyAllWindows()
