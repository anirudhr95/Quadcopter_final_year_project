import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('C:\opencv3\opencv\sources\data\haarcascades\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('C:\opencv3\opencv\sources\data\haarcascades\haarcascade_eye.xml')

img = cv2.VideoCapture(0)

while(1):
    _,f=img.read()
    gray = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(f,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = f[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    cv2.imshow('img',f)
    if cv2.waitKey(25) == 27:
        break

cv2.destroyAllWindows()
img.release()
