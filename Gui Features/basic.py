import numpy as np
import cv2

img = cv2.imread('./devilliers.jpeg')

cv2.imshow('image',img)

# Grey scale 
img1 = cv2.imread('./devilliers.jpeg',0)

cv2.imshow('grey',img1)

cv2.waitKey(0)

cv2.destroyAllWindows()

