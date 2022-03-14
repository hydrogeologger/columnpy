# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 09:26:39 2021

@author: s4680073
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 15:01:35 2021

@author: s4680073
"""
import pandas as pd
import operator
from datetime import datetime
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
import matplotlib as mpl
import glob, os

#read raw data from basin tests
column_radius_m=0.05

#path_im='/home/chenming/Projects/tailings/area_51_redmud_4cm_photo_'+sch_name+'/'
#import json
#inp_js = json.load(open('input/input.json'))

path_im2='C:\Project\MDBA\data_deliverable\photos\\column_camera2'
path_im1='C:\Project\MDBA\data_deliverable\photos\\column'

#path_im=str(tb_pandas.input_json['photo_path'])

files = filter(os.path.isfile, glob.glob(path_im1 + "*.jpg"))
#files.sort(key=lambda x: os.path.getmtime(x))
paths = sorted(Path(path_im1).iterdir(), key=os.path.getmtime)
file_name1=[str(i).split('/')[-1] for i in paths]

files2 = filter(os.path.isfile, glob.glob(path_im2 + "*.jpg"))
#files.sort(key=lambda x: os.path.getmtime(x))
paths2 = sorted(Path(path_im2).iterdir(), key=os.path.getmtime)
file_name2=[str(i).split('/')[-1] for i in paths2]
#file_name=[i.split('/')[-1] for i in files]
#import os
#for file in os.listdir("/home/chenming/Projects/tailings/area_51_redmud_4cm_photo/"):
#    if file.endswith(".jpg"):
#            print(os.path.join("/home/chenming/Projects/tailings/area_51_redmud_4cm_photo/", file))
#im=image.imread(img_list[0])


sp_sch.df['scale_decreasing_rate_gPday'] = \
    np.append(np.diff(sp_sch.df['scale']), np.nan) \
    / sp_input['delta_t_s']*constants.sPday
sp_sch.df['scale_decreasing_rate_gPday'].loc[np.abs(sp_sch.df['scale_decreasing_rate_gPday'])>1000]=np.nan
sp_sch.df['infiltrastion_rate_mmPday']=constants.mmPm*\
    constants.kgPg*sp_sch.df['scale_decreasing_rate_gPday']/(constants.rhow_pure_water*np.pi*column_radius_m**2)
sp_sch.df['infiltrastion_rate_mmPday'][sp_sch.df['infiltrastion_rate_mmPday']>0]=np.nan
# sp_sch.df['column_mo1_volumematric_moisture']=( 521-sp_sch.df['column_mo1'])/(521-267)*porosity
sp_sch.df['column_mo1_volumematric_moisture']=( 460-sp_sch.df['column_mo1'])/(460-267)*porosity
sp_sch.df['column_mo2_volumematric_moisture']=( 460-sp_sch.df['column_mo2'])/(460-267)*porosity
sp_sch.df['column_mo3_volumematric_moisture']=( 460-sp_sch.df['column_mo3'])/(460-267)*porosity
sp_sch.df['column_mo4_volumematric_moisture']=( 460-sp_sch.df['column_mo4'])/(460-267)*porosity
sp_sch.df['column_mo5_volumematric_moisture']=( 460-sp_sch.df['column_mo5'])/(460-267)*porosity
# sp_sch_new1=sp_sch.df.loc['2021-07-31 15:00':'2021-08-1 08:30']
# sp_sch_new2=sp_sch.df.loc['2021-08-20 13:30':]
# sp_sch.df=sp_sch_new1.append(sp_sch_new2)

#drying process
column_mo0_volumematric_moisture_dry=0.4
part1_dry_water_m=porosity*(column_mo0_volumematric_moisture_dry+sp_sch.df['column_mo1_volumematric_moisture'])/2*0.1
part2_dry_water_m=porosity*(sp_sch.df['column_mo1_volumematric_moisture']+sp_sch.df['column_mo2_volumematric_moisture'])/2*0.1
part3_dry_water_m=porosity*(sp_sch.df['column_mo2_volumematric_moisture']+sp_sch.df['column_mo3_volumematric_moisture'])/2*0.1
totalwater_m=(part1_dry_water_m+part2_dry_water_m+part3_dry_water_m)
infiltation_rate_mmPday=-np.append(np.nan,constants.mmPm*(np.diff(totalwater_m)/sp_input['delta_t_s'])/constants.dayPs)
infiltation_rate_mmPday[np.abs(infiltation_rate_mmPday)>5]=np.nan
# sp_sch.df['infiltration_rate_mmPday']=infiltation_rate_mmPday
sp_sch.df['totalwater_m']=totalwater_m

# plt.figure()
# plt.plot(sp_sch.df.index[1:],-evp_rate_mmPday)
# plt.xlabel('Time')
# plt.ylabel('Evaporation rate (mm)')



#path_im='/home/chenming/Projects/tailings/area_51_redmud_4cm_photo_'+sch_name+'/'
#import json
#inp_js = json.load(open('input/input.json'))

# path_im1='C:\Project\MDBA\data_deliverable\photos\\column_camera2'
path_im2='C:\Project\MDBA\data_deliverable\photos\column-daily\cut'

#path_im=str(tb_pandas.input_json['photo_path'])

# files = filter(os.path.isfile, glob.glob(path_im1 + "*.jpg"))
# #files.sort(key=lambda x: os.path.getmtime(x))
# paths = sorted(Path(path_im1).iterdir(), key=os.path.getmtime)
# file_name1=[str(i).split('/')[-1] for i in paths]

files2 = filter(os.path.isfile, glob.glob(path_im2 + "*.jpg"))
#files.sort(key=lambda x: os.path.getmtime(x))
paths2 = sorted(Path(path_im2).iterdir(), key=os.path.getmtime)
file_name2=[str(i).split('/')[-1] for i in paths2]
#file_name=[i.split('/')[-1] for i in files]
#import os
#for file in os.listdir("/home/chenming/Projects/tailings/area_51_redmud_4cm_photo/"):
#    if file.endswith(".jpg"):
#            print(os.path.join("/home/chenming/Projects/tailings/area_51_redmud_4cm_photo/", file))
#im=image.imread(img_list[0])


import matplotlib.pylab as pylab
plt.rcParams.update({
    "font.weight": "bold",
    "font.size": 18,
    # "figure.figsize": (9,6),
    "xtick.major.size": 5,
    "xtick.major.pad": 7,
    "xtick.labelsize": 14,
    "ytick.labelsize": 14,
    "axes.labelweight": 'bold',
    "grid.color": "0.5",
    "grid.linestyle": "-",
    "grid.linewidth": 2,
    "lines.linewidth": 4,
    "lines.color": "g",
    "axes.linewidth": 4,
    "legend.fontsize" : 14, 
    "legend.loc":'lower right',
    "legend.framealpha": 0.5,
})

lw=4
ms=9
mew=4
grid_width=2
y_fontsize=16
porosity=0.5
plt.ioff()
# camera1_time=[None]*len(file_name1)
# j=0
# for i in file_name1:
#     camera1_time_str=i[-41:-26]
#     camera1_time[j]=datetime.strptime(camera1_time_str, "%Y-%m-%d_%H%M")
#     j=j+1
# camera1_time=np.array(camera1_time)   
    
camera2_time=[None]*len(file_name2)
j=0
for i in file_name2:
    camera2_time_str=i[-33:-18]
    camera2_time[j]=datetime.strptime(camera2_time_str, "%Y-%m-%d_%H%M")
    j=j+1
camera2_time=np.array(camera2_time)   
y_fontsize=24
plt.ioff()
j=0
interval=2
array=sp_sch.df.to_numpy()
# cross0=[sp_sch['column_mo1_volumematric_moisture'][1],
#        sp_sch['column_mo2_volumematric_moisture'][0],
#        sp_sch['column_mo3_volumematric_moisture'][0],
#        sp_sch['column_mo4_volumematric_moisture'][0],
#        sp_sch['column_mo5_volumematric_moisture'][0]]
# for i in range(1,len(sp_sch.df),100):
    
for ii in file_name2[0:-1:interval]: 
    # im_column_camera2=image.imread(file_name2[j])
    # idx_im, min_value = min(enumerate( abs(camera2_time[j]-camera1_time)), key=operator.itemgetter(1))
    im_column_camera2=image.imread(file_name2[j])
    idx, min_value = min(enumerate( abs(sp_sch.df.index-camera2_time[j])), key=operator.itemgetter(1))
    print(idx)
    moisture_string=[sp_sch.df['column_mo1_volumematric_moisture'][idx],
           sp_sch.df['column_mo2_volumematric_moisture'][idx],
           sp_sch.df['column_mo3_volumematric_moisture'][idx],
           sp_sch.df['column_mo4_volumematric_moisture'][idx],
           sp_sch.df['column_mo5_volumematric_moisture'][idx]]
    # mass_of_water_in_column_kg=cross-cross0
    fig = plt.figure(figsize=(20,12))
    ax = [[] for i in range(6)]
    ax[0] = plt.subplot2grid((20, 12), (0, 0), colspan=5,rowspan=5)
    ax[1] = plt.subplot2grid((20, 12), (6, 0), colspan=5,rowspan=5)
    ax[2] = plt.subplot2grid((20, 12), (12, 0), colspan=5,rowspan=5)
    ax[3] = plt.subplot2grid((20, 12), (0, 5), colspan=3,rowspan=15)
    ax[4] = plt.subplot2grid((20, 12), (6, 8), colspan=8,rowspan=8)
    # ax[5] = plt.subplot2grid((20, 12), (8, 8), colspan=8,rowspan=8)
    plt.subplots_adjust(wspace=1.5)
    ax[0].plot(sp_sch.df['scale'][0]-sp_sch.df['scale'])
    ax[1].plot(sp_sch.df['column_mo1_volumematric_moisture'],label='10cm BGL')
    ax[1].plot(sp_sch.df['column_mo2_volumematric_moisture'],label='20cm BGL')
    ax[1].plot(sp_sch.df['column_mo3_volumematric_moisture'],label='30cm BGL')
    ax[1].plot(sp_sch.df['column_mo4_volumematric_moisture'],label='50cm BGL')
    ax[1].plot(sp_sch.df['column_mo5_volumematric_moisture'],label='70cm BGL')
    # ax[2].plot(constants.kg2g*constants.rhow_pure_water*(sp_sch.df['totalwater_m']-sp_sch.df['totalwater_m'])*(np.pi*column_radius_m**2))
    ax[2].plot(-sp_sch.df['infiltrastion_rate_mmPday'])
    ax[3].plot(moisture_string,[-0.1,-0.2,-0.3,-0.5,-0.7],linewidth=grid_width+2)
    ax[3].set_xlim([0,.5])
    ax[3].set_yticks([-0.7,-0.6,-0.5,-0.4,-0.3,-0.2,-0.1,0])
    ax[3].set_yticklabels(['0.7','0.6','0.5','0.4','0.3','0.2','0.1','0'])
    ax[3].set_xlabel('Volumetric water content (-)')
    ax[3].set_ylabel('Depth (m)')
    ax[0].grid(True,which="both",ls=":",color = '0.5')
    ax[1].grid(True,which="both",ls=":",color = '0.5')
    ax[2].grid(True,which="both",ls=":",color = '0.5')
    ax[3].grid(True,which="both",ls=":",color = '0.5')
    ax[0].axvline(camera2_time[j],color='r')
    ax[1].axvline(camera2_time[j],color='r')
    ax[2].axvline(camera2_time[j],color='r')
    ax[1].legend()

    ax[4].imshow(im_column_camera2)
    ax[4].axis('off')
    # fig.text(0.01,0.68,f'{im_time}',fontsize=y_fontsize,color='k')
    
    
    # ax[5].imshow(im_column_camera2,aspect='auto')
    # ax[5].axis('off')

    ax[0].set_xticklabels([])
    ax[1].set_xticklabels([])
    ax[2].set_xlabel('Time')
    ax[3].set_xlabel('Volumetric \nwater content \n(m$^3$/m$^3$)')
    ax[0].set_ylabel('Infiltration \n(g)')
    ax[1].set_ylabel('Volumetric \nwater content \n(m$^3$/m$^3$)')
    ax[2].set_ylabel('Infiltration \nrate \n(mm/day)')
    ax[3].set_ylabel('Depth (m)')
    # plt.setp(ax.spines.values(), linewidth=2)
    ax[2].xaxis.set_major_formatter(mdates.DateFormatter('%b/%d'))
    # ax[3].plot(sp_sch['column_mo1_volumematric_moisture'][0:idx],label='10cm below surface')
    # ax[3].plot(sp_sch['column_mo2_volumematric_moisture'][0:idx],label='20cm below surface')
    # ax[3].plot(sp_sch['column_mo3_volumematric_moisture'][0:idx],label='30cm below surface')
    # ax[3].plot(sp_sch['column_mo4_volumematric_moisture'][0:idx],label='50cm below surface')
    # ax[3].plot(sp_sch['column_mo5_volumematric_moisture'][0:idx],label='70cm below surface')
    # ax[3].plot(array[:,-5],label='10cm below surface',linewidth=grid_width+2)
    # ax[3].plot(array[:,-4],label='20cm below surface',linewidth=grid_width+2)
    # ax[3].plot(array[:,-3],label='30cm below surface',linewidth=grid_width+2)
    # ax[3].plot(array[:,-2],label='50cm below surface',linewidth=grid_width+2)
    # ax[3].plot(array[:,-1],label='70cm below surface',linewidth=grid_width+2)
    # ax[1].legend(loc='center left', bbox_to_anchor=(1, 0.5))
    # # ax[3].set_xlim([datetime.date(2021, 7, 31), datetime.date(2021, 8, 30)])
    # # ax[3].set_xlim([0,len(sp_sch)])
    # # ax[3].set_xticks(range(0,len(sp_sch),1152*2))#1152 is the number of 10 mins in 8 days
    # ax[3].set_xticklabels(['0','16','32','48','64','80','96',''],fontsize=y_fontsize)
    # ax[3].set_xlabel('Time (day)',fontsize=y_fontsize)
    # ax[3].set_ylim([0,0.5])
    # ax[3].set_ylabel('Volumetric water \n content (-)',fontsize=y_fontsize)
    # ax[3].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    # ax[3].vlines(idx, -50000, 50000,  colors='red', linestyles='-', linewidth=2).set_zorder(10)
    # ax[3].xaxis.set_major_formatter(mdates.DateFormatter('%b/%d'))
    plt.tight_layout()
    fig.savefig(ii.split('\\')[-1], format='jpg', dpi=100)
    plt.close()
    # n=n+1
    j=j+interval
    
img_array=[]
for filename in glob.glob('C:\Project\MDBA\dashboard_column\*.jpg'):    
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)


out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'), 15, size)
 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()
