
# this script is used for calibrating load cells
import matplotlib
import matplotlib.image as image
import matplotlib.pylab as pylab
lw=1.5
ms=1
mew=3
grid_width=2
y_fontsize=12

params = {'legend.fontsize': 4,
          'figure.figsize': (10, 5),
         'axes.labelsize': 11,
         'axes.titlesize':'11',
         'xtick.labelsize':'11',
         'ytick.labelsize':'11',
         'font.weight':'bold',
         'font.sans-serif':'Arial',
         'axes.labelweight':'bold',
         'lines.linewidth':2}#,
#         'title.fontweight':'bold'}

#         'axes.grid':'linewidth=grid_width,color = '0.5''}
#         'linewidth':lw,'markers.size':ms,'markers.edgewidth':mew}
pylab.rcParams.update(params)

lw=2
ms=6
mew=2
grid_width=2
y_fontsize=11
fig, ax = plt.subplots(4,sharex=True,figsize=(9,9))
fig.subplots_adjust(hspace=.10)
fig.subplots_adjust(left=0.17, right=0.89, top=0.97, bottom=0.05)

for i in ax:
  for axis in ['top','bottom','left','right']:
    i.spines[axis].set_linewidth(2)

sch_name='bacteria_first'
ax[0].plot(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.cum_evap_scale1*constants.m2mm,'o',color='brown'  ,markersize=ms,markeredgewidth=mew, markeredgecolor='brown'  ,label='Basin1',markevery=1)
ax[0].plot(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.cum_evap_scale2*constants.m2mm,'s',color='orange',markersize=ms,markeredgewidth=mew, markeredgecolor='orange',label='Basin2',markevery=2)
sch_name='bacteria_second'
ax[0].plot(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.cum_evap_scale1*constants.m2mm,'o',color='brown',markersize=ms,markeredgewidth=mew, markeredgecolor='brown',markevery=1)
ax[0].plot(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.cum_evap_scale2*constants.m2mm,'s',color='orange',markersize=ms,markeredgewidth=mew, markeredgecolor='orange',markevery=2)
sch_name='bacteria_third'
ax[0].plot(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.cum_evap_scale1*constants.m2mm,'o',color='brown',markersize=ms,markeredgewidth=mew, markeredgecolor='brown',markevery=1)
ax[0].plot(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.cum_evap_scale2*constants.m2mm,'s',color='orange',markersize=ms,markeredgewidth=mew, markeredgecolor='orange',markevery=2)

sch_name='bacteria_first'
ax[1].plot(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.evap_rate_scale1*constants.ms2mmday,'o',color='brown'  ,markersize=ms,markeredgewidth=mew, markeredgecolor='brown'  ,label='Basin1',markevery=1)
ax[1].plot(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.evap_rate_scale2*constants.ms2mmday,'s',color='orange',markersize=ms,markeredgewidth=mew, markeredgecolor='orange',label='Basin2',markevery=2)
sch_name='bacteria_second'
ax[1].plot(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.evap_rate_scale1*constants.ms2mmday,'o',color='brown',markersize=ms,markeredgewidth=mew, markeredgecolor='brown',markevery=1)
ax[1].plot(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.evap_rate_scale2*constants.ms2mmday,'s',color='orange',markersize=ms,markeredgewidth=mew, markeredgecolor='orange',markevery=2)
sch_name='bacteria_third'
ax[1].plot(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.evap_rate_scale1*constants.ms2mmday,'o',color='brown',markersize=ms,markeredgewidth=mew, markeredgecolor='brown',markevery=1)
ax[1].plot(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.evap_rate_scale1*constants.ms2mmday,'s',color='orange',markersize=ms,markeredgewidth=mew, markeredgecolor='orange',markevery=2)


