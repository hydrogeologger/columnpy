# -*- coding: utf-8 -*-
"""
1. Python version 3.7.1
2. This script is a combination of following:
    a). init_pandas_mo_su.py
    b). plot_mo_su.py
    c). read_schedule.py
    d). run_all.py
    e). video_ProjName.py 
You can still run them separately by copying different sections and pasting them into console.
3. The dataset is a csv file, which is directly pulled from Thingsboard.
4. OpenCV is used to make videos for Windows. You can also use FFMPEG if you are using Linux.
5. Outline:
    Line 37~142: Data preprocessing/initialisation (equiv. to init_pandas_mo_su.py)
    Line 144~255: Data processing/calculation (equiv. to read_schedule.py)
    Line 258~376: Plotting (equiv. to plot_mo_su.py)
    Line 368~599: Generating video images (equiv. to video_ProjName.py)
    Line 601~637: Generating video
"""

import os
import cv2
import sys
sys.path.append(os.environ['pyduino']+'/python/post_processing/')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import matplotlib.image as image
import constants
import operator
import glob
from datetime import datetime
from PIL import Image


"""Read the csv file and create a DataFrame"""
df=pd.read_csv('wwl_cali.csv')

"""Select durations
First, we need to ensure df['date_time'] is a Series with dtype datetime64.
Second, we make a boolean mask to select the duration we want"""

df['date_time']=pd.to_datetime(df['date_time'], format='%Y/%m/%d %H:%M:%S')
df['date_time']=df['date_time']+pd.DateOffset(hours=10) #add 10 hours 

start_date = '2019-07-14 12:00:00'  
end_date = '2019-07-27 22:00:00'     
mask = (df['date_time'] > start_date) & (df['date_time'] <= end_date)
df = df.loc[mask] 

#special treatment
df.ec1.loc[(df['date_time'] > '2019-07-16 18:00:00') & (df['date_time'] <= '2019-07-17 13:00:00')] = np.nan
df.ec2.loc[(df['date_time'] > '2019-07-17 23:00:00') & (df['date_time'] <= '2019-07-18 19:00:00')] = np.nan
df.ec3.loc[(df['date_time'] > '2019-07-19 19:00:00') & (df['date_time'] <= '2019-07-19 23:55:00')] = np.nan
df.ec6.loc[(df['date_time'] > '2019-07-15 16:00:00') & (df['date_time'] <= '2019-07-15 20:00:00')] = np.nan
df.ec6.loc[(df['date_time'] > '2019-07-16 12:00:00') & (df['date_time'] <= '2019-07-16 17:00:00')] = np.nan
df.ec6.loc[(df['date_time'] > '2019-07-15 06:00:00') & (df['date_time'] <= '2019-07-16 01:00:00')] = np.nan

"""Filter out invalid data by converting them to NaN 
invalid data can be:
    1. empty string (sometimes sensors could not get a reading and return an empty
                     string ' ', pandas treat empty string and NaN value differently)
    2. extreme values
    3. values that are nonsense (e.g. delta_t<0 for suction sensor or negative
                                  readings for scale)
"""
df['delta_t1'].loc[df['delta_t1']<1]=np.nan
df['delta_t2'].loc[df['delta_t2']<1]=np.nan
df['delta_t3'].loc[df['delta_t3']<1]=np.nan
df['delta_t4'].loc[df['delta_t4']<1]=np.nan
df['delta_t5'].loc[df['delta_t5']<1]=np.nan
df['delta_t6'].loc[df['delta_t6']<1]=np.nan
df['delta_t7'].loc[df['delta_t7']<1]=np.nan
df['delta_t8'].loc[df['delta_t8']<1]=np.nan
df['delta_t9'].loc[df['delta_t9']<1]=np.nan
df['delta_t10'].loc[df['delta_t10']<1]=np.nan

df['raw1'].loc[df['raw1']<1]=np.nan
df['raw2'].loc[df['raw2']<1]=np.nan
df['raw3'].loc[df['raw3']<1]=np.nan
df['raw4'].loc[df['raw4']<1]=np.nan
df['raw5'].loc[df['raw5']<1]=np.nan
df['raw6'].loc[df['raw6']<1]=np.nan

df['ec1'].loc[df['ec1']<1]=np.nan
df['ec2'].loc[df['ec2']<1]=np.nan
df['ec3'].loc[df['ec3']<1]=np.nan
df['ec4'].loc[df['ec4']<1]=np.nan
df['ec5'].loc[df['ec5']<1]=np.nan
df['ec6'].loc[df['ec6']<1]=np.nan

df['scale1'].loc[df['scale1']<1]=np.nan
df['scale2'].loc[df['scale2']<1]=np.nan

"""Deal with the NaN values"""
#-------------------------Method 1: Drop all NaN values------------------------
#drop NaN values from every column in the list called header and re-index
#If you are worried about losing too many data, you can use Method 2

#header = ['scale1','scale2',
#          'delta_t1','delta_t2','delta_t3','delta_t4','delta_t5',
#          'delta_t6','delta_t7','delta_t8','delta_t9','delta_t10',
#          'raw1','raw2','raw3','raw4','raw5','raw6',
#          'ec1','ec2','ec3','ec4','ec5','ec6',
#          't1_low','t1_high','t2_low','t2_high','t3_low','t3_high','t4_low','t4_high','t5_low','t5_high',
#          't6_low','t6_high','t7_low','t7_high','t8_low','t8_high','t9_low','t9_high','t10_low','t10_high']
#
#df = df.dropna(axis=0,subset=header).reset_index(drop=True)

#----------------------Method 2: Fill NaN with interpolated values-------------
#df = df.fillna(method="ffill") #fill NaN with the value in the forward row
#df = df.fillna(method="bfill") #fill NaN with the value in the backward row
#df = df.fillna({'col_A':0,'col_B':10,'col_C':'blabla'}) #fill NaN with customized value
df = df.interpolate()
df.reset_index(inplace=True, drop=True)

