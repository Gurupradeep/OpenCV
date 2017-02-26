import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('simple.jpeg')

blur = cv2.blur(img,(5,5))
blur1 = cv2.GaussianBlur(img,(5,5),0)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur1),plt.title('Averaging')
plt.xticks([]), plt.yticks([])

cv2.imshow('guassian',blur1);

plt.xticks([]), plt.yticks([])
plt.show()