sch_name='bacteria_first'
ax[2].plot(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.mmo0,'o',color='red',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='red',label='Mo1 (nobact)')
ax[2].plot(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.mmo1,'o',color='green',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='green',label='Mo2 (nobact)')
ax[2].plot(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.mmo2,'o',color='cyan',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='cyan',label='Mo3 (nobact)')
ax[2].plot(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.mmo3,'o',color='gold',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='gold',label='Mo4 (bact)')
ax[2].plot(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.mmo4,'o',color='black',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='black',label='Mo5 (bact)')
ax[2].plot(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.mmo5,'o',color='blue',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='blue',label='Mo6 (bact)')
ax[2].plot(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.sat_scale1,'o',color='brown',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='Basin1')
ax[2].plot(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.sat_scale2,'o',color='orange',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='orange',label='Basin2')
sch_name='bacteria_second'
ax[2].plot(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.mmo0,'o',color='red',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='red')
ax[2].plot(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.mmo1,'o',color='green',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='green')
ax[2].plot(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.mmo2,'o',color='cyan',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='cyan')
ax[2].plot(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.mmo3,'o',color='gold',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='gold')
ax[2].plot(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.mmo4,'o',color='black',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='black')
ax[2].plot(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.mmo5,'o',color='blue',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='blue')
ax[2].plot(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.sat_scale1,'o',color='brown',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown')
ax[2].plot(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.sat_scale2,'o',color='orange',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='orange')
sch_name='bacteria_third'
ax[2].plot(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.mmo0,'o',color='red',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='red')
ax[2].plot(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.mmo1,'o',color='green',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='green')
ax[2].plot(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.mmo2,'o',color='cyan',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='cyan')
ax[2].plot(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.mmo3,'o',color='gold',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='gold')
ax[2].plot(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.mmo4,'o',color='black',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='black')
ax[2].plot(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.mmo5,'o',color='blue',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='blue')
ax[2].plot(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.sat_scale1,'o',color='brown',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown')
ax[2].plot(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.sat_scale2,'o',color='orange',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='orange')

sch_name='bacteria_first'
ax[3].semilogy(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.suction0,'o',color='red',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='red',label='Suc.1 (nobact)')
ax[3].semilogy(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.suction1,'o',color='green',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='green',label='Suc.2 (nobact)')
ax[3].semilogy(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.suction2,'o',color='cyan',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='cyan',label='Suc.3 (nobact)')
ax[3].semilogy(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.suction3,'o',color='gold',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='gold',label='Suc.4 (bact)')
ax[3].semilogy(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.suction4,'o',color='black',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='black',label='Suc.5 (bact)')
ax[3].semilogy(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.suction5,'o',color='blue',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='blue',label='Suc.6 (bact)')
ax[3].semilogy(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.suc_scale1,'o',color='brown',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='Basin1')
ax[3].semilogy(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.suc_scale2,'o',color='orange',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='orange',label='Basin2')
sch_name='bacteria_second'
ax[3].semilogy(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.suc_scale1,'o',color='brown',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown')
ax[3].semilogy(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.suc_scale2,'o',color='orange',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='orange')
ax[3].semilogy(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.suction0,'o',color='red',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='red')
ax[3].semilogy(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.suction1,'o',color='green',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='green')
ax[3].semilogy(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.suction2,'o',color='cyan',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='cyan')
ax[3].semilogy(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.suction3,'o',color='gold',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='gold')
ax[3].semilogy(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.suction4,'o',color='black',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='black')
ax[3].semilogy(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.suction5,'o',color='blue',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='blue')
sch_name='bacteria_third'
ax[3].semilogy(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.suc_scale1,'o',color='brown',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown')
ax[3].semilogy(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.suc_scale2,'o',color='orange',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='orange')
ax[3].semilogy(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.suction0,'o',color='red',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='red')
ax[3].semilogy(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.suction1,'o',color='green',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='green')
ax[3].semilogy(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.suction2,'o',color='cyan',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='cyan')
ax[3].semilogy(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.suction3,'o',color='gold',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='gold')
ax[3].semilogy(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.suction4,'o',color='black',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='black')
ax[3].semilogy(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.suction5,'o',color='blue',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='blue')

#sch_name='bacteria_first'
#ax[4].plot(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.sat_scale1,'o',color='brown',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='Basin1')
#ax[4].plot(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.sat_scale2,'o',color='orange',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='orange',label='Basin2')
#sch_name='bacteria_second'
#ax[4].plot(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.sat_scale1,'o',color='brown',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown')
#ax[4].plot(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.sat_scale2,'o',color='orange',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='orange')
#sch_name='bacteria_third'
#ax[4].plot(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.sat_scale1,'o',color='brown',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown')
#ax[4].plot(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.sat_scale2,'o',color='orange',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='orange')

#sch_name='bacteria_first'
#ax[5].plot(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.suction0,'o',color='red',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='red',label='Suction 1')
#ax[5].plot(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.suction1,'o',color='green',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='green',label='Suction 2')
#ax[5].plot(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.suction2,'o',color='cyan',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='cyan',label='Suction 3')
#ax[5].plot(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.suction3,'o',color='brown',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='Suction 4')
#ax[5].plot(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.suction4,'o',color='black',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='black',label='Suction 5')
#ax[5].plot(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.suction5,'o',color='blue',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='blue',label='Suction 6')
#sch_name='bacteria_second'
#ax[5].plot(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.suction0,'o',color='red',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='red')
#ax[5].plot(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.suction1,'o',color='green',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='green')
#ax[5].plot(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.suction2,'o',color='cyan',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='cyan')
#ax[5].plot(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.suction3,'o',color='brown',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown')
#ax[5].plot(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.suction4,'o',color='black',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='black')
#ax[5].plot(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.suction5,'o',color='blue',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='blue')
#sch_name='bacteria_third'
#ax[5].plot(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.suction0,'o',color='red',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='red')
#ax[5].plot(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.suction1,'o',color='green',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='green')
#ax[5].plot(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.suction2,'o',color='cyan',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='cyan')
#ax[5].plot(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.suction3,'o',color='brown',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown')
#ax[5].plot(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.suction4,'o',color='black',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='black')
#ax[5].plot(sp_sch[sch_name].df['date_time'], sp_sch[sch_name].df.suction5,'o',color='blue',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='blue')

#sch_name='Marandoo_first'
#ax[4].plot(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.deltat_c_1, 'o',color='red',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='red',label='Suction 1')
#ax[4].plot(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.deltat_c_2, 'o',color='green',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='green',label='Suction 2')
#ax[4].plot(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.deltat_c_3, 'o',color='cyan',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='cyan',labe:q l='Suction 3')
#sch_name='Marandoo_third'
#ax[4].plot(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.deltat_c_1, 'o',color='brown',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='Suction 4')
#sch_name='Marandoo_second'
#ax[4].plot(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.deltat_c_2, 'o',color='black',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='black',label='Suction 5')
#ax[4].plot(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.deltat_c_3, 'o',color='blue',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='blue',label='Suction 6')
#
#sch_name='Marandoo_first'
#ax[5].plot(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.sat_scale1, 'o',color='red',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='red',label='Suction 1')
#ax[5].plot(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.sat_scale2, 'o',color='green',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='green',label='Suction 2')
#ax[5].plot(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.sat_scale3, 'o',color='cyan',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='cyan',label='Suction 3')
#sch_name='Marandoo_third'
#ax[5].plot(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.sat_scale1, 'o',color='brown',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='Suction 4')
#sch_name='Marandoo_second'
#ax[5].plot(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.sat_scale2, 'o',color='black',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='black',label='Suction 5')
#ax[5].plot(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.sat_scale3, 'o',color='blue',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='blue',label='Suction 6')



ax[0].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
ax[1].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
ax[2].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
ax[3].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
#ax[4].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
#ax[5].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
#ax[6].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
#ax[7].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')

#ax[2].set_ylim([6,30])
#ax[4].set_ylim([50,105])
ax[0].set_ylabel('CUMULATIVE\nEVAPORATION\n (mm)', fontsize=y_fontsize, labelpad=20)
ax[1].set_ylabel('EVAPORATION\nRATE\n(mm/Day)', fontsize=y_fontsize, labelpad=20)
ax[2].set_ylabel('DEG. OF SAT.', fontsize=y_fontsize, labelpad=20)
ax[3].set_ylabel('SUCTION\n(kPa)', fontsize=y_fontsize, labelpad=20)
#ax[4].set_ylabel('RISE OF TEMP.\n FROM \nSUCT. SENSORS', fontsize=y_fontsize, labelpad=20)
#ax[4].set_ylabel('DEG. OF SAT.\n FROM SCALE', fontsize=y_fontsize, labelpad=20)
#ax[5].set_ylabel('SUCTION\nFROM SENSOR\n(kPa) ', fontsize=y_fontsize, labelpad=20)
#ax[7].set_ylabel('SUCT. FROM \n TEMP. HUMI.\n SENSOR (M)', fontsize=y_fontsize, labelpad=20)

ax[3].set_xlabel('DATE', fontsize=y_fontsize,labelpad=3)
ax[0].set_ylim([0,30])
ax[1].set_ylim([0,7])
ax[2].set_ylim([-0.1,1.2])
ax[3].set_ylim([1,2.5e6])
#ax[4].set_ylim([1.1,-0.1])
#ax[5].set_ylim([1,1.2e6])

ax[0].legend(bbox_to_anchor=(1.07, 0.5 ), loc='center', borderaxespad=0.,fontsize=9,handletextpad=0.03,labelspacing=0.02,ncol=1,columnspacing=0.4)
ax[1].legend(bbox_to_anchor=(1.07, 0.5 ), loc='center', borderaxespad=0.,fontsize=9,handletextpad=0.03,labelspacing=0.02,ncol=1,columnspacing=0.4)
ax[2].legend(bbox_to_anchor=(1.07, 0.5 ), loc='center', borderaxespad=0.,fontsize=9,handletextpad=0.03,labelspacing=0.02,ncol=1,columnspacing=0.4)
ax[3].legend(bbox_to_anchor=(1.07, 0.5 ), loc='center', borderaxespad=0.,fontsize=9,handletextpad=0.03,labelspacing=0.02,ncol=1,columnspacing=0.4)
#ax[4].legend(bbox_to_anchor=(1.07, 0.5 ), loc='center', borderaxespad=0.,fontsize=9,handletextpad=0.03,labelspacing=0.02,ncol=1,columnspacing=0.4)
#ax[5].legend(bbox_to_anchor=(1.07, 0.5 ), loc='center', borderaxespad=0.,fontsize=9,handletextpad=0.03,labelspacing=0.02,ncol=1,columnspacing=0.4)
#ax[0].set_title('(A)',x=0.02,y=0.8)
#ax[1].set_title('(B)',x=0.02,y=0.87)
#ax[2].set_title('(C)',x=0.02,y=0.6)
#ax[3].set_title('(D)',x=0.02,y=0.8)
#ax[4].set_title('(E)',x=0.02,y=0.8)
#ax[5].set_title('(F)',x=0.02,y=0.8)
#ax[6].set_title('(G)',x=0.02,y=0.8)
#ax[7].set_title('(H)',x=0.02,y=0.8)
plt.show(block=False)


sch_name='bacteria_first'
sp_sch[sch_name].df.to_csv('output_data/'+sch_name+'.csv')
sch_name='bacteria_second'
sp_sch[sch_name].df.to_csv('output_data/'+sch_name+'.csv')
sch_name='bacteria_third'
sp_sch[sch_name].df.to_csv('output_data/'+sch_name+'.csv')


fig.savefig('figure/plot_bacteria'+sch_name+'.png', format='png', dpi=500)

