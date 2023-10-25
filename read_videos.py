import cv2 as cv

#capture = cv.VideoCapture(0)   ## args references the differnet cameras 0- web cam,1-computer or so on...

capture = cv.VideoCapture('Videos/Dog.mp4')   # gets instance of video

while True:
    isTrue,frame = capture.read()  # get the image
    cv.imshow('Video',frame)   # display each frame

    if cv.waitKey(20) & 0xFF == ord('d'):  # break out of the loop
        break

capture.release()   # release the capture and destroy the windows
cv.destroyAllWindows()
