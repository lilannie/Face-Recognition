import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('road.png', 0)
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.xticks([]), plt.ytickts([]) # to hide tick vaues on X and Y axis
plt.show()
