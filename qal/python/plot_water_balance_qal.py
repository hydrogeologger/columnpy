# below is to calculate penman monteith potential evaporation
# tc0_k removes all na to 25 degree as this way will fill many gaps
sp_sch[sch_name].df['tc0_k']=sp_sch[sch_name].df['tc'].fillna(25.0) +constants.kelvin
sp_sch[sch_name].df['wdspdkphavg2m_0']=sp_sch[sch_name].df['wdspdkphavg2m'].fillna(1.0)

sp_sch[sch_name].df['drhowv_sat_dt']=constants.dsvp_dtk( sp_sch[sch_name].df['tc0_k'] )
sp_sch[sch_name].df['latent_heat_JPkg']=constants.lhv(sp_sch[sch_name].df['tc0_k'])

# TO181205 during the large block of time tmp1 
sp_sch[sch_name].df['sat_vapor_pressure_soil_pa'] = constants.svp(sp_sch[sch_name].df['tmp_soil_surf']+constants.kelvin)
sp_sch[sch_name].df['vapor_pressure_air_pa'] = constants.svp(sp_sch[sch_name].df['tc0_k'])*sp_sch[sch_name].df['rh']
sp_sch[sch_name].df['Rn_wPm2']=  (sp_sch[sch_name].df['ir_up_daisy']-254)*1.28+ (sp_sch[sch_name].df['ir_up_concat']-252.)/20.512
time_end_ir_up_daisy=np.datetime64('2018-06-29T13:00')
sp_sch[sch_name].df['Rn_wPm2'].loc[:time_end_ir_up_daisy]=(sp_sch[sch_name].df['ir_up_daisy']-254)*1.28
#sp_sch[sch_name].df['Rn_wPm2_part1']=(sp_sch[sch_name].df['ir_up_daisy'].loc[:time_end_ir_up_daisy]-254)*1.28
#sp_sch[sch_name].df['Rn_wPm2_part1'].loc[sp_sch[sch_name].df['Rn_wPm2_part1']<0]=0
sp_sch[sch_name].df['Rn_wPm2'].loc[time_end_ir_up_daisy:]=(sp_sch[sch_name].df['ir_up_concat']-252.)/20.512
#sp_sch[sch_name].df['Rn_wPm2'].loc[sp_sch[sch_name].df['Rn_wPm2']<0]=np.nan
#sp_sch[sch_name].df['Rn_wPm2_part2']=(sp_sch[sch_name].df['ir_up_concat'].loc[time_end_ir_up_daisy:]-252.)/20.512
#sp_sch[sch_name].df['Rn_wPm2_part2'].loc[sp_sch[sch_name].df['Rn_wPm2_part2']<0]=0
#sp_sch[sch_name].df['Rn_wPm2']=sp_sch[sch_name].df['Rn_wPm2_part1']+sp_sch[sch_name].df['Rn_wPm2_part2']
#sp_sch[sch_name].df['Rn_wPm2']=  (sp_sch[sch_name].df['ir_up_daisy']-254)*1.18+ (sp_sch[sch_name].df['ir_up_concat']-252.)/20.512

sp_sch[sch_name].df['ra_sPm']=np.log(2/0.000001) **2.0 /0.41**2.0/sp_sch[sch_name].df['wdspdkphavg2m_0']
#sp_sch[sch_name].df['rs_sPm']=constants.rs1994(sp_sch[sch_name].df['mmo_surf'],1.0)
#rs1994_para=0.22;rs1994_param2=35.63 # good 
#rs1994_param=0.18;rs1994_param2=35.63 # good 
#rs1994_param=0.21;rs1994_param2=35.63 # good 

rs1994_param=0.18;rs1994_param2=35.63 # good 
rs1994_param=0.21;rs1994_param2=35.63 # good 

