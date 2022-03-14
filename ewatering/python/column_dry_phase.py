# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 08:57:49 2021

@author: s4680073
"""

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
from datetime import datetime
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
import pandas_scale_py3 as pandas_scale
import constants
import matplotlib.pyplot as plt
import thingsboard_to_pandas_py3
#reload(thingsboard_to_pandas_py3)
fontsize_label=20
porosity=0.5
column_radius_m=0.05

exec(open('C:\columnpy\columnpy\ewatering\python\\adjust_value.py').read())
exec(open('C:\columnpy\columnpy\ewatering\python\get_data_py3_sep_2021_jan_2022.py').read())
# sp_sch.df=sp_sch.df.astype(np.float32)
exec(open('C:\columnpy\columnpy\ewatering\python\calc_area.py').read())
exec(open('C:\columnpy\columnpy\ewatering\python\calc_evap.py').read())
exec(open('C:\columnpy\columnpy\ewatering\python\\read_pump_meter.py').read())
sp_sch_field=sp_sch
del sp_sch
# tb_pandas=thingsboard_to_pandas_py3.tingsboard_to_pandas('C:/pyduino/pyduino/python/tb_to_csv/tb_credential_column.json')

# sp_sch_field.df.loc['2021-12-31':'2022-1-5']=np.nan
sp_sch_field.df['sa2_mo1_volumematric_moisture']=( sp_sch_field.df['sa2_mo1']-1900)/(3083-1900)*porosity
sp_sch_field.df['sa2_mo2_volumematric_moisture']=( sp_sch_field.df['sa2_mo2']-1900)/(3083-1900)*porosity
sp_sch_field.df['sa2_mo3_volumematric_moisture']=( sp_sch_field.df['sa2_mo3']-1900)/(3083-1900)*porosity
sp_sch_field.df['sa2_mo4_volumematric_moisture']=( sp_sch_field.df['sa2_mo4']-1900)/(3083-1900)*porosity
sp_sch_field.df['sa2_mo5_volumematric_moisture']=( sp_sch_field.df['sa2_mo5']-1900)/(3083-1900)*porosity

sp_sch_field.df['sa3_mo1_volumematric_moisture']=( sp_sch_field.df['sa3_mo1']-180)/(380-180)*porosity
sp_sch_field.df['sa3_mo2_volumematric_moisture']=( sp_sch_field.df['sa3_mo2']-180)/(380-180)*porosity
sp_sch_field.df['sa3_mo3_volumematric_moisture']=( sp_sch_field.df['sa3_mo3']-180)/(380-180)*porosity
sp_sch_field.df['sa3_mo4_volumematric_moisture']=( sp_sch_field.df['sa3_mo4']-180)/(380-180)*porosity
sp_sch_field.df['sa3_mo5_volumematric_moisture']=( sp_sch_field.df['sa3_mo5']-180)/(380-180)*porosity
sp_sch_field.df.loc['2022-1-1':'2022-1-4']=np.nan
sp_sch_field_sa2=sp_sch_field.df.loc['2021-10-17':'2022-1-17']
sp_sch_field_sa3=sp_sch_field.df.loc['2021-9-16':'2022-1-17']
field_sa2_part1_dry_water_m=(sp_sch_field_sa2['sa2_mo1_volumematric_moisture']+sp_sch_field_sa2['sa2_mo2_volumematric_moisture'])/2*0.05
field_sa2_part2_dry_water_m=(sp_sch_field_sa2['sa2_mo2_volumematric_moisture']+sp_sch_field_sa2['sa2_mo3_volumematric_moisture'])/2*0.05
field_sa2_part3_dry_water_m=(sp_sch_field_sa2['sa2_mo3_volumematric_moisture']+sp_sch_field_sa2['sa2_mo4_volumematric_moisture'])/2*0.1
field_sa2_part4_dry_water_m=(sp_sch_field_sa2['sa2_mo4_volumematric_moisture']+sp_sch_field_sa2['sa2_mo5_volumematric_moisture'])/2*0.3

field_sa3_part1_dry_water_m=(sp_sch_field_sa3['sa3_mo1_volumematric_moisture']+sp_sch_field_sa3['sa3_mo2_volumematric_moisture'])/2*0.05
field_sa3_part2_dry_water_m=(sp_sch_field_sa3['sa3_mo2_volumematric_moisture']+sp_sch_field_sa3['sa3_mo3_volumematric_moisture'])/2*0.05
field_sa3_part3_dry_water_m=(sp_sch_field_sa3['sa3_mo3_volumematric_moisture']+sp_sch_field_sa3['sa3_mo4_volumematric_moisture'])/2*0.1
field_sa3_part4_dry_water_m=(sp_sch_field_sa3['sa3_mo4_volumematric_moisture']+sp_sch_field_sa3['sa3_mo5_volumematric_moisture'])/2*0.3

totalwater_sa2_evp_m=(field_sa2_part1_dry_water_m+field_sa2_part2_dry_water_m+field_sa2_part3_dry_water_m+field_sa2_part4_dry_water_m)
totalwater_sa3_evp_m=(field_sa3_part1_dry_water_m+field_sa3_part2_dry_water_m+field_sa3_part3_dry_water_m+field_sa3_part4_dry_water_m)
sa2_evp_rate_mmPday=-np.append(np.nan,constants.mmPm*(np.diff(totalwater_sa2_evp_m)/sp_input['delta_t_s'])/constants.dayPs)
sa3_evp_rate_mmPday=-np.append(np.nan,constants.mmPm*(np.diff(totalwater_sa3_evp_m)/sp_input['delta_t_s'])/constants.dayPs)


sp_sch_field_sa2['sa2_evp_rate_mmPday']=sa2_evp_rate_mmPday
sp_sch_field_sa2['sa2_totalwater_evp_m']=totalwater_sa2_evp_m
sp_sch_field_sa3['sa3_evp_rate_mmPday']=sa3_evp_rate_mmPday
sp_sch_field_sa3['sa3_totalwater_evp_m']=totalwater_sa3_evp_m


tb_pandas=thingsboard_to_pandas_py3.tingsboard_to_pandas('C:/pyduino/pyduino/python/tb_to_csv/tb_credential_column_phase2.json')
tb_pandas.get_token()    # get the token associated with the account
tb_pandas.get_keys()     # list of keys in the device
tb_pandas.get_data()     # obtain data from thingsboard stored at tb_pandas['results']
tb_pandas.convert_data_to_df()  # convert each datasets to pandas dataframe



# merge data    
with open('C:/pyduino/pyduino/python/tb_to_csv/schedule_column_phase2.json') as data_file:    
    sp_input = json.load(data_file)


# open_day='2020-03-15'
# close_day='2020-06-6'
# tb_pandas.result_df['2020-03-16':'2020-06-6']>=open_day
# con2=tb_pandas.result_df[sp_input['start_time']]<close_day
# tb_pandas.result_df=order_data[con1&con2]

sp_sch={}
#plot_interpolate=False
plot_interpolate=True

sp_sch=pandas_scale.concat_data_tb(
    pd.datetime.strptime(sp_input['start_time'],'%Y/%b/%d %H:%M'),
    pd.datetime.strptime(sp_input['end_time'],'%Y/%b/%d %H:%M'),
    sp_input['delta_t_s'] );

sp_sch.start_dt = pd.datetime.strptime(sp_input['start_time'],'%Y/%b/%d %H:%M')
sp_sch.end_dt   = pd.datetime.strptime(sp_input['end_time'  ],'%Y/%b/%d %H:%M')

# managing data
tb_pandas.result_df['column_mo1']['value'] \
    [ tb_pandas.result_df['column_mo1']['value'] >500 ] =np.nan 
tb_pandas.result_df['column_mo1'].loc['2021-09-14':]=450
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
        plot=plot_interpolate  ,coef=5e-18,rm_nan=True)
sp_sch.merge_data_from_tb(
        input_time_series=tb_pandas.result_df['column_mo2'].index, 
        input_data_series=tb_pandas.result_df['column_mo2']['value'], 
        output_time_series=sp_sch.df.index,key_name='column_mo2' ,
        plot=plot_interpolate  ,coef=5e-18,rm_nan=True)
sp_sch.merge_data_from_tb(
        input_time_series=tb_pandas.result_df['column_mo3'].index, 
        input_data_series=tb_pandas.result_df['column_mo3']['value'], 
        output_time_series=sp_sch.df.index,key_name='column_mo3' ,
        plot=plot_interpolate  ,coef=5e-18,rm_nan=True)
sp_sch.merge_data_from_tb(
        input_time_series=tb_pandas.result_df['column_mo4'].index, 
        input_data_series=tb_pandas.result_df['column_mo4']['value'], 
        output_time_series=sp_sch.df.index,key_name='column_mo4' ,
        plot=plot_interpolate  ,coef=5e-18,rm_nan=True)
sp_sch.merge_data_from_tb(
        input_time_series=tb_pandas.result_df['column_mo5'].index, 
        input_data_series=tb_pandas.result_df['column_mo5']['value'], 
        output_time_series=sp_sch.df.index,key_name='column_mo5' ,
        plot=plot_interpolate  ,coef=5e-18,rm_nan=True)
# tb_pandas.result_df['scale'][tb_pandas.result_df['scale']<=2000]=np.nan
# sp_sch.merge_data_from_tb(
#         input_time_series=tb_pandas.result_df['scale'].index, 
#         input_data_series=tb_pandas.result_df['scale']['value'], 
#         output_time_series=sp_sch.df.index,key_name='scale' ,
#         plot=plot_interpolate  ,coef=5e-18,rm_nan=True)
sp_sch.df['column_mo3'].loc['2021-08-21':'2021-08-22']=282
sp_sch.df['column_mo4'].loc['2021-08-21':'2021-08-22']=435
# sp_sch.df['scale'].loc['2021-03-15':'2021-05-11 13']=np.nan
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
# sp_sch.df['scale_decreasing_rate_gPday'] = \
#     np.append(np.diff(sp_sch.df['scale']), np.nan) \
#     / sp_input['delta_t_s']*constants.sPday
# sp_sch.df['scale_decreasing_rate_gPday'].loc[np.abs(sp_sch.df['scale_decreasing_rate_gPday'])>1000]=np.nan
# sp_sch.df['column_mo1_volumematric_moisture']=( 521-sp_sch.df['column_mo1'])/(521-267)*porosity
sp_sch.df['column_mo1_volumematric_moisture']=( 460-sp_sch.df['column_mo1'])/(460-267)*porosity
sp_sch.df['column_mo2_volumematric_moisture']=( 460-sp_sch.df['column_mo2'])/(460-259)*porosity
sp_sch.df['column_mo3_volumematric_moisture']=( 500-sp_sch.df['column_mo3'])/(500-269)*porosity
sp_sch.df['column_mo4_volumematric_moisture']=( 460-sp_sch.df['column_mo4'])/(460-269)*porosity
sp_sch.df['column_mo5_volumematric_moisture']=( 460-sp_sch.df['column_mo5'])/(460-269)*porosity
sp_sch_new1=sp_sch.df.loc['2021-07-31 15:00':'2021-08-1 08:30']
sp_sch_new2=sp_sch.df.loc['2021-08-20 13:30':]
sp_sch.df=sp_sch_new1.append(sp_sch_new2)

#drying process
column_mo0_volumematric_moisture_dry=0
part1_dry_water_m=(column_mo0_volumematric_moisture_dry+sp_sch.df['column_mo1_volumematric_moisture'])/2*0.1
part2_dry_water_m=(sp_sch.df['column_mo1_volumematric_moisture']+sp_sch.df['column_mo2_volumematric_moisture'])/2*0.1
part3_dry_water_m=(sp_sch.df['column_mo2_volumematric_moisture']+sp_sch.df['column_mo3_volumematric_moisture'])/2*0.1
totalwater_evp_m=(part1_dry_water_m+part2_dry_water_m+part3_dry_water_m)
evp_rate_mmPday=-np.append(np.nan,constants.mmPm*(np.diff(totalwater_evp_m)/sp_input['delta_t_s'])/constants.dayPs)
evp_rate_mmPday[np.abs(evp_rate_mmPday)>5]=np.nan
sp_sch.df['evp_rate_mmPday']=evp_rate_mmPday
sp_sch.df['totalwater_evp_m']=totalwater_evp_m

# plt.figure()
# plt.plot(sp_sch.df.index[1:],-evp_rate_mmPday)
# plt.xlabel('Time')
# plt.ylabel('Evaporation rate (mm)')


# second_pump_rising_time=second_pump.index-np.datetime64('2021-05-23 02')

#path_im='/home/chenming/Projects/tailings/area_51_redmud_4cm_photo_'+sch_name+'/'
#import json
#inp_js = json.load(open('input/input.json'))

path_im1='C:\Project\MDBA\data_deliverable\photos\\column_camera2'
path_im2='C:\Project\MDBA\data_deliverable\photos\\column'

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
camera1_time=[None]*len(file_name1)
j=0
from datetime import datetime

for i in file_name1:
    camera1_time_str=i[-41:-26]
    camera1_time[j]=datetime.strptime(camera1_time_str, "%Y-%m-%d_%H%M")
    j=j+1
camera1_time=np.array(camera1_time)   
    
camera2_time=[None]*len(file_name2)
j=0
for i in file_name2:
    camera2_time_str=i[-33:-18]
    camera2_time[j]=datetime.strptime(camera2_time_str, "%Y-%m-%d_%H%M")
    j=j+1
camera2_time=np.array(camera2_time)   
# y_fontsize=24
plt.ioff()
j=0
interval=10
array=sp_sch.df.to_numpy()
# cross0=[sp_sch['column_mo1_volumematric_moisture'][1],
#        sp_sch['column_mo2_volumematric_moisture'][0],
#        sp_sch['column_mo3_volumematric_moisture'][0],
#        sp_sch['column_mo4_volumematric_moisture'][0],
#        sp_sch['column_mo5_volumematric_moisture'][0]]
# for i in range(1,len(sp_sch.df),100):

for ii in file_name2[0:-1:interval]: 
    im_column_camera2=image.imread(file_name2[j])
    idx_im, min_value = min(enumerate( abs(camera2_time[j]-camera1_time)), key=operator.itemgetter(1))
    im_column_camera1=image.imread(file_name1[idx_im])
    idx, min_value = min(enumerate( abs(sp_sch.df.index-camera2_time[j])), key=operator.itemgetter(1))
    print(idx)
    moisture_string=[sp_sch.df['column_mo1_volumematric_moisture'][idx],
           sp_sch.df['column_mo2_volumematric_moisture'][idx],
           sp_sch.df['column_mo3_volumematric_moisture'][idx],
           sp_sch.df['column_mo4_volumematric_moisture'][idx]]
    moisture_string_sa2=[sp_sch_field_sa2['sa2_mo1_volumematric_moisture'][idx],
           sp_sch_field_sa2['sa2_mo2_volumematric_moisture'][idx],
           sp_sch_field_sa2['sa2_mo3_volumematric_moisture'][idx],
           sp_sch_field_sa2['sa2_mo4_volumematric_moisture'][idx],
           sp_sch_field_sa2['sa2_mo5_volumematric_moisture'][idx]]
    moisture_string_sa3=[sp_sch_field_sa3['sa3_mo1_volumematric_moisture'][idx],
           sp_sch_field_sa3['sa3_mo2_volumematric_moisture'][idx],
           sp_sch_field_sa3['sa3_mo3_volumematric_moisture'][idx],
           sp_sch_field_sa3['sa3_mo4_volumematric_moisture'][idx],
           sp_sch_field_sa3['sa3_mo5_volumematric_moisture'][idx]]    
    # mass_of_water_in_column_kg=cross-cross0
    fig = plt.figure(figsize=(20,12))
    ax = [[] for i in range(6)]
    ax[0] = plt.subplot2grid((20, 12), (0, 0), colspan=5,rowspan=5)
    ax[1] = plt.subplot2grid((20, 12), (6, 0), colspan=5,rowspan=5)
    ax[2] = plt.subplot2grid((20, 12), (12, 0), colspan=5,rowspan=5)
    ax[3] = plt.subplot2grid((20, 12), (0, 5), colspan=3,rowspan=15)
    ax[4] = plt.subplot2grid((20, 12), (0, 8), colspan=8,rowspan=8)
    ax[5] = plt.subplot2grid((20, 12), (8, 8), colspan=8,rowspan=8)
    plt.subplots_adjust(wspace=1.5)

    ax[0].plot((sp_sch_field_sa2.index-sp_sch_field_sa2.index[0])/np.timedelta64(1,'D'),sp_sch_field_sa2['sa2_evp_rate_mmPday'],'y-',label='SA2')
    ax[0].plot((sp_sch_field_sa3.index-sp_sch_field_sa3.index[0])/np.timedelta64(1,'D'),sp_sch_field_sa3['sa3_evp_rate_mmPday'],'k-',label='SA3')
    ax[0].plot((sp_sch.df.index-sp_sch.df.index[0])/np.timedelta64(1,'D'),sp_sch.df['evp_rate_mmPday'],'b-',label='Column')

    ax[1].plot((sp_sch.df.index-sp_sch.df.index[0])/np.timedelta64(1,'D'),sp_sch.df['column_mo1_volumematric_moisture'],label='10cm BGL')
    ax[1].plot((sp_sch.df.index-sp_sch.df.index[0])/np.timedelta64(1,'D'),sp_sch.df['column_mo2_volumematric_moisture'],label='20cm BGL')
    ax[1].plot((sp_sch.df.index-sp_sch.df.index[0])/np.timedelta64(1,'D'),sp_sch.df['column_mo3_volumematric_moisture'],label='30cm BGL')
    ax[1].plot((sp_sch.df.index-sp_sch.df.index[0])/np.timedelta64(1,'D'),sp_sch.df['column_mo4_volumematric_moisture'],label='50cm BGL')
    ax[1].plot((sp_sch.df.index-sp_sch.df.index[0])/np.timedelta64(1,'D'),sp_sch.df['column_mo5_volumematric_moisture'],label='70cm BGL')
    ax[2].plot((sp_sch.df.index-sp_sch.df.index[0])/np.timedelta64(1,'D'),sp_sch.df['totalwater_evp_m']*constants.m2mm,'b-',label='Column')
    ax[2].plot((sp_sch_field_sa2.index-sp_sch_field_sa2.index[0])/np.timedelta64(1,'D'),sp_sch_field_sa2['sa2_totalwater_evp_m']*constants.m2mm,'y-',label='SA2')
    ax[2].plot((sp_sch_field_sa3.index-sp_sch_field_sa3.index[0])/np.timedelta64(1,'D'),sp_sch_field_sa3['sa3_totalwater_evp_m']*constants.m2mm,'k-',label='SA3')

    ax[3].plot(moisture_string,[-0.1,-0.2,-0.3,-0.5],'b-',label='Column')
    ax[3].plot(moisture_string_sa2,[0,-0.05,-0.1,-0.2,-0.5],'y-',label='SA2')
    ax[3].plot(moisture_string_sa3,[0,-0.05,-0.1,-0.2,-0.5],'k-',label='SA3')
    
    ax[0].set_ylim([0,10])
    ax[3].set_xlim([0,.5])
    ax[3].set_yticks([-0.5,-0.4,-0.3,-0.2,-0.1,0])
    ax[3].set_yticklabels(['0.5','0.4','0.3','0.2','0.1','0'])
    ax[3].set_xlabel('Volumetric water content (-)')
    ax[3].set_ylabel('Depth (m)')
    ax[0].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[1].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[2].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[3].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[0].axvline(np.timedelta64(camera2_time[j]-camera2_time[0])/np.timedelta64(1,'D'),color='r')
    ax[1].axvline(np.timedelta64(camera2_time[j]-camera2_time[0])/np.timedelta64(1,'D'),color='r')
    ax[2].axvline(np.timedelta64(camera2_time[j]-camera2_time[0])/np.timedelta64(1,'D'),color='r')
    ax[0].legend()
    ax[1].legend()
    ax[2].legend()
    ax[3].legend()
    ax[4].imshow(im_column_camera1,aspect='auto')
    ax[4].axis('off')
    # fig.text(0.01,0.68,f'{im_time}',fontsize=y_fontsize,color='k')
    
    
    ax[5].imshow(im_column_camera2,aspect='auto')
    ax[5].axis('off')

    # ax[0].set_xticklabels([])
    # ax[1].set_xticklabels([])
    ax[2].set_xlabel('Time (days)')
    ax[3].set_xlabel('Volumetric \nwater content \n(m$^3$/m$^3$)')
    ax[0].set_ylabel('Water lossing rate \n(mm/day)')
    ax[1].set_ylabel('Volumetric \nwater content \nin the column\n(m$^3$/m$^3$)')
    ax[2].set_ylabel('Water depth\n(mm)')
    ax[3].set_ylabel('Depth (m)')
    # plt.setp(ax.spines.values(), linewidth=2)
    # ax[2].xaxis.set_major_formatter(mdates.DateFormatter('%b/%d'))
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
for filename in glob.glob('C:\Project\MDBA\dashboard_column_phase2\*.jpg'):    
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)


out = cv2.VideoWriter('column.avi',cv2.VideoWriter_fourcc(*'DIVX'), 15, size)
 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()
