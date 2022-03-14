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
import matplotlib.patches as mpatches 
import matplotlib.pyplot as plt
import thingsboard_to_pandas_py3
import datetime
pump=pd.read_csv('C:/Project/MDBA/pump.csv')
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
        input_data_series=pump['sum_scaled'], 
        output_time_series=sp_sch.df.index,key_name='pump' ,
        plot=plot_interpolate  ,coef=1e-3,rm_nan=True)
sp_sch.df['pump'].loc['2021-3-18 2:00':'2021-3-19 00:00']=9.43855
sp_sch.df['pump'].loc['2021-3-20 00:00':'2021-3-20 11:30']=19.38276
sp_sch.df['pump'].loc['2021-3-24 18:00':'2021-5-25 10:00']=49.9765
sp_sch.df['pump'].loc['2021-5-26 20:00':'2022-1-18 21:30']=59.75958
sp_sch.df['pump'].loc['2022-1-27 01:20':]=98.84958
plt.plot(sp_sch.df['pump'])


# plt.close()
# sp_sch.df['pump'].loc['2021-05-29':'2022-01-17']=0
# pump_scale=1.31
sp_sch.df['pump']=(sp_sch.df['pump']-sp_sch.df['pump'][0])
sp_sch.df['pump'][sp_sch.df['pump']<=0]=0
sp_sch.df['pumpMLPday']=np.zeros(sp_sch.df['pump'].size)
sp_sch.df['pumpMLPday'][0]  = 0
sp_sch.df['pumpMLPday'][1:] = (np.diff(sp_sch.df['pump'])/sp_input['delta_t_s']) * constants.sPday
sp_sch.df['pumpMLPday'][sp_sch.df['pumpMLPday']<0.2]=0
# plt.plot(sp_sch.df['pump'])

# plt.plot(sp_sch.df['pumpMLPday'])
# plt.title('pumping rate (ML/day)')
# plt.tight_layout()
# plt.savefig("pumping rate.png",dpi=300)

sp_sch.df['pet_volume_MLPDAY']=sp_sch.df['pet_mmPday']*constants.mm2m*sp_sch.df['areaTOTAL_m2']/constants.MLPton
sp_sch.df['rainfall_volume_ML']=(sp_sch.df['rainfall']*constants.mm2m)*sp_sch.df['areaTOTAL_m2']/constants.MLPton
# sp_sch.df['volumeTOTAL_ML'].loc['2022-1-19':'2022-1-21']=sp_sch.df['volumeTOTAL_ML'].loc['2022-1-19':'2022-1-21']*1.6
df_mean = sp_sch.df.resample('D').mean()

# plt.plot(df_mean['pet_volume_MLPDAY'])
# plt.plot(df_mean['pet_mmPday'])
# plt.plot(df_mean['recharge_mmPday'])
df_cumsum=sp_sch.df.cumsum()
df_cumsum['pump']=sp_sch.df['pump']
# df_cumsum['pet_volume_MLPDAY'].loc['2021-10-21':'2022-1-18']=df_cumsum['pet_volume_MLPDAY'].loc['2021-10-20 12:00']
df_cumsum['pet_volume_ML']=np.cumsum(sp_sch.df['pet_volume_MLPDAY']*600/86400)
df_cumsum['infiltration_ML']=sp_sch.df['pump']+df_cumsum['rainfall_volume_ML']-sp_sch.df['volumeTOTAL_ML']-df_cumsum['pet_volume_ML']
df_cumsum['infiltration_ML'][df_cumsum['infiltration_ML']<0]=0
sp_sch.df['infiltration_MLPDAY']=np.append(0,np.diff(df_cumsum['infiltration_ML']))/sp_input['delta_t_s']/constants.mmdayPms

a=plt.figure()

fig = plt.figure(figsize=(12, 9))
gs = gridspec.GridSpec(nrows=3, ncols=2)                     
fig.subplots_adjust(hspace=.20)
fig.subplots_adjust(left=0.1, right=0.99, top=0.97, bottom=0.05) 
levels = np.arange(0, 1.2, 0.05)
# fig.suptitle(f'Adjustable value (m) at SA2={SA2_water_depth_adjust} pumping scale={pump_scale} \n areascale={area_scale} plant_percent={plant_percentage1*100}%',font='font_title')
ax0 = fig.add_subplot(gs[0, 0])  

