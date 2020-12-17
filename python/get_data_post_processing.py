import os
import sys
import py_compile
current_path=os.getcwd()
pyduino_path = '/home/osboxes/pyduino_py3'
sys.path.append(os.path.join(pyduino_path,'python','post_processing'))
py_compile.compile(os.path.join(pyduino_path,'python','post_processing','thingsboard_to_pandas.py'))
py_compile.compile(os.path.join(pyduino_path,'python','post_processing','pandas_scale.py')  )
py_compile.compile(os.path.join(pyduino_path,'python','post_processing','constants.py')  )
py_compile.compile(pyduino_path+'/python/post_processing/constants.py')


import operator
import json
import pandas as pd
import numpy as np
import pdb
import getpass
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import thingsboard_to_pandas
import pandas_scale
import constants
#import sensorfun
#import figlib


if not os.path.exists('figure'):
        os.makedirs('figure')
if not os.path.exists('output_data'):
        os.makedirs('output_data')


tb_pandas=thingsboard_to_pandas.tingsboard_to_pandas('tb_credential.json')   # input is the location of the json file
# use the below command to show the comments on tb_credential.json
# print tb_pandas.input_json['comments'] 


tb_pandas.get_token()    # get the token associated with the account
tb_pandas.get_keys()     # list of keys in the device
tb_pandas.get_data()     # obtain data from thingsboard stored at tb_pandas['results']
tb_pandas.convert_data_to_df()  # convert each datasets to pandas dataframe

raw_moisture_list = ['mo1','mo2','mo3','mo4','mo5','mo6','mo7']

raw_suction_list = ['su_b0','su_b1','su_b2','su_b3','su_b4','su_c0','su_c1','su_c2','su_c3','su_c4',
                    'su_d0','su_d1','su_d2','su_d3','su_d4','su_e0','su_e1','su_e2','su_e3','su_e4',
                    'su_f0','su_f1','su_f2','su_f3','su_f4','su_g0','su_g1','su_g2','su_g3','su_g4',
                    'su_h0','su_h1','su_h2','su_h3','su_h4']

raw_moisture_list = ['mo1','mo2','mo3','mo4','mo6','mo7']

raw_temperature_list = ['temp_a','temp_b','temp_c','temp_d','temp_e','temp_f','temp_g','temp_h']

moisture_list = ['moisture1','moisture2','moisture3','moisture4','moisture6','moisture7']

vwc_list = ['vwc1','vwc2','vwc3','vwc4','vwc6','vwc7']

vwc_suction_list = ['suctiona0_vwc','suctionb0_vwc','suctiond0_vwc','suctione0_vwc','suctiong0_vwc','suctionh0_vwc']

suction_list = []

for i in raw_suction_list:
  suction_list.append('suction{}'.format(i[-2:]))

name_list = raw_moisture_list + raw_suction_list + raw_temperature_list 


# make the value to be nan where <1
for i in name_list:
        tb_pandas.result_df[i]['value'][tb_pandas.result_df[i]['value']<1]=np.nan

# processing the suctiond data
for i in raw_suction_list:
  if 'b' in i:
        tb_pandas.result_df[i]['value'].loc[tb_pandas.result_df[i]['value']>15]=np.nan

  elif 'd' in i:
        tb_pandas.result_df[i]['value'].loc[tb_pandas.result_df[i]['value']>15]=np.nan
    
  elif 'e' in i:
        tb_pandas.result_df[i]['value'].loc[tb_pandas.result_df[i]['value']>15]=np.nan

  elif 'f' in i:
        tb_pandas.result_df[i]['value'].loc[tb_pandas.result_df[i]['value']>15]=np.nan
    
  elif 'g' in i:
        tb_pandas.result_df[i]['value'].loc[tb_pandas.result_df[i]['value']>15]=np.nan
   
  elif 'h' in i:
        tb_pandas.result_df[i]['value'].loc[tb_pandas.result_df[i]['value']>15]=np.nan

