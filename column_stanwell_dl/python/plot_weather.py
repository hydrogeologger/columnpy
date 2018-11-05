import matplotlib
import matplotlib.image as image

lw=4
ms=1
mew=1.5
grid_width=2
y_fontsize=12



fig, ax = plt.subplots(6,sharex=True,figsize=(8,9))
#fig.subplots_adjust(hspace=.15)
fig.subplots_adjust(left=0.18, right=0.90, top=0.97, bottom=0.08)
mkevy=4


df_mean = sp_sch['stanwell'].df.resample('D').mean()
# the original time for mean value is at 12am, we shift it to 12pm
#df_mean['date_time']=df_mean['date_time']+pd.to_timedelta(12, unit='h')
#df_mean['date_time']=df_mean.index

df_mean.index=df_mean.index+pd.to_timedelta(12, unit='h')
df_mean['date_time']=df_mean.index

# it is not necessary to remove the night result and folcus on only the day time results as the number of point after interpolation is the same per day. 
#new = old.filter(['A','B','D'], axis=1)




for i in ax:
  for axis in ['top','bottom','left','right']:
    i.spines[axis].set_linewidth(2)

ta=sp_sch['stanwell'].df

ax[0].plot(ta['date_time'], ta['rainmm'], '-',color='maroon',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Dielectric suction A')

ax[1].plot(ta['date_time'], (ta['ir_up_concat']-254)/20.512, '-',color='maroon',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Incoming')
ax[1].plot(df_mean['date_time'], (df_mean['ir_up_concat']-254)/20.512, 'g-',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='Gust at 2m above ground',markevery=5)
ax[1].set_ylim([-5,1200])
#ax[1].plot(ta['date_time'], ta['ir_up'], '-',color='maroon',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Incoming')
#ax[1].plot(ta['date_time'], ta['ir_down'], 'g-',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Reflected')
#ax[1].set_ylim([-50,30200])


#plt.figure()
#plt.plot(ta['date_time'], ta['wdspdkphavg2m'])
ax[2].plot(ta['date_time'], ta['wdspdkphavg2m'], '-',color='maroon',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Average at 2m above ground')
ax[2].plot(ta['date_time'], ta['wdgstkph10m']/2.0, 'ko',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='Gust at 2m above ground',markevery=5)
#ax[4].plot(ta['date_time'], ta['ec1'], 'g-',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Dielectric suction A')
ax[2].set_ylim([-1,15])

#ax[3].plot(ta['date_time'][::mkevy].values, ta['tp_box_7'][::mkevy].values, 'g-',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='Electrical Enclosure',markevery=mkevy)
ax[3].plot(ta['date_time'][::mkevy].values, ta['tc'][::mkevy].values, '-',color='maroon',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Radiation Shield',markevery=mkevy)
ax[3].plot(df_mean['date_time'], df_mean['tc'], 'g-',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='Gust at 2m above ground',markevery=5)
ax[3].set_ylim([5,33])

mkevy=12
#ax[4].plot(ta['date_time'][::mkevy], ta['rh_box_7'][::mkevy], 'g-',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='Electrical Enclosure',markevery=mkevy)
mkevy=6
ax[4].plot(ta['date_time'][::mkevy], ta['rh'][::mkevy], '-',color='maroon',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Radiation Shield',markevery=mkevy)
ax[4].plot(df_mean['date_time'], df_mean['rh'], 'g-',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='Gust at 2m above ground',markevery=5)
ax[4].set_ylim([0,100])


ax[5].plot(ta['date_time'], ta['p']/1000, '-',color='maroon',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Dielectric suction A')
ax[5].plot(df_mean['date_time'], df_mean['p']/1000, 'g-',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='Gust at 2m above ground',markevery=5)
ax[5].set_ylim([100,103])



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
ax[0].set_ylabel('DAILY\nACCUMULATED\nRAINFALL (mm)', fontsize=y_fontsize, labelpad=12)
ax[1].set_ylabel('SOLAR\nRADIATION\n(W/m$^{2}$)', fontsize=y_fontsize, labelpad=10)
ax[2].set_ylabel('WIND\nSPEED\n(m/s)', fontsize=y_fontsize, labelpad=20)
ax[3].set_ylabel('TEMPERATURE\n($^\circ$C)', fontsize=y_fontsize, labelpad=20)
ax[4].set_ylabel('RELATIVE\nHUMIDITY\n(%)', fontsize=y_fontsize, labelpad=15)
ax[5].set_ylabel('ATMOSPHERIC\nPRESSURE\n(kPa)', fontsize=y_fontsize, labelpad=5)
ax[1].legend(bbox_to_anchor=(1.07, 0.5 ), loc='center', borderaxespad=0.,fontsize=9,handletextpad=0.03,labelspacing=0.02,ncol=1,columnspacing=0.4)
ax[2].legend(bbox_to_anchor=(1.07, 0.5 ), loc='center', borderaxespad=0.,fontsize=9,handletextpad=0.03,labelspacing=0.02,ncol=1,columnspacing=0.4)
ax[3].legend(bbox_to_anchor=(1.07, 0.5 ), loc='center', borderaxespad=0.,fontsize=9,handletextpad=0.03,labelspacing=0.02,ncol=1,columnspacing=0.4)
#ax[1].legend(bbox_to_anchor=(.70, 0.99 ), loc=2, borderaxespad=0.,fontsize=8,handletextpad=0.03,labelspacing=0.02,ncol=2,columnspacing=0.4)
#ax[2].legend(bbox_to_anchor=(.63, 0.95), loc=2, borderaxespad=0.,fontsize=8,handletextpad=0.13,labelspacing=0.05)
#ax[3].legend(bbox_to_anchor=(.55, 0.99 ), loc=2, borderaxespad=0.,fontsize=8,handletextpad=0.03,labelspacing=0.02,ncol=2,columnspacing=0.4)
#ax[4].legend(bbox_to_anchor=(.55, 0.99 ), loc=2, borderaxespad=0.,fontsize=8,handletextpad=0.03,labelspacing=0.02,ncol=2,columnspacing=0.4)
#





ax[3].xaxis.set_major_formatter(mdates.DateFormatter('%b/%d'))
ax[5].set_xlabel('DATE')
plt.show(block=False)

fig.savefig('figure/plot_weather.png', format='png', dpi=600)
sp_sch[sch_name].df.iloc[::4].to_csv('output_data/'+'column_stanwell'+'.csv')




