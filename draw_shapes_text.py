import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype = 'uint8')   # width,height and color channels (r,g,b)
#cv.imshow('Blank', blank)

#img = cv.imread('Images/Cats.jpg')  # read the image
#cv.imshow('Cat', img) # show the image

# blank[:] = 0,255,0   # b , g , r   ### this will be green
# blank[:] = 0,0,255   # b , g , r   ### this will be red
# blank[:] = 255,0,0   # b , g , r   ### this will be blue

#blank[:] = 0,123,122   # b , g , r   ### this will be lime brown... using these u get different combos of colors

# blank[200:300,300:400] = 0,123,122 ## set the size of the square

#cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=2)  # get a green rectangle from the origin thickness sets the size of the boundary
## origin point,size,color,thickness of boundary and here the box by default is on the right
#cv.rectangle(blank,(0,0),(250,500),(0,255,255),thickness=cv.FILLED)  # fills the entire rectangle
#cv.rectangle(blank,(0,0),(250,500),(0,255,0),thickness=-1) # appears on the left
cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,255,0),thickness=-1)  ## create a squre on the top left corner manipulating the square sizes
#cv.imshow('Green', blank)

# draw a circle
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255),thickness=cv.FILLED)
#cv.imshow("Circle",blank)


# draw a line
#cv.line(blank, (100,250), (blank.shape[1]//2,blank.shape[0]//2),(255,255,255),thickness=3)
cv.line(blank, (100,250), (300,400),(255,255,255),thickness=3)
cv.imshow("line",blank)

# write text on the image
cv.putText()

#cv.imshow("rectangle",blank)
cv.waitKey(0)