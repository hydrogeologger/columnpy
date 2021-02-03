import cv2 
import os

current_path=os.getcwd()
img_file_path=current_path+'/tank_photo/'
output_path = current_path+'/finalselected/'
list_path = os.listdir(img_file_path)

for old_name in list_path[:]:
  #print(old_name)
  new_name = os.path.join(output_path, old_name)
  old_name = os.path.join(img_file_path, old_name)
  if old_name[-3:] == 'jpg':
    img = cv2.imread(old_name)
    cropped = img[250:,100:1750]
    #print(old_name)
    #cv2.imshow('test',cropped)
    cv2.imwrite(new_name, cropped)