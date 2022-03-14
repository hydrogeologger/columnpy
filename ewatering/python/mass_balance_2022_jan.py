# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 10:18:35 2022

@author: s4680073
"""


exec(open('C:\columnpy\columnpy\ewatering\python\\adjust_value.py').read())
exec(open('C:\columnpy\columnpy\ewatering\python\get_data_py3_jan_2022.py').read())
# filename  = "C:/Project/MDBA/areasWGS84.tif"
# dem  = "C:/Project/MDBA/dem/north_channel.tif"
# exec(open('C:\columnpy\columnpy\ewatering\python\calc_area.py').read())
# exec(open('C:\columnpy\columnpy\ewatering\python\calc_evap.py').read())
# exec(open('C:\columnpy\columnpy\ewatering\python\\read_pump_meter.py').read())
# sp_sch.df['pet_volume_channel_ML']    =    df_cumsum['pet_volume_ML']
# sp_sch.df['rainfall_volume_channel_ML']    =    df_cumsum['rainfall_volume_ML']

# sp_sch.df['infiltration_channel_ML']  =    df_cumsum['infiltration_ML']
# sp_sch.df['areaTOTAL_channel_m2']     =    sp_sch.df['areaTOTAL_m2']
# sp_sch.df['volumeTOTAL_channel_ML']   =    sp_sch.df['volumeTOTAL_ML']
# sp_sch.df['areaTOTAL_channel_m2'].loc['2021-03-15':'2021-03-23']=0
# sp_sch.df['volumeTOTAL_channel_ML'].loc['2021-03-15':'2021-03-23']=0
# # sp_sch.df['volumeTOTAL_channel_ML'].loc['2022-01-18':'2022-01-25']=0


# sp_sch.df['areaTOTAL_basin_m2'].loc['2021-03-15':'2021-03-23']=0
# sp_sch.df['volumeTOTAL_basin_ML'].loc['2021-03-15':'2021-03-23']=0
# sp_sch.df['volumeTOTAL_basin_ML'].loc['2022-01-18':'2022-01-25']=0

dem  = "C:/Project/MDBA/dem/entire_basin.tif"
# filename  = "C:/Project/MDBA/upper_channel.tif"
exec(open('C:\columnpy\columnpy\ewatering\python\calc_area.py').read())
exec(open('C:\columnpy\columnpy\ewatering\python\calc_evap.py').read())
exec(open('C:\columnpy\columnpy\ewatering\python\\read_pump_meter.py').read())

# df_cumsum['pet_volume_channel_ML']      =    sp_sch.df['pet_volume_channel_ML']
# df_cumsum['rainfall_volume_channel_ML'] =    sp_sch.df['rainfall_volume_channel_ML']
# # df_cumsum['infiltration_channel_ML']  =    sp_sch.df['infiltration_channel_ML']
# df_cumsum['pet_volume_basin_ML']        =    sp_sch.df['pet_volume_basin_ML']
# df_cumsum['rainfall_volume_basin_ML']   =    sp_sch.df['rainfall_volume_basin_ML']
# df_cumsum['infiltration_basin_ML']      =    sp_sch.df['infiltration_basin_ML']

plt.rcParams.update({
    "font.weight": "bold",
    "font.size": 18,
    # "figure.figsize": (9,6),
    "xtick.major.size": 5,
    "xtick.major.pad": 7,
    "xtick.labelsize": 16,
    "ytick.labelsize": 16,
    "axes.labelweight": 'bold',
    "grid.color": "0.5",
    "grid.linestyle": "-",
    "grid.linewidth": 2,
    "lines.linewidth": 4,
    "lines.color": "g",
    "axes.linewidth": 4,
    "legend.fontsize" : 16, 
    "legend.loc":'lower right',
    "legend.framealpha": 0.5,
})


plt.figure()
# plt.plot(volumeTOTALML_channel)
# plt.plot(volumeTOTALML_basin)
# plt.plot(volumeTOTALML_basin-volumeTOTALML_channel)
fig = plt.figure(figsize=(12, 9))
gs = gridspec.GridSpec(nrows=1, ncols=1)                     
fig.subplots_adjust(hspace=.20)
fig.subplots_adjust(left=0.1, right=0.99, top=0.97, bottom=0.05) 
levels = np.arange(0, 1.2, 0.05)
# fig.suptitle(f'Adjustable value (m) at SA2={SA2_water_depth_adjust} pumping scale={pump_scale} \n areascale={area_scale} plant_percent={plant_percentage1*100}%',font='font_title')
ax0 = fig.add_subplot(gs[0, 0])  

ax0.plot(sp_sch.df['pump'],color='r',label='Cumulative pumped water volume (ML)')
ax0.plot(sp_sch.df['volumeTOTAL_ML'],color='pink',label='Volume of the surface water body with the northern channel(ML)')

# ax0.plot(sp_sch.df['pump']-sp_sch.df['volumeTOTALML'],label='Cumulative pump volume minus volume of water body(ML)')
# plt.plot(sp_sch.df['volumeTOTALML'],label='Volume of water body (ML)')
ax0.plot(df_cumsum['pet_volume_ML'],color='g',label='Cumulative PET (ML)')
ax0.plot(df_cumsum['rainfall_volume_ML'],color='purple',label='Cumulative rainfall volume (ML)')
ax0.plot(df_cumsum['infiltration_ML'],color='k',label='Infiltration with the northern channel (ML)')
ax0.xaxis.set_major_formatter(mdates.DateFormatter('%b/%Y'))
ax0.grid(True,which="both",ls=":",color = '0.5')

ax0.set_ylabel('Volume of water (ML)',  labelpad=10)
ax0.set_xlabel('Time', labelpad=10)
# ax0.legend(loc=[0,1.05],fontsize=font_legend)
# ax0.legend(loc=[1.01,0.55],fontsize=font_legend)
ax0.legend(loc='upper right')
# ax0.set_title('Time', fontsize=label_fontsize, labelpad=10)
# ax0.legend(loc='lower right')
plt.rcParams["font.family"] = "Arial"
plt.tight_layout()
plt.show()