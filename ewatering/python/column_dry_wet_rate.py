# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 16:15:29 2022

@author: s4680073
"""
#wetting process
##Calculate the infiltration and water loss of the large column
depth=[0.1,0.2,0.3,0.5,0.7]
#wetting process
porosity=0.5
#wetting process
column_mo0_volumematric_moisture_wet=0.4
part1_wet_m=(column_mo0_volumematric_moisture_wet+sp_sch.df['column_mo2_volumematric_moisture'])/2*0.1
part2_wet_m=(sp_sch.df['column_mo1_volumematric_moisture']+sp_sch.df['column_mo2_volumematric_moisture'])/2*0.1
part3_wet_m=(sp_sch.df['column_mo2_volumematric_moisture']+sp_sch.df['column_mo3_volumematric_moisture'])/2*0.1
totalwater_infiltration_m=(part1_wet+part2_wet+part3_wet)
infiltration_rate_mmPday=constants.mmPm*(np.diff(totalwater_infiltration_m)/sp_input['delta_t_s'])/constants.dayPs
infiltration_rate_mmPday[np.abs(infiltration_rate_mmPday)>20]=np.nan
plt.plot(sp_sch.df.index[1:],infiltration_rate_mmPday)
plt.xlabel('Time')
plt.ylabel('Infiltration rate (mm)')

#drying process
column_mo0_volumematric_moisture_dry=0
part1_dry_water_m=(column_mo0_volumematric_moisture_dry+sp_sch.df['column_mo1_volumematric_moisture'])/2*0.1
part2_dry_water_m=(sp_sch.df['column_mo1_volumematric_moisture']+sp_sch.df['column_mo2_volumematric_moisture'])/2*0.1
part3_dry_water_m=(sp_sch.df['column_mo2_volumematric_moisture']+sp_sch.df['column_mo3_volumematric_moisture'])/2*0.1
totalwater_evp_m=(part1_dry_water_m+part2_dry_water_m+part3_dry_water_m)
evp_rate_mmPday=constants.mmPm*(np.diff(totalwater_evp_m)/sp_input['delta_t_s'])/constants.dayPs
evp_rate_mmPday[np.abs(evp_rate_mmPday)>5]=np.nan
plt.figure()
plt.plot(sp_sch.df.index[1:],-evp_rate_mmPday)
plt.xlabel('Time')
plt.ylabel('Evaporation rate (mm)')

