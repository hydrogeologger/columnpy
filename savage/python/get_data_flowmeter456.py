# -*- coding: utf-8 -*-
import py_compile
import os
import sys
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas_scale
    
pyduino_path = os.environ['pyduino']
print(os.environ['pyduino'])
sys.path.append(os.path.join(pyduino_path,'python','post_processing'))
py_compile.compile(os.path.join(pyduino_path,'python','post_processing','thingsboard_to_pandas.py'))
import thingsboard_to_pandas



tb_pandas=thingsboard_to_pandas.tingsboard_to_pandas('tb_credential.json')   # input is the location of the json file
# use the below command to show the comments on tb_credential.json
# print tb_pandas.input_json['comments'] 



tb_pandas.get_token()    # get the token associated with the account (expire in 15 mins)
tb_pandas.get_keys()     # list of keys in the device
tb_pandas.get_data()     # obtain data from thingsboard stored at tb_pandas['results']
#print tb_pandas.result_json to see all the data
#list(tb_pandas.result_json) to see all the keys
#tb_pandas.result_json['scale1']      to show the data of of a specific key/column
tb_pandas.convert_data_to_df()  # convert each datasets to pandas dataframe
tb_pandas.result_df['rain_gauge4']['cumsum']=np.cumsum(tb_pandas.result_df['rain_gauge4']['value'])
tb_pandas.result_df['rain_gauge5']['cumsum']=np.cumsum(tb_pandas.result_df['rain_gauge5']['value'])
tb_pandas.result_df['rain_gauge6']['cumsum']=np.cumsum(tb_pandas.result_df['rain_gauge6']['value'])

#df1=pd.DataFrame.from_dict(tb_pandas.result_df['rain_gauge1'])
#df2=pd.DataFrame.from_dict(tb_pandas.result_df['rain_gauge2'])
#df3=pd.DataFrame.from_dict(tb_pandas.result_df['rain_gauge3'])

#merged1=df1.merge(df2, left_on='ts', right_on='ts')
#merged2=merged1.merge(df3, left_on='ts', right_on='ts')


with open('schedule.json') as data_file:    
    sp_input = json.load(data_file)


sp_sch=pandas_scale.concat_data_tb(pd.datetime.strptime(sp_input['start_time'],'%Y/%b/%d %H:%M'),
    pd.datetime.strptime(sp_input['end_time'],'%Y/%b/%d %H:%M'),sp_input['delta_t_s'] );
                                   
plot_interpolate=False
#plot_interpolate=True                                   
sp_sch.merge_data_from_tb(input_time_series=tb_pandas.result_df['rain_gauge4'].index, 
        input_data_series=tb_pandas.result_df['rain_gauge4']['cumsum'], 
        output_time_series=sp_sch.df.index,
        key_name='rain_gauge4_cumsum' ,
        plot=plot_interpolate  ,
        coef=5e-5,
        rm_nan=True)

sp_sch.merge_data_from_tb(input_time_series=tb_pandas.result_df['rain_gauge5'].index, 
        input_data_series=tb_pandas.result_df['rain_gauge5']['cumsum'], 
        output_time_series=sp_sch.df.index,
        key_name='rain_gauge5_cumsum' ,
        plot=plot_interpolate  ,
        coef=5e-5,
        rm_nan=True)

sp_sch.merge_data_from_tb(input_time_series=tb_pandas.result_df['rain_gauge6'].index, 
        input_data_series=tb_pandas.result_df['rain_gauge6']['cumsum'], 
        output_time_series=sp_sch.df.index,
        key_name='rain_gauge6_cumsum' ,
        plot=plot_interpolate  ,
        coef=5e-5,
        rm_nan=True)


volume_per_tip = 1.38E-3 #litre

sp_sch.df['rain_gauge4_rate']=(sp_sch.df['rain_gauge4_cumsum'] -sp_sch.df['rain_gauge4_cumsum'].shift(1))*volume_per_tip
sp_sch.df['rain_gauge5_rate']=(sp_sch.df['rain_gauge5_cumsum'] -sp_sch.df['rain_gauge5_cumsum'].shift(1))*volume_per_tip 
sp_sch.df['rain_gauge6_rate']=(sp_sch.df['rain_gauge6_cumsum'] -sp_sch.df['rain_gauge6_cumsum'].shift(1))*volume_per_tip 

sp_sch.df['rain_gauge4_cumsum'] = sp_sch.df['rain_gauge4_cumsum']*volume_per_tip
sp_sch.df['rain_gauge5_cumsum'] = sp_sch.df['rain_gauge5_cumsum']*volume_per_tip
sp_sch.df['rain_gauge6_cumsum'] = sp_sch.df['rain_gauge6_cumsum']*volume_per_tip

#fig = plt.figure(figsize=(16,10))
#ax = [[] for i in range(30)]
#ax[0] = plt.subplot2grid((3, 1), (0, 0), colspan=1)
#ax[1] = plt.subplot2grid((3, 1), (1, 0), colspan=1, sharex = ax[0])
#ax[2] = plt.subplot2grid((3, 1), (2, 0), colspan=1, sharex = ax[0])
#
#ax[0].plot(tb_pandas.result_df['rain_gauge1'].index,tb_pandas.result_df['rain_gauge1']['value'])
##ax[0].plot(tb_pandas.result_df['rain_gauge1'].index,tb_pandas.result_df['rain_gauge1']['value'])
#ax[0].plot(sp_sch.df.index,sp_sch.df['rain_gauge1_rate'])
#
#ax[1].plot(tb_pandas.result_df['rain_gauge2'].index,tb_pandas.result_df['rain_gauge2']['value'])
#ax[1].plot(sp_sch.df.index,sp_sch.df['rain_gauge2_rate'])
#
#ax[2].plot(tb_pandas.result_df['rain_gauge3'].index,tb_pandas.result_df['rain_gauge3']['value'])
#ax[2].plot(sp_sch.df.index,sp_sch.df['rain_gauge3_rate'])

sp_sch.df.to_csv('flowmeter456.csv')