ax0.plot(sp_sch.df['pump']-sp_sch.df['pump'][0],label='Cumulative pumped water volume (ML)')
ax0.plot(sp_sch.df['volumeTOTAL_ML'],label='Volume of the surface water body (ML)')
ax0.plot(sp_sch.df['pump']-sp_sch.df['pump'][0]-sp_sch.df['volumeTOTAL_ML'],label='Cumulative pump volume minus volume of water body(ML)')
# plt.plot(sp_sch.df['volumeTOTALML'],label='Volume of water body (ML)')
ax0.plot(df_cumsum['pet_volume_MLPDAY']*sp_input['delta_t_s'],label='Cumulative PET (ML)')
ax0.plot(df_cumsum['rainfall_volume_ML'],label='Cumulative rainfall volume (ML)')
ax0.plot(df_cumsum['infiltration_ML'],label='Infiltration into unsaturated zone (ML)',color='peru')
ax0.set_xlim(datetime.date(2022, 1, 18), datetime.date(2022, 3, 8))
# ax0.set_xticks([datetime.date(2021, 3, 17),
#                datetime.date(2021, 4, 28),
#                datetime.date(2021, 6, 28),
#                datetime.date(2021, 8, 28),
#                datetime.date(2021, 10,28)])
ax0.xaxis.set_major_formatter(mdates.DateFormatter('%b/%d'))
ax0.grid(True,which="both",ls=":",color = '0.5')
# ax0.tick_params(axis='both', which='minor', labelsize=6)
# plt.xticks(fontsize=tick_fontsize, rotation=0)
# plt.yticks(fontsize=tick_fontsize, rotation=0)
ax0.set_ylabel('Volume of water (ML)', labelpad=10)
ax0.set_xlabel('Time', labelpad=10)
# ax0.legend(loc=[0,1.05],)
ax0.legend(loc=[1.01,0.55])

# # ax0.set_title('Time', , labelpad=10)
# # ax0.legend(loc='lower right')
# plt.rcParams["font.family"] = "Arial"
# ax1 = fig.add_subplot(gs[1, 0])
# ax1.plot(sp_sch.df.index,water_depth_transducer_m_t_array,label='Water depth (m)')
# ax1.plot(sp_sch.df.index,sp_sch.df['p2_cs451']-0.48,'r--',label='p2_cs451 - 0.48 m')
# ax1.grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
# ax1.set_ylabel('Pond depth by transdu (m)', , labelpad=10)
# ax1.tick_params(axis='both', which='minor', labelsize=6)
# ax1.xaxis.set_major_formatter(mdates.DateFormatter('%b/%d'))
# ax1.set_xlim(datetime.date(2021, 3, 17), datetime.date(2021, 6, 5))
# ax1.set_ylim(0,1.0)
# ax1.set_xlabel('Time', , labelpad=10)
# plt.legend(loc='lower right',)
# plt.xticks(fontsize=8, rotation=0)
# plt.yticks(fontsize=8, rotation=0)
# plt.rcParams["font.family"] = "Arial"

# ax2 = fig.add_subplot(gs[1, 0])
# ax2.plot(100*(df_cumsum['pet_volume_MLPDAY']*sp_input['delta_t_s'])/sp_sch.df['pump'],label='Cumulative PET (ML)',color='red')
# ax2.plot(100*sp_sch.df['volumeTOTALML']/sp_sch.df['pump'],label='Volume of the surface water body (ML)',color='orange')
# ax2.plot(100*df_cumsum['infiltration_ML']/sp_sch.df['pump'],label='Infiltration into unsaturated zone (ML)',color='peru')
# ax2.grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
# ax2.set_ylabel('Percentage to the \npump volume', , labelpad=10)
# ax2.set_xlabel('Time', , labelpad=10)
# ax2.set_xlim(datetime.date(2021, 3, 17), datetime.date(2021, 10, 28))
# ax2.xaxis.set_major_formatter(mdates.DateFormatter('%b/%d'))
# ax2.legend(loc='upper right',)

# # plt.xticks(fontsize=tick_fontsize, rotation=0)
# # plt.yticks(fontsize=tick_fontsize, rotation=0)
# ax3 = fig.add_subplot(gs[0, 1])
# ax3.plot(water_depth_transducer_m_t_array,volumeTOTALML)
# ax3.grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
# ax3.set_ylabel('Volume of water \nin the pond (ML)', , labelpad=10)
# ax3.set_xlabel('Pond depth (m)', , labelpad=10)

