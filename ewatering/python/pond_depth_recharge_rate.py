# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 20:27:05 2021

@author: s4680073
"""
grid_width=2

#split day time
nighttime = sp_sch.df.between_time('0:00:00', '05:00:00')
# nighttime1 = sp_sch.df.between_time('0:00:00', '02:00:00')
# nighttime2 = sp_sch.df.between_time('02:0:00', '05:00:00')
nighttime_no_pumping_1=nighttime.loc['2021-03-25':'2021-05-24']
nighttime_no_pumping_2=nighttime.loc['2021-05-27':'2021-10-07']
nighttime_no_pumping=pd.concat([nighttime_no_pumping_1,nighttime_no_pumping_2])

# nighttime_no_pumping=[nighttime_no_pumping_1,nighttime_no_pumping_2]
# nighttime_no_pumping=pd.concat(nighttime_no_pumping)
# nighttime_no_pumping['infiltration_mmPday_p2'][nighttime_no_pumping['infiltration_mmPday_p2']<0]=np.nan
# plt.plot(nighttime_no_pumping['pond_falling_rate_cs451_3_mmPday'],nighttime_no_pumping['infiltration_mmPday_p3'],'.')
# plt.xlim([-20,0])
# plt.ylim([0,20])
# plt.xlabel('infiltration rate (mm/day)')
# plt.ylabel('Pond falling rate (mm/day)')
# plt.tight_layout()
# plt.savefig('falling_rate_infiltration_rate.png',dpi=300)

# plt.plot(nighttime['p3_cs451'],nighttime['pond_falling_rate_cs451_3_mmPday'],'.')
elev_1=nighttime_no_pumping_1['p2_cs451_coef100']-0.48
elev_2=nighttime_no_pumping_2['p2_cs451_coef100']-0.48
elev_1[elev_1<=0]=0
elev_2[elev_2<=0]=0
nighttime_no_pumping_1['infiltration_mmPday_p3'][elev_1>0.82]=np.nan
nighttime_no_pumping_2['infiltration_mmPday_p3'][elev_2<0.06]=np.nan

fig= plt.figure(figsize=(8, 4))
nighttime_no_pumping_1['infiltration_mmPday_p3'][nighttime_no_pumping_1['infiltration_mmPday_p3']<0]=np.nan
nighttime_no_pumping_2['infiltration_mmPday_p3'][nighttime_no_pumping_2['infiltration_mmPday_p3']<0]=np.nan
plt.plot(elev_1,nighttime_no_pumping_1['infiltration_mmPday_p3'],'r.',label='After the first pumping')
plt.plot(elev_2,nighttime_no_pumping_2['infiltration_mmPday_p3'],'g.',label='After the second pumping')

# plt.plot(nighttime_no_pumping['infiltration_mmPday_p3'],'.')

# elev_1[elev_1<=0]=0
# plt.plot(elev,nighttime['infiltration_mmPday_p2'],'k.',label='No pumping activity')
# plt.plot(nighttime_pumping['p2_cs451_coef100']-0.48,nighttime_pumping['infiltration_mmPday_p2'],'r.',label='During pumping activities')

# plt.plot(nighttime['infiltration_mmPday_p3'],'.')
# plt.plot(sp_sch.df['infiltration_mmPday_p3'])
# plt.plot(nighttime['pond_falling_rate_cs451_3_mmPday'],'.')
# plt.plot(daytime['infiltration_mmPday_p3'],daytime['pond_falling_rate_cs451_3_mmPday'])
plt.ylabel('Infiltration rate (mm/day)')
plt.xlabel('Pond depth near station SA2 (m)')
plt.legend()
plt.grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
plt.savefig('pond_depth_infiltration_rate.png',dpi=300)


