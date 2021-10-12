import cv2 as cv
import numpy as np
import os, requests, wget

def store_raw_images():
    neg_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n02917067'
    res = requests.get(neg_images_link)
    if res.status_code != 200:
        exit(1)
    neg_image_urls = res.content.decode("utf-8") 

    storename = 'negative'
    # storename = 'positive'
    if not os.path.exists(storename):
        os.mkdir(storename)

    pic_num = 0
    for geturl in neg_image_urls.split('\r\n'):
        try:
            print(geturl)
            dirname = os.getcwd() + '/' + storename + '/'
            image_name = dirname + geturl.split('/')[-1]
            retname = wget.download(url=geturl, out=image_name)
            if retname is not None:
                img = cv.imread(image_name,cv.IMREAD_GRAYSCALE)
                # should be larger than samples / pos pic (so we can place our image on it)
                resized_image = cv.resize(img, (100, 100))
                resizedname = dirname +str(pic_num) + '.'+ retname.split('.')[-1]
                cv.imwrite(resizedname,resized_image)
                print(retname)
                pic_num =+ 1

        except Exception as e:
            print(str(e))

if __name__ == "__main__":
    store_raw_images()