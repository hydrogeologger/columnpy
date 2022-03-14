# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 14:43:17 2021

@author: s4680073
"""

sp_sch.df['sa1_groundwater_table_mAHD']=(sp_sch.df['sa1_p_kpa'])*100/1000+14.673
sp_sch.df['sa2_groundwater_table_mAHD']=(sp_sch.df['sa2_p_kpa'])*100/1000+13.696
sp_sch.df['sa3_groundwater_table_mAHD']=(sp_sch.df['sa3_p_kpa'])*100/1000+13.922
sp_sch.df['sa4_groundwater_table_mAHD']=(sp_sch.df['sa4_p_kpa'])*100/1000+15.3
sp_sch.df['sa1_groundwater_table_rise_mm']=(sp_sch.df['sa1_p_kpa']-6.6  )*100
sp_sch.df['sa2_groundwater_table_rise_mm']=(sp_sch.df['sa2_p_kpa']-16.35)*100
sp_sch.df['sa3_groundwater_table_rise_mm']=(sp_sch.df['sa3_p_kpa']-9.85 )*100 
sp_sch.df['sa4_groundwater_table_rise_mm']=(sp_sch.df['sa4_p_kpa']-33.40)*100
plt.plot(sp_sch.df['sa1_groundwater_table_mAHD'],label='1')
plt.plot(sp_sch.df['sa2_groundwater_table_mAHD'],label='2')
plt.plot(sp_sch.df['sa3_groundwater_table_mAHD'],label='3')
plt.plot(sp_sch.df['sa4_groundwater_table_mAHD'],label='4')
sp_sch.df['infiltration_cum_ML']=df_cumsum['infiltration_ML']

# piezo_groundwater_table_mAHD=pd.DataFrame({'datetime':pd.to_datetime(sp_sch_30min.index, format = '%d/%m/%Y'),
#                             'sa1_groundwater_table_mAHD':sp_sch_30min['sa1_groundwater_table_mAHD'],
#                          'sa2_groundwater_table_mAHD':sp_sch_30min['sa2_groundwater_table_mAHD'],
#                          'sa3_groundwater_table_mAHD':sp_sch_30min['sa3_groundwater_table_mAHD'],
#                          'sa4_groundwater_table_mAHD':sp_sch_30min['sa4_groundwater_table_mAHD'],
#                          })
# piezo_groundwater_table_mAHD.to_excel('grounwater_tabel.xlsx', sheet_name='groundwater_table_mAHD')

sp_sch.df.to_excel('sp_sch.xlsx', sheet_name='all')

new=sp_sch.df['sa4_groundwater_table_rise_m'].loc['2021-3-15 15':'2021-7-15 12 0']
new.to_excel('new.xlsx', sheet_name='all')

sp_sch.df['sa1_groundwater_table_rise_mm_1']=(sp_sch.df['sa1_p_kpa_1']-6.6  )*100
sp_sch.df['sa1_groundwater_table_rise_mm_2']=(sp_sch.df['sa1_p_kpa_2']-6.6  )*100
sp_sch.df['sa1_groundwater_table_rise_mm_3']=(sp_sch.df['sa1_p_kpa_3']-6.6  )*100
plt.plot(sp_sch.df['sa1_groundwater_table_rise_mm_1']/1000)
plt.plot(sp_sch.df['sa1_groundwater_table_rise_mm_2']/1000)
plt.plot(sp_sch.df['sa1_groundwater_table_rise_mm_3']/1000)
plt.plot(sp_sch.df['sa1_p_5803']/10)
plt.plot(sp_sch.df['sa2_p_5803']/10)
plt.plot(sp_sch.df['sa3_p_5803']/10)
plt.plot(sp_sch.df['sa1_p_piezo'])


df_cumsum.to_excel('cumsum.xlsx', sheet_name='all')