#rs1994_param=0.41;rs1994_param2=50 # good 
rs1994_param=0.32;rs1994_param2=35.63 # good TO190712
rs1994_param=0.345;rs1994_param2=35.63 # good T20190713
rs1994_param=0.36;rs1994_param2=35.63 # good T20190723
#time_start=np.datetime64('2018-03-27 19:00')
#time_switch=np.datetime64('2018-11-01 00:00')
#time_end=np.datetime64('2019-03-04T06:30')
#mask1=sp_sch[sch_name].df['date_time'].between(time_start,time_switch)
#mask2=sp_sch[sch_name].df['date_time'].between(time_switch,time_end)

sp_sch[sch_name].df['rs_sPm']=10.*np.exp(rs1994_param2*(rs1994_param- sp_sch[sch_name].df['mmo_surf']  ))

sp_sch[sch_name].df['pet_pm_denom'] = sp_sch[sch_name].df['drhowv_sat_dt'] + constants.psych* ( 1.+ 1./sp_sch[sch_name].df['ra_sPm'] )

sp_sch[sch_name].df['aet_pm_denom_rs'] = sp_sch[sch_name].df['drhowv_sat_dt'] + constants.psych* \
        ( 1.+ sp_sch[sch_name].df['rs_sPm']/sp_sch[sch_name].df['ra_sPm'] )

sp_sch[sch_name].df['pet_pm_part1']= ( sp_sch[sch_name].df['drhowv_sat_dt'] * sp_sch[sch_name].df['Rn_wPm2']  ) \
        / sp_sch[sch_name].df['pet_pm_denom']
sp_sch[sch_name].df['pet_pm_part2']=constants.air_density_kgPm3*constants.heat_capacity_air_JPkgPK*  \
        ( sp_sch[sch_name].df['sat_vapor_pressure_soil_pa'] -  sp_sch[sch_name].df['vapor_pressure_air_pa']   ) \
        /sp_sch[sch_name].df['ra_sPm'] / sp_sch[sch_name].df['pet_pm_denom']

sp_sch[sch_name].df['pet_part1_mmPday']=sp_sch[sch_name].df['pet_pm_part1'] / \
        constants.lhv(298.15)/ constants.rhow_pure_water * constants.msPmmday
sp_sch[sch_name].df['pet_part2_mmPday']=sp_sch[sch_name].df['pet_pm_part2'] / \
        constants.lhv(298.15)/ constants.rhow_pure_water * constants.msPmmday

sp_sch[sch_name].df['aet_part1_mmPday']= ( sp_sch[sch_name].df['drhowv_sat_dt'] * sp_sch[sch_name].df['Rn_wPm2']  ) \
        / sp_sch[sch_name].df['aet_pm_denom_rs']/constants.lhv(298.15)/ constants.rhow_pure_water * constants.msPmmday

sp_sch[sch_name].df['aet_part2_mmPday']=constants.air_density_kgPm3*constants.heat_capacity_air_JPkgPK*  \
        ( sp_sch[sch_name].df['sat_vapor_pressure_soil_pa'] -  sp_sch[sch_name].df['vapor_pressure_air_pa']   ) \
        /sp_sch[sch_name].df['ra_sPm'] / sp_sch[sch_name].df['aet_pm_denom_rs'] \
        / constants.lhv(298.15)/ constants.rhow_pure_water * constants.msPmmday

sp_sch[sch_name].df['pet_mmPday']=sp_sch[sch_name].df['pet_part1_mmPday'] + sp_sch[sch_name].df['pet_part2_mmPday'].fillna(0)
sp_sch[sch_name].df['aet_mmPday']=sp_sch[sch_name].df['aet_part1_mmPday'] + sp_sch[sch_name].df['aet_part2_mmPday'].fillna(0)

df_mean = sp_sch[sch_name].df.resample('D').mean()
df_max = sp_sch['qal'].df.resample('D').max()
df_last = sp_sch['qal'].df.resample('D').last()

#df_mean.index,df_mean['pet_mmPday']

#time_start=np.datetime64('2019-01-24T10:00')
#time_end=np.datetime64('2019-01-26T10:00')
#mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)

