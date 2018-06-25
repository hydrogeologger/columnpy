# this script aoutmatically pull data from sparkfun

import sys
import os
sys.path.append   (os.environ['pyduino']+'/python/')
import csv_tools
import urllib



current_path=os.getcwd()
nectar_addr=csv_tools.get_one_line(current_path+'/credential/nectar_address')
public_qal_sali_gs3_p=csv_tools.get_one_line(current_path+'/credential/public_qal_sali_gs3_p')
public_qal_moisture_suction=csv_tools.get_one_line(current_path+'/credential/public_qal_moisture_suction')
public_weather_camellia=csv_tools.get_one_line(current_path+'/credential/public_weather_camellia')
public_daisy_weather=csv_tools.get_one_line(current_path+'/credential/public_daisy_weather')
retriver = urllib.URLopener()
# it is funny that the header has two lines for the new downloaded files
a=retriver.retrieve(nectar_addr+"/output/"+public_qal_sali_gs3_p      , "data/qal_sali_gs3_p/"+public_qal_sali_gs3_p+".dat")
b=retriver.retrieve(nectar_addr+"/output/"+public_qal_moisture_suction, "data/qal_moisture_suction/"+public_qal_moisture_suction+".dat")
c=retriver.retrieve(nectar_addr+"/output/"+public_daisy_weather, "data/daisy_weather_nectar/"+public_daisy_weather+".dat")
d=retriver.retrieve(nectar_addr+"/output/"+public_weather_camellia, "data/weather_camellia_on_the_roof/"+public_weather_camellia+".dat")

