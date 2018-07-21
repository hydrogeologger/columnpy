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
import csv_tools



dt_s=3600
scale=1
del scale

current_path=os.getcwd()
sys.path.append   (os.environ['pyduino']+'/python/post_processing/')
py_compile.compile(os.environ['pyduino']+'/python/post_processing/pandas_scale.py')
py_compile.compile(os.environ['pyduino']+'/python/post_processing/constants.py')
sys.path.append   (os.environ['pyduino']+'/python/')
python_file_path=current_path+'/python/'
sys.path.append(python_file_path)

import pandas_scale
import constants
reload(pandas_scale)
reload(constants)

if not os.path.exists('figure'):
        os.makedirs('figure')
if not os.path.exists('output_data'):
        os.makedirs('output_data')


title='compacted_redmud'

prof={'compacted_redmud':{'file_addr_abs':current_path+'/data/area51_compacted_redmud_csv_cor.dat',
        'file_path_abs':current_path+'/data/'}};

#data_date_time=['date_time']
data_date_time=['date_time']
# this new function is better as it provides miniseconds parsing as well,and this is a must. 
#dateparse =  lambda x: pd.datetime.strptime(x[:-1], '%Y-%m-%dT%H:%M:%S.%f')  # sparkfun output
dateparse =  lambda x: pd.datetime.strptime(x[:-1], '%d/%m/%Y %H:%M')  # sparkfun output

# 09/03/2017 remove the index column at the very beginning, by default, pandas will produce a column from first one.
index_col_sw=True
index_col_sw='date_time'

for key,value in prof.iteritems():
    print key
    header_string=csv_tools.get_first_line(value['file_addr_abs'])
    header=header_string.rstrip()
    value['header']=header.split(',')
    value['data']=pandas_scale.pandas_scale(file_path=value['file_path_abs'],
        source='raw',
        sep=',',
        header=3,
        names=value['header'],
        parse_dates=data_date_time,
        date_parser=dateparse,
        index_col=index_col_sw
        )
    value['data'].df.sort_index(ascending=True,inplace=True)
    value['data'].df.index=value['data'].df.index+pd.to_timedelta(10, unit='h')

prof['compacted_redmud']['data'].df['date_time']=prof['compacted_redmud']['data'].df.index
prof['compacted_redmud']['data'].df['scale']=prof['compacted_redmud']['data'].df['scale'].map(lambda x: x.replace(' ','') )
prof['compacted_redmud']['data'].df['scale']=prof['compacted_redmud']['data'].df['scale'].map(lambda x: x.replace('AllDone','') )
prof['compacted_redmud']['data'].df['scale']=prof['compacted_redmud']['data'].df['scale'].map(lambda x: x.replace('g','') )
prof['compacted_redmud']['data'].df['scale']=prof['compacted_redmud']['data'].df['scale'].map(lambda x: x.replace('?','') )
prof['compacted_redmud']['data'].df['scale']=prof['compacted_redmud']['data'].df['scale'].map(lambda x: float(x) )


#for key,value in prof.iteritems():
#    print key
#    header_string=csv_tools.get_first_line(value['file_addr_abs'])
#    header=header_string.rstrip()
#    value['header']=header.split(',')
#    value['data']=pandas_scale.pandas_scale(file_path=value['file_path_abs'],
#        source='raw',
#        sep=',',
#        header=3,
#        names=value['header'],
#        parse_dates=data_date_time,
#        date_parser=dateparse,
#        index_col=index_col_sw
#        )
#    value['data'].df.sort_index(ascending=True,inplace=True)
#    value['data'].df.index=value['data'].df.index+pd.to_timedelta(10, unit='h')








#data.df.sort_values('date_time',inplace=True)
### https://stackoverflow.com/questions/37787698/how-to-sort-pandas-dataframe-from-one-column
### reverse the dataframe by timestamp as the result is upside down
##data.df.sort_values('timestamp',inplace=True)
##
#data.df = data.df.reset_index(drop=True)
##
### 'date_time'  is the column with corrected time zones
#data.df['date_time']=data.df['date_time']+pd.to_timedelta(10, unit='h')
#
#
## it is always good to store a original data for visualisation
#data_raw=data
#data_raw2=data.df
####   special treatment
##data.df['mo_0'][data.df['mo_8']>570]=np.nan
##data.df['mo0'][data.df['mo0']>400]=np.nan
#data.df['mo1'].loc[data.df['mo1']>400]=np.nan
#data.df['mo1'].loc[data.df['mo1']<100]=np.nan
#data.df['mo2'].loc[data.df['mo2']>400]=np.nan
##data.df['mo2'].loc[data.df['mo2']<150]=np.nan
#data.df['mo3'].loc[data.df['mo3']>400]=np.nan
#data.df['mo3'].loc[data.df['mo3']<100]=np.nan
#data.df['mo4'].loc[data.df['mo4']>400]=np.nan
##data.df['mo4'].loc[data.df['mo4']<100]=np.nan
#data.df['mo4'].loc[data.df['mo4']<130]=np.nan
#data.df['mo4'][:5000][data.df['mo4'][:5000]<200]=np.nan
#data.df['mo5'].loc[data.df['mo5']>400]=np.nan
#data.df['mo5'].loc[data.df['mo5']<130]=np.nan
#
#data.df['mo6'].loc[data.df['mo6']>400]=np.nan
#
#data.df['mo7'].loc[data.df['mo7']>400]=np.nan
#data.df['mo7'].loc[data.df['mo7']<100]=np.nan
#
#
#
#data.df['mo10'].loc[data.df['mo10']>400]=np.nan
#data.df['mo10'].loc[data.df['mo10']<100]=np.nan
##
###data.df['mo7'][data.df['mo7']>400]=np.nan
##
##
##data.df['mo1'] = (data.df['mo1']**0.5  -180.0**0.5)/(300.0**0.5-180.0**0.5)
##data.df['mo2'] = (data.df['mo2']**0.5  -150.0**0.5)/(300.0**0.5-150.0**0.5)
##data.df['mo3'] = (data.df['mo3']**0.5  -150.0**0.5)/(300.0**0.5-150.0**0.5)
##data.df['mo4'] = (data.df['mo4']**0.5  -150.0**0.5)/(300.0**0.5-150.0**0.5)
##data.df['mo5'] = (data.df['mo5']**0.5  -150.0**0.5)/(300.0**0.5-150.0**0.5)
##data.df['mo7'] = (data.df['mo7']**0.5  -150.0**0.5)/(300.0**0.5-150.0**0.5)
##data.df['mo10'] = (data.df['mo10']**0.5-150.0**0.5)/(280.0**0.5-150.0**0.5)


