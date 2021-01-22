
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
fig, ax = plt.subplots(5,sharex=True,figsize=(12,16))
fig.subplots_adjust(hspace=.15)


for i in ax:
  for axis in ['top','bottom','left','right']:
    i.spines[axis].set_linewidth(2)

ax[0].plot(sp.df.time_days, sp.df.te/8.5e-3-14000,'ko'       ,markersize=ms,markeredgewidth=mew, markeredgecolor='k',label='load cell A')
ax[0].plot(sp.df.time_days, sp.df.tas606/18.5e-0,'ro'        ,markersize=ms,markeredgewidth=mew, markeredgecolor='r',label='load cell B')
ax[0].plot(sp.df.time_days[200:], sp.df.commercial[200:],'gx',markersize=ms,markeredgewidth=mew, markeredgecolor='g',label='commercial balance')

ax[1].plot(sp.df.time_days, sp.df.mo_7, 'ro',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Suction A')
ax[1].plot(sp.df.time_days, sp.df.mo_8, 'go',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='Suction B')
ax[1].plot(sp.df.time_days, sp.df.mo_9, 'bo',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='b',label='Moisture A')
ax[1].plot(sp.df.time_days, sp.df.mo_10,'ko',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='Moisture B')


ax[2].plot(sp.df.time_days, sp.df.suht_28e5_begin, 'bo',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='b',label='Fred. Suc. A')
ax[2].plot(sp.df.time_days, sp.df.suht_2847_begin, 'ko',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='Fred. Suc. B')
ax[2].plot(sp.df.time_days, sp.df.saltrh_2_tp, 'ro',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Temp.&Hum. A')
ax[2].plot(sp.df.time_days, sp.df.saltrh_3_tp,'go',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='Temp.&Hum. B')

ax[3].plot(sp.df.time_days, sp.df.suht_28e5_peak-sp.df.suht_28e5_begin, 'ro',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Temp. rise of Fred. Suc. A')
ax[3].plot(sp.df.time_days, sp.df.suht_2847_peak-sp.df.suht_2847_begin, 'go',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='Temp. fall of Fred. Suc. A')
ax[3].plot(sp.df.time_days, sp.df.suht_28e5_peak-sp.df.suht_28e5_end, 'bo',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='b',label='Temp. rise of Fred. Suc. A')
ax[3].plot(sp.df.time_days, sp.df.suht_2847_peak-sp.df.suht_2847_end, 'ko',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='Temp. fall of Fred. Suc. B')

ax[4].plot(sp.df.time_days, sp.df.saltrh_2_rh, 'ro',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Temp.&Hum. A')
ax[4].plot(sp.df.time_days, sp.df.saltrh_3_rh,'go',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='Temp.&Hum. B')

#for sch in sp_sch:
#    sp_sch[sch]['te_fit']=np.polyfit(sp_sch[sch]['df']['commercial'],sp_sch[sch]['df']['te'],1)
#    sp_sch[sch]['tas606_fit']=np.polyfit(sp_sch[sch]['df']['commercial'],sp_sch[sch]['df']['tas606'],1)
#legend_string_second_te="%.3e" % sp_sch['coal_second']['te_fit'][0] + ' * x +' "%.3e" % sp_sch['coal_second']['te_fit'][1]
#legend_string_second_tas606="%.3e" % sp_sch['coal_second']['tas606_fit'][0] + ' * x +' "%.3e" % sp_sch['coal_second']['tas606_fit'][1]
#legend_string_third_te="%.3e" % sp_sch['coal_third']['te_fit'][0] + ' * x +' "%.3e" % sp_sch['coal_third']['te_fit'][1]
#legend_string_third_tas606="%.3e" % sp_sch['coal_third']['tas606_fit'][0] + ' * x +' "%.3e" % sp_sch['coal_third']['tas606_fit'][1]
#
#
#ax[0].plot(sp_sch['coal_second']['df']['commercial'], sp_sch['coal_second']['df']['commercial']*sp_sch['coal_second']['te_fit'][0]
#    +sp_sch['coal_second']['te_fit'][1]  ,'r-',linewidth=lw,label=legend_string_second_te)
#ax[0].plot(sp_sch['coal_third']['df']['commercial'], sp_sch['coal_third']['df']['commercial']*sp_sch['coal_third']['te_fit'][0]
#    +sp_sch['coal_third']['te_fit'][1]  ,'b-',linewidth=lw,label=legend_string_third_te)
#ax[0].plot(sp_sch['coal_second']['df']['commercial'], sp_sch['coal_second']['df']['te'],'k+',
#    linewidth=lw,markersize=ms,markeredgewidth=mew,label='experiment 2')
#ax[0].plot(sp_sch['coal_third']['df']['commercial'], sp_sch['coal_third']['df']['te'],'kx', 
#    linewidth=lw,markersize=ms,markeredgewidth=mew,label='experiment 3')
#ax[0].set_title('(A)',x=0.03,y=1.03)
#
#
#ax[1].plot(sp_sch['coal_second']['df']['commercial'], sp_sch['coal_second']['df']['commercial']*sp_sch['coal_second']['tas606_fit'][0]
#    +sp_sch['coal_second']['tas606_fit'][1]  ,'r-',linewidth=lw,label=legend_string_second_tas606)
#ax[1].plot(sp_sch['coal_third']['df']['commercial'], sp_sch['coal_third']['df']['commercial']*sp_sch['coal_third']['tas606_fit'][0]
#    +sp_sch['coal_third']['tas606_fit'][1]  ,'b-',linewidth=lw,label=legend_string_third_tas606)
#ax[1].plot(sp_sch['coal_second']['df']['commercial'], sp_sch['coal_second']['df']['tas606'],'k+', 
#    linewidth=lw,markersize=ms,markeredgewidth=mew,label='experiment 2')
#ax[1].plot(sp_sch['coal_third']['df']['commercial'], sp_sch['coal_third']['df']['tas606'],'kx', 
#    linewidth=lw,markersize=ms,markeredgewidth=mew,label='experiment 3')
## show grid with gray color
ax[0].grid(linewidth=grid_width,color = '0.5')
ax[1].grid(linewidth=grid_width,color = '0.5')
ax[2].grid(linewidth=grid_width,color = '0.5')
ax[3].grid(linewidth=grid_width,color = '0.5')
ax[4].grid(linewidth=grid_width,color = '0.5')

ax[0].set_ylabel('WEIGHT (G)', fontsize=y_fontsize, labelpad=5)
ax[1].set_ylabel('RAW READING FROM \n DIELECTRIC SENSORS ', fontsize=y_fontsize, labelpad=5)
ax[2].set_ylabel('TEMP. (CELSIUS) ', fontsize=y_fontsize, labelpad=5)
ax[3].set_ylabel('TEMP. DIFF. (CELSIUS) ', fontsize=y_fontsize, labelpad=5)
ax[4].set_ylabel('RELATIVE HUMIDITY', fontsize=y_fontsize, labelpad=5)
ax[4].set_xlabel('TIME (DAYS)', fontsize=y_fontsize,labelpad=20)
#ax[1].set_ylim([155000,230000])
ax[0].legend(bbox_to_anchor=(.03, 0.99), loc=2, borderaxespad=0.,fontsize=10)
ax[1].legend(bbox_to_anchor=(.85, 0.5), loc=2, borderaxespad=0.,fontsize=10)
ax[2].legend(bbox_to_anchor=(.04, 0.53), loc=2, borderaxespad=0.,fontsize=10)
ax[3].legend(bbox_to_anchor=(.01, 0.99), loc=2, borderaxespad=0.,fontsize=10)
ax[4].legend(bbox_to_anchor=(.01, 0.3), loc=2, borderaxespad=0.,fontsize=10)
ax[0].set_title('(A)',x=0.02,y=1.0)
ax[1].set_title('(B)',x=0.02,y=1.0)
ax[2].set_title('(C)',x=0.02,y=1.0)
ax[3].set_title('(D)',x=0.02,y=1.0)
ax[4].set_title('(E)',x=0.02,y=1.0)
plt.show(block=False)


fig.savefig('plot_raw_result.png', format='png', dpi=500)
