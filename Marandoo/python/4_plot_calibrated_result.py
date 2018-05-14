
# this script is used for calibrating load cells
import matplotlib.pylab as pylab
params = {'legend.fontsize': 'x-large',
          'figure.figsize': (10, 5),
         'axes.labelsize': 22,
         'axes.titlesize':'22',
         'xtick.labelsize':'22',
         'ytick.labelsize':'22'}
#         'axes.grid':'linewidth=grid_width,color = '0.5''}
#         'linewidth':lw,'markers.size':ms,'markers.edgewidth':mew}
pylab.rcParams.update(params)

lw=4
ms=3
mew=3.5
grid_width=2
y_fontsize=22
fig, ax = plt.subplots(6,sharex=True,figsize=(12,18))
fig.subplots_adjust(hspace=.10)
fig.subplots_adjust(left=0.15, right=0.98, top=0.97, bottom=0.05)
for i in ax:
  for axis in ['top','bottom','left','right']:
    i.spines[axis].set_linewidth(2)

sch_name='Marandoo_first'
ax[0].plot(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.cum_evap_scale1*constants.m2mm,'o',color='red'  ,markersize=ms,markeredgewidth=mew, markeredgecolor='red'  ,label='Basin 1',markevery=1)
ax[0].plot(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.cum_evap_scale2*constants.m2mm,'s',color='green',markersize=ms,markeredgewidth=mew, markeredgecolor='green',label='Basin 2',markevery=2)
ax[0].plot(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.cum_evap_scale3*constants.m2mm,'v',color='cyan' ,markersize=ms,markeredgewidth=mew, markeredgecolor='cyan' ,label='Basin 3',markevery=3)
sch_name='Marandoo_third'
ax[0].plot(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.cum_evap_scale1*constants.m2mm,'o',color='brown'       ,markersize=ms,markeredgewidth=mew, markeredgecolor='brown',label='Basin 4',markevery=3)
sch_name='Marandoo_second'
ax[0].plot(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.cum_evap_scale2*constants.m2mm,'s',color='black'       ,markersize=ms,markeredgewidth=mew, markeredgecolor='black',label='Basin 5',markevery=4)
ax[0].plot(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.cum_evap_scale3*constants.m2mm,'v',color='blue'       ,markersize=ms,markeredgewidth=mew, markeredgecolor='blue',label='Basin 6',markevery=5)

sch_name='Marandoo_first'
ax[1].plot(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.evap_rate_scale1*constants.ms2mmday,'o' ,color='red'      ,markersize=ms,markeredgewidth=mew, markeredgecolor='red',label='Basin 1')
ax[1].plot(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.evap_rate_scale2*constants.ms2mmday,'o' ,color='green'      ,markersize=ms,markeredgewidth=mew, markeredgecolor='green',label='Basin 2')
ax[1].plot(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.evap_rate_scale3*constants.ms2mmday,'o' ,color='cyan'      ,markersize=ms,markeredgewidth=mew, markeredgecolor='cyan',label='Basin 3')
sch_name='Marandoo_third'
ax[1].plot(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.evap_rate_scale1*constants.ms2mmday,'o' ,color='brown'      ,markersize=ms,markeredgewidth=mew, markeredgecolor='brown',label='Basin 4')
sch_name='Marandoo_second'
ax[1].plot(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.evap_rate_scale2*constants.ms2mmday,'o' ,color='black'      ,markersize=ms,markeredgewidth=mew, markeredgecolor='black',label='Basin 5')
ax[1].plot(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.evap_rate_scale3*constants.ms2mmday,'o' ,color='blue'      ,markersize=ms,markeredgewidth=mew, markeredgecolor='blue',label='Basin 6')

sch_name='Marandoo_first'
ax[2].plot(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.vw_1,'o',color='red',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='red',label='Moisture 1')
ax[2].plot(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.vw_2,'o',color='green',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='green',label='Moisture 2')
ax[2].plot(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.vw_3,'o',color='cyan',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='cyan',label='Moisture 3')
sch_name='Marandoo_third'
ax[2].plot(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.vw_1,'o',color='brown',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='Moisture 4')
sch_name='Marandoo_second'
ax[2].plot(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.vw_2,'o',color='black',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='black',label='Moisture 5')
ax[2].plot(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.vw_3,'o',color='blue',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='blue',label='Moisture 6')


sch_name='Marandoo_first'
ax[3].plot(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.starttemp_c_1,'o',color='red',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='red',label='Suction 1')
ax[3].plot(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.starttemp_c_2,'o',color='green',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='green',label='Suction 2')
ax[3].plot(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.starttemp_c_3,'o',color='cyan',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='cyan',label='Suction 3')
sch_name='Marandoo_third'
ax[3].plot(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.starttemp_c_1,'o',color='brown',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='Suction 4')
sch_name='Marandoo_second'
ax[3].plot(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.starttemp_c_2,'o',color='black',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='black',label='Suction 5')
ax[3].plot(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.starttemp_c_3,'o',color='blue',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='blue',label='Suction 6')

