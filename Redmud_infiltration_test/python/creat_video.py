import os
import tqdm
from tqdm import trange
import cv2

current_path=os.getcwd()
img_path = current_path+'/output_figure/'

img_list_path = os.listdir(img_path)
fps = 30    
im = cv2.imread(img_path+img_list_path[0])
size = list(im.shape[:2])
size[0], size[1] = size[1], size[0]

fourcc = cv2.VideoWriter_fourcc(*'MJPG')
im = cv2.imread(img_list_path[0])
videoWriter = cv2.VideoWriter(current_path+'/test.mp4',fourcc,fps,tuple(size))
#i = 0
for i in trange(len(img_list_path),ncols = 100):
    name = os.path.join(img_path, img_list_path[i])
    if name[-3:] == 'jpg':
      frame = cv2.imread(name)

      videoWriter.write(frame)
videoWriter.release()