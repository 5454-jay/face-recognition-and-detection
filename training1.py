import cv2
import sqlite3
import numpy as np

faceDetect=cv2.CascadeClassifier('C:/Users/Jay/Anaconda3/Library/etc/haarcascades/haarcascade_frontalface_default.xml')
cam=cv2.VideoCapture(0);

def insertorupdate(Id,Name):
    conn=sqlite3.connect("E:/Programm/training/Facebase.db")
    cmd="SELECT * FROM person WHERE Id="+str(Id)
    cursos=conn.execute(cmd)
    isRecordExit=0
    for row in cursos:
        isRecordExit=1
    if (isRecordExit==1):
        cmd="UPDATE person SET Name='"+str(Name)+"' WHERE ID="+str(Id)
    else:
        cmd="INSERT INTO person(ID,Name) Values("+str(Id)+",'"+str(Name)+"')"
    conn.execute(cmd)
    conn.commit()
    conn.close()

Id=input('enter user Id = ')
Name=input('enter user Name =')
insertorupdate(Id,Name);
sampleNum=0;

while(True):

    ret, img = cam.read()
    if ret == True:
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=faceDetect.detectMultiScale(gray ,1.3,5);
        for (x,y,w,h) in faces:
            sampleNum=sampleNum+1;
            cv2.imwrite("E:/Programm/New folder/user."+str(Id)+"."+str(sampleNum)+".jpg",img[y:y+h,x:x+w])
            cv2.rectangle(img, (x,y), (x+w, y+h), (0, 0, 255), 1)
            cv2.waitKey(100)
        cv2.imshow('face',img)
        cv2.waitKey(1)
        if(sampleNum>20):   
            break
    else:
        break
cam.release()
cv2.destroyAllWindows()