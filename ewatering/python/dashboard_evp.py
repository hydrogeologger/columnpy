# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 10:21:00 2021
Create a dashboard to monitor evaporation process
@author: s4680073
"""
import matplotlib.pylab as pylab
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
import glob, os,cv2


sch_name='sa'
#path_im='/home/chenming/Projects/tailings/area_51_redmud_4cm_photo_'+sch_name+'/'
#import json
#inp_js = json.load(open('input/input.json'))

path_im='C:\Project\MDBA\data_deliverable\photos\sa2_scaled'
#path_im=str(tb_pandas.input_json['photo_path'])

files = filter(os.path.isfile, glob.glob(path_im + "*.jpg"))
#files.sort(key=lambda x: os.path.getmtime(x))
paths = sorted(Path(path_im).iterdir(), key=os.path.getmtime)
file_name=[str(i).split('/')[-1] for i in paths]
path_im_sa3='C:\Project\MDBA\data_deliverable\photos\sa3_scaled'
files_sa3 = filter(os.path.isfile, glob.glob(path_im_sa3 + "*.jpg"))
#files.sort(key=lambda x: os.path.getmtime(x))
paths_sa3 = sorted(Path(path_im_sa3).iterdir(), key=os.path.getmtime)
file_name_sa3=[str(i).split('/')[-1] for i in paths_sa3]
#file_name=[i.split('/')[-1] for i in files]
#import os
#for file in os.listdir("/home/chenming/Projects/tailings/area_51_redmud_4cm_photo/"):
#    if file.endswith(".jpg"):
#            print(os.path.join("/home/chenming/Projects/tailings/area_51_redmud_4cm_photo/", file))
#im=image.imread(img_list[0])

# files = filter(os.path.isfile, glob.glob(path_im + "*.jpg"))
# #files.sort(key=lambda x: os.path.getmtime(x))
# paths = sorted(Path(path_im).iterdir(), key=os.path.getmtime)
# file_name=[str(i).split('/')[-1] for i in paths]
# path_im_sa2='C:\Project\MBDA\data_deliverable\photos\sa2_scaled'
path_im_sa2='C:\Project\MDBA\data_deliverable\photos\sa2_scaled'

files_sa2 = filter(os.path.isfile, glob.glob(path_im_sa2 + "*.jpg"))
#files.sort(key=lambda x: os.path.getmtime(x))
paths_sa2 = sorted(Path(path_im_sa2).iterdir(), key=os.path.getmtime)
file_name_sa2=[str(i).split('/')[-1] for i in paths_sa2]
#file_name=[i.split('/')[-1] for i in files]

# this script is used for calibrating load cells
params = {'legend.fontsize': 11,
          'figure.figsize': (10, 5),
         'axes.labelsize': 12,
         'axes.titlesize':'18',
         'xtick.labelsize':'15',
         'ytick.labelsize':'15',
#         'ytick.labelweight':'bold',
          'axes.labelsize': 18,
          'axes.labelweight':'bold'}
#         'linewidth':lw,'markers.size':ms,'markers.edgewidth':mew}
plt.rcParams["font.weight"] = "bold"
plt.rcParams["axes.labelweight"] = "bold"
pylab.rcParams.update(params)
#plt.rcParams['axes.labelsize'] = 16
#plt.rcParams['axes.labelweight'] = 'bold'
sp_sch.df['sa1_mo1_volumematric_moisture']=( sp_sch.df['sa1_mo1']-1860)/(3000-1860)*porosity
sp_sch.df['sa1_mo2_volumematric_moisture']=( sp_sch.df['sa1_mo2']-1880)/(3000-1880)*porosity
sp_sch.df['sa1_mo3_volumematric_moisture']=( sp_sch.df['sa1_mo3']-1860)/(3000-1860)*porosity
sp_sch.df['sa1_mo4_volumematric_moisture']=( sp_sch.df['sa1_mo4']-1850)/(3000-1850)*porosity
sp_sch.df['sa1_mo5_volumematric_moisture']=( sp_sch.df['sa1_mo5']-1860)/(3000-1860)*porosity

sp_sch.df['sa2_mo1_volumematric_moisture']=( sp_sch.df['sa2_mo1']-1900)/(3083-1900)*porosity
sp_sch.df['sa2_mo2_volumematric_moisture']=( sp_sch.df['sa2_mo2']-1900)/(3083-1900)*porosity
sp_sch.df['sa2_mo3_volumematric_moisture']=( sp_sch.df['sa2_mo3']-1900)/(3083-1900)*porosity
sp_sch.df['sa2_mo4_volumematric_moisture']=( sp_sch.df['sa2_mo4']-1900)/(3083-1900)*porosity
sp_sch.df['sa2_mo5_volumematric_moisture']=( sp_sch.df['sa2_mo5']-1900)/(3083-1900)*porosity

sp_sch.df['sa3_mo1_volumematric_moisture']=( sp_sch.df['sa3_mo1']-180)/(380-180)*porosity
sp_sch.df['sa3_mo2_volumematric_moisture']=( sp_sch.df['sa3_mo2']-180)/(380-180)*porosity
sp_sch.df['sa3_mo3_volumematric_moisture']=( sp_sch.df['sa3_mo3']-180)/(380-180)*porosity
sp_sch.df['sa3_mo4_volumematric_moisture']=( sp_sch.df['sa3_mo4']-180)/(380-180)*porosity
sp_sch.df['sa3_mo5_volumematric_moisture']=( sp_sch.df['sa3_mo5']-180)/(380-180)*porosity

lw=4
ms=9
mew=4
grid_width=2
y_fontsize=14
sa3_time=[None]*len(file_name_sa3)
j=0
plt.ioff()
for idx in range(1,len(sp_sch.df),144):

    profile_sa1=np.array([sp_sch.df['sa1_mo2_volumematric_moisture'][idx],
            sp_sch.df['sa1_mo1_volumematric_moisture'][idx],
            sp_sch.df['sa1_mo3_volumematric_moisture'][idx],
            sp_sch.df['sa1_mo4_volumematric_moisture'][idx],
            sp_sch.df['sa1_mo5_volumematric_moisture'][idx]])
    profile_sa2=np.array([sp_sch.df['sa2_mo1_volumematric_moisture'][idx],
            sp_sch.df['sa2_mo2_volumematric_moisture'][idx],
            sp_sch.df['sa2_mo3_volumematric_moisture'][idx],
            sp_sch.df['sa2_mo4_volumematric_moisture'][idx],
            sp_sch.df['sa2_mo5_volumematric_moisture'][idx]])
    profile_sa3=np.array([sp_sch.df['sa3_mo1_volumematric_moisture'][idx],
            sp_sch.df['sa3_mo2_volumematric_moisture'][idx],
            sp_sch.df['sa3_mo3_volumematric_moisture'][idx],
            sp_sch.df['sa3_mo4_volumematric_moisture'][idx],
            sp_sch.df['sa3_mo5_volumematric_moisture'][idx]])
# for ii in file_name_sa2[:]: #[0:3]:

    print(str(j)+' of '+str(len(file_name)) )
    # im=image.imrd(ii) 

    # #im=np.rot90(im,-1)
    
    fig = plt.figure(figsize=(28,12))
    ax = [[] for i in range(8)]
    ax[0] = plt.subplot2grid((5, 8), (0, 0),colspan=3)
    ax[1] = plt.subplot2grid((5, 8), (1, 0),colspan=3)
    ax[2] = plt.subplot2grid((5, 8), (2, 0),colspan=3)
    ax[3] = plt.subplot2grid((5, 8), (3, 0),colspan=3)
    ax[4] = plt.subplot2grid((5, 8), (4, 0),colspan=3)
    ax[5] = plt.subplot2grid((5, 8), (0, 5),rowspan=4,colspan=1)
    ax[6] = plt.subplot2grid((5, 8), (0, 6),rowspan=4,colspan=1)
    ax[7] = plt.subplot2grid((5, 8), (0, 7),rowspan=4,colspan=1)


    # ax_area    = plt.subplot2grid((9, 7), (6,2),rowspan=3,colspan=1)
    # ax_img_sa3 = plt.subplot2grid((10, 13), (0,8),rowspan=6,colspan=5)
    # ax_img_sa2 = plt.subplot2grid((10, 13), (6,8),rowspan=6,colspan=5)
    
    fig.subplots_adjust(hspace=.20)
    fig.subplots_adjust(left=0.1, right=0.8, top=0.97, bottom=0.05)    
    
    # for i in ax:
    #   for axis in ['top','bottom','left','right']:
        # i.spines[axis].set_linewidth(2)
    
    ax[0].plot( sp_sch.df.index, sp_sch.df['pet_mmPday'],label='PET (mm)')
    ax[0].plot( sp_sch.df.index, sp_sch.df['pet_part1_mmPday'],'--',label='Solar (mm)')
    ax[0].plot( sp_sch.df.index, sp_sch.df['pet_part2_mmPday'],label='Wind (mm)')
    ax[0].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[0].set_xticklabels([])

    ax[1].plot( sp_sch.df.index, sp_sch.df['rainfall'])
    ax[1].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[1].set_xticklabels([])

    
    ax[2].plot( sp_sch.df.index, sp_sch.df['sa1_mo2_volumematric_moisture'],label='Mositure_content_Surface')
    ax[2].plot( sp_sch.df.index, sp_sch.df['sa1_mo1_volumematric_moisture'],label='Mositure_content_5cm_BGL')
    ax[2].plot( sp_sch.df.index, sp_sch.df['sa1_mo3_volumematric_moisture'],label='Mositure_content_10cm_BGL')
    ax[2].plot( sp_sch.df.index, sp_sch.df['sa1_mo4_volumematric_moisture'],label='Mositure_content_20cm_BGL')
    ax[2].plot( sp_sch.df.index, sp_sch.df['sa1_mo5_volumematric_moisture'],label='Mositure_content_50cm_BGL')
    ax[2].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[2].set_xticklabels([])
    
    ax[3].plot( sp_sch.df.index, sp_sch.df['sa2_mo1_volumematric_moisture'],label='Mositure_content_Surface')
    ax[3].plot( sp_sch.df.index, sp_sch.df['sa2_mo2_volumematric_moisture'],label='Mositure_content_5cm_BGL')
    ax[3].plot( sp_sch.df.index, sp_sch.df['sa2_mo3_volumematric_moisture'],label='Mositure_content_10cm_BGL')
    ax[3].plot( sp_sch.df.index, sp_sch.df['sa2_mo4_volumematric_moisture'],label='Mositure_content_20cm_BGL')
    ax[3].plot( sp_sch.df.index, sp_sch.df['sa2_mo5_volumematric_moisture'],label='Mositure_content_50cm_BGL')
    ax[3].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[3].set_xticklabels([])

    ax[4].plot( sp_sch.df.index, sp_sch.df['sa3_mo1_volumematric_moisture'],label='Mositure_content_Surface')
    ax[4].plot( sp_sch.df.index, sp_sch.df['sa3_mo2_volumematric_moisture'],label='Mositure_content_5cm_BGL')
    ax[4].plot( sp_sch.df.index, sp_sch.df['sa3_mo3_volumematric_moisture'],label='Mositure_content_10cm_BGL')
    ax[4].plot( sp_sch.df.index, sp_sch.df['sa3_mo4_volumematric_moisture'],label='Mositure_content_20cm_BGL')
    ax[4].plot( sp_sch.df.index, sp_sch.df['sa3_mo5_volumematric_moisture'],label='Mositure_content_50cm_BGL')
    ax[4].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    


    ax[5].plot(profile_sa1,[0,-0.05,-0.1,-0.2,-0.5],linewidth=grid_width+2)
    ax[5].set_xlim([0,.5])
    ax[5].set_xlabel('VOLUMETRIC \nMOISTURE \nCONTENT \nAT SA1 (-) ',fontsize=y_fontsize)
    ax[5].set_yticks([-0.5,-0.4,-0.3,-0.2,-0.1,0])
    ax[5].set_yticklabels(['0.5','0.4','0.3','0.2','0.1','0'],fontsize=y_fontsize)
    # ax[5].set_ylabel('Depth (m)',fontsize=y_fontsize)
    ax[5].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')

    ax[6].plot(profile_sa2,[0,-0.05,-0.1,-0.2,-0.5],linewidth=grid_width+2)
    ax[6].set_xlim([0,.5])
    ax[6].set_xlabel('VOLUMETRIC \nMOISTURE \nCONTENT \nAT SA2 (-)',fontsize=y_fontsize)
    ax[6].set_yticks([-0.5,-0.4,-0.3,-0.2,-0.1,0])
    ax[6].set_yticklabels(['0.5','0.4','0.3','0.2','0.1','0'],fontsize=y_fontsize)
    ax[6].set_ylabel('Depth (m)',fontsize=y_fontsize)
    ax[6].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    
    ax[7].plot(profile_sa3,[0,-0.05,-0.1,-0.2,-0.5],linewidth=grid_width+2)
    ax[7].set_xlim([0,.5])
    ax[7].set_xlabel('VOLUMETRIC \nMOISTURE \nCONTENT \nAT SA3 (-)',fontsize=y_fontsize)
    ax[7].set_yticks([-0.5,-0.4,-0.3,-0.2,-0.1,0])
    ax[7].set_yticklabels(['0.5','0.4','0.3','0.2','0.1','0'],fontsize=y_fontsize)
    # ax[7].set_ylabel('Depth (m)',fontsize=y_fontsize)
    ax[7].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[0].set_ylabel('POTENTIAL \nEVAPPORATION\nRATE\n(mm/Day)', fontsize=y_fontsize, labelpad=10)
    ax[1].set_ylabel('RAINFALL \n(mm)', fontsize=y_fontsize, labelpad=10)
    ax[2].set_ylabel('VOLUMETRIC \nWATER \nCONTENT AT \nSA1 (-)', fontsize=y_fontsize, labelpad=10)
    ax[3].set_ylabel('VOLUMETRIC \nWATER \nCONTENT AT \nSA2 (-)', fontsize=y_fontsize, labelpad=10)
    ax[4].set_ylabel('VOLUMETRIC \nWATER \nCONTENT AT \nSA3 (-)', fontsize=y_fontsize, labelpad=10)
    ax[5].set_ylabel('DEPTH (m)', fontsize=y_fontsize, labelpad=10)

    ax[4].set_xlabel('TIME', fontsize=y_fontsize, labelpad=10)
    # ax[0].set_xticks([])
    # ax[1].set_xticks([])
    # ax[2].set_xticks([])
    # ax[3].set_xticks([])
    ax[0].set_xlim([datetime.date(2021, 3, 16), datetime.date(2021, 12, 14)])
    ax[1].set_xlim([datetime.date(2021, 3, 16), datetime.date(2021, 12, 14)])
    ax[2].set_xlim([datetime.date(2021, 3, 16), datetime.date(2021, 12, 14)])
    ax[3].set_xlim([datetime.date(2021, 3, 16), datetime.date(2021, 12, 14)])
    ax[4].set_xlim([datetime.date(2021, 3, 16), datetime.date(2021, 12, 14)])
    ax[4].xaxis.set_major_formatter(mdates.DateFormatter('%b/%d'))

    ax[0].axvline(sp_sch.df.index[idx],color='r')
    ax[1].axvline(sp_sch.df.index[idx],color='r')
    ax[2].axvline(sp_sch.df.index[idx],color='r')
    ax[3].axvline(sp_sch.df.index[idx],color='r')
    ax[4].axvline(sp_sch.df.index[idx],color='r')
    
    ax[0].legend(bbox_to_anchor=(1., 1), loc='upper left', ncol=1,borderaxespad=0.,fontsize=y_fontsize)
    ax[2].legend(bbox_to_anchor=(1., 1), loc='upper left', ncol=1,borderaxespad=0.,fontsize=y_fontsize)
    ax[3].legend(bbox_to_anchor=(1., 1), loc='upper left',ncol=1, borderaxespad=0.,fontsize=y_fontsize)
    ax[4].legend(bbox_to_anchor=(1., 1), loc='upper left', ncol=1,borderaxespad=0.,fontsize=y_fontsize)
    plt.tight_layout()
    fig.savefig(f'{sp_sch.df.index[idx].strftime("%Y%m%d-%H%M%S")}.jpg', format='jpg', dpi=100)
    plt.close()
    j=j+1
img_array = []
for filename in sorted(glob.glob('C:\Project\MDBA\dashboard_evaporation\*.jpg')):    
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)


out = cv2.VideoWriter('video.avi',cv2.VideoWriter_fourcc(*'DIVX'), 15, size)
 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()
