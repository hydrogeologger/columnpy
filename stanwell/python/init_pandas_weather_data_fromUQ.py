
#initial weather data from UQ weather station
data_weather_fromUQ_path=current_path+'/data/weather_data_fromUQ/'    # warning, all the files should be .dat


data_weather_fromUQ_header=['date_time','WindDir_Mean(deg)','WindSpd_Mean(km/h)','WindSpd_Min(km/h)','WindSpd_Max(km/h)','Temp_Mean(deg)','RH_Mean(%)','MSLP_Mean(hPa)','Rain_Acc(mm)','Rain_Intensity(mm/h)','Hail_Acc(hits/cm2)','Hail_Intensity(hits/cm2hr)','Solar_Mean(W/m2)']

data_date_time=['date_time']
# 09/03/2017 here x[:-5] only sorts out from start to -5 position
# one can check the correct by
# dateparse('2017-03-09T09:02:48.588Z')
# and see if the parsing is successful
#dateparse =  lambda x: pd.datetime.strptime(x[:-5], '%Y-%m-%dT%H:%M:%S')  # sparkfun output
# this new function is better as it provides miniseconds parsing as well. 
#dateparse =  lambda x: pd.datetime.strptime(x[:-1], '%Y-%m-%dT%H:%M:%S.%f')  # sparkfun output
dateparse =  lambda x: pd.datetime.strptime(x[:-1], '%Y-%m-%d-%H:%M:%S')

# 09/03/2017 remove the index column at the very beginning, by default, pandas will produce a column from first one.
#index_col_sw=False
index_col_sw='date_time'

data_weather_fromUQ=pandas_scale.pandas_scale(file_path=data_weather_fromUQ_path,
    source='raw',
    sep=',',
    header=1,
    names=data_weather_fromUQ_header,
    parse_dates=data_date_time,
    date_parser=dateparse,
    index_col=index_col_sw
    )


#data_weather_fromUQ.df.sort_values('date_time',inplace=True)
#data_weather_fromUQ.df = data_weather_fromUQ.df.reset_index(drop=True)

data_weather_fromUQ.df.sort_index(ascending=True,inplace=True)
#data_weather_fromUQ.df.index=data_weather_camellia.df.index+pd.to_timedelta(10, unit='h') #for the data from UQ, the time zone is UTC+10.
data_weather_fromUQ.df['date_time']= data_weather_fromUQ.df.index


#initial data of surface settlement from manual script


data_settlement_header=['date_time','settlement_mm']
data_settlement_path=current_path+'/data/manual/manual_for_merge/update/'    # warning, all the files should be .dat

data_settlement=pandas_scale.pandas_scale(file_path=data_settlement_path,
    source='raw',
    sep=',',
    header=1,
    names=data_settlement_header,
    parse_dates=data_date_time,
    date_parser=dateparse,
    index_col=index_col_sw
    ) 

data_settlement.df.sort_index(ascending=True,inplace=True)
data_settlement.df['date_time']= data_settlement.df.index

