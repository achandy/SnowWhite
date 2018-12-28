import cv2
import numpy as np

img_file = 'images/Capture2.jpg'
img = cv2.imread(img_file, cv2.IMREAD_COLOR)           # rgb
alpha_img = cv2.imread(img_file, cv2.IMREAD_UNCHANGED) # rgba
hsv_img = cv2.imread(img_file, cv2.IMREAD_HSV)  # grayscale

print type(img)
print 'RGB shape: ', img.shape        # Rows, cols, channels
print 'ARGB shape:', alpha_img.shape
print 'Gray shape:', hsv_img.shape
print 'img.dtype: ', img.dtype
print 'img.size: ', img.size