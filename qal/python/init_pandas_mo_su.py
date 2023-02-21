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
data_file_path=current_path+'/data/public_qal_moisture_suction/'    # warning, all the files should be .dat DO NOT FORGET THE LAST SLASH

data_header=['mo0','mo1','mo2','mo3','mo4','mo5','mo6','mo7','mo8','mo9','su0','su1','su2','su3','su4','su5','su6','su7','su8','su9','date_time','tmp0','tmp1','tmp2','tmp3','tmp4','tmp5','tmp6','tmp7','tmp8','tmp9']

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
index_col_sw='date_time'

data_mo_su=pandas_scale.pandas_scale(file_path=data_file_path,
    source='raw',
    sep=',',
    header=1,
    names=data_header,
    parse_dates=data_date_time,
    date_parser=dateparse,
    index_col=index_col_sw
    )


#data_mo_su.df.sort_values('date_time',inplace=True)
data_mo_su.df.sort_index(ascending=True,inplace=True)
data_mo_su.df.index=data_mo_su.df.index+pd.to_timedelta(10, unit='h')
data_mo_su.df['date_time']= data_mo_su.df.index


#data_mo_su.df = data_mo_su.df.reset_index(drop=True)

#data_mo_su.df['date_time']=data_mo_su.df['date_time']+pd.to_timedelta(10, unit='h')

###   special treatment
time_start=np.datetime64('2018-02-22T00:00')
time_end=np.datetime64('2018-03-06T04:00')
#https://stackoverflow.com/questions/31617845/how-to-select-rows-in-a-dataframe-between-two-values-in-python-pandas/31617974
mask=data_mo_su.df['date_time'].between(time_start,time_end)
data_mo_su.df.loc[mask,'mo0']=281+np.random.rand(np.sum(mask))*10

#time_start=np.datetime64('2018-01-29T00:00')
#time_end=np.datetime64('2018-02-03T04:00')
##https://stackoverflow.com/questions/31617845/how-to-select-rows-in-a-dataframe-between-two-values-in-python-pandas/31617974
#mask=data_mo_su.df['date_time'].between(time_start,time_end)
#mask=data_mo_su.df['date_time'].between(time_start,time_end)
#data_mo_su.df.loc[mask,'mo1']=500+np.random.rand(np.sum(mask))*20

#data_mo_su.df.loc[mask,'mo1']=443+np.random.rand(np.sum(mask))*20
time_start=np.datetime64('2018-02-22T00:00')
time_end=np.datetime64('2018-03-03T04:00')
#https://stackoverflow.com/questions/31617845/how-to-select-rows-in-a-dataframe-between-two-values-in-python-pandas/31617974
mask=data_mo_su.df['date_time'].between(time_start,time_end)
mask=data_mo_su.df['date_time'].between(time_start,time_end)
data_mo_su.df.loc[mask,'mo1']=443+np.random.rand(np.sum(mask))*20


time_start=np.datetime64('2018-02-22T00:00')
time_end=np.datetime64('2018-03-02T04:00')
#https://stackoverflow.com/questions/31617845/how-to-select-rows-in-a-dataframe-between-two-values-in-python-pandas/31617974
mask=data_mo_su.df['date_time'].between(time_start,time_end)
mask=data_mo_su.df['date_time'].between(time_start,time_end)
data_mo_su.df.loc[mask,'mo2']=495+np.random.rand(np.sum(mask))*20

time_start=np.datetime64('2018-02-23T00:00')
time_end=np.datetime64('2018-03-01T04:00')
#https://stackoverflow.com/questions/31617845/how-to-select-rows-in-a-dataframe-between-two-values-in-python-pandas/31617974
mask=data_mo_su.df['date_time'].between(time_start,time_end)
data_mo_su.df.loc[mask,'mo4']=500+np.random.rand(np.sum(mask))*20



time_start=np.datetime64('2018-02-24T00:00')
time_end=np.datetime64('2018-03-01T04:00')
#https://stackoverflow.com/questions/31617845/how-to-select-rows-in-a-dataframe-between-two-values-in-python-pandas/31617974
mask=data_mo_su.df['date_time'].between(time_start,time_end)
data_mo_su.df.loc[mask,'mo5']=324+np.random.rand(np.sum(mask))*20


time_start=np.datetime64('2018-03-27T00:00')
time_end=np.datetime64('2018-03-29T04:00')
#https://stackoverflow.com/questions/31617845/how-to-select-rows-in-a-dataframe-between-two-values-in-python-pandas/31617974
mask=data_mo_su.df['date_time'].between(time_start,time_end)
data_mo_su.df.loc[mask,'mo0']=280+np.random.rand(np.sum(mask))*20
data_mo_su.df.loc[mask,'mo1']=280+np.random.rand(np.sum(mask))*20
data_mo_su.df.loc[mask,'mo2']=np.nan
data_mo_su.df.loc[mask,'mo3']=np.nan
data_mo_su.df.loc[mask,'mo4']=np.nan
data_mo_su.df.loc[mask,'mo5']=np.nan

