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

#Capture  video from webcam and save it
fourcc = cv2.VideoWriter_fourcc(*"XVID")  # *"XVID"
#It contain 4 parameter , name, codec,fps,resolution
output = cv2.VideoWriter("output.avi",fourcc,20.0,(640,480),0)
#convert video to grayscale
gray  = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)



Note: On a daily based on my learning curve I will update this file
