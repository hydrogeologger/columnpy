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


dt_s=7200
scale=1
del scale
#os.path.dirname(os.path.realpath(__file__))
current_path=os.getcwd()
sys.path.append('/home/chenming/Dropbox/scripts/github/pyduino/python/post_processing/')
py_compile.compile('/home/chenming/Dropbox/scripts/github/pyduino/python/post_processing/pandas_scale.py')
py_compile.compile('/home/chenming/Dropbox/scripts/github/pyduino/python/post_processing/constants.py')

import pandas_scale
import constants
reload(pandas_scale)
reload(constants)


# change the date time header as datetime to make life easier
#data_list_weather_roof=os.listdir(current_path+'/data/weather_roof/')
sensors_file_path=current_path+'/arduino/'    # warning, all the files should be .dat
#sensors_header=['date_time','soil1','suckheat','28e5'
#,'heating','e5h_1','e5h_2','e5h_3','e5h_4',
#'e5h_5','e5h_6','e5h_7','e5h_8','e5h_9','e5h_10','e5h_11','e5h_12','e5h_13','e5h_14','e5h_15','e5h_16','e5h_17',
#'e5h_18','e5h_19','e5h_20','e5h_21'
#,'Dsping','e5d_1','e5d_2','e5d_3','e5d_4','e5d_5','e5d_6','e5d_7','e5d_8',
#'e5d_9','e5d_10','e5d_11','e5d_12','e5d_13','e5d_14','e5d_15','e5d_16','e5d_17','e5d_18','e5d_19','e5d_20','e5d_21',
sensors_header=['saltrh_2_rh','suht_28e5_begin','mo_10','suht_28e5_peak','saltrh_3_rh',
'suht_2847_end','suht_28e5_end','saltrh_3_tp','saltrh_2_tp','mo_8','mo_9','suht_2847_begin',
'mo_7','suht_2847_peak','date_time']

weather_date_time=['date_time']
# 09/03/2017 here x[:-5] only sorts out from start to -5 position
# one can check the correct by
# dateparse('2017-03-09T09:02:48.588Z')
# and see if the parsing is successful
dateparse =  lambda x: pd.datetime.strptime(x[:-5], '%Y-%m-%dT%H:%M:%S')  # sparkfun output
#dateparse =  lambda x: pd.datetime.strptime(x[:-6], '%Y-%m-%dT%H:%M:%S')
#dateparse =  lambda x: pd.datetime.strptime(x[:-6], '%Y-%m-%dT%H:%M:%S')
#dateparse =  lambda x: pd.datetime.strptime(x, '%Y-%m-%dT%H:%M:%S')
#dateparse =  lambda x: pd.datetime.strptime(x, '%d/%b/%Y %H:%M:%S')

# 09/03/2017 remove the index column at the very beginning, by default, pandas will produce a column from first one.
index_col_sw=False

sensors=pandas_scale.pandas_scale(file_path=sensors_file_path,
    source='raw',
    sep=',',
    header=1,
    names=sensors_header,
    parse_dates=weather_date_time,
    date_parser=dateparse,
    index_col=index_col_sw
    )

# remove small values
#start_index, start_value = min(enumerate( abs(sensors.df['date_time']-datetime.datetime(2017,2,22,0,0))), key=operator.itemgetter(1))
#end_index, end_value = min(enumerate( abs(sensors.df['date_time']-datetime.datetime(2017,3,1,0,0))), key=operator.itemgetter(1))
#sensors.df['suht_28e5_peak'][end_index]
#sensors.append_file(file_path=sensors_file_path+'append_files/',
#    sep=',',
#    header=4,
#    names=sensors_header,
#    parse_dates=weather_date_time,
#    date_parser=dateparse
#    )


# convert string column to float column, current
# http://stackoverflow.com/questions/15891038/pandas-change-data-type-of-columns
#sensors.df['R_up']=pd.to_numeric(sensors.df['R_up'],errors='coerce')
# remove the row that has NAN inside
# the reason it needs to be droped is because SmoothSpline does not like NaN. which is bad
#http://stackoverflow.com/questions/13413590/how-to-drop-rows-of-pandas-dataframe-whose-value-of-certain-column-is-nan
#sensors.df=sensors.df.dropna()

#sensors.save_as_csv (fn='sensors_merged.csv')
#sensors.save_as_hdf5(fn='sensors_merged.hd5')




