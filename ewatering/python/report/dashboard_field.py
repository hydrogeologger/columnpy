# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 14:08:34 2021

@author: uqczhan2
"""

#G:\wille\Instrumentation\mdb\photo_sa3
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
#os.chdir("/home/chenming/Projects/tailings/area_51_redmud_4cm_photo/")
#img_list=glob.glob('/home/chenming/Projects/tailings/area_51_redmud_4cm_photo/*.jpg')
#for file in glob.glob("*.jpg"):
#    print(file)
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
lw=4
ms=9
mew=4
grid_width=2
y_fontsize=16
# this script is used for calibrating load cells
import matplotlib.pylab as pylab
params = {'legend.fontsize': 11,
          'figure.figsize': (10, 5),
         'axes.labelsize': 12,
         'axes.titlesize':'18',
         'xtick.labelsize':'15',
         'ytick.labelsize':'15',
#         'ytick.labelweight':'bold',
          'axes.labelsize': 20,
           'axes.labelweight':'bold'}
#         'axes.grid':'linewidth=grid_width,color = '0.5''}
        
#'markers.size':ms,'markers.edgewidth':mew}
plt.rcParams["font.weight"] = "bold"
plt.rcParams["axes.labelweight"] = "bold"
pylab.rcParams.update(params)
#plt.rcParams['axes.labelsize'] = 16
#plt.rcParams['axes.labelweight'] = 'bold'


sa3_time=[None]*len(file_name_sa3)
j=0
for i in file_name_sa3:
    sa3_time[j]=get_date_taken(i)
    j=j+1
sa3_time=np.array(sa3_time)   
j=0
#ii=939 last time
interval=10
n=0


# #im=np.rot90(im,-1)

fig = plt.figure(figsize=(8,4))
ax = [[] for i in range(8)]
ax[0] = plt.subplot2grid((8,4), (0, 0), rowspan=2, colspan=2)
ax[1] = plt.subplot2grid((8,4), (2, 0), rowspan=2, colspan=2)
ax[2] = plt.subplot2grid((8,4), (4, 0), rowspan=2, colspan=2)
ax[3] = plt.subplot2grid((8,4), (6, 0), rowspan=2, colspan=2)
ax[4] = plt.subplot2grid((8,4), (0, 2), rowspan=2, colspan=2)
ax[5] = plt.subplot2grid((8,4), (2, 2), rowspan=2, colspan=2)
ax[6] = plt.subplot2grid((8,4), (4, 2), rowspan=2, colspan=2)
ax[7] = plt.subplot2grid((8,4), (6, 2), rowspan=2, colspan=2)





fig.subplots_adjust(hspace=.20)
fig.subplots_adjust(left=0.1, right=0.99, top=0.97, bottom=0.05)    

for i in ax:
  for axis in ['top','bottom','left','right']:
    i.spines[axis].set_linewidth(2)

ax[0].plot( sp_sch.df.index, sp_sch.df['pet_mmPday'],label='PET (mm)',linewidth=lw)
ax[0].plot( sp_sch.df.index, sp_sch.df['pet_part1_mmPday'],'--',label='Solar (mm)',linewidth=lw)
ax[0].plot( sp_sch.df.index, sp_sch.df['pet_part2_mmPday'],label='Wind (mm)',linewidth=lw)
# ax[0].xaxis.set_major_formatter(mdates.DateFormatter('%b/%d'))
ax[0].set_xticklabels([])
ax[1].plot( sp_sch.df.index, np.cumsum(sp_sch.df['rainfall']),linewidth=lw)
ax[1].set_xticklabels([])


# ax[1].vlines(im_time, -100, 300,  colors='red', linestyles='-', linewidth=2).set_zorder(10)
ax[2].set_xticklabels([])
ax[2].plot( sp_sch.df.index, sp_sch.df['recharge_mmPday_p3'],linewidth=lw)
# ax[2].plot( sp_sch.df.index, sp_sch.df['recharge_mmPday_p3'])
# ax[2].plot( sp_sch.df.index, sp_sch.df['pond_falling_rate_cs451_3_mmPday'])
# ax[2].vlines(im_time, -300, 700,  colors='red', linestyles='-', linewidth=2).set_zorder(10)
ax[2].set_xticklabels([])   

# ax[4].plot( sp_sch.df.index, (sp_sch.df['p2_cs451']-0.34-0.2213+0.032) * constants.mmPm, label='cs451 sensor 1')    
ax[3].plot( sp_sch.df.index, (sp_sch.df['p2_cs451']-SA2_water_depth_adjust)* constants.mmPm, label='cs451 sensor 2',linewidth=lw) 
# ax[3].vlines(im_time, -1000, 3000,  colors='red', linestyles='-', linewidth=2).set_zorder(10)
ax[3].set_xticklabels([])


ax[4].plot( sp_sch.df.index, (sp_sch.df['sa1_p_kpa']-6.6  )*100,
label='SA1',linewidth=lw)    
ax[4].plot( sp_sch.df.index, (sp_sch.df['sa2_p_kpa']-16.35)*100 ,
label='SA2',linewidth=lw)    
ax[4].plot( sp_sch.df.index, (sp_sch.df['sa3_p_kpa']-9.85 )*100 ,
label='SA3',linewidth=lw)    
ax[4].plot( sp_sch.df.index, (sp_sch.df['sa4_p_kpa']-33.40)*100 ,
label='SA4',linewidth=lw )         
# ax[4].vlines(im_time, -3000, 3000,  colors='red', linestyles='-', linewidth=2).set_zorder(10)
ax[4].set_xticklabels([])

ax[5].plot( sp_sch.df.index, 
sp_sch.df['sa1_ec_piezo'],
label='SA1',linewidth=lw )      
ax[5].plot( sp_sch.df.index,
sp_sch.df['sa2_ec_piezo'],
label='SA2',linewidth=lw)      
ax[5].plot( sp_sch.df.index,
sp_sch.df['sa3_ec_piezo'],
label='SA3',linewidth=lw)      
ax[5].plot( sp_sch.df.index,
sp_sch.df['sa4_ec_piezo'],
label='SA4',linewidth=lw)    
# ax[5].vlines(im_time, -50000, 60000,  colors='red', linestyles='-', linewidth=2).set_zorder(10)
   
ax[5].set_xticklabels([])


ax[6].plot( sp_sch.df.index, sp_sch.df['sa1_t_piezo'] -21.0-0.06,
label='SA1',linewidth=lw)             
ax[6].plot( sp_sch.df.index, sp_sch.df['sa2_t_piezo'] -18.72-0.093 ,
label='SA2',linewidth=lw)          
ax[6].plot( sp_sch.df.index, sp_sch.df['sa3_t_piezo'] - 22.64,
label='SA3',linewidth=lw)          
ax[6].plot( sp_sch.df.index, sp_sch.df['sa4_t_piezo'] - 20.28,
label='SA4',linewidth=lw)  
# ax[6].vlines(im_time, -50000, 50000,  colors='red', linestyles='-', linewidth=2).set_zorder(10)
ax[6].set_xticklabels([])
# ax[5].set_ylim([0,60000])    

ax[7].plot( sp_sch.df.index, sp_sch.df['sa2_t_5803'] ,
label='2 m AGL',linewidth=lw)         
ax[7].plot( sp_sch.df.index, sp_sch.df['sa2_temp1'],
label='Ground Level',linewidth=lw)         
ax[7].plot( sp_sch.df.index, sp_sch.df['sa2_temp2'],
label='0.05 m BGL',linewidth=lw)         
ax[7].plot( sp_sch.df.index, sp_sch.df['sa2_temp3'],
label='0.1 m BGL',linewidth=lw)         
ax[7].plot( sp_sch.df.index, sp_sch.df['sa2_temp4'],
label='0.3 m BGL',linewidth=lw)         
ax[7].plot( sp_sch.df.index, sp_sch.df['sa2_temp5'],
label='0.5 m BGL',linewidth=lw)         
ax[7].plot(sp_sch.df.index, sp_sch.df['sa2_t_piezo'],
label='4.5 m BGL',linewidth=lw)         
ax[7].plot(sp_sch.df.index, sp_sch.df['t2_cs451'],linewidth=lw)  
ax[7].plot(sp_sch.df.index, sp_sch.df['t3_cs451'],linewidth=lw)         
# ax[7].vlines(im_time, -50000, 50000,  colors='red', linestyles='-', linewidth=2).set_zorder(10)
# ax[7].set_xticklabels([])
ax[0].set_xlim([datetime.date(2021, 3, 16), datetime.date(2021, 12, 14)])
ax[1].set_xlim([datetime.date(2021, 3, 16), datetime.date(2021, 12, 14)])
ax[2].set_xlim([datetime.date(2021, 3, 16), datetime.date(2021, 12, 14)])
ax[3].set_xlim([datetime.date(2021, 3, 16), datetime.date(2021, 12, 14)])
ax[4].set_xlim([datetime.date(2021, 3, 16), datetime.date(2021, 12, 14)])
ax[5].set_xlim([datetime.date(2021, 3, 16), datetime.date(2021, 12, 14)])
ax[6].set_xlim([datetime.date(2021, 3, 16), datetime.date(2021, 12, 14)])
ax[7].set_xlim([datetime.date(2021, 3, 16), datetime.date(2021, 12, 14)])
ax[3].xaxis.set_major_formatter(mdates.DateFormatter('%b/%d'))
ax[7].xaxis.set_major_formatter(mdates.DateFormatter('%b/%d'))


# ax[0].xticklabels([])
# ax[1].xticklabels([])
# ax[2].xticklabels([])
# ax[3].xticklabels([])
# ax[4].xticklabels([])
# ax[5].xticklabels([])
# ax[6].xticklabels([])

ax[0].set_ylim([-3,18])
ax[2].set_ylim([-15,30])
ax[3].set_ylim([-50,1200])
ax[4].set_ylim([-1000,2500])
ax[5].set_ylim([0,60000])    
ax[6].set_ylim([-6,1])
ax[7].set_ylim([0,40])


ax[0].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
ax[1].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
ax[2].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
ax[3].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
ax[4].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
ax[5].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
ax[6].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
ax[7].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
#ax[0].plot(ta['date_time'][::mkevy], ta['mmo0'][::mkevy], '-',color='maroon',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='1 cm',markevery=mkevy)
# ax_img.imshow(im)
# ax_img.axis('off')


# ax[0].xaxis.set_major_formatter(mdates.DateFormatter('%b/%d'))
# ax[1].xaxis.set_major_formatter(mdates.DateFormatter('%b/%d'))
# ax[1].xaxis.set_major_formatter(mdates.DateFormatter('%b/%d'))
# ax[3].xaxis.set_major_formatter(mdates.DateFormatter('%b/%d'))
# ax[4].xaxis.set_major_formatter(mdates.DateFormatter('%b/%d'))
# ax[5].xaxis.set_major_formatter(mdates.DateFormatter('%b/%d'))
# ax[6].xaxis.set_major_formatter(mdates.DateFormatter('%b/%d'))
# ax[7].xaxis.set_major_formatter(mdates.DateFormatter('%b/%d'))
# ax[7].set_xlabel('DATE')

ax[0].set_ylabel('POTENTIAL \nEVAPPORATION\nRATE\n(mm/Day)', fontsize=y_fontsize, labelpad=10)
ax[1].set_ylabel('CUMU.\nRAINFALL \n(mm)', fontsize=y_fontsize, labelpad=25)
ax[2].set_ylabel('RECHARGE \nRATE\n(mm/Day)', fontsize=y_fontsize, labelpad=25)
ax[3].set_ylabel('SURFACE \nWATER\nDEPTH (mm)', fontsize=y_fontsize, labelpad=5)
ax[4].set_ylabel('GROUND. \nHEAD RISE \n(mm)', fontsize=y_fontsize, labelpad=13)
ax[5].set_ylabel('GROUND. \nEC \n(µS/cm)', fontsize=y_fontsize, labelpad=15)
ax[6].set_ylabel('GROUND. \nTEMP. \nRISE ($^\circ$C)', fontsize=y_fontsize, labelpad=13)
ax[7].set_ylabel('TEMP.\nAT SA2\n($^\circ$C)', fontsize=y_fontsize, labelpad=13)

ax[7].set_xlabel('Time', loc='center',fontsize=y_fontsize+4, labelpad=13)

ax[0].get_yaxis().set_label_coords(-0.06,0.5)
ax[1].get_yaxis().set_label_coords(-0.06,0.5)
ax[2].get_yaxis().set_label_coords(-0.06,0.5)
ax[3].get_yaxis().set_label_coords(-0.06,0.5)
ax[4].get_yaxis().set_label_coords(-0.075,0.5)
ax[5].get_yaxis().set_label_coords(-0.075,0.5)
ax[6].get_yaxis().set_label_coords(-0.07,0.5)
ax[7].get_yaxis().set_label_coords(-0.07,0.5)



ax[0].legend(loc='lower left', 
  borderaxespad=0.,fontsize=y_fontsize,handletextpad=0.23,labelspacing=0.22,
  ncol=1,columnspacing=0.4)
ax[4].legend(loc='lower left', 
  borderaxespad=0.,fontsize=y_fontsize,handletextpad=0.23,labelspacing=0.22,
  ncol=1,columnspacing=0.4)
ax[5].legend(loc='lower left', 
  borderaxespad=0.,fontsize=y_fontsize,handletextpad=0.23,labelspacing=0.22,
  ncol=1,columnspacing=0.4)
ax[6].legend(loc='lower left',  
  borderaxespad=0.,fontsize=y_fontsize,handletextpad=0.23,labelspacing=0.22,
  ncol=1,columnspacing=0.4)    
ax[7].legend(loc='lower left', 
  borderaxespad=0.,fontsize=y_fontsize,handletextpad=0.23,labelspacing=0.22,
  ncol=1,columnspacing=0.4)    
# ax[0].legend(bbox_to_anchor=(1.08, 0.5 ), loc='center', 
#   borderaxespad=0.,fontsize=y_fontsize,handletextpad=0.23,labelspacing=0.22,
#   ncol=1,columnspacing=0.4)
# ax[4].legend(bbox_to_anchor=(1.10, 0.5 ), loc='center', 
#   borderaxespad=0.,fontsize=y_fontsize,handletextpad=0.23,labelspacing=0.22,
#   ncol=1,columnspacing=0.4)
# ax[5].legend(bbox_to_anchor=(1.08, 0.5 ), loc='center', 
#   borderaxespad=0.,fontsize=y_fontsize,handletextpad=0.23,labelspacing=0.22,
#   ncol=1,columnspacing=0.4)
# ax[6].legend(bbox_to_anchor=(1.08, 0.5 ), loc='center', 
#   borderaxespad=0.,fontsize=y_fontsize,handletextpad=0.23,labelspacing=0.22,
#   ncol=1,columnspacing=0.4)    
# ax[7].legend(bbox_to_anchor=(1.08, 0.5 ), loc='center', 
#   borderaxespad=0.,fontsize=y_fontsize,handletextpad=0.23,labelspacing=0.22,
#   ncol=1,columnspacing=0.4)    

fig.align_labels()
plt.rcParams['xtick.labelsize'] = y_fontsize
plt.rcParams['ytick.labelsize'] = y_fontsize
plt.rcParams['lines.linewidth'] = lw*2
plt.rcParams['axes.linewidth'] = lw+4

plt.tight_layout(pad=0.03)    
# plt.close()
# plt.show()
# img_array = []
# # for filename in glob.glob('C:/Project/MBDA/large/*.png'):
# for filename in glob.glob('C:\Project\MDBA\dashboard\\*.jpg'):    
#         img = cv2.imread(filename)
#         height, width, layers = img.shape
#         size = (width,height)
#         img_array.append(img)


# out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'), 15, size)
 
# for i in range(len(img_array)):
#     out.write(img_array[i])
# out.release()
