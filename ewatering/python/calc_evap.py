
#sp_sch.df['tc0_k']=sp_sch.df['tc'].fillna(25.0) +constants.kelvin
#sp_sch.df['wdspdkphavg2m_0']=sp_sch.df['wdspdkphavg2m'].fillna(1.0)

#sp_sch.df['drhowv_sat_dt']= \
#    constants.dsvp_dtk( sp_sch.df['sa1_sht31_temp_1'] )
    
sp_sch.df['drhowv_sat_dt']= \
    constants.dsvp_dtk( sp_sch.df['sa2_t_5803'] )    
    
sp_sch.df['latent_heat_JPkg']= \
    constants.lhv(sp_sch.df['sa2_t_5803'])

# TO181205 during the large block of time tmp1 
#sp_sch.df['sat_vapor_pressure_soil_pa'] =  \
#    constants.svp(sp_sch.df['tmp_soil_surf']+constants.kelvin)
sp_sch.df['sat_vapor_pressure_soil_pa'] = constants.svp(21.0+constants.kelvin)
sp_sch.df['vapor_pressure_air_pa'] = \
    constants.svp(sp_sch.df['sa2_t_5803'])* \
    sp_sch.df['sa1_sht31_humidity_1']
 
sp_sch.df['ra_sPm']=np.log(2/0.000001) **2.0 \
    /0.41**2.0/sp_sch.df['wind_speed_mPs'] 



#sp_sch.df['rs_sPm']= \
#    10.*np.exp(rs1994_param2*(rs1994_param- sp_sch.df['mmo_surf']  ))
sp_sch.df['pet_pm_denom'] = sp_sch.df['drhowv_sat_dt'] + \
    constants.psych* ( 1.+ 1./sp_sch.df['ra_sPm'] )

#sp_sch.df['aet_pm_denom_rs'] = sp_sch.df['drhowv_sat_dt'] + constants.psych* \
#        ( 1.+ sp_sch.df['rs_sPm']/sp_sch.df['ra_sPm'] )

sp_sch.df['pet_pm_part1']= \
    ( sp_sch.df['drhowv_sat_dt'] * sp_sch.df['rn_wPm2']  ) \
    / sp_sch.df['pet_pm_denom']
sp_sch.df['pet_pm_part2']= \
    constants.air_density_kgPm3*constants.heat_capacity_air_JPkgPK*  \
    ( sp_sch.df['sat_vapor_pressure_soil_pa'] -  \
    sp_sch.df['vapor_pressure_air_pa']   ) \
    /sp_sch.df['ra_sPm'] / sp_sch.df['pet_pm_denom']

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
#sp_sch.df['aet_mmPday']=sp_sch.df['aet_part1_mmPday'] + \
#    sp_sch.df['aet_part2_mmPday'].fillna(0) 
# -*- coding: utf-8 -*-

plt.figure()
plt.scatter(x= sp_sch.df.index, y=sp_sch.df['drhowv_sat_dt']
    ,color=['blue'])


plt.figure()

plt.scatter(x= sp_sch.df.index, y=sp_sch.df['pet_mmPday']
    ,color=['blue'])


df_mean = sp_sch.df.resample('D').mean()


plt.figure()

plt.scatter(x= df_mean.index, y=df_mean['pet_mmPday']
    ,color=['blue'])
