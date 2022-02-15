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




writer = pd.ExcelWriter('wwl1_rawdata_2.xlsx', engine='xlsxwriter') #If there is no module named "xlsxwriter", just sudo pip install xlsxwriter.
j=0
k=0
for i in tb_pandas.result_df.keys():
    j+=1
    if len(tb_pandas.result_df[i])>100:
        k+=1
        tb_pandas.result_df[i]=tb_pandas.result_df[i].rename(columns={'value':str(i)})
        tb_pandas.result_df[i].to_excel(writer, sheet_name = i) #Put all keys and values into different sheets in one Excel file.
        worksheet = writer.sheets[i]
        worksheet.set_column('A:A', 25) #Set the width of the first column
        workbook = writer.book
        chart = workbook.add_chart({'type': 'scatter'})
        chart.add_series({
            'name':       [i, 0, 1],
            'categories': [i, 1, 0, 1950, 0],
            'values':     [i, 1, 1, 1950, 1],
            'marker':     {'type': 'circle', 'size': 2},
        })

        chart.set_title({
            'name': i,
        })

        chart.set_x_axis({
            'name': 'Date_time',
            'name_font': {
                'name': 'Century',
                'color': 'black',
            },
            'num_format': 'dd/mm/yyyy',
            'num_font': {
                #'size': '5',
                'bold': True,
                'rotation':-45,
            },
            
        })
        
        chart.set_y_axis({
           'min': 0,
            'num_font': {
                'bold': True,
               'italic': False,
            },
           
        })
        chart.set_legend({'font': {'bold':1, 'italic':1}})     
        worksheet.insert_chart('D2', chart)
        
        #'name': ['sheetname', row, column],
        #'categories': ['sheetname', row1, column1, row2, column2],
        #'values': ['sheetname', row1, column1, row2, column2],
        
        #chart1 = worksheet.insert_chart({'type': 'scatter'}) 
        #name_string  =  '= ' + i+'!$B$1'
        #category_string  =  '= ' + i+'!$A$2:$A$1000'
        #value_string = '= ' + i+'!$B$2:$B$1000' 
        #chart1.add_series({ 
        #   'name':       name_string, 
        #   'categories': category_string, 
        #   'values':     value_string, 
        #}) 
       
    print ( i + '  ' +str(j) +'/ '+ str(k)+ '/' + str( len(tb_pandas.result_df.keys())) )

writer.save()


#------Reference: https://pandas-xlsxwriter-charts.readthedocs.io/chart_scatter.html#chart-scatter
#                 https://xlsxwriter.readthedocs.io/working_with_charts.html#chart-fonts




#for i in tb_pandas.result_df.keys():
#    tb_pandas.result_df[i]=tb_pandas.result_df[i].rename(columns={'value':str(i)})
#    tb_pandas.result_df[i].to_csv(i+'.csv')
#
#current_path=os.getcwd()
#
#all_files = glob.glob(os.path.join(current_path,"*.csv"))
#
#writer = pd.ExcelWriter('wwl1_rawdata.xlsx', engine='xlsxwriter') #If there is no module named "xlsxwriter", just sudo pip install xlsxwriter.
#
#for f in all_files:
#    df = pd.read_csv(f)
#    base = os.path.basename(f)
#    df.to_excel(writer, sheet_name = os.path.splitext(base)[0]) #Put all keys and values into different sheets in one Excel file.
#
#writer.save()
#
#
##result = pd.read_csv('cstemp_a.csv')
##
##for i in tb_pandas.result_df.keys():
##    print(i)
##    result = pd.concat([result, pd.read_csv(i+'.csv')[str(i)]],axis=1)
##
##result.to_csv('wwl1_rawdata.csv')
##This csv file contains all the raw data uploaded to Thingsboard without any interpolation
#
##-------------------Remove all CSV files named with keys but keep the final combined one----------------------
#file_path = current_path+'/wwl1_rawdata.xlsx'
#while not os.path.exists(file_path):
#    time.sleep(2)
#
#if os.path.isfile(file_path):
#    #Verifies CSV file was created, then deletes unneeded files.
#    for Cleanup in glob.glob(current_path+'/*.csv*'):
#        print (Cleanup, 'would be deleted')
#        if not Cleanup.endswith('wwl1_rawdata.xlsx'):
#            os.remove(Cleanup)
