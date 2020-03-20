import cv2,os
import numpy as npf
import pickle
import sqlite3
from PIL import Image
from six.moves import input


faceDetect=cv2.CascadeClassifier('C:/Users/Jay/Anaconda3/Library/etc/haarcascades/haarcascade_frontalface_default.xml');
rec= cv2.face.LBPHFaceRecognizer_create()
rec.read('E:/Programm/training/trainner.yml')

def getprofile(Id):
    conn=sqlite3.connect("E:/Programm/training/Facebase.db")
    cmd="SELECT * FROM person WHERE Id="+str(Id)
    cursor=conn.execute(cmd)
    profile=None
    for row in cursor:
        profile=row
    conn.close()
    return profile

cam=cv2.VideoCapture(0);
font = cv2.FONT_HERSHEY_SIMPLEX
#profiles={}
while(True):
    ret, img = cam.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,1.2,5);
  
    for (x,y,w,h) in faces:
        Id,conf=rec.predict(gray[y:y+h,x:x+w])
        cv2.rectangle(img, (x,y), (x+w, y+h), (225, 0, 0), 1)
        profile=getprofile(Id)
        if(profile!=None):
            cv2.putText(img,str(profile[1]),(x,y+h+30),font, 1, (255,255,0), 2) 
            #cv2.putText(img,str(profile[0]),(x,y+h+60),font, 1, (255,255,0), 1)
            cv2.imshow('face',img)
        else:
            cv2.putText(img,"buddy",(x,y+h+30),font, 1, (255,255,0), 2)
            cv2.imshow('face',img)
    if(cv2.waitKey(1) == ord('q')):   
        break
cam.release()
cv2.destroyAllWindows()