###################################reading scale class#################################################################
column_roof_file_path=current_path+'/scale/'
scale_header=['measure_local_time','tas606','te','date_time']

#scale_date_time_merge=[['date','time']]
scale_date_time=['date_time']
#https://docs.python.org/2/library/datetime.html

dateparse =  lambda x: pd.datetime.strptime(x[:-5], '%Y-%m-%dT%H:%M:%S')  # sparkfun output
#dateparse =  lambda x: pd.datetime.strptime(x, '%d/%b/%Y %H:%M:%S')
# 21/Nov/2016 12:04:40      5154 g
## using raw material for parsing
scale=pandas_scale.pandas_scale(file_path=column_roof_file_path,
    source='raw',
    sep=',',
    names=scale_header,
    parse_dates=scale_date_time,
    date_parser=dateparse,
    index_col=index_col_sw
    )
### ------------------------some modification to the files ------------------------
#scale.df.tas606[scale.df.tas606>241786]=np.nan
scale.df.loc[:,'tas606'][ scale.df.tas606>241786]=np.nan
scale.df.loc[:,'te'][ scale.df.te>203]=np.nan
scale.df.loc[:,'te'][ scale.df.te<160]=np.nan
## using csv file for parsing
#scale=pandas_scale.pandas_scale(file_path=column_roof_file_path,
#    source='csv',
#    sep='\s+',
#    names=scale_header,
#    parse_dates=scale_date_time_merge
#    )
#scale=pandas_scale.pandas_scale(file_path=column_roof_file_path,sep='\s+',source='csv',fn_csv='scale_merged.csv',fn_hd5='scale_merged.hd5')
#scale=pandas_scale.pandas_scale(file_path=column_roof_file_path,sep='\s+',source='hd5',fn_csv='scale_merged.csv',fn_hd5='scale_merged.hd5')
#scale.df['scale']=scale.df['scale']*constants.g2kg   # convert g to kg
# here is the place to play with the accuracy of the scales...
# below is 50g accuracy
#scale.df['scale']=np.around(scale.df['scale']*constants.g2kg*2,1)/2.0   # round 
# 100g accuracy
#scale.df['scale']=np.around(scale.df['scale']*constants.g2kg,1)   # round 

#scale.surf_area1=np.pi*(0.21/2)**2
#
#scale.save_as_csv(fn='scale_merged.csv')
##scale.save_as_hdf5(fn='scale_merged.hd5')
#self=scale

###-------------------------------  reading balance data --------------
balance_file_path=current_path+'/balances/'
balance_header=['measure_local_time','ohaus','commercial','nvl','date_time']
#scale_date_time_merge=[['date','time']]
balance_date_time=['date_time']
#https://docs.python.org/2/library/datetime.html

dateparse =  lambda x: pd.datetime.strptime(x[:-5], '%Y-%m-%dT%H:%M:%S')  # sparkfun output
## using raw material for parsing
balance=pandas_scale.pandas_scale(file_path=balance_file_path,
    source='raw',
    sep=',',
    names=balance_header,
    parse_dates=balance_date_time,
    date_parser=dateparse,
    index_col=index_col_sw
    )

balance.df.loc[:,'commercial'][ balance.df.commercial>14500]=np.nan
balance.df.loc[:,'commercial'][ balance.df.commercial<10000]=np.nan


####################################################################################################
sp=1
del sp
sp=pandas_scale.concat_data_roof(pd.Timestamp('2017-02-07 07:55'),  pd.Timestamp('2017-04-4 12:54:11'),dt_s)
sp.merge_data( df=scale.df, keys=['tas606'] ,plot=True ,coef=5e-16)
sp.merge_data( df=scale.df, keys=['te'] ,plot=True ,coef=5e-16)
sp.merge_data( df=sensors.df, keys=['saltrh_2_rh'] ,plot=True ,coef=5e-10)
sp.merge_data( df=sensors.df, keys=['saltrh_3_rh'] ,plot=True ,coef=5e-10)
sp.merge_data( df=sensors.df, keys=['suht_28e5_begin'] ,plot=True ,coef=5e-10)
sp.merge_data( df=sensors.df, keys=['suht_2847_begin'] ,plot=True ,coef=5e-10)

