# -*- coding: utf-8 -*-
"""
Created on Wed May  5 09:15:23 2021

@author: s4680073
"""
import py_compile
import os
import sys
import json
import pandas as pd
import numpy as np

import matplotlib
#matplotlib.use('Agg')
# %matplotlib qt  # run this 
import matplotlib.pyplot as plt
# plt.ioff()  # disable poping out figure automatically
# # recompile post_processing in case update are required
# pyduino_path = os.environ['pyduino']
# print(os.environ['pyduino'])
# sys.path.append(os.path.join(pyduino_path,'python','post_processing'))
# py_compile.compile(
#     os.path.join(pyduino_path,'python','post_processing',
#                  'thingsboard_to_pandas_py3.py'))
import thingsboard_to_pandas_py3
pump=pd.read_csv('C:/Project/MBDA/pump.csv')
# pump.index=pump['time']
format = '%Y.%m.%d %H:%M'
pump['date_time'] = pd.to_datetime(pump['time'], format=format)
pump=pump.set_index(pd.DatetimeIndex(pump['date_time']))
del pump['time']
del pump['date_time']
pump=pump.interpolate(method='linear')
# plt.plot(pump['meter'])
# pump=pump-pump['meter'][0]
plot_interpolate=True
sp_sch.merge_data_from_tb(
        input_time_series=pump.index, 
        input_data_series=pump['meter'], 
        output_time_series=sp_sch.df.index,key_name='pump' ,
        plot=plot_interpolate  ,coef=1.e-2,rm_nan=True)
plt.close()
sp_sch.df['pump']=sp_sch.df['pump']-sp_sch.df['pump'][0]
sp_sch.df['pumpMLPday']=np.zeros(sp_sch.df['pump'].size)
sp_sch.df['pumpMLPday'][0]=0
sp_sch.df['pumpMLPday'][1:]=86400*(np.diff(sp_sch.df['pump'])/sp_input['delta_t_s'])
sp_sch.df['pumpMLPday'][sp_sch.df['pumpMLPday']<0.2]=0
plt.plot(sp_sch.df['pump'])

plt.plot(sp_sch.df['pumpMLPday'])
plt.title('pumping rate (ML/day)')
plt.tight_layout()
plt.savefig("pumping rate.png",dpi=300)

sp_sch.df['pet_volume_MLPDAY']=sp_sch.df['pet_mmPday']*constants.mm2m*sp_sch.df['areaTOTAL']/1000/86400
df_mean = sp_sch.df.resample('D').mean()
# plt.plot(df_mean['pet_volume_MLPDAY'])
# plt.plot(df_mean['pet_mmPday'])
# plt.plot(df_mean['recharge_mmPday'])


df_cumsum=sp_sch.df.cumsum()
df_cumsum['infiltration_ML']=sp_sch.df['pump']-sp_sch.df['volumeTOTALML']-df_cumsum['pet_volume_MLPDAY']*sp_input['delta_t_s']
plt.plot(sp_sch.df['pump'],label='Accumulative pumped water volume (ML)')
plt.plot(sp_sch.df['volumeTOTALML'],label='Volume of the surface water body (ML)')
plt.plot(sp_sch.df['pump']-sp_sch.df['volumeTOTALML'],label='Accumulative pump volume minus volume of water body(ML)')
# plt.plot(sp_sch.df['volumeTOTALML'],label='Volume of water body (ML)')
plt.plot(df_cumsum['pet_volume_MLPDAY']*sp_input['delta_t_s'],label='Accumulative PET (ML)')
plt.plot(df_cumsum['infiltration_ML'],label='Infiltration into unsaturated zone (ML)')
plt.xlim(datetime.date(2021, 3, 17), datetime.date(2021, 6, 2))

# plt.set_ylabel('POTENTIAL\nEVAP.\nRATE\n(mm/Day)', fontsize=y_fontsize, labelpad=10)
# plt.grid(True)
# plt.legend()
# depthmean=np.zeros(depth[:,0,0].size)
# depthnozero=depth
# depthnozero[depthnozero==0]=np.nan
# for i in range(depth[:,0,0].size):
#     depthmean[i]=np.nanmean(depthnozero[i,:,:])
# volumemean={}
# volumemeanML=areaTOTAL*depthmean/1000
# plt.plot(volumemeanML)
# plt.plot(volumeTOTALML)