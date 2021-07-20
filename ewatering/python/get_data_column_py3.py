# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 21:27:40 2021

@author: s4680073
"""

import py_compile
import os
import sys
import json
import pandas as pd
import numpy as np
import datetime
import matplotlib
import matplotlib.dates as mdates

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
#reload(thingsboard_to_pandas_py3)
fontsize_label=20

tb_pandas=thingsboard_to_pandas_py3.tingsboard_to_pandas('C:/pyduino/pyduino/python/tb_to_csv/tb_credential_column.json')

# input is the location of the json file
# use the below command to show the comments on tb_credential.json
# print tb_pandas.input_json['comments'] 




tb_pandas.get_token()    # get the token associated with the account
tb_pandas.get_keys()     # list of keys in the device
tb_pandas.get_data()     # obtain data from thingsboard stored at tb_pandas['results']
tb_pandas.convert_data_to_df()  # convert each datasets to pandas dataframe



#'ec1,ec2,ec3,ec4,ec5,ec6,ec_piezo1,p1_cs451,p2_cs451,p3_cs451,p_5802,p_5802_2,p_piezo1,rainfall,raw2,raw3,raw4,raw5,raw6,rh_logger,sa1_ec1,sa1_ec2,sa1_ec3,sa1_ec4,sa1_ec5,sa1_ec_piezo,sa1_ir,sa1_p_5802,sa1_p_5803,sa1_p_piezo,sa1_raw1,sa1_raw2,sa1_raw3,sa1_raw4,sa1_raw5,sa1_rh_logger,sa1_sht31_humidity_1,sa1_sht31_temp_1,sa1_t_5802,sa1_t_5803,sa1_t_piezo,sa1_temp1,sa1_temp2,sa1_temp3,sa1_temp4,sa1_temp5,sa1_temp_logger,sa1_uv,sa1_vis,sa1_volt,sa2_ec1,sa2_ec2,sa2_ec3,sa2_ec4,sa2_ec5,sa2_ec_piezo,sa2_ir,sa2_p_5803,sa2_p_piezo,sa2_raw1,sa2_raw2,sa2_raw3,sa2_raw4,sa2_raw5,sa2_rh_logger,sa2_t_5803,sa2_t_piezo,sa2_temp1,sa2_temp2,sa2_temp3,sa2_temp4,sa2_temp5,sa2_temp_logger,sa2_uv,sa2_vis,sa2_volt,sa3_ec_piezo,sa3_ir,sa3_mo1,sa3_mo2,sa3_mo3,sa3_mo4,sa3_mo5,sa3_p_5803,sa3_p_piezo,sa3_rh_logger,sa3_t_5803,sa3_t_piezo,sa3_temp_logger,sa3_uv,sa3_vis,sa3_volt,sa4_ec_piezo,sa4_p_piezo,sa4_t_piezo,sht31_humidity_1,sht31_temp_1,t1_cs451,t2_cs451,t3_cs451,t_5802,t_5802_2,t_piezo1,temp2,temp3,temp4,temp5,temp6,temp_logger,volt,wind_direction,wind_speed'

## check the length of each pandas
#for i in list(tb_pandas.result_df):
#    print( i +' ' + str(len(   tb_pandas.result_df[i]   ))     )
#    print( i + len(i)     )


#tb_pandas.plot_df(['sa3_uv','sa3_vis'])

# small optation to the failed measurement

#tb_pandas.result_df['temp_2']['value'] [ tb_pandas.result_df['temp_2']['value'] <5  ] =np.nan 

#tb_pandas.result_df['scale1']['value'] [ tb_pandas.result_df['scale1']['value'] <5  ] =np.nan 

# merge data    
with open('C:/pyduino/pyduino/python/tb_to_csv/schedule_column.json') as data_file:    
    sp_input = json.load(data_file)
# with open('C:/pyduino/pyduino/python/tb_to_csv/schedule_column.json') as data_file:    
#     sp_input = json.load(data_file)

#sys.path.append   (os.environ['pyduino']+'/python/post_processing/')
#py_compile.compile(os.environ['pyduino']+'/python/post_processing/pandas_scale.py')
#py_compile.compile(os.environ['pyduino']+'/python/post_processing/constants.py')
#
#
#sys.path.join(os.environ['pyduino'],'python','post_processing')
#sys.path.append(os.path.join(os.environ['pyduino'],'python','post_processing'))
# py_compile.compile( os.path.join(
#         os.environ['pyduino'],'python','post_processing','pandas_scale.py')  )
# py_compile.compile( os.path.join(
#         os.environ['pyduino'],'python','post_processing','constants.py')  )

import pandas_scale_py3 as pandas_scale
import constants

# open_day='2020-03-15'
# close_day='2020-06-6'
# tb_pandas.result_df['2020-03-16':'2020-06-6']>=open_day
# con2=tb_pandas.result_df[sp_input['start_time']]<close_day
# tb_pandas.result_df=order_data[con1&con2]

sp_sch={}
#plot_interpolate=False
plot_interpolate=True

sp_sch=pandas_scale.concat_data_tb(
    pd.datetime.strptime(sp_input['start_time'],'%Y/%b/%d %H:%M'),
    pd.datetime.strptime(sp_input['end_time'],'%Y/%b/%d %H:%M'),
    sp_input['delta_t_s'] );

sp_sch.start_dt = pd.datetime.strptime(sp_input['start_time'],'%Y/%b/%d %H:%M')
sp_sch.end_dt   = pd.datetime.strptime(sp_input['end_time'  ],'%Y/%b/%d %H:%M')

# managing data
tb_pandas.result_df['column_mo1']['value'] \
    [ tb_pandas.result_df['column_mo1']['value'] >500 ] =np.nan 
tb_pandas.result_df['column_mo2']['value'] \
    [ tb_pandas.result_df['column_mo2']['value'] >500 ] =np.nan 
tb_pandas.result_df['column_mo3']['value'] \
    [ tb_pandas.result_df['column_mo3']['value'] >500 ] =np.nan 
tb_pandas.result_df['column_mo4']['value'] \
    [ tb_pandas.result_df['column_mo4']['value'] >500 ] =np.nan 
tb_pandas.result_df['column_mo5']['value'] \
    [ tb_pandas.result_df['column_mo5']['value'] >500 ] =np.nan 
mask = np.where(
        np.abs(np.diff(tb_pandas.result_df['column_mo5']['value']))>0.5)[0]
tb_pandas.result_df['column_mo5']['value'] [mask]=np.nan 
mask = np.where(
        np.abs(np.diff(tb_pandas.result_df['scale']['value']))>0.5)[0]
tb_pandas.result_df['scale']['value'] [mask]=np.nan 
sp_sch.merge_data_from_tb(
        input_time_series=tb_pandas.result_df['column_mo1'].index, 
        input_data_series=tb_pandas.result_df['column_mo1']['value'], 
        output_time_series=sp_sch.df.index,key_name='column_mo1' ,
        plot=plot_interpolate  ,coef=5e-12,rm_nan=True)
sp_sch.merge_data_from_tb(
        input_time_series=tb_pandas.result_df['column_mo2'].index, 
        input_data_series=tb_pandas.result_df['column_mo2']['value'], 
        output_time_series=sp_sch.df.index,key_name='column_mo2' ,
        plot=plot_interpolate  ,coef=5e-12,rm_nan=True)
sp_sch.merge_data_from_tb(
        input_time_series=tb_pandas.result_df['column_mo3'].index, 
        input_data_series=tb_pandas.result_df['column_mo3']['value'], 
        output_time_series=sp_sch.df.index,key_name='column_mo3' ,
        plot=plot_interpolate  ,coef=5e-12,rm_nan=True)
sp_sch.merge_data_from_tb(
        input_time_series=tb_pandas.result_df['column_mo4'].index, 
        input_data_series=tb_pandas.result_df['column_mo4']['value'], 
        output_time_series=sp_sch.df.index,key_name='column_mo4' ,
        plot=plot_interpolate  ,coef=5e-12,rm_nan=True)
sp_sch.merge_data_from_tb(
        input_time_series=tb_pandas.result_df['column_mo5'].index, 
        input_data_series=tb_pandas.result_df['column_mo5']['value'], 
        output_time_series=sp_sch.df.index,key_name='column_mo5' ,
        plot=plot_interpolate  ,coef=5e-12,rm_nan=True)
tb_pandas.result_df['scale'][tb_pandas.result_df['scale']<=2000]=np.nan
sp_sch.merge_data_from_tb(
        input_time_series=tb_pandas.result_df['scale'].index, 
        input_data_series=tb_pandas.result_df['scale']['value'], 
        output_time_series=sp_sch.df.index,key_name='scale' ,
        plot=plot_interpolate  ,coef=5e-11,rm_nan=True)
sp_sch.df['scale'].loc['2021-03-15':'2021-05-11 13']=np.nan
sp_sch.df['column_mo1_volumematric_moisture']=( 523-sp_sch.df['column_mo1'])/(523-269)*porosity
sp_sch.df['column_mo2_volumematric_moisture']=( 410-sp_sch.df['column_mo2'])/(410-269)*porosity
sp_sch.df['column_mo3_volumematric_moisture']=( 410-sp_sch.df['column_mo3'])/(410-269)*porosity
sp_sch.df['column_mo4_volumematric_moisture']=( 450-sp_sch.df['column_mo4'])/(450-269)*porosity
sp_sch.df['column_mo5_volumematric_moisture']=( 410-sp_sch.df['column_mo5'])/(410-269)*porosity
plt.plot(sp_sch.df['scale'])
fig, ax = plt.subplots(figsize=[30,9])
plt.setp(ax.spines.values(), linewidth=2)
ax.plot(sp_sch.df['column_mo1_volumematric_moisture'],label='10cm below surface')
ax.plot(sp_sch.df['column_mo2_volumematric_moisture'],label='20cm below surface')
ax.plot(sp_sch.df['column_mo3_volumematric_moisture'],label='30cm below surface')
ax.plot(sp_sch.df['column_mo4_volumematric_moisture'],label='50cm below surface')
ax.plot(sp_sch.df['column_mo5_volumematric_moisture'],label='70cm below surface')
ax.legend(loc=[0.79,0.5],fontsize=26)
ax.set_xlabel('Time',weight='bold',fontsize=35)
ax.set_ylabel('Volumetric water content (-)',weight='bold',fontsize=35)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b/%d'))
ax.set_xlim(datetime.date(2021, 4, 24), datetime.date(2021, 6, 5))
plt.xticks(fontsize=28, rotation=0)
plt.yticks(fontsize=28, rotation=0)
plt.grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
plt.savefig('Column_moisture_sensor.png',dpi=300,bbox_inches = 'tight',
    pad_inches = 0)



sp_sch_30min=sp_sch.df.resample('30T').ffill()

sp_sch_30min['column_mo1_volumematric_moisture']=( 523-sp_sch_30min['column_mo1'])/(523-269)*porosity
sp_sch_30min['column_mo2_volumematric_moisture']=( 523-sp_sch_30min['column_mo2'])/(523-269)*porosity
sp_sch_30min['column_mo3_volumematric_moisture']=( 523-sp_sch_30min['column_mo3'])/(523-269)*porosity
sp_sch_30min['column_mo4_volumematric_moisture']=( 523-sp_sch_30min['column_mo4'])/(523-269)*porosity
sp_sch_30min['column_mo5_volumematric_moisture']=( 523-sp_sch_30min['column_mo5'])/(523-269)*porosity
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b/%d'))
ax.legend(loc='upper right')
ax.set_xlim([datetime.date(2021, 4, 24), datetime.date(2021, 6, 5)])
ax.set_xlabel('Time',weight='bold',fontsize=fontsize_label)
ax.set_ylabel('Moisture sensor reading',weight='bold',fontsize=fontsize_label)
plt.savefig('Column_moisture sensor.png',dpi=300)
fig, ax = plt.subplots(figsize=[16,9])
ax.plot(sp_sch.df['scale'],label='Mass of Mariotte bottle')
ax.set_xlim([datetime.date(2021, 5, 12), datetime.date(2021, 6, 5)])
ax.set_ylim(6000,10000)


