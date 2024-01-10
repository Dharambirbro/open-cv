# Shape detection
import cv2
import numpy as np


def getContours(img):
    contours,hierarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area=cv2.contourArea(cnt)
        print(area)
        

        if area>0:
            cv2.drawContours(imgContour,cnt,-1,(255,0,0),1)
            peri=cv2.arcLength(cnt,True) # it is cloases so true
            print(peri)
            approx=cv2.approxPolyDP(cnt,0.037*peri,True) # play with it to get best result
            #print(approx) # gives point
            print(len(approx)) # gives how many pooint
            objCor=len(approx)
            x,y,w,h=cv2.boundingRect(approx)

            if objCor ==3 :objectType="Tri"
            elif objCor ==4 :
                aspRatio=w/float(h)
                if aspRatio>0.95 and aspRatio<1.05: objectType="square"
                else:objectType='Rect'

            else: objectType="circle"

            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2) # gives bounding rectangle to each shapes
            cv2.putText(imgContour,objectType,(x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),2)



path='assets/shape2.jpg'

img=cv2.imread(path)
imgContour=img.copy()

imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur=cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny=cv2.Canny(imgBlur,50,50)
getContours(imgCanny)
imgBlack=np.zeros_like(img)


cv2.imshow('Original',img)
cv2.imshow('Grey Image',imgGray)
cv2.imshow('Grey blur',imgBlur)
cv2.imshow('canny blur',imgCanny)
cv2.imshow('canny blur',imgBlack)
cv2.imshow('contour image',imgContour)


cv2.waitKey(0)
