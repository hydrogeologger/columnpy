
# this script is used for calibrating load cells
import matplotlib.pylab as pylab
params = {'legend.fontsize': 'x-large',
          'figure.figsize': (10, 5),
         'axes.labelsize': 10,
         'axes.titlesize':'large',
         'xtick.labelsize':'12',
         'ytick.labelsize':'12'}
#         'axes.grid':'linewidth=grid_width,color = '0.5''}
#         'linewidth':lw,'markers.size':ms,'markers.edgewidth':mew}
pylab.rcParams.update(params)

lw=4
ms=3
mew=1.5
grid_width=2
y_fontsize=12
fig, ax = plt.subplots(8,sharex=True,figsize=(12,18))
fig.subplots_adjust(hspace=.10)
sch_name='redmud_first'
fig.subplots_adjust(left=0.15, right=0.98, top=0.97, bottom=0.03)
for i in ax:
  for axis in ['top','bottom','left','right']:
    i.spines[axis].set_linewidth(2)

ax[0].plot(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.cum_evap_commercial*constants.m2mm,'o',color='brown'       ,markersize=ms,markeredgewidth=mew, markeredgecolor='brown',label='load cell')

ax[1].plot(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.evap_rate_commercial*constants.ms2mmday,'o' ,color='brown'      ,markersize=ms,markeredgewidth=mew, markeredgecolor='brown',label='load cell')

ax[2].plot(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.sat_commercial,'o',color='brown',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='Moisture B')

ax[3].plot(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.mo_9 ,'ko',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='Moisture A')
ax[3].plot(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.mo_10,'o',color='brown',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='Moisture B')

ax[4].plot(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.mo_7, 'ko',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='Dielectric suction A')
ax[4].plot(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.mo_8, 'o',color='brown',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='Dielectric suction B')

ax[5].plot(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.t_2896_begin, 'o',color='brown',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='Fred. Suc. A')

ax[6].plot(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.norm_deltat_2896_heat, 'o',color='brown',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='Fred. Suc. A')

ax[7].semilogy(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.saltrh_2_suction, 'o',color='brown',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='Temp.&Hum. A')
ax[7].semilogy(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.saltrh_11_suction,'ko',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='Temp.&Hum. B')



ax[0].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
ax[1].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
ax[2].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
ax[3].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
ax[4].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
ax[5].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
ax[6].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
ax[7].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')

#ax[2].set_ylim([6,30])
#ax[4].set_ylim([50,105])
ax[0].set_ylabel('CUMULATIVE\nEVAPORATION\n(MM)', fontsize=y_fontsize, labelpad=20)
ax[1].set_ylabel('EVAPORATION\nRATE\n(MM/DAY)', fontsize=y_fontsize, labelpad=20)
ax[2].set_ylabel('DEGREE\n OF\n SATURATION', fontsize=y_fontsize, labelpad=20)
ax[3].set_ylabel('RAW READING\n FROM DIEL.\n MOIS. SENSORS ', fontsize=y_fontsize, labelpad=20)
ax[4].set_ylabel('RAW READING\n FROM DIEL.\n SUCT. SENSORS ', fontsize=y_fontsize, labelpad=20)
ax[5].set_ylabel('TEMPERATURE \n(CELSIUS) ', fontsize=y_fontsize, labelpad=30)
ax[6].set_ylabel('NORMORIZED \nTEMP. DIFF. \n(CELSIUS) ', fontsize=y_fontsize, labelpad=20)
ax[7].set_ylabel('SUCT. FROM \n TEMP. HUMI.\n SENSOR (M)', fontsize=y_fontsize, labelpad=20)

ax[7].set_xlabel('TIME (DAYS)', fontsize=y_fontsize,labelpad=3)
ax[2].set_ylim([-0.05,1.05])
ax[3].legend(bbox_to_anchor=(.8, 0.5), loc=2, borderaxespad=0.,fontsize=12)
ax[4].legend(bbox_to_anchor=(.7, 0.4 ), loc=2, borderaxespad=0.,fontsize=12)
ax[7].legend(bbox_to_anchor=(.8, 0.4 ), loc=2, borderaxespad=0.,fontsize=12)
ax[0].set_title('(A)',x=0.02,y=0.8)
ax[1].set_title('(B)',x=0.02,y=0.8)
ax[2].set_title('(C)',x=0.02,y=0.8)
ax[3].set_title('(D)',x=0.02,y=0.8)
ax[4].set_title('(E)',x=0.02,y=0.8)
ax[5].set_title('(F)',x=0.02,y=0.8)
ax[6].set_title('(G)',x=0.02,y=0.8)
ax[7].set_title('(H)',x=0.02,y=0.8)
plt.show(block=False)


fig.savefig('plot_calibrated_result'+sch_name+'.png', format='png', dpi=500)

