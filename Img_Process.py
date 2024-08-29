# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 17:02:20 2024

@author: Adarsh
"""
import cv2 

img1 = cv2.imread("D:\RPA\OIP.jpg")
print(img1)
cv2.imshow("original",img1)
cv2.waitKey()
cv2.destroyAllWindows()


img1 = cv2.imread("D:\RPA\OIP.jpg",0)
print(img1)
cv2.imshow("Greayscale Image",img1)
cv2.waitKey()
cv2.destroyAllWindows()


k=cv2.waitKey(0)
if k == ord("s"):
   cv2.imwrite("D:\RPA\OIPP.png", img1)
    
else:
    cv2.destroyAllWindows()
