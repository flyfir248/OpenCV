import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype = 'uint8')   # width,height and color channels (r,g,b)
cv.imshow('Blank', blank)

#img = cv.imread('Images/Cats.jpg')  # read the image
#cv.imshow('Cat', img) # show the image

# blank[:] = 0,255,0   # b , g , r   ### this will be green
# blank[:] = 0,0,255   # b , g , r   ### this will be red
# blank[:] = 255,0,0   # b , g , r   ### this will be blue

#blank[:] = 0,123,122   # b , g , r   ### this will be lime brown... using these u get different combos of colors

# blank[200:300,300:400] = 0,123,122 ## set the size of the square

cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=2)  # get a green rectangle from the origin

#cv.imshow('Green', blank)

cv.imshow("rectangle",blank)
cv.waitKey(0)