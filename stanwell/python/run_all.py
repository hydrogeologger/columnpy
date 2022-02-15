#-------Preprocess data frame-----------------------------
execfile('python/init_pandas.py')
execfile('python/init_pandas_mo_su.py')
execfile('python/init_pandas_mo_su_thingsboard.py')
execfile('python/init_pandas_weather_two_stations_dl.py')
execfile('python/init_pandas_weather_data_fromUQ.py')
#-------Data processing----------------------------------
execfile('python/read_schedule.py')
#-------Data postprocessing------------------------------
execfile('python/plot_weather.py') # plot weather results
execfile('python/plot_stanwell.py')  # plot results from the instrumentation
execfile('python/plot_coef_moisture_balance.py') #plot the water mass balance
#execfile('plot_stanwell_video.py')  # producing video from photo and data. the photo path is also hardcoded in this script!!!!