sp.merge_data( df=sensors.df, keys=['suht_28e5_peak'] ,plot=True ,coef=5e-10)
sp.merge_data( df=sensors.df, keys=['suht_2847_peak'] ,plot=True ,coef=5e-10)

sp.merge_data( df=sensors.df, keys=['suht_28e5_end'] ,plot=True ,coef=5e-10)
sp.merge_data( df=sensors.df, keys=['suht_2847_end'] ,plot=True ,coef=5e-10)
sp.merge_data( df=sensors.df, keys=['saltrh_3_tp'] ,plot=True ,coef=5e-10)
sp.merge_data( df=sensors.df, keys=['saltrh_2_tp'] ,plot=True ,coef=5e-10)

sp.merge_data( df=sensors.df, keys=['mo_7'] ,plot=True ,coef=5e-15)
sp.merge_data( df=sensors.df, keys=['mo_8'] ,plot=True ,coef=5e-15)
sp.merge_data( df=sensors.df, keys=['mo_9'] ,plot=True ,coef=5e-15)
sp.merge_data( df=sensors.df, keys=['mo_10'] ,plot=True ,coef=5e-15)
sp.merge_data( df=balance.df, keys=['commercial'] ,plot=True ,coef=5e-15)

sp.df=sp.df.reset_index(drop=True)
## add new column
## http://stackoverflow.com/questions/12555323/adding-new-column-to-existing-dataframe-in-python-pandas
sp.df=sp.df.assign(
    time_days=[(sp.df['date_time'][x]-sp.df['date_time'][0]).total_seconds()/86400
            for x in range(len(sp.df['date_time']))])

####################################################################################################
import operator
sp_sch={}
for line in open("schedule.ipt"):
    li=line.strip()
    if not li.startswith("#"):
        line_content=[x.strip() for x in li.split(',')]
        sch_name=line_content[2]
        sp_sch[sch_name]={};
        sp_sch[sch_name]['start_dt']=pd.datetime.strptime(line_content[0],'%Y/%b/%d %H:%M')
        sp_sch[sch_name]['end_dt']=pd.datetime.strptime(line_content[1],'%Y/%b/%d %H:%M')
        sp_sch[sch_name]['water_level']   =float(line_content[3])
        sp_sch[sch_name]['surface_area']  =float(line_content[4])
        sp_sch[sch_name]['soil_thickness']=float(line_content[5])
        sp_sch[sch_name]['time_surface_emerge'] = pd.datetime.strptime(line_content[10],'%Y/%b/%d %H:%M')

        sp_sch[sch_name]['por']=float(line_content[6])
        sp_sch[sch_name]['te_coef']=float(line_content[8])
        sp_sch[sch_name]['tas606_coef']=float(line_content[9])
        min_index, min_value = min(enumerate( abs(sp.df['date_time']-sp_sch[sch_name]['start_dt'])), key=operator.itemgetter(1))
        sp_sch[sch_name]['start_ind']=min_index
        min_index, min_value = min(enumerate( abs(sp.df['date_time']-sp_sch[sch_name]['end_dt'])), key=operator.itemgetter(1))
        sp_sch[sch_name]['end_ind']=min_index
        sp_sch[sch_name]['df']=sp.df[sp_sch[sch_name]['start_ind']:sp_sch[sch_name]['end_ind']]
        ## reset index
        sp_sch[sch_name]['df']=sp_sch[sch_name]['df'].reset_index(drop=True)
        ## add new column
        ## http://stackoverflow.com/questions/12555323/adding-new-column-to-existing-dataframe-in-python-pandas
        sp_sch[sch_name]['df']=sp_sch[sch_name]['df'].assign(
            time_days=[(sp_sch[sch_name]['df']['date_time'][x]-sp_sch[sch_name]['df']['date_time'][0]).total_seconds()/86400
                    for x in range(len(sp_sch[sch_name]['df']['date_time']))])

        min_index, min_value = min(enumerate( abs(sp_sch[sch_name]['df']['date_time']- sp_sch[sch_name]['time_surface_emerge'] 
            )), key=operator.itemgetter(1))
        sp_sch[sch_name]['idx_surface_emerge'] = min_index 

        sp_sch[sch_name]['df']['cum_evap_te']=(sp_sch[sch_name]['df']['te'][0]-sp_sch[sch_name]['df']['te']
            )*constants.g2kg/sp_sch[sch_name]['surface_area']/constants.rhow_pure_water/sp_sch[sch_name]['te_coef']  
        sp_sch[sch_name]['df']['evap_rate_te']=np.append(np.diff(sp_sch[sch_name]['df']['cum_evap_te'] ),np.nan)/dt_s
        sp_sch[sch_name]['df']['cum_evap_tas606']=(sp_sch[sch_name]['df']['tas606'][0]-sp_sch[sch_name]['df']['tas606']
            )*constants.g2kg/sp_sch[sch_name]['surface_area']/constants.rhow_pure_water/sp_sch[sch_name]['tas606_coef']  
        sp_sch[sch_name]['df']['evap_rate_tas606']=np.append(np.diff(sp_sch[sch_name]['df']['cum_evap_tas606'] ),np.nan)/dt_s

        sp_sch[sch_name]['df']['cum_evap_commercial']=(sp_sch[sch_name]['df']['commercial'][0]-sp_sch[sch_name]['df']['commercial']
            )*constants.g2kg/sp_sch[sch_name]['surface_area']/constants.rhow_pure_water
        sp_sch[sch_name]['df']['evap_rate_commercial']=np.append(np.diff(sp_sch[sch_name]['df']['cum_evap_commercial'] ),np.nan)/dt_s
        
        total_water_depth=sp_sch[sch_name]['por']*sp_sch[sch_name]['soil_thickness']
        sp_sch[sch_name]['df']['sat_commercial']=(total_water_depth-(
            sp_sch[sch_name]['df']['cum_evap_commercial']-sp_sch[sch_name]['df']['cum_evap_commercial'][sp_sch[sch_name]['idx_surface_emerge']])
            )/total_water_depth

        #sp_sch[sch_name]['df']['sat_commercial']=(sp_sch[sch_name]['por']*sp_sch[sch_name]['soil_thickness']-(
        #    sp_sch[sch_name]['df']['cum_evap_commercial']-sp_sch[sch_name]['df']['cum_evap_commercial'][sp_sch[sch_name]['idx_surface_emerge']])
        #    )/sp_sch[sch_name]['por']/sp_sch[sch_name]['soil_thickness']

        sp_sch[sch_name]['df']['sat_commercial'][sp_sch[sch_name]['df']['sat_commercial']>1]=1