'''
plt.figure()
plt.plot(sp_sch[sch_name].df.index[mask],sp_sch[sch_name].df['sat_vapor_pressure_soil_pa'][mask])

plt.figure()
plt.plot(sp_sch[sch_name].df.index[mask],sp_sch[sch_name].df['vapor_pressure_air_pa'][mask])

plt.figure()
plt.plot(sp_sch[sch_name].df.index[mask],sp_sch[sch_name].df['tc0_k'][mask],'k-')

plt.figure()
plt.plot(sp_sch[sch_name].df.index,sp_sch[sch_name].df['tmp6'],'k-')

plt.figure()
plt.plot(sp_sch[sch_name].df.index[mask],sp_sch[sch_name].df['tmp7'][mask],'y-')

plt.figure()
plt.plot(sp_sch[sch_name].df.index,sp_sch[sch_name].df['tmp8'],'r-')

plt.figure()
plt.plot(sp_sch[sch_name].df.index,sp_sch[sch_name].df['mmo3_p1'],'r-')

plt.figure()
plt.plot(sp_sch[sch_name].df.index,sp_sch[sch_name].df['mmo3_p2'],'k-')


#---------moisture divided in two stages becaus of different values of dry and wet condition from 2 stages, so use different mask for each stage---------------
time_start=np.datetime64('2018-01-29T09:40')
time_switch=np.datetime64('2018-04-09T18:03')
time_end=np.datetime64('2019-03-22T11:40')
mask=sp_sch[sch_name].df['date_time'].between(time_start,time_switch)
mask1=sp_sch[sch_name].df['date_time'].between(time_switch,time_end)

plt.figure()
plt.plot(sp_sch[sch_name].df.index,sp_sch[sch_name].df['mo0'],'r-')

plt.figure()
plt.plot(sp_sch[sch_name].df.index,sp_sch[sch_name].df['mmo0'],'r-')

plt.figure()
plt.plot(sp_sch[sch_name].df.index[mask],sp_sch[sch_name].df['mmo0'][mask],'r-')

plt.figure()
plt.plot(sp_sch[sch_name].df.index,sp_sch[sch_name].df['mmo0'][mask1],'r-')


plt.figure()
plt.plot(sp_sch[sch_name].df.index,sp_sch[sch_name].df['mo1'],'b-')

plt.figure()
plt.plot(sp_sch[sch_name].df.index,sp_sch[sch_name].df['mmo1'],'b-')


plt.figure()
plt.plot(sp_sch[sch_name].df.index,sp_sch[sch_name].df['mo2'],'y-')

plt.figure()
plt.plot(sp_sch[sch_name].df.index,sp_sch[sch_name].df['mmo2'],'y-')


plt.figure()
plt.plot(sp_sch[sch_name].df.index,sp_sch[sch_name].df['mo3'],'k-')

plt.figure()
plt.plot(sp_sch[sch_name].df.index,sp_sch[sch_name].df['mmo3'],'k-')


plt.figure()
plt.plot(sp_sch[sch_name].df.index,sp_sch[sch_name].df['mo4'],'g-')

plt.figure()
plt.plot(sp_sch[sch_name].df.index,sp_sch[sch_name].df['mmo4'],'g-')


plt.figure()
plt.plot(sp_sch[sch_name].df.index,sp_sch[sch_name].df['mo5'],'c-')

plt.figure()
plt.plot(sp_sch[sch_name].df.index,sp_sch[sch_name].df['mmo5'],'c-')


plt.figure()
plt.plot(sp_sch[sch_name].df.index,sp_sch[sch_name].df['mo6'],'m-')

plt.figure()
plt.plot(sp_sch[sch_name].df.index,sp_sch[sch_name].df['mmo6'],'m-')


plt.figure()
plt.plot(sp_sch[sch_name].df.index,sp_sch[sch_name].df['mo7'],'r-')

plt.figure()
plt.plot(sp_sch[sch_name].df.index,sp_sch[sch_name].df['mmo7'],'r-')


plt.figure()
plt.plot(sp_sch[sch_name].df.index,sp_sch[sch_name].df['mo8'],'b-')

plt.figure()
plt.plot(sp_sch[sch_name].df.index,sp_sch[sch_name].df['mmo8'],'b-')


plt.figure()
plt.plot(sp_sch[sch_name].df.index,sp_sch[sch_name].df['mo9'],'c-')

plt.figure()
plt.plot(sp_sch[sch_name].df.index,sp_sch[sch_name].df['mmo9'],'c-')


plt.figure()
plt.plot(sp_sch[sch_name].df.index[mask],sp_sch[sch_name].df['aet_part1_mmPday'][mask])
plt.plot(sp_sch[sch_name].df.index[mask],sp_sch[sch_name].df['aet_part2_mmPday'][mask])
plt.plot(sp_sch[sch_name].df.index[mask],sp_sch[sch_name].df['aet_mmPday'][mask])

plt.figure()
plt.plot(sp_sch[sch_name].df.index[mask],sp_sch[sch_name].df['rs_sPm'][mask])

plt.figure()
plt.plot(sp_sch[sch_name].df.index[mask],sp_sch[sch_name].df['ra_sPm'][mask])

plt.figure()
plt.plot(sp_sch[sch_name].df.index[mask],sp_sch[sch_name].df['wdspdkphavg2m_0'][mask])


plt.figure()
plt.plot(sp_sch[sch_name].df.index[mask],sp_sch[sch_name].df['aet_part1_mmPday'][mask],'r-')
plt.plot(sp_sch[sch_name].df.index[mask],sp_sch[sch_name].df['aet_part2_mmPday'][mask],'g-')
plt.plot(sp_sch[sch_name].df.index[mask],sp_sch[sch_name].df['aet_mmPday'][mask])

plt.figure()
plt.plot(sp_sch[sch_name].df.index[mask],sp_sch[sch_name].df['pet_mmPday'][mask],'k-')
plt.plot(sp_sch[sch_name].df.index[mask],sp_sch[sch_name].df['pet_part1_mmPday'][mask],'r-') 
plt.plot(sp_sch[sch_name].df.index[mask],sp_sch[sch_name].df['pet_part2_mmPday'][mask],'g-') 


time_start=np.datetime64('2018-06-01T10:00')
time_end=np.datetime64('2018-06-30T10:00')
mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)


'''
'''
plt.figure()
plt.plot(sp_sch[sch_name].df.index[mask],sp_sch[sch_name].df['pet_mmPday'][mask])

plt.figure()
plt.plot(df_mean.index[mask],df_mean['pet_mmPday'][mask])


plt.figure()
plt.plot(sp_sch[sch_name].df.index[mask],sp_sch[sch_name].df['Rn_wPm2'][mask],'y-')

plt.figure()
plt.plot(sp_sch[sch_name].df.index[mask],sp_sch[sch_name].df['drhowv_sat_dt'][mask])

plt.figure()
plt.plot(sp_sch[sch_name].df.index[mask],sp_sch[sch_name].df['pet_pm_denom'][mask])

plt.figure()
plt.plot(df_mean.index,df_mean['cumsum_rainmm'])





fig, ax = plt.subplots(10,sharex=True,figsize=(9,12))
ax[0].plot(ta['date_time'], (ta['radiation'])*0.007+0.2*ta['wdspdkphavg2m_0'].fillna(0), '-',color='maroon',\
        markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Dielectric suction A')

ax[1].plot(sp_sch[sch_name].df.index,sp_sch[sch_name].df['pet_mmPday'])
ax[1].plot(sp_sch[sch_name].df.index,sp_sch[sch_name].df['aet_mmPday'])

ax[2].plot(sp_sch[sch_name].df.index,sp_sch[sch_name].df['pet_part2_mmPday']  )
ax[3].plot(sp_sch[sch_name].df.index,sp_sch[sch_name].df['pet_part1_mmPday']  )
ax[4].plot(sp_sch[sch_name].df.index,sp_sch[sch_name].df['Rn_wPm2'])
ax[5].plot(sp_sch[sch_name].df.index,sp_sch[sch_name].df['wdspdkphavg2m_0']     )
ax[6].plot(sp_sch[sch_name].df.index,sp_sch[sch_name].df['sat_vapor_pressure_soil_pa']     )
ax[7].plot(sp_sch[sch_name].df.index,sp_sch[sch_name].df['vapor_pressure_air_pa']  )
#ax[8].plot(sp_sch[sch_name].df.index,sp_sch[sch_name].df['tc']     )
#ax[9].plot(sp_sch[sch_name].df.index,sp_sch[sch_name].df['rh']  )

#ax[2].plot(sp_sch[sch_name].df.index,sp_sch[sch_name].df['pet_pm_part1'])
#ax[3].plot(sp_sch[sch_name].df.index,sp_sch[sch_name].df['pet_pm_part2'])

ax[0].set_ylabel('evp_fitting', fontsize=y_fontsize, labelpad=15)
ax[1].set_ylabel('pet_pm', fontsize=y_fontsize, labelpad=15)
ax[2].set_ylabel('part2\nmm/day', fontsize=y_fontsize, labelpad=15)
ax[3].set_ylabel('part1\nmm/day', fontsize=y_fontsize, labelpad=15)
#ax[2].set_ylabel('pet_pm_part1', fontsize=y_fontsize, labelpad=5)
#ax[3].set_ylabel('pet_pm_part2', fontsize=y_fontsize, labelpad=17)
ax[4].set_ylabel('Rn_wPm2', fontsize=y_fontsize, labelpad=7)
ax[5].set_ylabel('windspeed', fontsize=y_fontsize, labelpad=15)
ax[6].set_ylabel('sat_vapor_p soil', fontsize=y_fontsize, labelpad=15)
ax[7].set_ylabel('vapor_p_air', fontsize=y_fontsize, labelpad=15)

'''
##plot top moisture
#plt.figure()
#plt.plot(sp_sch[sch_name].df.index,sp_sch[sch_name].df['mmo0']     )
#plt.plot(sp_sch[sch_name].df.index,sp_sch[sch_name].df['mmo1']     )
#plt.plot(sp_sch[sch_name].df.index,sp_sch[sch_name].df['mmo2']     )
#plt.plot(sp_sch[sch_name].df.index,sp_sch[sch_name].df['mmo_surf']     )

