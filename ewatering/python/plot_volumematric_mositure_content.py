# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 10:42:26 2021

@author: s4680073
"""
fig, ax = plt.subplots(figsize=[30,9])
plt.setp(ax.spines.values(), linewidth=2)
ax.plot(sp_sch.df['sa2_mo1_volumematric_moisture'],label='5cm below surface')
ax.plot(sp_sch.df['sa2_mo2_volumematric_moisture'],label='10cm below surface')
ax.plot(sp_sch.df['sa2_mo3_volumematric_moisture'],label='20cm below surface')
ax.plot(sp_sch.df['sa2_mo4_volumematric_moisture'],label='30cm below surface')
ax.plot(sp_sch.df['sa2_mo5_volumematric_moisture'],label='50cm below surface')
ax.legend(loc='lower right',fontsize=26)
ax.set_xlabel('Time',weight='bold',fontsize=35)
ax.set_ylabel('Volumetric water content (-)',weight='bold',fontsize=35)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b/%d'))
ax.set_xlim(datetime.date(2021, 3, 16), datetime.date(2021, 6, 5))
plt.xticks(fontsize=28, rotation=0)
plt.yticks(fontsize=28, rotation=0)
plt.grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
# ax.set_ylim(0,1.1)
plt.savefig('sa2_moisture sensor.png',dpi=300,bbox_inches = 'tight',
    pad_inches = 0)

fig, ax = plt.subplots(figsize=[16,9])

ax.set_xlim([datetime.date(2021, 5, 12), datetime.date(2021, 6, 5)])

fig, ax = plt.subplots(figsize=[30,9])
plt.setp(ax.spines.values(), linewidth=2)
ax.plot(sp_sch.df['sa2_ec1'],label='5cm below surface')
ax.plot(sp_sch.df['sa2_ec2'],label='10cm below surface')
ax.plot(sp_sch.df['sa2_ec3'],label='20cm below surface')
ax.plot(sp_sch.df['sa2_ec4'],label='30cm below surface')
ax.plot(sp_sch.df['sa2_ec5'],label='50cm below surface')
ax.legend(loc='lower right',fontsize=26)
ax.set_xlabel('Time',weight='bold',fontsize=35)
ax.set_ylabel('EC of bulk soil (µS/cm)',weight='bold',fontsize=35)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b/%d'))
ax.set_xlim(datetime.date(2021, 3, 16), datetime.date(2021, 6, 5))
plt.xticks(fontsize=28, rotation=0)
plt.yticks(fontsize=28, rotation=0)
plt.grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
# ax.set_ylim(0,1.1)
plt.savefig('sa2_ec.png',dpi=300,bbox_inches = 'tight',
    pad_inches = 0)