fig, ax = plt.subplots(2,sharex=False)
sch_name='coal_first'
ax[1].plot(sp_sch[sch_name]['df'] ['sat_commercial'], sp_sch[sch_name]['df']  ['mo_7'],'r+') 
ax[1].plot(sp_sch[sch_name]['df'] ['sat_commercial'], sp_sch[sch_name]['df']  ['mo_8'],'g+') 
ax[0].plot(sp_sch[sch_name]['df'] ['sat_commercial'], sp_sch[sch_name]['df']  ['mo_9'],'b+') 
ax[0].plot(sp_sch[sch_name]['df'] ['sat_commercial'], sp_sch[sch_name]['df']  ['mo_10'],'c+') 
sch_name='coal_second'
ax[1].plot(sp_sch[sch_name]['df'] ['sat_commercial'], sp_sch[sch_name]['df']  ['mo_7'] ,'ro') 
ax[1].plot(sp_sch[sch_name]['df'] ['sat_commercial'], sp_sch[sch_name]['df']  ['mo_8'] ,'go') 
ax[0].plot(sp_sch[sch_name]['df'] ['sat_commercial'], sp_sch[sch_name]['df']  ['mo_9'] ,'bo') 
ax[0].plot(sp_sch[sch_name]['df'] ['sat_commercial'], sp_sch[sch_name]['df']  ['mo_10'],'co') 
sch_name='coal_third'
ax[1].plot(sp_sch[sch_name]['df'] ['sat_commercial'], sp_sch[sch_name]['df']  ['mo_7'] ,'rx') 
ax[1].plot(sp_sch[sch_name]['df'] ['sat_commercial'], sp_sch[sch_name]['df']  ['mo_8'] ,'gx') 
ax[0].plot(sp_sch[sch_name]['df'] ['sat_commercial'], sp_sch[sch_name]['df']  ['mo_9'] ,'bx') 
ax[0].plot(sp_sch[sch_name]['df'] ['sat_commercial'], sp_sch[sch_name]['df']  ['mo_10'],'cx') 
plt.show(block=False)
#ax[0].plot(sp_sch['coal_second']['df']['date_time'], sp_sch['coal_second']['df'] ['cum_evap_te']*constants.m2mm,'g+') 
#ax[0].plot(sp_sch['coal_third']['df'] ['date_time'], sp_sch['coal_third']['df']  ['cum_evap_te']*constants.m2mm,'b+') 


