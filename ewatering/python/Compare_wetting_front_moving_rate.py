# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 11:06:45 2022
Compare wetting front moving rate of columns
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
import matplotlib.pylab as pylab
plt.rcParams.update({
    "font.weight": "bold",
    "font.size": 18,
    # "figure.figsize": (9,6),
    "xtick.major.size": 5,
    "xtick.major.pad": 7,
    "xtick.labelsize": 16,
    "ytick.labelsize": 16,
    "axes.labelweight": 'bold',
    "grid.color": "0.5",
    "grid.linestyle": "-",
    "grid.linewidth": 2,
    "lines.linewidth": 4,
    "lines.color": "g",
    "axes.linewidth": 4,
    "legend.fontsize" : 16, 
    "legend.loc":'lower right',
    "legend.framealpha": 0.5,
})

fontsize_label=20
porosity=0.5
column_radius_m=0.05

microS_20000=pd.read_excel('C:/Project/MDBA/data_deliverable/lab/column_infiltration_rate.xls',sheet_name='20000microSm')
microS_50000=pd.read_excel('C:/Project/MDBA/data_deliverable/lab/column_infiltration_rate.xls',sheet_name='50000microSm')
Large_column_1=pd.read_excel('C:/Project/MDBA/data_deliverable/lab/column_infiltration_rate.xls',sheet_name='Large_column_1')
Large_column_2=pd.read_excel('C:/Project/MDBA/data_deliverable/lab/column_infiltration_rate.xls',sheet_name='Large_column_2')
microS_20000.wetting_front_moving_rate_mmPday[microS_20000.wetting_front_moving_rate_mmPday>1000]=np.nan
microS_50000.wetting_front_moving_rate_mmPday[microS_50000.wetting_front_moving_rate_mmPday>1000]=np.nan
exec(open('C:\columnpy\columnpy\ewatering\python\get_data_column_py3.py').read())
Large_column_1.wetting_front_moving_rate_mmPday[Large_column_1.wetting_front_moving_rate_mmPday>1000]=np.nan
sp_sch.merge_data_from_tb(
        input_time_series=Large_column_1.Time, 
        input_data_series=Large_column_1.wetting_front_moving_rate_mmPday, 
        output_time_series=sp_sch.df.index,key_name='wetting_front_moving_rate_mmPday' ,
        plot=plot_interpolate  ,coef=5e-17,rm_nan=True)
column_1=sp_sch

tb_pandas=thingsboard_to_pandas_py3.tingsboard_to_pandas('C:/pyduino/pyduino/python/tb_to_csv/tb_credential_column_feb_2022.json')
tb_pandas.get_token()    # get the token associated with the account
tb_pandas.get_keys()     # list of keys in the device
tb_pandas.get_data()     # obtain data from thingsboard stored at tb_pandas['results']
tb_pandas.convert_data_to_df()  # convert each datasets to pandas dataframe

# merge data    
with open('C:/pyduino/pyduino/python/tb_to_csv/schedule_column_feb_2022.json') as data_file:    
    sp_input = json.load(data_file)


# open_day='2020-03-15'
# close_day='2020-06-6'
# tb_pandas.result_df['2020-03-16':'2020-06-6']>=open_day
# con2=tb_pandas.result_df[sp_input['start_time']]<close_day
# tb_pandas.result_df=order_data[con1&con2]

sp_sch={}
#plot_interpolate=False
plot_interpolate=False

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
tb_pandas.result_df['scale_2'][tb_pandas.result_df['scale_2']>10000]=np.nan
tb_pandas.result_df['scale_2'][tb_pandas.result_df['scale_2']==0]=np.nan
tb_pandas.result_df['scale_2'].loc['2022-02-14':'2022-02-15']=np.nan

tb_pandas.result_df['scale_2'].loc['2022-02-14':'2022-02-15']=np.nan
plot_interpolate=True
tb_pandas.result_df['scale_2'].loc['2022-02-15':'2022-02-23 21:00']=np.nan
tb_pandas.result_df['scale_2'].loc['2022-02-23 21:00':]=tb_pandas.result_df['scale_2'].loc['2022-02-23 21:00':]+(6430-5850)
tb_pandas.result_df['scale_2'].loc['2022-02-28 1:00':'2022-02-28 9:00']=np.nan
tb_pandas.result_df['scale_2'].loc['2022-02-28 9:00':]=tb_pandas.result_df['scale_2'].loc['2022-02-28 9:00':]+(5686-4300)
sp_sch.merge_data_from_tb(
        input_time_series=tb_pandas.result_df['scale_2'].index, 
        input_data_series=tb_pandas.result_df['scale_2']['value'], 
        output_time_series=sp_sch.df.index,key_name='scale' ,
        plot=plot_interpolate  ,coef=5e-16,rm_nan=True)
