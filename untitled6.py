# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TsxhlFMAJTG2pDrwEH9iaIbKj0AmYSUu
"""

import cv2

import numpy as np

import cv2

#faceCascade = cv2.CascadeClassifier(‘/content/haarcascade_frontalface_default.xml’)
faceCascade = cv2.CascadeClassifier('/content/haarcascade_frontalface_default.xml')

# /content/haarcascade_frontalface_default.xml

cap = cv2.VideoCapture(0)

cap.set(3,640) # set Width

cap.set(4,480) # set Height

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly, ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(20, 20)
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

    cv2.imshow('video', frame)

    k = cv2.waitKey(30) & 0xff

    if k == 27:  # press 'ESC' to quit
        break

cap.release()
cv2.destroyAllWindows()

from google.colab.patches import cv2_imshow

cap = cv2.VideoCapture('/content/WIN_20231113_19_39_21_Pro.mp4')  # Change to your video file or camera index

if not cap.isOpened():
    print("Error: Could not open video.")
else:
    while True:
        ret, frame = cap.read()

        if not ret:
            print("Error: Can't receive frame (stream end?). Exiting ...")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(20, 20)
        )

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]

        cv2_imshow(frame)

        k = cv2.waitKey(30) & 0xff
        if k == 27:  # press 'ESC' to quit
            break

    cap.release()
    cv2.destroyAllWindows()







from google.colab.patches import cv2_imshow
from IPython.display import display, Javascript
import numpy as np
import cv2

# Function to start webcam
def start_webcam():
    js = (
        "var video = document.createElement('video');"
        "document.body.appendChild(video);"
        "navigator.mediaDevices.getUserMedia({ video: true }).then("
        "  function(stream) {"
        "    video.srcObject = stream;"
        "    video.onloadedmetadata = function() {"
        "      video.play();"
        "    };"
        "  }"
        ");"
    )
    display(Javascript(js))

# Function to capture a frame from the webcam
def capture_frame():
    js = (
        "var canvas = document.createElement('canvas');"
        "canvas.width = video.videoWidth;"
        "canvas.height = video.videoHeight;"
        "var context = canvas.getContext('2d');"
        "context.drawImage(video, 0, 0, canvas.width, canvas.height);"
        "IPython.notebook.kernel.execute('frame = ' + JSON.stringify(context.getImageData(0, 0, canvas.width, canvas.height).data.buffer));"
    )
    display(Javascript(js))

# Start webcam
start_webcam()

# Load face cascade
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + '/content/haarcascade_frontalface_default.xml')

while True:
    # Capture frame from webcam
    capture_frame()

    # Check if frame is not None
    if 'frame' in locals() and frame is not None:
        # Convert the captured frame to a numpy array
        frame = np.frombuffer(frame, dtype=np.uint8).reshape((480, 640, 4))  # Adjust dimensions based on your webcam

        # Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_RGBA2GRAY)

        # Perform face detection
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(20, 20)
        )

        # Draw rectangles around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Display the result
        cv2_imshow(frame)

    # Break the loop if 'ESC' key is pressed
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Release the webcam
cv2.destroyAllWindows()