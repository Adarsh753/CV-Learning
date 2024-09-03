Computer Vision Learning Journey
Welcome to the daily log of my Computer Vision learning journey! This repository chronicles my progress and discoveries as I dive into computer vision concepts, tools, and projects. Each day’s entry reflects the new skills and knowledge I've acquired.

Table of Contents
Day 1: Basic Image Handling with OpenCV



Day 1: Basic Image Handling with OpenCV
What I Learned:
How to read and write images using OpenCV.
Display images in a window.
Tools Used: OpenCV (cv2), Python
Key Commands:
python
Copy code
import cv2

# Read an image
image = cv2.imread('path_to_image.jpg')

# Show the image
cv2.imshow('Image Window', image)

# Write an image
cv2.imwrite('output_image.jpg', image)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()

# Resize an image
resized_image = cv2.resize(image, (width, height))
Day 2 : Video operation and capturing videos from various sources
#Here with the help of videoCapture fucntion we easily ready any video.
"""
cap = cv2.VideoCapture("Data\\filename.mp4")   #Here parameter is a path of any video

Day2: Read,write,save and capture video from real time to existing video to various other sources
#Capture  video from webcam and save it

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)   #Here parameter 0 is a path of any video use for webcam
print("check===",cap.isOpened())
#capture video from various source and save it
fourcc = cv2.VideoWriter_fourcc(*"XVID")  # *"XVID"
#It contain 4 parameter , name, codec,fps,resolution
output = cv2.VideoWriter("output.avi",fourcc,20.0,(640,480),0

#convert video to grayscale
 gray  = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

 capture video from mobile cam and youtube
 camera = "http://192.168.0.102:8080/video"
#connect your laptop and android device with same network either wifi or hotspot
cap = cv2.VideoCapture(0)   #Here parameter 0 is a path of any video use for webcam
cap.open(camera)
print("check===",cap.isOpened())
#it is 4 byte code which is use to specify the video codec
fourcc = cv2.VideoWriter_fourcc(*"XVID")  # *"XVID"
#It contain 4 parameter , name, codec,fps,resolution
output = cv2.VideoWriter("output.avi",fourcc,20.0,(640,480),0)

#video capture from youtube using pafy library

import pafy      #open anaconda prompt and type pip install pafy
import cv2
url = "https://www.youtube.com/watch?v=wIAs97ynODo&list=PLaHodugB5x-Ddy_H951h0VHjOjfzZNCBh&index=7"
data = pafy.new(url )
data = data.getbest(preftype="mp4")
cap = cv2.VideoCapture()   #Here parameter 0 is a path of any video use for webcam
cap.open(data.url)

#Day 3 Screen recording

Library Learnt - Opencv,Pyautogui,Numpy,Drawing shapes using OpenCV



 

Note: On a daily based on my learning curve I will update this file


Note: On a daily based on my learning curve I will update this file