# merge data    
with open('schedule.json') as data_file:    
    sp_input = json.load(data_file)


sp_sch={}
#plot_interpolate=True
plot_interpolate=False

sp_sch=pandas_scale.concat_data_tb(pd.to_datetime(sp_input['start_time'],format='%Y/%b/%d %H:%M'),
    pd.to_datetime(sp_input['end_time'],format='%Y/%b/%d %H:%M'),sp_input['delta_t_s'] )

sp_sch.start_dt = pd.to_datetime(sp_input['start_time'],format='%Y/%b/%d %H:%M')
sp_sch.end_dt   = pd.to_datetime(sp_input['end_time'  ],format='%Y/%b/%d %H:%M')

# merge data from tb
for i in name_list:
        sp_sch.merge_data_from_tb(
                input_time_series=tb_pandas.result_df[i].index,
                input_data_series=tb_pandas.result_df[i]['value'],
                output_time_series=sp_sch.df.index,
                key_name=i,
                rm_nan=True
        )

     
# plot the fig
'''
fig = plt.figure(figsize=(16,10))
ax = [[] for i in range(30)]
ax[0] = plt.subplot2grid((2, 1), (0, 0), colspan=1)
ax[1] = plt.subplot2grid((2, 1), (1, 0), colspan=1, sharex = ax[0])

ax[0].plot(sp_sch.df.index,sp_sch.df['temp_a'])
ax[0].plot(sp_sch.df.index,sp_sch.df['temp_b'])
ax[0].plot(sp_sch.df.index,sp_sch.df['temp_c'])
ax[0].plot(sp_sch.df.index,sp_sch.df['temp_d'])
ax[0].plot(sp_sch.df.index,sp_sch.df['temp_e'])
ax[0].plot(sp_sch.df.index,sp_sch.df['temp_f'])
ax[0].plot(sp_sch.df.index,sp_sch.df['temp_g'])
ax[0].plot(sp_sch.df.index,sp_sch.df['temp_h'])

ax[1].plot(sp_sch.df.index,sp_sch.df['mo1'])
ax[1].plot(sp_sch.df.index,sp_sch.df['mo2'])
ax[1].plot(sp_sch.df.index,sp_sch.df['mo3'])
ax[1].plot(sp_sch.df.index,sp_sch.df['mo4'])
ax[1].plot(sp_sch.df.index,sp_sch.df['mo5'])
ax[1].plot(sp_sch.df.index,sp_sch.df['mo6'])
ax[1].plot(sp_sch.df.index,sp_sch.df['mo7'])

#ax[1].plot(sp_sch.df.index,sp_sch.df['scale1'][0]-sp_sch.df['scale1'])
#ax[1].plot(sp_sch.df.index,sp_sch.df['scale2'][0]-sp_sch.df['scale2'])
'''
#plt.show()

sp_sch.df.to_csv('data/result.dat')
pd.DataFrame(sp_sch.df, columns=name_list).to_csv('data/result_raw.csv')
#pd.DataFrame(sp_sch.df, columns=name_list).to_csv('data/railway_tank_nov/result_raw.dat')
#plt.close()

#===================================================================================
#============================INITIATE===============================================
#===================================================================================

#import sys
#sys.modules[__name__].__dict__.clear()


python_file_path=current_path+'/python/'
sys.path.append(python_file_path)
# change the date time header as datetime to make life easier
#data_list_data_roof=os.listdir(current_path+'/data/data_roof/')
data_file_path=current_path+'/data/'    # warning, all the files should be .dat DO NOT FORGET THE LAST SLASH


# data_header needs to be the same as the sp_sch.df columns
data_header=['date_time','time_days'] + raw_moisture_list + raw_suction_list + raw_temperature_list

data_date_time=['date_time']

# 01/02/2018 please make sure date_time is the name for making date times
# 09/03/2017 here x[:-5] only sorts out from start to -5 position
# one can check the correct by
# dateparse('2017-03-09T09:02:48.588Z')
# and see if the parsing is successful
#dateparse =  lambda x: pd.to_datetime(x[:-5],format= '%Y-%m-%dT%H:%M:%S')  # sparkfun output
# this new function is better as it provides miniseconds parsing as well. 