"""Plot to see how our data look like by unhashing the following"""
#df.plot(x='date_time',y='delta_t1')
#df.plot(x='date_time',y='delta_t2')
#df.plot(x='date_time',y='delta_t3')
#df.plot(x='date_time',y='delta_t4')
#df.plot(x='date_time',y='delta_t5')
#df.plot(x='date_time',y='delta_t6')
#df.plot(x='date_time',y='delta_t7')
#df.plot(x='date_time',y='delta_t8')
#df.plot(x='date_time',y='delta_t9')
#df.plot(x='date_time',y='delta_t10')
#df.plot(x='date_time',y='raw1')
#df.plot(x='date_time',y='raw2') 
#df.plot(x='date_time',y='raw3')
#df.plot(x='date_time',y='raw4')
#df.plot(x='date_time',y='raw5')
#df.plot(x='date_time',y='raw6')
#df.plot(x='date_time',y='ec1')
#df.plot(x='date_time',y='ec2')
#df.plot(x='date_time',y='ec3')
#df.plot(x='date_time',y='ec4')
#df.plot(x='date_time',y='ec5')
#df.plot(x='date_time',y='ec6')
#df.plot(x='date_time',y='scale1')
#df.plot(x='date_time',y='scale2')

SURFACE_AREA = 0.09720 #m2 red basin
POROSITY = 0.55
df.por = 0.55
dt_s = 1800 #s this has to be the same with the one in schedule.json!!!
#time_surface_emerge_1 = '2019-07-15 18:00:00'
time_surface_emerge_1 = '2019-07-17 23:00:00'
time_surface_emerge_1 = pd.to_datetime(time_surface_emerge_1, format='%Y/%m/%d %H:%M:%S')
time_surface_emerge_2 = '2019-07-15 12:00:00'
time_surface_emerge_2 = pd.to_datetime(time_surface_emerge_2, format='%Y/%m/%d %H:%M:%S')
aa=-1.1
bb=10
moist_minimum = 0.12 #Don't foget to measure the MC at the end of the test

# normal_delta_t = 0 for dry soil and 1 for saturated soil
df.delta_t_max_su1,df.delta_t_min_su1 = np.average(df.delta_t1[-20:]),np.average(df.delta_t1[0])
df['norm_delta_t_su1'] = (df.delta_t1 - df.delta_t_min_su1)/(df.delta_t_max_su1 - df.delta_t_min_su1)
df.delta_t_max_su2,df.delta_t_min_su2 = np.average(df.delta_t2[-20:]),np.average(df.delta_t2[0])
df['norm_delta_t_su2'] = (df.delta_t2 - df.delta_t_min_su2)/(df.delta_t_max_su2 - df.delta_t_min_su2)
df.delta_t_max_su3,df.delta_t_min_su3 = np.average(df.delta_t2[-20:]),np.average(df.delta_t3[0])
df['norm_delta_t_su3'] = (df.delta_t3 - df.delta_t_min_su3)/(df.delta_t_max_su3 - df.delta_t_min_su3)
df.delta_t_max_su4,df.delta_t_min_su4 = np.average(df.delta_t2[-20:]),np.average(df.delta_t4[0])
df['norm_delta_t_su4'] = (df.delta_t4 - df.delta_t_min_su4)/(df.delta_t_max_su4 - df.delta_t_min_su4)
df.delta_t_max_su5,df.delta_t_min_su5 = np.average(df.delta_t2[-20:]),np.average(df.delta_t5[0])
df['norm_delta_t_su5'] = (df.delta_t5 - df.delta_t_min_su5)/(df.delta_t_max_su5 - df.delta_t_min_su5)
df.delta_t_max_su6,df.delta_t_min_su6 = np.average(df.delta_t2[-20:]),np.average(df.delta_t6[0])
df['norm_delta_t_su6'] = (df.delta_t6 - df.delta_t_min_su6)/(df.delta_t_max_su6 - df.delta_t_min_su6)
df.delta_t_max_su7,df.delta_t_min_su7 = np.average(df.delta_t2[-20:]),np.average(df.delta_t7[0])
df['norm_delta_t_su7'] = (df.delta_t7 - df.delta_t_min_su7)/(df.delta_t_max_su7 - df.delta_t_min_su7)
df.delta_t_max_su8,df.delta_t_min_su8 = np.average(df.delta_t2[-20:]),np.average(df.delta_t8[0])
df['norm_delta_t_su8'] = (df.delta_t8 - df.delta_t_min_su8)/(df.delta_t_max_su8 - df.delta_t_min_su8)
df.delta_t_max_su9,df.delta_t_min_su9 = np.average(df.delta_t2[-20:]),np.average(df.delta_t9[0])
df['norm_delta_t_su9'] = (df.delta_t9 - df.delta_t_min_su9)/(df.delta_t_max_su9 - df.delta_t_min_su9)
df.delta_t_max_su10,df.delta_t_min_su10 = np.average(df.delta_t2[-20:]),np.average(df.delta_t10[0])
df['norm_delta_t_su10'] = (df.delta_t10 - df.delta_t_min_su10)/(df.delta_t_max_su10 - df.delta_t_min_su10)

df['suction1']=np.exp(-1.5*(df['norm_delta_t_su1']**aa-bb))
df['suction2']=np.exp(-1.5*(df['norm_delta_t_su2']**aa-bb))
df['suction3']=np.exp(-1.5*(df['norm_delta_t_su3']**aa-bb))
df['suction4']=np.exp(-1.5*(df['norm_delta_t_su4']**aa-bb))
df['suction5']=np.exp(-1.5*(df['norm_delta_t_su5']**aa-bb))
df['suction6']=np.exp(-1.5*(df['norm_delta_t_su6']**aa-bb))
df['suction7']=np.exp(-1.5*(df['norm_delta_t_su7']**aa-bb))
df['suction8']=np.exp(-1.5*(df['norm_delta_t_su8']**aa-bb))
df['suction9']=np.exp(-1.5*(df['norm_delta_t_su9']**aa-bb))
df['suction10']=np.exp(-1.5*(df['norm_delta_t_su10']**aa-bb))

