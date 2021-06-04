# -*- coding: utf-8 -*-
"""
Created on Wed May  5 09:15:23 2021

@author: s4680073
"""
import py_compile
import os
import sys
import json
import pandas as pd
import numpy as np
import matplotlib.dates as mdates
import matplotlib
from mpl_toolkits.basemap import Basemap

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
grid_width=2
y_fontsize=12
import thingsboard_to_pandas_py3
pump=pd.read_csv('C:/Project/MBDA/pump.csv')
# pump.index=pump['time']
format = '%Y.%m.%d %H:%M'
pump['date_time'] = pd.to_datetime(pump['time'], format=format)
pump=pump.set_index(pd.DatetimeIndex(pump['date_time']))
del pump['time']
del pump['date_time']
pump=pump.interpolate(method='linear')
# plt.plot(pump['meter'])
# pump=pump-pump['meter'][0]
plot_interpolate=True
sp_sch.merge_data_from_tb(
        input_time_series=pump.index, 
        input_data_series=pump['meter'], 
        output_time_series=sp_sch.df.index,key_name='pump' ,
        plot=plot_interpolate  ,coef=1.e-2,rm_nan=True)
plt.close()
sp_sch.df['pump']=sp_sch.df['pump']-sp_sch.df['pump'][0]
sp_sch.df['pumpMLPday']=np.zeros(sp_sch.df['pump'].size)
sp_sch.df['pumpMLPday'][0]  = 0
sp_sch.df['pumpMLPday'][1:] = (np.diff(sp_sch.df['pump'])/sp_input['delta_t_s']) * constants.sPday
sp_sch.df['pumpMLPday'][sp_sch.df['pumpMLPday']<0.2]=0
plt.plot(sp_sch.df['pump'])

plt.plot(sp_sch.df['pumpMLPday'])
plt.title('pumping rate (ML/day)')
plt.tight_layout()
plt.savefig("pumping rate.png",dpi=300)

sp_sch.df['pet_volume_MLPDAY']=sp_sch.df['pet_mmPday']*constants.mm2m*sp_sch.df['areaTOTAL']*constants.mmdayPms
df_mean = sp_sch.df.resample('D').mean()
# plt.plot(df_mean['pet_volume_MLPDAY'])
# plt.plot(df_mean['pet_mmPday'])
# plt.plot(df_mean['recharge_mmPday'])

a=plt.figure()

t=10000
fig = plt.figure(figsize=(12, 9))
gs = gridspec.GridSpec(nrows=3, ncols=3)                     
fig.subplots_adjust(hspace=.20)
fig.subplots_adjust(left=0.1, right=0.99, top=0.97, bottom=0.05) 
levels = np.arange(0, 1.2, 0.05)
ax0 = fig.add_subplot(gs[0, 0])
  

df_cumsum=sp_sch.df.cumsum()
df_cumsum['infiltration_ML']=sp_sch.df['pump']-sp_sch.df['volumeTOTALML']-df_cumsum['pet_volume_MLPDAY']*sp_input['delta_t_s']
ax0.plot(sp_sch.df['pump'],label='Accumulative pumped water volume (ML)')
ax0.plot(sp_sch.df['volumeTOTALML'],label='Volume of the surface water body (ML)')
ax0.plot(sp_sch.df['pump']-sp_sch.df['volumeTOTALML'],label='Accumulative pump volume minus volume of water body(ML)')
# plt.plot(sp_sch.df['volumeTOTALML'],label='Volume of water body (ML)')
ax0.plot(df_cumsum['pet_volume_MLPDAY']*sp_input['delta_t_s'],label='Accumulative PET (ML)')
ax0.plot(df_cumsum['infiltration_ML'],label='Infiltration into unsaturated zone (ML)')
ax0.set_xlim(datetime.date(2021, 3, 17), datetime.date(2021, 6, 2))
ax0.xaxis.set_major_formatter(mdates.DateFormatter('%b/%d'))
ax0.grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
ax0.set_ylabel('Water Volume (ML)', fontsize=y_fontsize, labelpad=10)
ax0.set_xlabel('Time', fontsize=y_fontsize, labelpad=10)
ax0.legend(loc='lower right')

ax1 = fig.add_subplot(gs[1, 0])
ax1.plot(sp_sch.df.index,water_depth_transducer_m_t_array)
ax1.plot(sp_sch.df.index,sp_sch.df['p2_cs451'])
ax1.grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
ax1.set_ylabel('Pond depth  by transdu. (m)', fontsize=y_fontsize, labelpad=10)
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%b/%d'))
ax1.set_xlabel('Time', fontsize=y_fontsize, labelpad=10)


# below snippet checks the surface area vs total water depth
ax2 = fig.add_subplot(gs[2, 0])
ax2.plot(water_depth_transducer_m_t_array,areaTOTAL)
ax2.grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
ax2.set_ylabel('Pond area. (m2)', fontsize=y_fontsize, labelpad=10)
ax2.set_xlabel('Pond depth (m)', fontsize=y_fontsize, labelpad=10)

