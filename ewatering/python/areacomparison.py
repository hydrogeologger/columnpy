# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 19:28:15 2021

@author: s4680073
"""
t=10080+2*24*6-5*6-4
fig, ax = plt.subplots()
# ax4 = fig.add_subplot(gs[0:2, 2])
# ax4.set_ylabel('y (m)', fontsize=y_fontsize, labelpad=10)
# ax4.set_xlabel('x (m)', fontsize=y_fontsize, labelpad=10)
# ax4.set_title('DEM vs walk track at 210321 09:00')
map= Basemap(projection='lcc', resolution='h',
            width=width*2, height=height*2, 
            lat_0=ymid, lon_0=xmid)
map.readshapefile('C:/Project/MBDA/Murtho_gps_points/shp/202105260920/aerial', '202105260920_area_from_aerial_image',color='r',linewidth=1.5)
blue_patch = mpatches.Patch(color='red', label='Water edge from aerial images')
plt.legend(handles=[blue_patch],loc='lower right',fontsize=8)
# plt.title('DEM vs result from aerial images at 26/May/2021 09:20')
area_slice=area[t,:,:]
area_slice=np.ma.masked_where(area_slice==0,area_slice)
map.contourf(xx,yy,area_slice,cmap='hsv')
plt.savefig('track_compare_202105260920.png',dpi=300)
t=10080
fig, ax = plt.subplots()
# ax4 = fig.add_subplot(gs[0:2, 2])
# ax4.set_ylabel('y (m)', fontsize=y_fontsize, labelpad=10)
# ax4.set_xlabel('x (m)', fontsize=y_fontsize, labelpad=10)
# ax4.set_title('DEM vs walk track at 210321 09:00')
map= Basemap(projection='lcc', resolution='h',
            width=width*2, height=height*2, 
            lat_0=ymid, lon_0=xmid)
map.readshapefile('C:/Project/MBDA/Murtho_gps_points/shp/202105241630/walk', '202105241630_track',linewidth=1.5)
map.readshapefile('C:/Project/MBDA/Murtho_gps_points/shp/202105241630/aerial', '202105241630_area_from_aerial_image',color='r',linewidth=1.5)
red_patch = mpatches.Patch(color='black', label='Water edge from walking track')
blue_patch = mpatches.Patch(color='red', label='Water edge from aerial images')
plt.legend(handles=[red_patch, blue_patch],loc='lower right',fontsize=8)
# plt.title('DEM vs walk track at 24/May/2021 16:30')
area_slice=area[t,:,:]
area_slice=np.ma.masked_where(area_slice==0,area_slice)
map.contourf(xx,yy,area_slice,cmap='hsv')
plt.savefig('track_compare_202105241630.png',dpi=300)
t=804
fig, ax = plt.subplots()
# ax4 = fig.add_subplot(gs[0:2, 2])
# ax4.set_ylabel('y (m)', fontsize=y_fontsize, labelpad=10)
# ax4.set_xlabel('x (m)', fontsize=y_fontsize, labelpad=10)
# ax4.set_title('DEM vs walk track at 210524 16:30')
map= Basemap(projection='lcc', resolution='h',
            width=width*2, height=height*2, 
            lat_0=ymid, lon_0=xmid)
map.readshapefile('C:/Project/MBDA/Murtho_gps_points/shp/202103210900/walk', '202103210900_track',linewidth=1.5)
map.readshapefile('C:/Project/MBDA/Murtho_gps_points/shp/202103210900/aerial_line', '202103210900_area_from_aerial_image',color='r',linewidth=1.5)
red_patch = mpatches.Patch(color='black', label='Water edge from walking track')
blue_patch = mpatches.Patch(color='red', label='Water edge from aerial images')
plt.legend(handles=[red_patch, blue_patch],loc='lower right',fontsize=8)
area_slice=area[t,:,:]
area_slice=np.ma.masked_where(area_slice==0,area_slice)
# plt.title('DEM vs walk track at 21/May/2021 09:00')
map.contourf(xx,yy,area_slice,cmap='hsv')
plt.savefig('track_compare_202103210900.png',dpi=300)


t=726
fig, ax = plt.subplots()
map= Basemap(projection='lcc', resolution='h',
            width=width*2, height=height*2, 
            lat_0=ymid, lon_0=xmid)
map.readshapefile('C:/Project/MBDA/Murtho_gps_points/shp/202103201600/walk', '202103201600_track',linewidth=1.5)
map.readshapefile('C:/Project/MBDA/Murtho_gps_points/shp/202103201600/aerial', '202103201600_aerial',color='r',linewidth=1.5)
red_patch = mpatches.Patch(color='black', label='Water edge from walking track')
blue_patch = mpatches.Patch(color='red', label='Water edge from aerial images')
plt.legend(handles=[red_patch, blue_patch],loc='lower right',fontsize=8)
area_slice=area[t,:,:]
area_slice=np.ma.masked_where(area_slice==0,area_slice)
map.contourf(xx,yy,area_slice,cmap='hsv')
# plt.title('DEM vs walk track at 20/Mar/2021 16:00')
plt.savefig('track_compare_202103201600.png',dpi=300)


t=555
fig, ax = plt.subplots()
map= Basemap(projection='lcc', resolution='h',
            width=width*2, height=height*2, 
            lat_0=ymid, lon_0=xmid)
map.readshapefile('C:/Project/MBDA/Murtho_gps_points/shp/202103191130/walk', '202103191130_track',linewidth=1.5)
map.readshapefile('C:/Project/MBDA/Murtho_gps_points/shp/202103191130/aerial', '202103191130_aerial',color='r',linewidth=1.5)
red_patch = mpatches.Patch(color='black', label='Water edge from walking track')
blue_patch = mpatches.Patch(color='red', label='Water edge from aerial images')
plt.legend(handles=[red_patch, blue_patch],loc='lower right',fontsize=8)
area_slice=area[t,:,:]
area_slice=np.ma.masked_where(area_slice==0,area_slice)
map.contourf(xx,yy,area_slice,cmap='hsv')
# plt.title('DEM vs walk track at 19/Mar/21 11:30')
plt.savefig('track_compare_202103191130.png',dpi=300)


t=438
fig, ax = plt.subplots()
map= Basemap(projection='lcc', resolution='h',
            width=width*2, height=height*2, 
            lat_0=ymid, lon_0=xmid)
map.readshapefile('C:/Project/MBDA/Murtho_gps_points/shp/202103181600/walk', '202103181600_track',linewidth=1.5)
map.readshapefile('C:/Project/MBDA/Murtho_gps_points/shp/202103181600/aerial', '202103181600_aerial',color='r',linewidth=1.5)
red_patch = mpatches.Patch(color='black', label='Water edge from walking track')
blue_patch = mpatches.Patch(color='red', label='Water edge from aerial images')
plt.legend(handles=[red_patch, blue_patch],loc='lower right',fontsize=8)
area_slice=area[t,:,:]
area_slice=np.ma.masked_where(area_slice==0,area_slice)
map.contourf(xx,yy,area_slice,cmap='hsv')
# plt.title('DEM vs walk track at 18/Mar/21 16:00')
plt.savefig('track_compare_202103181600.png',dpi=300)

t=258
fig, ax = plt.subplots()
map= Basemap(projection='lcc', resolution='h',
            width=width*2, height=height*2, 
            lat_0=ymid, lon_0=xmid)
map.readshapefile('C:/Project/MBDA/Murtho_gps_points/shp/202103171000/walk', '202103171000_track',linewidth=1.5)
map.readshapefile('C:/Project/MBDA/Murtho_gps_points/shp/202103171000/aerial', '202103171000_aerial',color='r',linewidth=1.5)
red_patch = mpatches.Patch(color='black', label='Water edge from walking track')
blue_patch = mpatches.Patch(color='red', label='Water edge from aerial images')
plt.legend(handles=[red_patch, blue_patch],loc='lower right',fontsize=8)
area_slice=area[t,:,:]
area_slice=np.ma.masked_where(area_slice==0,area_slice)
map.contourf(xx,yy,area_slice,cmap='hsv')
# plt.title('DEM vs walk track at 17/Mar/21 10:00')
plt.savefig('track_compare_202103171000.png',dpi=300)

