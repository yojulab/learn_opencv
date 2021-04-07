import numpy as np
height,width = 150,200,
arr_img = np.zeros((height,width,3), np.uint8)

import matplotlib.pyplot as plt

red_img = arr_img.copy()
red_img[:,:,0] = 255   # red

green_img = arr_img.copy()
green_img[:,:,1] = 255   # green

blue_img = arr_img.copy()
blue_img[:,:,2] = 255   # blue

fig, axes = plt.subplots(1, 4)
axes[0].set_title("arr_img")
axes[0].imshow(arr_img)
axes[1].set_title("blue_img")
axes[1].imshow(blue_img)
axes[2].set_title("green_img")
axes[2].imshow(green_img)
axes[3].set_title("red_img")
axes[3].imshow(red_img)

plt.show()
