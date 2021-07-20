# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 20:27:05 2021

@author: s4680073
"""
#split day time
nighttime = sp_sch.df.between_time('0:00:00', '05:00:00')
nighttime1 = sp_sch.df.between_time('0:00:00', '02:00:00')
nighttime2 = sp_sch.df.between_time('02:0:00', '05:00:00')
nighttime_no_pumping_1=nighttime.loc['2021-03-25':'2021-05-24']
nighttime_no_pumping_2=nighttime.loc['2021-05-27':'2021-06-05']

nighttime_no_pumping=[nighttime_no_pumping_1,nighttime_no_pumping_2]
nighttime_no_pumping=pd.concat(nighttime_no_pumping)
nighttime_no_pumping['recharge_mmPday_p2'][nighttime_no_pumping['recharge_mmPday_p2']<0]=np.nan
plt.plot(nighttime_no_pumping['pond_falling_rate_cs451_3_mmPday'],nighttime_no_pumping['recharge_mmPday_p3'],'.')
plt.xlim([-20,0])
plt.ylim([0,20])
plt.xlabel('Recharge rate (mm/day)')
plt.ylabel('Pond falling rate (mm/day)')
plt.tight_layout()
plt.savefig('falling_rate_recharge_rate.png',dpi=300)

plt.plot(nighttime['p3_cs451'],nighttime['pond_falling_rate_cs451_3_mmPday'],'.')
fig= plt.figure(figsize=(8, 4))
elev=nighttime_no_pumping['p2_cs451_coef100']-0.48

plt.plot(elev,nighttime_no_pumping['recharge_mmPday_p2'],'b.')
# plt.plot(nighttime_no_pumping['recharge_mmPday_p3'],'.')

elev[elev<=0]=0
# plt.plot(elev,nighttime['recharge_mmPday_p2'],'k.',label='No pumping activity')
# plt.plot(nighttime_pumping['p2_cs451_coef100']-0.48,nighttime_pumping['recharge_mmPday_p2'],'r.',label='During pumping activities')

# plt.plot(nighttime['recharge_mmPday_p3'],'.')
# plt.plot(sp_sch.df['recharge_mmPday_p3'])
# plt.plot(nighttime['pond_falling_rate_cs451_3_mmPday'],'.')
# plt.plot(daytime['recharge_mmPday_p3'],daytime['pond_falling_rate_cs451_3_mmPday'])
plt.ylabel('Recharge rate (mm/day)')
plt.xlabel('Pond depth near station SA2 (m)')
plt.tight_layout()
plt.legend()
plt.grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')

plt.savefig('pond_depth_recharge_rate.png',dpi=300)
