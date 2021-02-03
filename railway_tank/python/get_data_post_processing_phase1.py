import os
import sys
import py_compile
current_path=os.getcwd()+'/railway_tank'
pyduino_path = '/home/osboxes/pyduino'
sys.path.append(os.path.join(pyduino_path,'python','post_processing'))
py_compile.compile(os.path.join(pyduino_path,'python','post_processing','thingsboard_to_pandas.py'))
py_compile.compile(os.path.join(pyduino_path,'python','post_processing','pandas_scale.py')  )
py_compile.compile(os.path.join(pyduino_path,'python','post_processing','constants.py')  )
#py_compile.compile(os.environ['pyduino']+'/python/post_processing/sensorfun.py')
#py_compile.compile(os.environ['pyduino']+'/python/post_processing/figlib.py')
'''

2020/Mar/30 15:00,   2020/Jul/15 13:00 

'''
project_name = 'RAILWAY_TANK_PHASE1'

import operator
import json
import pandas as pd
import numpy as np
import pdb
import getpass
import matplotlib
#matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import thingsboard_to_pandas
import pandas_scale
import constants
#import sensorfun
#import figlib


if not os.path.exists('figure'):
        os.makedirs('figure')
if not os.path.exists('output_data'):
        os.makedirs('output_data')


tb_pandas=thingsboard_to_pandas.tingsboard_to_pandas(current_path+'/tb_credential.json')   # input is the location of the json file

tb_pandas.get_token()    # get the token associated with the account
tb_pandas.get_keys()     # list of keys in the device
tb_pandas.get_data()     # obtain data from thingsboard stored at tb_pandas['results']
tb_pandas.convert_data_to_df()  # convert each datasets to pandas dataframe

raw_suction_list = ['su_a0','su_a2','su_a4','su_b0','su_b2','su_b4',
                    'su_d0','su_d2','su_d4','su_e0','su_e2','su_e4',
                    'su_f0','su_f2','su_f4','su_f1','su_f3','su_g0','su_g2','su_g4',
                    'su_h0','su_h2','su_h4']

raw_moisture_list = ['mo1','mo2','mo3','mo4','mo5','mo6','mo7']

raw_temperature_list = ['temp_a','temp_b','temp_c','temp_d','temp_e','temp_f','temp_g','temp_h']

moisture_list = ['moisture1','moisture2','moisture3','moisture4','moisture5','moisture6','moisture7']

vwc_list = ['vwc1','vwc2','vwc3','vwc4','vwc6','vwc7']

vwc_suction_list = ['suctiona0_vwc','suctionb0_vwc','suctiond0_vwc','suctione0_vwc','suctiong0_vwc','suctionh0_vwc']

suction_list = []

for i in raw_suction_list:
  suction_list.append('suction{}'.format(i[-2:]))

name_list = raw_moisture_list + raw_suction_list + raw_temperature_list 


# make the value to be nan where <1
for i in name_list:
  if i == 'mo6':
    tb_pandas.result_df[i]['value'][tb_pandas.result_df[i]['value']>665]=np.nan
  else:
    tb_pandas.result_df[i]['value'][tb_pandas.result_df[i]['value']<1]=np.nan
  
        

# processing the suctiond data
#for i in raw_suction_list:
#  if 'b' in i:
#        tb_pandas.result_df[i]['value'].loc[tb_pandas.result_df[i]['value']>15]=np.nan
#
#  elif 'd' in i:
#        tb_pandas.result_df[i]['value'].loc[tb_pandas.result_df[i]['value']>15]=np.nan
#    
#  elif 'e' in i:
#        tb_pandas.result_df[i]['value'].loc[tb_pandas.result_df[i]['value']>15]=np.nan
#
#  elif 'f' in i:
#        tb_pandas.result_df[i]['value'].loc[tb_pandas.result_df[i]['value']>15]=np.nan
#    
#  elif 'g' in i:
#        tb_pandas.result_df[i]['value'].loc[tb_pandas.result_df[i]['value']>15]=np.nan
#   
#  elif 'h' in i:
#        tb_pandas.result_df[i]['value'].loc[tb_pandas.result_df[i]['value']>15]=np.nan

# merge data    
with open(current_path+'/schedule.json') as data_file:    
    sp_input = json.load(data_file)[project_name][0]


sp_sch={}
#plot_interpolate=True
plot_interpolate=False

