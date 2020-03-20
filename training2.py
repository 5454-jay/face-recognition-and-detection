import cv2,os
import numpy as np
from PIL import Image

rec= cv2.face.LBPHFaceRecognizer_create()
path='E:/Programm/New folder/'
def getImagesWithID(path):
    imagePaths=[os.path.join(path,f) for
     f in os.listdir(path)] 
    faces=[]
    IDs=[]
    for imagePath in imagePaths:
        faceImage=Image.open(imagePath).convert('L')
        faceNp=np.array(faceImage,'uint8')
        Id=int((os.path.split(imagePath)[-1].split('.')[1]))
        faces.append(faceNp)
        print (Id)
        IDs.append(Id)
        cv2.imshow("training",faceNp)
        cv2.waitKey(10)
    return IDs, faces

Ids,faces= getImagesWithID('E:/Programm/New folder/')
rec.train(faces, np.array(Ids))
rec.save('E:/Programm/training/trainner.yml')
print("Model Trained Complete")