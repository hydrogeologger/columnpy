# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 15:32:28 2021

@author: s4680073
"""
import datetime
import datetime
import numpy as np
import scipy as sp
import scipy.fftpack
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
plt.figure()
deltatime.total_seconds()
plt.plot(tb_pandas.result_df['p3_cs451'].index,tb_pandas.result_df['t3_cs451'].value,'r-')
plt.plot(tb_pandas.result_df['sa2_uv'].index,tb_pandas.result_df['sa2_uv']['value']/1000,'k-')
plt.plot(tb_pandas.result_df['p2_cs451'].index,tb_pandas.result_df['p2_cs451']['value'],'k-')
plt.plot(tb_pandas.result_df['p2_cs451'].index,tb_pandas.result_df['pond_falling_rate_cs451_2_mmPday'])
plt.plot(df2.index,df2['pond_falling_rate_cs451_2_mmPday_array'])
plt.plot(sp_sch.df.index,sp_sch.df['pond_falling_rate_cs451_3_mmPday_array'])

plt.plot( sp_sch.df.index, sp_sch.df['pet_mmPday'],'--',linewidth=0.7,label='pet')

plt.plot( sp_sch.df.index, sp_sch.df['pet_mmPday'],'--',linewidth=0.7,label='pet')
plt.plot(tb_pandas.result_df['sa1_sht31_temp_1'].index,tb_pandas.result_df['sa1_sht31_temp_1'].value,'m-')       
plt.plot(tb_pandas.result_df['sa2_temp1'].index,tb_pandas.result_df['sa2_temp1'].value,'g-')
plt.plot(tb_pandas.result_df['sa2_temp2'].index,tb_pandas.result_df['sa2_temp2'].value,'b-')
plt.plot(tb_pandas.result_df['sa2_t_5803'].index,tb_pandas.result_df['sa2_t_5803'].value,'c-')

plt.show()
sp_sch.merge_data_from_tb(
        input_time_series=tb_pandas.result_df['p2_cs451'].index, 
        input_data_series=tb_pandas.result_df['p2_cs451']['value'], 
        output_time_series=sp_sch.df.index,key_name='p2_cs451' ,
        plot=plot_interpolate ,coef=coef_2*100,rm_nan=True)
# plt.plot( sp_sch.df.index, sp_sch.df['p2_cs451'],linewidth=0.7,label='pet')
# plt.plot(tb_pandas.result_df['p2_cs451'].index,tb_pandas.result_df['p2_cs451']['value'],'k-')
# sp_sch.df['pond_falling_rate_cs451_2_mmPday']= \
#     np.append(np.diff(sp_sch.df['p2_cs451'] ),np.nan) \
#     /sp_input['delta_t_s']*constants.msPmmday
plt.plot(sp_sch.df['pond_falling_rate_cs451_2_mmPday_array'].index,sp_sch.df['pond_falling_rate_cs451_2_mmPday_array'],'k-')


zz=np.diff(tb_pandas.result_df['p2_cs451']['value'])
plt.plot(zz.index,zz)

zz=np.diff(tb_pandas.result_df['p2_cs451']['value'])
tb_pandas.result_df['pond_falling_rate_cs451_2_mmPday']= \
    np.append(np.diff(tb_pandas.result_df['p2_cs451']['value']),np.nan) 
plt.plot(tb_pandas.result_df['p2_cs451'].index,tb_pandas.result_df['pond_falling_rate_cs451_2_mmPday'])
deltatime=(tb_pandas.result_df['p2_cs451'].index[1]-tb_pandas.result_df['p2_cs451'].index[0])
pond_falling_rate_cs451_2_mmPday_array=np.zeros(tb_pandas.result_df['p2_cs451'].size)
for i in range(1,tb_pandas.result_df['p2_cs451'].size):
    diff_t=(tb_pandas.result_df['p2_cs451'].index[i]-tb_pandas.result_df['p2_cs451'].index[i-1])
    diff_t=diff_t.total_seconds()
    diff_pond_level=tb_pandas.result_df['p2_cs451']['value'][i]-tb_pandas.result_df['p2_cs451']['value'][i-1]
    pond_falling_rate_cs451_2_mmPday_array[i]=86400*(diff_pond_level/diff_t)*1000
    print(diff_t)
pond_falling_rate_cs451_2_mmPday_array[np.isnan(pond_falling_rate_cs451_2_mmPday_array)]=0
pond_falling_rate_cs451_2_mmPday_array[np.abs(pond_falling_rate_cs451_2_mmPday_array)>1000]=0
pond_fft=scipy.fft.fft(pond_falling_rate_cs451_2_mmPday_array)
pond_fft_f=abs(pond_fft)
pond_fft_f1=abs(pond_fft)/((len(pond_falling_rate_cs451_2_mmPday_array)/2))   
pond_fft_f2=pond_fft_f1[range(int(len(pond_falling_rate_cs451_2_mmPday_array)/2))]
plt.plot(pond_fft_f2)
test_pond=pond_fft
for i in range(len(pond_fft)):
    if i <=4950 and i>=50:#filter used for 
        test_pond[i]=0
test = scipy.fft.ifft(test_pond)
plt.plot(test)
pond_falling_rate_cs451_2_mmPday_array={'pond_falling_rate_cs451_2_mmPday_array':test}    
df2 = pd.DataFrame(data=pond_falling_rate_cs451_2_mmPday_array,index=tb_pandas.result_df['p2_cs451'].index)
df2.index=tb_pandas.result_df['p2_cs451'].index
# mask = np.where(df2['pond_falling_rate_cs451_2_mmPday_array']>0)[0]
# df2['pond_falling_rate_cs451_2_mmPday_array'][mask]=np.nan 
# mask = np.where(np.abs(df2['pond_falling_rate_cs451_2_mmPday_array'])>1000)[0]
# df2['pond_falling_rate_cs451_2_mmPday_array'][mask]=np.nan 
sp_sch.merge_data_from_tb(
        input_time_series=df2.index, 
        input_data_series=df2['pond_falling_rate_cs451_2_mmPday_array'], 
        output_time_series=sp_sch.df.index,key_name='pond_falling_rate_cs451_2_mmPday_array' ,
        plot=plot_interpolate ,coef=1e-8,rm_nan=True)
plt.plot(df2)


pond_falling_rate_cs451_3_mmPday_array=np.zeros(tb_pandas.result_df['p3_cs451'].size)
for i in range(1,tb_pandas.result_df['p3_cs451'].size):
    diff_t=(tb_pandas.result_df['p3_cs451'].index[i]-tb_pandas.result_df['p3_cs451'].index[i-1])
    diff_t=diff_t.total_seconds()
    diff_pond_level=tb_pandas.result_df['p3_cs451']['value'][i]-tb_pandas.result_df['p3_cs451']['value'][i-1]
    pond_falling_rate_cs451_3_mmPday_array[i]=86400*(diff_pond_level/diff_t)*1000
    print(diff_t)
pond_falling_rate_cs451_3_mmPday_array[np.isnan(pond_falling_rate_cs451_3_mmPday_array)]=0
pond_falling_rate_cs451_3_mmPday_array[np.abs(pond_falling_rate_cs451_3_mmPday_array)>1000]=0
pond_fft=scipy.fft.fft(pond_falling_rate_cs451_3_mmPday_array)
pond_fft_f=abs(pond_fft)
pond_fft_f1=abs(pond_fft)/((len(pond_falling_rate_cs451_3_mmPday_array)/2))   
pond_fft_f2=pond_fft_f1[range(int(len(pond_falling_rate_cs451_3_mmPday_array)/2))]
plt.plot(pond_fft_f2)
test_pond=scipy.fft.fft(pond_falling_rate_cs451_3_mmPday_array)
for i in range(len(test_pond)):
    if i >=20 and i<=4945:#filter used for 
        test_pond[i]=0
test = scipy.fft.ifft(test_pond)
plt.plot(test)
pond_falling_rate_cs451_3_mmPday_array={'pond_falling_rate_cs451_3_mmPday_array':test}    
df3 = pd.DataFrame(data=pond_falling_rate_cs451_3_mmPday_array,index=tb_pandas.result_df['p3_cs451'].index)
df3.index=tb_pandas.result_df['p3_cs451'].index
# mask = np.where(df2['pond_falling_rate_cs451_2_mmPday_array']>0)[0]
# df2['pond_falling_rate_cs451_2_mmPday_array'][mask]=np.nan 
# mask = np.where(np.abs(df2['pond_falling_rate_cs451_2_mmPday_array'])>1000)[0]
# df2['pond_falling_rate_cs451_2_mmPday_array'][mask]=np.nan 
sp_sch.merge_data_from_tb(
        input_time_series=df3.index, 
        input_data_series=df3['pond_falling_rate_cs451_3_mmPday_array'], 
        output_time_series=sp_sch.df.index,key_name='pond_falling_rate_cs451_3_mmPday_array' ,
        plot=plot_interpolate ,coef=1e-9,rm_nan=True)
plt.plot(df3)


mask = np.where(df2.pond_falling_rate_cs451_2_mmPday_array)==np.nan)[0]
pond_falling_rate_cs451_2_mmPday_array[mask]=0
pond_falling_rate_cs451_2_mmPday_array_fft=sp.fftpack.fft(pond_falling_rate_cs451_2_mmPday_array)
pond_falling_rate_cs451_2_mmPday_array_psd = np.abs(pond_falling_rate_cs451_2_mmPday_array_fft) ** 2
fftfreq = sp.fftpack.fftfreq(len(pond_falling_rate_cs451_2_mmPday_array_psd), 1. / 365)
fig, ax = plt.subplots(1, 1, figsize=(8, 4))
ax.plot(fftfreq[i], 10 * np.log10(pond_falling_rate_cs451_2_mmPday_array_psd[i]))
# ax.set_xlim(0, 5)
ax.set_xlabel('Frequency (1/year)')
ax.set_ylabel('PSD (dB)')

i = fftfreq > 0


