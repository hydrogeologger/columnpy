fig, ax = plt.subplots(figsize=(10,8))
for axis in ['top','bottom','left','right']:
  i.spines[axis].set_linewidth(2)
#plt.plot(df_mean.index,df_mean['cumsum_net_water_pos_out_m']*1000,'-c',label='From weather station')
#plt.plot(df_mean.index,(85.-df_mean['total_moisture_cm'])*0.01*1000,'brown',label='From moisture profile')
plt.plot(df_mean.index,watermass_from_weather_station,'-c',linewidth=1.7,label='Calculated from weather station')
#plt.plot(df_mean.index[mask2],df_mean['cumsum_net_water_storage_m'][mask2]*1000+1200,'-c',linewidth=1.7,label='Calculated from weather station')
plt.plot(df_mean.index,watermass_from_moisture_profile,'brown',linewidth=1.7,label='Calculated from moisture profile')
ax.set_ylim([0,900])



#ax.xaxis.set_major_formatter(mdates.DateFormatter('%b/%d'))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b/%y'))
ax.set_xlabel('DATE',fontsize=12)
#ax.set_ylabel('WATER LOSS FROM COLUMN (mm)')
ax.set_ylabel('EQUIVALENT WATER STORAGE IN COLUMN (mm)',fontsize=12, labelpad=10)
ax.legend(bbox_to_anchor=(0.1, 0.99 ), loc='upper left', borderaxespad=0.,fontsize=12,handletextpad=0.6,labelspacing=1,ncol=1,columnspacing=0.1)
ax.grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
fig.savefig('figure/update/plot_water_balance_over_time.png', format='png', dpi=100)