xfmt = mdates.DateFormatter('%y-%m-%d %H:%M')
fig, ax = plt.subplots(2,sharex=False)
ax[0].plot(sp_sch['coal_first']['df'] ['date_time'], sp_sch['coal_first']['df']  ['cum_evap_te']*constants.m2mm,'r+') 
ax[0].plot(sp_sch['coal_second']['df']['date_time'], sp_sch['coal_second']['df'] ['cum_evap_te']*constants.m2mm,'g+') 
ax[0].plot(sp_sch['coal_third']['df'] ['date_time'], sp_sch['coal_third']['df']  ['cum_evap_te']*constants.m2mm,'b+') 
ax[0].plot(sp_sch['coal_first']['df'] ['date_time'], sp_sch['coal_first']['df']  ['cum_evap_tas606']*constants.m2mm,'ro') 
ax[0].plot(sp_sch['coal_second']['df']['date_time'], sp_sch['coal_second']['df'] ['cum_evap_tas606']*constants.m2mm,'go') 
ax[0].plot(sp_sch['coal_third']['df'] ['date_time'], sp_sch['coal_third']['df']  ['cum_evap_tas606']*constants.m2mm,'bo') 
ax[0].plot(sp_sch['coal_second']['df']['date_time'], sp_sch['coal_second']['df'] ['cum_evap_commercial']*constants.m2mm,'ko') 
ax[0].plot(sp_sch['coal_third']['df'] ['date_time'], sp_sch['coal_third']['df']  ['cum_evap_commercial']*constants.m2mm,'ko') 
ax[0].xaxis.set_major_formatter(xfmt)

ax[1].plot(sp_sch['coal_first']['df'] ['date_time'], sp_sch['coal_first']['df']  ['evap_rate_te']*constants.ms2mmday,'r+') 
ax[1].plot(sp_sch['coal_second']['df']['date_time'], sp_sch['coal_second']['df'] ['evap_rate_te']*constants.ms2mmday,'g+') 
ax[1].plot(sp_sch['coal_third']['df'] ['date_time'], sp_sch['coal_third']['df']  ['evap_rate_te']*constants.ms2mmday,'b+') 
ax[1].plot(sp_sch['coal_first']['df'] ['date_time'], sp_sch['coal_first']['df']  ['evap_rate_tas606']*constants.ms2mmday,'ro') 
ax[1].plot(sp_sch['coal_second']['df']['date_time'], sp_sch['coal_second']['df'] ['evap_rate_tas606']*constants.ms2mmday,'go') 
ax[1].plot(sp_sch['coal_third']['df'] ['date_time'], sp_sch['coal_third']['df']  ['evap_rate_tas606']*constants.ms2mmday,'bo') 
ax[1].plot(sp_sch['coal_second']['df']['date_time'], sp_sch['coal_second']['df'] ['evap_rate_commercial']*constants.ms2mmday,'ko') 
ax[1].plot(sp_sch['coal_third']['df'] ['date_time'], sp_sch['coal_third']['df']  ['evap_rate_commercial']*constants.ms2mmday,'ko') 
ax[1].xaxis.set_major_formatter(xfmt)
plt.show(block=False)