sp_sch=pandas_scale.concat_data_tb(pd.to_datetime(sp_input['start_time'],format='%Y/%b/%d %H:%M'),
    pd.to_datetime(sp_input['end_time'],format='%Y/%b/%d %H:%M'),sp_input['delta_t_s'] )

sp_sch.start_dt = pd.to_datetime(sp_input['start_time'],format='%Y/%b/%d %H:%M')
sp_sch.end_dt   = pd.to_datetime(sp_input['end_time'  ],format='%Y/%b/%d %H:%M')

# merge data from tb
for i in name_list:
        sp_sch.merge_data_from_tb(
                input_time_series=tb_pandas.result_df[i].index,
                input_data_series=tb_pandas.result_df[i]['value'],
                output_time_series=sp_sch.df.index,
                key_name=i,
                rm_nan=True
        )

     
# plot the fig
'''
fig = plt.figure(figsize=(16,10))
ax = [[] for i in range(30)]
ax[0] = plt.subplot2grid((2, 1), (0, 0), colspan=1)
ax[1] = plt.subplot2grid((2, 1), (1, 0), colspan=1, sharex = ax[0])

ax[0].plot(sp_sch.df.index,sp_sch.df['temp_a'])
ax[0].plot(sp_sch.df.index,sp_sch.df['temp_b'])
ax[0].plot(sp_sch.df.index,sp_sch.df['temp_c'])
ax[0].plot(sp_sch.df.index,sp_sch.df['temp_d'])
ax[0].plot(sp_sch.df.index,sp_sch.df['temp_e'])
ax[0].plot(sp_sch.df.index,sp_sch.df['temp_f'])
ax[0].plot(sp_sch.df.index,sp_sch.df['temp_g'])
ax[0].plot(sp_sch.df.index,sp_sch.df['temp_h'])

ax[1].plot(sp_sch.df.index,sp_sch.df['mo1'])
ax[1].plot(sp_sch.df.index,sp_sch.df['mo2'])
ax[1].plot(sp_sch.df.index,sp_sch.df['mo3'])
ax[1].plot(sp_sch.df.index,sp_sch.df['mo4'])
ax[1].plot(sp_sch.df.index,sp_sch.df['mo5'])
ax[1].plot(sp_sch.df.index,sp_sch.df['mo6'])
ax[1].plot(sp_sch.df.index,sp_sch.df['mo7'])

#ax[1].plot(sp_sch.df.index,sp_sch.df['scale1'][0]-sp_sch.df['scale1'])
#ax[1].plot(sp_sch.df.index,sp_sch.df['scale2'][0]-sp_sch.df['scale2'])
'''
#plt.show()

sp_sch.df.to_csv(current_path+'/data/result.dat')
#pd.DataFrame(sp_sch.df, columns=name_list).to_csv('/content/drive/MyDrive/summer/data/railway_tank_nov/result_raw.csv')
#pd.DataFrame(sp_sch.df, columns=name_list).to_csv('data/railway_tank_nov/result_raw.dat')
#plt.close()

#===================================================================================
#============================INITIATE===============================================
#===================================================================================

#import sys
#sys.modules[__name__].__dict__.clear()

python_file_path=current_path+'/python/'
sys.path.append(python_file_path)
# change the date time header as datetime to make life easier
#data_list_data_roof=os.listdir(current_path+'/data/data_roof/')
data_file_path=current_path+'/data/'    # warning, all the files should be .dat DO NOT FORGET THE LAST SLASH




# data_header needs to be the same as the sp_sch.df columns
data_header=['date_time','time_days'] + raw_moisture_list + raw_suction_list + raw_temperature_list

data_date_time=['date_time']

# 01/02/2018 please make sure date_time is the name for making date times
# 09/03/2017 here x[:-5] only sorts out from start to -5 position
# one can check the correct by
# dateparse('2017-03-09T09:02:48.588Z')
# and see if the parsing is successful
#dateparse =  lambda x: pd.to_datetime(x[:-5],format= '%Y-%m-%dT%H:%M:%S')  # sparkfun output
# this new function is better as it provides miniseconds parsing as well. 

#dateparse =  lambda x: pd.to_datetime(x[:-1], format='%Y-%m-%dT%H:%M:%S.%f')  # sparkfun output
dateparse =  lambda x: pd.to_datetime(x[:], format='%Y-%m-%d %H:%M:%S.%f')  # sparkfun output
#dateparse =  lambda x: pd.to_datetime(x[:-5], format='%Y-%m-%dT%H:%M.%f')  # 18/Jun/2017 23:29:03

