# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 13:07:49 2024

@author: Adarsh
"""
#Color Picker Project
import cv2
import numpy as np

def cross(x):
    pass

#Create a blank image
img = np.zeros((300,512,3),np.uint8)
cv2.namedWindow("ColorPicker")

#create switch
switch = "0:OFF\n1:ON"
cv2.createTrackbar(switch,"ColorPicker", 0, 1,cross)

#Create rgb trackbar

cv2.createTrackbar("R","ColorPicker", 0, 255,cross)
cv2.createTrackbar("G","ColorPicker", 0, 255,cross)
cv2.createTrackbar("B","ColorPicker", 0, 255,cross)

while  True:
    cv2.imshow("ColorPicker",img)
    k=cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    
    #gET tRACKERBALL POS
    s = cv2.getTrackbarPos(switch,"ColorPicker")
    r = cv2.getTrackbarPos("R","ColorPicker")
    g = cv2.getTrackbarPos("G","ColorPicker")
    b = cv2.getTrackbarPos("B","ColorPicker")
    
    if s1 == 0:
        img[:] = 0  
    else:
        img[:] = [r,g,b]
        
cv2.destroyAllWindows()

