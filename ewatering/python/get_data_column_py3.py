# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 21:27:40 2021

@author: s4680073
"""
import operator
import py_compile
import os
import sys
import json
import pandas as pd
import numpy as np
import datetime
import matplotlib.image as image
from PIL import Image
import cv2
import matplotlib as mpl
from pathlib import Path
import matplotlib
import matplotlib.dates as mdates
import matplotlib.animation as animation
def get_date_taken(path):
    from datetime import datetime
    return datetime.strptime(Image.open(path)._getexif()[36867],'%Y:%m:%d %H:%M:%S')
import glob, os
import scipy.stats as st
import seaborn as sns

#matplotlib.use('Agg')
# %matplotlib qt  # run this 

import matplotlib.pyplot as plt
# plt.ioff()  # disable poping out figure automatically
# # recompile post_processing in case update are required
# pyduino_path = os.environ['pyduino']
# print(os.environ['pyduino'])
# sys.path.append(os.path.join(pyduino_path,'python','post_processing'))
# py_compile.compile(
#     os.path.join(pyduino_path,'python','post_processing',
#                  'thingsboard_to_pandas_py3.py'))
import thingsboard_to_pandas_py3
#reload(thingsboard_to_pandas_py3)
fontsize_label=20
porosity=0.4
line_width=2
tb_pandas=thingsboard_to_pandas_py3.tingsboard_to_pandas('C:/pyduino/pyduino/python/tb_to_csv/tb_credential_column.json')
# tb_pandas=thingsboard_to_pandas_py3.tingsboard_to_pandas('C:/pyduino/pyduino/python/tb_to_csv/tb_credential_column_phase2.json')

# input is the location of the json file
# use the below command to show the comments on tb_credential.json
# print tb_pandas.input_json['comments'] 




tb_pandas.get_token()    # get the token associated with the account
tb_pandas.get_keys()     # list of keys in the device
tb_pandas.get_data()     # obtain data from thingsboard stored at tb_pandas['results']
tb_pandas.convert_data_to_df()  # convert each datasets to pandas dataframe



#'ec1,ec2,ec3,ec4,ec5,ec6,ec_piezo1,p1_cs451,p2_cs451,p3_cs451,p_5802,p_5802_2,p_piezo1,rainfall,raw2,raw3,raw4,raw5,raw6,rh_logger,sa1_ec1,sa1_ec2,sa1_ec3,sa1_ec4,sa1_ec5,sa1_ec_piezo,sa1_ir,sa1_p_5802,sa1_p_5803,sa1_p_piezo,sa1_raw1,sa1_raw2,sa1_raw3,sa1_raw4,sa1_raw5,sa1_rh_logger,sa1_sht31_humidity_1,sa1_sht31_temp_1,sa1_t_5802,sa1_t_5803,sa1_t_piezo,sa1_temp1,sa1_temp2,sa1_temp3,sa1_temp4,sa1_temp5,sa1_temp_logger,sa1_uv,sa1_vis,sa1_volt,sa2_ec1,sa2_ec2,sa2_ec3,sa2_ec4,sa2_ec5,sa2_ec_piezo,sa2_ir,sa2_p_5803,sa2_p_piezo,sa2_raw1,sa2_raw2,sa2_raw3,sa2_raw4,sa2_raw5,sa2_rh_logger,sa2_t_5803,sa2_t_piezo,sa2_temp1,sa2_temp2,sa2_temp3,sa2_temp4,sa2_temp5,sa2_temp_logger,sa2_uv,sa2_vis,sa2_volt,sa3_ec_piezo,sa3_ir,sa3_mo1,sa3_mo2,sa3_mo3,sa3_mo4,sa3_mo5,sa3_p_5803,sa3_p_piezo,sa3_rh_logger,sa3_t_5803,sa3_t_piezo,sa3_temp_logger,sa3_uv,sa3_vis,sa3_volt,sa4_ec_piezo,sa4_p_piezo,sa4_t_piezo,sht31_humidity_1,sht31_temp_1,t1_cs451,t2_cs451,t3_cs451,t_5802,t_5802_2,t_piezo1,temp2,temp3,temp4,temp5,temp6,temp_logger,volt,wind_direction,wind_speed'

## check the length of each pandas
#for i in list(tb_pandas.result_df):
#    print( i +' ' + str(len(   tb_pandas.result_df[i]   ))     )
#    print( i + len(i)     )


#tb_pandas.plot_df(['sa3_uv','sa3_vis'])

# small optation to the failed measurement

#tb_pandas.result_df['temp_2']['value'] [ tb_pandas.result_df['temp_2']['value'] <5  ] =np.nan 

#tb_pandas.result_df['scale1']['value'] [ tb_pandas.result_df['scale1']['value'] <5  ] =np.nan 

# merge data    
# with open('C:/pyduino/pyduino/python/tb_to_csv/schedule_column_phase2.json') as data_file:    
#     sp_input = json.load(data_file)
with open('C:/pyduino/pyduino/python/tb_to_csv/schedule_column.json') as data_file:    
    sp_input = json.load(data_file)

#sys.path.append   (os.environ['pyduino']+'/python/post_processing/')
#py_compile.compile(os.environ['pyduino']+'/python/post_processing/pandas_scale.py')
#py_compile.compile(os.environ['pyduino']+'/python/post_processing/constants.py')
#
#
#sys.path.join(os.environ['pyduino'],'python','post_processing')
#sys.path.append(os.path.join(os.environ['pyduino'],'python','post_processing'))
# py_compile.compile( os.path.join(
#         os.environ['pyduino'],'python','post_processing','pandas_scale.py')  )
# py_compile.compile( os.path.join(
#         os.environ['pyduino'],'python','post_processing','constants.py')  )

import pandas_scale_py3 as pandas_scale
import constants

# open_day='2020-03-15'
# close_day='2020-06-6'
# tb_pandas.result_df['2020-03-16':'2020-06-6']>=open_day
# con2=tb_pandas.result_df[sp_input['start_time']]<close_day
# tb_pandas.result_df=order_data[con1&con2]

sp_sch={}
plot_interpolate=False
# plot_interpolate=True

sp_sch=pandas_scale.concat_data_tb(
    pd.datetime.strptime(sp_input['start_time'],'%Y/%b/%d %H:%M'),
    pd.datetime.strptime(sp_input['end_time'],'%Y/%b/%d %H:%M'),
    sp_input['delta_t_s'] );

sp_sch.start_dt = pd.datetime.strptime(sp_input['start_time'],'%Y/%b/%d %H:%M')
sp_sch.end_dt   = pd.datetime.strptime(sp_input['end_time'  ],'%Y/%b/%d %H:%M')

# managing data
tb_pandas.result_df['column_mo1']['value'] \
    [ tb_pandas.result_df['column_mo1']['value'] >500 ] =np.nan 
tb_pandas.result_df['column_mo2']['value'] \
    [ tb_pandas.result_df['column_mo2']['value'] >500 ] =np.nan 
tb_pandas.result_df['column_mo3']['value'] \
    [ tb_pandas.result_df['column_mo3']['value'] >500 ] =np.nan 
tb_pandas.result_df['column_mo4']['value'] \
    [ tb_pandas.result_df['column_mo4']['value'] >500 ] =np.nan 
tb_pandas.result_df['column_mo5']['value'] \
    [ tb_pandas.result_df['column_mo5']['value'] >500 ] =np.nan 
mask = np.where(
        np.abs(np.diff(tb_pandas.result_df['column_mo5']['value']))>0.5)[0]
tb_pandas.result_df['column_mo5']['value'] [mask]=np.nan 
mask = np.where(
        np.abs(np.diff(tb_pandas.result_df['scale']['value']))>0.5)[0]
tb_pandas.result_df['scale']['value'] [mask]=np.nan 
sp_sch.merge_data_from_tb(
        input_time_series=tb_pandas.result_df['column_mo1'].index, 
        input_data_series=tb_pandas.result_df['column_mo1']['value'], 
        output_time_series=sp_sch.df.index,key_name='column_mo1' ,
        plot=plot_interpolate  ,coef=5e-16,rm_nan=True)
sp_sch.merge_data_from_tb(
        input_time_series=tb_pandas.result_df['column_mo2'].index, 
        input_data_series=tb_pandas.result_df['column_mo2']['value'], 
        output_time_series=sp_sch.df.index,key_name='column_mo2' ,
        plot=plot_interpolate  ,coef=5e-16,rm_nan=True)
sp_sch.merge_data_from_tb(
        input_time_series=tb_pandas.result_df['column_mo3'].index, 
        input_data_series=tb_pandas.result_df['column_mo3']['value'], 
        output_time_series=sp_sch.df.index,key_name='column_mo3' ,
        plot=plot_interpolate  ,coef=5e-16,rm_nan=True)
sp_sch.merge_data_from_tb(
        input_time_series=tb_pandas.result_df['column_mo4'].index, 
        input_data_series=tb_pandas.result_df['column_mo4']['value'], 
        output_time_series=sp_sch.df.index,key_name='column_mo4' ,
        plot=plot_interpolate  ,coef=5e-16,rm_nan=True)
sp_sch.merge_data_from_tb(
        input_time_series=tb_pandas.result_df['column_mo5'].index, 
        input_data_series=tb_pandas.result_df['column_mo5']['value'], 
        output_time_series=sp_sch.df.index,key_name='column_mo5' ,
        plot=plot_interpolate  ,coef=5e-16,rm_nan=True)
tb_pandas.result_df['scale'][tb_pandas.result_df['scale']<=2000]=np.nan
sp_sch.merge_data_from_tb(
        input_time_series=tb_pandas.result_df['scale'].index, 
        input_data_series=tb_pandas.result_df['scale']['value'], 
        output_time_series=sp_sch.df.index,key_name='scale' ,
        plot=plot_interpolate  ,coef=5e-20,rm_nan=True)
sp_sch.df['column_mo3'].loc['2021-08-21':'2021-08-22']=282
sp_sch.df['column_mo4'].loc['2021-08-21':'2021-08-22']=435
sp_sch.df['scale'].loc['2021-03-15':'2021-05-11 13']=np.nan
# sp_sch.df['scale'].loc['2021-05-31 12:30':'2021-06-03 14:00']=sp_sch.df['scale'].loc['2021-05-31 12:30':'2021-06-03 14:00']-15
# sp_sch.df['scale'].loc['2021-06-03 13:00':'2021-06-08 7:00']=sp_sch.df['scale'].loc['2021-06-03 13:00':'2021-06-08 07:00']-10
sp_sch.df['column_mo1'].loc['2021-07-09 12':'2021-07-09 21']=267
sp_sch.df['column_mo2'].loc['2021-07-09 12':'2021-07-09 21']=260
sp_sch.df['column_mo3'].loc['2021-07-09 12':'2021-07-09 21']=318
sp_sch.df['column_mo4'].loc['2021-07-09 12':'2021-07-09 21']=439
sp_sch.df['column_mo5'].loc['2021-07-09 12':'2021-07-09 21']=398

sp_sch.df['column_mo3'].loc['2021-08-21':'2021-08-22']=282
sp_sch.df['column_mo3'].loc['2021-08-21':'2021-08-22']=282
sp_sch.df['column_mo3'].loc['2021-08-21':'2021-08-22']=282
sp_sch.df['column_mo3'].loc['2021-08-21':'2021-08-22']=282
# sp_sch.df['scale'].loc['2021-06-03 13:00':'2021-06-03 13:00']=np.nan
sp_sch.df['scale_decreasing_rate_mmPday'] = \
    constants.m2mm*constants.sPday*constants.kgPg*np.append(np.diff(sp_sch.df['scale']), np.nan) \
    / sp_input['delta_t_s']/(np.pi*0.1**2)/1000
# sp_sch.df['scale_decreasing_rate_gPday'].loc[np.abs(sp_sch.df['scale_decreasing_rate_gPday'])>1000]=np.nan
sp_sch.df['scale_decreasing_rate_mmPday'].loc[np.abs(sp_sch.df['scale_decreasing_rate_mmPday'])>10]=np.nan

# sp_sch.df['column_mo1_volumematric_moisture']=( 521-sp_sch.df['column_mo1'])/(521-267)*porosity
sp_sch.df['column_mo1_volumematric_moisture']=( 493-sp_sch.df['column_mo1'])/(493-267)*porosity
sp_sch.df['column_mo2_volumematric_moisture']=( 403-sp_sch.df['column_mo2'])/(403-259)*porosity
sp_sch.df['column_mo3_volumematric_moisture']=( 410-sp_sch.df['column_mo3'])/(410-269)*porosity
sp_sch.df['column_mo4_volumematric_moisture']=( 450-sp_sch.df['column_mo4'])/(450-269)*porosity
sp_sch.df['column_mo5_volumematric_moisture']=( 410-sp_sch.df['column_mo5'])/(410-269)*porosity
sp_sch_new1=sp_sch.df.loc['2021-07-31 15:00':'2021-08-1 08:30']
sp_sch_new2=sp_sch.df.loc['2021-08-20 13:30':]
sp_sch_phase2=sp_sch_new1.append(sp_sch_new2)
#wetting process
##Calculate the infiltration and water loss of the large column
#wetting process
# porosity=0.4
# #wetting process
# column_mo0_volumematric_moisture_wet=0.4
# part1_wet_m=(column_mo0_volumematric_moisture_wet+sp_sch.df['column_mo2_volumematric_moisture'])/2*0.1
# part2_wet_m=(sp_sch.df['column_mo1_volumematric_moisture']+sp_sch.df['column_mo2_volumematric_moisture'])/2*0.1
# part3_wet_m=(sp_sch.df['column_mo2_volumematric_moisture']+sp_sch.df['column_mo3_volumematric_moisture'])/2*0.1
# totalwater_infiltration_m=(part1_wet+part2_wet+part3_wet)
# totalwater_infiltration_gram=totalwater_infiltration_m*(np.pi*0.1**2)*1000*constants.kg2g

# infiltration_rate_mmPday=constants.mmPm*(np.diff(totalwater_infiltration_m)/sp_input['delta_t_s'])/constants.dayPs
# infiltration_rate_mmPday[np.abs(infiltration_rate_mmPday)>20]=np.nan
# plt.plot(sp_sch.df.index[1:],infiltration_rate_mmPday)
# plt.xlabel('Time')
# plt.ylabel('Infiltration rate (mm)')

# #drying process
# column_mo0_volumematric_moisture_dry=0
# part1_dry=(column_mo0_volumematric_moisture_dry+sp_sch.df['column_mo2_volumematric_moisture'])/2*0.1
# part2_dry=(sp_sch.df['column_mo1_volumematric_moisture']+sp_sch.df['column_mo2_volumematric_moisture'])/2*0.1
# part3_dry=(sp_sch.df['column_mo2_volumematric_moisture']+sp_sch.df['column_mo3_volumematric_moisture'])/2*0.1
# totalwater_evp_m=(part1_dry+part2_dry+part3_dry)
# evp_rate_mmPday=constants.mmPm*(np.diff(totalwater_evp_m)/sp_input['delta_t_s'])/constants.dayPs
# evp_rate_mmPday[np.abs(evp_rate_mmPday)>5]=np.nan
# plt.plot(sp_sch.df.index[1:],-evp_rate_mmPday)
# plt.xlabel('Time')
# plt.ylabel('Evaporation rate (mm)')


# plt.plot(sp_sch.df['scale'])
# fig, ax = plt.subplots(figsize=[30,9])
# plt.setp(ax.spines.values(), linewidth=2)
# ax.plot(sp_sch.df['column_mo1_volumematric_moisture'],label='10cm below surface')
# ax.plot(sp_sch.df['column_mo2_volumematric_moisture'],label='20cm below surface')
# ax.plot(sp_sch.df['column_mo3_volumematric_moisture'],label='30cm below surface')
# ax.plot(sp_sch.df['column_mo4_volumematric_moisture'],label='50cm below surface')
# ax.plot(sp_sch.df['column_mo5_volumematric_moisture'],label='70cm below surface')
# ax.legend(loc=[0.79,0.5],fontsize=26)
# ax.set_xlabel('Time',weight='bold',fontsize=35)
# ax.set_ylabel('Volumetric water content (-)',weight='bold',fontsize=35)
# ax.xaxis.set_major_formatter(mdates.DateFormatter('%b/%d'))
# ax.set_xlim(datetime.date(2021, 4, 24), datetime.date(2021, 6, 5))
# plt.xticks(fontsize=28, rotation=0)
# plt.yticks(fontsize=28, rotation=0)
# plt.grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
# plt.savefig('Column_moisture_sensor.png',dpi=300,bbox_inches = 'tight',
#     pad_inches = 0)
sp_sch.df['infiltrated_water_bottle']=sp_sch.df['scale'].loc['2021-05-12 8:30']-sp_sch.df['scale']
#create dashboard
path_im='C:\Project\MDBA\data_deliverable\photos\column-daily\cut'
files = filter(os.path.isfile, glob.glob(path_im + "*.jpg"))
paths = sorted(Path(path_im).iterdir(), key=os.path.getmtime)
file_name=[str(i).split('/')[-1] for i in paths]
# y_fontsize=18
y_fontsize=24
plt.ioff()
j=0
# cross0=np.array([sp_sch.df['column_mo1_volumematric_moisture'][0],
#         sp_sch.df['column_mo2_volumematric_moisture'][0],
#         sp_sch.df['column_mo3_volumematric_moisture'][0],
#         sp_sch.df['column_mo4_volumematric_moisture'][0],
#         sp_sch.df['column_mo5_volumematric_moisture'][0]])
# sensor_distance=[0.1 0.1 0.2 0.2]
# for i in range(1,len(sp_sch.df),100):
totaltime=sp_sch.df.index-sp_sch.df.index[0]
totaltime_seconds=totaltime.total_seconds()
# for ii in file_name[:]: 
#     im_column=image.imread(file_name[j])
#     im_time=get_date_taken(ii)
#     idx, min_value = min(enumerate( abs(sp_sch.df.index-im_time)), key=operator.itemgetter(1))
#     cross=np.array([sp_sch.df['column_mo1_volumematric_moisture'][idx],
#             sp_sch.df['column_mo2_volumematric_moisture'][idx],
#             sp_sch.df['column_mo3_volumematric_moisture'][idx],
#             sp_sch.df['column_mo4_volumematric_moisture'][idx],
#             sp_sch.df['column_mo5_volumematric_moisture'][idx]])
#     # cross_water_content_diff=cross-cross0
#     # np.diff()
#     fig = plt.figure(figsize=(28,12),linewidth=3)
#     ax = [[] for i in range(9)]
#     ax[0] = plt.subplot2grid((6, 6), (2, 0), colspan=1,rowspan=6)
#     ax[1] = plt.subplot2grid((6, 6), (0, 1), colspan=1,rowspan=6)
#     ax[2] = plt.subplot2grid((6, 6), (0, 2), colspan=4,rowspan=2)
#     ax[3] = plt.subplot2grid((6, 6), (2, 2), colspan=4,rowspan=2)
#     ax[4] = plt.subplot2grid((6, 6), (4, 2), colspan=4,rowspan=2)
    
#     ax[0].imshow(im_column)
#     ax[0].axis('off')
#     fig.text(0.01,0.68,f'{im_time}',fontsize=y_fontsize,color='k')

#     ax[1].plot(cross,[-0.1,-0.2,-0.3,-0.5,-0.7],linewidth=grid_width+2)
#     ax[1].set_xlim([0,.5])
#     ax[1].set_xlabel('Volumetric water content (-)',fontsize=y_fontsize)
#     ax[1].set_yticks([-0.7,-0.6,-0.5,-0.4,-0.3,-0.2,-0.1,0])
#     ax[1].set_yticklabels(['0.7','0.6','0.5','0.4','0.3','0.2','0.1','0'],fontsize=y_fontsize)
#     ax[1].set_ylabel('Depth (m)',fontsize=y_fontsize)
#     ax[1].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
#     ax[2].plot(sp_sch.df['infiltrated_water_bottle'][0:idx],linewidth=grid_width+2,label='Infiltration from Mariotte Bottle')
#     ax[2].plot(totalwater_infiltration_gram[0:idx],linewidth=grid_width+2,label='Infiltration  from Moisture sensors')
#     ax[2].set_ylabel('Mass (g)',fontsize=y_fontsize)    
#     ax[2].set_xlim([datetime.date(2021, 4, 29), datetime.date(2021, 7, 27)])
#     ax[2].set_ylim([0,5000])
#     # ax[2].set_yticks([0, 50,100, 150, 200 ,250])
#     # ax[2].set_yticklabels(['0','50','100','150','200','250'],fontsize=y_fontsize)
#     ax[2].legend(loc='upper left',fontsize=y_fontsize)
#     ax[2].set_xticklabels([])
#     ax[2].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    
#     ax[3].plot(-sp_sch.df['scale_decreasing_rate_mmPday'][0:idx],linewidth=grid_width+2,label='Water loss from Mariobtte bottle')
#     ax[3].plot(sp_sch.df.index[1:idx],infiltration_rate_mmPday[0:idx-1],linewidth=grid_width+2,label='Infiltration rate from Moisture sensors')

#     ax[3].set_ylabel('Rate (mm/day)',fontsize=y_fontsize)    
#     ax[3].set_xlim([datetime.date(2021, 4, 29), datetime.date(2021, 7, 27)])
#     ax[3].set_ylim([0,2])
#     ax[3].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
#     ax[3].legend(loc='upper left',fontsize=y_fontsize)
#     ax[3].set_xticklabels([])
#     # plt.setp(ax.spines.values(), linewidth=2)
    
#     ax[4].plot(sp_sch.df['column_mo1_volumematric_moisture'][0:idx],label='10cm below surface',linewidth=grid_width+2)
#     ax[4].plot(sp_sch.df['column_mo2_volumematric_moisture'][0:idx],label='20cm below surface',linewidth=grid_width+2)
#     ax[4].plot(sp_sch.df['column_mo3_volumematric_moisture'][0:idx],label='30cm below surface',linewidth=grid_width+2)
#     ax[4].plot(sp_sch.df['column_mo4_volumematric_moisture'][0:idx],label='50cm below surface',linewidth=grid_width+2)
#     ax[4].plot(sp_sch.df['column_mo5_volumematric_moisture'][0:idx],label='70cm below surface',linewidth=grid_width+2)
#     ax[4].legend(loc='upper right',fontsize=y_fontsize)
#     ax[4].set_xlim([datetime.date(2021, 4, 29), datetime.date(2021, 7, 27)])
#     ax[4].set_xlabel('Time',fontsize=y_fontsize)
#     ax[4].set_ylim([0,0.5])
#     ax[4].set_ylabel('Volumetric water \ncontent (-)',fontsize=y_fontsize)
#     ax[4].xaxis.set_major_formatter(mdates.DateFormatter('%b/%d'))
#     ax[4].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
#     ax[1].tick_params(axis='both', which='minor', labelsize=y_fontsize) 
#     ax[2].tick_params(axis='both', which='minor', labelsize=y_fontsize) 
#     ax[3].tick_params(axis='both', which='minor', labelsize=y_fontsize) 
#     ax[4].tick_params(axis='both', which='minor', labelsize=y_fontsize) 
#     mpl.rcParams['xtick.labelsize'] = y_fontsize
#     mpl.rcParams['xtick.labelsize'] = y_fontsize
#     # plt.rcParams['ytick.labelsize'] = y_fontsize-1
#     plt.tight_layout()
#     print(j)
#     print(idx)
#     fig.savefig(ii.split('\\')[-1], format='jpg', dpi=100)
#     plt.close()
#     j=j+1
    
# img_array = []
# for filename in glob.glob('C:\Project\MDBA\column_dashboard\\*.jpg'):        
#     img = cv2.imread(filename)
#     height, width, layers = img.shape
#     size = (width,height)
#     img_array.append(img)


# out = cv2.VideoWriter('project.mp4',cv2.VideoWriter_fourcc(*'DIVX'), 3, size)
 
# for i in range(len(img_array)):
#     out.write(img_array[i])
# out.release()    

# # sp_sch_30min=sp_sch.df.resample('30T').ffill()

# # # sp_sch_30min['column_mo1_volumematric_moisture']=( 523-sp_sch_30min['column_mo1'])/(523-269)*porosity
# # # sp_sch_30min['column_mo2_volumematric_moisture']=( 523-sp_sch_30min['column_mo2'])/(523-269)*porosity
# # # sp_sch_30min['column_mo3_volumematric_moisture']=( 523-sp_sch_30min['column_mo3'])/(523-269)*porosity
# # # sp_sch_30min['column_mo4_volumematric_moisture']=( 523-sp_sch_30min['column_mo4'])/(523-269)*porosity
# # # sp_sch_30min['column_mo5_volumematric_moisture']=( 523-sp_sch_30min['column_mo5'])/(523-269)*porosity
# # # ax.xaxis.set_major_formatter(mdates.DateFormatter('%b/%d'))
# # # ax.legend(loc='upper right')
# # # ax.set_xlim([datetime.date(2021, 4, 24), datetime.date(2021, 6, 5)])
# # # ax.set_xlabel('Time',weight='bold',fontsize=fontsize_label)
# # # ax.set_ylabel('Moisture sensor reading',weight='bold',fontsize=fontsize_label)
# # # plt.savefig('Column_moisture sensor.png',dpi=300)
# # # fig, ax = plt.subplots(figsize=[16,9])
# # # ax.plot(sp_sch.df['scale'],label='Mass of Mariotte bottle')
# # # ax.set_xlim([datetime.date(2021, 5, 12), datetime.date(2021, 6, 5)])
# # # ax.set_ylim(6000,10000)

# # # plot
# ax=plt.plot(sp_sch.df.index,sp_sch.df['column_mo1_volumematric_moisture'],label='10cm below surface',linewidth=line_width)
# ax=plt.plot(sp_sch.df['column_mo2_volumematric_moisture'],label='20cm below surface',linewidth=line_width)
# ax=plt.plot(sp_sch.df['column_mo3_volumematric_moisture'],label='30cm below surface',linewidth=line_width)
# ax=plt.plot(sp_sch.df['column_mo4_volumematric_moisture'],label='50cm below surface',linewidth=line_width)
# ax=plt.plot(sp_sch.df['column_mo5_volumematric_moisture'],label='70cm below surface',linewidth=line_width)
# ax.xaxis.set_major_formatter(mdates.DateFormatter('%b/%d'))