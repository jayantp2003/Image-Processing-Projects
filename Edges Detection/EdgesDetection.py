# Importing the libraries
import cv2 as cv
import numpy as np

# Reading the file and converting it to Grayscale Image
img = cv.imread("Edges Detection//Img//Img2.webp")
img1 = cv.cvtColor(img,code=cv.COLOR_BGR2GRAY)

# using the canny edge detection algorith to detect edges in the image
edge = cv.Canny(img1,60,200,apertureSize=3)
cv.namedWindow("Original Image",cv.WINDOW_FULLSCREEN)

imgf = np.concatenate((img1,edge),axis=1)
# cv.imshow("Original Image1",img)
# cv.imshow("Original Image2",img1)
cv.imshow("Original Image",imgf)
cv.imwrite("Edges.webp",edge)
cv.waitKey(0)
cv.destroyAllWindows()