#dateparse =  lambda x: pd.to_datetime(x[:-1], format='%Y-%m-%dT%H:%M:%S.%f')  # sparkfun output
dateparse =  lambda x: pd.to_datetime(x[:], format='%Y-%m-%d %H:%M:%S.%f')  # sparkfun output
#dateparse =  lambda x: pd.to_datetime(x[:-5], format='%Y-%m-%dT%H:%M.%f')  # 18/Jun/2017 23:29:03

# 09/03/2017 remove the index column at the very beginning, by default, pandas will produce a column from first one.
index_col_sw=False

data=pandas_scale.pandas_scale(file_path=data_file_path,
    source='raw',
    sep=',',
    header=1,
    names=data_header,
    parse_dates=data_date_time,
    date_parser=dateparse,
    index_col=index_col_sw
    )


#data_mo_su.df.sort_index(ascending=True,inplace=True)
data.df.sort_values('date_time',inplace=True)
## https://stackoverflow.com/questions/37787698/how-to-sort-pandas-dataframe-from-one-column
## reverse the dataframe by timestamp as the result is upside down
#data.df.sort_values('timestamp',inplace=True)
#
data.df = data.df.set_index('date_time',drop=False)
#data.df = data.df.reset_index(drop=True)
#
## 'date_time'  is the column with corrected time zones
#data.df['date_time']=data.df['date_time']+pd.to_timedelta(10, unit='h')
#data_mo_su.df.index=data_mo_su.df.index+pd.to_timedelta(10, unit='h')

# make inf data to be nan
data.df.replace([np.inf, -np.inf], np.nan, inplace=True)


#===================================================================================
#============================READSCHEDULE===========================================
#===================================================================================


dt_s=3600
sp_sch={}

