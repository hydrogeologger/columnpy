#import sys
#sys.modules[__name__].__dict__.clear()
import os
import numpy as np
#http://stackoverflow.com/questions/5607283/how-can-i-manually-generate-a-pyc-file-from-a-py-file
import py_compile
import sys
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

import pandas as pd
import pdb
#https://stackoverflow.com/questions/842059/is-there-a-portable-way-to-get-the-current-username-in-python
import getpass



scale=1
del scale
#os.path.dirname(os.path.realpath(__file__))

current_path=os.getcwd()
sys.path.append   (os.environ['pyduino']+'/python/post_processing/')
py_compile.compile(os.environ['pyduino']+'/python/post_processing/pandas_scale.py')
py_compile.compile(os.environ['pyduino']+'/python/post_processing/constants.py')

import pandas_scale
import constants
reload(pandas_scale)
reload(constants)


python_file_path=current_path+'/python/'
sys.path.append(python_file_path)
# change the date time header as datetime to make life easier
#data_list_data_roof=os.listdir(current_path+'/data/data_roof/')
#---------below line works for 20180505 ---------------------
#data_file_path=current_path+'/data/stanwell_moisture_suction/'    # warning, all the files should be .dat DO NOT FORGET THE LAST SLASH

#---------below line works for 20181005 ---------------------
data_file_path=current_path+'/data/public_stanwell_moiosture_suction/data_from_phant/'   

# things to do
#1. change csv to dat
#2. add header, 
#3. arrange header formate, 
#4. change date_time as time axis

#93 fields
data_header=['mo0','mo1','mo2','mo3','mo4','mo5','mo6','mo7','mo8','mo9','su0','su1','su2','su3','su4','su5','su6','su7','su8','su9','date_time','tmp0','tmp1','tmp2','tmp3','tmp4','tmp5','tmp6','tmp7','tmp8','tmp9']


data_date_time=['date_time']
# 01/02/2018 please make sure date_time is the name for making date times
# 09/03/2017 here x[:-5] only sorts out from start to -5 position
# one can check the correct by
# dateparse('2017-03-09T09:02:48.588Z')
# and see if the parsing is successful
#dateparse =  lambda x: pd.datetime.strptime(x[:-5], '%Y-%m-%dT%H:%M:%S')  # sparkfun output
# this new function is better as it provides miniseconds parsing as well. 
#dateparse =  lambda x: pd.datetime.strptime(x[:-1], '%Y-%m-%dT%H:%M:%S')  #example:2020-02-01T00:00:00
dateparse =  lambda x: pd.datetime.strptime(x[:-1], '%Y-%m-%dT%H:%M:%S.%f')  # sparkfun output
#dateparse =  lambda x: pd.datetime.strptime(x[:-1], '%d/%b/%Y %H:%M:%S')  # 18/Jun/2017 23:29:03

# 09/03/2017 remove the index column at the very beginning, by default, pandas will produce a column from first one.
#index_col_sw=False
index_col_sw='date_time'


data_mo_su=pandas_scale.pandas_scale(file_path=data_file_path,
    source='raw',
    sep=',',
    header=2,
    names=data_header,
    parse_dates=data_date_time,
    date_parser=dateparse,
    index_col=index_col_sw
    )
####below is to set the index as datetime
data_mo_su.df.sort_index(ascending=True,inplace=True)
data_mo_su.df.index=data_mo_su.df.index+pd.to_timedelta(10, unit='h')
data_mo_su.df['date_time']= data_mo_su.df.index


#######below is to set the index as ordinal 
#data_mo_su.df.sort_values('date_time',inplace=True)
#data_mo_su.df = data_mo_su.df.reset_index(drop=True)
#data_mo_su.df['date_time']=data_mo_su.df['date_time']+pd.to_timedelta(10, unit='h')
#################
## https://stackoverflow.com/questions/37787698/how-to-sort-pandas-dataframe-from-one-column
## reverse the dataframe by timestamp as the result is upside down
#data.df.sort_values('timestamp',inplace=True)
#
#
## 'date_time'  is the column with corrected time zones




data_mo_su.df['tmp0'].loc[data_mo_su.df['tmp0']<1]=np.nan;
data_mo_su.df['tmp1'].loc[data_mo_su.df['tmp1']<1]=np.nan;
data_mo_su.df['tmp2'].loc[data_mo_su.df['tmp2']<1]=np.nan;
data_mo_su.df['tmp3'].loc[data_mo_su.df['tmp3']<1]=np.nan;
data_mo_su.df['tmp4'].loc[data_mo_su.df['tmp4']<1]=np.nan;
data_mo_su.df['tmp5'].loc[data_mo_su.df['tmp5']<1]=np.nan;
data_mo_su.df['tmp6'].loc[data_mo_su.df['tmp6']<1]=np.nan;
data_mo_su.df['tmp7'].loc[data_mo_su.df['tmp7']<1]=np.nan;
data_mo_su.df['tmp8'].loc[data_mo_su.df['tmp8']<1]=np.nan;
data_mo_su.df['tmp9'].loc[data_mo_su.df['tmp9']<1]=np.nan;


