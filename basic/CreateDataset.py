import os
import cv2 as cv
import numpy as np

def create_dataset(img_folder):
    img_data_array = []
    class_name = []

    IMG_WIDTH = 200
    IMG_HEIGHT = 200
    for dir1 in os.listdir(img_folder):
        for file in os.listdir(os.path.join(img_folder, dir1)):
            image_path = os.path.join(img_folder, dir1,  file)
            image = cv.imread(image_path, cv.COLOR_BGR2RGB)
            image = cv.resize(image, (IMG_HEIGHT, IMG_WIDTH),
                        interpolation=cv.INTER_AREA)
            image = np.array(image)
            image = image.astype('float32')
            image /= 255
            img_data_array.append(image)
            class_name.append(dir1)

    return (img_data_array, class_name)

# extract the image array and class name
img_data, class_name = create_dataset('datas/images/dataset')

print(class_name)

cv.imshow('image', img_data[3])
cv.waitKey(0)