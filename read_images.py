import cv2 as cv

img = cv.imread("Images/Cat_white.jpg")

cv.imshow("Cat_brown",img) # good for small images...

cv.waitKey(0)

## larger images are offset