sp_sch.df['scale'].loc['2022-02-15':'2022-02-22']=np.nan

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
sp_sch.merge_data_from_tb(
        input_time_series=Large_column_2.Time, 
        input_data_series=Large_column_2.wetting_front_moving_rate_mmPday, 
        output_time_series=sp_sch.df.index,key_name='wetting_front_moving_rate_mmPday' ,
        plot=plot_interpolate  ,coef=5e-10,rm_nan=True)
sp_sch.df['wetting_front_moving_rate_mmPday'][sp_sch.df['wetting_front_moving_rate_mmPday']<0]=np.nan
column_2=sp_sch
sp_sch.merge_data_from_tb(
        input_time_series=Large_column_2.Time, 
        input_data_series=Large_column_2.wetting_front_moving_rate_mmPday, 
        output_time_series=sp_sch.df.index,key_name='wetting_front_moving_rate_mmPday' ,
        plot=plot_interpolate  ,coef=5e-11,rm_nan=True)
sp_sch.df['wetting_front_moving_rate_mmPday'][sp_sch.df['wetting_front_moving_rate_mmPday']<0]=0

fig = plt.figure(figsize=(20,12))
ax1 = plt.subplot(311)
ax1.plot((microS_20000.Time-microS_20000.Time[0])/np.timedelta64(1,'D'),microS_20000.surface_water_falling_rate_mmPday,label='20,000\u03BCS/cm',color='r')
ax1.plot((column_2.df.index-column_2.df.index[0])/np.timedelta64(1,'D'),-column_2.df['infiltrastion_rate_mmPday'],label='200\u03BCS/cm',color='k')
ax1.legend(loc='upper right')
ax1.set_xlim([0,25])
# ax1.set_ylim([0,50])
ax1.set_xticklabels([])
ax1.set_ylabel('Surface water \nfalling (nfiltration) \n rate \n(mm/day)')
ax1.grid(True,which="both",ls=":",color = '0.5')
# ax1.set_yscale('log')

ax2 = plt.subplot(312)

ax2.plot((column_1.df.index-column_1.df.index[0])/np.timedelta64(1,'D'),column_1.df['wetting_front_moving_rate_mmPday'],label='Deionsied water',color='b')
ax2.plot((column_2.df.index-column_2.df.index[0])/np.timedelta64(1,'D'),column_2.df['wetting_front_moving_rate_mmPday'],label='200\u03BCS/cm',color='k')
ax2.plot((microS_20000.Time-microS_20000.Time[0])/np.timedelta64(1,'D'),microS_20000.wetting_front_moving_rate_mmPday,label='20,000\u03BCS/cm',color='r')
ax2.plot((microS_50000.Time-microS_50000.Time[0])/np.timedelta64(1,'D'),microS_50000.wetting_front_moving_rate_mmPday,label='50,000\u03BCS/cm',color='g')
# ax2.set_ylim([0,500])
ax2.set_xlim([0,25])
ax2.set_xlabel('Time (Days)')
ax2.set_ylabel('Wetting front \n falling rate \n(mm/day)')
ax2.legend(loc='upper right')
ax2.grid(True,which="both",ls=":",color = '0.5')
ax2.set_yscale('log')

plt.show()
# ax3 = plt.subplot(313)
# ax2.plot((microS_20000.Time-microS_20000.Time[0])/np.timedelta64(1,'D'),microS_20000.wetting_front_moving_rate_mmPday,,label='20,000\u03BCS/cm')
# ax2.plot((microS_50000.Time-microS_50000.Time[0])/np.timedelta64(1,'D'),microS_50000.wetting_front_moving_rate_mmPday,label='50,000\u03BCS/cm')

# ax1.xaxis.set_major_formatter(mdates.DateFormatter('%d'))

#First column