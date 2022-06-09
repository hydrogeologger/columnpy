fig, ax = plt.subplots(figsize=(15,10))
for axis in ['top','bottom','left','right']:
    i.spines[axis].set_linewidth(2)

#waterMass_from_moisture_profile = df_mean['total_moisture_cm']*constants.cm2mm
#waterMass_from_weather_station = df_mean['cumsum_net_water_storage_m']*constants.m2mm

#diff_water_storage = waterMass_from_moisture_profile.diff()


ax.plot(df_mean.index,waterMass_from_weather_station,'-c',linewidth=1.7,label='Calculated from weather station')
#ax.plot(df_mean.index,diff_water_storage,'brown',linewidth=1.7,label='Calculated from moisture profile')
ax.plot(df_mean.index,waterMass_from_moisture_profile,'brown',linewidth=1.7,label='Calculated from moisture profile')
#ax.tick_params(axis='y',labelsize=28)
ax.tick_params(axis='both',labelsize=25)
ax.set_ylim([0,800])
#ax.set_ylim([0,800])


#ax.xaxis.set_major_formatter(mdates.DateFormatter('%b/%d'))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b/%y'))
ax.set_xlabel('DATE',fontsize=28)
#ax.set_ylabel('WATER LOSS FROM COLUMN (mm)')
ax.set_ylabel('EQUIVALENT WATER STORAGE\nIN COLUMN (mm)',fontsize=28, labelpad=10)
ax.legend(bbox_to_anchor=(0.1, 0.99 ), loc='upper left', borderaxespad=0.,fontsize=20,handletextpad=0.6,labelspacing=1,ncol=1,columnspacing=0.1)
ax.grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')

#fig.savefig('figure/figure_update/update_to_2021/plot_water_balance_over_time.png', format='png', dpi=300)
fig.savefig('figure/figure_update/update_to_2021/plot_water_balance.png', format='png', dpi=300)
