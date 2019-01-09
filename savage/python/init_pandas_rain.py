#import sys
#sys.modules[__name__].__dict__.clear()
import os
import numpy as np
#http://stackoverflow.com/questions/5607283/how-can-i-manually-generate-a-pyc-file-from-a-py-file
import py_compile
import sys
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib
import matplotlib.image as image
import glob, os

import pandas as pd
import pdb

import matplotlib.pylab as pylab
lw=2
ms=0.5
mew=3
grid_width=2

params = {'legend.fontsize': 6,
          'figure.figsize': (10, 5),
         'axes.labelsize': 11,
         'axes.titlesize':'11',
         'xtick.labelsize':'11',
         'ytick.labelsize':'11',
         'font.weight':'bold',
         'axes.labelweight':'bold',
         'lines.linewidth':2}#,
#         'title.fontweight':'bold'}

#         'axes.grid':'linewidth=grid_width,color = '0.5''}
#         'linewidth':lw,'markers.size':ms,'markers.edgewidth':mew}
pylab.rcParams.update(params)

lw=2
ms=6
mew=2
grid_width=2
y_fontsize=9
#fig, ax = plt.subplots(6,sharex=True,figsize=(8,9))
fig.subplots_adjust(hspace=.10)
fig.subplots_adjust(left=0.15, right=0.98, top=0.90, bottom=0.08)


for i in ax:
  for axis in ['top','bottom','left','right']:
    i.spines[axis].set_linewidth(2)


dt_s=3600
scale=1
del scale

current_path=os.getcwd()
sys.path.append   (os.environ['pyduino']+'/python/post_processing/')
py_compile.compile(os.environ['pyduino']+'/python/post_processing/pandas_scale.py')
py_compile.compile(os.environ['pyduino']+'/python/post_processing/constants.py')
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


title='grange_rain'


rain={'rain':{}}
rain
name_profile='rain'
rain[name_profile]={}
#rain[name_profile]['credential_path']=i
#rain[name_profile]['public_keys']=csv_tools.get_one_line(i)
#rain[name_profile]['web_link']=nectar_addr+"/output/"+prof[name_profile]['public_keys']
rain[name_profile]['file_path_abs']=current_path+"/data/grange_rain/"
#rain[name_profile]['file_addr_abs']=rain[name_profile]['file_path_abs']+'IDCJAC0009_097047_2018_Data.dat'
rain[name_profile]['file_addr_abs']=rain[name_profile]['file_path_abs']+'savage_rainfall_2018_Data.dat'

#data_date_time=['date_time']
data_date_time=['Year','Month','Day']
# this new function is better as it provides miniseconds parsing as well,and this is a must. 
#dateparse =  lambda x: pd.datetime.strptime(x[:-1], '%Y-%m-%dT%H:%M:%S.%f')  # sparkfun output
dateparse =  lambda x: pd.datetime.strptime(x, '%Y')  # sparkfun output
dateparse_mon =  lambda x: pd.datetime.strptime(str(x), '%m')  # sparkfun output
dateparse_day =  lambda x: pd.datetime.strptime(str(x), '%d')  # sparkfun output

dateparse_mon =  lambda x: pd.to_timedelta(x, unit='m')  # sparkfun output
dateparse_day =  lambda x: pd.to_timedelta(x, unit='d')  # sparkfun output


# 09/03/2017 remove the index column at the very beginning, by default, pandas will produce a column from first one.
#index_col_sw='Year'
data_date_time=['Year','Month','Day']
#index_col_sw='timestamp'
#index_col_sw=True



#  self.df_sub[i]=pd.read_csv(fn,sep=arg['sep'],names=arg['names'], header=arg['header'],date_parser=arg['date_parser'],parse_dates=arg['parse_dates'],index_col=arg['index_col'])
#  pd.read_csv(rain[name_profile]['file_addr_abs'],parse_dates=data_date_time)
rain['rain']['df']=pd.read_csv(rain[name_profile]['file_addr_abs'])
#pd.read_csv(rain[name_profile]['file_addr_abs'],parse_dates=data_date_time)
#rain['rain']['df'].index=rain['rain']['df']

rain['rain']['df'].index=pd.to_datetime(rain['rain']['df'][['Year', 'Month', 'Day']])

rain['rain']['df']['rain_cumsum']=rain['rain']['df']['Rainfall amount (millimetres)'].cumsum()

#ax = rain['rain']['df'].plot.bar( y='Rainfall amount (millimetres)')
#
#ax.xaxis.set_major_locator(mdates.MonthLocator())
#
#plt.show(block=False)
#
#
#ax=plt.figure()
#
#plt.bar(rain['rain']['df'].index,rain['rain']['df']['Rainfall amount (millimetres)'])
#plt.plot(rain['rain']['df'].index,rain['rain']['df']['rain_cumsum'])
#plt.show(block=False)
#



fig, ax1 = plt.subplots()

#for axis in ['top','bottom','left','right']:
#  i.spines[axis].set_linewidth(2)

ax1.bar(rain['rain']['df'].index,rain['rain']['df']['Rainfall amount (millimetres)'],color='red')
ax1.set_xlabel('DATE')
# Make the y-axis label, ticks and tick labels match the line color.
ax1.set_ylabel('RAINFALL (mm)', color='red')
ax1.tick_params('y', colors='red')

ax2 = ax1.twinx()
#s2 = np.sin(2 * np.pi * t)
ax2.plot(rain['rain']['df'].index,rain['rain']['df']['rain_cumsum'], 'k')
ax2.set_ylabel('CUMULATIVE RAINFALL (mm)', color='k')
ax2.tick_params('y', colors='k')

fig.tight_layout()

ax1.xaxis.set_major_formatter(mdates.DateFormatter('%b-%d'))
plt.show()


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


fig.savefig('figure/plot_'+sch_name+'rain.png', format='png', dpi=600)
