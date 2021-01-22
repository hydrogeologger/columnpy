import re
import os
import gc
import pandas as pd
import numpy as np
from tqdm import tqdm
import matplotlib
import matplotlib.image as image
import matplotlib.pylab as pylab
import matplotlib.pyplot as plt
import matplotlib.dates as mdates



current_path=os.getcwd()+'/Redmud_infiltration_test'
column1_back_photo = current_path+'/photos/column1_back/'
column2_back_photo = current_path+'/photos/column2_back/'
column1_front_photo = current_path+'/photos/column1_front/'
column2_front_photo = current_path+'/photos/column2_front/'
output_figure_path = current_path+'/output_figure/'

photo_dir_list = [column1_back_photo,column2_back_photo,
            column1_front_photo,column2_front_photo]

data_file_path = current_path+'/data/'
data = pd.read_csv(data_file_path+'result.csv')

# create pic_dict_keys
key_list = ['column1_front','column2_front',
                'column1_back','column2_back']

pic_dict = { x: {} for x in key_list}

# I really cant find a better way to do this.. 
# if you can plz change these shit
# the purpose for these shit is to identify the pic name 
# and put the date:path to the empty dict

for i in photo_dir_list: # four folder in this path
    for name in os.listdir(i): # path name
        if name[-3:] == 'jpg':
            for ii in key_list: # get the keywords
                if ii in name: # identify which keyword should this pic locate
                    path = os.path.join(output_figure_path,name)
                    pic_idx = pd.to_datetime(''.join(re.findall(r'\d+',path))[1:],
                        format=('%Y%m%d%H%M%S')).strftime('%Y-%m-%d %H:%M:%S')
                    pic_dict[ii][pic_idx]=path # put the date:path to the big nested dict

            #if 'column1_front' in name:
            #    path = os.path.join(output_figure_path,name)
            #    pic_idx = pd.to_datetime(''.join(re.findall(r'\d+',path))[1:],
            #            format=('%Y%m%d%H%M%S')).strftime('%Y-%m-%d %H:%M:%S')
            #    pic_dict['column1_front'][pic_idx]=path
            

            
    



print('test')



