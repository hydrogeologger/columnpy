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
#---------below line works for 20180505 ---------------------
#data_file_path=current_path+'/data/stanwell_sali_gs3_p/'    # warning, all the files should be .dat DO NOT FORGET THE LAST SLASH


#---------below line works for 20181005 ---------------------
data_file_path=current_path+'/data/public_stanwell_sali_gs3_p/' # new downloadable data 2018-10-18


# things to do
#1. change csv to dat
#2. add header, 
#3. arrange header formate, 
#4. change date_time as time axis

#93 fields
#data_header=['date_time','1','2','3','4','5','6','7','8','temp7','22.6','temp6','22.2','temp5','21.4','temp4','21.48','temp8','22.71','mo28','341.0','mo29','550.36','mo22','563.36','mo23','535.45','mo26','573.09','mo27','353.0','mo24','564.09','mo25','567.18','ip2','0.0','mo31','327.91','mo30','324.91','evap2','0.0','evap1','0.0','suction8','5.591','suction7','6.391','suction6','6.316','suction5','7999.0','suction4','7999.0','suction3','7999.0','suction2','7999.0','suction1','7999.0','All','Mo','22','563.36','Mo','23','535.45','Mo','24','564.09','Mo','25','567.18','Mo','26','573.09','Mo','27','353.00','Mo','28','341.00','Mo','29','550.36','Mo','30','324.91','Mo','31','327.91','AllDone']
#data_header=['dhthum0','dhttmp0','dp0','dp1','ec0','ec1','gstemp1','gstmp0','hum0','hum1','hum2','pre0','pre1','pretmp0','pretmp1','date_time','tmp0','tmp1','tmp10','tmp11','tmp12','tmp2','tmp4','tmp5','tmp6','tmp7','tmp8','tmp9','volt0']
data_header=['dhthum0','dhttmp0','dp0','ec0','gstmp0','hum0','hum1','hum2','hum3','pre0','pre1','pretmp0','pretmp1','date_time','tmp0','tmp1','tmp10','tmp11','tmp12','tmp2','tmp3','tmp4','tmp5','tmp6','tmp7','tmp8','tmp9','volt0']


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


data.df.sort_values('date_time',inplace=True)
## https://stackoverflow.com/questions/37787698/how-to-sort-pandas-dataframe-from-one-column
## reverse the dataframe by timestamp as the result is upside down
#data.df.sort_values('timestamp',inplace=True)
#
data.df = data.df.reset_index(drop=True)
#
### 'date_time'  is the column with corrected time zones
##data.df['date_time']=data.df['date_time']+pd.to_timedelta(10, unit='h')
##



#        if (d.su0<5 || d.su0>20){ d.su0=NaN};
#        if (d.su1<5 || d.su1>20){ d.su1=NaN};
#        if (d.su2<5 || d.su2>20){ d.su2=NaN};
#        if (d.su3<5 || d.su3>20){ d.su3=NaN};
#        if (d.su4<5 || d.su4>20){ d.su4=NaN};
#        if (d.su5<5 || d.su5>20){ d.su5=NaN};
#        if (d.su6<5 || d.su6>20){ d.su6=NaN};
#        if (d.su7<5 || d.su7>20){ d.su7=NaN};
#        if (d.su8<5 || d.su8>20){ d.su8=NaN};
#        if (d.su9<5 || d.su9>20){ d.su9=NaN};


#data.df['tmp0'].loc[data.df['tmp0']<1]=np.nan;
#data.df['tmp1'].loc[data.df['tmp1']<1]=np.nan;
#data.df['tmp2'].loc[data.df['tmp2']<1]=np.nan;
#data.df['tmp3'].loc[data.df['tmp3']<1]=np.nan;
#data.df['tmp4'].loc[data.df['tmp4']<1]=np.nan;
#data.df['tmp5'].loc[data.df['tmp5']<1]=np.nan;
#data.df['tmp6'].loc[data.df['tmp6']<1]=np.nan;
#data.df['tmp7'].loc[data.df['tmp7']<1]=np.nan;
#data.df['tmp8'].loc[data.df['tmp8']<1]=np.nan;
#data.df['tmp9'].loc[data.df['tmp9']<1]=np.nan;

data.df['pre0'][data.df['pre0']>1060]=np.nan
data.df['pre1'][data.df['pre1']>1120]=np.nan
data.df['pre0'][data.df['pre0']<1000]=np.nan
data.df['pre1'][data.df['pre1']<1000]=np.nan
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


