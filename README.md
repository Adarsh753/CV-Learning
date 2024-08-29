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

Note: On a daily based on my learning curve I will update this file
