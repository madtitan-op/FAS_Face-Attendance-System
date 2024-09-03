import cv2
import numpy as np



# Load Haar Cascade classifiers for face and eye detection
face_R = cv2.face.LBPHFaceRecognizer_create()
face_R.read("model/model.yml")
face_D = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
font = cv2.FONT_HERSHEY_SIMPLEX

if face_D.empty() or eye.empty():
    raise IOError("Error: Could not load one or more Haar Cascade classifiers.")

# Initialize video capture
cam = cv2.VideoCapture(0)
if not cam.isOpened():
    print("Error: Could not open video capture.")
    exit()

while True:
    ret, image = cam.read()
    if not ret:
        print("Error: Failed to capture image.")
        break

    if image is None or not isinstance(image, np.ndarray) or image.size == 0:
        print("Error: Invalid frame.")
        break

    # Convert to RGB for face_recognition
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_D.detectMultiScale(gray_image, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))
    for (x, y, w, h) in faces:
        # Draw rectangle around face
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
        # Extract face ROI
        roi_gray = gray_image[y:y+h, x:x+w]
        roi_color = image[y:y+h, x:x+w]

        #eye detection
        eyes = eye.detectMultiScale(roi_color)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ex+eh),(0,255,0),3)

        #recognition part
        id, conf= face_R.predict(roi_gray)
        if(conf<50):
            cv2.putText(image,"successful",(x-50,y-50),font,1,(255,255,0),2)
            if(id==0):
                cv2.putText(image,"animesh mahata",(x-25,y-25),font,1,(255,255,0),2)
            elif(id==1):
                cv2.putText(image,"jyotirmay tewary",(x-25,y-25),font,1,(255,255,0),2)
            elif(id==2):
                cv2.putText(image,"surjya",(x-25,y-25),font,1,(255,255,0),2)
            elif(id==3):
                cv2.putText(image,"priyanshu kumar",(x-25,y-25),font,1,(255,255,0),2)
            elif(id==4):
                cv2.putText(image,"rohan bhakat",(x-25,y-25),font,1,(255,255,0),2)

            else:
                cv2.putText(image,"none",(x-25,y-25),font,1,(255,255,0),2)
        else:
            cv2.putText(image,"Not successful",(x-50,y-50),font,1,(255,255,0),2)

        #cv2.putText(image,str(conf),(x,y+h),font,1,(255,255,0),2)
        
    # Display the resulting frame
    cv2.imshow('Face Detection', image)

    # Exit on 'q' key
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close windows
cam.release()
cv2.destroyAllWindows()
