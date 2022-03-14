# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 17:16:37 2021

@author: s4680073
"""

import cv2
import numpy as np
import glob

img_array = []
# for filename in glob.glob('C:/Project/MBDA/large/*.png'):
for filename in glob.glob('*.jpg'):    
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)


out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'), 15, size)
 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()

# from moviepy.editor import *
# clip = (VideoFileClip("ENTER THE FILE PATH HERE"))
# clip.write_gif("output.gif")
# import cv2
# import numpy as np
# import glob
 
# img_array = []
# for filename in glob.glob('C:/New folder/Images/*.jpg'):
#     img = cv2.imread(filename)
#     height, width, layers = img.shape
#     size = (width,height)
#     img_array.append(img)
 
 
# out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'), 15, size)
 
# for i in range(len(img_array)):
#     out.write(img_array[i])
# out.release()
import cv2
import numpy as np
import glob

img_array = []
for filename in glob.glob('C:\Project\MDBA\data_deliverable\photos\column_camera3_labeled\*.PNG'):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (720,1280)
    img_array.append(img)


out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'), 3,size)
 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()