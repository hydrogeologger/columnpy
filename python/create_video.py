import cv2
import os
from PIL import Image
import tqdm
from tqdm import trange

current_path=os.getcwd()
img_path=current_path+'/output_figure/'

img_list_path = os.listdir(img_path)
#MJPG --> .avi
#mp4v -->.mp4
fps = 30    
size=(6480, 2880) # this size must be the same as plot size !!!
fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
videoWriter = cv2.VideoWriter(current_path+'/test.mp4',fourcc,fps,size)
#i = 0
for i in trange(len(img_list_path),ncols = 100):
    name = os.path.join(img_path, img_list_path[i])
    if name[-3:] == 'jpg':
      frame = cv2.imread(name)
      #img = Image.open(name)
      #print(img.size)
      #print(i)
      #i+=1
      videoWriter.write(frame)
videoWriter.release()