# 09/03/2017 remove the index column at the very beginning, by default, pandas will produce a column from first one.
index_col_sw=False

data=pandas_scale.pandas_scale(file_path=data_file_path,
    source='raw',
    sep=',',
    header=1,
    names=data_header,
    parse_dates=data_date_time,
    date_parser=dateparse,
    index_col=index_col_sw
    )


#data_mo_su.df.sort_index(ascending=True,inplace=True)
data.df.sort_values('date_time',inplace=True)
## https://stackoverflow.com/questions/37787698/how-to-sort-pandas-dataframe-from-one-column
## reverse the dataframe by timestamp as the result is upside down
#data.df.sort_values('timestamp',inplace=True)
#
data.df = data.df.set_index('date_time',drop=False)
#data.df = data.df.reset_index(drop=True)
#
## 'date_time'  is the column with corrected time zones
#data.df['date_time']=data.df['date_time']+pd.to_timedelta(10, unit='h')
#data_mo_su.df.index=data_mo_su.df.index+pd.to_timedelta(10, unit='h')

# make inf data to be nan
data.df.replace([np.inf, -np.inf], np.nan, inplace=True)

#------select time period for moisture sensor--------

time_start_sud0=np.datetime64('2020-04-22 23:00')
time_end_sud0=np.datetime64('2020-04-28 21:30')
mask_sud0=data.df['date_time'].between(time_start_sud0,time_end_sud0)
data.df['su_d0'].loc[mask_sud0]=np.nan

#===================================================================================
#============================READSCHEDULE===========================================
#===================================================================================


dt_s=3600
sp_sch = {}

sch_name=project_name
sp_sch[sch_name]=pandas_scale.concat_data_roof(pd.datetime.strptime(sp_input['start_time'],'%Y/%b/%d %H:%M'),pd.datetime.strptime(sp_input['end_time'],'%Y/%b/%d %H:%M'),dt_s );
sp_sch[sch_name].df.index=sp_sch[sch_name].df['date_time']
sp_sch[sch_name].start_dt=pd.datetime.strptime(sp_input['start_time'],'%Y/%b/%d %H:%M')
sp_sch[sch_name].end_dt=pd.datetime.strptime(sp_input['end_time'],'%Y/%b/%d %H:%M')

#sp_sch[sch_name].surface_area=float(line_content[4])
#sp_sch[sch_name].por=float(line_content[6])
#sp_sch[sch_name].time_surface_emerge = pd.datetime.strptime(line_content[10],'%Y/%b/%d %H:%M')
#time_start = np.datetime64('2018-03-02T08:00')
#time_end   = np.datetime64('2018-05-29T00:00')
##https://stackoverflow.com/questions/31617845/how-to-select-rows-in-a-dataframe-between-two-values-in-python-pandas/31617974
#mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
#sp_sch[sch_name].df['tmp2'][mask]=np.random.random(len(mask))*50+710
coef_suction_list = [5e-15]*len(raw_suction_list)
coef_suction_dict = dict(zip(raw_suction_list, coef_suction_list))
coef_suction_dict['su_a0']=1e-16
coef_suction_dict['su_d0']=1e-16
for i in coef_suction_dict:
        sp_sch[sch_name].merge_data(
                df=data.df,
                keys=[i],
                plot=plot_interpolate,
                coef=coef_suction_dict[i]
        )        
average_elements_list = [-20]*len(raw_suction_list)
average_elements_dict = dict(zip(raw_suction_list, average_elements_list))
aa_dict = dict(zip(raw_suction_list, [-1.1]*len(raw_suction_list))) # Degree of volatility
bb_dict = dict(zip(raw_suction_list, [7]*len(raw_suction_list)))   # scale the values
# if you want to change the coeff, use the example below
change_list = ['su_d0','su_e0','su_f0','su_g0','su_f0','su_h0']
for i in change_list:
        average_elements_dict[i]=-30
# version that only save the final value into the dataframe
for i in average_elements_dict:
        sorted = sp_sch[sch_name].df[i].sort_values()
        max_delta_t = np.average(sorted[average_elements_dict[i]:])
        min_delta_t = np.average(sorted[0])
        norm_delta_t = -(min_delta_t-sp_sch[sch_name].df[i])/(max_delta_t-min_delta_t)
        sp_sch[sch_name].df['suction{}'.format(i[-2:])] = np.exp(-1.5*(norm_delta_t**aa_dict[i]-bb_dict[i]))