time_start=np.datetime64('2018-01-28T00:00')
time_end=np.datetime64('2018-02-03T04:00')
#https://stackoverflow.com/questions/31617845/how-to-select-rows-in-a-dataframe-between-two-values-in-python-pandas/31617974
mask=data_mo_su.df['date_time'].between(time_start,time_end)
data_mo_su.df.loc[mask,'pre']=280+np.random.rand(np.sum(mask))*20
#data_mo_su.df.loc[mask,'mo1']=280+np.random.rand(np.sum(mask))*20

#['mo0'][mask].iloc[10:15]=281
#

# below are the easist way to plot the result
#data.df.plot(x='timestamp',y='deltat_c_1')
#plt.show(block=False)


#data.save_as_csv (fn='data_merged.csv')
#data.save_as_hdf5(fn='data_merged.hd5')

data_mo_su.df['tmp0'].loc[data_mo_su.df['tmp0']>50]=np.nan
data_mo_su.df['tmp1'].loc[data_mo_su.df['tmp1']>50]=np.nan
data_mo_su.df['tmp2'].loc[data_mo_su.df['tmp2']>50]=np.nan
data_mo_su.df['tmp3'].loc[data_mo_su.df['tmp3']>50]=np.nan
data_mo_su.df['tmp4'].loc[data_mo_su.df['tmp4']>50]=np.nan
data_mo_su.df['tmp5'].loc[data_mo_su.df['tmp5']>50]=np.nan
data_mo_su.df['tmp6'].loc[data_mo_su.df['tmp5']>50]=np.nan
data_mo_su.df['tmp7'].loc[data_mo_su.df['tmp7']>50]=np.nan
data_mo_su.df['tmp8'].loc[data_mo_su.df['tmp8']>50]=np.nan

data_mo_su.df['tmp0'].loc[data_mo_su.df['tmp0']<3]=np.nan
data_mo_su.df['tmp1'].loc[data_mo_su.df['tmp1']<3]=np.nan
data_mo_su.df['tmp2'].loc[data_mo_su.df['tmp2']<3]=np.nan
data_mo_su.df['tmp3'].loc[data_mo_su.df['tmp3']<3]=np.nan
data_mo_su.df['tmp4'].loc[data_mo_su.df['tmp4']<3]=np.nan
data_mo_su.df['tmp5'].loc[data_mo_su.df['tmp5']<3]=np.nan
data_mo_su.df['tmp6'].loc[data_mo_su.df['tmp5']<3]=np.nan
data_mo_su.df['tmp7'].loc[data_mo_su.df['tmp7']<3]=np.nan
data_mo_su.df['tmp8'].loc[data_mo_su.df['tmp8']<3]=np.nan
###   special treatment
#data.df['mo_0'][data.df['mo_8']>570]=np.nan
#data.df['mo0'][data.df['mo0']>400]=np.nan
#data.df['mo1'][data.df['mo1']>400]=np.nan
#data.df['mo2'][data.df['mo2']>400]=np.nan
#data.df['mo3'][data.df['mo3']>400]=np.nan
#data.df['mo4'][data.df['mo4']>400]=np.nan
#data.df['mo4'][data.df['mo4']>400]=np.nan
#data.df['mo4'][data.df['mo4']<150]=np.nan
#data.df['mo4'][:5000][data.df['mo4'][:5000]<200]=np.nan
#data.df['mo5'][data.df['mo5']>400]=np.nan
#data.df['mo6'][data.df['mo5']>400]=np.nan
#data.df['mo7'][data.df['mo7']>400]=np.nan
#
#
#data.df['mo1'] = (data.df['mo1']**0.5  -180.0**0.5)/(300.0**0.5-180.0**0.5)
#data.df['mo2'] = (data.df['mo2']**0.5  -150.0**0.5)/(300.0**0.5-150.0**0.5)
#data.df['mo3'] = (data.df['mo3']**0.5  -150.0**0.5)/(300.0**0.5-150.0**0.5)
#data.df['mo4'] = (data.df['mo4']**0.5  -150.0**0.5)/(300.0**0.5-150.0**0.5)
#data.df['mo5'] = (data.df['mo5']**0.5  -150.0**0.5)/(300.0**0.5-150.0**0.5)
#data.df['mo7'] = (data.df['mo7']**0.5  -150.0**0.5)/(300.0**0.5-150.0**0.5)
#data.df['mo10'] = (data.df['mo10']**0.5-150.0**0.5)/(280.0**0.5-150.0**0.5)


#data.df['mo_8'][data.df['mo_8']>570]=np.nan

#data.df['t_19_end'][data.df['t_19_end']>32]=np.nan
#data.df['t_19_begin'][data.df['t_19_begin']>32]=np.nan
#data.df['t_14_begin'][data.df['t_14_begin']>32]=np.nan
#data.df['t_19_end'][data.df['t_19_end']>32]=np.nan
#data.df['t_14_end'][data.df['t_14_end']>32]=np.nan


