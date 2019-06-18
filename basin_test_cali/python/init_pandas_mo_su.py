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


dt_s=3600
scale=1
del scale
#os.path.dirname(os.path.realpath(__file__))

current_path=os.getcwd()
sys.path.append   (os.environ['pyduino']+'/python/post_processing/')
py_compile.compile(os.environ['pyduino']+'/python/post_processing/pandas_scale.py')
py_compile.compile(os.environ['pyduino']+'/python/post_processing/constants.py')


if not os.path.exists('figure'):
        os.makedirs('figure')
if not os.path.exists('output_data'):
        os.makedirs('output_data')


import pandas_scale
import constants
reload(pandas_scale)
reload(constants)


python_file_path=current_path+'/python/'
sys.path.append(python_file_path)
# change the date time header as datetime to make life easier
#data_list_data_roof=os.listdir(current_path+'/data/data_roof/')
data_file_path=current_path+'/data/public_basin_test_wenqiang_mo_su/'    # warning, all the files should be .dat DO NOT FORGET THE LAST SLASH


# things to do
#1. change csv to dat
#2. add header, 
#3. arrange header formate, 
#4. change date_time as time axis

#93 fields
data_header=['hum_dht22','moa1','moa2','moa3','mob1','mob2','mob3','moc1','moc2','moc3','scale1','scale2','scale3','sua1','sua2','sua3','sub1','sub2','sub3','suc1','suc2','suc3','temp_dht22','tempa1_a','tempa1_b','tempa2_a','tempa2_b','tempa3_a','tempa3_b','tempb1_a','tempb1_b','tempb2_a','tempb2_b','tempb3_a','tempb3_b','tempc1_a','tempc1_b','tempc2_a','tempc2_b','tempc3_a','tempc3_b','date_time','tmp1','tmp2','tmp3','tmp4','tmp5','tmp6','tmp7','tmp8']


data_date_time=['date_time']
# 01/02/2018 please make sure date_time is the name for making date times
# 09/03/2017 here x[:-5] only sorts out from start to -5 position
# one can check the correct by
# dateparse('2017-03-09T09:02:48.588Z')
# and see if the parsing is successful
#dateparse =  lambda x: pd.datetime.strptime(x[:-5], '%Y-%m-%dT%H:%M:%S')  # sparkfun output
# this new function is better as it provides miniseconds parsing as well. 
dateparse =  lambda x: pd.datetime.strptime(x[:-1], '%Y-%m-%dT%H:%M:%S.%f')  # sparkfun output
#dateparse =  lambda x: pd.datetime.strptime(x[:-1], '%d/%b/%Y %H:%M:%S')  # 18/Jun/2017 23:29:03

# 09/03/2017 remove the index column at the very beginning, by default, pandas will produce a column from first one.
#index_col_sw='date_time'
index_col_sw=False

data_mo_su=pandas_scale.pandas_scale(file_path=data_file_path,
    source='raw',
    sep=',',
    header=1,
    names=data_header,
    parse_dates=data_date_time,
    date_parser=dateparse,
    index_col=index_col_sw
    )


#data_mo_su.df.sort_index(ascending=True,inplace=True)
data_mo_su.df.sort_values('date_time',inplace=True)
## https://stackoverflow.com/questions/37787698/how-to-sort-pandas-dataframe-from-one-column
## reverse the dataframe by timestamp as the result is upside down
#data.df.sort_values('timestamp',inplace=True)
#
data_mo_su.df = data_mo_su.df.set_index('date_time',drop=False)
#data_mo_su.df = data_mo_su.df.reset_index(drop=True)
#
## 'date_time'  is the column with corrected time zones
data_mo_su.df['date_time']=data_mo_su.df['date_time']+pd.to_timedelta(10, unit='h')
#data_mo_su.df.index=data_mo_su.df.index+pd.to_timedelta(10, unit='h')

#select 'date time' column as index column