plot_interpolate=False
#plot_interpolate=True
for line in open("schedule.ipt"):
    li=line.strip()
    if not li.startswith("#"):
        line_content=[x.strip() for x in li.split(',')]
        sch_name=line_content[2]
        sp_sch[sch_name]=pandas_scale.concat_data_roof(pd.to_datetime(line_content[0],format='%Y/%b/%d %H:%M'),pd.to_datetime(line_content[1],format='%Y/%b/%d %H:%M'),dt_s );
        sp_sch[sch_name].df.index=sp_sch[sch_name].df['date_time']

        sp_sch[sch_name].start_dt=pd.to_datetime(line_content[0],format='%Y/%b/%d %H:%M')
        sp_sch[sch_name].end_dt=pd.to_datetime(line_content[1],format='%Y/%b/%d %H:%M')
        
        sp_sch[sch_name].surface_area=float(line_content[4])
        sp_sch[sch_name].por=float(line_content[6])
        sp_sch[sch_name].time_surface_emerge = pd.to_datetime(line_content[10],format='%Y/%b/%d %H:%M')


        #time_start = np.datetime64('2020-09-10T08:00')
        #time_end   = np.datetime64('2020-11-10T00:00')
        ##https://stackoverflow.com/questions/31617845/how-to-select-rows-in-a-dataframe-between-two-values-in-python-pandas/31617974
        #mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
        #sp_sch[sch_name].df['tmp2'][mask]=np.random.random(len(mask))*50+710
        
        # create the dict of the coef. like 'su_b0':1e-15,'su_b1':1e-15
        coef_suction_list = [5e-15]*len(raw_suction_list)
        coef_suction_dict = dict(zip(raw_suction_list, coef_suction_list))

        # if you want change any of the coef, just change the value of the dict.
        # EXAMPLE: if i want the change the coef for su_b0 as 1e-16: 
        # coef_dict['su_b0']=1e-16
         
        # merge data using the dict
        for i in coef_suction_dict:
                sp_sch[sch_name].merge_data(
                        df=data.df,
                        keys=[i],
                        plot=plot_interpolate,
                        coef=coef_suction_dict[i]
                )

        
        # create the dict for how many values to be average to get the delta
        # same method as above, firstly assume the last 20 values will be the average max
        
        average_elements_list = [-20]*len(raw_suction_list)
        average_elements_dict = dict(zip(raw_suction_list, average_elements_list))

        aa_dict = dict(zip(raw_suction_list, [-0.5]*len(raw_suction_list))) # Degree of volatility
        bb_dict = dict(zip(raw_suction_list, [10]*len(raw_suction_list)))   # scale the values

        # if you want to change the coeff, use the example below
        #change_list = ['su_e0','su_e1','su_e2','su_e3','su_e4']
        #change_list2 = ['su_g0','su_g1','su_g2','su_g3','su_g4']
        #for i in change_list2:
        #        aa_dict[i]=-0.5
        #        bb_dict[i]=10
        #        average_elements_dict[i]=-10

        # version that only save the final value into the dataframe
        for i in average_elements_dict:
                sorted = sp_sch[sch_name].df[i].sort_values()
                max_delta_t = np.average(sorted[average_elements_dict[i]:])
                min_delta_t = np.average(sorted[0])
                norm_delta_t = -(min_delta_t-sp_sch[sch_name].df[i])/(max_delta_t-min_delta_t)
                sp_sch[sch_name].df['suction{}'.format(i[-2:])] = np.exp(-1.5*(norm_delta_t**aa_dict[i]-bb_dict[i])) 

        # version that save all values into the dataframe
        #for i in average_elements_dict:
        #        locals()['delta_t_su{}_low2_high'.format(i[-2:])]=sorted(sp_sch[sch_name].df[i],key=float)
        #        sp_sch[sch_name].df['delta_t_su{}'.format(i[-2:])]=sp_sch[sch_name].df[i]
        #        average_value_max = np.average(sorted(sp_sch[sch_name].df[i],key=float)[average_elements_dict[i]:])
        #        average_value_min = np.average(sorted(sp_sch[sch_name].df[i],key=float)[0])
        #        sp_sch[sch_name].df['norm_delta_t_su{}'.format(i[-2:])] = -(average_value_min-sp_sch[sch_name].df['delta_t_su{}'.format(i[-2:])]\
        #                )/(average_value_max-average_value_min)
	#aa=-1.1 #coef tested best
	#aa=-0.51 #coef tested best
	#bb=7 #coef tested best
	#aa1=-3 #coef tested best
	#bb1=10 #coef tested best
        # calculate the real suction value
        #for i in suction_list:
        #        sp_sch[sch_name].df['suction{}'.format(i[-2:])]=np.exp(-1.5*(sp_sch[sch_name].df['norm_delta_t_su{}'.format(i[-2:])]**aa-bb))
        #sp_sch[sch_name].df['suctionb0']=np.exp(-1.5*(sp_sch[sch_name].df['norm_delta_t_sub0']**aa1-bb))

        def cut_aberrant(df,name,dic):
        #this function is to cut the aberrant data using the datetime_index
        #df: data
        #name: the column name that you want to cut
        #dic: {'start':['','','',...],'end':['','','',...]}

                for i in range(len(dic['start'])):
                        df[name][(df.index >= dic['start'][i]) & (df.index <= dic['end'][i])]=np.nan
                        df[name].fillna(method='bfill',inplace=True)
                return None

        cut_aberrant(sp_sch[sch_name].df,'suctiond1',{'start':['2020-10-29'],
                                                        'end':['2020-11-04']})
        cut_aberrant(sp_sch[sch_name].df,'suctionb3',{'start':['2020-10-29'],
                                                        'end':['2020-11-04']})

        # merge coef (smooth the curve) for temperature
        coef_temperature_list = [5e-15]*len(raw_temperature_list)
        coef_temperature_dict = dict(zip(raw_temperature_list, coef_temperature_list))
        coef_raw_moisture_list = [5e-15]*len(raw_moisture_list)
        coef_raw_moisture_dict = dict(zip(raw_moisture_list, coef_raw_moisture_list))

        # if you want change any of the coef, just change the value of the dict.
        # coef_#_dict['xxx']=1e-1x
         
        # merge data using the coef dict
        for i in coef_temperature_dict:
                sp_sch[sch_name].merge_data(
                        df=data.df,
                        keys=[i],
                        plot=plot_interpolate,
                        coef=coef_temperature_dict[i]
                )

        for i in coef_raw_moisture_dict:
                sp_sch[sch_name].merge_data(
                        df=data.df,
                        keys=[i],
                        plot=plot_interpolate,
                        coef=coef_raw_moisture_dict[i]
                )

        # processing the moisture and vwc
        # degree of saturation
        # the numbers below are selected by the max and min value of the whole wet and dry process
        alpha_mo = -5
        porosity = 0.3
        sp_sch[sch_name].df['moisture1']=(596.0**alpha_mo-sp_sch[sch_name].df['mo1']**alpha_mo)/(596.0**alpha_mo-365**alpha_mo)
        sp_sch[sch_name].df['moisture2']=(618.0**alpha_mo-sp_sch[sch_name].df['mo2']**alpha_mo)/(618.**alpha_mo-354**alpha_mo)
        sp_sch[sch_name].df['moisture3']=(638.0**alpha_mo-sp_sch[sch_name].df['mo3']**alpha_mo)/(638.**alpha_mo-326**alpha_mo)
        sp_sch[sch_name].df['moisture4']=(645.0**alpha_mo-sp_sch[sch_name].df['mo4']**alpha_mo)/(645.**alpha_mo-351**alpha_mo)
        #sp_sch[sch_name].df['moisture5']=(610.0**alpha_mo-sp_sch[sch_name].df['mo5']**alpha_mo)/(610.**alpha_mo-377**alpha_mo)
        sp_sch[sch_name].df['moisture6']=(658.0**alpha_mo-sp_sch[sch_name].df['mo6']**alpha_mo)/(658.**alpha_mo-325**alpha_mo)
        sp_sch[sch_name].df['moisture7']=(486.0**alpha_mo-sp_sch[sch_name].df['mo7']**alpha_mo)/(486.**alpha_mo-323**alpha_mo) 

        #for i in moisture_list:
        #        sp_sch[sch_name].df[i][(sp_sch[sch_name].df[i] >= 1)]=np.nan
        #        sp_sch[sch_name].df[i][(sp_sch[sch_name].df[i] <= 0)]=np.nan
        #        #print('for {}, max = {}, min = {}, number of nan = {}'.format(i,sp_sch[sch_name].df[i].max(),sp_sch[sch_name].df[i].min(), sum(sp_sch[sch_name].df[i].isna())))

        sp_sch[sch_name].df['vwc1']=sp_sch[sch_name].df['moisture1']*porosity
        sp_sch[sch_name].df['vwc2']=sp_sch[sch_name].df['moisture2']*porosity
        sp_sch[sch_name].df['vwc3']=sp_sch[sch_name].df['moisture3']*porosity
        sp_sch[sch_name].df['vwc4']=sp_sch[sch_name].df['moisture4']*porosity
        #sp_sch[sch_name].df['vwc5']=sp_sch[sch_name].df['moisture5']*porosity
        sp_sch[sch_name].df['vwc6']=sp_sch[sch_name].df['moisture6']*porosity
        sp_sch[sch_name].df['vwc7']=sp_sch[sch_name].df['moisture7']*porosity
       
        #----calculating suction by using voumetric water content (SWCC)-------
        sp_sch[sch_name].df['suctiona0_vwc']=constants.swcc_reverse_fredlund_xing_1994(nf=0.71,mf=2.74,af=475.98,hr=4154.68,vwc=sp_sch[sch_name].df['vwc1']) #convert Pa to kPa
        #sp_sch[sch_name].df['suctionf0_vwc']=constants.swcc_reverse_fredlund_xing_1994(nf=0.71,mf=2.74,af=475.98,hr=4154.68,vwc=sp_sch[sch_name].df['vwc5']) #convert Pa to kPa
        sp_sch[sch_name].df['suctiong0_vwc']=constants.swcc_reverse_fredlund_xing_1994(nf=0.71,mf=2.74,af=475.98,hr=4154.68,vwc=sp_sch[sch_name].df['vwc6'])
        sp_sch[sch_name].df['suctione0_vwc']=constants.swcc_reverse_fredlund_xing_1994(nf=0.71,mf=2.74,af=475.98,hr=4154.68,vwc=sp_sch[sch_name].df['vwc4'])
        sp_sch[sch_name].df['suctionb0_vwc']=constants.swcc_reverse_fredlund_xing_1994(nf=0.71,mf=2.74,af=475.98,hr=4154.68,vwc=sp_sch[sch_name].df['vwc2']) #convert Pa to kPa
        sp_sch[sch_name].df['suctiond0_vwc']=constants.swcc_reverse_fredlund_xing_1994(nf=0.71,mf=2.74,af=475.98,hr=4154.68,vwc=sp_sch[sch_name].df['vwc3'])
        sp_sch[sch_name].df['suctionh0_vwc']=constants.swcc_reverse_fredlund_xing_1994(nf=0.71,mf=2.74,af=475.98,hr=4154.68,vwc=sp_sch[sch_name].df['vwc7'])
        #sp_sch[sch_name].df['su3_vwc']=constants.swcc_reverse_fredlund_xing_1994(nf=1.5,mf=0.15,af=3.8,vwc=sp_sch[sch_name].df['mmo3'])/1000
        #sp_sch[sch_name].df['su4_vwc']=constants.swcc_reverse_fredlund_xing_1994(nf=1.5,mf=0.15,af=3.8,vwc=sp_sch[sch_name].df['mmo4'])/1000
        #sp_sch[sch_name].df['su5_vwc']=constants.swcc_reverse_fredlund_xing_1994(nf=1.5,mf=0.15,af=3.8,vwc=sp_sch[sch_name].df['mmo5'])/1000
        #sp_sch[sch_name].df['su6_vwc']=constants.swcc_reverse_fredlund_xing_1994(nf=1.5,mf=0.15,af=3.8,vwc=sp_sch[sch_name].df['mmo6'])/1000
        #sp_sch[sch_name].df['su7_vwc']=constants.swcc_reverse_fredlund_xing_1994(nf=1.5,mf=0.15,af=3.8,vwc=sp_sch[sch_name].df['mmo7'])/1000


