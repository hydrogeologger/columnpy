import matplotlib
import matplotlib.image as image

# Force matplotlib to not use any Xwindows backend.
matplotlib.use('Agg')
import matplotlib.pyplot as plt
    
sch_name='column_camellia'
    
import matplotlib.pylab as pylab
lw=2
ms=0.5
mew=3
grid_width=2
y_fontsize=12

idx_im=886
params = {'legend.fontsize': 11,
          'figure.figsize': (10, 5),
         'axes.labelsize': 11,
         'axes.titlesize':'11',
         'xtick.labelsize':'11',
         'ytick.labelsize':'11',
         'font.weight':'bold',
         'axes.labelweight':'bold',
         'lines.linewidth':2}#,
pylab.rcParams.update(params)

lw=2
ms=6
mew=2
grid_width=2
y_fontsize=11
fig, ax = plt.subplots(3,sharex=True,figsize=(9,7))
fig.subplots_adjust(hspace=.10)
fig.subplots_adjust(left=0.11, right=0.86, top=0.97, bottom=0.08)
    
for i in ax:
  for axis in ['top','bottom','left','right']:
    i.spines[axis].set_linewidth(2)


ax[0].plot(sp_sch[sch_name].df.time_days[:idx_im]+10, sp_sch[sch_name].df.ir_up[:idx_im]/100.0,'-',color='maroon'       ,markersize=ms-7,markeredgewidth=mew, markeredgecolor='brown',label='up',markevery=1)
ax[0].set_ylim([-2,19])
mark_every=30;interval_array=3

ax[1].plot(sp_sch[sch_name].df.time_days[:idx_im:interval_array]+10, sp_sch[sch_name].df.mo0[:idx_im:interval_array],'-',color='firebrick',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='1 cm',markevery=mark_every)
ax[1].plot(sp_sch[sch_name].df.time_days[:idx_im:interval_array]+10, sp_sch[sch_name].df.mo7[:idx_im:interval_array],'-',color='maroon',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='2 cm',markevery=mark_every,ms=12)
ax[1].plot(sp_sch[sch_name].df.time_days[:idx_im:interval_array]+10, sp_sch[sch_name].df.mo2[:idx_im:interval_array],'-',color='sienna',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='6 cm',markevery=mark_every,ms=12)
ax[1].plot(sp_sch[sch_name].df.time_days[:idx_im:interval_array]+10, sp_sch[sch_name].df.mo4[:idx_im:interval_array],'-',color='peru',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='11cm',markevery=mark_every,ms=12)
ax[1].plot(sp_sch[sch_name].df.time_days[:idx_im:interval_array]+10, sp_sch[sch_name].df.mo1[:idx_im:interval_array],'-',color='olive',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='20cm',ms=12,markevery=mark_every)
ax[1].plot(sp_sch[sch_name].df.time_days[:idx_im:interval_array]+10, sp_sch[sch_name].df.mo9[:idx_im:interval_array],'-',color='darkblue',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='85cm',markevery=mark_every,ms=12)
ax[1].set_ylim([-0.1,1.1])

mark_every=1
ax[2].plot(sp_sch[sch_name].df.time_days[:idx_im]+10, sp_sch[sch_name].df.t26_begin[:idx_im],'-',color='firebrick',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='1 cm',markevery=mark_every)
ax[2].plot(sp_sch[sch_name].df.time_days[:idx_im]+10, sp_sch[sch_name].df.t45_begin[:idx_im],'-',color='maroon',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='2 cm',ms=12,markevery=mark_every)
ax[2].plot(sp_sch[sch_name].df.time_days[:idx_im]+10, sp_sch[sch_name].df.t57_begin[:idx_im],'-',color='sienna',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='6 cm',markevery=mark_every,ms=12)
ax[2].plot(sp_sch[sch_name].df.time_days[:idx_im]+10, sp_sch[sch_name].df.t7b_begin[:idx_im],'-',color='peru',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='11cm',markevery=mark_every,ms=12)
ax[2].plot(sp_sch[sch_name].df.time_days[:idx_im]+10, sp_sch[sch_name].df.te2_begin[:idx_im],'-',color='olive',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='20cm',markevery=mark_every,ms=12)
ax[2].plot(sp_sch[sch_name].df.time_days[:idx_im]+10, sp_sch[sch_name].df.tfb_begin[:idx_im],'-',color='darkblue',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='b',label='85cm',markevery=mark_every,ms=12)
ax[2].set_ylim([7,53])
ax[0].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
ax[1].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
ax[2].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')

#ax[0].set_ylim([-1,11])
#ax[1].set_ylim([-0.1,1.1])
#ax[2].set_ylim([-50,580])
#ax[3].set_ylim([8,38])
#ax[0].set_ylabel('CUMULATIVE\nEVAPORATION\n(mm)', fontsize=y_fontsize, labelpad=20)
ax[0].set_ylabel('EVAPORATION RATE\nFROM WEATHER \nSTATION(mm/day)', fontsize=y_fontsize, labelpad=10)
ax[1].set_ylabel('DEGREE OF\nSATURATION', fontsize=y_fontsize, labelpad=10)
#ax[2].set_ylabel('DEGREE OF SAT.\nBY DIELECTRIC\nMOISTURE\nSENSOR', fontsize=y_fontsize, labelpad=10)
#ax[2].set_ylabel('SUCTION (kPa)', fontsize=y_fontsize, labelpad=10)
ax[2].set_ylabel('TEMPERATURE\n($^\circ$C)', fontsize=y_fontsize, labelpad=10)
#ax[5].set_ylabel('TEMPERATURE\n($^\circ$c)', fontsize=y_fontsize, labelpad=20)
#ax[6].set_ylabel('NORMALIZED\nRISE OF\nTEMPERATURE', fontsize=y_fontsize, labelpad=10)
#ax[7].set_ylabel('SUCTION BY\nTEMPERATURE\nHUMIDITY\n SENSOR (m)', fontsize=y_fontsize, labelpad=10)

