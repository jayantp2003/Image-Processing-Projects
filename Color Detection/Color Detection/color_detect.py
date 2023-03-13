# Importing the libraries needed
import numpy as np
import pandas as pd
import cv2 as cv

# Reading csv file with pandas and giving names to each column and also reading the image
index1=["color","color_name","hex","R","G","B"]
df = pd.read_csv("Color Detection//colors.csv", names=index1, header=None)
img = cv.imread("Color Detection//Trial Image.webp")

# declaring Global variables
clicked = False
b=g=r=xpos=ypos=0

def colorName(R,G,B):
    thres = 10000
    min=-1
    cname=""
    for i in range(len(df)):
        dis = abs(R-int(df.loc[i,"R"]))+abs(G-int(df.loc[i,"G"]))+abs(B-int(df.loc[i,"B"]))
        if(dis<=thres):
            thres=dis
            cname = df.loc[i,"color_name"]
    
    return cname

def draw_function(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        global b,g,r,xpos,ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b,g,r = img[y,x]
        b = int(b)
        g = int(g)
        r = int(r)

cv.namedWindow("Image",cv.WINDOW_FREERATIO)
cv.setMouseCallback('Image',draw_function)

while(1):
    cv.imshow("Image",img)
    if(clicked):
        cv.rectangle(img,(20,20),(750,60),(b,g,r),-1)
        text = colorName(r,g,b) +" R = "+str(r)+" G = "+str(g)+" B = "+str(b)
        cv.putText(img,text,(50,50),2,0.8,(255,255,255),2,cv.LINE_AA)
        if(r+g+b>=600):
            cv.putText(img,text,(50,50),2,0.8,(0,0,0),2,cv.LINE_AA)
        clicked=False
    
    if(cv.waitKey(20) & 0xFF == 27):
        break

# cv.waitKey(0)
cv.destroyAllWindows()
