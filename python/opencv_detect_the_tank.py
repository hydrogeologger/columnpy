# Python code to detect an arrow (seven-sided shape) from an image. 
import numpy as np 
import matplotlib.pyplot as plt
import cv2 
import os
   
# Reading image 
current_path=os.getcwd()
img_file_path=current_path+'/tank_photo/'
path = img_file_path + 'railway_tank_2020_09_08_09_10_01.jpg'
img2 = cv2.imread(path, cv2.IMREAD_COLOR) 
   
# Reading same image in another variable and  
# converting to gray scale. 
img = cv2.imread(path, cv2.IMREAD_GRAYSCALE) 
   
# Converting image to a binary image  
# (black and white only image). 
_,threshold = cv2.threshold(img, 110, 255,  
                            cv2.THRESH_BINARY) 
   
# Detecting shapes in image by selecting region  
# with same colors or intensity. 
contours,_=cv2.findContours(threshold, cv2.RETR_TREE, 
                            cv2.CHAIN_APPROX_SIMPLE) 
   
# Searching through every region selected to  
# find the required polygon. 
for cnt in contours : 
    area = cv2.contourArea(cnt) 
   
    # Shortlisting the regions based on there area. 
    # 4000 needs to be modified
    if area > 4000:  
        approx = cv2.approxPolyDP(cnt, 0.009 * cv2.arcLength(cnt, True), True) 
        # Checking if the no. of sides of the selected region. 
        if(len(approx) == 4):  
            #cv2.drawContours(img2, [approx], 0, (0, 0, 255), 5) 
            #（x，y）: upleft point of the box
            x,y,w,h = cv2.boundingRect(cnt) 
            # params need to be modified 
            img2 = cv2.rectangle(img2,(x,y-400),(x+w+900,y+h),(0,255,0),2)
   
plt.imshow(img2)
plt.show()
