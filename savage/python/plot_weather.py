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
sch_name='rain_solar'


import matplotlib.pylab as pylab
lw=2
ms=0.5
mew=3
grid_width=2

params = {'legend.fontsize': 6,
          'figure.figsize': (10, 6),
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

#lw=2
#ms=6
#mew=2
#grid_width=2
y_fontsize=12
x_fontsize=12
fig, ax = plt.subplots(2,sharex=True,figsize=(10,6))
fig.subplots_adjust(hspace=.10)
fig.subplots_adjust(left=0.12, right=0.85, top=0.93, bottom=0.08)
ax2=ax[1].twinx()
    
for i in ax:
  for axis in ['top','bottom','left','right']:
    i.spines[axis].set_linewidth(2)


sp=solar['solar']['df']
ax[0].bar(sp.index, sp['Daily global solar exposure (KWh/m*m)'],color='maroon',edgecolor='maroon')

sp=rain['rain']['df']

ax[1].bar(sp.index, sp['Rainfall amount (millimetres)'],color='royalblue',edgecolor='royalblue')
ax2.plot(sp.index, sp['rain_cumsum'],color='darkblue')



#ax[3].set_axisbelow(True)
ax[0].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
ax[1].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')


#
#ax[0].set_ylabel('CUMULATIVE\nEVAPORATION\n(mm)', fontsize=y_fontsize, labelpad=20)
ax[0].set_ylabel('GLOBAL\nSOLAR EXPOSURE\n(KWh/m*m)', fontsize=y_fontsize, labelpad=10)
ax[1].set_ylabel('RAINFALL\n(mm)', fontsize=y_fontsize, labelpad=10)
ax2.set_ylabel('CUMULATIVE RAINFALL\n(mm)', fontsize=y_fontsize, labelpad=10)


ax[1].set_xlabel('DATE', fontsize=x_fontsize,labelpad=3)
ax[0].set_ylim([0,10])
ax[1].set_ylim([0,60])
ax2.set_ylim([0,2500])


ax[0].set_title('(A)',x=0.03,y=0.9,fontweight='bold')
ax[1].set_title('(B)',x=0.03,y=0.9,fontweight='bold')



#ax[5].legend(bbox_to_anchor=(1.10, 0.06),  loc='center' , borderaxespad=0.,fontsize=10,handletextpad=0.03,labelspacing=0.02,ncol=1,columnspacing=0.2,title="SOIL DEPTHS\n(C,D,E,F,G,H)")
#ax[2].legend(bbox_to_anchor=(1.09, 0.5 ), loc='center' , borderaxespad=0.,fontsize=12,handletextpad=0.03,labelspacing=0.02,ncol=1,columnspacing=0.4)



ax[1].xaxis.set_major_formatter(mdates.DateFormatter('%b-%d'))

#ax[4].set_title('(E)',x=0.03,y=0.75,fontweight='bold')
#ax[5].set_title('(F)',x=0.03,y=0.75,fontweight='bold')
#ax[6].set_title('(G)',x=0.03,y=0.75,fontweight='bold')
#ax[7].set_title('(H)',x=0.03,y=0.75,fontweight='bold')
#xlim=[sp_sch[sch_name].df.time_days[0],sp_sch[sch_name].df.time_days[len(sp_sch[sch_name].df)-1]]
#ax[0].set_xlim(xlim)
#ax[1].set_xlim(xlim)
#ax[2].set_xlim(xlim)
#ax[3].set_xlim(xlim)
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


plt.show(block=False)


fig.savefig('figure/plot_'+sch_name+'.png', format='png', dpi=600)
#plt.close()



#sp_sch[sch_name].df.to_csv('output_data/'+sch_name+'.csv', sep=',', encoding='utf-8')

