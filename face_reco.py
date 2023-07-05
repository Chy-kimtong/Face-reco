import cv2 
import numpy as np
import pickle

face_cascade = cv2.CascadeClassifier('C:/Users/ASUSKIM/Desktop/AR/New folder/openCV/haarcascade_frontalface_alt2.xml')
eye_cascade = cv2.CascadeClassifier('C:/Users/ASUSKIM/Desktop/AR/New folder/openCV/haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('C:/Users/ASUSKIM/Desktop/AR/New folder/openCV/haarcascade_smile.xml')

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainner.yml")

labels = {"person_name":1}
with open("labels.pickle","rb") as f:
    og_labels = pickle.load(f)
    labels = {v:k for k, v in og_labels.items()}


cap = cv2.VideoCapture(0)

while(True):
    
    # capture frame by frame
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5,minNeighbors=5)
    for (x,y,w,h) in faces:
        # print(x,y,w,h)
        
        roi_gray = gray[y:y+h, x:x+w]   #(cordinate 1 -> height, cordinate 2 -> height)
        roi_color = frame[y:y+h, x:x+w] #(ycorde_start, ycord_end)
        
        # recognize? deep learned model predict keras tensorflow pytorch scikit learn
        id_,conf = recognizer.predict(roi_gray)
        if conf>=45: #and conf <=85:
            # print(id_)
            # print(labels[id_])
            font = cv2.FONT_HERSHEY_SIMPLEX
            name = labels[id_]
            color = (255,255,255)
            stroke = 2
            cv2.putText(frame,name,(x,y),font,1 ,color,stroke,cv2.LINE_AA)
            
            
            
        img_item = "Kimtong1.png"
        cv2.imwrite(img_item,roi_color)
        
        color = (255, 0, 0) #BGR 0-255
        stroke = 2  #thick of line
        end_cord_x = x+w
        end_cord_y = y+h
        cv2.rectangle(frame,(x,y),(end_cord_x,end_cord_y),color,stroke)
        
        # detect eyes
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        # detect smile
        smile = smile_cascade.detectMultiScale(roi_gray)
        for (sx,sy,sw,sh) in smile:
            cv2.rectangle(roi_color,(sx,sy),(sx+sw,sy+sh),(0,0,255),2)   
        
    # displaying the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
    
# when everthing done, release the capture
cap.release()
cv2.destroyAllWindows()