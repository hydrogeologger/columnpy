# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 14:08:34 2021

@author: uqczhan2
"""

#G:\wille\Instrumentation\mdb\photo_sa3


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
#os.chdir("/home/chenming/Projects/tailings/area_51_redmud_4cm_photo/")
#img_list=glob.glob('/home/chenming/Projects/tailings/area_51_redmud_4cm_photo/*.jpg')
#for file in glob.glob("*.jpg"):
#    print(file)
sch_name='sa'
#path_im='/home/chenming/Projects/tailings/area_51_redmud_4cm_photo_'+sch_name+'/'
#import json
#inp_js = json.load(open('input/input.json'))

#path_im='/home/chenming/Projects/tailings/column_daisy/15/'
#path_im=str(tb_pandas.input_json['photo_path'])

path_im='c:\\Users\\uqczhan2\\Documents\\columnpy\\ewatering\\sa3_photo\\'
#import os
#for file in os.listdir("/home/chenming/Projects/tailings/area_51_redmud_4cm_photo/"):
#    if file.endswith(".jpg"):
#            print(os.path.join("/home/chenming/Projects/tailings/area_51_redmud_4cm_photo/", file))
#im=image.imread(img_list[0])

files = filter(os.path.isfile, glob.glob(path_im + "*.jpg"))
#files.sort(key=lambda x: os.path.getmtime(x))
paths = sorted(Path(path_im).iterdir(), key=os.path.getmtime)
file_name=[str(i).split('/')[-1] for i in paths]
path_im_sa2='c:\\Users\\uqczhan2\\Documents\\columnpy\\ewatering\\sa2_photo\\'
files_sa2 = filter(os.path.isfile, glob.glob(path_im_sa2 + "*.jpg"))
#files.sort(key=lambda x: os.path.getmtime(x))
paths_sa2 = sorted(Path(path_im_sa2).iterdir(), key=os.path.getmtime)
file_name_sa2=[str(i).split('/')[-1] for i in paths_sa2]
#file_name=[i.split('/')[-1] for i in files]

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
y_fontsize=17

j=0
for ii in file_name: #[0:3]:
    print(str(j)+' of '+str(len(file_name)) )
    im=image.imread(ii)   
    im_sa2=image.imread(file_name_sa2[j])
    im_time=get_date_taken(ii)
    #idx_im, min_value = min(enumerate( abs(sp_sch[sch_name].df['date_time']-im_time)), key=operator.itemgetter(1))
    #im=np.rot90(im,-1)

    fig = plt.figure(figsize=(28,12))
    ax = [[] for i in range(7)]
    ax[0] = plt.subplot2grid((7, 5), (0, 0), colspan=3)
    ax[1] = plt.subplot2grid((7, 5), (1, 0), colspan=3)
    ax[2] = plt.subplot2grid((7, 5), (2, 0), colspan=3)
    ax[3] = plt.subplot2grid((7, 5), (3, 0), colspan=3)
    ax[4] = plt.subplot2grid((7, 5), (4, 0), colspan=3)
    ax[5] = plt.subplot2grid((7, 5), (5, 0), colspan=3)
    ax[6] = plt.subplot2grid((7, 5), (6, 0), colspan=3)
    ax_img = plt.subplot2grid((8, 6), (0,4),rowspan=4,colspan=3)
    ax_img_sa2 = plt.subplot2grid((8, 6), (4,4),rowspan=4,colspan=3)
    
    fig.subplots_adjust(hspace=.20)
    fig.subplots_adjust(left=0.1, right=0.99, top=0.97, bottom=0.05)    

    for i in ax:
          for axis in ['top','bottom','left','right']:
            i.spines[axis].set_linewidth(2)

    ax[0].plot( sp_sch.df.index, sp_sch.df['pet_mmPday'])
    ax[0].vlines(im_time, -2, 50,  colors='red', linestyles='-', linewidth=2).set_zorder(10)

    ax[1].plot( sp_sch.df.index, sp_sch.df['pond_falling_rate_cs451_2_mmPday'])
    ax[1].plot( sp_sch.df.index, sp_sch.df['pond_falling_rate_cs451_3_mmPday'])
    ax[1].vlines(im_time, -100, 300,  colors='red', linestyles='-', linewidth=2).set_zorder(10)

    
    ax[2].plot( sp_sch.df.index, (sp_sch.df['p2_cs451']-0.34-0.2213+0.032) * constants.mmPm  )    
    ax[2].plot( sp_sch.df.index, (sp_sch.df['p3_cs451']-0.2213)* constants.mmPm    ) 
    ax[2].vlines(im_time, -1000, 3000,  colors='red', linestyles='-', linewidth=2).set_zorder(10)

    
    ax[3].plot( sp_sch.df.index, (sp_sch.df['sa1_p_kpa']-6.6  )*100,
        label='SA1' )    
    ax[3].plot( sp_sch.df.index, (sp_sch.df['sa2_p_kpa']-16.35)*100 ,
        label='SA2' )    
    ax[3].plot( sp_sch.df.index, (sp_sch.df['sa3_p_kpa']-9.85 )*100 ,
        label='SA3' )    
    ax[3].plot( sp_sch.df.index, (sp_sch.df['sa4_p_kpa']-33.40)*100 ,
        label='SA4' )         
    ax[3].vlines(im_time, -3000, 3000,  colors='red', linestyles='-', linewidth=2).set_zorder(10)

    ax[4].plot( tb_pandas.result_df['sa1_ec_piezo'].index, 
        tb_pandas.result_df['sa1_ec_piezo'].value,
        label='SA1' )      
    ax[4].plot( tb_pandas.result_df['sa2_ec_piezo'].index, 
        tb_pandas.result_df['sa2_ec_piezo'].value,
        label='SA2' )      
    ax[4].plot( tb_pandas.result_df['sa3_ec_piezo'].index, 
        tb_pandas.result_df['sa3_ec_piezo'].value,
        label='SA3' )      
    ax[4].plot( tb_pandas.result_df['sa4_ec_piezo'].index, 
        tb_pandas.result_df['sa4_ec_piezo'].value,
        label='SA4' )    
    ax[4].vlines(im_time, -50000, 50000,  colors='red', linestyles='-', linewidth=2).set_zorder(10)


    ax[5].plot( sp_sch.df.index, sp_sch.df['sa1_t_piezo'] -21.0-0.06,
        label='SA1' )             
    ax[5].plot( sp_sch.df.index, sp_sch.df['sa2_t_piezo'] -18.72-0.093 ,
        label='SA2' )          
    ax[5].plot( sp_sch.df.index, sp_sch.df['sa3_t_piezo'] - 22.64,
        label='SA3' )          
    ax[5].plot( sp_sch.df.index, sp_sch.df['sa4_t_piezo'] - 20.28,
        label='SA4' )  
    ax[5].vlines(im_time, -50000, 50000,  colors='red', linestyles='-', linewidth=2).set_zorder(10)
        
    
    ax[6].plot( sp_sch.df.index, sp_sch.df['sa2_t_5803'] ,
        label='2 m AGL' )         
    ax[6].plot( sp_sch.df.index, sp_sch.df['sa2_temp1'],
        label='Ground Level' )         
    ax[6].plot( sp_sch.df.index, sp_sch.df['sa2_temp2'],
        label='0.05 m BGL' )         
    ax[6].plot( sp_sch.df.index, sp_sch.df['sa2_temp3'],
        label='0.1 m BGL' )         
    ax[6].plot( sp_sch.df.index, sp_sch.df['sa2_temp4'],
        label='0.3 m BGL' )         
    ax[6].plot( sp_sch.df.index, sp_sch.df['sa2_temp5'],
        label='0.5 m BGL' )         
    ax[6].plot(sp_sch.df.index, sp_sch.df['sa2_t_piezo'],
        label='4.5 m BGL' )         
    ax[6].plot(sp_sch.df.index, sp_sch.df['t2_cs451']    )  
    ax[6].plot(sp_sch.df.index, sp_sch.df['t3_cs451'] )         
    ax[6].vlines(im_time, -50000, 50000,  colors='red', linestyles='-', linewidth=2).set_zorder(10)
    
    
    
    ax[1].set_ylim([-50,200])
    ax[5].set_ylim([-0.01,0.4])
    ax[6].set_ylim([10,40])
    
    
    ax[0].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[1].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[2].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[3].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[4].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[5].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[6].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    #ax[0].plot(ta['date_time'][::mkevy], ta['mmo0'][::mkevy], '-',color='maroon',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='1 cm',markevery=mkevy)
    ax_img.imshow(im)
    ax_img.axis('off')
    ax_img_sa2.imshow(im_sa2)
    ax_img_sa2.axis('off')
    ax[0].xaxis.set_major_formatter(mdates.DateFormatter('%b/%d'))
    ax[1].xaxis.set_major_formatter(mdates.DateFormatter('%b/%d'))
    ax[2].xaxis.set_major_formatter(mdates.DateFormatter('%b/%d'))
    ax[3].xaxis.set_major_formatter(mdates.DateFormatter('%b/%d'))
    ax[4].xaxis.set_major_formatter(mdates.DateFormatter('%b/%d'))
    ax[5].xaxis.set_major_formatter(mdates.DateFormatter('%b/%d'))
    ax[6].xaxis.set_major_formatter(mdates.DateFormatter('%b/%d'))
    ax[6].set_xlabel('DATE')

    
    

    ax[0].set_ylabel('POTENTIAL\nEVAP.\nRATE\n(mm/Day)', fontsize=y_fontsize, labelpad=10)
    ax[1].set_ylabel('SURFACE\nWATER\nRISING\nRATE\n(mm/Day)', fontsize=y_fontsize, labelpad=25)
    ax[2].set_ylabel('SURFACE\nWATER\nDEPTH\n(mm)', fontsize=y_fontsize, labelpad=5)
    ax[3].set_ylabel('GROUND\nWATER\nHEAD\nRISE\n(mm)', fontsize=y_fontsize, labelpad=13)
    ax[4].set_ylabel('GROUND\nWATER\n EC \n(microS/cm)', fontsize=y_fontsize, labelpad=15)
    ax[5].set_ylabel('GROUND\nWATER\nTEMP.\nRISE\n($^\circ$C)', fontsize=y_fontsize, labelpad=13)
    ax[6].set_ylabel('TEMPERATURE\nAT SA2\n($^\circ$C)', fontsize=y_fontsize, labelpad=13)

    ax[3].legend(bbox_to_anchor=(1.07, 0.5 ), loc='center', 
      borderaxespad=0.,fontsize=15,handletextpad=0.23,labelspacing=0.22,
      ncol=1,columnspacing=0.4)
    ax[4].legend(bbox_to_anchor=(1.07, 0.5 ), loc='center', 
      borderaxespad=0.,fontsize=15,handletextpad=0.23,labelspacing=0.22,
      ncol=1,columnspacing=0.4)    
    ax[5].legend(bbox_to_anchor=(1.07, 0.5 ), loc='center', 
      borderaxespad=0.,fontsize=15,handletextpad=0.23,labelspacing=0.22,
      ncol=1,columnspacing=0.4)    
    ax[6].legend(bbox_to_anchor=(1.10, 0.5 ), loc='center', 
      borderaxespad=0.,fontsize=15,handletextpad=0.23,labelspacing=0.22,
      ncol=1,columnspacing=0.4)    
    fig.savefig(ii.split('\\')[-1], format='jpg', dpi=100)
    j+=1
    
plt.show()