# # plt.xticks(fontsize=tick_fontsize, rotation=0)
# # plt.yticks(fontsize=tick_fontsize, rotation=0)
# plt.rcParams["font.family"] = "Arial"
# # below snippet checks the surface area vs total water depth
# # ax2 = fig.add_subplot(gs[1, 0])
# # ax2.plot(water_depth_transducer_m_t_array,areaTOTAL)
# # ax2.grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
# # ax2.set_ylabel('Surface area \nof the pond ($\mathregular{m^2}$)', , labelpad=10)
# # ax2.set_xlabel('Water depth of the pond (m)', , labelpad=10)
# # # plt.xticks(fontsize=tick_fontsize, rotation=0)
# # # plt.yticks(fontsize=tick_fontsize, rotation=0)
# # ax3 = fig.add_subplot(gs[0, 1])
# # ax3.plot(water_depth_transducer_m_t_array,volumeTOTALML)
# # ax3.grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
# # ax3.set_ylabel('Volume of water \nin the pond (ML)', , labelpad=10)
# # ax3.set_xlabel('Pond depth (m)', , labelpad=10)
# # # plt.xticks(fontsize=tick_fontsize, rotation=0)
# # # plt.yticks(fontsize=tick_fontsize, rotation=0)
# # plt.rcParams["font.family"] = "Arial"
# # ax4 = fig.add_subplot(gs[0:2, 2])
# # ax4.set_ylabel('y (m)', , labelpad=10)
# # ax4.set_xlabel('x (m)', , labelpad=10)
# # ax4.set_title('DEM vs walk track at 210321')
# # map= Basemap(projection='lcc', resolution='h',
# #             width=width*2, height=height*2, 
# #             lat_0=ymid, lon_0=xmid)
# # map.readshapefile('C:/Project/MDBA/Murtho_gps_points/shp/202003210900/walk', '202003210900_track',linewidth=1.5)
# # map.readshapefile('C:/Project/MDBA/Murtho_gps_points/shp/202003210900/aerial_line', '202003210900_area_from_aerial_image',color='r',linewidth=1.5)
# # red_patch = mpatches.Patch(color='black', label='Wetting front from walking track')
# # blue_patch = mpatches.Patch(color='red', label='Wetting front from aerial images')
# # plt.legend(handles=[red_patch, blue_patch],loc='lower right',fontsize=8)
# # area_slice=area[t,:,:]
# # area_slice=np.ma.masked_where(area_slice==0,area_slice)
# # map.contourf(xx,yy,area_slice,cmap='hsv')
# # t=10080+2*24*6-5*6-4
# # # ax4 = fig.add_subplot(gs[0:2, 2])
# # # ax4.set_ylabel('y (m)', , labelpad=10)
# # # ax4.set_xlabel('x (m)', , labelpad=10)
# # # ax4.set_title('DEM vs walk track at 210321 09:00')
# # map= Basemap(projection='lcc', resolution='h',
# #             width=width*2, height=height*2, 
# #             lat_0=ymid, lon_0=xmid)
# # map.readshapefile('C:/Project/MDBA/Murtho_gps_points/shp/202105260920/aerial', '202105260920_area_from_aerial_image',color='pink',linewidth=1.5)
# # plt.legend(handles=[blue_patch],loc='lower right',fontsize=8)
# # area_slice=area[t,:,:]
# # area_slice=np.ma.masked_where(area_slice==0,area_slice)
# # map.contourf(xx,yy,area_slice)
# # t=10080
# # # ax4 = fig.add_subplot(gs[0:2, 2])
# # # ax4.set_ylabel('y (m)', , labelpad=10)
# # # ax4.set_xlabel('x (m)', , labelpad=10)
# # # ax4.set_title('DEM vs walk track at 210321 09:00')
# # map.readshapefile('C:/Project/MDBA/Murtho_gps_points/shp/202105241630/walk', '202105241630_track',linewidth=1.5)
# # map.readshapefile('C:/Project/MDBA/Murtho_gps_points/shp/202105241630/aerial', '202105241630_area_from_aerial_image',color='r',linewidth=1.5)
# # pink_patch = mpatches.Patch(color='pink', label='Water edge from aerial images 26/May/2021')
# # black_patch    = mpatches.Patch(color='black', label='Water edge from walking track 24/May/2021')
# # red_patch   = mpatches.Patch(color='red', label='Water edge from aerial images 24/May/2021')
# # green_patch  = mpatches.Patch(color='green', label='Pond water body calculated by DEM 24/May/2021')
# # blue_patch   = mpatches.Patch(color='#3A528B', label='Pond water body calculated by DEM 26/May/2021')
# # plt.legend(handles=[red_patch, black_patch, pink_patch, green_patch,blue_patch],loc=[-0.25,-0.05],fontsize=6)
# # area_slice=area[t,:,:]
# # area_slice=np.ma.masked_where(area_slice==0,area_slice)
# # map.contourf(xx,yy,area_slice,cmap='hsv')
# # plt.tight_layout()
# # fig.set_size_inches(16, 9)
# # plt.savefig('track_compare.png',dpi=300)



