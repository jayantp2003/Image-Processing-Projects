# importing the libraries required
import time
import cv2 as cv
import numpy as np

# in this case we will need the tool to read video files
vid = cv.VideoCapture(0)

# sent the system to sleep 
time.sleep(3)

# captured the background 
background = 0
for i in range(60):
    ret, background = vid.read()
background = np.flip(background, axis=1)

# Computation

cv.namedWindow("Video")
while True:
    flag,frame = vid.read()
    frame = np.flip(frame,1)

    # Converting the file to HSV formate
    framehsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)

    # thresholding factor
    lr = np.array([0,120,50])
    ur = np.array([10,255,255])
    mask1 = cv.inRange(framehsv,lr,ur)

    lr = np.array([170, 120, 70])
    ur = np.array([180, 255, 255])
    mask2 = cv.inRange(framehsv, lr, ur)
    
    mask1= mask1+mask2
    
    mask1 = cv.morphologyEx(mask1, cv.MORPH_OPEN, np.ones((3, 3), np.uint8))
    mask1 = cv.morphologyEx(mask1, cv.MORPH_DILATE, np.ones((3, 3), np.uint8))

    mask2= cv.bitwise_not(mask1)

    res1 = cv.bitwise_and(frame,frame,mask=mask2)
    res2 = cv.bitwise_and(background,background,mask=mask1)
    finalOutput = cv.addWeighted(res1, 1, res2, 1,0)

    cv.imshow("Video",finalOutput)

    # cv.imshow("Video", frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break



vid.release()
cv.destroyAllWindows()