#time_tb_start = np.datetime64('2020-06-30T12:00')
#
#data_mo_su.df['tmp0'].loc[time_tb_start:]=np.nan;
#data_mo_su.df['tmp1'].loc[time_tb_start:]=np.nan;
#data_mo_su.df['tmp2'].loc[time_tb_start:]=np.nan;
#data_mo_su.df['tmp3'].loc[time_tb_start:]=np.nan;
#data_mo_su.df['tmp4'].loc[time_tb_start:]=np.nan;
#data_mo_su.df['tmp5'].loc[time_tb_start:]=np.nan;
#data_mo_su.df['tmp6'].loc[time_tb_start:]=np.nan;
#data_mo_su.df['tmp7'].loc[time_tb_start:]=np.nan;
#data_mo_su.df['tmp8'].loc[time_tb_start:]=np.nan;
#data_mo_su.df['tmp9'].loc[time_tb_start:]=np.nan;
#
#
#data_mo_su.df['mo0'].loc[time_tb_start:]=np.nan;
#data_mo_su.df['mo1'].loc[time_tb_start:]=np.nan;
#data_mo_su.df['mo2'].loc[time_tb_start:]=np.nan;
#data_mo_su.df['mo3'].loc[time_tb_start:]=np.nan;
#data_mo_su.df['mo4'].loc[time_tb_start:]=np.nan;
#data_mo_su.df['mo5'].loc[time_tb_start:]=np.nan;
#data_mo_su.df['mo6'].loc[time_tb_start:]=np.nan;
#data_mo_su.df['mo7'].loc[time_tb_start:]=np.nan;
#data_mo_su.df['mo8'].loc[time_tb_start:]=np.nan;
#data_mo_su.df['mo9'].loc[time_tb_start:]=np.nan;


#------------fill missing data-------------------
#time_start=np.datetime64('2018-08-30 02:10')
#time_end=np.datetime64('2018-09-14 13:00')
#period=data_mo_su.df['date_time'].between(time_start,time_end)
#data_mo_su.df['tmp0'][period]=np.random.randint()



####   special treatment
#time_start=np.datetime64('2018-02-22T00:00')
#time_end=np.datetime64('2018-03-06T04:00')
##https://stackoverflow.com/questions/31617845/how-to-select-rows-in-a-dataframe-between-two-values-in-python-pandas/31617974
#mask=data_mo_su.df['date_time'].between(time_start,time_end)
#data_mo_su.df.loc[mask,'mo0']=281+np.random.rand(np.sum(mask))*10
#
##time_start=np.datetime64('2018-01-29T00:00')
##time_end=np.datetime64('2018-02-03T04:00')
###https://stackoverflow.com/questions/31617845/how-to-select-rows-in-a-dataframe-between-two-values-in-python-pandas/31617974
##mask=data_mo_su.df['date_time'].between(time_start,time_end)
##mask=data_mo_su.df['date_time'].between(time_start,time_end)
##data_mo_su.df.loc[mask,'mo1']=500+np.random.rand(np.sum(mask))*20
#
##data_mo_su.df.loc[mask,'mo1']=443+np.random.rand(np.sum(mask))*20
#time_start=np.datetime64('2018-02-22T00:00')
#time_end=np.datetime64('2018-03-03T04:00')
##https://stackoverflow.com/questions/31617845/how-to-select-rows-in-a-dataframe-between-two-values-in-python-pandas/31617974
#mask=data_mo_su.df['date_time'].between(time_start,time_end)
#mask=data_mo_su.df['date_time'].between(time_start,time_end)
#data_mo_su.df.loc[mask,'mo1']=443+np.random.rand(np.sum(mask))*20
#
#
#time_start=np.datetime64('2018-02-22T00:00')
#time_end=np.datetime64('2018-03-02T04:00')
##https://stackoverflow.com/questions/31617845/how-to-select-rows-in-a-dataframe-between-two-values-in-python-pandas/31617974
#mask=data_mo_su.df['date_time'].between(time_start,time_end)
#mask=data_mo_su.df['date_time'].between(time_start,time_end)
#data_mo_su.df.loc[mask,'mo2']=495+np.random.rand(np.sum(mask))*20
#
#time_start=np.datetime64('2018-02-23T00:00')
#time_end=np.datetime64('2018-03-01T04:00')
##https://stackoverflow.com/questions/31617845/how-to-select-rows-in-a-dataframe-between-two-values-in-python-pandas/31617974
#mask=data_mo_su.df['date_time'].between(time_start,time_end)
#data_mo_su.df.loc[mask,'mo4']=500+np.random.rand(np.sum(mask))*20
#
#
#
#time_start=np.datetime64('2018-02-24T00:00')
#time_end=np.datetime64('2018-03-01T04:00')
##https://stackoverflow.com/questions/31617845/how-to-select-rows-in-a-dataframe-between-two-values-in-python-pandas/31617974
#mask=data_mo_su.df['date_time'].between(time_start,time_end)
#data_mo_su.df.loc[mask,'mo5']=324+np.random.rand(np.sum(mask))*20
#
#
#time_start=np.datetime64('2018-03-27T00:00')
#time_end=np.datetime64('2018-03-29T04:00')
##https://stackoverflow.com/questions/31617845/how-to-select-rows-in-a-dataframe-between-two-values-in-python-pandas/31617974
#mask=data_mo_su.df['date_time'].between(time_start,time_end)
#data_mo_su.df.loc[mask,'mo0']=280+np.random.rand(np.sum(mask))*20
#data_mo_su.df.loc[mask,'mo1']=280+np.random.rand(np.sum(mask))*20
#data_mo_su.df.loc[mask,'mo2']=np.nan
#data_mo_su.df.loc[mask,'mo3']=np.nan
#data_mo_su.df.loc[mask,'mo4']=np.nan
#data_mo_su.df.loc[mask,'mo5']=np.nan
#
#time_start=np.datetime64('2018-01-28T00:00')
#time_end=np.datetime64('2018-02-03T04:00')
##https://stackoverflow.com/questions/31617845/how-to-select-rows-in-a-dataframe-between-two-values-in-python-pandas/31617974
#mask=data_mo_su.df['date_time'].between(time_start,time_end)
#data_mo_su.df.loc[mask,'pre']=280+np.random.rand(np.sum(mask))*20
##data_mo_su.df.loc[mask,'mo1']=280+np.random.rand(np.sum(mask))*20
#
