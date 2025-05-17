# pylint: disable=no-member

import numpy as np
import cv2 as cv

# Use built-in Haar cascade path
haar_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']

# Load trained recognizer
face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

# Load a specific test image
img = cv.imread(r'D:\XXX.BADI BAAT CHEET.XXX\openCV\face\demo face photos\Elton John\Elton John.jpg')  # Replace with real file

if img is None:
    raise FileNotFoundError("Could not read the test image. Check the path and filename.")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Person', gray)

# Detect the face in the image
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+w]

    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Label = {people[label]} with a confidence of {confidence}')

    cv.putText(img, str(people[label]), (x, y - 10), cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), 2)
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv.imshow('Detected Face', img)
cv.waitKey(0)
cv.destroyAllWindows()
