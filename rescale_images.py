import cv2 as cv

#img = cv.imread("Images/Cat_white.jpg")
#cv.imshow("Cat_brown",img) # good for small images...

## resize and rescale
def rescale(frame,scale=0.75):
    width= int(frame.shape[1]*scale)    # sets the width
    height= int(frame.shape[0]*scale)    # sets the height

    dimensions =(width,height)    # returns the dimensions

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)   # returns
    # the resized image,dimensions and has interpolations

capture = cv.VideoCapture('Videos/Dog.mp4')   # gets instance of video

while True:
    isTrue,frame = capture.read()  # get the image

    frame_resized = rescale(frame,0.2)

    cv.imshow('Video',frame)   # display each frame
    cv.imshow('Video_resize',frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):  # break out of the loop
        break

capture.release()   # release the capture and destroy the windows
cv.destroyAllWindows()