cut_list = ['suctiond0','suctionc3','suctionb3','suctionf0','suctionh1','suctione3']
# find the min value for log plot
def find_min_and_cut_before(df,name):
  for i in name:
    df[i][:np.argmin(df[i])]=np.nan

  return None

find_min_and_cut_before(sp_sch[sch_name].df,cut_list)

sp_sch[sch_name].df.to_csv('data/finalresult.csv')



import re
import os
import pandas as pd
import matplotlib
import matplotlib.image as image
import matplotlib.pylab as pylab
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


current_path=os.getcwd()
pic_path = current_path+'/finalselected/'
output_path = current_path+'/output_figure/'

list_path = os.listdir(pic_path)
pic_dict = {}
for old_name in list_path[:]:
  if old_name[-3:]=='jpg':
    old_name = os.path.join(pic_path, old_name)

    pic_idx = pd.to_datetime(''.join(re.findall(r"\d+",old_name))[:],format = ('%Y%m%d%H%M%S')).strftime('%Y-%m-%d %H:%M:%S')
    pic_dict[pic_idx]=old_name
    #print(os.listdir(output_path)[1])
#print(pic_dict)
pic_dict_keys = list(pic_dict.keys())


def pic_of_closest_date(date):
  time_diff = abs(pd.to_datetime(pic_dict_keys)-date)
  min_idx = np.asarray(np.where(time_diff==min(time_diff))).flatten()
  return pic_dict[pic_dict_keys[min_idx[0]]]