ax[2].set_xlabel('TIME (days)', fontsize=y_fontsize,labelpad=3)
ax[0].set_xlim([0,45])
#ax[3].set_xlabel('TIME (days)', fontsize=y_fontsize,labelpad=3)
#ax[0].set_ylim([-0.2,35])
#ax[0].set_ylim([-1,13])
#ax[1].set_ylim([-0.09,0.64])
##ax[2].set_ylim([200,650])
#ax[2].set_ylim([1e-0,1e8])
#ax[5].set_ylim([8,27])
#ax[6].set_ylim([-0.1,1.1])
#ax[7].set_ylim([9,40000])
ax[1].legend(bbox_to_anchor=(1.09, 0.5),  loc='center' , borderaxespad=0.,fontsize=12,handletextpad=0.03,labelspacing=0.02,ncol=1,columnspacing=0.4)
ax[2].legend(bbox_to_anchor=(1.09, 0.5 ), loc='center' , borderaxespad=0.,fontsize=12,handletextpad=0.03,labelspacing=0.02,ncol=1,columnspacing=0.4)
#ax[3].legend(bbox_to_anchor=(.01, 0.6 ), loc=2, borderaxespad=0.)
#ax[7].legend(bbox_to_anchor=(.1, 0.55 ), loc=2, borderaxespad=0.)
#ax[0].set_title('(A)',x=0.04,y=0.86,fontweight='bold')
#ax[1].set_title('(B)',x=0.04,y=0.86,fontweight='bold')
#ax[2].set_title('(C)',x=0.04,y=0.86,fontweight='bold')
#ax[3].set_title('(D)',x=0.04,y=0.85,fontweight='bold')
#ax[3].set_title('(D)',x=0.04,y=0.75,fontweight='bold')
#ax[4].set_title('(E)',x=0.03,y=0.75,fontweight='bold')
#ax[5].set_title('(F)',x=0.03,y=0.75,fontweight='bold')
#ax[6].set_title('(G)',x=0.03,y=0.75,fontweight='bold')
#ax[7].set_title('(H)',x=0.03,y=0.75,fontweight='bold')
#xlim=[sp_sch[sch_name].df.time_days[0],sp_sch[sch_name].df.time_days[len(sp_sch[sch_name].df)-1]]
#ax[0].set_xlim(xlim)
#ax[0].set_xlim([10,45])
#ax[1].set_xlim(xlim)
##ax[2].set_xlim(xlim)
#ax[2].set_xlim(xlim)
#ax[4].set_xlim(xlim)
#ax[5].set_xlim(xlim)
#ax[6].set_xlim(xlim)
#ax[7].set_xlim(xlim)
#ax[2].set_xticklabels([])
#ax[3].set_xticklabels([])
#ax[4].set_xticklabels([])
#ax[5].set_xticklabels([])
#ax[6].set_xticklabels([])
#plt.text(0.5, 0.5, 's', fontsize=18)
#plt.text(-100,1000, 'Moisture\nsensor 1', fontsize=18,color='b')
#ax_img.annotate('Moisture\nsensor A',
#            xy=(300, 1000),
#            xytext=(0.51, 0.6),    # fraction, fraction
#            textcoords='figure fraction',
#            arrowprops=dict(facecolor='yellow', shrink=0.05),
#            horizontalalignment='left',
#            verticalalignment='bottom',fontsize=18
#            )
#ax_img.annotate('Moisture\nsensor B',
#            xy=(200, 1200),
#            xytext=(0.51, 0.5),    # fraction, fraction
#            textcoords='figure fraction',
#            arrowprops=dict(facecolor='yellow', shrink=0.05),
#            horizontalalignment='left',
#            verticalalignment='bottom',fontsize=18
#            )
#ax_img.annotate('Suction\nsensor A',
#            xy=(300, 1400),
#            xytext=(0.51, 0.4),    # fraction, fraction
#            textcoords='figure fraction',
#            arrowprops=dict(facecolor='yellow', shrink=0.05),
#            horizontalalignment='left',
#            verticalalignment='bottom',fontsize=18
#            )
#ax_img.annotate('Suction\nsensor B',
#            xy=(400, 1600),
#            xytext=(0.51, 0.3),    # fraction, fraction
#            textcoords='figure fraction',
#            arrowprops=dict(facecolor='yellow', shrink=0.05),
#            horizontalalignment='left',
#            verticalalignment='bottom',fontsize=18
#            )


#plt.show(block=False)


fig.savefig('figure/plot_camellia_'+sch_name+'.png', format='png', dpi=600)
plt.close()
sp_sch[sch_name].df.to_csv('output_data/'+sch_name+'.csv', sep=',', encoding='utf-8')

