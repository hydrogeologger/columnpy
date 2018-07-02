

#data_weather_camellia_path=current_path+'/data_weather_camellia/'    # warning, all the files should be .dat


data_weather_camellia_header=['et','batt','dlyrainmm','ip','ir_down','ir_up','lt','mo_soil','p','pet','rainmm','rh','rh_box_6','rh_box_7','tc',
    'temp_soil','date_time','tp_box_6','tp_box_7','uv_down','uv_up','vis_down','vis_up','wddir','wddiravg2m','wdgstdir','wdgstdir10m','wdgstkph',
    'wdgstkph10m','wdspdkph','wdspdkphavg2m']

data_date_time=['date_time']
# 09/03/2017 here x[:-5] only sorts out from start to -5 position
# one can check the correct by
# dateparse('2017-03-09T09:02:48.588Z')
# this new function is better as it provides miniseconds parsing as well. 
dateparse =  lambda x: pd.datetime.strptime(x[:-1], '%Y-%m-%dT%H:%M:%S.%f')  # sparkfun output

# 09/03/2017 remove the index column at the very beginning, by default, pandas will produce a column from first one.
#index_col_sw=False
#index_col_sw=False
index_col_sw='date_time'
#data_weather_camellia=pandas_scale.pandas_scale(file_path=data_weather_camellia_path,
data_weather_camellia=pandas_scale.pandas_scale(file_path=camellia_weather.file_dir,
    source='raw',
    sep=',',
    header=1,
    names=data_weather_camellia_header,
    parse_dates=data_date_time,
    date_parser=dateparse,
    index_col=index_col_sw
    )



data_weather_camellia.df.sort_index(ascending=True,inplace=True)
data_weather_camellia.df['date_time']=data.df['date_time']+pd.to_timedelta(10, unit='h')

data_weather_daisy_header=['aet','batt','dlyrainmm','ip','ir_down','ir_up','lt','mo_soil','p','pet','rainmm','rh','rh_box_6','rh_box_7','tc',
    'temp_soil','date_time','tp_box_6','tp_box_7','uv_down','uv_up','vis_down','vis_up','wddir','wddiravg2m','wdgstdir','wdgstdir10m','wdgstkph',
    'wdgstkph10m','wdspdkph','wdspdkphavg2m']


#data_weather_daisy_path=current_path+'/data_weather_daisy/'    # warning, all the files should be .dat
#data_weather_daisy=pandas_scale.pandas_scale(file_path=data_weather_daisy_path,
data_weather_daisy=pandas_scale.pandas_scale(file_path=daisy_weather.file_dir,
    source='raw',
    sep=',',
    header=1,
    names=data_weather_daisy_header,
    parse_dates=data_date_time,
    date_parser=dateparse,
    index_col=index_col_sw
    )


data_weather_daisy.df.sort_index(ascending=True,inplace=True)
#data_weather_daisy.df.sort_values('date_time',inplace=True)
### https://stackoverflow.com/questions/37787698/how-to-sort-pandas-dataframe-from-one-column
### reverse the dataframe by timestamp as the result is upside down
##data.df.sort_values('timestamp',inplace=True)
##
#data_weather_daisy.df = data.df.reset_index(drop=True)
##
### 'date_time'  is the column with corrected time zones
# put this to 11 hours as rain resets around 00:30
data_weather_daisy.df['date_time']=data.df['date_time']+pd.to_timedelta(10, unit='h')


data_weather_daisy_daily=data_weather_daisy.df.between_time('22:30','22:59')
data_weather_daisy_daily.index=data_weather_daisy_daily.index.date

#data_weather_daisy_daily.plot.bar(y='dlyrainmm')
ax1=plt.figure()
plt.bar(data_weather_daisy_daily.index,data_weather_daisy_daily['dlyrainmm'])


data_weather_camellia_daily=data_weather_camellia.df.between_time('22:30','22:59')
data_weather_camellia_daily.index=data_weather_camellia_daily.index.date

#data_weather_daisy_daily.plot.bar(y='dlyrainmm')
ax2=plt.figure()
plt.bar(data_weather_camellia_daily.index,data_weather_camellia_daily['dlyrainmm'])
#
#
##data.save_as_csv (fn='data_merged.csv')
##data.save_as_hdf5(fn='data_merged.hd5')
#
#
####   special treatment
data_weather_daisy.df['ir_up'][data_weather_daisy.df['ir_up']>40000]=np.nan
data_weather_daisy.df['ir_up']=(data_weather_daisy.df['ir_up']-224.0)/20.512
data_weather_daisy.df['ir_down'][data_weather_daisy.df['ir_down']>40000]=np.nan
data_weather_daisy.df['ir_down']=(data_weather_daisy.df['ir_down']-224.0)/20.512
data_weather_daisy.df['rh']=(data_weather_daisy.df['rh']-.0)/120
data_weather_daisy.df['wdspdkph']=(data_weather_daisy.df['wdspdkph']-.0)*16.0




