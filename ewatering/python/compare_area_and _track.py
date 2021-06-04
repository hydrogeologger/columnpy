# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 08:52:28 2021

@author: s4680073
"""

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from pyproj import Proj, transform
from osgeo import ogr,gdal

# map = Basemap(llcrnrlon=140.856971,llcrnrlat=-34.040833,urcrnrlon=140.859778,urcrnrlat=-34.035842,
#              resolution='i', projection='tmerc', lat_0 = -34, lon_0 = 1)
# map = Basemap(llcrnrlon=140.856971,llcrnrlat=-34.0409,urcrnrlon=140.859778,urcrnrlat=-34.035842,
#              resolution='h', projection='lcc',lat_0 = -34.04, lon_0 = 140.858)
# map = Basemap()
# m.etopo()
# plt.show()



filename = "C:/Project/MBDA/mid_size.tif"
gdal_data = gdal.Open(filename)
gdal_band = gdal_data.GetRasterBand(1)
nodataval = gdal_band.GetNoDataValue()
data_array = gdal_data.ReadAsArray().astype(np.float)
width = gdal_data.RasterXSize
height = gdal_data.RasterYSize
gt = gdal_data.GetGeoTransform()
minx = gt[0]
miny = gt[3] + width*gt[4] + height*gt[5] 
maxx = gt[0] + width*gt[1] + height*gt[2]
maxy = gt[3] 
xmid=(minx+maxx)/2
ymid=(miny+maxy)/2
# myProj = Proj("+proj=utm +zone=54H, +south +ellps=WGS84 +datum=WGS84 +units=m +no_defs")

# lonmax, latmax = myProj(maxx, maxy, inverse=True)
x = linspace(minx,maxx, num=width)
y = linspace(miny,maxy, num=height)
# #data_array
# x = linspace(0, map.urcrnrx, data.shape[1])
# y = linspace(0, map.urcrnry, data.shape[0])
map= Basemap(projection='lcc', resolution='h',
            width=width*2, height=height*2, 
            lat_0=ymid, lon_0=xmid)
x = linspace(0, map.urcrnrx, data_array.shape[1])
y = linspace(0, map.urcrnry, data_array.shape[0])
xx, yy = meshgrid(x, y)
z=area[k,:,:]
z=np.ma.masked_where(z==0,z)
map.contourf(xx,yy,z,cmap='hsv')
map.readshapefile('C:/Project/MBDA/Murtho_gps_points/shp/Current_Track__24_MAY_2021_15_36/Current_Track_24_MAY_2021_15_36-line', 'Current_Track_24_MAY_2021_15_36-line')
map.readshapefile('C:/Project/MBDA/Murtho_gps_points/shp/20-Mar-21_1600 - Copy/202103200400', '202103200400')

# map.arcgisimage(service='ESRI_Imagery_World_2D', xpixels = 1500, verbose= True)
# plt.show()
# m.etopo(scale=0.5, alpha=0.5)
