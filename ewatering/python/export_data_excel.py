# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 21:39:39 2021

@author: s4680073
"""
import datetime
sp_sch_30min=sp_sch.df.resample('30T').ffill()
##save DF to excel
with pd.ExcelWriter('Piezo.xlsx') as writer:  
    #piezo data
    piezo_pressure=pd.DataFrame({'datetime':pd.to_datetime(sp_sch_30min.index, format = '%d/%m/%Y'),
                                'sa1_p_piezo':sp_sch_30min['sa1_p_piezo'],
                             'sa2_p_piezo':sp_sch_30min['sa2_p_piezo'],
                             'sa3_p_piezo':sp_sch_30min['sa3_p_piezo'],
                             'sa4_p_piezo':sp_sch_30min['sa4_p_piezo'],
                             })
    piezo_pressure.to_excel(writer, sheet_name='Piezo_water_level')
    piezo_ec=pd.DataFrame({'datetime':pd.to_datetime(sp_sch_30min.index, format = '%d/%m/%Y'),
                         'sa1_ec_piezo':sp_sch_30min['sa1_ec_piezo'],
                         'sa2_ec_piezo':sp_sch_30min['sa2_ec_piezo'],
                         'sa3_ec_piezo':sp_sch_30min['sa3_ec_piezo'],
                         'sa4_ec_piezo':sp_sch_30min['sa4_ec_piezo'],
                         })
    piezo_ec.to_excel(writer, sheet_name='Piezo_ec')
    piezo_temp=pd.DataFrame({'datetime':pd.to_datetime(sp_sch_30min.index, format = '%d/%m/%Y'),
        'sa1_temp_piezo':sp_sch_30min['sa1_t_piezo'],
                     'sa2_temp_piezo':sp_sch_30min['sa2_t_piezo'],
                     'sa3_temp_piezo':sp_sch_30min['sa3_t_piezo'],
                     'sa4_temp_piezo':sp_sch_30min['sa4_t_piezo'],
                     })
    piezo_temp.to_excel(writer, sheet_name='Piezo_temp')
    
with pd.ExcelWriter('Weather_data.xlsx') as writer:  
    Weather_station=pd.DataFrame({'temp':sp_sch_30min['sa1_sht31_temp_1'],
                             'wind_speed':sp_sch_30min['wind_speed_mPs'],
                             'uv':sp_sch_30min['sa2_uv'],
                             'rn_wPm2':sp_sch_30min['rn_wPm2'],
                             'rainfall':sp_sch_30min['rainfall'],
                             '5803':sp_sch_30min['sa1_p_5803'],
                             'humidity':sp_sch_30min['sa1_sht31_humidity_1']
                             })
    Weather_station.to_excel(writer, sheet_name='Weather_data')
    
sp_sch.merge_data_from_tb(
        input_time_series=tb_pandas.result_df['sa1_sht31_humidity_1'].index, 
        input_data_series=tb_pandas.result_df['sa1_sht31_humidity_1']['value'], 
        output_time_series=sp_sch.df.index,key_name='sa1_sht31_humidity_1' ,
        plot=plot_interpolate  ,coef=5e-8,rm_nan=True)
    # sp_sch_30min['sa1_p_piezo'].to_excel(writer, sheet_name='sa1_p_piezo')
    # sp_sch_30min['sa1_ec_piezo'].to_excel(writer, sheet_name='sa1_ec_piezo')
    # sp_sch_30min['sa2_t_piezo'].to_excel(writer, sheet_name='sa2_t_piezo')
    # sp_sch_30min['sa2_p_piezo'].to_excel(writer, sheet_name='sa2_p_piezo')
    # sp_sch_30min['sa2_ec_piezo'].to_excel(writer, sheet_name='sa2_ec_piezo')
    # sp_sch_30min['sa3_t_piezo'].to_excel(writer, sheet_name='sa3_t_piezo')
    # sp_sch_30min['sa3_p_piezo'].to_excel(writer, sheet_name='sa3_p_piezo')
    # sp_sch_30min['sa3_ec_piezo'].to_excel(writer, sheet_name='sa3_ec_piezo')
    # sp_sch_30min['sa4_t_piezo'].to_excel(writer, sheet_name='sa4_t_piezo')
    # sp_sch_30min['sa4_p_piezo'].to_excel(writer, sheet_name='sa4_p_piezo')
    # sp_sch_30min['sa4_ec_piezo'].to_excel(writer, sheet_name='sa4_ec_piezo')
    #Weather station data
    sp_sch_30min['sa1_sht31_temp_1'].to_excel(writer, sheet_name='sa1_sht31_temp_1')
    sp_sch_30min['wind_speed_mPs'].to_excel(writer, sheet_name='wind_speed_mPs')
    sp_sch_30min['sa2_uv'].to_excel(writer, sheet_name='sa2_uv')
    sp_sch_30min['sa1_ir'].to_excel(writer, sheet_name='sa1_ir')
    sp_sch_30min['rainfall'].to_excel(writer, sheet_name='rainfall')
    sp_sch_30min['sa1_p_5803'].to_excel(writer, sheet_name='Barometric pressure')
    #moisture 
    porosity=0.46
with pd.ExcelWriter('moisture_sensors_updated.xlsx') as writer:  
    moisture_sa3=pd.DataFrame({'sa3_surface_volumematric_moisture':sp_sch_30min['sa3_mo1_volumematric_moisture'],
                            'sa3_5cm_volumematric_moisture':sp_sch_30min['sa3_mo2_volumematric_moisture'],
                            'sa3_10cm_volumematric_moisture':sp_sch_30min['sa3_mo3_volumematric_moisture'],
                            'sa3_20cm_volumematric_moisture':sp_sch_30min['sa3_mo4_volumematric_moisture'],
                            'sa3_50cm_volumematric_moisture':sp_sch_30min['sa3_mo5_volumematric_moisture'],
                         })
    moisture_sa3.to_excel(writer, sheet_name='Moisture_probe_volumemetric_water_content_sa3')

    sp_sch_30min['sa2_mo1_volumematric_moisture']=( sp_sch_30min['sa2_mo1']-1800)/(3095-1800)*porosity
    sp_sch_30min['sa2_mo2_volumematric_moisture']=( sp_sch_30min['sa2_mo2']-1800)/(3050-1800)*porosity
    sp_sch_30min['sa2_mo3_volumematric_moisture']=( sp_sch_30min['sa2_mo3']-1800)/(3028-1800)*porosity
    sp_sch_30min['sa2_mo4_volumematric_moisture']=( sp_sch_30min['sa2_mo4']-1800)/(2980-1800)*porosity
    sp_sch_30min['sa2_mo5_volumematric_moisture']=( sp_sch_30min['sa2_mo5']-1800)/(3001-1800)*porosity
    moisture_SA2=pd.DataFrame({'sa2_surface_volumematric_water_content':sp_sch_30min['sa2_mo1_volumematric_moisture'],
                                'sa2_5cm_volumematric_water_content':sp_sch_30min['sa2_mo2_volumematric_moisture'],
                                'sa2_10cm_volumematric_water_content':sp_sch_30min['sa2_mo3_volumematric_moisture'],
                                'sa2_20cm_volumematric_water_content':sp_sch_30min['sa2_mo4_volumematric_moisture'],
                                'sa2_50cm_volumematric_water_content':sp_sch_30min['sa2_mo5_volumematric_moisture']
                             })
    moisture_SA2.to_excel(writer, sheet_name='Moisture_probe_volumemetric_water_content_sa2')
    moisture_temp_SA2=pd.DataFrame({'sa2_surface_temp':sp_sch_30min['sa2_temp1'],
                                'sa2_5cm_temp':sp_sch_30min['sa2_temp2'],
                                'sa2_10cm_temp':sp_sch_30min['sa2_temp3'],
                                'sa2_20cm_temp':sp_sch_30min['sa2_temp4'],
                                'sa2_50cm_temp':sp_sch_30min['sa2_temp5']
                             })
    moisture_temp_SA2.to_excel(writer, sheet_name='Moisture_probe_temp_sa2')
    moisture_ec_SA2=pd.DataFrame({'sa2_surface_ec':sp_sch_30min['sa2_ec1'],
                                'sa2_5cm_ec':sp_sch_30min['sa2_ec2'],
                                'sa2_10cm_ec':sp_sch_30min['sa2_ec3'],
                                'sa2_20cm_ec':sp_sch_30min['sa2_ec4'],
                                'sa2_50cm_ec':sp_sch_30min['sa2_ec5']
                             })
    moisture_ec_SA2.to_excel(writer, sheet_name='Moisture_probe_ec_sa2')    
    sp_sch_30min['sa1_mo1_volumematric_moisture']=( sp_sch_30min['sa1_mo1']-1800)/(3095-1800)*porosity
    sp_sch_30min['sa1_mo2_volumematric_moisture']=( sp_sch_30min['sa1_mo2']-1800)/(3050-1800)*porosity
    sp_sch_30min['sa1_mo3_volumematric_moisture']=( sp_sch_30min['sa1_mo3']-1800)/(3028-1800)*porosity
    sp_sch_30min['sa1_mo4_volumematric_moisture']=( sp_sch_30min['sa1_mo4']-1800)/(2980-1800)*porosity
    sp_sch_30min['sa1_mo5_volumematric_moisture']=( sp_sch_30min['sa1_mo5']-1800)/(3001-1800)*porosity
    moisture_sa1=pd.DataFrame({'sa1_surface_volumematric_moisture':sp_sch_30min['sa1_mo1_volumematric_moisture'],
                                'sa1_5cm_volumematric_moisture':sp_sch_30min['sa1_mo2_volumematric_moisture'],
                                'sa1_10cm_volumematric_moisture':sp_sch_30min['sa1_mo3_volumematric_moisture'],
                                'sa1_20cm_volumematric_moisture':sp_sch_30min['sa1_mo4_volumematric_moisture'],
                                'sa1_50cm_volumematric_moisture':sp_sch_30min['sa1_mo5_volumematric_moisture'],
                             })
    moisture_sa1.to_excel(writer, sheet_name='Moisture_probe_volumemetric_moisture_content_sa1')
    moisture_temp_sa1=pd.DataFrame({'sa1_surface_temp':sp_sch_30min['sa1_temp1'],
                                'sa1_5cm_temp':sp_sch_30min['sa1_temp2'],
                                'sa1_10cm_temp':sp_sch_30min['sa1_temp3'],
                                'sa1_20cm_temp':sp_sch_30min['sa1_temp4'],
                                'sa1_50cm_temp':sp_sch_30min['sa1_temp5'],
                             })
    moisture_temp_sa1.to_excel(writer, sheet_name='Moisture_probe_temp_sa1')
    moisture_ec_sa1=pd.DataFrame({'sa1_surface_ec':sp_sch_30min['sa1_ec1'],
                                'sa1_5cm_ec':sp_sch_30min['sa1_ec2'],
                                'sa1_10cm_ec':sp_sch_30min['sa1_ec3'],
                                'sa1_20cm_ec':sp_sch_30min['sa1_ec4'],
                                'sa1_50cm_ec':sp_sch_30min['sa1_ec5'],
                             })
    moisture_ec_sa1.to_excel(writer, sheet_name='Moisture_probe_ec_sa1')       
    sp_sch_30min['sa2_temp1'].to_excel(writer, sheet_name='sa2_temp1')
    sp_sch_30min['sa2_temp2'].to_excel(writer, sheet_name='sa2_temp2')
    sp_sch_30min['sa2_temp3'].to_excel(writer, sheet_name='sa2_temp3')
    sp_sch_30min['sa2_temp4'].to_excel(writer, sheet_name='sa2_temp4')
    sp_sch_30min['sa2_temp5'].to_excel(writer, sheet_name='sa2_temp5')
    sp_sch_30min['sa2_ec1'].to_excel(writer, sheet_name='sa2_moisture_sensor_ec1')
    sp_sch_30min['sa2_ec2'].to_excel(writer, sheet_name='sa2_moisture_sensor_ec2')
    sp_sch_30min['sa2_ec3'].to_excel(writer, sheet_name='sa2_moisture_sensor_ec3')
    sp_sch_30min['sa2_ec4'].to_excel(writer, sheet_name='sa2_moisture_sensor_ec4')
    sp_sch_30min['sa2_ec5'].to_excel(writer, sheet_name='sa2_moisture_sensor_ec5')
    sp_sch_30min['sa1_mo1_volumematric_moisture']=( sp_sch_30min['sa1_raw1']-1935)/(3095-1935)
    sp_sch_30min['sa1_mo2_volumematric_moisture']=( sp_sch_30min['sa1_raw2']-1950)/(3050-1950)
    sp_sch_30min['sa1_mo3_volumematric_moisture']=( sp_sch_30min['sa1_raw3']-1965)/(3028-1965)
    sp_sch_30min['sa1_mo4_volumematric_moisture']=( sp_sch_30min['sa1_raw4']-1925)/(2980-1925)
    sp_sch_30min['sa1_mo5_volumematric_moisture']=( sp_sch_30min['sa1_raw5']-1945)/(3001-1925)
    sp_sch_30min['sa1_temp1'].to_excel(writer, sheet_name='sa1_temp1')
    sp_sch_30min['sa1_temp2'].to_excel(writer, sheet_name='sa1_temp2')
    sp_sch_30min['sa1_temp3'].to_excel(writer, sheet_name='sa1_temp3')
    sp_sch_30min['sa1_temp4'].to_excel(writer, sheet_name='sa1_temp4')
    sp_sch_30min['sa1_temp5'].to_excel(writer, sheet_name='sa1_temp5')
    sp_sch_30min['sa3_ec1'].to_excel(writer, sheet_name='sa3_moisture_sensor_ec1')
    sp_sch_30min['sa3_ec2'].to_excel(writer, sheet_name='sa3_moisture_sensor_ec2')
    sp_sch_30min['sa3_ec3'].to_excel(writer, sheet_name='sa3_moisture_sensor_ec3')
    sp_sch_30min['sa3_ec4'].to_excel(writer, sheet_name='sa3_moisture_sensor_ec4')
    sp_sch_30min['sa3_ec5'].to_excel(writer, sheet_name='sa3_moisture_sensor_ec5')
    


with pd.ExcelWriter('rainfall.xlsx') as writer:  

    sp_sch_30min['rainfall'].to_excel(writer)