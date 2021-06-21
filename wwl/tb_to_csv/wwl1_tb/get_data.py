import py_compile
import os
import sys
import json
import pandas as pd
import numpy as np
import csv
import matplotlib
matplotlib.use('Agg')
import os
import glob
import time

import matplotlib.pyplot as plt
plt.ioff()  # disable poping out figure automatically
# recompile post_processing in case update are required
pyduino_path = os.environ['pyduino']
print(os.environ['pyduino'])
sys.path.append(os.path.join(pyduino_path,'python','post_processing'))
py_compile.compile(os.path.join(pyduino_path,'python','post_processing','thingsboard_to_pandas.py'))
import thingsboard_to_pandas
reload(thingsboard_to_pandas)


tb_pandas=thingsboard_to_pandas.tingsboard_to_pandas('tb_credential.json')   # input is the location of the json file
# use the below command to show the comments on tb_credential.json

tb_pandas.get_token()    # get the token associated with the account
tb_pandas.get_keys()     # list of keys in the device
tb_pandas.get_data()     # obtain data from thingsboard stored at tb_pandas['results']
tb_pandas.convert_data_to_df()  # convert each datasets to pandas dataframe
#tb_pandas.result_df is the dictionary that contains the dataframe


for i in tb_pandas.result_df.keys():
    tb_pandas.result_df[i]=tb_pandas.result_df[i].rename(columns={'value':str(i)})
    tb_pandas.result_df[i].to_csv(i+'.csv')

result = pd.read_csv('cstemp_a.csv')

for i in tb_pandas.result_df.keys():
    print(i)
    result = pd.concat([result, pd.read_csv(i+'.csv')[str(i)]],axis=1)

result.to_csv('wwl1_rawdata.csv')
#This csv file contains all the raw data uploaded to Thingsboard without any interpolation

#-------------------Remove all CSV files named with keys but keep the final combined one----------------------
current_path=os.getcwd()
file_path = current_path+'/wwl1_rawdata.csv'
while not os.path.exists(file_path):
    time.sleep(2)

if os.path.isfile(file_path):
    #Verifies CSV file was created, then deletes unneeded files.
    for Cleanup in glob.glob(current_path+'/*.csv*'):
        print (Cleanup, 'would be deleted')
        if not Cleanup.endswith('wwl1_rawdata.csv'):
            os.remove(Cleanup)