#evap_rate_scale1: evaporation rate calculated from scale, unit is m/s
df['cum_evap_scale1']=(df['scale1'][1]-df['scale1'])*constants.g2kg/SURFACE_AREA/constants.rhow_pure_water
df['evap_rate_scale1']=np.append(np.diff(df['cum_evap_scale1'] ),np.nan)/dt_s
df['cum_evap_scale2']=(df['scale2'][1]-df['scale2'])*constants.g2kg/SURFACE_AREA/constants.rhow_pure_water
df['evap_rate_scale2']=np.append(np.diff(df['cum_evap_scale2'] ),np.nan)/dt_s
df['evap_rate_scale1'].loc[df['evap_rate_scale1']<0]=0
df['evap_rate_scale2'].loc[df['evap_rate_scale2']<0]=0
df['evap_rate_scale1'].loc[df['evap_rate_scale1']>6e-8]=np.nan
df['evap_rate_scale2'].loc[df['evap_rate_scale2']>5e-8]=np.nan
df['evap_rate_scale2'].loc[(df['date_time'] < '2019-07-15 12:00:00')] = np.nan
df['evap_rate_scale1']=df['evap_rate_scale1'].fillna(method='ffill')
df['evap_rate_scale2']=df['evap_rate_scale2'].fillna(method='bfill')

#find the index of the date_time when surface emerged (supernatant water disappeared)
dry_index_1 = df['date_time'].loc[df['date_time']==time_surface_emerge_1].index[0]
dry_index_2 = df['date_time'].loc[df['date_time']==time_surface_emerge_2].index[0]
#the evaporation of supernatant water needs to be excluded when calculating degree of saturation
df['sat_scale1']=(df['cum_evap_scale1'].iloc[-1]-df['cum_evap_scale1'])/(df['cum_evap_scale1'].iloc[-1]-df['cum_evap_scale1'].iloc[dry_index_1])
df['sat_scale2']=(df['cum_evap_scale2'].iloc[-1]-df['cum_evap_scale2'])/(df['cum_evap_scale2'].iloc[-1]-df['cum_evap_scale2'].iloc[dry_index_2])
df['sat_scale1']= (df['sat_scale1']-1)*(1-moist_minimum)+1
df['sat_scale2']= (df['sat_scale2']-1)*(1-moist_minimum)+1
   
df['sat_scale1'].loc[df['sat_scale1']>1]=1
df['sat_scale2'].loc[df['sat_scale2']>1]=1

df['suc_scale1']=constants.swcc_reverse_fredlund_xing_1994(nf=0.35,mf=0.145,af=23,vwc=df.sat_scale1*df.por,por=0.55)
df['suc_scale2']=constants.swcc_reverse_fredlund_xing_1994(nf=0.45,mf=0.19,af=11.3,vwc=df.sat_scale2*df.por,por=0.55)
#Teros-12 Manual: http://publications.metergroup.com/Manuals/20587_TEROS11-12_Manual_Web.pdf
#Calculate Dielectric permeability, VMC, Degree of Saturation from Raw readings
#For mineral soils, use the following
df['VMC1']=3.879*1e-4*df['raw1']-0.6956
df['VMC2']=3.879*1e-4*df['raw2']-0.6956
df['VMC3']=3.879*1e-4*df['raw3']-0.6956
df['VMC4']=3.879*1e-4*df['raw4']-0.6956
df['VMC5']=3.879*1e-4*df['raw5']-0.6956
df['VMC6']=3.879*1e-4*df['raw6']-0.6956
#For soilless media, use the following:
#df['VMC1']=6.771*1e-10*(df['raw1']**3)-5.105*1e-6*(df['raw1']**2)+1.302*1e-2*df['raw1']-10.848
#df['VMC2']=6.771*1e-10*(df['raw2']**3)-5.105*1e-6*(df['raw2']**2)+1.302*1e-2*df['raw2']-10.848
#df['VMC3']=6.771*1e-10*(df['raw3']**3)-5.105*1e-6*(df['raw3']**2)+1.302*1e-2*df['raw3']-10.848
#df['VMC4']=6.771*1e-10*(df['raw4']**3)-5.105*1e-6*(df['raw4']**2)+1.302*1e-2*df['raw4']-10.848
#df['VMC5']=6.771*1e-10*(df['raw5']**3)-5.105*1e-6*(df['raw5']**2)+1.302*1e-2*df['raw5']-10.848
#df['VMC6']=6.771*1e-10*(df['raw6']**3)-5.105*1e-6*(df['raw6']**2)+1.302*1e-2*df['raw6']-10.848

#Dielectric permeability
df['dp1']=(2.887*1e-9*(df['raw1']**3)-2.080*1e-5*(df['raw1']**2)+5.276*1e-2*df['raw1']-43.39)**2
df['dp2']=(2.887*1e-9*(df['raw2']**3)-2.080*1e-5*(df['raw2']**2)+5.276*1e-2*df['raw2']-43.39)**2
df['dp3']=(2.887*1e-9*(df['raw3']**3)-2.080*1e-5*(df['raw3']**2)+5.276*1e-2*df['raw3']-43.39)**2
df['dp4']=(2.887*1e-9*(df['raw4']**3)-2.080*1e-5*(df['raw4']**2)+5.276*1e-2*df['raw4']-43.39)**2
df['dp5']=(2.887*1e-9*(df['raw5']**3)-2.080*1e-5*(df['raw5']**2)+5.276*1e-2*df['raw5']-43.39)**2
df['dp6']=(2.887*1e-9*(df['raw6']**3)-2.080*1e-5*(df['raw6']**2)+5.276*1e-2*df['raw6']-43.39)**2

