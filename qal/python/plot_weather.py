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

pylab.rcParams.update(params)

lw=1.2
ms=1
mew=1.5
grid_width=1.5
y_fontsize=16
ticklabel_size=16
legend_fsz= 14

fig, ax = plt.subplots(6,sharex=True,figsize=(11,12))
#fig.subplots_adjust(hspace=.15)
fig.subplots_adjust(left=0.15, right=0.87, top=0.96, bottom=0.06)
mkevy=4


# it is not necessary to remove the night result and folcus on only the day time results as the number of point after interpolation is the same per day. 
#new = old.filter(['A','B','D'], axis=1)




for i in ax:
  for axis in ['top','bottom','left','right']:
    i.spines[axis].set_linewidth(2)

ta=sp_sch['qal'].df
#ta1=sp_sch['qal1807'].df
df_max = sp_sch['qal'].df.resample('D').max()
df_max['date_time']=df_max.index
#df_max1 = sp_sch['qal1807'].df.resample('D').max()
#df_max1['date_time']=df_max1.index


df_mean = sp_sch['qal'].df.resample('D').mean()
df_mean['date_time']=df_mean.index
df_mean['ir_up_daisy'].loc[df_mean['ir_up_daisy']>400]=df_mean['ir_up_daisy']*0.75
df_mean['cumsum_rainmm']=np.cumsum(df_last['rainmm'])
#df_mean1 = sp_sch['qal1807'].df.resample('D').mean()
#df_mean1['date_time']=df_mean1.index

#ax[0].plot(ta['date_time'], ta['rainmm'], '-',color='maroon',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Daily rainfall') 
#ax[0].plot(ta['date_time'], ta['rainmm'], '-',color='cornflowerblue',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='cornflowerblue',label='Daily rainfall') #Change the line colour

#ax[0].bar(df_mean.index, df_last['rainmm'], width=1.8, color='royalblue', edgecolor='white',linewidth=0.2) #color = 'maroon'
#ax[0].set_ylim([-0.1,40])
#ax[0].tick_params(axis='y',labelsize=ticklabel_size)

ax1=ax[0]
ax1.bar(df_mean.index, df_last['rainmm'], width=1.8, color='royalblue', edgecolor='white',linewidth=0.2) #color = 'maroon'
ax2=ax1.twinx()
ax2.plot(df_mean.index,df_mean['cumsum_rainmm'],'-',color='black',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='black')
ax1.set_ylim([-0.1,110])
ax2.set_ylim([-0.1,1200])
ax1.tick_params(axis='y',colors='black',labelsize=ticklabel_size)
ax2.tick_params(axis='y',colors='black',labelsize=ticklabel_size)


