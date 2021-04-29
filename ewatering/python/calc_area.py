# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 16:32:35 2021

@author: s4680073
"""

elev_original=sp_sch.df['p3_cs451']-0.2213
elev_original[elev_original<0]=0
elev_original[elev_original>120]=np.nan
# fs = 100  # Sampling frequency
# fc = 1  # Cut-off frequency of the filter
# w = fc / (fs / 2) # Normalize the frequency
# b, a = signal.butter(5, w, 'low')
# elev= signal.filtfilt(b, a,elev_original)
# plot(output)

# sp_sch.df['elev']=elev
sp_sch.df['elev']=elev_original
time_start = np.datetime64('2021-03-16T00:00')
sp_sch.df.loc[time_start:datetime.datetime(2021,3,17,00,0),'elev']=0
pumpingrate=6000000/constants.msPmmday
#calculte the pumping rate
pumping=np.zeros(shape=(sp_sch.df['elev'].size))
pumpingMLday=np.zeros(shape=(sp_sch.df['elev'].size))
for i in range(elev.size):
    if datetime.datetime(2021, 3, 16,15)<sp_sch.df['elev'].index[i]<=datetime.datetime(2021, 3, 17,15):
        pumping[i]=pumpingrate
    elif  datetime.datetime(2021, 3, 17,15)<sp_sch.df['elev'].index[i]<datetime.datetime(2021, 3, 24,17,0):
        if sp_sch.df['elevchange'][i]<=0:
            pumping[i]=0
        elif sp_sch.df['elevchange'][i]>0: 
            pumping[i]=pumpingrate
    else:
        pumping[i]=0
    if pumping[i]!=0:
        pumpingMLday[i]=6
    else:
        pumpingMLday[i]=0
sp_sch.df['pumping']=pumping
# sp_sch.df.loc[time_start:datetime.datetime(2021,3,17,10,0),'pumping']=0
plt.plot(sp_sch.df['pumping'])
Q=np.percentile(elevchange, [25, 50, 75])
# Interquartile range (IQR)
IQR=Q[2]-Q[0]
 # outlier step
outlier_step = 1.5 * IQR
elevchange=np.zeros(shape=(sp_sch.df['elev'].size))
elevchange[1:]=np.diff(sp_sch.df['elev'])/sp_input['delta_t_s']
sp_sch.df['elevchange']=elevchange
for i in range(elevchange.size):
        if ( elevchange[i]< Q[0] - outlier_step) | (elevchange[i] > Q[2] + outlier_step):
            elevchange[i]=(elevchange[i-2]+elevchange[i+2])/2
            # print(i)
surface_water=sp_sch.df['elev']
surface_water[surface_water<=0]=0 
surface_water[surface_water>=1.5]=0 
z1=elev_lidar[-1]#z1 is the sensor location
z2=data[:]-z1
area=np.zeros(shape=(surface_water.size,z2[:,1].size,z2[1,:].size))
areav=np.zeros(shape=(surface_water.size,z2[:,1].size,z2[1,:].size))
depth=np.zeros(shape=(surface_water.size,z2[:,1].size,z2[1,:].size))
depthv=np.zeros(shape=(surface_water.size,z2[:,1].size,z2[1,:].size))
areaTOTAL=np.zeros(shape=(surface_water.size))
volumn=np.zeros(shape=(surface_water.size,z2[:,1].size,z2[1,:].size))
volumnTOTAL=np.zeros(shape=(surface_water.size))
areaTOTALv=np.zeros(shape=(surface_water.size))
surface_waterv=np.zeros(shape=(surface_water.size))
for k in range(surface_water.size):
            if 0<k<=surface_water.size-3 and surface_water[k+1]-surface_water[k]<-0.05 and surface_water[k]-surface_water[k-1]>0.05:
                surface_water[k]=(surface_water[k+2]+surface_water[k-2])/2
                depth[k,:,:]=surface_water[k]-z2[:,:]
                depth[k,:,:]=(depth[k,:,:]>0).choose(0,depth[k,:,:])
                depth[k,:,:]=(surface_water[k]>0).choose(0,depth[k,:,:])   
                area[k,:,:]=(depth[k,:,:]>0).choose(0,4)
            # area[k,:,:]=(surface_water[k]>0).choose(0,area[k,:,:])
                areaTOTAL[k]=np.sum(area[k,:,:])
                areaTOTAL[k]=(areaTOTAL[k]>3000).choose(0,areaTOTAL[k])
                volumn[k,:,:]=depth[k,:,:]*area[k,:,:]
                volumnTOTAL[k]=np.sum(volumn[k,:,:])
            # volumnTOTAL[k]=(volumnTOTAL[k]==0).choose(0,volumnTOTAL[k])
            if k==0:
                depthv[k,:,:]=0
                areav[k,:,:]=0
                areaTOTALv[k]=0
                surface_waterv[k]=0
            else :
                depthv[k,:,:]=(depth[k,:,:]-depth[k-1,:,:])/sp_input['delta_t_s'] 
                areav[k,:,:]=(area[k,:,:]-area[k-1,:,:])/sp_input['delta_t_s']
                areaTOTALv[k]=(areaTOTAL[k]-areaTOTAL[k-1])/sp_input['delta_t_s']   
                surface_waterv[k]=(surface_water[k]-surface_water[k-1])/sp_input['delta_t_s']
#convert depth changing rate and area changing rate to mmday and m2day
                areaTOTALv[np.abs(areaTOTALv)>4]=0 
                areaTOTALvm2day=areaTOTALv/constants.second2day
                surface_watervm2day=surface_waterv/constants.second2day
# Q=np.percentile(areaTOTALv, [25, 50, 75])
# # Interquartile range (IQR)
# IQR=Q[2]-Q[0]      
# outlier_step = 1.5 * IQR
# for i in range(elevchange.size-2):
#         if ( areaTOTALv[i]< Q[0] - outlier_step) | (areaTOTALv[i] > Q[2] + outlier_step):
#             areaTOTALv[i]=(areaTOTALv[i-2]+areaTOTALv[i+2])/2
#             print(i)        
# areaTOTALv[np.abs(areaTOTALv)>4]=0 
plt.ioff()
for i in range(1,surface_water.size,10):
    #plt.contour(area[i,:,:])
    #fig1=plt.figure() 
    #spec = gridspec.GridSpec(ncols=2, nrows=1,
                         #width_ratios=[2, 1])
    fig = plt.figure(figsize=(10, 5))
    gs = GridSpec(nrows=4, ncols=2)                     
    # f,(a0,a1,a2) = plt.subplots(3, 1, gridspec_kw={'height_ratios': [10,2,2]},
    #                             figsize=(10, 10))
    levels = np.arange(0, 1.2, 0.05)
    a0 = fig.add_subplot(gs[0, 0])
    a0.plot(sp_sch.df['p2_cs451'].index,areaTOTAL)
    a0.set_title('Area ($\mathregular{m^2}$)', fontsize = 10.0)
    a0.set_yticks(range(0,40000,10000))
    a0.set_xticklabels([])
    a0.axvline(sp_sch.df['p2_cs451'][i:i+1].index,color='red')
    a1 = fig.add_subplot(gs[1, 0])
    a1.plot(sp_sch.df['elev'].index,sp_sch.df['elev'])
    a1.axvline(sp_sch.df['p2_cs451'][i:i+1].index,color='red')
    a1.set_title('Depth at SA2 (m)', fontsize = 10.0)
    a1.set_xticklabels([])
    a2 = fig.add_subplot(gs[2, 0])
    a2.plot(sp_sch.df['elev'].index,areaTOTALvm2day)
    a2.set_title('Area change rate ($\mathregular{m^2}$/day)', fontsize = 10.0)
    # a2.set_yticks(range(0,1,0.5))
    a2.set_xticklabels([])
    a2.axvline(sp_sch.df['p2_cs451'][i:i+1].index,color='red')
    a3 = fig.add_subplot(gs[3, 0])
    a3.plot(sp_sch.df['elev'].index,surface_watervm2day)
    a3.axvline(sp_sch.df['p2_cs451'][i:i+1].index,color='red')
    a3.set_title('Depth change rate at SA2 (mm/day)', fontsize = 10.0)
    a3.tick_params(axis='x', which='major', labelsize=10, rotation=30)
    a3.tick_params(axis='x', which='major', labelsize=10, rotation=30)
    a4 = fig.add_subplot(gs[:, 1])
    z1=a4.contourf(depth[i,:,:],cmap = "jet",levels=levels)
    a4.title.set_text('Water depth at different locations (m)')
    plt.colorbar(z1,ax=a4)
    
    # a2.plot(elev.index,elev)
    # a2.axvline(sp_sch.df['p2_cs451'][i:i+1].index,color='red')
    # a2.set_ylabel('depth at SA2 (m)', fontsize = 10.0)
    # a2.tick_params(axis='x', which='major', labelsize=10, rotation=30)
    #F
    plt.tight_layout()
    plt.savefig(f"{i:04d}.png",dpi=300)
    plt.close()

for i in range(1,surface_water.size,10):
    #plt.contour(area[i,:,:])
    #fig1=plt.figure() 
    #plt.ion()
    #spec = gridspec.GridSpec(ncols=2, nrows=1,
                         #width_ratios=[2, 1])
    f,(a0,a1,a2) = plt.subplots(3, 1, gridspec_kw={'height_ratios': [10,2,2]},
                                figsize=(10, 10))
    levels = np.arange(0, 0.2, 0.01)
    z1=a0.contourf(depthv[i,:,:],cmap = "jet",levels=levels)
    plt.colorbar(z1,ax=a0)
    a1.plot(elev.index,areaTOTALv)
    a1.set_ylabel('area ($\mathregular{m^2}$)', fontsize = 10.0)
    a1.set_yticks(range(0,1000,100))
    a1.set_xticklabels([])
    a1.axvline(elev[i:i+1].index,color='red')
    a2.plot(elev.index,elevchange)
    a2.axvline(elev[i:i+1].index,color='red')
    a2.set_ylabel('depth at SA2 (m)', fontsize = 10.0)
    a2.tick_params(axis='x', which='major', labelsize=10, rotation=30)
    #F
    plt.tight_layout()
    plt.savefig(f"variation{i:04d}.png",dpi=300)
    plt.close()    
    print(i)
    
    plt.pause(1)
plt.colorbar()
plt.plot(tb_pandas.result_df['p2_cs451'][198:].index,areaTOTAL)

    
#calculate recharge in ML and evaporation in ML
#evaporation = evaporation in mm cross the area
# for i in range(areaTOTAL[:,1].size)
sp_sch.df['areaTOTAL']=areaTOTAL
volumnTOTALv=np.zeros(volumnTOTAL.size)
volumnTOTALv[1:]=diff(volumnTOTAL)
sp_sch.df['volumnTOTAL']=volumnTOTAL
sp_sch.df['volumnTOTALv']=volumnTOTALv
df_mean= sp_sch.df.resample('D').mean() 
df_mean['evp']=df_mean['areaTOTAL']*df_mean['pet_mmPday']*constants.mm2m
sp_sch.df['evp']=areaTOTAL*sp_sch.df['pet_mmPday']*constants.mm2m
sp_sch.df['evpmega']=sp_sch.df['evp']/1000
df_mean['evpmega']=df_mean['evp']/1000

#recharge into the basin
sp_sch.df['recharge']=pumping-sp_sch.df['areaTOTAL']*(elevchange/20*60+sp_sch.df['pet_mmPday']*constants.mm2m/constants.msPmmday)          
df_mean= sp_sch.df.resample('D').mean() 
# f,(a0,a1,a2) = plt.subplots(3, 1, gridspec_kw={'height_ratios': [10,2,2]},
#                                 figsize=(10, 10))     
f,(a0,a1,a2,a3,a4,a5) = plt.subplots(6, 1,sharex=True,constrained_layout=True,figsize=(10,8))
# a0.set_aspect('auto')
a0.grid(b = True, color ='grey',
        linestyle ='-.', linewidth = 0.5,
        alpha = 0.2)
a1.grid(b = True, color ='grey',
        linestyle ='-.', linewidth = 0.5,
        alpha = 0.2)
a2.grid(b = True, color ='grey',
        linestyle ='-.', linewidth = 0.5,
        alpha = 0.2)
a3.grid(b = True, color ='grey',
        linestyle ='-.', linewidth = 0.5,
        alpha = 0.2)
a4.grid(b = True, color ='grey',
        linestyle ='-.', linewidth = 0.5,
        alpha = 0.2)
a5.grid(b = True, color ='grey',
        linestyle ='-.', linewidth = 0.5,
        alpha = 0.2)
a0.bar(df_mean.index, df_mean['evpmega'])
a0.set_title('Daily water loss from the basin calculated by PET (ML/day)’', fontsize = 10.0,wrap=True)
# a0.set_yticks(range(0,500,200))
a0.set_xticklabels([])
a1.bar(df_mean.index, df_mean['pet_mmPday'])
a1.set_title('Daily PET (mm/day)’', fontsize = 10.0,wrap=True)
a1.set_xticklabels([])
a1.set_aspect('auto')
a2.plot(df_mean.index, df_mean['pet_mmPday'].cumsum())
a2.set_title('cumulative ET (mm)', fontsize = 10.0,wrap=True)
a2.set_aspect('auto')
# a2.set_yticks(range(0,500,100))
a3.set_xticklabels([])
a3.plot(df_mean.index, df_mean['evpmega'].cumsum())
a3.set_title('Cumulative water loss by ET (ML)', fontsize = 10.0,wrap=True)
# a2.set_yticks(range(0,500,100))
a3.set_xticklabels([])
a3.set_aspect('auto')
a4.plot(df_mean.index, df_mean['areaTOTAL'])
a4.set_title('Area of basin ($\mathregular{m^2}$)', fontsize = 10.0,wrap=True)
a4.set_xticklabels([])
a4.set_aspect('auto')
a5.plot(df_mean.index, df_mean['volumnTOTAL']/1000)
# a5.plot(sp_sch.df['pumping'].index, pumpingMLday)
a5.set_title('Volumn of surface water body (ML)', fontsize = 10.0,wrap=True)
a5.set_aspect('auto')
f.subplots_adjust(left=None, bottom=None, right=None, top=None,
                wspace=None, hspace=None)
plt.tight_layout()


plt.savefig("evaporation.png",dpi=300)

#area[0:,i,j]=depth  
#area[0:,i,j]=0
#area=area*4
# areaTOTAL=np.cumsum(area,axis=1)
# area_profile=area_profile[0:,area_profile[1,0:].size-1]
# plt.plot(surface_water.ts,area_profile)
# surface_water.ts
# plt.plot(surface_water['ts'],area_profile)
# plt.plot(tb_pandas.surface_water['ser'],area_profile)
# plt.plot(tb_pandas['surface_water']['ts'],area_profile)
# plt.plot(tb_pandas['surface_water'].ts,area_profile)
# plt.plot(tb_pandas['surface_water'].index,area_profile)
# plt.plot(tb_pandas.result_df['temp2'].index,area_profile)
# tb_pandas.result_df['temp2'].index
# surface_water=tb_pandas.result_df['p2_cs451']['value'][3:]-0.47;
# plt.plot(tb_pandas.result_df['surface_water'].index,area_profile)
# tb_pandas.result_df['surface_water'].index
# a=tb_pandas.result_df['temp2'].index
# surface_water=tb_pandas.result_df['p2_cs451'][3:]-0.47;
# a=tb_pandas.result_df['temp2']
# a=tb_pandas.result_df['temp2'].index
 f1,(a0,a1,a2) = plt.subplots(3, 1)
 a0.plot(sp_sch.df['p2_cs451'].index,elev_original)
 a1.plot(sp_sch.df['p2_cs451'].index,sp_sch.df['elev'])
 a2.plot(sp_sch.df['p2_cs451'].index,sp_sch.df['pumping'])
