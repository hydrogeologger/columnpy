#execfile('python/pull_data2.py')
#----------------Preprocess data frame-------------------
execfile('python/init_pandas.py')
execfile('python/init_pandas_mo_su.py')
execfile('python/init_pandas_weather_two_stations_dl.py')
execfile('python/init_pandas_weather_data_fromUQ.py')
#----------------Data processing------------------------
execfile('python/read_schedule_update_June2019.py')
#----------------Data postprocessing---------------------
execfile('python/plot_weather.py') # Plot weather results
execfile('python/plot_qal_modify.py') # Plot results from the instrumentation
execfile('python/plot_water_balance_qal.py') # Plot the water mass balance

