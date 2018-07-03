import matplotlib
import matplotlib.image as image

# Force matplotlib to not use any Xwindows backend.
#matplotlib.use('Agg')
import matplotlib.pyplot as plt

import glob, os
#os.chdir("/home/chenming/Projects/tailings/area_51_redmud_4cm_photo/")
#img_list=glob.glob('/home/chenming/Projects/tailings/area_51_redmud_4cm_photo/*.jpg')
#for file in glob.glob("*.jpg"):
#    print(file)
sch_name='column_daisy'


import matplotlib.pylab as pylab
lw=2
ms=0.5
mew=3
grid_width=2
y_fontsize=12

params = {'legend.fontsize': 8,
          'figure.figsize': (10, 5),
         'axes.labelsize': 11,
         'axes.titlesize':'11',
         'xtick.labelsize':'11',
         'ytick.labelsize':'11',
         'font.weight':'bold',
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
fig, ax = plt.subplots(4,sharex=True,figsize=(8,9))
fig.subplots_adjust(hspace=.10)
fig.subplots_adjust(left=0.18, right=0.98, top=0.97, bottom=0.08)


    
    
    
    
for i in ax:
  for axis in ['top','bottom','left','right']:
    i.spines[axis].set_linewidth(2)


ax[0].plot(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.ir_up/100.0,'-',color='r'       ,markersize=ms-7,markeredgewidth=mew, markeredgecolor='brown',label='up',markevery=1)
#ax[0].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.ir_down[:idx_im],'o',color='k'       ,markersize=ms,markeredgewidth=mew, markeredgecolor='k',label='down',markevery=3)
mark_every=20
ax[1].plot(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.mo1,'-',color='maroon',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='4 cm',markevery=mark_every)
ax[1].plot(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.mo2,'-',color='peru',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='8 cm',ms=12,markevery=mark_every)
ax[1].plot(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.mo3,'-',color='gold',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='13cm',markevery=mark_every,ms=12)
ax[1].plot(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.mo4,'-',color='olive',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='20cm',markevery=mark_every,ms=12)
ax[1].plot(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.mo5,'-',color='limegreen',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='30cm',markevery=mark_every,ms=12)
ax[1].plot(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.mo7,'-',color='lightblue',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='b',label='60cm',markevery=mark_every,ms=12)
ax[1].plot(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.mo10,'-',color='royalblue',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='85cm',markevery=mark_every,ms=12)


ax[2].plot(sp_sch[sch_name].df.time_days, -sp_sch[sch_name].df.su3,'-',color='r',markersize=ms+4,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='13cm',markevery=mark_every)
ax[2].plot(sp_sch[sch_name].df.time_days, -sp_sch[sch_name].df.su2,'-',color='g',markersize=ms+2,markeredgewidth=mew,fillstyle='none', markeredgecolor='r',label='20cm',markevery=mark_every)
ax[2].plot(sp_sch[sch_name].df.time_days, -sp_sch[sch_name].df.su4,'-',color='b',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='green',label='30cm',markevery=mark_every,ms=12)
ax[2].plot(sp_sch[sch_name].df.time_days, -sp_sch[sch_name].df.su1,'-',color='c',markersize=ms-2,markeredgewidth=mew,fillstyle='full', markeredgecolor='orange',label='60cm',markevery=mark_every,ms=12)

mark_every=1
ax[3].plot(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.tp3,'-',color='r',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='4cm',markevery=mark_every)
ax[3].plot(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.tp2,'-',color='g',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='8cm',ms=12,markevery=mark_every)
ax[3].plot(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.tp4,'-',color='b',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='13cm',markevery=mark_every,ms=12)
ax[3].plot(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.tp1,'-',color='c',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='20cm',markevery=mark_every,ms=12)
ax[3].plot(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.tpa3,'-',color='m',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='30cm',markevery=mark_every,ms=12)
ax[3].plot(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.tpf0,'-',color='k',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='b',label='60cm',markevery=mark_every,ms=12)
ax[3].plot(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.tc,'-',color='brown',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='Weather Station',markevery=mark_every,ms=12)

ax[3].set_axisbelow(True)
ax[0].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
ax[1].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
ax[2].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
ax[3].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
#ax[3].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
#ax[4].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
#ax[5].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
#ax[6].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
#ax[7].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')

ax[0].set_ylim([-1,11])
ax[1].set_ylim([-0.1,1.2])
ax[2].set_ylim([-50,580])
ax[3].set_ylim([8,38])
#ax[0].set_ylabel('CUMULATIVE\nEVAPORATION\n(mm)', fontsize=y_fontsize, labelpad=20)
ax[0].set_ylabel('EVAPORATION RATE\nFROM WEATHER \nSTATION(mm/day)', fontsize=y_fontsize, labelpad=10)
ax[1].set_ylabel('DEGREE OF\nSATURATION', fontsize=y_fontsize, labelpad=10)
#ax[2].set_ylabel('DEGREE OF SAT.\nBY DIELECTRIC\nMOISTURE\nSENSOR', fontsize=y_fontsize, labelpad=10)
ax[2].set_ylabel('SUCTION (kPa)', fontsize=y_fontsize, labelpad=10)
ax[3].set_ylabel('TEMPERATURE\n($^\circ$c)', fontsize=y_fontsize, labelpad=10)
#ax[5].set_ylabel('TEMPERATURE\n($^\circ$c)', fontsize=y_fontsize, labelpad=20)
#ax[6].set_ylabel('NORMALIZED\nRISE OF\nTEMPERATURE', fontsize=y_fontsize, labelpad=10)
#ax[7].set_ylabel('SUCTION BY\nTEMPERATURE\nHUMIDITY\n SENSOR (m)', fontsize=y_fontsize, labelpad=10)

ax[3].set_xlabel('TIME (days)', fontsize=y_fontsize,labelpad=3)
#ax[0].set_ylim([-0.2,35])
#ax[0].set_ylim([-1,13])
#ax[1].set_ylim([-0.09,0.64])
##ax[2].set_ylim([200,650])
#ax[2].set_ylim([1e-0,1e8])
#ax[5].set_ylim([8,27])
#ax[6].set_ylim([-0.1,1.1])
#ax[7].set_ylim([9,40000])
ax[1].legend(bbox_to_anchor=(.01, 0.65), loc=2, borderaxespad=0.)
ax[2].legend(bbox_to_anchor=(.01, 0.55 ), loc=2, borderaxespad=0.)
ax[3].legend(bbox_to_anchor=(.08, 0.97 ), loc=2, borderaxespad=0.,ncol=7,columnspacing=0.5)
#ax[7].legend(bbox_to_anchor=(.1, 0.55 ), loc=2, borderaxespad=0.)
ax[0].set_title('(A)',x=0.04,y=0.85,fontweight='bold')
ax[1].set_title('(B)',x=0.04,y=0.85,fontweight='bold')
ax[2].set_title('(C)',x=0.04,y=0.85,fontweight='bold')
ax[3].set_title('(D)',x=0.04,y=0.85,fontweight='bold')
#ax[3].set_title('(D)',x=0.04,y=0.75,fontweight='bold')
#ax[4].set_title('(E)',x=0.03,y=0.75,fontweight='bold')
#ax[5].set_title('(F)',x=0.03,y=0.75,fontweight='bold')
#ax[6].set_title('(G)',x=0.03,y=0.75,fontweight='bold')
#ax[7].set_title('(H)',x=0.03,y=0.75,fontweight='bold')
xlim=[sp_sch[sch_name].df.time_days[0],sp_sch[sch_name].df.time_days[len(sp_sch[sch_name].df)-1]]
ax[0].set_xlim(xlim)
ax[1].set_xlim(xlim)
ax[2].set_xlim(xlim)
ax[3].set_xlim(xlim)
#ax[4].set_xlim(xlim)
#ax[5].set_xlim(xlim)
#ax[6].set_xlim(xlim)
#ax[7].set_xlim(xlim)
#ax[0].set_xticklabels([])
#ax[1].set_xticklabels([])
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


fig.savefig('figure/plot_'+sch_name+'mwt2018.png', format='png', dpi=600)
#plt.close()



sp_sch[sch_name].df.to_csv('output_data/'+sch_name+'.csv', sep=',', encoding='utf-8')