alpha_mo = -5.0
porosity = 0.3
# merge coef (smooth the curve) for temperature
coef_temperature_list = [5e-15]*len(raw_temperature_list)
coef_temperature_dict = dict(zip(raw_temperature_list, coef_temperature_list))
coef_raw_moisture_list = [5e-15]*len(raw_moisture_list)
coef_raw_moisture_dict = dict(zip(raw_moisture_list, coef_raw_moisture_list))
# if you want change any of the coef, just change the value of the dict.
# coef_#_dict['xxx']=1e-1x
 
# merge data using the coef dict
for i in coef_temperature_dict:
        sp_sch[sch_name].merge_data(
                df=data.df,
                keys=[i],
                plot=plot_interpolate,
                coef=coef_temperature_dict[i]
        )
for i in coef_raw_moisture_dict:
        sp_sch[sch_name].merge_data(
                df=data.df,
                keys=[i],
                plot=plot_interpolate,
                coef=coef_raw_moisture_dict[i]
        )        

#degree of saturation
sp_sch[sch_name].df['moisture1']=(610.0**alpha_mo-sp_sch[sch_name].df['mo1']**alpha_mo)/(610.**alpha_mo-450**alpha_mo)
sp_sch[sch_name].df['moisture2']=(640.0**alpha_mo-sp_sch[sch_name].df['mo2']**alpha_mo)/(640.**alpha_mo-470**alpha_mo)
sp_sch[sch_name].df['moisture3']=(540.0**alpha_mo-sp_sch[sch_name].df['mo3']**alpha_mo)/(540.**alpha_mo-390**alpha_mo)
sp_sch[sch_name].df['moisture4']=(650.0**alpha_mo-sp_sch[sch_name].df['mo4']**alpha_mo)/(650.**alpha_mo-510**alpha_mo)
sp_sch[sch_name].df['moisture5']=(590.0**alpha_mo-sp_sch[sch_name].df['mo5']**alpha_mo)/(590.**alpha_mo-490**alpha_mo)
#sp_sch[sch_name].df['moisture6']=(680.0**alpha_mo-sp_sch[sch_name].df['mo6']**alpha_mo)/(680.**alpha_mo-440**alpha_mo)
sp_sch[sch_name].df['moisture6']=(665.0**alpha_mo-sp_sch[sch_name].df['mo6']**alpha_mo)/(665.**alpha_mo-440**alpha_mo)
sp_sch[sch_name].df['moisture7']=(600.0**alpha_mo-sp_sch[sch_name].df['mo7']**alpha_mo)/(600.**alpha_mo-475**alpha_mo)

#vwc
sp_sch[sch_name].df['vwc1']=sp_sch[sch_name].df['moisture1']*porosity
sp_sch[sch_name].df['vwc2']=sp_sch[sch_name].df['moisture2']*porosity
sp_sch[sch_name].df['vwc3']=sp_sch[sch_name].df['moisture3']*porosity
sp_sch[sch_name].df['vwc4']=sp_sch[sch_name].df['moisture4']*porosity
sp_sch[sch_name].df['vwc5']=sp_sch[sch_name].df['moisture5']*porosity
sp_sch[sch_name].df['vwc6']=sp_sch[sch_name].df['moisture6']*porosity
sp_sch[sch_name].df['vwc7']=sp_sch[sch_name].df['moisture7']*porosity

sp_sch[sch_name].df['suctione0_vwc']=constants.swcc_reverse_fredlund_xing_1994(nf=0.71,mf=2.74,af=475.98,hr=4154.68,vwc=sp_sch[sch_name].df['vwc4'])
sp_sch[sch_name].df['suctionf0_vwc']=constants.swcc_reverse_fredlund_xing_1994(nf=0.71,mf=2.74,af=475.98,hr=4154.68,vwc=sp_sch[sch_name].df['vwc5']) #convert Pa to kPa
sp_sch[sch_name].df['suctiong0_vwc']=constants.swcc_reverse_fredlund_xing_1994(nf=0.71,mf=2.74,af=475.98,hr=4154.68,vwc=sp_sch[sch_name].df['vwc6'])
sp_sch[sch_name].df['suctionh0_vwc']=constants.swcc_reverse_fredlund_xing_1994(nf=0.71,mf=2.74,af=475.98,hr=4154.68,vwc=sp_sch[sch_name].df['vwc7'])


