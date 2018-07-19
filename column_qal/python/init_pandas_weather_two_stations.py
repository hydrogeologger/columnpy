

data_weather_camellia_path=current_path+'/data/public_weather_camellia/'    # warning, all the files should be .dat


data_weather_camellia_header=['et','batt','dlyrainmm','ip','ir_down','ir_up','lt','mo_soil','p','pet','rainmm','rh','rh_box_6','rh_box_7','tc',
    'temp_soil','date_time','tp_box_6','tp_box_7','uv_down','uv_up','vis_down','vis_up','wddir','wddiravg2m','wdgstdir','wdgstdir10m','wdgstkph',
    'wdgstkph10m','wdspdkph','wdspdkphavg2m']

data_date_time=['date_time']
# 09/03/2017 here x[:-5] only sorts out from start to -5 position
# one can check the correct by
# dateparse('2017-03-09T09:02:48.588Z')
# and see if the parsing is successful
#dateparse =  lambda x: pd.datetime.strptime(x[:-5], '%Y-%m-%dT%H:%M:%S')  # sparkfun output
# this new function is better as it provides miniseconds parsing as well. 
dateparse =  lambda x: pd.datetime.strptime(x[:-1], '%Y-%m-%dT%H:%M:%S.%f')  # sparkfun output

# 09/03/2017 remove the index column at the very beginning, by default, pandas will produce a column from first one.
#index_col_sw=False
index_col_sw=False

data_weather_camellia=pandas_scale.pandas_scale(file_path=data_weather_camellia_path,
    source='raw',
    sep=',',
    header=1,
    names=data_weather_camellia_header,
    parse_dates=data_date_time,
    date_parser=dateparse,
    index_col=index_col_sw
    )



data_weather_camellia.df.sort_values('date_time',inplace=True)
## https://stackoverflow.com/questions/37787698/how-to-sort-pandas-dataframe-from-one-column
## reverse the dataframe by timestamp as the result is upside down
#data.df.sort_values('timestamp',inplace=True)
#
data_weather_camellia.df = data_weather_camellia.df.reset_index(drop=True)
#
# 'date_time'  is the column with corrected time zones
data_weather_camellia.df['date_time']=data_weather_camellia.df['date_time']+pd.to_timedelta(10, unit='h')


data_weather_daisy_header=['aet','batt','dlyrainmm','ip','ir_down','ir_up','lt','mo_soil','p','pet','rainmm','rh','rh_box_6','rh_box_7','tc',
    'temp_soil','date_time','tp_box_6','tp_box_7','uv_down','uv_up','vis_down','vis_up','wddir','wddiravg2m','wdgstdir','wdgstdir10m','wdgstkph',
    'wdgstkph10m','wdspdkph','wdspdkphavg2m']


data_weather_daisy_path=current_path+'/data/public_daisy_weather/'    # warning, all the files should be .dat
data_weather_daisy=pandas_scale.pandas_scale(file_path=data_weather_daisy_path,
    source='raw',
    sep=',',
    header=1,
    names=data_weather_daisy_header,
    parse_dates=data_date_time,
    date_parser=dateparse,
    index_col=index_col_sw
    )
data_weather_daisy.df.sort_values('date_time',inplace=True)
## https://stackoverflow.com/questions/37787698/how-to-sort-pandas-dataframe-from-one-column
## reverse the dataframe by timestamp as the result is upside down
#data.df.sort_values('timestamp',inplace=True)
#
data_weather_daisy.df = data_weather_daisy.df.reset_index(drop=True)
#
# 'date_time'  is the column with corrected time zones
data_weather_daisy.df['date_time']=data_weather_daisy.df['date_time']+pd.to_timedelta(10, unit='h')
#
#
####   special treatment

data_weather_daisy.df['ir_up'][data_weather_daisy.df['ir_up']>40000]=np.nan
data_weather_daisy.df['ir_up']=(data_weather_daisy.df['ir_up']-224.0)/20.512
data_weather_daisy.df['ir_down'][data_weather_daisy.df['ir_down']>40000]=np.nan
data_weather_daisy.df['ir_down']=(data_weather_daisy.df['ir_down']-224.0)/20.512
#data_weather_daisy.df['rh']=(data_weather_daisy.df['rh']-.0)/120
#data_weather_daisy.df['wdspdkph']=(data_weather_daisy.df['wdspdkph']-.0)*16.0

##data.df['mo_0'][data.df['mo_8']>570]=np.nan
##data.df['mo0'][data.df['mo0']>400]=np.nan
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
##data.df['mo_8'][data.df['mo_8']>570]=np.nan
##data.df['t_19_end'][data.df['t_19_end']>32]=np.nan
##data.df['t_19_begin'][data.df['t_19_begin']>32]=np.nan
##data.df['t_14_begin'][data.df['t_14_begin']>32]=np.nan
##data.df['t_19_end'][data.df['t_19_end']>32]=np.nan
##data.df['t_14_end'][data.df['t_14_end']>32]=np.nan
#


time_start = np.datetime64('2018-02-13T00:00')
time_end   = np.datetime64('2018-02-14T00:00')
#https://stackoverflow.com/questions/31617845/how-to-select-rows-in-a-dataframe-between-two-values-in-python-pandas/31617974
mask=data_weather_daisy.df['date_time'].between(time_start,time_end)
data_weather_daisy.df['rainmm'][mask]=0

time_start = np.datetime64('2018-03-26T00:00')
time_end   = np.datetime64('2018-03-27T00:00')
#https://stackoverflow.com/questions/31617845/how-to-select-rows-in-a-dataframe-between-two-values-in-python-pandas/31617974
mask=data_weather_daisy.df['date_time'].between(time_start,time_end)
data_weather_daisy.df['rainmm'][mask]=data_weather_daisy.df['rainmm'][mask]*22

####    treat rain data  ##
#data_weather_daisy.df
#data_weather_daisy.df['rainmm'].values
#data_weather_daisy.df['date_time'].values
#
#
#raindata=data_weather_daisy.df['rainmm'].values
#
#dt_ns =data_weather_daisy.df['date_time'].values- np.datetime64('2017-08-16T00:00:00.000000')   #ns
#dt_day=dt_ns.astype('timedelta64[D]')
#dt_days=(dt_day/ np.timedelta64(1, 'D')).astype(int)
#
#
#for day_idx in np.arange(dt_days[0],dt_days[-1]):
#    rain_current_day=rainvalue[dt_days==day_idx]
