# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 11:45:14 2021

@author: s4680073
"""

sp_sch.merge_data_from_tb(
        input_time_series=tb_pandas.result_df['sa3_mo1'].index, 
        input_data_series=tb_pandas.result_df['sa3_mo1']['value'], 
        output_time_series=sp_sch.df.index,key_name='sa3_mo1' ,
        plot=plot_interpolate  ,coef=2e-10,rm_nan=True)
sp_sch.merge_data_from_tb(
        input_time_series=tb_pandas.result_df['sa3_mo2'].index, 
        input_data_series=tb_pandas.result_df['sa3_mo2']['value'], 
        output_time_series=sp_sch.df.index,key_name='sa3_mo2' ,
        plot=plot_interpolate  ,coef=2e-10,rm_nan=True)
sp_sch.merge_data_from_tb(
        input_time_series=tb_pandas.result_df['sa3_mo3'].index, 
        input_data_series=tb_pandas.result_df['sa3_mo3']['value'], 
        output_time_series=sp_sch.df.index,key_name='sa3_mo3' ,
        plot=plot_interpolate  ,coef=2e-10,rm_nan=True)
sp_sch.merge_data_from_tb(
        input_time_series=tb_pandas.result_df['sa3_mo4'].index, 
        input_data_series=tb_pandas.result_df['sa3_mo4']['value'], 
        output_time_series=sp_sch.df.index,key_name='sa3_mo4' ,
        plot=plot_interpolate  ,coef=2e-10,rm_nan=True)
sp_sch.merge_data_from_tb(
        input_time_series=tb_pandas.result_df['sa3_mo5'].index, 
        input_data_series=tb_pandas.result_df['sa3_mo5']['value'], 
        output_time_series=sp_sch.df.index,key_name='sa3_mo5' ,
        plot=plot_interpolate  ,coef=2e-10,rm_nan=True)

sp_sch.df['sa3_mo1_volumematric_moisture']=( sp_sch.df['sa3_mo1']-222)/(372-222)*porosity
sp_sch.df['sa3_mo2_volumematric_moisture']=( sp_sch.df['sa3_mo2']-279)/(372-279)*porosity
sp_sch.df['sa3_mo3_volumematric_moisture']=( sp_sch.df['sa3_mo3']-293)/(382-293)*porosity
sp_sch.df['sa3_mo4_volumematric_moisture']=( sp_sch.df['sa3_mo4']-272)/(382-272)*porosity
sp_sch.df['sa3_mo5_volumematric_moisture']=( sp_sch.df['sa3_mo5']-222)/(372-222)*porosity
fig, ax = plt.subplots(figsize=[30,9])
plt.setp(ax.spines.values(), linewidth=2)
ax.plot(sp_sch.df['sa3_mo1_volumematric_moisture'],label='5cm below surface')
ax.plot(sp_sch.df['sa3_mo2_volumematric_moisture'],label='10cm below surface')
ax.plot(sp_sch.df['sa3_mo3_volumematric_moisture'],label='20cm below surface')
ax.plot(sp_sch.df['sa3_mo4_volumematric_moisture'],label='30cm below surface')
ax.plot(sp_sch.df['sa3_mo5_volumematric_moisture'],label='50cm below surface')
ax.legend(loc='lower right',fontsize=26)
ax.set_xlabel('Time',weight='bold',fontsize=35)
ax.set_ylabel('Volumetric water content (-)',weight='bold',fontsize=35)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b/%d'))
ax.set_xlim(datetime.date(2021, 3,16), datetime.date(2021, 6, 5))
plt.xticks(fontsize=28, rotation=0)
plt.yticks(fontsize=28, rotation=0)
plt.grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
plt.savefig('sa3_moisture_sensor.png',dpi=300,bbox_inches = 'tight',
    pad_inches = 0)

    moisture_sa3=pd.DataFrame({'sa3_surface_volumematric_moisture':sp_sch_30min['sa3_mo1_volumematric_moisture'],
                                'sa3_5cm_volumematric_moisture':sp_sch_30min['sa3_mo2_volumematric_moisture'],
                                'sa3_10cm_volumematric_moisture':sp_sch_30min['sa3_mo3_volumematric_moisture'],
                                'sa3_20cm_volumematric_moisture':sp_sch_30min['sa3_mo4_volumematric_moisture'],
                                'sa3_50cm_volumematric_moisture':sp_sch_30min['sa3_mo5_volumematric_moisture'],
                             })