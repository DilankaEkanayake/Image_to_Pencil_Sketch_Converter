# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 10:01:26 2022

@author: Padmamali M.M.L.   Ekanayake E.M.D.D.D.
"""
import numpy as np # numerical data analyse
import cv2 # opencv libraries for image processing

# Read image -- step 1
img = cv2.imread("minions.png")
img = cv2.resize (img,(800,800))

# Create trackbar
def nothing(x):
    pass

# Window name
cv2.namedWindow("Color Adjustments", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Color Adjustments",(300,300))
cv2.createTrackbar("Scale","Color Adjustments",0,255,nothing)
cv2.createTrackbar("Color","Color Adjustments",0,255,nothing)

# Convert into gray
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

while True:
    scale = cv2.getTrackbarPos("Scale","Color Adjustments")
    # Get trackbar value
    clr = cv2.getTrackbarPos ("Color","Color Adjustments")
    
    #Extracting color code
    inverted_gray = clr - gray # invert color image
    blur_img = cv2.GaussianBlur(inverted_gray,(21,21),0)
    inverted_blur = clr - blur_img # invert blurred image
    filtr = cv2.divide(gray,inverted_blur,scale = scale)
    
    
# Output
cv2.imshow("opt",gray)
k = cv2.waitKey (1)
if k == ord("q"):
        cv2.imwrite("break")
if k == ord("s"):
        cv2.imwrite("result.png",filtr)
    
cv2.distroyAllWindows()


