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


################################get scale data####################################################################


dt_s=3600
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

if not os.path.exists('figure'):
        os.makedirs('figure')
if not os.path.exists('output_data'):
        os.makedirs('output_data')


python_file_path=current_path+'/python/'
sys.path.append(python_file_path)
# change the date time header as datetime to make life easier
#data_list_data_roof=os.listdir(current_path+'/data/data_roof/')
#data_file_path=current_path+'/data/'+folder_name+'/'    # warning, all the files should be .dat


data_header=['mo0','mo1','mo10','mo11','mo12','mo13','mo14','mo15','mo2','mo3','mo4','mo5','mo6','mo7','mo8',
    'mo9','su1','su2','su3','su4','date_time','tp1','tp11','tp2','tp3','tp4','tp8d','tpa3','tpf0','tphr45','tphr47']

data_date_time=['date_time']
# 09/03/2017 here x[:-5] only sorts out from start to -5 position
# one can check the correct by
# this new function is better as it provides miniseconds parsing as well,and this is a must. 
dateparse =  lambda x: pd.datetime.strptime(x[:-1], '%Y-%m-%dT%H:%M:%S.%f')  # sparkfun output

# 09/03/2017 remove the index column at the very beginning, by default, pandas will produce a column from first one.
index_col_sw=False
#index_col_sw=True

data=pandas_scale.pandas_scale(file_path=daisy_sensor.file_dir,
    source='raw',
    sep=',',
    header=3,
    names=data_header,
    parse_dates=data_date_time,
    date_parser=dateparse,
    index_col=index_col_sw
    )


data.df.sort_values('date_time',inplace=True)
## https://stackoverflow.com/questions/37787698/how-to-sort-pandas-dataframe-from-one-column
## reverse the dataframe by timestamp as the result is upside down
#data.df.sort_values('timestamp',inplace=True)
#
data.df = data.df.reset_index(drop=True)
#
## 'date_time'  is the column with corrected time zones
data.df['date_time']=data.df['date_time']+pd.to_timedelta(10, unit='h')


# it is always good to store a original data for visualisation
data_raw=data
data_raw2=data.df
###   special treatment
#data.df['mo_0'][data.df['mo_8']>570]=np.nan
#data.df['mo0'][data.df['mo0']>400]=np.nan
data.df['mo1'].loc[data.df['mo1']>400]=np.nan
data.df['mo1'].loc[data.df['mo1']<100]=np.nan
data.df['mo2'].loc[data.df['mo2']>400]=np.nan
#data.df['mo2'].loc[data.df['mo2']<150]=np.nan
data.df['mo3'].loc[data.df['mo3']>400]=np.nan
data.df['mo3'].loc[data.df['mo3']<100]=np.nan
data.df['mo4'].loc[data.df['mo4']>400]=np.nan
#data.df['mo4'].loc[data.df['mo4']<100]=np.nan
data.df['mo4'].loc[data.df['mo4']<130]=np.nan
data.df['mo4'][:5000][data.df['mo4'][:5000]<200]=np.nan
data.df['mo5'].loc[data.df['mo5']>400]=np.nan
data.df['mo5'].loc[data.df['mo5']<130]=np.nan

data.df['mo6'].loc[data.df['mo6']>400]=np.nan

data.df['mo7'].loc[data.df['mo7']>400]=np.nan
data.df['mo7'].loc[data.df['mo7']<100]=np.nan



data.df['mo10'].loc[data.df['mo10']>400]=np.nan
data.df['mo10'].loc[data.df['mo10']<100]=np.nan
#
##data.df['mo7'][data.df['mo7']>400]=np.nan
#
#
#data.df['mo1'] = (data.df['mo1']**0.5  -180.0**0.5)/(300.0**0.5-180.0**0.5)
#data.df['mo2'] = (data.df['mo2']**0.5  -150.0**0.5)/(300.0**0.5-150.0**0.5)
#data.df['mo3'] = (data.df['mo3']**0.5  -150.0**0.5)/(300.0**0.5-150.0**0.5)
#data.df['mo4'] = (data.df['mo4']**0.5  -150.0**0.5)/(300.0**0.5-150.0**0.5)
#data.df['mo5'] = (data.df['mo5']**0.5  -150.0**0.5)/(300.0**0.5-150.0**0.5)
#data.df['mo7'] = (data.df['mo7']**0.5  -150.0**0.5)/(300.0**0.5-150.0**0.5)
#data.df['mo10'] = (data.df['mo10']**0.5-150.0**0.5)/(280.0**0.5-150.0**0.5)


