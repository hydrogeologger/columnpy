sp_sch.df['tc0_k']=sp_sch.df['sa1_sht31_temp_1'] +constants.kelvin 
sp_sch.df['drhowv_sat_dt']= \
    constants.dsvp_dtk( sp_sch.df['sa2_temp1']+constants.kelvin)
sp_sch.df['latent_heat_JPkg']= \
    constants.lhv(sp_sch.df['drhowv_sat_dt'])

sp_sch.df['sat_vapor_pressure_soil_pa'] = constants.svp(sp_sch.df['sa2_temp1']+constants.kelvin)
sp_sch.df['vapor_pressure_air_pa'] = \
    constants.svp(sp_sch.df['tc0_k'])* \
    (sp_sch.df['sa1_sht31_humidity_1']/100)

sp_sch.df['ra_sPm']=np.log(2/zom) **2.0 \
     /0.41**2.0/sp_sch.df['wind_speed_mPs']/alpha
# Check Penman-Monteith equation
# h=0.1
# zom=0.000001
# zoh=0.1*zom
# sp_sch.df['ra_sPm']=np.log((2-h*2/3)/zom) *np.log((2-h*2/3)/zoh/10) \
#     /0.41**2.0/sp_sch.df['wind_speed_mPs'] 


#sp_sch.df['rs_sPm']= \
#    10.*np.exp(rs1994_param2*(rs1994_param- sp_sch.df['mmo_surf']  ))
sp_sch.df['pet_pm_denom'] = sp_sch.df['drhowv_sat_dt'] + \
    constants.psych* ( 1.+ 1./sp_sch.df['ra_sPm'] )

#sp_sch.df['aet_pm_denom_rs'] = sp_sch.df['drhowv_sat_dt'] + constants.psych* \
#        ( 1.+ sp_sch.df['rs_sPm']/sp_sch.df['ra_sPm'] )
# G=heat_conductance*(sp_sch.df['sa2_temp2']-sp_sch.df['sa2_temp1'])/0.05 #0.05m is the distance between two moisture sensors
G=0
sp_sch.df['pet_pm_part1']= \
    ( sp_sch.df['drhowv_sat_dt'] *(sp_sch.df['rn_wPm2']-G)) \
    / sp_sch.df['pet_pm_denom']
sp_sch.df['pet_pm_part2']= \
    constants.air_density_kgPm3*constants.heat_capacity_air_JPkgPK*  \
    ( sp_sch.df['sat_vapor_pressure_soil_pa'] -  \
    sp_sch.df['vapor_pressure_air_pa']   ) \
    /sp_sch.df['ra_sPm'] / sp_sch.df['pet_pm_denom']
    # y=sp_sch.df['pet_pm_part2']['value']
    # sp_sch.df['pet_pm_part2'].loc[sp_sch.df['pet_pm_part2']<0]=0
sp_sch.df['pet_part1_mmPday']=sp_sch.df['pet_pm_part1'] / \
        constants.lhv(298.15)/ constants.rhow_pure_water * constants.msPmmday
sp_sch.df['pet_part2_mmPday']=sp_sch.df['pet_pm_part2'] / \
        constants.lhv(298.15)/ constants.rhow_pure_water * constants.msPmmday

#sp_sch.df['aet_part1_mmPday']= ( sp_sch.df['drhowv_sat_dt'] * sp_sch.df['Rn_wPm2']  ) \
#        / sp_sch.df['aet_pm_denom_rs']/constants.lhv(298.15)/ constants.rhow_pure_water * constants.msPmmday
#
#sp_sch.df['aet_part2_mmPday']=constants.air_density_kgPm3*constants.heat_capacity_air_JPkgPK*  \
#        ( sp_sch.df['sat_vapor_pressure_soil_pa'] -  sp_sch.df['vapor_pressure_air_pa']   ) \
#        /sp_sch.df['ra_sPm'] / sp_sch.df['aet_pm_denom_rs'] \
#        / constants.lhv(298.15)/ constants.rhow_pure_water * constants.msPmmday
sp_sch.df['pet_mmPday']=sp_sch.df['pet_part1_mmPday'] + \
    sp_sch.df['pet_part2_mmPday'].fillna(0) 
sp_sch.df['pet_mmPday'][sp_sch.df['pet_mmPday']>30]=0   
sp_sch.df['pet_mmPday'].loc['2021-10-12':'2022-1-18']=0 
#sp_sch.df['aet_mmPday']=sp_sch.df['aet_part1_mmPday'] + \
#    sp_sch.df['aet_part2_mmPday'].fillna(0) 
# -*- coding: utf-8 -*-
# plt.figure()
# plt.scatter(x= sp_sch.df.index, y=sp_sch.df['drhowv_sat_dt']
#     ,color=['blue'])
plt.figure()
plt.scatter(x= sp_sch.df.index, y=sp_sch.df['pet_mmPday']
    ,color=['blue'])
# df_mean = sp_sch.df.resample('D').mean()
# plt.scatter(x= df_mean.index, y=df_mean['pet_mmPday']
#     ,color=['blue'])
# sp_sch.df
# plt.figure()
# plt.scatter(x= df_mean.index, y=df_mean['pet_mmPday']
#     ,color=['blue'])
sp_sch.df['infiltration_mmPday_p3']=-(sp_sch.df['pond_falling_rate_cs451_3_mmPday']+sp_sch.df['pet_mmPday'])
sp_sch.df['infiltration_mmPday_p2']=-(sp_sch.df['pond_falling_rate_cs451_2_mmPday']+sp_sch.df['pet_mmPday'])
# sp_sch.df['recharge_mmPday_p3']=-(sp_sch.df['pond_falling_rate_cs451_3_mmPday']+sp_sch.df['pet_mmPday']-sp_sch.df['pumped_water_depth'])
# sp_sch.df['recharge_mmPday_p2']=-(sp_sch.df['pond_falling_rate_cs451_2_mmPday']+sp_sch.df['pet_mmPday']-sp_sch.df['pumped_water_depth'])