sch_name='Marandoo_first'
ax[4].plot(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.deltat_c_1, 'o',color='red',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='red',label='Suction 1')
ax[4].plot(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.deltat_c_2, 'o',color='green',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='green',label='Suction 2')
ax[4].plot(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.deltat_c_3, 'o',color='cyan',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='cyan',label='Suction 3')
sch_name='Marandoo_third'
ax[4].plot(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.deltat_c_1, 'o',color='brown',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='Suction 4')
sch_name='Marandoo_second'
ax[4].plot(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.deltat_c_2, 'o',color='black',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='black',label='Suction 5')
ax[4].plot(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.deltat_c_3, 'o',color='blue',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='blue',label='Suction 6')

sch_name='Marandoo_first'
ax[5].plot(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.sat_scale1, 'o',color='red',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='red',label='Suction 1')
ax[5].plot(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.sat_scale2, 'o',color='green',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='green',label='Suction 2')
ax[5].plot(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.sat_scale3, 'o',color='cyan',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='cyan',label='Suction 3')
sch_name='Marandoo_third'
ax[5].plot(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.sat_scale1, 'o',color='brown',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='Suction 4')
sch_name='Marandoo_second'
ax[5].plot(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.sat_scale2, 'o',color='black',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='black',label='Suction 5')
ax[5].plot(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.sat_scale3, 'o',color='blue',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='blue',label='Suction 6')



ax[0].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
ax[1].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
ax[2].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
ax[3].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
ax[4].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
ax[5].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
#ax[6].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
#ax[7].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')

#ax[2].set_ylim([6,30])
#ax[4].set_ylim([50,105])
ax[0].set_ylabel('CUMULATIVE\nEVAPORATION\n(MM)', fontsize=y_fontsize, labelpad=20)
ax[1].set_ylabel('EVAPORATION\nRATE\n(MM/DAY)', fontsize=y_fontsize, labelpad=20)
ax[2].set_ylabel('DIELECTRIC\n PERMITIVITY', fontsize=y_fontsize, labelpad=20)
ax[3].set_ylabel('TEMPERATURE\n FROM \nSUC. SENSORS ', fontsize=y_fontsize, labelpad=20)
ax[4].set_ylabel('RISE OF TEMP.\n FROM \nSUCT. SENSORS', fontsize=y_fontsize, labelpad=20)
ax[5].set_ylabel('DEG. OF SAT.\n FROM SCALE', fontsize=y_fontsize, labelpad=30)
#ax[6].set_ylabel('NORMORIZED \nTEMP. DIFF. \n(CELSIUS) ', fontsize=y_fontsize, labelpad=20)
#ax[7].set_ylabel('SUCT. FROM \n TEMP. HUMI.\n SENSOR (M)', fontsize=y_fontsize, labelpad=20)

ax[5].set_xlabel('TIME (DAYS)', fontsize=y_fontsize,labelpad=3)
ax[0].set_ylim([-1.02,24])
ax[1].set_ylim([-1.02,13.05])
ax[2].set_ylim([13,29])
ax[3].set_ylim([18.5,26.9])
ax[4].set_ylim([0.6,3.7])
ax[5].set_ylim([1.1,-0.1])

ax[0].legend(bbox_to_anchor=(.8, 0.9), loc=2, borderaxespad=0.,fontsize=18,handletextpad=0.13,labelspacing=0.05)
ax[1].legend(bbox_to_anchor=(.8, 0.85), loc=2, borderaxespad=0.,fontsize=18,handletextpad=0.13,labelspacing=0.05)
ax[2].legend(bbox_to_anchor=(.77, 0.99 ), loc=2, borderaxespad=0.,fontsize=18,handletextpad=0.13,labelspacing=0.05)
ax[3].legend(bbox_to_anchor=(.8, 0.9), loc=2, borderaxespad=0.,fontsize=18,handletextpad=0.13,labelspacing=0.05)
ax[4].legend(bbox_to_anchor=(.8, 0.9 ), loc=2, borderaxespad=0.,fontsize=18,handletextpad=0.13,labelspacing=0.05)
ax[5].legend(bbox_to_anchor=(.8, 0.7 ), loc=2, borderaxespad=0.,fontsize=18,handletextpad=0.13,labelspacing=0.05)

ax[0].set_title('(A)',x=0.02,y=0.8)
ax[1].set_title('(B)',x=0.02,y=0.87)
ax[2].set_title('(C)',x=0.02,y=0.6)
ax[3].set_title('(D)',x=0.02,y=0.8)
ax[4].set_title('(E)',x=0.02,y=0.8)
ax[5].set_title('(F)',x=0.02,y=0.8)
#ax[6].set_title('(G)',x=0.02,y=0.8)
#ax[7].set_title('(H)',x=0.02,y=0.8)
plt.show(block=False)


fig.savefig('figure/plot_calibrated_result'+sch_name+'.png', format='png', dpi=500)

