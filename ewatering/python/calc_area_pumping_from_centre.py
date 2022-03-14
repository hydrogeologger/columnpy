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
from numpy import linspace
from numpy import meshgrid
import matplotlib.patches as mpatches

elevation_sa2_mAHD=18.29
#import DEM data by GDAL
dem  = "C:/Project/MDBA/areasWGS84.tif"
# dem  = "C:/Project/MDBA/areasWGS84.tif"
# dem  = "C:/Project/MDBA/upper_channel.tif"
# dem  = "C:/Project/MDBA/mid_size.tif"

gdal_data = gdal.Open(dem)
gdal_band = gdal_data.GetRasterBand(1)
nodataval = gdal_band.GetNoDataValue()
DEM_elevation_m_mtx = gdal_data.ReadAsArray().astype(np.float64)

# the below code only works when areas.tif is used...
cell_width_m = gdal_data.RasterXSize
cell_height_m = gdal_data.RasterYSize
gt = gdal_data.GetGeoTransform()
minx = gt[0]
miny = gt[3] + cell_width_m*gt[4] + cell_height_m*gt[5] 
maxx = gt[0] + cell_width_m*gt[1] + cell_height_m*gt[2]
maxy = gt[3] 

sp_sch.df['elevation_sa2_m']=sp_sch.df['p2_cs451']-SA2_water_depth_adjust

sp_sch.df['elevation_sa2_m'][sp_sch.df['elevation_sa2_m']<0]=0
sp_sch.df['elevation_sa2_m'][abs(sp_sch.df['elevation_sa2_m'])<0.001]=0
sp_sch.df['elevation_sa2_m'][sp_sch.df['elevation_sa2_m']>120]=np.nan


# elevation_sa2_mAHD=elev_lidar[-1]#elevation_sa2_mAHD is the sensor location
# elevation_sa2_mAHD=18.29#elevation_sa2_mAHD is the sensor location
#elevation_sa2_mAHD is the sensor location
elevation_to_sa2_m=DEM_elevation_m_mtx [:]-elevation_sa2_mAHD
area          = np.zeros(shape=(elevation_to_sa2_m[:,1].size,elevation_to_sa2_m[1,:].size))
areaTOTAL_m2     = np.zeros(sp_sch.df['elevation_sa2_m'].size)
ele_water_depth_m_mtx   = np.zeros(shape=(elevation_to_sa2_m[:,1].size,elevation_to_sa2_m[1,:].size))
volumeML      = np.zeros(shape=(elevation_to_sa2_m[:,1].size,elevation_to_sa2_m[1,:].size))
volumeTOTALML = np.zeros(shape=(sp_sch.df['elevation_sa2_m'].size))

for k in range(sp_sch.df['elevation_sa2_m'].size):
                ele_water_depth_m_mtx[:,:]  =  sp_sch.df['elevation_sa2_m'][k]-elevation_to_sa2_m[:,:]                
                ele_water_depth_m_mtx[:,:]  =  (ele_water_depth_m_mtx[:,:]>0).choose(0,ele_water_depth_m_mtx[:,:])                  
                area[:,:]                   =  area_scale*(ele_water_depth_m_mtx[:,:]>0).choose(0,4)                
                areaTOTAL_m2[k]             =  np.sum(area[:,:])       
                volumeML[:,:]               =  ele_water_depth_m_mtx[:,:]*area[:,:]/1000
                volumeTOTALML[k]            =  np.sum(volumeML[:,:])
                if 1<k<500 and sp_sch.df['elevation_sa2_m'][k]>0 and sp_sch.df['elevation_sa2_m'][k-1]<=0:
                    cut_value = k  #sa2 starts to wet  
areaTOTAL[0:cut_value]=np.linspace(0,areaTOTAL[cut_value],num=cut_value)
areaTOTAL[areaTOTAL<0]=0
volumeTOTALML[0:cut_value]=np.linspace(0,volumeTOTALML[cut_value],num=cut_value)
volumeTOTALML[volumeTOTALML<0]=0
sp_sch.df['areaTOTAL_m2']=areaTOTAL
sp_sch.df['volumeTOTAL_ML']=volumeTOTALML
df_mean= sp_sch.df.resample('D').mean() 