# read from manual.xlsx, currently sellement data is mannually read and stored in the excel file
#https://stackoverflow.com/questions/16888888/how-to-read-a-xlsx-file-using-the-pandas-library-in-ipython
#xl_file = pd.ExcelFile( schedule['manual_excel'])
#daily_data_manual = xl_file.parse(index_col='date_time') 

#df_mean = sp_sch['stanwell'].df.resample('D').mean()
#df_max = sp_sch['stanwell'].df.resample('D').max()
#df_last = sp_sch['stanwell'].df.resample('D').last()
# the original time for mean value is at 12am, we shift it to 12pm
#df_mean['date_time']=df_mean['date_time']+pd.to_timedelta(12, unit='h')
#df_mean['date_time']=df_mean.index

df_mean.index=df_mean.index+pd.to_timedelta(12, unit='h')
df_mean['date_time']=df_mean.index
depth_y=np.array([1,3,8,13,20,28,38,48,70,85]) #acordording to location sensor
depth_y=np.array([1,3,8,13,20,28,38,48,70,85])
responsible_depth_cm=np.concatenate( (np.diff(depth_y),np.array([36])) )

df_mean['total_moisture_cm']=df_mean['mmo0'].fillna(0)*responsible_depth_cm[0] \
    +df_mean['mmo1'].fillna(0)*responsible_depth_cm[1] \
    +df_mean['mmo2'].fillna(0)*responsible_depth_cm[2] \
    +df_mean['mmo3'].fillna(0)*responsible_depth_cm[3] \
    +df_mean['mmo4'].fillna(0)*responsible_depth_cm[4] \
    +df_mean['mmo5'].fillna(0)*responsible_depth_cm[5] \
    +df_mean['mmo6'].fillna(0)*responsible_depth_cm[6] \
    +df_mean['mmo7'].fillna(0)*responsible_depth_cm[7] \
    +df_mean['mmo8'].fillna(0)*responsible_depth_cm[8] \
    +df_mean['mmo9'].fillna(0)*responsible_depth_cm[9]

