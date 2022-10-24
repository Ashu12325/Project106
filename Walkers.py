import cv2
import numpy as np

# Create our body classifier
body_classifier = cv2.CascadeClassifier('C:/Users/akhin/Downloads/PRO-106-ProjectTemplate-main/PRO-106-ProjectTemplate-main/haarcascade_fullbody.xml')

# Initiate video capture for video file
cap = cv2.VideoCapture('C:/Users/akhin/Downloads/PRO-106-ProjectTemplate-main\PRO-106-ProjectTemplate-main/walking.avi')

# Loop once video is successfully loaded
while True:
    
    # Read first frame
    ret, frame = cap.read()
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    bodies = body_classifier.detectMultiScale(gray, 1.2,3)
    for (x, y, w, h) in bodies: 
     cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
     cv2.imshow('pedestrian',frame)
    
    #Convert Each Frame into Grayscale
    
    # Pass frame to our body classifier
    
    
    # Extract bounding boxes for any bodies identified
    

    if cv2.waitKey(1) == 32: #32 is the Space Key
        break

cap.release()
cv2.destroyAllWindows()
