# this script aoutmatically pull data from sparkfun

import sys
import os,glob
import py_compile
sys.path.append   (os.environ['pyduino']+'/python/post_processing')
py_compile.compile(os.environ['pyduino']+'/python/post_processing/phant_downloader.py')
import phant_downloader
reload(phant_downloader)
import csv_tools
#import urllib
import urllib2
from time import sleep


#sw_download=False
sw_download=True


current_path=os.getcwd()
nectar_addr=csv_tools.get_one_line(current_path+'/credential/nectar_address')


paths_profile = filter(os.path.isfile, glob.glob(current_path+'/credential/profiles/' + "*"))

# create profile with all data listed
prof={}
for i in paths_profile:
    name_profile=i.split('/')[-1]
    prof[name_profile]={}
    prof[name_profile]['credential_path']=i
    prof[name_profile]['public_keys']=csv_tools.get_one_line(i)
    prof[name_profile]['web_link']=nectar_addr+"/output/"+prof[name_profile]['public_keys']
    prof[name_profile]['file_path_abs']=current_path+"/data/"+name_profile+"/"
    prof[name_profile]['file_addr_abs']=current_path+"/data/"+name_profile+"/"+name_profile+".dat"


# download data
for i in prof:
    if not os.path.exists(prof[i]['file_path_abs']):
        os.makedirs(prof[i]['file_path_abs'])
    downloader=phant_downloader.phant_downloader(web_addr=prof[i]['web_link'],file_path_abs=prof[i]['file_addr_abs'],download=sw_download)
    sleep(1)