#Degree of Saturation (calculated from VWC)
df['DoS_1']=df['VMC1']/df.por
df['DoS_2']=df['VMC2']/df.por
df['DoS_3']=df['VMC3']/df.por
df['DoS_4']=df['VMC4']/df.por
df['DoS_5']=df['VMC5']/df.por
df['DoS_6']=df['VMC6']/df.por

#df['DoS_1'].loc[df['DoS_1']>1]=1
#df['DoS_2'].loc[df['DoS_2']>1]=1
#df['DoS_3'].loc[df['DoS_3']>1]=1
#df['DoS_4'].loc[df['DoS_4']>1]=1
#df['DoS_5'].loc[df['DoS_5']>1]=1
#df['DoS_6'].loc[df['DoS_6']>1]=1
"""---------------------------------Plots-----------------------------------"""
#Overall styles
params = {'legend.fontsize': 4,
          'figure.figsize': (10, 5),
          'axes.labelsize': 11,
          'axes.titlesize':'11',
          'xtick.labelsize':'11',
          'ytick.labelsize':'11',
          'font.weight':'bold',
          'font.sans-serif':'Arial',
          'axes.labelweight':'bold',
          'lines.linewidth':2}

pylab.rcParams.update(params)

lw=2
ms=6
mew=2
grid_width=2
y_fontsize=11

fig1, ax1 = plt.subplots(5,sharex=True,figsize=(9,9))
fig2, ax2 = plt.subplots(5,sharex=True,figsize=(9,9))
#fig1.subplots_adjust(hspace=.10)
fig1.subplots_adjust(left=0.15, right=0.79, top=0.97, bottom=0.05)
fig2.subplots_adjust(left=0.15, right=0.79, top=0.97, bottom=0.05)

for i in ax1:
  for axis in ['top','bottom','left','right']:
    i.spines[axis].set_linewidth(2)
    
for i in ax2:
  for axis in ['top','bottom','left','right']:
    i.spines[axis].set_linewidth(2)