ax[1].plot(ta['date_time'], (ta['ir_up_concat']-254)/20.512, '-',color='firebrick',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Instant')
ax[1].plot(df_mean['date_time'], (df_mean['ir_up_concat']-254)/20.512, '-',color='gold',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='gold',label='Daily \nAverage')
ax[1].tick_params(axis='y',labelsize=ticklabel_size)
ax[1].set_ylim([-5,1200])


ax[2].plot(ta['date_time'], ta['wdspd2m'], '-',color='dimgray',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='dimgray',label='Instant')
ax[2].plot(ta['date_time'], ta['wdgst10m']/2.0, 'ko',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='Gust',markevery=5)
ax[2].plot(df_mean['date_time'], df_mean['wdspd2m'], '-',color = 'gold',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='gold',label='Daily \nAverage')
#ax[4].plot(ta['date_time'], ta['ec1'], 'g-',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Dielectric suction A')
ax[2].tick_params(axis='y',labelsize=ticklabel_size)
ax[2].set_ylim([-0.1,15])

#ax[2].plot(ta['date_time'], ta['wdspdkphavg2m'], '-',color='maroon',linewidth=lw,  markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Instant')
#ax[2].plot(ta['date_time'], ta['wdgstkph10m']/2.0, 'ko', linewidth=lw, markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='Gust',markevery=5)
#ax[2].plot(df_mean['date_time'], df_mean['wdspdkphavg2m'], 'g-', linewidth=lw, markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='Daily \nAverage')
#ax[2].set_ylim([-1,15])

ax[3].plot(ta['date_time'][::mkevy].values, ta['temperature'][::mkevy].values, '-',color='darkred',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='darkred',label='Instant',markevery=mkevy)
ax[3].plot(df_mean['date_time'], df_mean['temperature'], '-',color='gold',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='gold',label='Daily\nAverage')
ax[3].tick_params(axis='y',labelsize=ticklabel_size)
ax[3].set_ylim([5,38])

#ax[3].plot(ta['date_time'][::mkevy].values, ta['tc'][::mkevy].values, '-',color='maroon',linewidth=lw,  markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Instant',markevery=mkevy)
#ax[3].plot(df_mean['date_time'], df_mean['tc'], 'g-', linewidth=lw, markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='Daily\nAverage')
#ax[3].set_ylim([5,38])


ax[4].plot(ta['date_time'][::mkevy], ta['RH'][::mkevy]*100., '-',color='steelblue',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='steelblue',label='Instant',markevery=mkevy)
ax[4].plot(df_mean['date_time'], df_mean['RH']*100., '-',color='gold',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='gold',label='Daily\nAverage')
ax[4].tick_params(axis='y',labelsize=ticklabel_size)
ax[4].set_ylim([0,100])

#ax[4].plot(ta['date_time'][::mkevy], ta['rh'][::mkevy]*100., '-',color='maroon', linewidth=lw, markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Instant',markevery=mkevy)
#ax[4].plot(df_mean['date_time'], df_mean['rh']*100., 'g-', linewidth=lw, markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='Daily\nAverage')
#ax[4].set_ylim([0,100])


ax[5].plot(ta['date_time'], ta['AP']/1000, '-',color='navy',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='navy',label='Instant')
ax[5].plot(df_mean['date_time'], df_mean['AP']/1000, '-',color='gold',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='gold',label='Daily\nAverage')
ax[5].tick_params(axis='y',labelsize=ticklabel_size)
ax[5].set_ylim([100,103])

#ax[5].plot(ta['date_time'], ta['p']/1000, '-',color='maroon', linewidth=lw, markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Instant')
#ax[5].plot(df_mean['date_time'], df_mean['p']/1000, 'g-', linewidth=lw, markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='Daily\nAverage')
#ax[5].set_ylim([100,103])



ax[0].set_title('(a)',x=0.03,y=0.8,fontweight='bold',fontsize=ticklabel_size)
ax[1].set_title('(b)',x=0.03,y=0.8,fontweight='bold',fontsize=ticklabel_size)
ax[2].set_title('(c)',x=0.03,y=0.8,fontweight='bold',fontsize=ticklabel_size)
ax[3].set_title('(d)',x=0.03,y=0.8,fontweight='bold',fontsize=ticklabel_size)
ax[4].set_title('(e)',x=0.03,y=0.8,fontweight='bold',fontsize=ticklabel_size)
ax[5].set_title('(f)',x=0.03,y=0.8,fontweight='bold',fontsize=ticklabel_size)
ax[0].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
ax[1].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
ax[2].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
ax[3].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
ax[4].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
ax[5].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
ax[0].set_axisbelow(True)
ax[1].set_axisbelow(True)
ax[2].set_axisbelow(True)
ax[3].set_axisbelow(True)
ax[4].set_axisbelow(True)
ax[5].set_axisbelow(True)

ax1.set_ylabel('RAINFALL\n(mm/day)', fontsize=y_fontsize, labelpad=18,color='black')
ax2.set_ylabel('CUMULATIVE\nRAINFALL\n(mm)', fontsize=y_fontsize, labelpad=6,color='black')
#ax[0].set_ylabel('DAILY\nRAINFALL\n(mm)', fontsize=y_fontsize, labelpad=17)
ax[1].set_ylabel('SOLAR\nRADIATION\n(W/m$^{2}$)', fontsize=y_fontsize, labelpad=4)
ax[2].set_ylabel('WIND\nSPEED\n(m/s)', fontsize=y_fontsize, labelpad=18)
ax[3].set_ylabel('TEMPERATURE\n($^\circ$C)', fontsize=y_fontsize, labelpad=18)
ax[4].set_ylabel('RELATIVE\nHUMIDITY\n(%)', fontsize=y_fontsize, labelpad=14)
ax[5].set_ylabel('ATMOSPHERIC\nPRESSURE\n(kPa)', fontsize=y_fontsize, labelpad=7)
ax[1].legend(bbox_to_anchor=(1.09, 0.5 ), loc='center', borderaxespad=0.,fontsize=legend_fsz,handletextpad=0.33,labelspacing=0.35,ncol=1,columnspacing=0.4)
ax[2].legend(bbox_to_anchor=(1.09, 0.5 ), loc='center', borderaxespad=0.,fontsize=legend_fsz,handletextpad=0.33,labelspacing=0.35,ncol=1,columnspacing=0.4)
ax[3].legend(bbox_to_anchor=(1.09, 0.5 ), loc='center', borderaxespad=0.,fontsize=legend_fsz,handletextpad=0.33,labelspacing=0.35,ncol=1,columnspacing=0.4)
ax[4].legend(bbox_to_anchor=(1.09, 0.5 ), loc='center', borderaxespad=0.,fontsize=legend_fsz,handletextpad=0.33,labelspacing=0.35,ncol=1,columnspacing=0.4)
ax[5].legend(bbox_to_anchor=(1.09, 0.5 ), loc='center', borderaxespad=0.,fontsize=legend_fsz,handletextpad=0.33,labelspacing=0.35,ncol=1,columnspacing=0.4)


#ax[3].xaxis.set_major_formatter(mdates.DateFormatter('%d/%b/%y'))
mondays=MonthLocator()
locate=MonthLocator(range(1,13),bymonthday=1,interval=3)
ax[5].xaxis.set_major_locator(locate)
ax[5].xaxis.set_minor_locator(mondays)

ax[5].xaxis.set_major_formatter(mdates.DateFormatter('%b/%y'))
ax[5].set_xlabel('DATE',fontsize=y_fontsize)
ax[5].tick_params(axis='x',labelsize=ticklabel_size)
plt.show(block=False)

#fig.savefig('figure/figure_update/plot_weather.png', format='png', dpi=600)
fig.savefig('figure/figure_update/update_to_2021/plot_weather.png', format='png', dpi=600)
#sp_sch[sch_name].df.iloc[::4].to_csv('output_data/'+'column_qal'+'.csv')
sp_sch[sch_name].df.to_csv('output_data/'+'column_qal_1h_mkevy'+'.csv')
#fig.close()