df_mean['evap_rate']=np.concatenate( (np.diff(df_mean['total_moisture_cm']),np.array([np.nan])))

df_mean['total_moisture_07_cm']=df_mean['mmo0'].fillna(0)*responsible_depth_cm[0] \
    +df_mean['mmo1'].fillna(0)*responsible_depth_cm[1] \
    +df_mean['mmo2'].fillna(0)*responsible_depth_cm[2] \
    +df_mean['mmo3'].fillna(0)*responsible_depth_cm[3] \
    +df_mean['mmo4'].fillna(0)*responsible_depth_cm[4] \
    +df_mean['mmo5'].fillna(0)*responsible_depth_cm[5] \
    +df_mean['mmo6'].fillna(0)*responsible_depth_cm[6] \
    +df_mean['mmo7'].fillna(0)*responsible_depth_cm[7]

##plot total moisture
#plt.figure()
#plt.plot(df_mean.index,df_mean['total_moisture_cm'])
#plt.plot(df_mean.index,df_mean['total_moisture_07_cm'])

bb=df_mean.index-df_mean.index[0]

cc= bb.total_seconds()

interp_method=wf.SmoothSpline(cc,df_mean['total_moisture_cm'],p=1e-14)
dd=interp_method(cc)
df_mean['evap_rate_dd']=np.concatenate( (np.diff(dd),np.array([np.nan])))

