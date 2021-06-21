fig, ax1 = plt.subplots(figsize=(15,10))
for axis in ['top','bottom','left','right']:
    i.spines[axis].set_linewidth(2)
#plt.plot(df_mean.index,df_mean['cumsum_net_water_pos_out_m']*1000,'-c',label='From weather station')
#plt.plot(df_mean.index,(85.-df_mean['total_moisture_cm'])*0.01*1000,'brown',label='From moisture profile')
ax1.plot(df_mean.index,watermass_from_weather_station,'-c',linewidth=1.7,label='Calculated from weather station')
#plt.plot(df_mean.index[mask2],df_mean['cumsum_net_water_storage_m'][mask2]*1000+1200,'-c',linewidth=1.7,label='Calculated from weather station')
ax1.plot(df_mean.index,watermass_from_moisture_profile,'brown',linewidth=1.7,label='Calculated from moisture profile')
ax1.tick_params(axis='y',labelsize=28)
ax1.set_ylim([0,900])

ax2=ax1.twinx()
#ax2.bar(df_mean.index, df_last['distance_to_surfsoil'], width=1.8,edgecolor='white',lw=0.1)
ax2.plot(df_mean.index, df_last['distance_to_surfsoil']*1000, '-',color='peru',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r')
ax2.tick_params(axis='y',colors='peru',labelsize=28)
#ax2.plot(, settle_mmo1,'-',color='peru',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r')
#ax2.plot(df_mean.index, settle_mmo3,'-',color='peru',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r')
#ax2.plot(df_mean.index, settle_mmo4,'-',color='peru',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r')
#ax2.plot(df_mean.index, settle_mmo5,'-',color='peru',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r')
ax2.set_ylim([-1,450])

#-----plot surface moisture---------------
#ax2.plot(ta['date_time'][::mkevy].values,mo_surf[::mkevy].values,'-',color='peru',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r')
#ax2.set_ylim([-0.05,0.8])


#ax.vline(time_end_mmo0, 0,900,colors='peru', linestyles='-', linewidth=2).set_zorder(2)
#ax.vline(time_end_mmo1, 0,900,colors='peru', linestyles='-', linewidth=2).set_zorder(2)
#ax.vline(time_end_mmo3, 0,900,colors='peru', linestyles='-', linewidth=2).set_zorder(2)
#ax.vline(time_end_mmo4, 0,900,colors='peru', linestyles='-', linewidth=2).set_zorder(2)
#ax.vline(time_end_mmo5, 0,900,colors='peru', linestyles='-', linewidth=2).set_zorder(2)


mondays=MonthLocator()
locate=MonthLocator(range(1,13),bymonthday=1,interval=4)
#ax1.xaxis.set_major_locator(locate)
#ax1.xaxis.set_minor_locator(mondays)
#ax.xaxis.set_major_formatter(mdates.DateFormatter('%b/%d'))
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%b/%y'))
ax1.tick_params(axis='x',labelsize=22)
ax1.set_xlabel('DATE',fontsize=28)
#ax.set_ylabel('WATER LOSS FROM COLUMN (mm)')
ax1.set_ylabel('EQUIVALENT WATER STORAGE\nIN COLUMN (mm)',fontsize=28, labelpad=6)
ax2.set_ylabel('DISTANCE TO SOIL SURFACE\n (mm)',fontsize=28,color='peru', labelpad=6)
ax1.legend(bbox_to_anchor=(0.3, 0.999 ), loc='upper left', borderaxespad=0.,fontsize=26,handletextpad=0.4,labelspacing=0.3,ncol=1,columnspacing=0.1)
ax1.grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
fig.savefig('figure/update/plot_water_balance_over_time.png', format='png', dpi=100)