ax3 = fig.add_subplot(gs[0, 1])
ax3.plot(water_depth_transducer_m_t_array,volumeTOTALML)
ax3.grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
ax3.set_ylabel('Pond Volume (ML)', fontsize=y_fontsize, labelpad=10)
ax3.set_xlabel('Pond depth (m)', fontsize=y_fontsize, labelpad=10)

ax4 = fig.add_subplot(gs[0, 2])
ax4.set_ylabel('y (m)', fontsize=y_fontsize, labelpad=10)
ax4.set_xlabel('x (m)', fontsize=y_fontsize, labelpad=10)
ax4.set_title('DEM vs walk track at 210524')
map= Basemap(projection='lcc', resolution='h',
            width=width*2, height=height*2, 
            lat_0=ymid, lon_0=xmid)
map.readshapefile('C:/Project/MBDA/Murtho_gps_points/shp/Current_Track__24_MAY_2021_15_36/Current_Track_24_MAY_2021_15_36-line', 'Current_Track_24_MAY_2021_15_36-line')
area_slice=area[t,:,:]
area_slice=np.ma.masked_where(z==0,z)
map.contourf(xx,yy,area_slice,cmap='hsv')


ax5 = fig.add_subplot(gs[1, 1])
walking_track_area_m2=pd.read_csv('C:/Project/MBDA/walkingtrackarea.csv')
# pump.index=pump['time']
format = '%Y.%m.%d %H:%M'
walking_track_area_m2['date_time'] = pd.to_datetime(walking_track_area_m2['time'], format=format)
walking_track_area_m2=walking_track_area_m2.set_index(pd.DatetimeIndex(walking_track_area_m2['date_time']))
del walking_track_area_m2['time']
del walking_track_area_m2['date_time']

for i in range(0,areaTOTAL_cases[:,1].size-1):
    ax5.plot(sp_sch.df.index,areaTOTAL_cases[i,:],label=(40+4*i)/100)
ax5.legend(loc='lower right')
ax5.plot(walking_track_area_m2.index,walking_track_area_m2,'r.')
ax5.xaxis.set_major_formatter(mdates.DateFormatter('%b/%d'))
plt.tight_layout()
fig.savefig('dashboard.jpg', format='jpg', dpi=100)

# a1.plot(sp_sch.df['elev'].index,sp_sch.df['elev'])
# a1.axvline(sp_sch.df['p2_cs451'][i:i+1].index,color='red')
# a1.set_title('ele_water_depth_m_mtx at SA2 (m)', fontsize = 10.0)
# a1.set_xticklabels([])

# a2.plot(sp_sch.df['elev'].index,areaTOTALv)
# a2.set_title('Area change rate ($\mathregular{m^2}$/day)', fontsize = 10.0)
# # a2.set_yticks(range(0,1,0.5))
# a2.set_xticklabels([])
# a2.axvline(sp_sch.df['p2_cs451'][i:i+1].index,color='red')
# a3 = fig.add_subplot(gs[3, 0])
# a3.plot(sp_sch.df['elev'].index,water_depth_transducer_m_t_array)
# a3.axvline(sp_sch.df['p2_cs451'][i:i+1].index,color='red')
# a3.set_title('ele_water_depth_m_mtx change rate at SA2 (mm/day)', fontsize = 10.0)
# a3.tick_params(axis='x', which='major', labelsize=10, rotation=30)
# a3.tick_params(axis='x', which='major', labelsize=10, rotation=30)
# a4 = fig.add_subplot(gs[:, 1])
# z1=a4.contourf(ele_water_depth_m_mtx[i,:,:],cmap = "jet",levels=levels)
# a4.title.set_text('Water ele_water_depth_m_mtx at different locations (m)')
# plt.colorbar(z1,ax=a4)
# a5 = fig.add_subplot(gs[:, 2])
# z1=a4.contourf(ele_water_depth_m_mtx[i,:,:],cmap = "jet",levels=levels)
# a4.title.set_text('Water ele_water_depth_m_mtx at different locations (m)')
# plt.colorbar(z1,ax=a4)    



# plt.set_ylabel('POTENTIAL\nEVAP.\nRATE\n(mm/Day)', fontsize=y_fontsize, labelpad=10)
# plt.grid(True)
# plt.legend()
# depthmean=np.zeros(depth[:,0,0].size)
# depthnozero=depth
# depthnozero[depthnozero==0]=np.nan
# for i in range(depth[:,0,0].size):
#     depthmean[i]=np.nanmean(depthnozero[i,:,:])
# volumemean={}
# volumemeanML=areaTOTAL*depthmean/1000
# plt.plot(volumemeanML)
# plt.plot(volumeTOTALML)