interp_method=wf.SmoothSpline(cc,df_mean['total_moisture_cm'],p=5e-15)
ee=interp_method(cc)
df_mean['evap_rate_ee']=np.concatenate( (np.diff(ee),np.array([np.nan])))

#plt.figure()
#plt.plot(df_mean.index,dd)
#plt.plot(df_mean.index,ee)
#plt.plot(df_mean.index,df_mean['total_moisture_cm'])
#plt.plot(df_mean.index,df_mean['total_moisture_07_cm'])


## below is to calcuate evaporation rate from total moisture
#plt.subplot()
#plt.plot(df_mean.index,-df_mean['evap_rate_dd']*10)
#plt.plot(df_mean.index,-df_mean['evap_rate_ee']*10)
#plt.grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
#
#
#plt.plot(df_mean.index,dd)
#plt.figure()
#plt.plot(df_mean.index,df_mean['total_moisture_07'])

#plt.figure()
#plt.bar(df_mean.index,df_mean['pet_mmPday'])
#plt.bar(df_mean.index,df_mean['aet_mmPday'])

df_mean['total_water_out_m']=np.cumsum(df_mean['aet_mmPday'])*constants.mPmm
df_last['total_water_in_m']=np.cumsum(df_last['rainmm'].fillna(0))*constants.mPmm
#df_mean['net_water_pos_out_mPday']=(df_mean['aet_mmPday'].fillna(0)-list(df_last['rainmm'].fillna(0))) * constants.mPmm
#df_mean['cumsum_net_water_pos_out_m']=np.cumsum(df_mean['net_water_pos_out_mPday'])
df_mean['net_water_storage_mPday']=(list(df_last['rainmm'].fillna(0))-df_mean['aet_mmPday'].fillna(0)) * constants.mPmm
df_mean['cumsum_net_water_storage_m']=np.cumsum(df_mean['net_water_storage_mPday'])