color_list = ['red','orange','maroon','gold','darkblue','olive','blue','violet']
moisture_label_list = ['5 cm (M1)','15 cm (M2)','15 cm (M3)',
              '25 cm (M4)','25 cm (M5)','35 cm (M6)','35 cm (M7)']
selected_suction_list = ['suctionb3','suctionc3','suctionf0','suctionh1']
suction_label_list = ['5 cm (S1)','15 cm (S2)','25 cm (S4)','35 cm (S5)']

vwc_suction_list = ['suctiona0_vwc','suctionb0_vwc','suctiond0_vwc','suctione0_vwc','suctiong0_vwc','suctionh0_vwc']
vwc_suction_label_list = ['5 cm (S1)','15 cm (S2)','15 cm (S3)',
              '25 cm (S4)','25 cm (S5)','35 cm (S6)']

raw_temperature_list = ['temp_a','temp_b','temp_c','temp_d','temp_e','temp_f','temp_g','temp_h']
temperature_label_list = ['5 cm (S1)','5 cm (S2)','15 cm (S3)','15 cm (S4)',
              '25 cm (S5)','25 cm (S6)','35 cm (S7)','35 cm (S8)']

moisture_color_dict = dict(zip(moisture_list,color_list))
moisture_label_dict = dict(zip(moisture_list,moisture_label_list))
suction_label_dict = dict(zip(selected_suction_list,suction_label_list))
vwc_label_dict = dict(zip(vwc_suction_list,vwc_suction_label_list))
temperature_label_dict = dict(zip(raw_temperature_list,temperature_label_list))
#sns.set_style('whitegrid')
params = {'legend.fontsize': 4,
          #'figure.figsize': (10, 5),
         'axes.labelsize': '25',
         'axes.titlesize':'20',
         'xtick.labelsize':'50',
         'ytick.labelsize':'50',
         'font.weight':'bold',
         'font.sans-serif':'Arial',
         'axes.labelweight':'bold',
         'lines.linewidth':10,}
