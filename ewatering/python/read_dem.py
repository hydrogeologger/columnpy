# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 10:59:13 2022

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
dem  = "areasWGS84.tif"


gdal_data           = gdal.Open(dem)
gdal_band           = gdal_data.GetRasterBand(1)
nodataval           = gdal_band.GetNoDataValue()
DEM_elevation_m_mtx = gdal_data.ReadAsArray().astype(np.float64)
DEM_elevation_m_mtx[DEM_elevation_m_mtx<-0]=np.nan