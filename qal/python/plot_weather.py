import matplotlib
import matplotlib.image as image
import matplotlib.pylab as pylab

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

lw=1
ms=1
mew=1.5
grid_width=1.5
y_fontsize=13
ticklabel_size=14

fig, ax = plt.subplots(6,sharex=True,figsize=(10,9))
#fig.subplots_adjust(hspace=.15)
fig.subplots_adjust(left=0.18, right=0.87, top=0.97, bottom=0.08)
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
#df_mean1 = sp_sch['qal1807'].df.resample('D').mean()
#df_mean1['date_time']=df_mean1.index

ax[0].plot(ta['date_time'], ta['rainmm'], '-',color='maroon',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Dielectric suction A')

#ax[0].bar(df_mean.index, df_last['rainmm'], width=1.8, color='maroon', edgecolor='white',lw=0.1)
#ax[0].set_ylim([-0.1,40])

ax[1].plot(ta['date_time'], (ta['ir_up_concat']-254)/20.512, '-',color='maroon',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Instant')
ax[1].plot(df_mean['date_time'], (df_mean['ir_up_concat']-254)/20.512, 'g-',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='Daily \nAverage')
ax[1].set_ylim([-5,1200])

#ax[1].plot(ta['date_time'], (ta['ir_up_daisy']-254)*1.25, '-',color='maroon',linewidth=lw, markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r')
#ax[1].plot(df_mean['date_time'],(df_mean['ir_up_daisy']-254)*1.25, 'g-',linewidth=lw, markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='g')
#ax[1].plot(ta['date_time'], (ta['ir_up_concat']-254)/20.512, '-',color='maroon',linewidth=lw, markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Instant')
#ax[1].plot(df_mean['date_time'],(df_mean['ir_up_concat']-254)/20.512, 'g-',linewidth=lw, markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='Daily \nAverage')
#ax[1].set_ylim([-5,1200])


ax[2].plot(ta['date_time'], ta['wdspd2m'], '-',color='maroon',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Instant')
ax[2].plot(ta['date_time'], ta['wdgst10m']/2.0, 'ko',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='Gust',markevery=5)
ax[2].plot(df_mean['date_time'], df_mean['wdspd2m'], 'g-',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='Daily \nAverage')
#ax[4].plot(ta['date_time'], ta['ec1'], 'g-',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Dielectric suction A')
ax[2].set_ylim([-1,15])

#ax[2].plot(ta['date_time'], ta['wdspdkphavg2m'], '-',color='maroon',linewidth=lw,  markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Instant')
#ax[2].plot(ta['date_time'], ta['wdgstkph10m']/2.0, 'ko', linewidth=lw, markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='Gust',markevery=5)
#ax[2].plot(df_mean['date_time'], df_mean['wdspdkphavg2m'], 'g-', linewidth=lw, markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='Daily \nAverage')
#ax[2].set_ylim([-1,15])

ax[3].plot(ta['date_time'][::mkevy].values, ta['temperature'][::mkevy].values, '-',color='maroon',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Instant',markevery=mkevy)
ax[3].plot(df_mean['date_time'], df_mean['temperature'], 'g-',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='Daily\nAverage')
ax[3].set_ylim([5,38])

#ax[3].plot(ta['date_time'][::mkevy].values, ta['tc'][::mkevy].values, '-',color='maroon',linewidth=lw,  markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Instant',markevery=mkevy)
#ax[3].plot(df_mean['date_time'], df_mean['tc'], 'g-', linewidth=lw, markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='Daily\nAverage')
#ax[3].set_ylim([5,38])


ax[4].plot(ta['date_time'][::mkevy], ta['RH'][::mkevy]*100., '-',color='maroon',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Instant',markevery=mkevy)
ax[4].plot(df_mean['date_time'], df_mean['RH']*100., 'g-',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='Daily\nAverage')
ax[4].set_ylim([0,100])

#ax[4].plot(ta['date_time'][::mkevy], ta['rh'][::mkevy]*100., '-',color='maroon', linewidth=lw, markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Instant',markevery=mkevy)
#ax[4].plot(df_mean['date_time'], df_mean['rh']*100., 'g-', linewidth=lw, markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='Daily\nAverage')
#ax[4].set_ylim([0,100])


ax[5].plot(ta['date_time'], ta['AP']/1000, '-',color='maroon',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Instant')
ax[5].plot(df_mean['date_time'], df_mean['AP']/1000, 'g-',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='Daily\nAverage')
ax[5].set_ylim([100,103])

#ax[5].plot(ta['date_time'], ta['p']/1000, '-',color='maroon', linewidth=lw, markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Instant')
#ax[5].plot(df_mean['date_time'], df_mean['p']/1000, 'g-', linewidth=lw, markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='Daily\nAverage')
#ax[5].set_ylim([100,103])



ax[0].set_title('(A)',x=0.04,y=0.8,fontweight='bold')
ax[1].set_title('(B)',x=0.04,y=0.8,fontweight='bold')
ax[2].set_title('(C)',x=0.04,y=0.8,fontweight='bold')
ax[3].set_title('(D)',x=0.04,y=0.8,fontweight='bold')
ax[4].set_title('(E)',x=0.04,y=0.8,fontweight='bold')
ax[5].set_title('(F)',x=0.04,y=0.8,fontweight='bold')
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
ax[0].set_ylabel('DAILY\nRAINFALL\n(mm)', fontsize=y_fontsize, labelpad=17)
ax[1].set_ylabel('SOLAR\nRADIATION\n(W/m$^{2}$)', fontsize=y_fontsize, labelpad=4)
ax[2].set_ylabel('WIND\nSPEED\n(m/s)', fontsize=y_fontsize, labelpad=18)
ax[3].set_ylabel('TEMPERATURE\n($^\circ$C)', fontsize=y_fontsize, labelpad=18)
ax[4].set_ylabel('RELATIVE\nHUMIDITY\n(%)', fontsize=y_fontsize, labelpad=14)
ax[5].set_ylabel('ATMOSPHERIC\nPRESSURE\n(kPa)', fontsize=y_fontsize, labelpad=7)
ax[1].legend(bbox_to_anchor=(1.09, 0.5 ), loc='center', borderaxespad=0.,fontsize=9,handletextpad=0.33,labelspacing=0.35,ncol=1,columnspacing=0.4)
ax[2].legend(bbox_to_anchor=(1.09, 0.5 ), loc='center', borderaxespad=0.,fontsize=9,handletextpad=0.33,labelspacing=0.35,ncol=1,columnspacing=0.4)
ax[3].legend(bbox_to_anchor=(1.09, 0.5 ), loc='center', borderaxespad=0.,fontsize=9,handletextpad=0.33,labelspacing=0.35,ncol=1,columnspacing=0.4)
ax[4].legend(bbox_to_anchor=(1.09, 0.5 ), loc='center', borderaxespad=0.,fontsize=9,handletextpad=0.33,labelspacing=0.35,ncol=1,columnspacing=0.4)
ax[5].legend(bbox_to_anchor=(1.09, 0.5 ), loc='center', borderaxespad=0.,fontsize=9,handletextpad=0.33,labelspacing=0.35,ncol=1,columnspacing=0.4)


ax[3].xaxis.set_major_formatter(mdates.DateFormatter('%b/%d'))
#ax[3].xaxis.set_major_formatter(mdates.DateFormatter('%d/%b/%y'))
ax[5].set_xlabel('DATE')
plt.show(block=False)

#fig.savefig('figure/figure_update/plot_weather.png', format='png', dpi=600)
fig.savefig('figure/figure_update/update_to_2021/plot_weather.png', format='png', dpi=600)
#sp_sch[sch_name].df.iloc[::4].to_csv('output_data/'+'column_qal'+'.csv')
sp_sch[sch_name].df.to_csv('output_data/'+'column_qal_1h_mkevy'+'.csv')
#fig.close()