# ax5 = fig.add_subplot(gs[1, 1])
# walking_track_area_m2=pd.read_csv('C:/Project/MDBA/walkingtrackarea.csv')
# # pump.index=pump['time']
# format = '%Y.%m.%d %H:%M'
# walking_track_area_m2['date_time'] = pd.to_datetime(walking_track_area_m2['time'], format=format)
# walking_track_area_m2=walking_track_area_m2.set_index(pd.DatetimeIndex(walking_track_area_m2['date_time']))
# del walking_track_area_m2['time']
# del walking_track_area_m2['date_time']
# # for i in range(0,areaTOTAL_cases[:,1].size-1):
# #     ax5.plot(sp_sch.df.index,areaTOTAL_cases[i,:],label=(40+4*i)/100)
# ax5.plot(sp_sch.df.index,areaTOTAL,label='Lidar scaning')
# ax5.plot(walking_track_area_m2.index,walking_track_area_m2.GPS,'r.',label='Walking track along \nthe water edge')
# ax5.plot(walking_track_area_m2.index,walking_track_area_m2.aerial,'b.',label='Aerial images')
# ax5.legend(loc='lower right',)
# ax5.xaxis.set_major_formatter(mdates.DateFormatter('%b/%d'))
# ax5.set_xlim(datetime.date(2021, 3, 17), datetime.date(2021, 10, 28))
# ax5.set_xticks([datetime.date(2021, 3, 17),
#                 datetime.date(2021, 4, 28),
#                 datetime.date(2021, 5, 28),
#                 datetime.date(2021, 6, 28),
#                 datetime.date(2021, 7, 28),
#                 datetime.date(2021, 10, 28)])
# ax5.grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
# ax5.set_xlabel('Time', , labelpad=10)
# ax5.set_ylabel('Surface area \nof the pond ($\mathregular{m^2}$)', , labelpad=10)
# # plt.xticks(fontsize=tick_fontsize, rotation=0)
# # plt.yticks(fontsize=tick_fontsize, rotation=0)
# plt.rcParams["font.family"] = "Arial"
# ax6 = fig.add_subplot(gs[2, 1])
# # pump.index=pump['time']
# format = '%Y.%m.%d %H:%M'
# # for i in range(0,areaTOTAL_cases[:,1].size-1):
# #     ax5.plot(sp_sch.df.index,areaTOTAL_cases[i,:],label=(40+4*i)/100)

# ax6.plot(sp_sch.df.index,sp_sch.df['pond_falling_rate_cs451_3_mmPday'],label='cs451_3')
# ax6.plot(sp_sch.df.index,sp_sch.df['pond_falling_rate_cs451_2_mmPday'],label='cs451_2')
# ax6.legend(loc='upper right',)
# ax6.xaxis.set_major_formatter(mdates.DateFormatter('%b/%d'))
# ax6.set_xlim(datetime.date(2021, 3, 17), datetime.date(2021,9 , 6))
# ax6.set_xticks([datetime.date(2021, 3, 17),
#                 datetime.date(2021, 4, 28),
#                 datetime.date(2021, 5, 28),
#                 datetime.date(2021, 6, 28),
#                 datetime.date(2021, 7, 28),
#                 datetime.date(2021, 10, 28)])
# ax6.grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
# ax6.set_ylim(-30,30)
# ax6.set_xlabel('Time', , labelpad=10)
# ax6.set_ylabel('Rising rate of \nwater level \nin the pond (mm/day)', , labelpad=10)
# # ax1 = fig.add_subplot(gs[2, 2])
# # # pump.index=pump['time']
# # format = '%Y.%m.%d %H:%M'
# # # for i in range(0,areaTOTAL_cases[:,1].size-1):
# # #     ax5.plot(sp_sch.df.index,areaTOTAL_cases[i,:],label=(40+4*i)/100)
# # ax1.plot(sp_sch.df.index,sp_sch.df['pond_falling_rate_cs451_3_mmPday'],label='cs451_3 pond falling rate (mm)')
# # ax1.plot(sp_sch.df.index,sp_sch.df['pond_falling_rate_cs451_2_mmPday'],label='cs451_2 pond falling rate (mm)')
# # ax1.legend(loc='upper right')
# # ax1.xaxis.set_major_formatter(mdates.DateFormatter('%b/%d'))
# # ax1.set_xlim(datetime.date(2021, 3, 17), datetime.date(2021, 6, 5))
# # ax6.set_ylim(-0.5,0)
# # plt.xticks(fontsize=tick_fontsize, rotation=0)
# # plt.yticks(fontsize=tick_fontsize, rotation=0)
# # ax1.grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
# plt.rcParams["font.family"] = "Arial"

