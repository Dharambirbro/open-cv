# face detection

import cv2
import numpy as np

path='assets/face1.jpg'

faceCascade=cv2.CascadeClassifier("data/haarcascades/haarcascade_frontalface_default.xml")
img=cv2.imread(path)
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces=faceCascade.detectMultiScale(imgGray,1.1,4) #scale factor=1.1,min neighbour=4

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow('original image',img)

cv2.waitKey(0)