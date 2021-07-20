# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 14:43:17 2021

@author: s4680073
"""

sp_sch.df['sa1_groundwater_table_mAHD']=(sp_sch.df['sa1_p_kpa'])*100/1000+14.673
sp_sch.df['sa2_groundwater_table_mAHD']=(sp_sch.df['sa2_p_kpa'])*100/1000+13.696
sp_sch.df['sa3_groundwater_table_mAHD']=(sp_sch.df['sa3_p_kpa'])*100/1000+13.922
sp_sch.df['sa4_groundwater_table_mAHD']=(sp_sch.df['sa4_p_kpa'])*100/1000+15.3
sp_sch.df['sa2_groundwater_table_rise_m']=(sp_sch.df['sa2_p_kpa']-16.35)*100
plt.plot(sp_sch.df['sa1_groundwater_table_mAHD'],label='1')
plt.plot(sp_sch.df['sa2_groundwater_table_mAHD'],label='2')
plt.plot(sp_sch.df['sa3_groundwater_table_mAHD'],label='3')
plt.plot(sp_sch.df['sa4_groundwater_table_mAHD'],label='4')

piezo_groundwater_table_mAHD=pd.DataFrame({'datetime':pd.to_datetime(sp_sch_30min.index, format = '%d/%m/%Y'),
                            'sa1_groundwater_table_mAHD':sp_sch_30min['sa1_groundwater_table_mAHD'],
                         'sa2_groundwater_table_mAHD':sp_sch_30min['sa2_groundwater_table_mAHD'],
                         'sa3_groundwater_table_mAHD':sp_sch_30min['sa3_groundwater_table_mAHD'],
                         'sa4_groundwater_table_mAHD':sp_sch_30min['sa4_groundwater_table_mAHD'],
                         })
piezo_groundwater_table_mAHD.to_excel('grounwater_tabel.xlsx', sheet_name='groundwater_table_mAHD')
