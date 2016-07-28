#import sys
#sys.modules[__name__].__dict__.clear()
import os
import numpy as np
#http://stackoverflow.com/questions/5607283/how-can-i-manually-generate-a-pyc-file-from-a-py-file
import py_compile
import sys
a=1
del a
#os.path.dirname(os.path.realpath(__file__))
current_path=os.getcwd()
#path_column_roof='/home/chenming/Dropbox/tailing_column/data/column_on_roof/'
data_list_column_roof=os.listdir(current_path+'/data/column_on_roof/')
file_path=current_path+'/data/column_on_roof/'
#execfile('class_scale.py')
sys.path.append(current_path+'/python/pandas_scale')
sys.path.append(current_path+'/python')
py_compile.compile(current_path+'/python/pandas_scale/pandas_scale.py')
import pandas_scale
import constants
reload(pandas_scale)

#a=pandas_scale.pandas_scale(file_path,source='raw')
#a=pandas_scale.pandas_scale(file_path,source='csv')
a=pandas_scale.pandas_scale(file_path,source='hdf5')
a.df['scale']=a.df['scale']*constants.g2kg   # convert g to kg
a.surf_area1=np.pi*(0.265/2)**2

#
#a.surf_area1=np.pi*(0.265/2)**2
#a.save_as_csv(fn='scale_merged.csv')
#a.save_as_hdf5(fn='scale_merged.hd5')
self=a


sp=pandas_scale.concat_data_roof()
sp.merge_data( df=a.df, keys=['scale'] ,plot=True )
sp.surf_area1=np.pi*(0.265/2)**2
# get cumulative evaporation
sp.df['cum_evap']=(sp.df['scale'][0]-sp.df['scale'])/sp.surf_area1/constants.rhow_pure_water



#sp.df.plot(x='date_time', y='cum_evap')

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