#data_mo_su.df['hum_dht22'].loc[data_mo_su.df['hum_dht22']<1]=np.nan;
data_mo_su.df['moa1'].loc[data_mo_su.df['moa1']<1]=np.nan;
#data_mo_su.df['moa2'].loc[data_mo_su.df['moa2']<1]=np.nan;
data_mo_su.df['moa3'].loc[data_mo_su.df['moa3']<1]=np.nan;
data_mo_su.df['mob1'].loc[data_mo_su.df['mob1']<1]=np.nan;
data_mo_su.df['mob2'].loc[data_mo_su.df['mob2']<1]=np.nan;
data_mo_su.df['mob3'].loc[data_mo_su.df['mob3']<1]=np.nan;
data_mo_su.df['moc1'].loc[data_mo_su.df['moc1']<1]=np.nan;
data_mo_su.df['moc2'].loc[data_mo_su.df['moc2']<1]=np.nan;
data_mo_su.df['moc3'].loc[data_mo_su.df['moc3']<1]=np.nan;
data_mo_su.df['scale1'].loc[data_mo_su.df['scale1']<1]=np.nan;
data_mo_su.df['scale2'].loc[data_mo_su.df['scale2']<1]=np.nan;
data_mo_su.df['scale3'].loc[data_mo_su.df['scale3']<1]=np.nan;
data_mo_su.df['sua1'].loc[data_mo_su.df['sua1']<1]=np.nan;
data_mo_su.df['sua2'].loc[data_mo_su.df['sua2']<1]=np.nan;
data_mo_su.df['sua3'].loc[data_mo_su.df['sua3']<1]=np.nan;
data_mo_su.df['sub1'].loc[data_mo_su.df['sub1']<1]=np.nan;
data_mo_su.df['sub2'].loc[data_mo_su.df['sub2']<1]=np.nan;
data_mo_su.df['sub3'].loc[data_mo_su.df['sub3']<1]=np.nan;
data_mo_su.df['suc1'].loc[data_mo_su.df['suc1']<1]=np.nan;
data_mo_su.df['suc2'].loc[data_mo_su.df['suc2']<1]=np.nan;
data_mo_su.df['suc3'].loc[data_mo_su.df['suc3']<1]=np.nan;
#data_mo_su.df['temp_dht22'].loc[data_mo_su.df['temp_dht22']<1]=np.nan;


####   special treatment
time_start=np.datetime64('2018-12-21 23:00')
time_end=np.datetime64('2019-01-06 21:30')
mask=data_mo_su.df['date_time'].between(time_start,time_end)
#time_start_scale=np.datetime64('2018-03-06T08:00')
#time_end_scale=np.datetime64('2018-03-06T12:30')
##https://stackoverflow.com/questions/31617845/how-to-select-rows-in-a-dataframe-between-two-values-in-python-pandas/
#mask_scale=data_mo_su.df['date_time'].between(time_start_scale,time_end_scale)
#data_mo_su.df.loc[mask_scale,'scale1']=np.nan;

#------select time period for moisture sensor--------
time_start_scale3=np.datetime64('2019-01-04 12:00')
data_mo_su.df['scale3'].loc[time_start_scale3:]=np.nan
#time_end_scale3=np.datetime64('2019-01-05 02:00')
#mask_scale3=data_mo_su.df['date_time'].between(time_start_scale3,time_end_scale3)
#data_mo_su.df.loc[mask_scale3,'scale3']=np.nan

time_start_scale1=np.datetime64('2018-12-21 23:00')
time_end_scale1=np.datetime64('2018-12-22 20:00')
data_mo_su.df['scale1'].loc[:time_end_scale1]=np.nan
time_end_scale2=np.datetime64('2018-12-22 22:00')
data_mo_su.df['scale2'].loc[:time_end_scale2]=np.nan

time_end_scale3=np.datetime64('2018-12-23 02:00')
data_mo_su.df['scale3'].loc[:time_end_scale3]=np.nan


time_start=np.datetime64('2018-12-21 23:00')
time_end=np.datetime64('2018-12-23 03:00')
#mask_moa1=data_mo_su.df['date_time'].between(time_start_moa1,time_end_moa1)
#data_mo_su.df.loc[mask_moa1,'moa1']=np.nan
time_end_moa1=np.datetime64('2018-12-24 18:00')
data_mo_su.df['moa1'].loc[:time_end_moa1]=np.nan
time_end_moa3=np.datetime64('2018-12-24 12:00')
data_mo_su.df['moa3'].loc[:time_end_moa3]=np.nan

time_end_mob1=np.datetime64('2018-12-26 14:30')
data_mo_su.df['mob1'].loc[:time_end_mob1]=np.nan
time_end_mob2=np.datetime64('2018-12-23 06:00')
data_mo_su.df['mob2'].loc[:time_end_mob2]=np.nan

data_mo_su.df['mob3'].loc[:time_end]=np.nan

time_end_moc1=np.datetime64('2018-12-24 23:00')
data_mo_su.df['moc1'].loc[:time_end_moc1]=np.nan

time_end_moc2=np.datetime64('2018-12-24 07:00')
data_mo_su.df['moc2'].loc[:time_end_moc2]=np.nan
time_end_moc3=np.datetime64('2018-12-26 13:30')
data_mo_su.df['moc3'].loc[:time_end_moc3]=np.nan