df['date_time']=pd.to_datetime(df['date_time'], format='%Y/%m/%d %H:%M:%S')
"""-----------------------------Plot Basin 1--------------------------------"""
ax1[0].plot(df['date_time'], df.cum_evap_scale1*constants.m2mm, '-',color='brown'  ,markersize=ms,markeredgewidth=mew, markeredgecolor='brown'  ,label='Basin 1 (Gold Tailings)',markevery=1)
ax1[1].plot(df['date_time'], df.evap_rate_scale1*constants.ms2mmday,'-',color='orange'  ,markersize=ms,markeredgewidth=mew,markeredgecolor='orange',label='Basin 1 (Gold Tailings)',markevery=1)
ax1[2].plot(df['date_time'], df.sat_scale1,'-',color='purple',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='purple',label='Calculated by scale reading')
ax1[2].plot(df['date_time'], df.DoS_1,'-',color='r',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Calculated by Teros 1 raw reading')
ax1[2].plot(df['date_time'], df.DoS_2,'-',color='g',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='Calculated by Teros 2 raw reading')
ax1[2].plot(df['date_time'], df.DoS_3,'-',color='c',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='Calculated by Teros 3 raw reading')
ax1[3].plot(df['date_time'], df.ec1,'-',color='r',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Teros 1 direct reading')
ax1[3].plot(df['date_time'], df.ec2,'-',color='g',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='Teros 2 direct reading')
ax1[3].plot(df['date_time'], df.ec3,'-',color='c',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='Teros 3 direct reading')
ax1[4].semilogy(df['date_time'], df.suction1,'-',color='r',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Suction 1 (Basin 1)')
ax1[4].semilogy(df['date_time'], df.suction2,'-',color='g',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='Suction 2 (Basin 1)')
ax1[4].semilogy(df['date_time'], df.suction3,'-',color='c',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='Suction 3 (Basin 1)')
ax1[4].semilogy(df['date_time'], df.suction4,'-',color='m',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='Suction 4 (Basin 1)')
ax1[4].semilogy(df['date_time'], df.suction5,'-',color='y',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='y',label='Suction 5 (Basin 1)')
ax1[4].semilogy(df['date_time'], df.suc_scale1,'-',color='b',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='b',label='Scale 1 SWCC')
#Plot settings
#Grids
ax1[0].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
ax1[1].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
ax1[2].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
ax1[3].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
ax1[4].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
#Labels
ax1[4].set_xlabel('DATE', fontsize=y_fontsize,labelpad=3)
ax1[0].set_ylabel('CUMULATIVE\nEVAPORATION\n (mm)', fontsize=y_fontsize, labelpad=20)
ax1[1].set_ylabel('EVAPORATION\nRATE\n(mm/Day)', fontsize=y_fontsize, labelpad=20)
ax1[2].set_ylabel('DEGREE OF\nSATURATION', fontsize=y_fontsize, labelpad=20)
ax1[3].set_ylabel('ELECTRICAL\nCONDUCTIVITY\n (\u03BCS/cm)', fontsize=y_fontsize, labelpad=20)
ax1[4].set_ylabel('SUCTION\n(kPa)', fontsize=y_fontsize, labelpad=20)
#Axis limits
ax1[0].set_ylim([-0.5,40])
ax1[1].set_ylim([-0.2,7])
ax1[2].set_ylim([-0.2,1.5])
ax1[3].set_ylim([0,1100])
ax1[4].set_ylim([1,2.5e6])
#Legends
ax1[0].legend(bbox_to_anchor=(1.07, 0.5 ), loc='center', borderaxespad=0.,fontsize=9,handletextpad=0.03,labelspacing=0.02,ncol=1,columnspacing=0.4)
ax1[1].legend(bbox_to_anchor=(1.07, 0.5 ), loc='center', borderaxespad=0.,fontsize=9,handletextpad=0.03,labelspacing=0.02,ncol=1,columnspacing=0.4)
ax1[2].legend(bbox_to_anchor=(1.07, 0.5 ), loc='center', borderaxespad=0.,fontsize=9,handletextpad=0.03,labelspacing=0.02,ncol=1,columnspacing=0.4)
ax1[3].legend(bbox_to_anchor=(1.07, 0.5 ), loc='center', borderaxespad=0.,fontsize=9,handletextpad=0.03,labelspacing=0.02,ncol=1,columnspacing=0.4)
ax1[4].legend(bbox_to_anchor=(1.07, 0.5 ), loc='center', borderaxespad=0.,fontsize=9,handletextpad=0.03,labelspacing=0.02,ncol=1,columnspacing=0.4)

"""-----------------------------Plot Basin 2--------------------------------"""
ax2[0].plot(df['date_time'], df.cum_evap_scale2*constants.m2mm, '-',color='brown',markersize=ms,markeredgewidth=mew, markeredgecolor='brown',label='Basin 2 (Red Mud)',markevery=2)
ax2[1].plot(df['date_time'], df.evap_rate_scale2*constants.ms2mmday,'-',color='orange',markersize=ms,markeredgewidth=mew, markeredgecolor='orange',label='Basin 2 (Red Mud)',markevery=2)
ax2[2].plot(df['date_time'], df.sat_scale1,'-',color='purple',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='purple',label='Calculated by scale reading')
ax2[2].plot(df['date_time'], df.DoS_4,'-',color='r',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Calculated by Teros 4 raw reading')
ax2[2].plot(df['date_time'], df.DoS_5,'-',color='g',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='Calculated by Teros 5 raw reading')
ax2[2].plot(df['date_time'], df.DoS_6,'-',color='c',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='Calculated by Teros 6 raw reading')
ax2[3].plot(df['date_time'], df.ec4,'-',color='r',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Teros 4 direct reading')
ax2[3].plot(df['date_time'], df.ec5,'-',color='g',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='Teros 5 direct reading')
ax2[3].plot(df['date_time'], df.ec6,'-',color='c',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='Teros 6 direct reading')
ax2[4].semilogy(df['date_time'], df.suction6,'-',color='r',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Suction 6 (Basin 2)')
ax2[4].semilogy(df['date_time'], df.suction7,'-',color='g',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='Suction 7 (Basin 2)')
ax2[4].semilogy(df['date_time'], df.suction8,'-',color='c',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='Suction 8 (Basin 2)')
#ax2[4].semilogy(df['date_time'], df.suction9,'-',color='m',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='Suction 9 (Basin 2)')
#ax2[4].semilogy(df['date_time'], df.suction10,'-',color='y',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='y',label='Suction 10 (Basin 2)')
ax2[4].semilogy(df['date_time'], df.suc_scale2,'-',color='b',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='b',label='Scale 2 SWCC')
#Plot settings
#Grids
ax2[0].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
ax2[1].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
ax2[2].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
ax2[3].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
ax2[4].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
#Labels
ax2[4].set_xlabel('DATE', fontsize=y_fontsize,labelpad=3)
ax2[0].set_ylabel('CUMULATIVE\nEVAPORATION\n (mm)', fontsize=y_fontsize, labelpad=20)
ax2[1].set_ylabel('EVAPORATION\nRATE\n(mm/Day)', fontsize=y_fontsize, labelpad=20)
ax2[2].set_ylabel('DEGREE OF\nSATURATION', fontsize=y_fontsize, labelpad=20)
ax2[3].set_ylabel('ELECTRICAL\nCONDUCTIVITY\n (\u03BCS/cm)', fontsize=y_fontsize, labelpad=20)
ax2[4].set_ylabel('SUCTION\n(kPa)', fontsize=y_fontsize, labelpad=20)
#Axis Limits
ax2[0].set_ylim([-0.5,40])
ax2[1].set_ylim([-0.2,7])
ax2[2].set_ylim([-0.2,1.5])
ax2[3].set_ylim([0,20000])
ax2[4].set_ylim([1,2.5e6])
#Legends
ax2[0].legend(bbox_to_anchor=(1.07, 0.5 ), loc='center', borderaxespad=0.,fontsize=9,handletextpad=0.03,labelspacing=0.02,ncol=1,columnspacing=0.4)
ax2[1].legend(bbox_to_anchor=(1.07, 0.5 ), loc='center', borderaxespad=0.,fontsize=9,handletextpad=0.03,labelspacing=0.02,ncol=1,columnspacing=0.4)
ax2[2].legend(bbox_to_anchor=(1.07, 0.5 ), loc='center', borderaxespad=0.,fontsize=9,handletextpad=0.03,labelspacing=0.02,ncol=1,columnspacing=0.4)
ax2[3].legend(bbox_to_anchor=(1.07, 0.5 ), loc='center', borderaxespad=0.,fontsize=9,handletextpad=0.03,labelspacing=0.02,ncol=1,columnspacing=0.4)
ax2[4].legend(bbox_to_anchor=(1.07, 0.5 ), loc='center', borderaxespad=0.,fontsize=9,handletextpad=0.03,labelspacing=0.02,ncol=1,columnspacing=0.4)

"""------------------------------Video images-------------------------------"""
#def get_date_taken(path):
#    return datetime.strptime(Image.open(path)._getexif()[36867],'%Y:%m:%d %H:%M:%S')
#Image.open(path)._getexif()[36867] will be 'NoneType' if the image does not
#have exif data (if you crop images and rename them, this will happen)    
#path in windows is like: 'E:/photo_basin_1\\2019_07_17_03_43_wwl_cali.jpg'
def get_date_taken(path):
    return datetime.strptime(path.split("\\")[-1][:16],'%Y_%m_%d_%H_%M')

lw=2
ms=2
mew=3
grid_width=2
y_fontsize=12

params = {'legend.fontsize': 4,
          'figure.figsize': (10, 5),
          'axes.labelsize': 15,
          'axes.titlesize':'50',
          'xtick.labelsize':'15',
          'ytick.labelsize':'15',
          'font.weight':'bold',
          'font.sans-serif':'Arial',
          'axes.labelweight':'bold',
          'lines.linewidth':2,
          'title.fontweight':'bold'}

path_im_basin_1='E:/wwl_cali/photo_basin_1/'    
path_im_basin_2='E:/wwl_cali/photo_basin_2/' 
files_basin_1 = list(filter(os.path.isfile, glob.glob(path_im_basin_1 + "*.jpg")))
files_basin_2 = list(filter(os.path.isfile, glob.glob(path_im_basin_2 + "*.jpg")))
files_basin_1.sort(key=lambda x: get_date_taken(x))
files_basin_2.sort(key=lambda x: get_date_taken(x))
files_name_basin_1 = []
files_name_basin_2 = []
for i in files_basin_1:
    files_name_basin_1.append(i.split('\\')[-1])
for i in files_basin_2:
    files_name_basin_2.append(i.split('\\')[-1])
files_name_basin_1.sort()
files_name_basin_2.sort()

photo_taken_time_basin_1=[i[:16] for i in files_name_basin_1]
photo_taken_time_basin_2=[i[:16] for i in files_name_basin_1]
date=[datetime.strptime(x,'%Y_%m_%d_%H_%M') for x in photo_taken_time_basin_1]
date=[datetime.strptime(x,'%Y_%m_%d_%H_%M') for x in photo_taken_time_basin_2]

for ii in range(len(date)):
    im_path_basin_1 = path_im_basin_1+files_name_basin_1[ii]
    im_path_basin_2 = path_im_basin_2+files_name_basin_2[ii]
    im_basin_1=image.imread(im_path_basin_1) 
    im_basin_2=image.imread(im_path_basin_2) 

    im_time=date[ii]
    idx_im, min_value = min(enumerate( abs(df['date_time']-im_time)), key=operator.itemgetter(1))

#-------------------------Basin 1 Video images---------------------------------
    fig1 = plt.figure(num='Basin 1',figsize=(18,9))
    ax1 = [[] for i in range(6)]
    ax1[0] = plt.subplot2grid((5, 2), (0, 0), colspan=1)
    ax1[1] = plt.subplot2grid((5, 2), (1, 0), colspan=1)
    ax1[2] = plt.subplot2grid((5, 2), (2, 0), colspan=1)
    ax1[3] = plt.subplot2grid((5, 2), (3, 0), colspan=1)
    ax1[4] = plt.subplot2grid((5, 2), (4, 0), colspan=1)

    fig1.subplots_adjust(hspace=.20)
    fig1.subplots_adjust(left=0.07, right=0.93, top=0.97, bottom=0.07)

    ax_img_basin_1 = plt.subplot2grid((3, 3), (0,2))
    ax_img_basin_1.set_position([0.52,0.45,0.43,0.5])

    ax1[0].plot(df.time_days[:idx_im], df.cum_evap_scale1[:idx_im]*constants.m2mm,'-',color='brown'  ,markersize=ms,markeredgewidth=mew, markeredgecolor='brown'  ,label='Basin 1 (Gold Tailings)',markevery=2)
    ax1[1].plot(df.time_days[:idx_im], df.evap_rate_scale1[:idx_im]*constants.ms2mmday,'-',color='orange'  ,markersize=ms,markeredgewidth=mew, markeredgecolor='orange'  ,label='Basin 1 (Gold Tailings)',markevery=2)
    ax1[2].plot(df.time_days[:idx_im], df.sat_scale1[:idx_im],'-',color='purple',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='purple',label='Calculated by scale reading',markevery=2)
    ax1[2].plot(df.time_days[:idx_im], df.DoS_1[:idx_im],'-',color='r',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Calculated by Teros 1 raw reading',markevery=2)
    ax1[2].plot(df.time_days[:idx_im], df.DoS_2[:idx_im],'-',color='g',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='Calculated by Teros 2 raw reading',markevery=2)
    ax1[2].plot(df.time_days[:idx_im], df.DoS_3[:idx_im],'-',color='c',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='Calculated by Teros 3 raw reading',markevery=2)    
    ax1[3].plot(df.time_days[:idx_im], df.ec1[:idx_im],'-',color='r',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Teros 1 direct reading',markevery=2)
    ax1[3].plot(df.time_days[:idx_im], df.ec2[:idx_im],'-',color='g',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='Teros 2 direct reading',markevery=2)
    ax1[3].plot(df.time_days[:idx_im], df.ec3[:idx_im],'-',color='c',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='Teros 3 direct reading',markevery=2)    
    ax1[4].semilogy(df.time_days[:idx_im], df.suction1[:idx_im],'-',color='r',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Suction 1 (Basin 1)')
    ax1[4].semilogy(df.time_days[:idx_im], df.suction2[:idx_im],'-',color='g',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='Suction 2 (Basin 1)')
    ax1[4].semilogy(df.time_days[:idx_im], df.suction3[:idx_im],'-',color='c',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='Suction 3 (Basin 1)')
    ax1[4].semilogy(df.time_days[:idx_im], df.suction4[:idx_im],'-',color='m',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='Suction 4 (Basin 1)')
    ax1[4].semilogy(df.time_days[:idx_im], df.suction5[:idx_im],'-',color='y',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='y',label='Suction 5 (Basin 1)')
    ax1[4].semilogy(df.time_days[:idx_im], df.suc_scale1[:idx_im],'-',color='b',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='b',label='Scale 1 SWCC',markevery=2)
   
    ax1[0].set_xticklabels([])
    ax1[1].set_xticklabels([])
    ax1[2].set_xticklabels([])
    ax1[3].set_xticklabels([])

    xlim=[df.time_days[0],df.time_days[len(df)-1]]

    ax1[0].set_xlim(xlim)
    ax1[1].set_xlim(xlim)
    ax1[2].set_xlim(xlim)
    ax1[3].set_xlim(xlim)
    ax1[4].set_xlim(xlim)

    ax1[4].set_xlabel('TIME (Days)', fontsize=y_fontsize,labelpad=3)     
    ax1[0].set_ylabel('CUMULATIVE\nEVAPORATION\n (mm)', fontsize=y_fontsize, labelpad=10)
    ax1[1].set_ylabel('EVAPORATION\nRATE\n(mm/Day)', fontsize=y_fontsize, labelpad=10)
    ax1[2].set_ylabel('DEGREE OF\nSATURATION', fontsize=y_fontsize, labelpad=10)
    ax1[3].set_ylabel('ELECTRICAL\nCONDUCTIVITY\n (\u03BCS/cm)', fontsize=y_fontsize, labelpad=20)
    ax1[4].set_ylabel('SUCTION\n(kPa)', fontsize=y_fontsize, labelpad=10)

    ax1[0].set_axisbelow(True)
    ax1[1].set_axisbelow(True)
    ax1[2].set_axisbelow(True)
    ax1[3].set_axisbelow(True)
    ax1[4].set_axisbelow(True)

    ax1[0].legend(bbox_to_anchor=(1.09, 0.5 ), loc='center', borderaxespad=0.,fontsize=10,handletextpad=0.03,labelspacing=0.1,ncol=1,columnspacing=0.4)
    ax1[1].legend(bbox_to_anchor=(1.09, 0.5 ), loc='center', borderaxespad=0.,fontsize=10,handletextpad=0.03,labelspacing=0.1,ncol=1,columnspacing=0.4)
    ax1[2].legend(bbox_to_anchor=(1.09, 0.5 ), loc='center', borderaxespad=0.,fontsize=10,handletextpad=0.03,labelspacing=0.1,ncol=1,columnspacing=0.4)
    ax1[3].legend(bbox_to_anchor=(1.09, 0.5 ), loc='center', borderaxespad=0.,fontsize=10,handletextpad=0.03,labelspacing=0.1,ncol=1,columnspacing=0.4)
    ax1[4].legend(bbox_to_anchor=(1.09, 0.5 ), loc='center', borderaxespad=0.,fontsize=10,handletextpad=0.03,labelspacing=0.1,ncol=1,columnspacing=0.4)
    
    ax_img_basin_1.imshow(im_basin_1)
    ax_img_basin_1.axis('off')
    ax_img_basin_1.set_title('Basin 1',x=0.05,y=0.85,fontweight='bold',fontsize=35,color='white',loc='left')
    
    ax1[0].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax1[1].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax1[2].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax1[3].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax1[4].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')

    ax1[0].set_ylim([-0.5,40])
    ax1[1].set_ylim([-0.2,7])
    ax1[2].set_ylim([-0.2,1.5])
    ax1[3].set_ylim([0,1100])
    ax1[4].set_ylim([1,2.5e6])

    plt.show(block=False)
    output_name = 'E:/wwl_cali/photo_video_basin_1/'+str(ii)+'.jpg'
    fig1.savefig(output_name, format='jpg', dpi=100)
    plt.close()

#-------------------------Basin 2 Video images---------------------------------
    fig2 = plt.figure(num='Basin 2',figsize=(18,9))
    ax2 = [[] for i in range(6)]
    ax2[0] = plt.subplot2grid((5, 2), (0, 0), colspan=1)
    ax2[1] = plt.subplot2grid((5, 2), (1, 0), colspan=1)
    ax2[2] = plt.subplot2grid((5, 2), (2, 0), colspan=1)
    ax2[3] = plt.subplot2grid((5, 2), (3, 0), colspan=1)
    ax2[4] = plt.subplot2grid((5, 2), (4, 0), colspan=1)

    fig2.subplots_adjust(hspace=.20)
    fig2.subplots_adjust(left=0.07, right=0.93, top=0.97, bottom=0.07)

    ax_img_basin_2 = plt.subplot2grid((3, 3), (0,2))
    ax_img_basin_2.set_position([0.52,0.45,0.43,0.5])
    ax2[0].plot(df.time_days[:idx_im], df.cum_evap_scale2[:idx_im]*constants.m2mm,'-',color='brown',markersize=ms,markeredgewidth=mew, markeredgecolor='brown',label='Basin 2 (Red Mud)',markevery=2)
    ax2[1].plot(df.time_days[:idx_im], df.evap_rate_scale2[:idx_im]*constants.ms2mmday,'-',color='orange',markersize=ms,markeredgewidth=mew, markeredgecolor='orange',label='Basin 2 (Red Mud)',markevery=2)
    ax2[2].plot(df.time_days[:idx_im], df.sat_scale2[:idx_im],'-',color='purple',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='purple',label='Calculated by scale reading',markevery=2)
    ax2[2].plot(df.time_days[:idx_im], df.DoS_4[:idx_im],'-',color='r',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Calculated by Teros 4 raw reading',markevery=2)
    ax2[2].plot(df.time_days[:idx_im], df.DoS_5[:idx_im],'-',color='g',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='Calculated by Teros 5 raw reading',markevery=2)
    ax2[2].plot(df.time_days[:idx_im], df.DoS_6[:idx_im],'-',color='c',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='Calculated by Teros 6 raw reading',markevery=2)    
    ax2[3].plot(df.time_days[:idx_im], df.ec4[:idx_im],'-',color='r',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Teros 4 direct reading',markevery=2)
    ax2[3].plot(df.time_days[:idx_im], df.ec5[:idx_im],'-',color='g',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='Teros 5 direct reading',markevery=2)
    ax2[3].plot(df.time_days[:idx_im], df.ec6[:idx_im],'-',color='c',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='Teros 6 direct reading',markevery=2)    
    ax2[4].semilogy(df.time_days[:idx_im], df.suction6[:idx_im],'-',color='r',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Suction 6 (Basin 2)')
    ax2[4].semilogy(df.time_days[:idx_im], df.suction7[:idx_im],'-',color='g',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='Suction 7 (Basin 2)')
    ax2[4].semilogy(df.time_days[:idx_im], df.suction8[:idx_im],'-',color='c',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='Suction 8 (Basin 2)')
#    ax2[4].semilogy(df.time_days[:idx_im], df.suction9[:idx_im],'-',color='m',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='Suction 9 (Basin 2)')
#    ax2[4].semilogy(df.time_days[:idx_im], df.suction10[:idx_im],'-',color='y',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='y',label='Suction 10 (Basin 2)')
    ax2[4].semilogy(df.time_days[:idx_im], df.suc_scale2[:idx_im],'-',color='b',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='b',label='Scale 2 SWCC',markevery=2)

    ax2[0].set_xticklabels([])
    ax2[1].set_xticklabels([])
    ax2[2].set_xticklabels([])
    ax2[3].set_xticklabels([])

    xlim=[df.time_days[0],df.time_days[len(df)-1]]

    ax2[0].set_xlim(xlim)
    ax2[1].set_xlim(xlim)
    ax2[2].set_xlim(xlim)
    ax2[3].set_xlim(xlim)
    ax2[4].set_xlim(xlim)

    ax2[4].set_xlabel('TIME (Days)', fontsize=y_fontsize,labelpad=3)    
    ax2[0].set_ylabel('CUMULATIVE\nEVAPORATION\n (mm)', fontsize=y_fontsize, labelpad=10)
    ax2[1].set_ylabel('EVAPORATION\nRATE\n(mm/Day)', fontsize=y_fontsize, labelpad=10)
    ax2[2].set_ylabel('DEGREE OF\nSATURATION', fontsize=y_fontsize, labelpad=10)
    ax2[3].set_ylabel('ELECTRICAL\nCONDUCTIVITY\n (\u03BCS/cm)', fontsize=y_fontsize, labelpad=20)
    ax2[4].set_ylabel('SUCTION\n(kPa)', fontsize=y_fontsize, labelpad=10)

    ax2[0].set_axisbelow(True)
    ax2[1].set_axisbelow(True)
    ax2[2].set_axisbelow(True)
    ax2[3].set_axisbelow(True)
    ax2[4].set_axisbelow(True)

    ax2[0].legend(bbox_to_anchor=(1.09, 0.5 ), loc='center', borderaxespad=0.,fontsize=10,handletextpad=0.03,labelspacing=0.1,ncol=1,columnspacing=0.4)
    ax2[1].legend(bbox_to_anchor=(1.09, 0.5 ), loc='center', borderaxespad=0.,fontsize=10,handletextpad=0.03,labelspacing=0.1,ncol=1,columnspacing=0.4)
    ax2[2].legend(bbox_to_anchor=(1.09, 0.5 ), loc='center', borderaxespad=0.,fontsize=10,handletextpad=0.03,labelspacing=0.1,ncol=1,columnspacing=0.4)
    ax2[3].legend(bbox_to_anchor=(1.09, 0.5 ), loc='center', borderaxespad=0.,fontsize=10,handletextpad=0.03,labelspacing=0.1,ncol=1,columnspacing=0.4)
    ax2[4].legend(bbox_to_anchor=(1.09, 0.5 ), loc='center', borderaxespad=0.,fontsize=10,handletextpad=0.03,labelspacing=0.1,ncol=1,columnspacing=0.4)
    
    ax_img_basin_2.imshow(im_basin_2)
    ax_img_basin_2.axis('off')
    ax_img_basin_2.set_title('Basin 2',x=0.05,y=0.85,fontweight='bold',fontsize=35,color='white',loc='left')
    
    ax2[0].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax2[1].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax2[2].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax2[3].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax2[4].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')

    ax2[0].set_ylim([-0.5,40])
    ax2[1].set_ylim([-0.2,7])
    ax2[2].set_ylim([-0.2,1.5])
    ax2[3].set_ylim([0,20000])
    ax2[4].set_ylim([1,2.5e6])

    plt.show(block=False)
    output_name = 'E:/wwl_cali/photo_video_basin_2/'+str(ii)+'.jpg'
    fig2.savefig(output_name, format='jpg', dpi=100)
    plt.close()
       
"""Converting images to video
1. The sequence of the images is important because the video plays images in order.
However, by default, 10.jpg will play before 2.jpg because '10' < '2' in str comparison.
Thus we need to convert them to floats and then we can sort them mathematically.
"""    
#Convert images to video for basin 1
def get_jpg_number(jpg_name):
    return float(jpg_name.split('.')[-2])

#image_folder = 'figure/basin_1'
image_folder = 'E:/wwl_cali/photo_video_basin_1'
video_name = 'E:/wwl_cali/basin_1.avi'
images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
images.sort(key=lambda x: get_jpg_number(x))
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape
video = cv2.VideoWriter(video_name, 0, 1, (width,height))

for img in images:
    video.write(cv2.imread(os.path.join(image_folder, img)))

cv2.destroyAllWindows()
video.release()
#Convert images to video for basin 2
image_folder = 'E:/wwl_cali/photo_video_basin_2'
video_name = 'E:/wwl_cali/basin_2.avi'
images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
images.sort(key=lambda x: get_jpg_number(x))
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape
video = cv2.VideoWriter(video_name, 0, 1, (width,height))

for img in images:
    video.write(cv2.imread(os.path.join(image_folder, img)))

cv2.destroyAllWindows()
video.release()


