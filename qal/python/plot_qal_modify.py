import matplotlib
import matplotlib.image as image
import matplotlib.pylab as pylab
import matplotlib.ticker as ticker
from matplotlib.dates import DateFormatter, MONDAY, MonthLocator, YearLocator

params = {'legend.fontsize': 4,
          'figure.figsize': (10, 5),
         'axes.labelsize': 11,
         'axes.titlesize':'11',
         'xtick.labelsize':'11',
         'ytick.labelsize':'11',
         'font.weight':'bold',
         #'font.sans-serif':'Arial',
         'font.sans-serif':'TimesNewroman',
         'axes.labelweight':'bold',
         'lines.linewidth':2}#,
#         'title.fontweight':'bold'}

#         'axes.grid':'linewidth=grid_width,color = '0.5''}
#         'linewidth':lw,'markers.size':ms,'markers.edgewidth':mew}
pylab.rcParams.update(params)

lw=2
ms=6
mew=2
grid_width=0.5
y_fontsize=15
ticklabel_size=15
legend_fsz=12

fig, ax = plt.subplots(6,sharex=True,figsize=(11,12))
fig.subplots_adjust(hspace=.10)
fig.subplots_adjust(left=0.17, right=0.89, top=0.97, bottom=0.05)


#fig, ax = plt.subplots(6,sharex=True,figsize=(6,8))
#fig.subplots_adjust(hspace=.15)
mkevy=4


for i in ax:
  for axis in ['top','bottom','left','right']:
    i.spines[axis].set_linewidth(2)

ta=sp_sch['qal'].df
ta=sp_sch[sch_name].df
ta['radiation']=(ta['ir_up_concat']-254)/20.512
df_mean['radiation']=(df_mean['ir_up_concat']-254)/20.512
df_mean['cumsum_rainmm']=np.cumsum(df_last['rainmm'])
#df_mean['cumsum_aetmm']=np.cumsum(df_mean['aet_mmPday'])

