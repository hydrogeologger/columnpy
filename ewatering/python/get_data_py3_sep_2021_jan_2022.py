# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 09:18:37 2022

@author: s4680073
"""

import constants
import pandas_scale_py3 as pandas_scale
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
#reload(thingsboard_to_pandas_py3)


# tb_pandas = thingsboard_to_pandas_py3.tingsboard_to_pandas(
#     'C:/pyduino/pyduino/python/tb_to_csv/tb_credential_mar_2021_oct_2021.json')
tb_pandas = thingsboard_to_pandas_py3.tingsboard_to_pandas(
    'C:/pyduino/pyduino/python/tb_to_csv/tb_credential_sep_2021_jan_2022.json')
# input is the location of the json file
# use the below command to show the comments on tb_credential.json
# print tb_pandas.input_json['comments']


tb_pandas.get_token()    # get the token associated with the account
tb_pandas.get_keys()     # list of keys in the device
# obtain data from thingsboard stored at tb_pandas['results']
tb_pandas.get_data()
tb_pandas.convert_data_to_df()  # convert each datasets to pandas dataframe
# tb_pandas.result_df.astype(np.float32)

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
# with open('C:/pyduino/pyduino/python/tb_to_csv/schedule_mar_2021_oct_2021.json') as data_file:
#     sp_input = json.load(data_file)
with open('C:/pyduino/pyduino/python/tb_to_csv/schedule_sep_2021_jan_2022.json') as data_file:
    sp_input = json.load(data_file)

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


sp_sch = {}
#plot_interpolate=False
plot_interpolate = False

sp_sch = pandas_scale.concat_data_tb(
    pd.datetime.strptime(sp_input['start_time'], '%Y/%b/%d %H:%M'),
    pd.datetime.strptime(sp_input['end_time'], '%Y/%b/%d %H:%M'),
    sp_input['delta_t_s'])

sp_sch.start_dt = pd.datetime.strptime(
    sp_input['start_time'], '%Y/%b/%d %H:%M')
sp_sch.end_dt = pd.datetime.strptime(sp_input['end_time'], '%Y/%b/%d %H:%M')

# managing data

sp_sch.merge_data_from_tb(
    input_time_series=tb_pandas.result_df['sa2_uv'].index,
    input_data_series=tb_pandas.result_df['sa2_uv']['value'],
    output_time_series=sp_sch.df.index, key_name='sa2_uv',
    plot=plot_interpolate, coef=5e-11, rm_nan=True)
sp_sch.merge_data_from_tb(
    input_time_series=tb_pandas.result_df['sa1_uv'].index,
    input_data_series=tb_pandas.result_df['sa1_uv']['value'],
    output_time_series=sp_sch.df.index, key_name='sa1_uv',
    plot=plot_interpolate, coef=5e-11, rm_nan=True)
#CM210408 done

tb_pandas.result_df['sa1_sht31_temp_1']['value'][tb_pandas.result_df['sa1_sht31_temp_1']
                                                 ['value'] > 60] = np.nan
sp_sch.merge_data_from_tb(
    input_time_series=tb_pandas.result_df['sa1_sht31_temp_1'].index,
    input_data_series=tb_pandas.result_df['sa1_sht31_temp_1']['value'],
    output_time_series=sp_sch.df.index, key_name='sa1_sht31_temp_1',
    plot=plot_interpolate, coef=5e-8, rm_nan=True)
#CM210408 done

sp_sch.merge_data_from_tb(
    input_time_series=tb_pandas.result_df['sa1_sht31_humidity_1'].index,
    input_data_series=tb_pandas.result_df['sa1_sht31_humidity_1']['value'],
    output_time_series=sp_sch.df.index, key_name='sa1_sht31_humidity_1',
    plot=plot_interpolate, coef=5e-8, rm_nan=True)
#CM210408 done

sp_sch.merge_data_from_tb(
    input_time_series=tb_pandas.result_df['rainfall'].index,
    input_data_series=tb_pandas.result_df['rainfall']['value'],
    output_time_series=sp_sch.df.index, key_name='rainfall',
    plot=plot_interpolate, coef=5e-6, rm_nan=True)
mask = np.where(sp_sch.df['rainfall'] < 0)[0]
sp_sch.df['rainfall'][mask] = 0
#find way to delete the value that comes with a abrupt change of values
#sum(np.abs(np.diff(tb_pandas.result_df['p3_cs451']['value']))>2)
# 0.5 is found by the difference between the neibouring data
mask = np.where(
    np.abs(np.diff(tb_pandas.result_df['p3_cs451']['value'])) > 0.5)[0]
tb_pandas.result_df['p3_cs451']['value'][mask] = np.nan

coef_3 = 4.e-12
coef_2 = 1.e-13
# sp_sch.merge_data_from_tb(
#         input_time_series=tb_pandas.result_df['p3_cs451'].index,
#         input_data_series=tb_pandas.result_df['p3_cs451']['value'],
#         output_time_series=sp_sch.df.index,key_name='p3_cs451' ,
#         plot=False  ,coef=coef_3,rm_nan=True)
sp_sch.merge_data_from_tb(
    input_time_series=tb_pandas.result_df['p3_cs451'].index,
    input_data_series=tb_pandas.result_df['p3_cs451']['value'],
    output_time_series=sp_sch.df.index, key_name='p3_cs451',
    plot=plot_interpolate, coef=coef_3, rm_nan=True)
sp_sch.merge_data_from_tb(
    input_time_series=tb_pandas.result_df['p3_cs451'].index,
    input_data_series=tb_pandas.result_df['p3_cs451']['value'],
    output_time_series=sp_sch.df.index, key_name='p3_cs451_coef100',
    plot=plot_interpolate, coef=coef_3/cs451_scale, rm_nan=True)
#CM210408 done


mask = np.where(
    np.abs(np.diff(tb_pandas.result_df['p2_cs451']['value'])) > 0.5)[0]
tb_pandas.result_df['p2_cs451']['value'][mask] = np.nan
mask = np.where(
    np.abs(tb_pandas.result_df['p2_cs451']['value']) > 1000)[0]
tb_pandas.result_df['p2_cs451']['value'][mask] = np.nan

# sp_sch.merge_data_from_tb(
#         input_time_series=tb_pandas.result_df['p2_cs451'].index,
#         input_data_series=tb_pandas.result_df['p2_cs451']['value'],
#         output_time_series=sp_sch.df.index,key_name='p2_cs451_coef100' ,
#         plot=plot_interpolate ,coef=coef_2//100,rm_nan=True)
sp_sch.merge_data_from_tb(
    input_time_series=tb_pandas.result_df['p2_cs451'].index,
    input_data_series=tb_pandas.result_df['p2_cs451']['value'],
    output_time_series=sp_sch.df.index, key_name='p2_cs451_coef100',
    plot=plot_interpolate, coef=coef_2/cs451_scale, rm_nan=True)
#CM210408
sp_sch.merge_data_from_tb(
    input_time_series=tb_pandas.result_df['p2_cs451'].index,
    input_data_series=tb_pandas.result_df['p2_cs451']['value'],
    output_time_series=sp_sch.df.index, key_name='p2_cs451',
    plot=plot_interpolate, coef=coef_2, rm_nan=True)
sp_sch.df['pond_falling_rate_cs451_2_mmPday'] = \
    np.append(np.diff(sp_sch.df['p2_cs451']), np.nan) \
    / sp_input['delta_t_s']*constants.msPmmday
sp_sch.df['pond_falling_rate_cs451_3_mmPday'] = \
    np.append(np.diff(sp_sch.df['p3_cs451']), np.nan) \
    / sp_input['delta_t_s']*constants.msPmmday

# fig=plt.figure()
# plt.scatter(x= sp_sch.df.index, y=sp_sch.df['pond_falling_rate_cs451_2_mmPday']
#     ,color=['blue'])
# plt.scatter(x= sp_sch.df.index, y=sp_sch.df['pond_falling_rate_cs451_3_mmPday']
#     ,color=['red'])
# fig.suptitle('red3'+str(coef_3)+'blue2'+str(coef_2), fontsize=20)

axes = plt.gca()
axes.set_ylim([-200, 500])

tb_pandas.result_df['sa1_t_piezo']['value'][tb_pandas.result_df['sa1_t_piezo']
                                            ['value'] > 21.5] = np.nan
tb_pandas.result_df['sa1_t_piezo']['value'][tb_pandas.result_df['sa1_t_piezo']
                                            ['value'] < 15] = np.nan
sp_sch.merge_data_from_tb(
    input_time_series=tb_pandas.result_df['sa1_t_piezo'].index,
    input_data_series=tb_pandas.result_df['sa1_t_piezo']['value'],
    output_time_series=sp_sch.df.index, key_name='sa1_t_piezo',
    plot=plot_interpolate, coef=5e-10, rm_nan=True)
tb_pandas.result_df['sa2_t_piezo']['value'][tb_pandas.result_df['sa2_t_piezo']
                                            ['value'] > 22] = np.nan
sp_sch.merge_data_from_tb(
    input_time_series=tb_pandas.result_df['sa2_t_piezo'].index,
    input_data_series=tb_pandas.result_df['sa2_t_piezo']['value'],
    output_time_series=sp_sch.df.index, key_name='sa2_t_piezo',
    plot=plot_interpolate, coef=5e-13, rm_nan=True)
sp_sch.merge_data_from_tb(
    input_time_series=tb_pandas.result_df['sa3_t_piezo'].index,
    input_data_series=tb_pandas.result_df['sa3_t_piezo']['value'],
    output_time_series=sp_sch.df.index, key_name='sa3_t_piezo',
    plot=plot_interpolate, coef=5e-13, rm_nan=True)
tb_pandas.result_df['sa4_t_piezo']['value'][tb_pandas.result_df['sa4_t_piezo']
                                            ['value'] > 25] = np.nan
tb_pandas.result_df['sa4_t_piezo']['value'][tb_pandas.result_df['sa4_t_piezo']
                                            ['value'] < 19.5] = np.nan
sp_sch.merge_data_from_tb(
    input_time_series=tb_pandas.result_df['sa4_t_piezo'].index,
    input_data_series=tb_pandas.result_df['sa4_t_piezo']['value'],
    output_time_series=sp_sch.df.index, key_name='sa4_t_piezo',
    plot=plot_interpolate, coef=5e-11, rm_nan=True)
sp_sch.df['sa4_t_piezo'].loc['2021-03-15':'2021-03-18 11'] = np.nan

sp_sch.merge_data_from_tb(
    input_time_series=tb_pandas.result_df['sa2_temp1'].index,
    input_data_series=tb_pandas.result_df['sa2_temp1']['value'],
    output_time_series=sp_sch.df.index, key_name='sa2_temp1',
    plot=plot_interpolate, coef=5e-10, rm_nan=True)

sp_sch.merge_data_from_tb(
    input_time_series=tb_pandas.result_df['sa2_temp2'].index,
    input_data_series=tb_pandas.result_df['sa2_temp2']['value'],
    output_time_series=sp_sch.df.index, key_name='sa2_temp2',
    plot=plot_interpolate, coef=5e-10, rm_nan=True)
sp_sch.merge_data_from_tb(
    input_time_series=tb_pandas.result_df['sa2_temp3'].index,
    input_data_series=tb_pandas.result_df['sa2_temp3']['value'],
    output_time_series=sp_sch.df.index, key_name='sa2_temp3',
    plot=plot_interpolate, coef=5e-10, rm_nan=True)
sp_sch.merge_data_from_tb(
    input_time_series=tb_pandas.result_df['sa2_temp4'].index,
    input_data_series=tb_pandas.result_df['sa2_temp4']['value'],
    output_time_series=sp_sch.df.index, key_name='sa2_temp4',
    plot=plot_interpolate, coef=5e-10, rm_nan=True)
sp_sch.merge_data_from_tb(
    input_time_series=tb_pandas.result_df['sa2_temp5'].index,
    input_data_series=tb_pandas.result_df['sa2_temp5']['value'],
    output_time_series=sp_sch.df.index, key_name='sa2_temp5',
    plot=plot_interpolate, coef=5e-10, rm_nan=True)
sp_sch.merge_data_from_tb(
    input_time_series=tb_pandas.result_df['t2_cs451'].index,
    input_data_series=tb_pandas.result_df['t2_cs451']['value'],
    output_time_series=sp_sch.df.index, key_name='t2_cs451',
    plot=plot_interpolate, coef=5e-10, rm_nan=True)
sp_sch.merge_data_from_tb(
    input_time_series=tb_pandas.result_df['t3_cs451'].index,
    input_data_series=tb_pandas.result_df['t3_cs451']['value'],
    output_time_series=sp_sch.df.index, key_name='t3_cs451',
    plot=plot_interpolate, coef=5e-10, rm_nan=True)


sp_sch.merge_data_from_tb(
    input_time_series=tb_pandas.result_df['sa1_p_piezo'].index,
    input_data_series=tb_pandas.result_df['sa1_p_piezo']['value'],
    output_time_series=sp_sch.df.index, key_name='sa1_p_piezo',
    plot=plot_interpolate, coef=5e-10, rm_nan=True)

tb_pandas.result_df['sa2_p_piezo']['value'][tb_pandas.result_df['sa2_p_piezo']
                                            ['value'] < 60] = np.nan

# sp_sch.merge_data_from_tb(
#         input_time_series=tb_pandas.result_df['sa2_p_piezo'].index,
#         input_data_series=tb_pandas.result_df['sa2_p_piezo']['value'],
#         output_time_series=sp_sch.df.index,key_name='sa2_p_piezo' ,
#         plot=plot_interpolate  ,coef=5e-3,rm_nan=True)

sp_sch.merge_data_from_tb(
    input_time_series=tb_pandas.result_df['sa2_p_piezo'].index,
    input_data_series=tb_pandas.result_df['sa2_p_piezo']['value'],
    output_time_series=sp_sch.df.index, key_name='sa2_p_piezo',
    plot=plot_interpolate, coef=5e-7, rm_nan=True)


sp_sch.merge_data_from_tb(
    input_time_series=tb_pandas.result_df['sa3_p_piezo'].index,
    input_data_series=tb_pandas.result_df['sa3_p_piezo']['value'],
    output_time_series=sp_sch.df.index, key_name='sa3_p_piezo',
    plot=plot_interpolate, coef=5e-7, rm_nan=True)

tb_pandas.result_df['sa4_p_piezo']['value'][tb_pandas.result_df['sa4_p_piezo']
                                            ['value'] < 103] = np.nan

sp_sch.merge_data_from_tb(
    input_time_series=tb_pandas.result_df['sa4_p_piezo'].index,
    input_data_series=tb_pandas.result_df['sa4_p_piezo']['value'],
    output_time_series=sp_sch.df.index, key_name='sa4_p_piezo',
    plot=plot_interpolate, coef=5e-7, rm_nan=True)
sp_sch.df['sa4_p_piezo'].loc['2021-03-15':'2021-03-18 01'] = np.nan
sp_sch.df['sa1_p_piezo'].loc['2022-01-01':'2022-01-05 01'] = np.nan
sp_sch.df['sa2_p_piezo'].loc['2022-01-01':'2022-01-05 01'] = np.nan
sp_sch.df['sa3_p_piezo'].loc['2022-01-01':'2022-01-05 01'] = np.nan
sp_sch.df['sa4_p_piezo'].loc['2022-01-01':'2022-01-05 01'] = np.nan

# time_start = np.datetime64('2021-03-16T00:00')
# time_end   = np.datetime64('2021-04-27T15:00')
# sp_sch.df.loc[time_start:time_end,'sa4_p_piezo']=np.nan
#tb_pandas.plot_df(['sa4_p_piezo','sa3_p_piezo'])
#plt.figure()
#
#plt.scatter(x= sp_sch.df.index, y=sp_sch.df['sa3_p_piezo'],color=['blue'])
#plt.scatter(x= sp_sch.df.index, y=sp_sch.df['sa4_p_piezo'],color=['red'])

tb_pandas.result_df['sa1_p_5803']['value'][tb_pandas.result_df['sa1_p_5803']
                                           ['value'] > 6000] = np.nan
sp_sch.merge_data_from_tb(
    input_time_series=tb_pandas.result_df['sa1_p_5803'].index,
    input_data_series=tb_pandas.result_df['sa1_p_5803']['value'],
    output_time_series=sp_sch.df.index, key_name='sa1_p_5803',
    plot=plot_interpolate, coef=5e-8, rm_nan=True)


mask = np.where(
    np.abs(np.diff(tb_pandas.result_df['sa2_p_5803']['value'])) > 3)[0]
tb_pandas.result_df['sa2_p_5803']['value'][mask] = np.nan

tb_pandas.result_df['sa2_p_5803']['value'][tb_pandas.result_df['sa2_p_5803']
                                           ['value'] > 6000] = np.nan
sp_sch.merge_data_from_tb(
    input_time_series=tb_pandas.result_df['sa2_p_5803'].index,
    input_data_series=tb_pandas.result_df['sa2_p_5803']['value'],
    output_time_series=sp_sch.df.index, key_name='sa2_p_5803',
    plot=plot_interpolate, coef=5e-4, rm_nan=True)


mask = np.where(
    np.abs(np.diff(tb_pandas.result_df['sa3_p_5803']['value'])) > 3)[0]
tb_pandas.result_df['sa3_p_5803']['value'][mask] = np.nan

#tb_pandas.result_df['sa3_p_5803']['value'] \
#    [ tb_pandas.result_df['sa3_p_5803']['value'] >6000 ] =np.nan
sp_sch.merge_data_from_tb(
    input_time_series=tb_pandas.result_df['sa3_p_5803'].index,
    input_data_series=tb_pandas.result_df['sa3_p_5803']['value'],
    output_time_series=sp_sch.df.index, key_name='sa3_p_5803',
    plot=plot_interpolate, coef=5e-4, rm_nan=True)


sp_sch.df['sa1_p_kpa'] = sp_sch.df['sa1_p_piezo'] -  \
    sp_sch.df['sa1_p_5803']/10
sp_sch.df['sa2_p_kpa'] = sp_sch.df['sa2_p_piezo'] -  \
    sp_sch.df['sa1_p_5803']/10
sp_sch.df['sa3_p_kpa'] = sp_sch.df['sa3_p_piezo'] -  \
    sp_sch.df['sa1_p_5803']/10
sp_sch.df['sa4_p_kpa'] = sp_sch.df['sa4_p_piezo'] -  \
    sp_sch.df['sa1_p_5803']/10

# plt.figure()
# plt.scatter(x= sp_sch.df.index, y=sp_sch.df['sa1_p_kpa'],color=['blue'])
# plt.scatter(x= sp_sch.df.index, y=sp_sch.df['sa2_p_kpa'],color=['red'])
# plt.scatter(x= sp_sch.df.index, y=sp_sch.df['sa3_p_kpa'],color=['green'])
# plt.scatter(x= sp_sch.df.index, y=sp_sch.df['sa4_p_kpa'],color=['black'])

# plt.figure()
# plt.scatter(x= sp_sch.df.index, y=sp_sch.df['p2_cs451'],color=['blue'])
# plt.scatter(x= sp_sch.df.index, y=sp_sch.df['p3_cs451'],color=['red'])


sp_sch.df['pond_falling_rate_cs451_2_mPs'] = \
    np.append(np.diff(sp_sch.df['p2_cs451']), np.nan)/sp_input['delta_t_s']
sp_sch.df['pond_falling_rate_cs451_3_mPs'] = \
    np.append(np.diff(sp_sch.df['p3_cs451']), np.nan)/sp_input['delta_t_s']


sp_sch.merge_data_from_tb(
    input_time_series=tb_pandas.result_df['wind_speed'].index,
    input_data_series=tb_pandas.result_df['wind_speed']['value'],
    output_time_series=sp_sch.df.index, key_name='wind_speed_mPs',
    plot=plot_interpolate, coef=1e-12, rm_nan=True)


sp_sch.merge_data_from_tb(
    input_time_series=tb_pandas.result_df['sa1_ec_piezo'].index,
    input_data_series=tb_pandas.result_df['sa1_ec_piezo']['value'],
    output_time_series=sp_sch.df.index, key_name='sa1_ec_piezo',
    plot=plot_interpolate, coef=5e-15, rm_nan=True)

sp_sch.merge_data_from_tb(
    input_time_series=tb_pandas.result_df['sa2_ec_piezo'].index,
    input_data_series=tb_pandas.result_df['sa2_ec_piezo']['value'],
    output_time_series=sp_sch.df.index, key_name='sa2_ec_piezo',
    plot=plot_interpolate, coef=5e-13, rm_nan=True)
sp_sch.merge_data_from_tb(
    input_time_series=tb_pandas.result_df['sa3_ec_piezo'].index,
    input_data_series=tb_pandas.result_df['sa3_ec_piezo']['value'],
    output_time_series=sp_sch.df.index, key_name='sa3_ec_piezo',
    plot=plot_interpolate, coef=5e-13, rm_nan=True)
sp_sch.merge_data_from_tb(
    input_time_series=tb_pandas.result_df['sa4_ec_piezo'].index,
    input_data_series=tb_pandas.result_df['sa4_ec_piezo']['value'],
    output_time_series=sp_sch.df.index, key_name='sa4_ec_piezo',
    plot=plot_interpolate, coef=5e-15, rm_nan=True)
sp_sch.df['sa4_t_piezo'].loc['2021-03-15':'2021-03-18 11'] = np.nan
sp_sch.merge_data_from_tb(
    input_time_series=tb_pandas.result_df['sa2_ec_piezo'].index,
    input_data_series=tb_pandas.result_df['sa2_ec_piezo']['value'],
    output_time_series=sp_sch.df.index, key_name='sa2_ec_piezo',
    plot=plot_interpolate, coef=5e-13, rm_nan=True)
sp_sch.merge_data_from_tb(
    input_time_series=tb_pandas.result_df['sa3_ec_piezo'].index,
    input_data_series=tb_pandas.result_df['sa3_ec_piezo']['value'],
    output_time_series=sp_sch.df.index, key_name='sa3_ec_piezo',
    plot=plot_interpolate, coef=5e-13, rm_nan=True)
sp_sch.merge_data_from_tb(
    input_time_series=tb_pandas.result_df['sa4_ec_piezo'].index,
    input_data_series=tb_pandas.result_df['sa4_ec_piezo']['value'],
    output_time_series=sp_sch.df.index, key_name='sa4_ec_piezo',
    plot=plot_interpolate, coef=5e-13, rm_nan=True)
sp_sch.df['sa4_ec_piezo'].loc['2021-03-15':'2021-03-18 11'] = np.nan

# sp_sch.merge_data_from_tb(
#         input_time_series=tb_pandas.result_df['sa2_ir'].index,
#         input_data_series=tb_pandas.result_df['sa2_ir']['value'] /10 -25.5,
#         output_time_series=sp_sch.df.index,key_name='rn_wPm2' ,
#         plot=plot_interpolate  ,coef=5e-8,rm_nan=True)
# sp_sch.merge_data_from_tb(
#         input_time_series=tb_pandas.result_df['sa2_ir'].index,
#         input_data_series=(tb_pandas.result_df['sa2_ir']['value']-255) /20,
#         output_time_series=sp_sch.df.index,key_name='rn_wPm2' ,
#         plot=plot_interpolate  ,coef=5e-8,rm_nan=True)
sp_sch.merge_data_from_tb(
    input_time_series=tb_pandas.result_df['sa1_ir'].index,
    input_data_series=(tb_pandas.result_df['sa1_ir']['value']-255) / ir_scale,
    output_time_series=sp_sch.df.index, key_name='rn_wPm2',
    plot=plot_interpolate, coef=8e-12, rm_nan=True)

mask = np.where(sp_sch.df['rn_wPm2'] < 0)[0]
sp_sch.df['rn_wPm2'][mask] = 0
mask = np.where(sp_sch.df['rn_wPm2'] > 600)[0]
sp_sch.df['rn_wPm2'][mask] = np.nan


sp_sch.merge_data_from_tb(
    input_time_series=tb_pandas.result_df['sa2_t_5803'].index,
    input_data_series=tb_pandas.result_df['sa2_t_5803']['value'],
    output_time_series=sp_sch.df.index, key_name='sa2_t_5803',
    plot=plot_interpolate, coef=5e-8, rm_nan=True)

tb_pandas.result_df['sa2_raw1'].loc['2021-12-31':'2022-1-5']=np.nan
tb_pandas.result_df['sa2_raw2'].loc['2021-12-31':'2022-1-5']=np.nan
tb_pandas.result_df['sa2_raw3'].loc['2021-12-31':'2022-1-5']=np.nan
tb_pandas.result_df['sa2_raw4'].loc['2021-12-31':'2022-1-5']=np.nan
tb_pandas.result_df['sa2_raw5'].loc['2021-12-31':'2022-1-5']=np.nan

sp_sch.merge_data_from_tb(
    input_time_series=tb_pandas.result_df['sa2_raw1'].index,
    input_data_series=tb_pandas.result_df['sa2_raw1']['value'],
    output_time_series=sp_sch.df.index, key_name='sa2_mo1',
    plot=plot_interpolate, coef=2e-12, rm_nan=True)
sp_sch.df['sa2_mo1'][sp_sch.df['sa2_mo1'] < 1900] = np.nan
sp_sch.df['sa2_mo1'].loc['2021-5-23'] = np.nan


sp_sch.df['sa2_mo1_volumematric_moisture'] = (
    sp_sch.df['sa2_mo1']-1800)/(3095-1800)*porosity
sp_sch.merge_data_from_tb(
    input_time_series=tb_pandas.result_df['sa2_raw2'].index,
    input_data_series=tb_pandas.result_df['sa2_raw2']['value'],
    output_time_series=sp_sch.df.index, key_name='sa2_mo2',
    plot=plot_interpolate, coef=2e-12, rm_nan=True)
sp_sch.df['sa2_mo2_volumematric_moisture'] = (
    sp_sch.df['sa2_mo2']-1800)/(3050-1800)*porosity

sp_sch.merge_data_from_tb(
    input_time_series=tb_pandas.result_df['sa2_raw3'].index,
    input_data_series=tb_pandas.result_df['sa2_raw3']['value'],
    output_time_series=sp_sch.df.index, key_name='sa2_mo3',
    plot=plot_interpolate, coef=2e-12, rm_nan=True)

# sp_sch.df['sa2_mo3'][sp_sch.df['sa2_mo3']>3040]=np.nan
sp_sch.df['sa2_mo3_volumematric_moisture'] = (
    sp_sch.df['sa2_mo3']-1800)/(3028-1800)*porosity

sp_sch.merge_data_from_tb(
    input_time_series=tb_pandas.result_df['sa2_raw4'].index,
    input_data_series=tb_pandas.result_df['sa2_raw4']['value'],
    output_time_series=sp_sch.df.index, key_name='sa2_mo4',
    plot=plot_interpolate, coef=5e-12, rm_nan=True)
sp_sch.df['sa2_mo4'][sp_sch.df['sa2_mo4'] < 1900] = np.nan

sp_sch.df['sa2_mo4_volumematric_moisture'] = (
    sp_sch.df['sa2_mo4']-1800)/(2980-1800)*porosity

sp_sch.merge_data_from_tb(
    input_time_series=tb_pandas.result_df['sa2_raw5'].index,
    input_data_series=tb_pandas.result_df['sa2_raw5']['value'],
    output_time_series=sp_sch.df.index, key_name='sa2_mo5',
    plot=plot_interpolate, coef=2e-12, rm_nan=True)
sp_sch.df['sa2_mo5_volumematric_moisture'] = (
    sp_sch.df['sa2_mo5']-1800)/(3001-1800)*porosity

sp_sch.merge_data_from_tb(
    input_time_series=tb_pandas.result_df['sa2_ec1'].index,
    input_data_series=tb_pandas.result_df['sa2_ec1']['value'],
    output_time_series=sp_sch.df.index, key_name='sa2_ec1',
    plot=plot_interpolate, coef=5e-12, rm_nan=True)
sp_sch.merge_data_from_tb(
    input_time_series=tb_pandas.result_df['sa2_ec2'].index,
    input_data_series=tb_pandas.result_df['sa2_ec2']['value'],
    output_time_series=sp_sch.df.index, key_name='sa2_ec2',
    plot=plot_interpolate, coef=5e-9, rm_nan=True)
sp_sch.merge_data_from_tb(
    input_time_series=tb_pandas.result_df['sa2_ec3'].index,
    input_data_series=tb_pandas.result_df['sa2_ec3']['value'],
    output_time_series=sp_sch.df.index, key_name='sa2_ec3',
    plot=plot_interpolate, coef=5e-9, rm_nan=True)
sp_sch.merge_data_from_tb(
    input_time_series=tb_pandas.result_df['sa2_ec4'].index,
    input_data_series=tb_pandas.result_df['sa2_ec4']['value'],
    output_time_series=sp_sch.df.index, key_name='sa2_ec4',
    plot=plot_interpolate, coef=5e-9, rm_nan=True)
sp_sch.merge_data_from_tb(
    input_time_series=tb_pandas.result_df['sa2_ec5'].index,
    input_data_series=tb_pandas.result_df['sa2_ec5']['value'],
    output_time_series=sp_sch.df.index, key_name='sa2_ec5',
    plot=plot_interpolate, coef=5e-9, rm_nan=True)
sp_sch.df['sa2_ec1'][sp_sch.df['sa2_ec1'] <= 0] = 0
sp_sch.df['sa2_ec2'][sp_sch.df['sa2_ec2'] <= 0] = 0
sp_sch.df['sa2_ec3'][sp_sch.df['sa2_ec3'] <= 0] = 0
sp_sch.df['sa2_ec4'][sp_sch.df['sa2_ec4'] <= 0] = 0
sp_sch.df['sa2_ec5'][sp_sch.df['sa2_ec5'] <= 0] = 0
sp_sch.df['sa2_ec5'].loc
sp_sch.merge_data_from_tb(
    input_time_series=tb_pandas.result_df['sa1_raw1'].index,
    input_data_series=tb_pandas.result_df['sa1_raw1']['value'],
    output_time_series=sp_sch.df.index, key_name='sa1_mo1',
    plot=plot_interpolate, coef=2e-18, rm_nan=True)
sp_sch.merge_data_from_tb(
    input_time_series=tb_pandas.result_df['sa1_raw2'].index,
    input_data_series=tb_pandas.result_df['sa1_raw2']['value'],
    output_time_series=sp_sch.df.index, key_name='sa1_mo2',
    plot=plot_interpolate, coef=2e-18, rm_nan=True)

sp_sch.merge_data_from_tb(
    input_time_series=tb_pandas.result_df['sa1_raw3'].index,
    input_data_series=tb_pandas.result_df['sa1_raw3']['value'],
    output_time_series=sp_sch.df.index, key_name='sa1_mo3',
    plot=plot_interpolate, coef=2e-18, rm_nan=True)
sp_sch.merge_data_from_tb(
    input_time_series=tb_pandas.result_df['sa1_raw4'].index,
    input_data_series=tb_pandas.result_df['sa1_raw4']['value'],
    output_time_series=sp_sch.df.index, key_name='sa1_mo4',
    plot=plot_interpolate, coef=2e-18, rm_nan=True)
sp_sch.merge_data_from_tb(
    input_time_series=tb_pandas.result_df['sa1_raw5'].index,
    input_data_series=tb_pandas.result_df['sa1_raw5']['value'],
    output_time_series=sp_sch.df.index, key_name='sa1_mo5',
    plot=plot_interpolate, coef=2e-18, rm_nan=True)
sp_sch.merge_data_from_tb(
    input_time_series=tb_pandas.result_df['sa1_temp1'].index,
    input_data_series=tb_pandas.result_df['sa1_temp1']['value'],
    output_time_series=sp_sch.df.index, key_name='sa1_temp1',
    plot=plot_interpolate, coef=2e-11, rm_nan=True)
sp_sch.merge_data_from_tb(
    input_time_series=tb_pandas.result_df['sa1_temp2'].index,
    input_data_series=tb_pandas.result_df['sa1_temp2']['value'],
    output_time_series=sp_sch.df.index, key_name='sa1_temp2',
    plot=plot_interpolate, coef=2e-11, rm_nan=True)

sp_sch.merge_data_from_tb(
    input_time_series=tb_pandas.result_df['sa1_temp3'].index,
    input_data_series=tb_pandas.result_df['sa1_temp3']['value'],
    output_time_series=sp_sch.df.index, key_name='sa1_temp3',
    plot=plot_interpolate, coef=2e-11, rm_nan=True)
sp_sch.merge_data_from_tb(
    input_time_series=tb_pandas.result_df['sa1_temp4'].index,
    input_data_series=tb_pandas.result_df['sa1_temp4']['value'],
    output_time_series=sp_sch.df.index, key_name='sa1_temp4',
    plot=plot_interpolate, coef=2e-11, rm_nan=True)
sp_sch.merge_data_from_tb(
    input_time_series=tb_pandas.result_df['sa1_temp5'].index,
    input_data_series=tb_pandas.result_df['sa1_temp5']['value'],
    output_time_series=sp_sch.df.index, key_name='sa1_temp5',
    plot=plot_interpolate, coef=2e-11, rm_nan=True)
sp_sch.merge_data_from_tb(
    input_time_series=tb_pandas.result_df['sa1_ec1'].index,
    input_data_series=tb_pandas.result_df['sa1_ec1']['value'],
    output_time_series=sp_sch.df.index, key_name='sa1_ec1',
    plot=plot_interpolate, coef=2e-11, rm_nan=True)
sp_sch.merge_data_from_tb(
    input_time_series=tb_pandas.result_df['sa1_ec2'].index,
    input_data_series=tb_pandas.result_df['sa1_ec2']['value'],
    output_time_series=sp_sch.df.index, key_name='sa1_ec2',
    plot=plot_interpolate, coef=2e-11, rm_nan=True)

sp_sch.merge_data_from_tb(
    input_time_series=tb_pandas.result_df['sa1_ec3'].index,
    input_data_series=tb_pandas.result_df['sa1_ec3']['value'],
    output_time_series=sp_sch.df.index, key_name='sa1_ec3',
    plot=plot_interpolate, coef=2e-11, rm_nan=True)
sp_sch.merge_data_from_tb(
    input_time_series=tb_pandas.result_df['sa1_ec4'].index,
    input_data_series=tb_pandas.result_df['sa1_ec4']['value'],
    output_time_series=sp_sch.df.index, key_name='sa1_ec4',
    plot=plot_interpolate, coef=2e-11, rm_nan=True)
sp_sch.merge_data_from_tb(
    input_time_series=tb_pandas.result_df['sa1_ec5'].index,
    input_data_series=tb_pandas.result_df['sa1_ec5']['value'],
    output_time_series=sp_sch.df.index, key_name='sa1_ec5',
    plot=plot_interpolate, coef=2e-18, rm_nan=True)

sp_sch.merge_data_from_tb(
    input_time_series=tb_pandas.result_df['sa3_mo1'].index,
    input_data_series=tb_pandas.result_df['sa3_mo1']['value'],
    output_time_series=sp_sch.df.index, key_name='sa3_mo1',
    plot=plot_interpolate, coef=2e-18, rm_nan=True)
sp_sch.merge_data_from_tb(
    input_time_series=tb_pandas.result_df['sa3_mo2'].index,
    input_data_series=tb_pandas.result_df['sa3_mo2']['value'],
    output_time_series=sp_sch.df.index, key_name='sa3_mo2',
    plot=plot_interpolate, coef=2e-15, rm_nan=True)

sp_sch.merge_data_from_tb(
    input_time_series=tb_pandas.result_df['sa3_mo3'].index,
    input_data_series=tb_pandas.result_df['sa3_mo3']['value'],
    output_time_series=sp_sch.df.index, key_name='sa3_mo3',
    plot=plot_interpolate, coef=2e-15, rm_nan=True)
sp_sch.merge_data_from_tb(
    input_time_series=tb_pandas.result_df['sa3_mo4'].index,
    input_data_series=tb_pandas.result_df['sa3_mo4']['value'],
    output_time_series=sp_sch.df.index, key_name='sa3_mo4',
    plot=plot_interpolate, coef=2e-15, rm_nan=True)
sp_sch.merge_data_from_tb(
    input_time_series=tb_pandas.result_df['sa3_mo5'].index,
    input_data_series=tb_pandas.result_df['sa3_mo5']['value'],
    output_time_series=sp_sch.df.index, key_name='sa3_mo5',
    plot=plot_interpolate, coef=2e-15, rm_nan=True)

sp_sch.df=sp_sch.df.ffill()