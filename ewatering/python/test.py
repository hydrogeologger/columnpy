# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 14:38:55 2021

@author: s4680073
"""
j=0
areaTOTAL_cases=np.zeros((len(range(40,80,4)),water_depth_transducer_m_t_array.size))
z1=elev_lidar[-1]#z1 is the sensor location
z2=data[:]-z1
time_start = np.datetime64('2021-03-16T00:00')
sp_sch.df.loc[time_start:datetime.datetime(2021,3,17,00,0),'elev']=0        
for ii in range(40,80,4):
    for k in range(water_depth_transducer_m_t_array.size):
        adjust=ii*0.01
        surface_water=sp_sch.df['p2_cs451']-adjust
        np.where(surface_water>0,surface_water,0)
        # elev_original[elev_original>120]=np.nan
        # sp_sch.df['elev']=elev_original 
        # # Q=np.percentile(elevchange, [25, 50, 75])
        # # # Interquartile range (IQR)
        # # IQR=Q[2]-Q[0]
        # #  # outlier step
        # # outlier_step = 1.5 * IQR            
        # # # for i in range(elevchange.size):
        # # #     if ( elevchange[i]< Q[0] - outlier_step) | (elevchange[i] > Q[2] + outlier_step):
        # # #         elevchange[i]=(elevchange[i-2]+elevchange[i+2])/2
        # #         # print(i)
        # surface_water=sp_sch.df['elev']
        # surface_water[surface_water<=0]=0 
        # surface_water[surface_water>=1.5]=0 
        area_case=np.zeros(shape=(z2[:,1].size,z2[1,:].size))
        depth=np.zeros(shape=(z2[:,1].size,z2[1,:].size))
        # volumeML=np.zeros(shape=(z2[:,1].size,z2[1,:].size))
        # if 1<k<=surface_water.size and np.abs(surface_water[k]-surface_water[k-1])<0.05 :
                # if 2<k<=surface_water.size:
                    # surface_water[k]=(surface_water[k+2]+surface_water[k-2])/2
    # for k in range(water_depth_transducer_m_t_array.size):
        depth[:,:]=surface_water[k]-z2[:,:]
        np.where(depth>0,depth,0)
        # depth[:,:]=(surface_water[k]>0).choose(0,depth[:,:])   
        area_case[:,:]=(depth[:,:]>0).choose(0,4)
        # wetmap[:,:]=(depth[k,:,:]>0).choose(0,1)
# area[k,:,:]=(surface_water[k]>0).choose(0,area[k,:,:])
        areaTOTAL_cases[j,k]=np.sum(area_case[:,:])
        np.where(areaTOTAL_cases>3000,areaTOTAL_cases,0)
                    # volumeML[:,:]=depth[:,:]*area[:,:]/1000
                    # volumeTOTALML=np.sum(volumeML[:,:])
                    # map.contourf(xx,yy,np.ma.masked_where(area==0,area),cmap='jet')
                    # map.readshapefile('C:/Project/MBDA/Murtho_gps_points/shp/Current_Track__24_MAY_2021_15_36/Current_Track_24_MAY_2021_15_36-line', 'Current_Track_24_MAY_2021_15_36-line')
                    # plt.savefig(f"{ii:02d}.png",dpi=300)
                    # plt.close()
    j=j+1
    print(ii)

    