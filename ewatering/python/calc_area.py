# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 15:08:17 2021

@author: s4680073
"""
import datetime
import matplotlib.pyplot as plt
from matplotlib import cm
import py_compile
import os
import sys
import json
import pandas as pd
import numpy as np
import thingsboard_to_pandas_py3
from osgeo import ogr,gdal
import ffmpeg
import constants
from scipy import signal
import matplotlib.gridspec as gridspec
elev_lidar=np.loadtxt("C:/Project/MBDA/Murtho_gps_points/SA2toSA1_Lidar.txt")[:, 1]
from numpy import linspace
from numpy import meshgrid

#elev_drone=np.loadtxt("C:/Project/MBDA/Murtho_gps_points/SA2toSA1_dron.txt")[:, 1]
#This script is used to extract GeoTIFF data(i.e. DEM) into Python for calculating the area of a bisin.
# runfile('C:/columnpy/columnpy/ewatering/python/get_data_py3.py')
#import DEM data
filename = "C:/Project/MBDA/areasWGS84.tif"
gdal_data = gdal.Open(filename)
gdal_band = gdal_data.GetRasterBand(1)
nodataval = gdal_band.GetNoDataValue()
data_array = gdal_data.ReadAsArray().astype(np.float)
width = gdal_data.RasterXSize
height = gdal_data.RasterYSize
gt = gdal_data.GetGeoTransform()
# minx = gt[0]
# miny = gt[3] + width*gt[4] + height*gt[5] 
# maxx = gt[0] + width*gt[1] + height*gt[2]
# maxy = gt[3] 
# myProj = Proj("+proj=utm +zone=54H, +south +ellps=WGS84 +datum=WGS84 +units=m +no_defs")
# lonmin, latmin = myProj(minx, miny, inverse=True)
# lonmax, latmax = myProj(maxx, maxy, inverse=True)
# x = linspace(lonmin, lonmax,num=148)
# y = linspace(latmin, latmax,num=232)
# # #data_array

# surface elevation data plot
data=np.flipud(data_array)
x = linspace(0, map.urcrnrx, data.shape[1])
y = linspace(0, map.urcrnry, data.shape[0])
xx, yy = meshgrid(x, y)
map.contourf(xx,yy,data)

#np.nan(data(data>100))
#plt.plot(tb_pandas.result_df['temp2'].index,tb_pandas.result_df['temp2']['value'])
#plt.plot(surface_water.ts,area_profile)
# sp_sch.df.loc[time_start:datetime.datetime(2021,3,17,10,0),'p2_cs451']=0
# elev_original=sp_sch.df['p2_cs451']-0.49
# elev_original=sp_sch.df['p2_cs451']-0.76
elev_original=sp_sch.df['p2_cs451']-0.76

elev_original[elev_original<0]=0

elev_original[elev_original>120]=np.nan
# fs = 100  # Sampling frequency
# fc = 1  # Cut-off frequency of the filter
# w = fc / (fs / 2) # Normalize the frequency
# b, a = signal.butter(5, w, 'low')
# elev= signal.filtfilt(b, a,elev_original)
# plot(output)
# elev_original=sp_sch.df['p3_cs451']-0.2213
# elev_original=sp_sch.df['p3_cs451']-0.05
# elev_original[elev_original<0]=0
# elev_original[elev_original>120]=np.nan
# fs = 100  # Sampling frequency
# fc = 1  # Cut-off frequency of the filter
# w = fc / (fs / 2) # Normalize the frequency
# b, a = signal.butter(5, w, 'low')
# elev= signal.filtfilt(b, a,elev_original)
# plot(output)
# sp_sch.df['recharge_mmPday_p3']=-(sp_sch.df['pond_falling_rate_cs451_3_mmPday']+sp_sch.df['pet_mmPday'])
# sp_sch.df['recharge_mmPday_p2']=-(sp_sch.df['pond_falling_rate_cs451_2_mmPday']+sp_sch.df['pet_mmPday'])

# sp_sch.df['elev']=elev_original
sp_sch.df['elev']=elev_original
time_start = np.datetime64('2021-03-16T00:00')

sp_sch.df.loc[time_start:datetime.datetime(2021,3,17,00,0),'elev']=0

elevchange=np.zeros(shape=(sp_sch.df['elev'].size))

elevchange[1:]=np.diff(sp_sch.df['elev'])/sp_input['delta_t_s']

sp_sch.df['elevchange']=elevchange

Q=np.percentile(elevchange, [25, 50, 75])
# Interquartile range (IQR)
IQR=Q[2]-Q[0]
 # outlier step
outlier_step = 1.5 * IQR            
for i in range(elevchange.size):
        if ( elevchange[i]< Q[0] - outlier_step) | (elevchange[i] > Q[2] + outlier_step):
            elevchange[i]=(elevchange[i-2]+elevchange[i+2])/2
            # print(i)

surface_water=sp_sch.df['elev']
surface_water[surface_water<=0]=0 
surface_water[surface_water>=1.5]=0 


z1=elev_lidar[-1]#z1 is the sensor location
z2=data[:]-z1
area          = np.zeros(shape=(surface_water.size,z2[:,1].size,z2[1,:].size))
areav         = np.zeros(shape=(surface_water.size,z2[:,1].size,z2[1,:].size))
depth         = np.zeros(shape=(surface_water.size,z2[:,1].size,z2[1,:].size))
depthv        = np.zeros(shape=(surface_water.size,z2[:,1].size,z2[1,:].size))
areaTOTAL     = np.zeros(shape=(surface_water.size))
volumeML      = np.zeros(shape=(surface_water.size,z2[:,1].size,z2[1,:].size))
volumeTOTALML = np.zeros(shape=(surface_water.size))
areaTOTALv    = np.zeros(shape=(surface_water.size))
surface_waterv= np.zeros(shape=(surface_water.size))
wetmap=[z2[:,1].size,z2[1,:].size]
for k in range(surface_water.size):
            if 1<k<=surface_water.size and np.abs(surface_water[k]-surface_water[k-1])<0.05 :
            # if 2<k<=surface_water.size:
                # surface_water[k]=(surface_water[k+2]+surface_water[k-2])/2
                depth[k,:,:]  =  surface_water[k]-z2[:,:]
                depth[k,:,:]  =  (depth[k,:,:]>0).choose(0,depth[k,:,:])
                depth[k,:,:]  =  (surface_water[k]>0).choose(0,depth[k,:,:])   
                area[k,:,:]   =  (depth[k,:,:]>0).choose(0,4)
                # wetmap[:,:]=(depth[k,:,:]>0).choose(0,1)
        # area[k,:,:]=(surface_water[k]>0).choose(0,area[k,:,:])
                areaTOTAL[k]=np.sum(area[k,:,:])
                areaTOTAL[k]=(areaTOTAL[k]>3000).choose(0,areaTOTAL[k])
                volumeML[k,:,:]=depth[k,:,:]*area[k,:,:]/1000
                volumeTOTALML[k]=np.sum(volumeML[k,:,:])
                # print(k)
            # volumnTOTAL[k]=(volumnTOTAL[k]==0).choose(0,volumnTOTAL[k])
#             if k==0:
#                 depthv[k,:,:]=0
#                 areav[k,:,:]=0
#                 areaTOTALv[k]=0
#                 surface_waterv[k]=0
#             else :
#                 depthv[k,:,:]=(depth[k,:,:]-depth[k-1,:,:])/sp_input['delta_t_s'] 
#                 areav[k,:,:]=(area[k,:,:]-area[k-1,:,:])/sp_input['delta_t_s']
#                 areaTOTALv[k]=(areaTOTAL[k]-areaTOTAL[k-1])/sp_input['delta_t_s']   
#                 surface_waterv[k]=(surface_water[k]-surface_water[k-1])/sp_input['delta_t_s']
# #convert depth changing rate and area changing rate to mmday and m2day
#                 areaTOTALv[np.abs(areaTOTALv)>4]=0 
#                 areaTOTALvm2day=areaTOTALv/constants.second2day
#                 surface_watervm2day=surface_waterv/constants.second2day

sp_sch.df['areaTOTAL']=areaTOTAL
sp_sch.df['volumeTOTALML']=volumeTOTALML              
# sp_sch.df['area_x']=area[:,]
# Q=np.percentile(areaTOTALv, [25, 50, 75])
# # Interquartile range (IQR)
# IQR=Q[2]-Q[0]      
# outlier_step = 1.5 * IQR
# for i in range(elevchange.size-2):
#         if ( areaTOTALv[i]< Q[0] - outlier_step) | (areaTOTALv[i] > Q[2] + outlier_step):
#             areaTOTALv[i]=(areaTOTALv[i-2]+areaTOTALv[i+2])/2
#             print(i)        
# areaTOTALv[np.abs(areaTOTALv)>4]=0 
# plt.ioff()
# for i in range(1,surface_water.size,10):
#     #plt.contour(area[i,:,:])
#     #fig1=plt.figure() 
#     #spec = gridspec.GridSpec(ncols=2, nrows=1,
#                          #width_ratios=[2, 1])
#     fig = plt.figure(figsize=(10, 5))
#     gs = gridspec.GridSpec(nrows=4, ncols=2)                     
#     # f,(a0,a1,a2) = plt.subplots(3, 1, gridspec_kw={'height_ratios': [10,2,2]},
#     #                             figsize=(10, 10))
#     levels = np.arange(0, 1.2, 0.05)
#     a0 = fig.add_subplot(gs[0, 0])
#     a0.plot(sp_sch.df['p2_cs451'].index,areaTOTAL)
#     a0.set_title('Area ($\mathregular{m^2}$)', fontsize = 10.0)
#     a0.set_yticks(range(0,40000,10000))
#     a0.set_xticklabels([])
#     a0.axvline(sp_sch.df['p2_cs451'][i:i+1].index,color='red')
#     a1 = fig.add_subplot(gs[1, 0])
#     a1.plot(sp_sch.df['elev'].index,sp_sch.df['elev'])
#     a1.axvline(sp_sch.df['p2_cs451'][i:i+1].index,color='red')
#     a1.set_title('Depth at SA2 (m)', fontsize = 10.0)
#     a1.set_xticklabels([])
#     a2 = fig.add_subplot(gs[2, 0])
#     a2.plot(sp_sch.df['elev'].index,areaTOTALvm2day)
#     a2.set_title('Area change rate ($\mathregular{m^2}$/day)', fontsize = 10.0)
#     # a2.set_yticks(range(0,1,0.5))
#     a2.set_xticklabels([])
#     a2.axvline(sp_sch.df['p2_cs451'][i:i+1].index,color='red')
#     a3 = fig.add_subplot(gs[3, 0])
#     a3.plot(sp_sch.df['elev'].index,surface_watervm2day)
#     a3.axvline(sp_sch.df['p2_cs451'][i:i+1].index,color='red')
#     a3.set_title('Depth change rate at SA2 (mm/day)', fontsize = 10.0)
#     a3.tick_params(axis='x', which='major', labelsize=10, rotation=30)
#     a3.tick_params(axis='x', which='major', labelsize=10, rotation=30)
#     a4 = fig.add_subplot(gs[:, 1])
#     z1=a4.contourf(depth[i,:,:],cmap = "jet",levels=levels)
#     a4.title.set_text('Water depth at different locations (m)')
#     plt.colorbar(z1,ax=a4)
    
#     # a2.plot(elev.index,elev)
#     # a2.axvline(sp_sch.df['p2_cs451'][i:i+1].index,color='red')
#     # a2.set_ylabel('depth at SA2 (m)', fontsize = 10.0)
#     # a2.tick_params(axis='x', which='major', labelsize=10, rotation=30)
#     #F
#     plt.tight_layout()
#     plt.savefig(f"{i:04d}.png",dpi=300)
#     plt.close()

# for i in range(1,surface_water.size,10):
#     #plt.contour(area[i,:,:])
#     #fig1=plt.figure() 
#     #plt.ion()
#     #spec = gridspec.GridSpec(ncols=2, nrows=1,
#                          #width_ratios=[2, 1])
#     f,(a0,a1,a2) = plt.subplots(3, 1, gridspec_kw={'height_ratios': [10,2,2]},
#                                 figsize=(10, 10))
#     levels = np.arange(0, 0.2, 0.01)
#     z1=a0.contourf(depthv[i,:,:],cmap = "jet",levels=levels)
#     plt.colorbar(z1,ax=a0)
#     a1.plot(elev.index,areaTOTALv)
#     a1.set_ylabel('area ($\mathregular{m^2}$)', fontsize = 10.0)
#     a1.set_yticks(range(0,1000,100))
#     a1.set_xticklabels([])
#     a1.axvline(elev[i:i+1].index,color='red')
#     a2.plot(elev.index,elevchange)
#     a2.axvline(elev[i:i+1].index,color='red')
#     a2.set_ylabel('depth at SA2 (m)', fontsize = 10.0)
#     a2.tick_params(axis='x', which='major', labelsize=10, rotation=30)
#     #F
#     plt.tight_layout()
#     plt.savefig(f"variation{i:04d}.png",dpi=300)
#     plt.close()    
#     print(i)
    
#     plt.pause(1)
# plt.colorbar()
# plt.plot(tb_pandas.result_df['p2_cs451'][198:].index,areaTOTAL)

    
#calculate recharge in ML and evaporation in ML
#evaporation = evaporation in mm cross the area
# for i in range(areaTOTAL[:,1].size)
sp_sch.df['areaTOTAL']=areaTOTAL
volumnTOTALMLv=np.zeros(volumeTOTALML.size)
volumnTOTALMLv[1:]=np.diff(volumeTOTALML)
sp_sch.df['volumeTOTALML']=volumeTOTALML
sp_sch.df['volumnTOTALMLv']=volumnTOTALMLv
df_mean= sp_sch.df.resample('D').mean() 
df_mean['evp']=df_mean['areaTOTAL']*df_mean['pet_mmPday']*constants.mm2m
sp_sch.df['evp']=areaTOTAL*sp_sch.df['pet_mmPday']*constants.mm2m
sp_sch.df['evpmega']=sp_sch.df['evp']/1000
df_mean['evpmega']=df_mean['evp']/1000

#recharge into the basin
df_mean= sp_sch.df.resample('D').mean() 
# f,(a0,a1,a2) = plt.subplots(3, 1, gridspec_kw={'height_ratios': [10,2,2]},
#                                 figsize=(10, 10))     
# f,(a0,a1,a2,a3,a4,a5) = plt.subplots(6, 1,sharex=True,constrained_layout=True,figsize=(10,8))
# # a0.set_aspect('auto')
# a0.grid(b = True, color ='grey',
#         linestyle ='-.', linewidth = 0.5,
#         alpha = 0.2)
# a1.grid(b = True, color ='grey',
#         linestyle ='-.', linewidth = 0.5,
#         alpha = 0.2)
# a2.grid(b = True, color ='grey',
#         linestyle ='-.', linewidth = 0.5,
#         alpha = 0.2)
# a3.grid(b = True, color ='grey',
#         linestyle ='-.', linewidth = 0.5,
#         alpha = 0.2)
# a4.grid(b = True, color ='grey',
#         linestyle ='-.', linewidth = 0.5,
#         alpha = 0.2)
# a5.grid(b = True, color ='grey',
#         linestyle ='-.', linewidth = 0.5,
#         alpha = 0.2)
# a0.bar(df_mean.index, df_mean['evpmega'])
# a0.set_title('Daily water loss from the basin calculated by PET (ML/day)’', fontsize = 10.0,wrap=True)
# # a0.set_yticks(range(0,500,200))
# a0.set_xticklabels([])
# a1.bar(df_mean.index, df_mean['pet_mmPday'])
# a1.set_title('Daily PET (mm/day)’', fontsize = 10.0,wrap=True)
# a1.set_xticklabels([])
# a1.set_aspect('auto')
# a2.plot(df_mean.index, df_mean['pet_mmPday'].cumsum())
# a2.set_title('cumulative ET (mm)', fontsize = 10.0,wrap=True)
# a2.set_aspect('auto')
# # a2.set_yticks(range(0,500,100))
# a3.set_xticklabels([])
# a3.plot(df_mean.index, df_mean['evpmega'].cumsum())
# a3.set_title('Cumulative water loss by ET (ML)', fontsize = 10.0,wrap=True)
# # a2.set_yticks(range(0,500,100))
# a3.set_xticklabels([])
# a3.set_aspect('auto')
# a4.plot(df_mean.index, df_mean['areaTOTAL'])
# a4.set_title('Area of basin ($\mathregular{m^2}$)', fontsize = 10.0,wrap=True)
# a4.set_xticklabels([])
# a4.set_aspect('auto')
# a5.plot(df_mean.index, df_mean['volumnTOTAL']/1000)
# # a5.plot(sp_sch.df['pumping'].index, pumpingMLday)
# a5.set_title('Volumn of surface water body (ML)', fontsize = 10.0,wrap=True)
# a5.set_aspect('auto')
# f.subplots_adjust(left=None, bottom=None, right=None, top=None,
#                 wspace=None, hspace=None)
# plt.tight_layout()


# plt.savefig("evaporation.png",dpi=300)
# fig, ax = plt.subplots(figsize=[5, 4])
# ax.plot(elev_original,areaTOTAL)
# ax.set_xlabel('depth (m)')
# ax.set_ylabel('area ($\mathregular{m^2}$)')
# plt.tight_layout()
# plt.savefig("depth_area.png",dpi=300)

# fig, ax = plt.subplots(figsize=[5, 4])
# ax.plot(elev_original,volumeTOTAL)
# ax.set_xlabel('depth (m)')
# ax.set_ylabel('volume of surface \n water body ($\mathregular{m^3}$)')
# plt.tight_layout()
# plt.savefig("depth_volume.png",dpi=300)

# #area[0:,i,j]=depth  
# #area[0:,i,j]=0
# #area=area*4
# # areaTOTAL=np.cumsum(area,axis=1)
# # area_profile=area_profile[0:,area_profile[1,0:].size-1]
# # plt.plot(surface_water.ts,area_profile)
# # surface_water.ts
# # plt.plot(surface_water['ts'],area_profile)
# # plt.plot(tb_pandas.surface_water['ser'],area_profile)
# # plt.plot(tb_pandas['surface_water']['ts'],area_profile)
# # plt.plot(tb_pandas['surface_water'].ts,area_profile)
# # plt.plot(tb_pandas['surface_water'].index,area_profile)
# # plt.plot(tb_pandas.result_df['temp2'].index,area_profile)
# # tb_pandas.result_df['temp2'].index
# # surface_water=tb_pandas.result_df['p2_cs451']['value'][3:]-0.47;
# # plt.plot(tb_pandas.result_df['surface_water'].index,area_profile)
# # tb_pandas.result_df['surface_water'].index
# # a=tb_pandas.result_df['temp2'].index
# # surface_water=tb_pandas.result_df['p2_cs451'][3:]-0.47;
# # a=tb_pandas.result_df['temp2']
# # a=tb_pandas.result_df['temp2'].index
#  f1,(a0,a1,a2) = plt.subplots(3, 1)
#  a0.plot(sp_sch.df['p2_cs451'].index,elev_original)
#  a1.plot(sp_sch.df['p2_cs451'].index,sp_sch.df['elev'])
#  a2.plot(sp_sch.df['p2_cs451'].index,sp_sch.df['pumping'])