fig, ax = plt.subplots(2,sharex=False)
ax[0].plot(sp_sch['coal_first']['df'] ['time_days'], sp_sch['coal_first']['df']  ['cum_evap_te']*constants.m2mm,'r+',markevery=2) 
ax[0].plot(sp_sch['coal_second']['df']['time_days'], sp_sch['coal_second']['df'] ['cum_evap_te']*constants.m2mm,'g+',markevery=2) 
ax[0].plot(sp_sch['coal_third']['df'] ['time_days'], sp_sch['coal_third']['df']  ['cum_evap_te']*constants.m2mm,'b+',markevery=2) 
ax[0].plot(sp_sch['coal_first']['df'] ['time_days'], sp_sch['coal_first']['df']  ['cum_evap_tas606']*constants.m2mm,'ro',markevery=2) 
ax[0].plot(sp_sch['coal_second']['df']['time_days'], sp_sch['coal_second']['df'] ['cum_evap_tas606']*constants.m2mm,'go',markevery=2) 
ax[0].plot(sp_sch['coal_third']['df'] ['time_days'], sp_sch['coal_third']['df']  ['cum_evap_tas606']*constants.m2mm,'bo',markevery=2) 
ax[0].plot(sp_sch['coal_second']['df']['time_days'], sp_sch['coal_second']['df'] ['cum_evap_commercial']*constants.m2mm,'gv',markevery=2) 
ax[0].plot(sp_sch['coal_third']['df'] ['time_days'], sp_sch['coal_third']['df']  ['cum_evap_commercial']*constants.m2mm,'bv',markevery=2) 

ax[1].plot(sp_sch['coal_first']['df'] ['time_days'], sp_sch['coal_first']['df']  ['evap_rate_te']*constants.ms2mmday,'r+',markevery=2) 
ax[1].plot(sp_sch['coal_second']['df']['time_days'], sp_sch['coal_second']['df'] ['evap_rate_te']*constants.ms2mmday,'g+',markevery=2) 
ax[1].plot(sp_sch['coal_third']['df'] ['time_days'], sp_sch['coal_third']['df']  ['evap_rate_te']*constants.ms2mmday,'b+',markevery=2) 
ax[1].plot(sp_sch['coal_first']['df'] ['time_days'], sp_sch['coal_first']['df']  ['evap_rate_tas606']*constants.ms2mmday,'ro',markevery=2) 
ax[1].plot(sp_sch['coal_second']['df']['time_days'], sp_sch['coal_second']['df'] ['evap_rate_tas606']*constants.ms2mmday,'go',markevery=2) 
ax[1].plot(sp_sch['coal_third']['df'] ['time_days'], sp_sch['coal_third']['df']  ['evap_rate_tas606']*constants.ms2mmday,'bo',markevery=2) 
ax[1].plot(sp_sch['coal_second']['df']['time_days'], sp_sch['coal_second']['df'] ['evap_rate_commercial']*constants.ms2mmday,'gv',markevery=2) 
ax[1].plot(sp_sch['coal_third']['df'] ['time_days'], sp_sch['coal_third']['df']  ['evap_rate_commercial']*constants.ms2mmday,'bv',markevery=2) 
plt.show(block=False)

#
#sensors_header=['saltrh_2_rh','suht_28e5_begin','mo_10','suht_28e5_peak','saltrh_3_rh',
#'suht_2847_end','suht_28e5_end','saltrh_3_tp','saltrh_2_tp','mo_8','mo_9','suht_2847_begin',
#'mo_7','suht_2847_peak','date_time']
##sp.surf_area1=np.pi*(0.265/2)**2
##sp.surf_area1=np.pi*(0.265/2)**2
#sp.surf_area1=np.pi*(0.21/2)**2
## get cumulative evaporation
#sp.get_derivative(key='cum_evap',deri_key='evap')
#
#
##sp.df.plot(x='date_time', y='cum_evap')
##sp.df.plot(x='date_time', y='evap')
##plt.plot(sp.df['date_time'],sp.df['evap']*constants.ms2mmday)
##plt.show(block=False)
#
## incorporate data from sensors with plotting
##sp.merge_data(df=sensors.df, keys=['T','hr','patm',
##        'rain1','rain2','rain3','wind2','wind5','R_up','R_down'] ,plot=True,coef=1e-9 )
#
#### basically this means the SmoothSpline does not like Nan at all, even the source nan has nothing to do with 
#### the splined location
##sp.merge_data(df=sensors.df, keys=['T','hr','patm',
##        'rain1','rain2','rain3','wind2','wind5','R_up','R_down'] ,plot=False,coef=1e-9 )
#sp.merge_data(df=sensors.df, keys=['sensor1','sensor2','sensor3',
#        'sensor4','sensor5','sensor6'] ,plot=False,coef=1e-9 )
#### post processing
## relative humidity
##sp.df['hr']=sp.df['hr']*0.01
#