'''
fig, ax = plt.subplots(7,sharex=True,figsize=(9,12))
#ax[0].plot(df_mean.index,df_mean['total_water_out_m'],'r-')
ax[0].plot(sp_sch[sch_name].df.index,sp_sch[sch_name].df['mmo0']     )
ax[0].plot(sp_sch[sch_name].df.index,sp_sch[sch_name].df['mmo1']     )
ax[0].plot(sp_sch[sch_name].df.index,sp_sch[sch_name].df['mmo2']     )
ax[1].plot(df_mean.index,-df_last['total_water_in_m'],'b-')
ax[2].bar(df_mean.index,df_mean['pet_mmPday'])
ax[2].bar(df_mean.index,df_mean['aet_mmPday'])
#ax[2].plot(df_mean.index,df_mean['aet_mmPday'].fillna(0))
#ax[2].plot(df_mean.index,df_mean['pet_mmPday'].fillna(0))
ax[3].plot(df_mean.index,-df_mean['rainmm'].fillna(0),'b-')
ax[4].plot(df_mean.index,df_mean['net_water_pos_out_mPday'])
ax[5].plot(df_mean.index,df_mean['cumsum_net_water_pos_out_m'],'-c')
ax[5].plot(df_mean.index,(85.-df_mean['total_moisture_cm'])*0.01,'brown')
ax[6].plot(df_mean.index,(85.-df_mean['total_moisture_cm'])*0.01)

y_fontsize=8
ax[0].set_title(str(rs1994_param)+ ' '+str(rs1994_param2)+ ' '+str(coef))
ax[0].set_ylabel('total_water_out', fontsize=y_fontsize, labelpad=15)
ax[1].set_ylabel('ttl_water_in', fontsize=y_fontsize, labelpad=15)
ax[2].set_ylabel('aet_mmPday', fontsize=y_fontsize, labelpad=15)
ax[3].set_ylabel('rainmm', fontsize=y_fontsize, labelpad=15)
ax[4].set_ylabel('net_water_\npost_out_mPday', fontsize=y_fontsize, labelpad=7)
ax[5].set_ylabel('cumsum_out_m', fontsize=y_fontsize, labelpad=15)
ax[6].set_ylabel('total_moisture', fontsize=y_fontsize, labelpad=15)
'''
#ax[6].set_ylabel('sat_vapor_p soil', fontsize=y_fontsize, labelpad=15)
#ax[7].set_ylabel('vapor_p_air', fontsize=y_fontsize, labelpad=15)


#ax[3].plot(df_last.index, df_last['rainmm'])
'''
# it is found the maximum rainfall is always different from daily ones so this plot tells the difference
plt.figure()
plt.plot(ta['date_time'], ta['rainmm'], '-',color='maroon',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Dielectric suction A')
plt.plot(df_mean.index, df_last['rainmm']) #, width=1.0)
'''


#ax=plt.figure(figsize=(6,6))
fig, ax = plt.subplots(figsize=(10,8))
for axis in ['top','bottom','left','right']:
  i.spines[axis].set_linewidth(2)
#plt.plot(df_mean.index,df_mean['cumsum_net_water_pos_out_m']*1000,'-c',label='Calculated from\nweather station')
#plt.plot(df_mean.index,(85.-df_mean['total_moisture_cm'])*0.01*1000,'brown',label='Calculated from\nmoisture profile')
plt.plot(df_mean.index,df_mean['cumsum_net_water_storage_m']*1000+610,'-c',label='Calculated from\nweather station')
plt.plot(df_mean.index,(df_mean['total_moisture_cm'])*0.01*1000,'brown',label='Calculated from\nmoisture profile')

#ax.set_ylim([-10,360])

ax.xaxis.set_major_formatter(mdates.DateFormatter('%b/%d'))
ax.set_xlabel('DATE')
#ax.set_ylabel('WATER LOSS FROM COLUMN (mm)')
ax.set_ylabel('EQUIVALENT WATER STORAGE IN COLUMN (mm)')
ax.legend(bbox_to_anchor=(0.1, 0.99 ), loc='upper left', borderaxespad=0.,fontsize=9,handletextpad=0.83,labelspacing=1.32,ncol=1,columnspacing=0.4)
ax.grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
fig.savefig('figure/plot_water_balance_over_time.png', format='png', dpi=100)
