# this script aoutmatically pull data from sparkfun

import sys
import os
import py_compile
sys.path.append   (os.environ['pyduino']+'/python/post_processing')
py_compile.compile(os.environ['pyduino']+'/python/post_processing/phant_downloader.py')
import phant_downloader
reload(phant_downloader)
import csv_tools
#import urllib
import urllib2

sw_download=False


current_path=os.getcwd()
nectar_addr=csv_tools.get_one_line(current_path+'/credential/nectar_address')
#
folder_name_camellia_sensor='camellia_sensor'
public_camellia_prototype_sensor=csv_tools.get_one_line(current_path+'/credential/public_' +folder_name_camellia_sensor)
camellia_sensor=phant_downloader.phant_downloader(web_addr=nectar_addr+"/output/"+public_camellia_prototype_sensor, file_path_abs="data/"+ folder_name_camellia_sensor+ "/"+folder_name_camellia_sensor+".dat",download=sw_download)

folder_name_weather_camellia='weather_camellia'
public_weather_camellia=csv_tools.get_one_line(current_path+'/credential/public_weather_camellia')
camellia_weather=phant_downloader.phant_downloader(web_addr=nectar_addr+"/output/"+public_weather_camellia, file_path_abs="data/"+ folder_name_weather_camellia+ "/"+folder_name_weather_camellia+".dat",download=sw_download)

folder_name_daisy_weather='weather_daisy'
public_daisy_weather=csv_tools.get_one_line(current_path+'/credential/public_daisy_weather')
path_daisy_weather="data/"+ folder_name_daisy_weather+ "/"
daisy_weather=phant_downloader.phant_downloader(web_addr=nectar_addr+"/output/"+public_daisy_weather, file_path_abs=path_daisy_weather+folder_name_daisy_weather+".dat",download=sw_download)







