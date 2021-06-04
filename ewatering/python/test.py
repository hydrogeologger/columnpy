# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 14:38:55 2021

@author: s4680073
"""
elev_original=sp_sch.df['p2_cs451']-adjust
elev_original[elev_original<0]=0
elev_original[elev_original>120]=np.nan
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
area=np.zeros(shape=(z2[:,1].size,z2[1,:].size))
depth=np.zeros(shape=(z2[:,1].size,z2[1,:].size))
areaTOTAL=0
volumeML=np.zeros(shape=(z2[:,1].size,z2[1,:].size))
volumeTOTALML=0
if 1<k<=surface_water.size and np.abs(surface_water[k]-surface_water[k-1])<0.05 :
            # if 2<k<=surface_water.size:
                # surface_water[k]=(surface_water[k+2]+surface_water[k-2])/2
                depth[:,:]=surface_water[k]-z2[:,:]
                depth[:,:]=(depth[:,:]>0).choose(0,depth[:,:])
                depth[:,:]=(surface_water[k]>0).choose(0,depth[:,:])   
                area[:,:]=(depth[:,:]>0).choose(0,4)
                # wetmap[:,:]=(depth[k,:,:]>0).choose(0,1)
        # area[k,:,:]=(surface_water[k]>0).choose(0,area[k,:,:])
                areaTOTAL=np.sum(area[:,:])
                areaTOTAL=(areaTOTAL>3000).choose(0,areaTOTAL)
                volumeML[:,:]=depth[:,:]*area[:,:]/1000
                volumeTOTALML=np.sum(volumeML[:,:])