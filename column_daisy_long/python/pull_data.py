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
folder_name_daisy_sensor='daisy_prototype_sensor'
public_daisy_prototype_sensor=csv_tools.get_one_line(current_path+'/credential/public_' +folder_name_daisy_sensor)
daisy_sensor=phant_downloader.phant_downloader(web_addr=nectar_addr+"/output/"+public_daisy_prototype_sensor, file_path_abs="data/"+ folder_name_daisy_sensor+ "/"+folder_name_daisy_sensor+".dat",download=sw_download)

folder_name_weather_camellia='weather_camellia'
public_weather_camellia=csv_tools.get_one_line(current_path+'/credential/public_weather_camellia')
camellia_weather=phant_downloader.phant_downloader(web_addr=nectar_addr+"/output/"+public_weather_camellia, file_path_abs="data/"+ folder_name_weather_camellia+ "/"+folder_name_weather_camellia+".dat",download=sw_download)

folder_name_daisy_weather='weather_daisy'
public_daisy_weather=csv_tools.get_one_line(current_path+'/credential/public_daisy_weather')
path_daisy_weather="data/"+ folder_name_daisy_weather+ "/"
daisy_weather=phant_downloader.phant_downloader(web_addr=nectar_addr+"/output/"+public_daisy_weather, file_path_abs=path_daisy_weather+folder_name_daisy_weather+".dat",download=sw_download)
# the below method sucks as it produces a line with "^M" every block, searth from vimdiff
#TO 20180625
#retriver = urllib.URLopener()

## it is funny that the header has two lines for the new downloaded files
#
#a=retriver.retrieve(nectar_addr+"/output/"+public_daisy_prototype_sensor  ,     "data/"+ folder_name+ "/"+folder_name+".dat")
#
#a=retriver.retrieve(nectar_addr+"/output/"+public_qal_sali_gs3_p      , "data/qal_sali_gs3_p/"+public_qal_sali_gs3_p+".dat")
#c=retriver.retrieve(nectar_addr+"/output/"+public_daisy_weather, "data/daisy_weather_nectar/"+public_daisy_weather+".dat")
#d=retriver.retrieve(nectar_addr+"/output/"+public_weather_camellia, "data/weather_camellia_on_the_roof/"+public_weather_camellia+".dat")


#below is a better solution for larger files