#ax[0].plot(ta['date_time'], ta['rainmm'], '-',color='maroon',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Dielectric suction A')
#ax[0].set_ylim([-5,100])
ax1=ax[0]
ax1.bar(df_mean.index, df_last['rainmm'], width=1.8,edgecolor='white',lw=0.1)
ax2=ax1.twinx()
ax2.plot(df_mean.index,df_mean['cumsum_rainmm'],'-',color='red',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r')
ax1.set_ylim([-0.1,110])
ax2.set_ylim([-0.1,1200])
ax1.tick_params(axis='y',colors='blue',labelsize=ticklabel_size)
ax2.tick_params(axis='y',colors='red',labelsize=ticklabel_size)

#ax[1].plot(ta['date_time'], (ta['ir_up']-ta['ir_down'])*0.007+0.2*ta['wdspdkphavg2m'].fillna(0), '-',color='maroon',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Dielectric suction A')
#ax[1].set_ylim([-0.100,9])
#ax3=ax[1]
#ax4=ax3.twinx()
ax[1].bar(df_mean.index,df_mean['pet_mmPday'],width=1.0,color='brown',edgecolor='white',label='Pote.\nevap.',lw=0.1)
ax[1].bar(df_mean.index,df_mean['aet_mmPday'],width=1.0,color='orange',edgecolor='white',label='Actu.\nevap.',lw=0.1)
ax[1].tick_params(axis='y',labelsize=ticklabel_size)
ax[1].set_ylim([-0.1,11])

#ax3.bar(df_mean.index,df_mean['pet_mmPday'],width=1.0,color='brown',edgecolor='white',label='Pote.\nevap.',lw=0.1)
#ax3.bar(df_mean.index,df_mean['aet_mmPday'],width=1.0,color='orange',edgecolor='white',label='Actu.\nevap.',lw=0.1)
#ax4.plot(df_mean.index,df_mean['cumsum_aetmm'],'-',color='red',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r')
#ax3.set_ylim([-0.1,11])


#ax[2].plot(ta['date_time'], -(ta['pre0']-60), 'r-',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='30 cm below soil surface')
#ax[2].plot(ta['date_time'], -(ta['pre1']-110), 'g-',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='60 cm below soil surface')
#ax[2].set_ylim([-10-110,140-110])
#ax[2].set_ylim([-140+110,120,])
ax[2].plot(ta['date_time'], ta['Pre0'], '-',color='cyan',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='500 mm')
ax[2].plot(ta['date_time'], ta['Pre1'], '-',color='darkblue',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='1000 mm')
#ax[2].set_ylim([-10-110,140-110])
ax[2].set_ylim([-100,1100])
ax[2].tick_params(axis='y',labelsize=ticklabel_size)
#ax[2].set_ylim([-140+110,120,])

#ax[3].plot(ta['date_time'][::mkevy].values, ta['tmp0'][::mkevy].values, '-' ,color='maroon',linewidth=lw,markersize=ms           ,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='1 cm',markevery=mkevy)
#ax[3].plot(ta['date_time'][::mkevy].values, ta['tmp1'][::mkevy].values, '-' ,color='peru',linewidth=lw,markersize=ms           ,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='5 cm',markevery=mkevy)
#ax[3].plot(ta['date_time'][::mkevy].values, ta['tmp2'][::mkevy].values, '-' ,color='gold',linewidth=lw,markersize=ms           ,markeredgewidth=mew,fillstyle='full', markeredgecolor='b',label='8 cm',markevery=mkevy)
#ax[3].plot(ta['date_time'][::mkevy].values, ta['tmp3'][::mkevy].values, '-' ,color='olive',linewidth=lw,markersize=ms           ,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='13cm',markevery=mkevy)
#ax[3].plot(ta['date_time'][::mkevy].values, ta['tmp4'][::mkevy].values, '-' ,color='limegreen',linewidth=lw,markersize=ms           ,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='20cm',markevery=mkevy)
#ax[3].plot(ta['date_time'][::mkevy].values, ta['tmp5'][::mkevy].values, '-' ,color='lightblue',linewidth=lw,markersize=ms           ,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='28cm',markevery=mkevy)
#ax[3].plot(ta['date_time'][::mkevy].values, ta['tmp6'][::mkevy].values, '-' ,color='royalblue'  ,linewidth=lw,markerfacecolor='brown' ,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='38cm',markevery=mkevy)
#ax[3].plot(ta['date_time'][::mkevy].values, ta['tmp7'][::mkevy].values, '-' ,color='darkblue' ,linewidth=lw,markerfacecolor='yellow',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='yellow',label='48cm',markevery=mkevy)
#ax[3].plot(ta['date_time'][::mkevy].values, ta['tmp8'][::mkevy].values, '-' ,color='crimson',linewidth=lw,markerfacecolor='orange',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='orange',label='70cm',markevery=mkevy)
#ax[3].plot(ta['date_time'][::mkevy].values, ta['tmp9'][::mkevy].values, '-' ,color='pink'   ,linewidth=lw,markerfacecolor='grey'  ,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='grey',label='85cm',markevery=mkevy)


ax[3].plot(ta['date_time'][::mkevy].values, ta['tmp0'][::mkevy].values, '-' ,color='maroon',linewidth=lw,markersize=ms           ,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='15 mm',markevery=mkevy)
ax[3].plot(ta['date_time'][::mkevy].values, ta['tmp1'][::mkevy].values, '-' ,color='olive',linewidth=lw,markersize=ms           ,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='50 mm',markevery=mkevy)
ax[3].plot(ta['date_time'][::mkevy].values, ta['tmp2'][::mkevy].values, '-' ,color='peru',linewidth=lw,markersize=ms           ,markeredgewidth=mew,fillstyle='full', markeredgecolor='b',label='80 mm',markevery=mkevy)
ax[3].plot(ta['date_time'][::mkevy].values, ta['tmp3'][::mkevy].values, '-' ,color='pink',linewidth=lw,markersize=ms           ,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='135 mm',markevery=mkevy)
ax[3].plot(ta['date_time'][::mkevy].values, ta['tmp4'][::mkevy].values, '-' ,color='gold',linewidth=lw,markersize=ms           ,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='200 mm',markevery=mkevy)
ax[3].plot(ta['date_time'][::mkevy].values, ta['tmp5'][::mkevy].values, '-' ,color='lightgreen',linewidth=lw,markersize=ms           ,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='285 mm',markevery=mkevy)
ax[3].plot(ta['date_time'][::mkevy].values, ta['tmp6'][::mkevy].values, '-' ,color='lightblue'  ,linewidth=lw,markerfacecolor='brown' ,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='385 mm',markevery=mkevy)
ax[3].plot(ta['date_time'][::mkevy].values, ta['tmp7'][::mkevy].values, '-' ,color='cyan' ,linewidth=lw,markerfacecolor='yellow',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='yellow',label='485 mm',markevery=mkevy)
ax[3].plot(ta['date_time'][::mkevy].values, ta['tmp8'][::mkevy].values, '-' ,color='royalblue',linewidth=lw,markerfacecolor='orange',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='orange',label='700 mm',markevery=mkevy)
ax[3].plot(ta['date_time'][::mkevy].values, ta['tmp9'][::mkevy].values, '-' ,color='darkblue'   ,linewidth=lw,markerfacecolor='grey'  ,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='grey',label='850 mm',markevery=mkevy)
ax[3].set_ylim([5,45])
ax[3].tick_params(axis='y',labelsize=ticklabel_size)

mkevy=24

#ax[4].plot(ta['date_time'][::mkevy], ta['mmo0'][::mkevy], '-',color='maroon',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='1 cm',markevery=mkevy)
#ax[4].plot(ta['date_time'][::mkevy], ta['mmo1'][::mkevy], '-',color='peru',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='5 cm',markevery=mkevy)
#ax[4].plot(ta['date_time'][::mkevy], ta['mmo2'][::mkevy], '-',color='gold',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='b',label='8 cm',markevery=mkevy)
#ax[4].plot(ta['date_time'][::mkevy], ta['mmo3'][::mkevy], '-',color='olive',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='13cm',markevery=mkevy)
#ax[4].plot(ta['date_time'][::mkevy], ta['mmo4'][::mkevy], '-',color='limegreen',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='20cm',markevery=mkevy)
#ax[4].plot(ta['date_time'][::mkevy], ta['mmo5'][::mkevy], '-',color='lightblue',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='28cm',markevery=mkevy)
#ax[4].plot(ta['date_time'][::mkevy], ta['mmo6'][::mkevy], '-' ,color='royalblue',linewidth=lw ,markerfacecolor='brown' ,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='38cm',markevery=mkevy)
#ax[4].plot(ta['date_time'][::mkevy], ta['mmo7'][::mkevy], '-' ,color='darkblue',linewidth=lw, markerfacecolor='yellow' ,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='yellow',label='48cm',markevery=mkevy)
#ax[4].plot(ta['date_time'][::mkevy], ta['mmo8'][::mkevy], '-' ,color='crimson',linewidth=lw,markerfacecolor='crimson' ,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='crimson',label='70cm',markevery=mkevy)
#ax[4].plot(ta['date_time'][::mkevy], ta['mmo9'][::mkevy], '-' ,color='pink',linewidth=lw,markerfacecolor='pink' ,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='pink',label='85cm',markevery=mkevy)
ax[4].plot(ta['date_time'][::mkevy], ta['mmo0'][::mkevy], '-',color='maroon',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='15 mm',markevery=mkevy)
ax[4].plot(ta['date_time'][::mkevy], ta['mmo1'][::mkevy], '-',color='olive',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='50 mm',markevery=mkevy)
ax[4].plot(ta['date_time'][::mkevy], ta['mmo2'][::mkevy], '-',color='peru',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='b',label='80 mm',markevery=mkevy)
ax[4].plot(ta['date_time'][::mkevy], ta['mmo3'][::mkevy], '-',color='pink',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='135 mm',markevery=mkevy)
ax[4].plot(ta['date_time'][::mkevy], ta['mmo4'][::mkevy], '-',color='gold',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='200 mm',markevery=mkevy)
ax[4].plot(ta['date_time'][::mkevy], ta['mmo5'][::mkevy], '-',color='lightgreen',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='285 mm',markevery=mkevy)
ax[4].plot(ta['date_time'][::mkevy], ta['mmo6'][::mkevy], '-' ,color='lightblue',linewidth=lw ,markerfacecolor='brown' ,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='385 mm',markevery=mkevy)
ax[4].plot(ta['date_time'][::mkevy], ta['mmo7'][::mkevy], '-' ,color='cyan',linewidth=lw, markerfacecolor='yellow' ,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='yellow',label='485 mm',markevery=mkevy)
ax[4].plot(ta['date_time'][::mkevy], ta['mmo8'][::mkevy], '-' ,color='royalblue',linewidth=lw,markerfacecolor='crimson' ,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='crimson',label='700 mm',markevery=mkevy)
ax[4].plot(ta['date_time'][::mkevy], ta['mmo9'][::mkevy], '-' ,color='darkblue',linewidth=lw,markerfacecolor='pink' ,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='pink',label='850 mm',markevery=mkevy)
ax[4].set_ylim([-0.01,0.61])
ax[4].tick_params(axis='y',labelsize=ticklabel_size)


ax[5].plot(ta['date_time'], ta['ec0']/1000., '-',color='olive',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='50 mm')
ax[5].plot(ta['date_time'], ta['ec1']/1000., '-',color='royalblue',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='600 mm')
ax[5].set_ylim([-0.2,8.1])
ax[5].tick_params(axis='y',labelsize=ticklabel_size)



ax1.set_ylabel('RAINFALL\n(mm/day)', fontsize=y_fontsize, labelpad=18,color='blue')
ax2.set_ylabel('CUMULATIVE\nRAINFALL\n(mm)', fontsize=y_fontsize, labelpad=6,color='red')
#ax[1].set_ylabel('DAILY\nEVAPORATION\n(mm)', fontsize=y_fontsize, labelpad=15)
ax[1].set_ylabel('EVAPORATION\n(mm/day)', fontsize=y_fontsize, labelpad=17)
ax[2].set_ylabel('WATER\nPRESSURE\n(mm)', fontsize=y_fontsize, labelpad=5)
ax[3].set_ylabel('TEMPERATURE\n($^\circ$C)', fontsize=y_fontsize, labelpad=11)
#ax[4].set_ylabel('VOLUMETRIC\nWATER CONTENT', fontsize=y_fontsize, labelpad=15)
ax[4].set_ylabel('VOLUMETRIC\nWATER\nCONTENT\n(m$^3$/m$^3$)', fontsize=y_fontsize, labelpad=5)
#ax[5].set_ylabel('ELECTRICAL\nCONDUCTIVITY\n(dS/m)', fontsize=y_fontsize, labelpad=12)
ax[5].set_ylabel('ELECTRICAL\nCONDUCTIVITY\n(dS/m)', fontsize=y_fontsize, labelpad=9)

ax[0].set_title('(a)',x=0.03,y=0.8,fontweight='bold',fontsize=ticklabel_size)
ax[1].set_title('(b)',x=0.03,y=0.8,fontweight='bold',fontsize=ticklabel_size)
ax[2].set_title('(c)',x=0.03,y=0.8,fontweight='bold',fontsize=ticklabel_size)
ax[3].set_title('(d)',x=0.03,y=0.8,fontweight='bold',fontsize=ticklabel_size)
ax[4].set_title('(e)',x=0.03,y=0.8,fontweight='bold',fontsize=ticklabel_size)
ax[5].set_title('(f)',x=0.03,y=0.8,fontweight='bold',fontsize=ticklabel_size)

ax[0].set_axisbelow(True)
ax[1].set_axisbelow(True)
ax[2].set_axisbelow(True)
ax[3].set_axisbelow(True)
ax[4].set_axisbelow(True)
ax[5].set_axisbelow(True)

ax[1].legend(bbox_to_anchor=(1.07, 0.5 ), loc='center', borderaxespad=0.,fontsize=legend_fsz,handletextpad=0.83,labelspacing=1.32,ncol=1,columnspacing=0.4)
ax[2].legend(bbox_to_anchor=(1.07, 0.5 ), loc='center', borderaxespad=0.,fontsize=legend_fsz,handletextpad=0.03,labelspacing=0.02,ncol=1,columnspacing=0.4)
ax[3].legend(bbox_to_anchor=(1.07, 0.5 ), loc='center', borderaxespad=0.,fontsize=legend_fsz,handletextpad=0.03,labelspacing=0.02,ncol=1,columnspacing=0.4)
ax[4].legend(bbox_to_anchor=(1.07, 0.5 ), loc='center', borderaxespad=0.,fontsize=legend_fsz,handletextpad=0.02,labelspacing=0.01,ncol=1,columnspacing=0.4)
ax[5].legend(bbox_to_anchor=(1.07, 0.5 ), loc='center', borderaxespad=0.,fontsize=legend_fsz,handletextpad=0.03,labelspacing=0.02,ncol=1,columnspacing=0.4)

ax1.minorticks_on()
ax[1].minorticks_on()
ax[2].minorticks_on()
ax[3].minorticks_on()
ax[4].minorticks_on()
ax[5].minorticks_on()

ax[0].grid(which="major",ls="-",linewidth=grid_width,color = 'black')
ax[0].grid(which="minor",ls=":",linewidth=grid_width,color = 'black')
ax[1].grid(which="major",ls="-",linewidth=grid_width,color = 'black')
ax[1].grid(which="minor",ls=":",linewidth=grid_width,color = 'black')
ax[2].grid(which="major",ls="-",linewidth=grid_width,color = 'black')
ax[2].grid(which="minor",ls=":",linewidth=grid_width,color = 'black')
ax[3].grid(which="major",ls="-",linewidth=grid_width,color = 'black')
ax[3].grid(which="minor",ls=":",linewidth=grid_width,color = 'black')
ax[4].grid(which="major",ls="-",linewidth=grid_width,color = 'black')
ax[4].grid(which="minor",ls=":",linewidth=grid_width,color = 'black')
ax[5].grid(which="major",ls="-",linewidth=grid_width,color = 'black')
ax[5].grid(which="minor",ls=":",linewidth=grid_width,color = 'black')



#ax[0].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
#ax[1].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
#ax[2].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
#ax[3].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
#ax[4].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
#ax[5].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
#ax[2].plot(ta['date_time'], ta['su5'], 'ro',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Dielectric suction A')
#ax[2].plot(ta['date_time'], ta['su6'], 'go',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='Dielectric suction B')
#ax[2].plot(ta['date_time'], ta['su7'], 'bo',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='b',label='Moisture A')
#ax[2].plot(ta['date_time'], ta['su8'], 'co',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='Moisture A')
#
#
#ax[3].plot(ta['date_time'], ta['temp_suc1'], 'ro',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Dielectric suction A')
#ax[3].plot(ta['date_time'], ta['temp_suc2'], 'go',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='Dielectric suction B')
#ax[3].plot(ta['date_time'], ta['temp_suc3'], 'bo',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='b',label='Moisture A')
#ax[3].plot(ta['date_time'], ta['temp_suc4'], 'co',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='Moisture A')
#ax[3].plot(ta['date_time'], ta['temp_suc5'], 'mo',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='Moisture A')
#ax[3].plot(ta['date_time'], ta['temp_suc6'], 'ko',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='Moisture A')
#ax[3].plot(ta['date_time'], ta['temp_suc7'], 'o' ,markerfacecolor='brown' ,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='Moisture A')

mondays=MonthLocator()
locate=MonthLocator(range(1,13),bymonthday=1,interval=3)
ax[5].xaxis.set_major_locator(locate)
ax[5].xaxis.set_minor_locator(mondays)

#ax[5].xaxis.set_major_formatter(mdates.DateFormatter('%b/%d'))
ax[5].xaxis.set_major_formatter(mdates.DateFormatter('%b/%y'))
ax[5].set_xlabel('DATE',fontsize=y_fontsize)
ax[5].tick_params(axis='x',labelsize=ticklabel_size)
#plt.xticks(rotation=45)
plt.show(block=False)



#fig.savefig('figure/figure_update/plot_'+sch_name+'.png', format='png', dpi=600)
fig.savefig('figure/figure_update/update_to_2021/plot_'+sch_name+'.png', format='png', dpi=600)
df_mean['pet_mmPday'].to_csv('output_data/'+'PET_mean'+'.csv')
df_mean['aet_mmPday'].to_csv('output_data/'+'AET_mean'+'.csv')
