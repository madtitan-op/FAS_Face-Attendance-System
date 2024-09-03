import cv2
import numpy as np



def facedetection() :
    face_D = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    eye = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_eye.xml')

    cam = cv2.VideoCapture(0)

    while 1:
        ret,image=cam.read()
        gray= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        faces= face_D.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=5,minSize=(30,30))

        for (x,y,w,h) in faces:
            cv2.rectangle(image,(x,y),((x+w),(y+h)),(255,0,0),3)
            roi_gray=gray[y:y+h,x:x+w]
            roi_color=image[y:y+h,x:x+w]

            cv2.imshow('face detection',image)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                return



    cam.release()
    cv2.destroyAllWindows()