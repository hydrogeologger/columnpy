#import sys
#sys.modules[__name__].__dict__.clear()
import os
import numpy as np
#http://stackoverflow.com/questions/5607283/how-can-i-manually-generate-a-pyc-file-from-a-py-file
import py_compile
import sys
import matplotlib.pyplot as plt
################################get scale data####################################################################

#weather_roof=




scale=1
del scale
#os.path.dirname(os.path.realpath(__file__))
current_path=os.getcwd()
sys.path.append(current_path+'/python')
sys.path.append(current_path+'/python/pandas_scale')
py_compile.compile(current_path+'/python/pandas_scale/pandas_scale.py')

import pandas_scale
import constants
reload(pandas_scale)


#data_list_weather_roof=os.listdir(current_path+'/data/weather_roof/')
weather_roof_file_path=current_path+'/data/weather_roof/'
weather_roof_header=['date','time','scale','stable','e','f','g','h','i','j','k','l','m','n','o','p']
weather_roof=pandas_scale.pandas_scale(file_path=weather_roof_file_path,
    sep=',',
    source='raw',
    header=4,
    names=weather_roof_header
    )
weather_roof.save_as_csv (fn='weather_roof_merged.csv')
#weather_roof.save_as_hdf5(fn='weather_roof_merged.hd5')




####################################################################################################
column_roof_file_path=current_path+'/data/column_roof/'
#a=pandas_scale.pandas_scale(file_path=file_path,source='hdf5',fn_csv='scale_merged.csv',fn_hd5='scale_merged.hd5')
scale_header=['date','time','scale','stable']
scale_date_time_merge=[['date','time']]

scale=pandas_scale.pandas_scale(file_path=column_roof_file_path,
    sep='\s+',
    source='csv',
    names=scale_header,
    parse_dates=scale_date_time_merge
    )
#scale=pandas_scale.pandas_scale(file_path=column_roof_file_path,sep='\s+',source='csv',fn_csv='scale_merged.csv',fn_hd5='scale_merged.hd5')
#scale=pandas_scale.pandas_scale(file_path=column_roof_file_path,sep='\s+',source='hd5',fn_csv='scale_merged.csv',fn_hd5='scale_merged.hd5')
scale.df['scale']=scale.df['scale']*constants.g2kg   # convert g to kg
scale.surf_area1=np.pi*(0.265/2)**2

scale.save_as_csv(fn='scale_merged.csv')
#scale.save_as_hdf5(fn='scale_merged.hd5')
self=scale

####################################################################################################
sp=1
del sp
sp=pandas_scale.concat_data_roof()
sp.merge_data( df=scale.df, keys=['scale'] ,plot=True )
sp.surf_area1=np.pi*(0.265/2)**2
# get cumulative evaporation
sp.df['cum_evap']=(sp.df['scale'][0]-sp.df['scale'])/sp.surf_area1/constants.rhow_pure_water
sp.get_derivative(key='cum_evap',deri_key='evap')


sp.df.plot(x='date_time', y='cum_evap')
sp.df.plot(x='date_time', y='evap')
plt.plot(sp.df['date_time'],sp.df['evap']*constants.ms2mmday)
plt.show(block=False)
####################################################################################################
#
#
#for n in np.arange(len(file_list_column_roof)):
#    a.append_file(path_data_column_roof+file_list_column_roof[n])
#
#a.export_data_as_csv('2016-06-25_2016-07-11.dat')
##a.spline_scale_readings(coef=0.001,time_interval_sec_sp=600)
##a.spline_scale_readings(coef=0.0000001,time_interval_sec_sp=600)
##a.spline_scale_readings(coef=1e-8,time_interval_sec_sp=600)
##a.spline_scale_readings(coef=1e-10,time_interval_sec_sp=600)
##a.spline_scale_readings(coef=1e-13,time_interval_sec_sp=600)
#a.spline_scale_readings(coef=1e-14,time_interval_sec_sp=600)
##a.spline_scale_readings(coef=1e-15,time_interval_sec_sp=600)
