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
data_file_path=current_path+'/data/'    # warning, all the files should be .dat

#data_header=['deltat_c_1','deltat_c_2','deltat_c_3','ip','scale1','scale2','scale3','starttemp_c_1','starttemp_c_2','starttemp_c_3',
#    'date_time','vw_1','vw_2','vw_3']
data_header=['date_time','ip','0.0','temp3','21.54','temp2','21.59','temp1','21.69','temp7','22.6','temp6','22.2','temp5','21.4','temp4','21.48','temp8','22.71','mo28','341.0','mo29','550.36','mo22','563.36','mo23','535.45','mo26','573.09','mo27','353.0','mo24','564.09','mo25','567.18','ip2','0.0','mo31','327.91','mo30','324.91','evap2','0.0','evap1','0.0','suction8','5.591','suction7','6.391','suction6','6.316','suction5','7999.0','suction4','7999.0','suction3','7999.0','suction2','7999.0','suction1','7999.0','All','Mo1','22','563.36','Mo2','23','535.45','Mo3','24','564.09','Mo4','25','567.18','Mo5','26','573.09','Mo6','27','353.00','Mo7','28','341.00','Mo8','29','550.36','Mo9','30','324.91','Mo10','31','327.91','AllDone']

data_header=['date_time','ip','1400016','temp3','temp_suc3','temp2','temp_suc2','temp1','temp_suc1','temp7','temp_suc7','temp6','temp_suc6','temp5','temp_suc5','temp4','temp_suc4','temp8','temp_suc8','mo28','moisture_28','mo29','moisture_29_bad','mo22','moisture_22','mo23','moisture_23','mo26','moisture_26','mo27','moisture_27','mo24','moisture_24','mo25','moisture_25','ip2','0.4','mo31','moisture_31','mo30','moisture_30','evap2','0.1','evap1','0.0','suction8','su8','suction7','su7','suction6','su6','suction5','su5','suction4','su4','suction3','su3','suction2','su2','suction1','su1','teltat_c_8','dt8','teltat_c_7','dt7','teltat_c_6','dt6','teltat_c_5','dt5','teltat_c_4','dt4','teltat_c_3','dt3','teltat_c_2','dt2','teltat_c_1','dt1','All','Mo','22','mom_22','Mo','23','mom_23','Mo','24','mom_24','Mo','25','mom_25','Mo','26','mom_26','Mo','27','mom_27','Mo','28','mom_28','Mo','29','mom_29_bad','Mo','30','mom_30','Mo','31','balance_bottom','AllDone']

# things to do
#1. change csv to dat
#2. add header, 
#3. arrange header formate, 
#4. change date_time as time axis

#93 fields
#data_header=['date_time','1','2','3','4','5','6','7','8','temp7','22.6','temp6','22.2','temp5','21.4','temp4','21.48','temp8','22.71','mo28','341.0','mo29','550.36','mo22','563.36','mo23','535.45','mo26','573.09','mo27','353.0','mo24','564.09','mo25','567.18','ip2','0.0','mo31','327.91','mo30','324.91','evap2','0.0','evap1','0.0','suction8','5.591','suction7','6.391','suction6','6.316','suction5','7999.0','suction4','7999.0','suction3','7999.0','suction2','7999.0','suction1','7999.0','All','Mo','22','563.36','Mo','23','535.45','Mo','24','564.09','Mo','25','567.18','Mo','26','573.09','Mo','27','353.00','Mo','28','341.00','Mo','29','550.36','Mo','30','324.91','Mo','31','327.91','AllDone']

data_date_time=['date_time']
# 01/02/2018 please make sure date_time is the name for making date times
# 09/03/2017 here x[:-5] only sorts out from start to -5 position
# one can check the correct by
# dateparse('2017-03-09T09:02:48.588Z')
# and see if the parsing is successful
#dateparse =  lambda x: pd.datetime.strptime(x[:-5], '%Y-%m-%dT%H:%M:%S')  # sparkfun output
# this new function is better as it provides miniseconds parsing as well. 
dateparse =  lambda x: pd.datetime.strptime(x[:-1], '%Y-%m-%dT%H:%M:%S.%f')  # sparkfun output
dateparse =  lambda x: pd.datetime.strptime(x[:-1], '%d/%b/%Y %H:%M:%S')  # 18/Jun/2017 23:29:03

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
## 'date_time'  is the column with corrected time zones
#data.df['date_time']=data.df['timestamp']+pd.to_timedelta(10, unit='h')



# below are the easist way to plot the result
#data.df.plot(x='timestamp',y='deltat_c_1')
#plt.show(block=False)


#data.save_as_csv (fn='data_merged.csv')
#data.save_as_hdf5(fn='data_merged.hd5')


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