lw=2
ms=6
mew=2
grid_width=5
y_fontsize=50
pylab.rcParams.update(params)

# how much pic you wanna choose, use the index
for date_idx,date_i in enumerate(sp_sch[sch_name].df.index[:2]):
  grid = plt.GridSpec(4, 2, wspace=0.3, hspace=0.1)
  fig = plt.figure(figsize=(90, 40)) #120,60
  ax_0 = fig.add_subplot(grid[2:3, 0:1])
  ax_1 = fig.add_subplot(grid[2:3, 1:2], sharex=ax_0)
  ax_2 = fig.add_subplot(grid[3:4, 0:1], sharex=ax_0)
  ax_3 = fig.add_subplot(grid[3:4, 1:2], sharex=ax_0)
  ax_4 = fig.add_subplot(grid[0:2, 0:2])

  
  I = plt.imread(pic_of_closest_date(date_i))
  #pic_of_closest_date(sp_sch[sch_name].df.index[100])
  #print(pic_of_closest_date(date_i))
  ax_4.imshow(I)

  #plt.xlim(sp_sch[sch_name].df.index[0], sp_sch[sch_name].df.index[-1])
  #plt.xticks(rotation=45)

  for idx,i in enumerate(moisture_list):
    ax_0.plot(
        sp_sch[sch_name].df.index,
        sp_sch[sch_name].df[i],
        '-',
        color = color_list[idx],
        markersize = ms,
        markeredgewidth = mew,
        fillstyle = 'full',
        label = moisture_label_dict[i]
    )

  for idx, i in enumerate(selected_suction_list):
    ax_1.semilogy(
        sp_sch[sch_name].df.index,
        sp_sch[sch_name].df[i],
        '-',
        color = color_list[idx],
        markeredgewidth = mew,
        fillstyle = 'full',
        label = suction_label_dict[i]    
    )

  for idx,i in enumerate(vwc_suction_list):
    ax_2.semilogy(
        sp_sch[sch_name].df.index,
        sp_sch[sch_name].df[i],
        '-',
        color = color_list[idx],
        markeredgewidth = mew,
        fillstyle = 'full',
        label = vwc_label_dict[i]   
    )  

  for idx,i in enumerate(raw_temperature_list):
    ax_3.plot(
        sp_sch[sch_name].df.index,
        sp_sch[sch_name].df[i],
        '-',
        color = color_list[idx],
        markeredgewidth = mew,
        fillstyle = 'full',
        label = temperature_label_dict[i]   
    )

  #for old_name in list_path[]:
    #old_name = os.path.join(src_path, old_name)
    #print('old_name:', old_name)
    #new_name = src_path + '/' + ''.join(i for i in re.findall(r"\d+",old_name))[:11] +'.jpg'
    #I = plt.imread(pic_dict[pic_idx])
    #ax_4.imshow(I)



  ax_0.set_ylabel('DEG. OF SAT.', fontsize=y_fontsize, labelpad=20)
  ax_0.grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
  ax_0.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m'))
  ax_0.set_ylim([0,1])
  ax_0.set_xlim([sp_sch[sch_name].df.index[0],sp_sch[sch_name].df.index[-1]])
  ax_0.legend(bbox_to_anchor=(1, 0.5 ),
              loc='center left', borderaxespad=0.,
              fontsize=40,handletextpad=0.03,
              labelspacing=0.02,ncol=1,columnspacing=0.4)
  ax_0.set_title('(A)',x=0.02,y=0.05, fontsize=50)

  ax_1.grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
  ax_1.set_ylabel('SUCTION (kPa)\nIN EMBANKMENT', fontsize=y_fontsize, labelpad=20)
  ax_1.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m'))
  ax_1.set_ylim([10,10e5])
  ax_1.legend(bbox_to_anchor=(1.01, 0.5 ), 
              loc='center left', borderaxespad=0.,
              fontsize=40,handletextpad=0.03,
              labelspacing=0.02,ncol=1,columnspacing=0.4)
  ax_1.set_title('(B)',x=0.02,y=0.9,fontsize=50)

  ax_2.grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
  ax_2.set_ylabel('SUCTION (kPa)\nIN SUBGRADE', fontsize=y_fontsize, labelpad=20)
  ax_2.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m'))
  ax_2.set_xlabel('DATE', fontsize=y_fontsize,labelpad=3)
  ax_2.set_ylim([0,3e4])
  ax_2.legend(bbox_to_anchor=(0.94, 0.5),
              loc='center left', borderaxespad=3.,
              fontsize=40,handletextpad=0.03,
              labelspacing=0.02,ncol=1,columnspacing=0.4)
  ax_2.set_title('(C)',x=0.02,y=0.9,fontsize=50)

  ax_3.grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
  ax_3.set_ylabel('TEMPERATURE\n($^\circ$C)', fontsize=y_fontsize, labelpad=20)
  ax_3.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m'))
  ax_3.set_xlabel('DATE', fontsize=y_fontsize,labelpad=3)
  ax_3.set_ylim([20,40])
  ax_3.legend(bbox_to_anchor=(1.01, 0.5), loc='center left', 
              borderaxespad=0.,fontsize=40,
              handletextpad=0.03,labelspacing=0.02,
              ncol=1,columnspacing=0.4)
  ax_3.set_title('(D)',x=0.02,y=0.9,fontsize=50)

  ax_0.axvline(date_i,color="red")
  ax_1.axvline(date_i,color="red")
  ax_2.axvline(date_i,color="red")
  ax_3.axvline(date_i,color="red")

  ax_4.axis('off')

  plt.savefig(output_path+'{}.jpg'.format(date_i))
  #plt.clf()
  #plt.tight_layout()
  #plt.show()

  plt.close('all')
  #plt.close(fig)
  