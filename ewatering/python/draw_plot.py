# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 21:39:12 2021

@author: s4680073
"""
fig,ax5=plt.subplots(figsize=[9,4])
walking_track_area_m2=pd.read_csv('C:/Project/MBDA/walkingtrackarea.csv')
# pump.index=pump['time']
format = '%Y.%m.%d %H:%M'
walking_track_area_m2['date_time'] = pd.to_datetime(walking_track_area_m2['time'], format=format)
walking_track_area_m2=walking_track_area_m2.set_index(pd.DatetimeIndex(walking_track_area_m2['date_time']))
del walking_track_area_m2['time']
del walking_track_area_m2['date_time']
# for i in range(0,areaTOTAL_cases[:,1].size-1):
#     ax5.plot(sp_sch.df.index,areaTOTAL_cases[i,:],label=(40+4*i)/100)
ax5.plot(sp_sch.df.index,areaTOTAL,label='Lidar scaning')
ax5.plot(walking_track_area_m2.index,walking_track_area_m2.GPS,'r.',label='Walking track along \nthe water edge')
ax5.plot(walking_track_area_m2.index,walking_track_area_m2.aerial,'b.',label='Aerial images')
ax5.legend(loc='lower right',fontsize=font_legend+4)
ax5.xaxis.set_major_formatter(mdates.DateFormatter('%b/%d'))
ax5.set_xlim(datetime.date(2021, 3, 17), datetime.date(2021, 6, 5))
ax5.grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
ax5.set_xlabel('Time', fontsize=label_fontsize, labelpad=10)
ax5.set_ylabel('Surface area \nof the pond ($\mathregular{m^2}$)', fontsize=label_fontsize, labelpad=10)
plt.xticks(fontsize=tick_fontsize, rotation=0)
plt.yticks(fontsize=tick_fontsize, rotation=0)
plt.rcParams["font.family"] = "Arial"
plt.tight_layout()
plt.savefig('compare_track.png',dpi=300)