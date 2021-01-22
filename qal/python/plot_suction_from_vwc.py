import glob
import collections
import matplotlib

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
         'lines.linewidth':2}
pylab.rcParams.update(params)

lw=2
ms=6
mew=2
grid_width=2
y_fontsize=11

matplotlib.rcParams['axes.unicode_minus']=False #make the minus sign shown in the axes

fig, ax = plt.subplots(1,1,sharex=True,figsize=(15,6))

fig.subplots_adjust(hspace=.10)
fig.subplots_adjust(left=0.06, right=0.93, top=0.97, bottom=0.1)
fig.subplots_adjust(wspace=.2)


mkevy=4

ta=sp_sch[sch_name].df

ax.semilogy(ta['date_time'][::mkevy], ta['su0_vwc'][::mkevy], '-',color='maroon',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='1 cm',markevery=mkevy)
ax.semilogy(ta['date_time'][::mkevy], ta['su1_vwc'][::mkevy], '-',color='olive',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='5 cm',markevery=mkevy)
ax.semilogy(ta['date_time'][::mkevy], ta['su2_vwc'][::mkevy], '-',color='peru',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='b',label='8 cm',markevery=mkevy)
ax.semilogy(ta['date_time'][::mkevy], ta['su3_vwc'][::mkevy], '-',color='pink',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='13cm',markevery=mkevy)
ax.semilogy(ta['date_time'][::mkevy], ta['su4_vwc'][::mkevy], '-',color='gold',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='20cm',markevery=mkevy)
ax.semilogy(ta['date_time'][::mkevy], ta['su5_vwc'][::mkevy], '-',color='lightgreen',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='28cm',markevery=mkevy)
ax.semilogy(ta['date_time'][::mkevy], ta['su6_vwc'][::mkevy], '-' ,color='lightblue',linewidth=lw ,markerfacecolor='brown' ,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='38cm',markevery=mkevy)
ax.semilogy(ta['date_time'][::mkevy], ta['su7_vwc'][::mkevy], '-' ,color='cyan',linewidth=lw, markerfacecolor='yellow' ,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='yellow',label='48cm',markevery=mkevy)
ax.semilogy(ta['date_time'][::mkevy], ta['su8_vwc'][::mkevy], '-' ,color='royalblue',linewidth=lw,markerfacecolor='crimson' ,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='crimson',label='70cm',markevery=mkevy)
ax.semilogy(ta['date_time'][::mkevy], ta['su9_vwc'][::mkevy], '-' ,color='darkblue',linewidth=lw,markerfacecolor='pink' ,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='pink',label='85cm',markevery=mkevy)

ax.set_ylim([0.01,1010 ])






ax.legend(bbox_to_anchor=(1.03, 0.5 ), loc='center', borderaxespad=0.,fontsize=8.8,handletextpad=0.53,labelspacing=0.52,ncol=1,columnspacing=0.4)

ax.grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')

ax.set_ylabel('SUCTION (kPa)', labelpad=2,fontsize=15)

ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%b/%y'))
ax.set_xlabel('DATE',labelpad=2,fontsize=15)

fig.savefig('figure/figure_update/plot_suction_'+sch_name+'.png', format='png', dpi=600)



