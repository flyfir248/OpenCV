import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype = 'uint8')   # width,height and color channels (r,g,b)
cv.imshow('Blank', blank)

#img = cv.imread('Images/Cats.jpg')  # read the image
#cv.imshow('Cat', img) # show the image

blank[:] = 0,255,0
cv.imshow('Green', blank)

cv.waitKey(0)