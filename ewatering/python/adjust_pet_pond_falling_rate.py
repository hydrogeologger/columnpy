# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 09:33:00 2021

@author: s4680073
"""
fig = plt.figure(figsize=(8, 4))
plt.plot( sp_sch.df.index, sp_sch.df['recharge_mmPday_p3'],linewidth=0.7,label='recharge')
plt.plot( sp_sch.df.index, sp_sch.df['pet_mmPday'],'--',linewidth=0.7,label='pet')
# plt.plot( sp_sch.df.index, sp_sch.df['rn_wPm2'],linewidth=0.7,label='pet')

plt.plot( sp_sch.df.index, sp_sch.df['pond_falling_rate_cs451_3_mmPday_array'],linewidth=0.7,label='falling rate')
plt.ylim([-25,30])
plt.legend(loc="upper right")
plt.savefig(f'cs451_scale_{cs451_scale}_zom_{zom}_irscale_{ir_scale}_alpha_{alpha}.png',dpi=300)
plt.close()

