
#sp_sch.df['tc0_k']=sp_sch.df['tc'].fillna(25.0) +constants.kelvin
#sp_sch.df['wdspdkphavg2m_0']=sp_sch.df['wdspdkphavg2m'].fillna(1.0)

#sp_sch.df['drhowv_sat_dt']= \
#    constants.dsvp_dtk( sp_sch.df['sa1_sht31_temp_1'] )
# runfile('C:\columnpy\columnpy\ewatering\python\get_data_py3.py')
# runfile('C:\columnpy\columnpy\ewatering\python\calc_area.py')
# def sp_sch()
# runfile('c:\columnpy\columnpy\ewatering\python\get_data_py3.py')
sp_sch.df['tc0_k']=sp_sch.df['sa1_sht31_temp_1'] +constants.kelvin
sp_sch.df['drhowv_sat_dt']= \
    constants.dsvp_dtk( sp_sch.df['tc0_k'])   
# sp_sch.merge_data_from_tb(
#         input_time_series=tb_pandas.result_df['drhowv_sat_dt'].index, 
#         input_data_series=tb_pandas.result_df['drhowv_sat_dt']['value'], 
#         output_time_series=sp_sch.df.index,key_name='drhowv_sat_dt' ,
#         plot=plot_interpolate  ,coef=5e-8,rm_nan=True)    

 
# sp_sch.merge_data_from_tb(
#         input_time_series=tb_pandas.result_df['drhowv_sat_dt'].index, 
#         input_data_series=tb_pandas.result_df['drhowv_sat_dt']['value'], 
#         output_time_series=sp_sch.df.index,key_name='drhowv_sat_dt' ,
#         plot=plot_interpolate  ,coef=5e-8,rm_nan=True)    
sp_sch.df['tc0_k']=sp_sch.df['sa2_t_5803'] +constants.kelvin
sp_sch.df['drhowv_sat_dt']= \
    constants.dsvp_dtk( sp_sch.df['tc0_k'])    

    
sp_sch.df['latent_heat_JPkg']= \
    constants.lhv(sp_sch.df['drhowv_sat_dt'])

# TO181205 during the large block of time tmp1 
#sp_sch.df['sat_vapor_pressure_soil_pa'] =  \
#    constants.svp(sp_sch.df['tmp_soil_surf']+constants.kelvin)
# sp_sch.df['sat_vapor_pressure_soil_pa'] = constants.svp(21.0+constants.kelvin)
sp_sch.df['sat_vapor_pressure_soil_pa'] = constants.svp(sp_sch.df['sa2_temp1']+constants.kelvin)

sp_sch.df['vapor_pressure_air_pa'] = \
    constants.svp(sp_sch.df['tc0_k'])* \
    (sp_sch.df['sa1_sht31_humidity_1']/100)
 
sp_sch.df['ra_sPm']=np.log(2/0.000001) **2.0 \
     /0.41**2.0/sp_sch.df['wind_speed_mPs']/1.0
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

sp_sch.df['pet_pm_part1']= \
    ( sp_sch.df['drhowv_sat_dt'] * sp_sch.df['rn_wPm2']  ) \
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
sp_sch.df['recharge_mmPday_p3']=-(sp_sch.df['pond_falling_rate_cs451_3_mmPday']+sp_sch.df['pet_mmPday'])
sp_sch.df['recharge_mmPday_p2']=-(sp_sch.df['pond_falling_rate_cs451_2_mmPday']+sp_sch.df['pet_mmPday'])