import os
import sys
import py_compile

current_path=os.getcwd()
pyduino_path = '/home/osboxes/pyduino_py3'
sys.path.append(os.path.join(pyduino_path,'python','post_processing'))

import operator
import json
import pandas as pd
import numpy as np
import pdb
import getpass
import thingsboard_to_pandas
import pandas_scale
import constants

current_path = os.getcwd()+'/Redmud_infiltration_test/'
tb_pandas=thingsboard_to_pandas.tingsboard_to_pandas(current_path+'tb_credential.json')   # input is the location of the json file
tb_pandas.get_token()    # get the token associated with the account
tb_pandas.get_keys()     # list of keys in the device
tb_pandas.get_data()     # obtain data from thingsboard stored at tb_pandas['results']
tb_pandas.convert_data_to_df()  # convert each datasets to pandas dataframe

name_list = ['scale1','scale2']

for i in name_list:
        tb_pandas.result_df[i]['value'][tb_pandas.result_df[i]['value']<1]=np.nan

with open(current_path+'schedule.json') as data_file:    
    sp_input = json.load(data_file)

sp_sch={}
plot_interpolate = False

sp_sch=pandas_scale.concat_data_tb(pd.to_datetime(sp_input['start_time'],format='%Y/%b/%d %H:%M'),
    pd.to_datetime(sp_input['end_time'],format='%Y/%b/%d %H:%M'),sp_input['delta_t_s'] )

sp_sch.start_dt = pd.to_datetime(sp_input['start_time'],format='%Y/%b/%d %H:%M')
sp_sch.end_dt   = pd.to_datetime(sp_input['end_time'  ],format='%Y/%b/%d %H:%M')

for i in name_list:
        sp_sch.merge_data_from_tb(
                input_time_series=tb_pandas.result_df[i].index,
                input_data_series=tb_pandas.result_df[i]['value'],
                output_time_series=sp_sch.df.index,
                key_name=i,
                rm_nan=True
        )

data_file_path = current_path+'/data/'




sp_sch.df.to_csv(data_file_path+'/result.csv')