#------select time period for suction sensor-------
time_end_su=np.datetime64('2018-12-22 12:00')

time_end_sua1=np.datetime64('2018-12-23 13:00')
data_mo_su.df['sua1'].loc[:time_end_sua1]=np.nan

time_end_sua2=np.datetime64('2018-12-22 23:00')
data_mo_su.df['sua2'].loc[:time_end_su]=np.nan

time_end_sua3=np.datetime64('2018-12-23 23:30')
data_mo_su.df['sua3'].loc[:time_end_su]=np.nan

time_end_sub1=np.datetime64('2018-12-22 06:00')
data_mo_su.df['sub1'].loc[:time_end_sub1]=np.nan

time_end_sub3=np.datetime64('2018-12-22 03:00')
data_mo_su.df['sub3'].loc[:time_end_sub3]=np.nan

time_end_suc1=np.datetime64('2018-12-22 21:00')
data_mo_su.df['suc1'].loc[:time_end_su]=np.nan

time_end_suc2=np.datetime64('2018-12-23 09:00')
data_mo_su.df['suc2'].loc[:time_end_suc2]=np.nan

time_end_suc3=np.datetime64('2018-12-24 10:00')
data_mo_su.df['suc3'].loc[:time_end_suc3]=np.nan



#time_start_first=np.datetime64('2018-03-05T23:30')
#time_end_first=np.datetime64('2018-03-08T11:30')
##https://stackoverflow.com/questions/31617845/how-to-select-rows-in-a-dataframe-between-two-values-in-python-pandas/
#mask_first=data_mo_su.df['date_time'].between(time_start_first,time_end_first)
#data_mo_su.df.loc[mask_first,'su0']=np.nan;
#data_mo_su.df.loc[mask_first,'su1']=np.nan;
#data_mo_su.df.loc[mask_first,'su2']=np.nan;
#data_mo_su.df.loc[mask_first,'su3']=np.nan;
#data_mo_su.df.loc[mask_first,'su4']=np.nan;
#data_mo_su.df.loc[mask_first,'su5']=np.nan;
#
#time_start_second=np.datetime64('2018-03-14T20:30')
#time_end_second=np.datetime64('2018-03-17T14:30')
##https://stackoverflow.com/questions/31617845/how-to-select-rows-in-a-dataframe-between-two-values-in-python-pandas/
#mask_second=data_mo_su.df['date_time'].between(time_start_second,time_end_second)
#data_mo_su.df.loc[mask_second,'su0']=np.nan;
#data_mo_su.df.loc[mask_second,'su1']=np.nan;
#data_mo_su.df.loc[mask_second,'su2']=np.nan;
#data_mo_su.df.loc[mask_second,'su3']=np.nan;
#data_mo_su.df.loc[mask_second,'su4']=np.nan;
#data_mo_su.df.loc[mask_second,'su5']=np.nan;
#
#time_start_third=np.datetime64('2018-03-30T20:30')
#time_end_third=np.datetime64('2018-04-03T14:30')
##https://stackoverflow.com/questions/31617845/how-to-select-rows-in-a-dataframe-between-two-values-in-python-pandas/
#mask_third=data_mo_su.df['date_time'].between(time_start_third,time_end_third)
#data_mo_su.df.loc[mask_third,'su0']=np.nan;
#data_mo_su.df.loc[mask_third,'su1']=np.nan;
#data_mo_su.df.loc[mask_third,'su2']=np.nan;
#data_mo_su.df.loc[mask_third,'su3']=np.nan;
#data_mo_su.df.loc[mask_third,'su4']=np.nan;
#data_mo_su.df.loc[mask_third,'su5']=np.nan;

#data_mo_su.df['tmp3'].loc[data_mo_su.df['tmp3']<1]=np.nan;
#data_mo_su.df['tmp4'].loc[data_mo_su.df['tmp4']<1]=np.nan;
#data_mo_su.df['tmp5'].loc[data_mo_su.df['tmp5']<1]=np.nan;
#data_mo_su.df['tmp6'].loc[data_mo_su.df['tmp6']<1]=np.nan;
#data_mo_su.df['tmp7'].loc[data_mo_su.df['tmp7']<1]=np.nan;
#data_mo_su.df['tmp8'].loc[data_mo_su.df['tmp8']<1]=np.nan;
#data_mo_su.df['tmp9'].loc[data_mo_su.df['tmp9']<1]=np.nan;

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