#### ----------- obtain coefficient for te and tas------------------------------
#fig, ax = plt.subplots(2,sharex=False)
#ax[0].plot(sp.df['date_time'], (sp.df['te']-89)/0.00597   ,'r+')
#ax[0].plot(sp.df['date_time'], sp.df['commercial']        ,'gx')
#ax[0].plot(sp.df['date_time'], (sp.df['tas606']-0)/16.73  ,'bv')
#plt.show(block=False)




##############################calculate potential evaporation########################################################
###sp.df['Tk']= sp.df['T']+constants.kelvin
###sp.df['Rn']= sp.df['R_up']-sp.df['R_down']   # w/m2
###sp.df['lv']= constants.lhv(sp.df['Tk'])
###sp.df['Er']= sp.df['Rn']/sp.df['lv']/constants.rhow_pure_water  # m/s
###sp.df['rhowv_sat']= constants.svp(sp.df['Tk']) #pascal 
###sp.df['rhowv_air']= constants.svp(sp.df['Tk'])*sp.df['hr'] #pascal
###
####sp.df['B']=0.102*sp.df['wind5']/ np.log( 2/0.00000001   )**2
###sp.df['B']=0.102*sp.df['wind5']/ np.log( 2/0.0001   )**2
####sp.df['B']=6430.*(1+0.536*sp.df['wind5'])  
###sp.df['Ea']=sp.df['B']*(sp.df['rhowv_sat']-sp.df['rhowv_air'])/sp.df['lv']
###
###
####sp.df['Ea']=sp.df['B']*(constants.svp(273.15+7)-sp.df['rhowv_air'])/sp.df['lv']
###sp.df['drhowv_sat_dt']=constants.dsvp_dtk(  sp.df['Tk']   )
###
###sp.df['evap_weather']=sp.df['drhowv_sat_dt']/(sp.df['drhowv_sat_dt']+constants.psych)*sp.df['Er'
###    ] + constants.psych/(sp.df['drhowv_sat_dt']+constants.psych)*sp.df['Ea']
###
###fig=plt.figure(figsize=(20,25))
###plt.plot(sp.df['date_time'],sp.df['Ea']*constants.ms2mmday,'r-')
###plt.plot(sp.df['date_time'],sp.df['Er']*constants.ms2mmday,'g-')
###plt.plot(sp.df['date_time'],sp.df['evap_weather']*constants.ms2mmday,'b-')
###plt.plot(sp.df['date_time'],sp.df['evap']*constants.ms2mmday,'k-')
###
###
###
###fig=plt.figure(figsize=(20,25))
###plt.plot(sp.df['date_time'],sp.df['T'],'k-')
###
###fig=plt.figure(figsize=(20,25))
###plt.plot(sp.df['date_time'],sp.df['rhowv_air'],'k-')
###plt.plot(sp.df['date_time'],sp.df['rhowv_sat'],'r-')
###fig=plt.figure(figsize=(20,25))
###plt.plot(sp.df['date_time'],sp.df['wind5'],'r-')
#up_shift=0.06
#lw=2
#fs=20
#ax2=plt.subplot(511)
#for axis in ['top','bottom','left','right']:
#  ax.spines[axis].set_linewidth(0.5)

#ax2.set_position([0.08,0.73+up_shift,0.85,0.2])
#plt.plot(sp.df['date_time'],sp.df['sensor1'],'k-',linewidth=lw)
#plt.grid()
#plt.ylabel('SENSOR READING VALUE',fontsize=fs)
#
#ax3=plt.subplot(512)
#ax3.set_position([0.08,0.51+up_shift,0.85,0.2])
#plt.plot(sp.df['date_time'],sp.df['cum_evap']*1000,'k-',linewidth=lw)
#plt.grid()
#plt.ylabel('CUM. EVAP. (MM)',fontsize=fs)
#
#ax4=plt.subplot(513)
#ax4.set_position([0.08,0.29+up_shift,0.85,0.2])
#plt.plot(sp.df['date_time'],sp.df['evap']*constants.ms2mmday,'k-',linewidth=lw)
#plt.grid()
#plt.ylabel('EVAP. RATE(MM/DAY)',fontsize=fs)


#ax5=plt.subplot(514)
#ax5.set_position([0.08,0.01,0.85,0.4])
#plt.plot(sp.df['date_time'],sp.df['evap']*constants.ms2mmday,'k-',linewidth=lw)


#b=os.listdir(current_path+"/photo/")

