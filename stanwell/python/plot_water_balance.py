import datetime
'''
plt.figure()
plt.plot(sp_sch[sch_name].df.index,sp_sch[sch_name].df['sat_vapor_pressure_soil_pa'])

plt.figure()
plt.plot(sp_sch[sch_name].df.index,sp_sch[sch_name].df['aet_part1_mmPday'])
plt.plot(sp_sch[sch_name].df.index,sp_sch[sch_name].df['aet_part2_mmPday'])
plt.plot(sp_sch[sch_name].df.index,sp_sch[sch_name].df['aet_mmPday'])

plt.figure()
plt.plot(sp_sch[sch_name].df.index,sp_sch[sch_name].df['rs_sPm'])

plt.figure()
plt.plot(sp_sch[sch_name].df.index,sp_sch[sch_name].df['aet_part1_mmPday'],'r-')
plt.plot(sp_sch[sch_name].df.index,sp_sch[sch_name].df['aet_part2_mmPday'],'g-')
plt.plot(sp_sch[sch_name].df.index,sp_sch[sch_name].df['aet_mmPday'])

plt.figure()
plt.plot(sp_sch[sch_name].df.index,sp_sch[sch_name].df['pet_part1_mmPday'],'r-') 
plt.plot(sp_sch[sch_name].df.index,sp_sch[sch_name].df['pet_part2_mmPday'],'g-') 

plt.figure()
plt.plot(sp_sch[sch_name].df.index,sp_sch[sch_name].df['aet_mmPday'],'r-') 

plt.figure()
plt.plot(sp_sch[sch_name].df.index[mask],sp_sch[sch_name].df['rainmm'][mask],'r-') 


'''
'''
plt.figure()
plt.plot(sp_sch[sch_name].df.index,sp_sch[sch_name].df['pet_mmPday'])

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

time_start_mmo3 = datetime.datetime(2018,10,14,12,00)
time_end_mmo3 = datetime.datetime(2019,03,14,12,00)
time_end_mmo4 = datetime.datetime(2019,12,16,12,00)
time_end = datetime.datetime(2020,04,20,12,00)
mask_mmo3=df_mean['date_time'].between(time_start_mmo3,time_end_mmo3)
mask_mmo4=df_mean['date_time'].between(time_end_mmo3,time_end_mmo4)
mask_mmo5=df_mean['date_time'].between(time_end_mmo4,time_end)
settlement_time_end_mmo3 = 169 #Unit is mm
cum_responsible_depth_above_mmo4 = 190 #Unit is mm
settlement_time_end_mmo4 = 227 #Unit is mm
cum_responsible_depth_above_mmo5 = 270 #Unit is mm
settlement_time_end = 285 #Unit is mm
cum_responsible_depth_above_mmo6 = 370 #Unit is mm

df_mean['total_moisture_cm'].loc[mask_mmo3]=df_mean['mmo_surf'].fillna(0)*((settlement_time_end_mmo3-df_mean['settlement_mm']) / 10) \
    +df_mean['mmo3'].fillna(0)*(cum_responsible_depth_above_mmo4 - settlement_time_end_mmo3)/10 \
    +df_mean['mmo4'].fillna(0)*responsible_depth_cm[4] \
    +df_mean['mmo5'].fillna(0)*responsible_depth_cm[5] \
    +df_mean['mmo6'].fillna(0)*responsible_depth_cm[6] \
    +df_mean['mmo7'].fillna(0)*responsible_depth_cm[7] \
    +df_mean['mmo8'].fillna(0)*responsible_depth_cm[8] \
    +df_mean['mmo9'].fillna(0)*responsible_depth_cm[9]

df_mean['total_moisture_cm'].loc[mask_mmo4]=df_mean['mmo_surf'].fillna(0)*(settlement_time_end_mmo4-df_mean['settlement_mm'])/10 \
    +df_mean['mmo4'].fillna(0)*(cum_responsible_depth_above_mmo5 - settlement_time_end_mmo4)/10 \
    +df_mean['mmo5'].fillna(0)*responsible_depth_cm[5] \
    +df_mean['mmo6'].fillna(0)*responsible_depth_cm[6] \
    +df_mean['mmo7'].fillna(0)*responsible_depth_cm[7] \
    +df_mean['mmo8'].fillna(0)*responsible_depth_cm[8] \
    +df_mean['mmo9'].fillna(0)*responsible_depth_cm[9] 

df_mean['total_moisture_cm'].loc[mask_mmo5]=df_mean['mmo_surf'].fillna(0)*(settlement_time_end - df_mean['settlement_mm'])/10 \
    +df_mean['mmo4'].fillna(0)*(cum_responsible_depth_above_mmo6 - settlement_time_end)/10 \
    +df_mean['mmo6'].fillna(0)*responsible_depth_cm[6] \
    +df_mean['mmo7'].fillna(0)*responsible_depth_cm[7] \
    +df_mean['mmo8'].fillna(0)*responsible_depth_cm[8] \
    +df_mean['mmo9'].fillna(0)*responsible_depth_cm[9]
#----Above is to calculate the water mass balance considering the settlement of tailings. the first number is 
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
time_start_ponding1 = datetime.datetime(2019,03,28,12,00)
time_end_ponding1 = datetime.datetime(2019,04,02,12,00)
time_start_ponding2 = datetime.datetime(2020,01,18,12,00)
time_end_ponding2 = datetime.datetime(2020,01,31,12,00)
time_start_ponding3 = datetime.datetime(2020,02,06,12,00)
time_end_ponding3 = datetime.datetime(2020,03,10,12,00)
mask1=df_mean['date_time'].between(time_start_ponding1,time_end_ponding1)#the first time period when the column was obviously filled with ponding water above soil surface
mask2=df_mean['date_time'].between(time_start_ponding2,time_end_ponding2)#the second time period when the column was obviously filled with ponding water above soil surface
mask3=df_mean['date_time'].between(time_start_ponding3,time_end_ponding3)#the third time period when the column was obviously filled with ponding water above soil surface

df_mean['aet_mmPday'].loc[mask1]=0
df_mean['aet_mmPday'].loc[mask2]=0
df_mean['aet_mmPday'].loc[mask3]=0


df_mean['total_water_out_m']=np.cumsum(df_mean['aet_mmPday'])*constants.mPmm
df_last['total_water_in_m']=np.cumsum(df_last['rainmm'].fillna(0))*constants.mPmm
#df_mean['net_water_pos_out_mPday']=(df_mean['aet_mmPday'].fillna(0)-list(df_last['rainmm'].fillna(0))) * constants.mPmm
#df_mean['cumsum_net_water_pos_out_m']=np.cumsum(df_mean['net_water_pos_out_mPday'])
df_last['total_water_in_m'].loc[datetime.datetime(2019,03,28,12,00)]=np.cumsum(df_last['rainmm'].fillna(0))*constants.mPmm + 0.02
df_last['total_water_in_m'].loc[datetime.datetime(2020,01,18,12,00)]=np.cumsum(df_last['rainmm'].fillna(0))*constants.mPmm + 0.07
df_last['total_water_in_m'].loc[datetime.datetime(2020,02,06,12,00)]=np.cumsum(df_last['rainmm'].fillna(0))*constants.mPmm + 0.14



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
#plt.plot(df_mean.index,df_mean['cumsum_net_water_pos_out_m']*1000,'-c',label='From weather station')
#plt.plot(df_mean.index,(85.-df_mean['total_moisture_cm'])*0.01*1000,'brown',label='From moisture profile')
plt.plot(df_mean.index,df_mean['cumsum_net_water_storage_m']*1000+900,'-c',linewidth=1.7,label='Calculated from weather station')
#plt.plot(df_mean.index[mask2],df_mean['cumsum_net_water_storage_m'][mask2]*1000+1200,'-c',linewidth=1.7,label='Calculated from weather station')
plt.plot(df_mean.index,(df_mean['total_moisture_cm'])*0.01*1000-20,'brown',linewidth=1.7,label='Calculated from moisture profile')
ax.set_ylim([0,900])



#ax.xaxis.set_major_formatter(mdates.DateFormatter('%b/%d'))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b/%y'))
ax.set_xlabel('DATE',fontsize=12)
#ax.set_ylabel('WATER LOSS FROM COLUMN (mm)')
ax.set_ylabel('EQUIVALENT WATER STORAGE IN COLUMN (mm)',fontsize=12, labelpad=10)
ax.legend(bbox_to_anchor=(0.1, 0.99 ), loc='upper left', borderaxespad=0.,fontsize=12,handletextpad=0.6,labelspacing=1,ncol=1,columnspacing=0.1)
ax.grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
fig.savefig('figure/update/plot_water_balance_over_time.png', format='png', dpi=100)
