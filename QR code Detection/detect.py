import cv2 as cv
import webbrowser as wb

# vid = cv.VideoCapture(0)
# det= cv.QRCodeDetector()
# ans="www.google.com"
# while(True):
#     flag,img = vid.read() 
#     if(flag==False):
#         break
    
#     data,box,_=det.detectAndDecode(img)

#     if(data):
#         ans = data
#         break

#     cv.imshow("QRCODEscanner", img)    
#     if cv.waitKey(1) == ord("q"):
#         break

# b=wb.open(str(ans))
# vid.release()

img = cv.imread("QR code Detection\img2.png")
detobj = cv.QRCodeDetector()
data,box,_=detobj.detectAndDecode(img)
if(len(data)):
    ans=data
else:
    ans="https://www.google.com"

b=wb.open(str(ans))
# cv.imshow("Output",img)

cv.waitKey(0)
cv.destroyAllWindows()