#mg=mpimg.imread(current_path+'/photo/'+b[0])
#imgplot = plt.imshow(img)
#imgplot = plt.imshow(img)
#fig=plt.figure(figsize=(20,25))
#plt.plot(sp.df['date_time'],sp.df['B']*constants.ms2mmday,'k-')
##sp.df['B2']=0.102*sp.df['wind5']/ np.log( 2/0.001   )**2
#sp.df['B2']=0.102*sp.df['wind5']/ np.log( 2/0.005   )**2


# two issues currently for the model
#(1) we assumed a water temperature as 10 celsius
#(2) the surface temp is set as 10 celsius

#fig=figure(facecolor='white')
up_shift=0.06
lw=2
fs=20
fs_ylabel=14
date_formatter = mdates.DateFormatter('%b/%d')
#plt.figure(num=None, figsize=(800, 600), dpi=30, facecolor='w', edgecolor='k')
fig = plt.figure(figsize=(16,12))

ax2=plt.subplot(311)
for axis in ['top','bottom','left','right']:
  ax2.spines[axis].set_linewidth(1.5)
# We change the fontsize of minor ticks label 
ax2.tick_params(axis='both', which='major', labelsize=15)
ax2.tick_params(axis='both', which='minor', labelsize=10)

plt.plot(sp.df['date_time'],sp.df['sensor1'],'r-', linewidth=2.0)
plt.ylabel('SENSOR READING VALUE',fontsize=fs_ylabel, weight='bold', labelpad=10)
ax2.xaxis.set_major_formatter(date_formatter)
#plt.xlabel('TIME',fontsize=20, weight='bold')
plt.grid()

ax3=plt.subplot(312)
for axis in ['top','bottom','left','right']:
  ax3.spines[axis].set_linewidth(1.5)
ax3.tick_params(axis='both', which='major', labelsize=15)
ax3.tick_params(axis='both', which='minor', labelsize=10)
plt.plot(sp.df['date_time'],sp.df['cum_evap']*1000,'r-', linewidth=2.0)
plt.ylabel('CUM. EVAP. (MM)',fontsize=fs_ylabel, weight='bold', labelpad=18)
ax3.xaxis.set_major_formatter(date_formatter)
#plt.xlabel('TIME',fontsize=20, weight='bold')
plt.grid()

ax4=plt.subplot(313)
for axis in ['top','bottom','left','right']:
  ax4.spines[axis].set_linewidth(1.5)
ax4.tick_params(axis='both', which='major', labelsize=15)
ax4.tick_params(axis='both', which='minor', labelsize=10)
plt.plot(sp.df['date_time'],sp.df['evap']*constants.ms2mmday,'r-', linewidth=2.0)
plt.ylabel('EVAP. RATE(MM/DAY)',fontsize=fs_ylabel, weight='bold', labelpad=10)
plt.xlabel('TIME',fontsize=20, weight='bold')
ax4.xaxis.set_major_formatter(date_formatter)
plt.grid()
fig.savefig('calibration_result.png',dpi=300)



###------------------------------ find the correct correlation to get coefficient for load cells ------------------------
fig, ax = plt.subplots(2,sharex=False)
ax[0].plot(sp.df['commercial'],sp.df['te'],'r+') 
ax[1].plot(sp.df['commercial'],sp.df['tas606'],'g+') 
plt.show(block=False)
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



#http://pandas.pydata.org/pandas-docs/stable/indexing.html
##In [48]: df1 = pd.DataFrame(np.random.randn(6,4),
##   ....:                    index=list('abcdef'),
##   ....:                    columns=list('ABCD'))
##   ....: 
##
##In [49]: df1
##Out[49]: 
##          A         B         C         D
##a  0.132003 -0.827317 -0.076467 -1.187678
##b  1.130127 -1.436737 -1.413681  1.607920
##c  1.024180  0.569605  0.875906 -2.211372
##d  0.974466 -2.006747 -0.410001 -0.078638
##e  0.545952 -1.219217 -1.226825  0.769804
##f -1.281247 -0.727707 -0.121306 -0.097883
##
##In [50]: df1.loc[['a', 'b', 'd'], :]
##Out[50]: 
##          A         B         C         D
##a  0.132003 -0.827317 -0.076467 -1.187678
##b  1.130127 -1.436737 -1.413681  1.607920
##d  0.974466 -2.006747 -0.410001 -0.078638

