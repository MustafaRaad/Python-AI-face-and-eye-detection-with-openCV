# Programmed By Mustafa Raad Mutashar
# @mustafa_raad7 mustafa.raad.m7@gmail.com

import cv2
#-----Import Classifier----------------------------------------------------
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
#-----Reading the image-----------------------------------------------------
cap = cv2.VideoCapture(0)
#-----Cap---------------
while cap.isOpened():
    _, img = cap.read()
    img = cv2.flip(img, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    
    for (x, y , w ,h) in faces:
        cv2.rectangle(gray, (x,y), (x+w, y+h), (255, 100 , 100), 3)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey ,ew, eh) in eyes:
            cv2.rectangle(roi_gray, (ex,ey), (ex+ew, ey+eh), (200, 200, 200), 5)

    # Display the output
    cv2.imshow('Webcam', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()