# ax7 = fig.add_subplot(gs[2, 0])
# # pump.index=pump['time']
# format = '%Y.%m.%d %H:%M'
# # for i in range(0,areaTOTAL_cases[:,1].size-1):
# #     ax5.plot(sp_sch.df.index,areaTOTAL_cases[i,:],label=(40+4*i)/100)

# ax7.plot(np.cumsum(sp_sch.df['rainfall']))
# ax7.xaxis.set_major_formatter(mdates.DateFormatter('%b/%d'))
# ax7.set_xlim(datetime.date(2021, 3, 17), datetime.date(2021, 10, 28))
# ax7.set_xticks([datetime.date(2021, 3, 17),
#                 datetime.date(2021, 4, 28),
#                 datetime.date(2021, 5, 28),
#                 datetime.date(2021, 6, 28),
#                 datetime.date(2021, 7, 28),
#                 datetime.date(2021, 10, 28)])
# ax7.grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
# ax7.set_ylim(0,80)
# ax7.set_xlabel('Time', , labelpad=10)
# ax7.set_ylabel('Cumulative rainfall (mm)', , labelpad=10)
# plt.rcParams['xtick.labelsize'] = label_fontsize-2
# plt.rcParams['ytick.labelsize'] = label_fontsize-2
# # plt.xticks(fontsize=tick_fontsize, rotation=0)
# # plt.yticks(fontsize=tick_fontsize, rotation=0)
# # fig.set_size_inches(20, 12)
# plt.tight_layout()
# fig.align_labels()
# fig.savefig(f'Dashboard_adjustable_value_(m)_at_SA2={SA2_water_depth_adjust}_pumping_scale={pump_scale}areascale={area_scale}_plant_percent={plant_percentage1}.jpg', format='jpg', dpi=300)

# # a2.plot(sp_sch.df['elev'].index,areaTOTALv)
# # a2.set_title('Area change rate ($\mathregular{m^2}$/day)', fontsize = 10.0)
# # # a2.set_yticks(range(0,1,0.5))
# # a2.set_xticklabels([])
# # a2.axvline(sp_sch.df['p2_cs451'][i:i+1].index,color='red')
# # a3 = fig.add_subplot(gs[3, 0])
# # a3.plot(sp_sch.df['elev'].index,water_depth_transducer_m_t_array)
# # a3.axvline(sp_sch.df['p2_cs451'][i:i+1].index,color='red')
# # a3.set_title('ele_water_depth_m_mtx change rate at SA2 (mm/day)', fontsize = 10.0)
# # a3.tick_params(axis='x', which='major', labelsize=10, rotation=30)
# # a3.tick_params(axis='x', which='major', labelsize=10, rotation=30)
# # a4 = fig.add_subplot(gs[:, 1])
# # z1=a4.contourf(ele_water_depth_m_mtx[i,:,:],cmap = "jet",levels=levels)
# # a4.title.set_text('Water ele_water_depth_m_mtx at different locations (m)')
# # plt.colorbar(z1,ax=a4)
# # a5 = fig.add_subplot(gs[:, 2])
# # z1=a4.contourf(ele_water_depth_m_mtx[i,:,:],cmap = "jet",levels=levels)
# # a4.title.set_text('Water ele_water_depth_m_mtx at different locations (m)')
# # plt.colorbar(z1,ax=a4)    



# # plt.set_ylabel('POTENTIAL\nEVAP.\nRATE\n(mm/Day)', fontsize=y_fontsize, labelpad=10)
# # plt.grid(True)
# # plt.legend()
# # depthmean=np.zeros(depth[:,0,0].size)
# # depthnozero=depth
# # depthnozero[depthnozero==0]=np.nan
# # for i in range(depth[:,0,0].size):
# #     depthmean[i]=np.nanmean(depthnozero[i,:,:])
# # volumemean={}
# # volumemeanML=areaTOTAL*depthmean/1000
# # plt.plot(volumemeanML)
# # plt.plot(volumeTOTALML)