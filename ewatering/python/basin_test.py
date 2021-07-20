# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 15:01:35 2021

@author: s4680073
"""
import pandas as pd
import operator
import datetime
import matplotlib
import matplotlib.image as image
from pathlib import Path
import matplotlib.dates as mdates
# Force matplotlib to not use any Xwindows backend.
#matplotlib.use('Agg')
import matplotlib.pyplot as plt
from PIL import Image
def get_date_taken(path):
    from datetime import datetime
    return datetime.strptime(Image.open(path)._getexif()[36867],'%Y:%m:%d %H:%M:%S')
import glob, os
label_fontsize=12
#read raw data from basin tests
basin_mo      =     pd.read_csv('C:/Project/MBDA/basin_test/moisture.csv',usecols=[0,1])
format = '%m/%d/%Y %H:%M'
basin_mo['date_time'] = pd.to_datetime(basin_mo['Time'], format=format)
# basin_mo.set_index(pd.DatetimeIndex(basin_mo['date_time']))

basin_scale      =     pd.read_csv('C:/Project/MBDA/basin_test/scale.csv',usecols=[0,1])
format = '%m/%d/%Y %H:%M'
basin_scale['date_time'] = pd.to_datetime(basin_scale['Time'], format=format)
# basin_scale.set_index(pd.DatetimeIndex(basin_scale['date_time']))
basin=pd.concat([basin_mo,basin_scale])
basin=basin.set_index(pd.DatetimeIndex(basin['date_time']))
del basin['Time']
del basin['date_time']
sch_name='basin'
basin_mo_high=sorted(basin['mo'], key=float)

#path_im='/home/chenming/Projects/tailings/area_51_redmud_4cm_photo_'+sch_name+'/'
#import json
#inp_js = json.load(open('input/input.json'))

path_im='C:/Project/MBDA/basin_test/photo'
#path_im=str(tb_pandas.input_json['photo_path'])

files = filter(os.path.isfile, glob.glob(path_im + "*.jpg"))
#files.sort(key=lambda x: os.path.getmtime(x))
paths = sorted(Path(path_im).iterdir(), key=os.path.getmtime)
file_name=[str(i).split('/')[-1] for i in paths]

#file_name=[i.split('/')[-1] for i in files]
#import os
#for file in os.listdir("/home/chenming/Projects/tailings/area_51_redmud_4cm_photo/"):
#    if file.endswith(".jpg"):
#            print(os.path.join("/home/chenming/Projects/tailings/area_51_redmud_4cm_photo/", file))
#im=image.imread(img_list[0])


# this script is used for calibrating load cells
import matplotlib.pylab as pylab
params = {'legend.fontsize': 11,
          'figure.figsize': (10, 5),
         'axes.labelsize': 12,
         'axes.titlesize':'18',
         'xtick.labelsize':'15',
         'ytick.labelsize':'15',
#         'ytick.labelweight':'bold',
          'axes.labelsize': 18,
           'axes.labelweight':'bold'}
#         'axes.grid':'linewidth=grid_width,color = '0.5''}
#         'linewidth':lw,'markers.size':ms,'markers.edgewidth':mew}
plt.rcParams["font.weight"] = "bold"
plt.rcParams["axes.labelweight"] = "bold"
pylab.rcParams.update(params)
#plt.rcParams['axes.labelsize'] = 16
#plt.rcParams['axes.labelweight'] = 'bold'

lw=4
ms=9
mew=4
grid_width=2
y_fontsize=12
porosity=0.45
basin['volumetric_water_content']=porosity*(basin['mo']-201)/(np.mean(basin['mo'][0:20])-201)
j=0
plt.ioff()
for ii in file_name[:]: #[0:3]:
    plt.rcParams['xtick.labelsize'] = label_fontsize-4
    plt.rcParams['ytick.labelsize'] = label_fontsize-4
    print(str(j)+' of '+str(len(file_name)) )
    # im=image.imrd(ii) 
    im=image.imread(file_name[j])
    
    im_time=get_date_taken(ii)
    # idx_im, min_value = min(enumerate( abs(basin.index-im_time)), key=operator.itemgetter(1))
    
    # im=np.rot90(im,-1)
    
    fig = plt.figure(figsize=(12,8))
    ax = [[] for i in range(4)]
    ax[0] = plt.subplot2grid((2, 2), (0, 0), colspan=1)
    ax[1] = plt.subplot2grid((2, 2), (1, 0), colspan=1)
    ax[0].plot(basin['volumetric_water_content'])
    ax[0].xaxis.set_major_formatter(mdates.DateFormatter('%b/%d'))
    ax[0].axvline(im_time,color='r')
    ax[1].plot(basin['scale'])
    ax[1].xaxis.set_major_formatter(mdates.DateFormatter('%b/%d'))
    ax[1].axvline(im_time,color='r')

    ax[0].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[1].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    
    # ax7.set_ylim(0,20)
    ax[0].set_xlabel('Time', fontsize=label_fontsize, labelpad=10)
    ax[1].set_xlabel('Time', fontsize=label_fontsize, labelpad=10)
    
    ax[0].set_ylabel('Volumetric water \ncontent (-)', fontsize=label_fontsize, labelpad=10)
    ax[1].set_ylabel('Mass (g)', fontsize=label_fontsize, labelpad=10)
    
    
    ax[3]= plt.subplot2grid((2, 2), (0,1),rowspan=2,colspan=1)
    ax[3].imshow(im)
    ax[3].axis('off')

    plt.tight_layout()
    fig.text(0.6,0.2,f'{im_time}',fontsize=label_fontsize+4)
    plt.savefig(ii.split('\\')[-1], format='jpg', dpi=300)
    j=j+1
    plt.close()
img_array = []
for filename in glob.glob('C:/Project/MBDA/basin_test/animation/*.jpg'):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)

out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'), 20, size)
 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()