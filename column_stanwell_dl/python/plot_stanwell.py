import matplotlib
import matplotlib.image as image
import matplotlib.pylab as pylab

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
grid_width=2
y_fontsize=11
fig, ax = plt.subplots(7,sharex=True,figsize=(9,12))
fig.subplots_adjust(hspace=.10)
fig.subplots_adjust(left=0.17, right=0.89, top=0.97, bottom=0.05)


#fig, ax = plt.subplots(6,sharex=True,figsize=(6,8))
#fig.subplots_adjust(hspace=.15)
mkevy=4


for i in ax:
  for axis in ['top','bottom','left','right']:
    i.spines[axis].set_linewidth(2)

ta=sp_sch['stanwell'].df
ta['radiation']=(ta['ir_up_concat']-254)/20.512
df_mean['radiation']=(df_mean['ir_up_concat']-254)/20.512

#ax[0].plot(ta['date_time'], ta['rainmm'], '-',color='maroon',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Dielectric suction A')
#ax[0].set_ylim([-1,19])
ax[0].bar(df_mean.index, df_last['rainmm'], width=1.0)

##ax[1].plot(ta['date_time'], (ta['ir_up']-ta['ir_down'])*0.007+0.2*ta['wdspdkphavg2m'].fillna(0), '-',color='maroon',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Dielectric suction A')
#plt.figure()
#plt.plot(ta['date_time'], (ta['radiation'])*0.007+0.2*ta['wdspdkphavg2m'].fillna(0), '-',color='maroon',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Dielectric suction A')
##plt.plot(ta['date_time'], 0.2*ta['wdspdkphavg2m'].fillna(0), '-',color='maroon',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Dielectric suction A')

#ax[1].plot(ta['date_time'], (ta['radiation'])*0.007+0.2*ta['wdspdkphavg2m'].fillna(0), '-',color='maroon',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Dielectric suction A')
#ax[1].set_ylim([-0.100,9])
#temp= df_mean['radiation']*0.007+0.2*df_mean['wdspdkphavg2m'].fillna(0)
#ax[1].bar(df_mean.index, temp, width=1.0)
#ax[1].bar(df_mean.index,-df_mean['evap_rate_ee']*2, width=1.0)

ax[1].bar(df_mean.index,df_mean['pet_mmPday'],width=1.0,color='brown',label='Pote.\nevap.')
ax[1].bar(df_mean.index,df_mean['aet_mmPday'],width=1.0,color='orange',label='Actu.\nevap.')


#ax[2].plot(ta['date_time'], -(ta['pre0']-60), 'r-',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='30 cm below soil surface')
#ax[2].plot(ta['date_time'], -(ta['pre1']-110), 'g-',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='60 cm below soil surface')
#ax[2].set_ylim([-10-110,140-110])
#ax[2].set_ylim([-140+110,120,])
#ax[2].set_ylim([-140+110,120,])
ax[2].plot(ta['date_time'], ta['pre0'], '-',color='cyan',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='50 cm')
ax[2].plot(ta['date_time'], ta['pre1'], '-',color='darkblue',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='100 cm')
#ax[2].set_ylim([-10-110,140-110])
ax[2].set_ylim([-100,1300])

#ax[2].bar(df_mean.index,-df_mean['evap_rate_ee']*10, width=1.0)
##ax[2].bar(df_mean.index,-df_mean['evap_rate_ee']*10)
#ax[2].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')


#ax[2].plot(df_mean.index,df_mean['cumsum_net_water_pos_out_m'],'-c',label='')
#ax[2].plot(df_mean.index,(85.-df_mean['total_moisture_cm'])*0.01,'brown',label='')



ax[3].plot(ta['date_time'][::mkevy].values, ta['tmp0'][::mkevy].values, '-' ,color='maroon',linewidth=lw,markersize=ms           ,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='1 cm',markevery=mkevy)
ax[3].plot(ta['date_time'][::mkevy].values, ta['tmp1'][::mkevy].values, '-' ,color='olive',linewidth=lw,markersize=ms           ,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='5 cm',markevery=mkevy)
ax[3].plot(ta['date_time'][::mkevy].values, ta['tmp2'][::mkevy].values, '-' ,color='peru',linewidth=lw,markersize=ms           ,markeredgewidth=mew,fillstyle='full', markeredgecolor='b',label='8 cm',markevery=mkevy)
ax[3].plot(ta['date_time'][::mkevy].values, ta['tmp3'][::mkevy].values, '-' ,color='pink',linewidth=lw,markersize=ms           ,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='13cm',markevery=mkevy)
ax[3].plot(ta['date_time'][::mkevy].values, ta['tmp4'][::mkevy].values, '-' ,color='gold',linewidth=lw,markersize=ms           ,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='20cm',markevery=mkevy)
#ax[3].plot(ta['date_time'][::mkevy].values, ta['tmp5'][::mkevy].values, '-' ,color='lightgreen',linewidth=lw,markersize=ms           ,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='28cm',markevery=mkevy)
ax[3].plot(ta['date_time'][::mkevy].values, ta['tmp6'][::mkevy].values, '-' ,color='lightblue'  ,linewidth=lw,markerfacecolor='brown' ,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='38cm',markevery=mkevy)
ax[3].plot(ta['date_time'][::mkevy].values, ta['tmp7'][::mkevy].values, '-' ,color='cyan' ,linewidth=lw,markerfacecolor='yellow',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='yellow',label='48cm',markevery=mkevy)
#ax[3].plot(ta['date_time'][::mkevy].values, ta['tmp8'][::mkevy].values, '-' ,color='royalblue',linewidth=lw,markerfacecolor='orange',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='orange',label='70cm',markevery=mkevy)
ax[3].plot(ta['date_time'][::mkevy].values, ta['tmp9'][::mkevy].values, '-' ,color='darkblue'   ,linewidth=lw,markerfacecolor='grey'  ,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='grey',label='85cm',markevery=mkevy)
ax[3].set_ylim([5,40])

mkevy=24

ax[4].plot(ta['date_time'][::mkevy], ta['mmo0'][::mkevy], '-',color='maroon',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='1 cm',markevery=mkevy)
ax[4].plot(ta['date_time'][::mkevy], ta['mmo1'][::mkevy], '-',color='olive',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='5 cm',markevery=mkevy)
ax[4].plot(ta['date_time'][::mkevy], ta['mmo2'][::mkevy], '-',color='peru',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='b',label='8 cm',markevery=mkevy)
ax[4].plot(ta['date_time'][::mkevy], ta['mmo3'][::mkevy], '-',color='pink',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='13cm',markevery=mkevy)
ax[4].plot(ta['date_time'][::mkevy], ta['mmo4'][::mkevy], '-',color='gold',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='20cm',markevery=mkevy)
ax[4].plot(ta['date_time'][::mkevy], ta['mmo5'][::mkevy], '-',color='lightgreen',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='28cm',markevery=mkevy)
ax[4].plot(ta['date_time'][::mkevy], ta['mmo6'][::mkevy], '-' ,color='lightblue',linewidth=lw ,markerfacecolor='brown' ,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='38cm',markevery=mkevy)
ax[4].plot(ta['date_time'][::mkevy], ta['mmo7'][::mkevy], '-' ,color='cyan',linewidth=lw, markerfacecolor='yellow' ,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='yellow',label='48cm',markevery=mkevy)
ax[4].plot(ta['date_time'][::mkevy], ta['mmo8'][::mkevy], '-' ,color='royalblue',linewidth=lw,markerfacecolor='crimson' ,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='crimson',label='70cm',markevery=mkevy)
ax[4].plot(ta['date_time'][::mkevy], ta['mmo9'][::mkevy], '-' ,color='darkblue',linewidth=lw,markerfacecolor='pink' ,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='pink',label='85cm',markevery=mkevy)
ax[4].set_ylim([-0.1,0.8])

ax[5].plot(ta['date_time'], ta['ec0']/1000., '-',color='olive',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='5 cm')
ax[5].plot(ta['date_time'], ta['ec2']/1000., '-',color='royalblue',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='60cm')
ax[5].set_ylim([-0.2,1.7])

ax[6].plot(daily_data_manual.index, daily_data_manual['settlement_mm'], '-',color='maroon',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='5 cm')
ax[6].set_ylim([-1,101])


ax[0].set_ylabel('DAILY\nACCUMULATED\nRAINFALL (mm)', fontsize=y_fontsize, labelpad=15)
ax[1].set_ylabel('DAILY\nEVAPORATION\n(mm)', fontsize=y_fontsize, labelpad=15)
ax[2].set_ylabel('WATER\nPRESSURE\n(mm)', fontsize=y_fontsize, labelpad=5)
ax[3].set_ylabel('TEMPERATURE\nBELOW COLUMN\nSURFACE\n($^\circ$C)', fontsize=y_fontsize, labelpad=17)
ax[4].set_ylabel('VOL. MOIS.\nCONTENT\nBELOW COLUMN\nSURFACE', fontsize=y_fontsize, labelpad=7)
ax[5].set_ylabel('ELECTRICAL\nCONDUCTIVITY\nBELOW COLUMN\nSURFACE \n(dS/m)', fontsize=y_fontsize, labelpad=15)
ax[6].set_ylabel('SURFACE \n SETTLEMENT\n(mm)', fontsize=y_fontsize, labelpad=15)

ax[0].set_title('(A)',x=0.04,y=0.8,fontweight='bold')
ax[1].set_title('(B)',x=0.04,y=0.8,fontweight='bold')
ax[2].set_title('(C)',x=0.04,y=0.8,fontweight='bold')
ax[3].set_title('(D)',x=0.04,y=0.8,fontweight='bold')
ax[4].set_title('(E)',x=0.04,y=0.8,fontweight='bold')
ax[5].set_title('(F)',x=0.04,y=0.8,fontweight='bold')
ax[6].set_title('(G)',x=0.04,y=0.8,fontweight='bold')
ax[0].set_axisbelow(True)
ax[1].set_axisbelow(True)
ax[2].set_axisbelow(True)
ax[3].set_axisbelow(True)
ax[4].set_axisbelow(True)
ax[5].set_axisbelow(True)
ax[1].legend(bbox_to_anchor=(1.07, 0.5 ), loc='center', borderaxespad=0.,fontsize=9,handletextpad=0.83,labelspacing=1.32,ncol=1,columnspacing=0.4)
ax[2].legend(bbox_to_anchor=(1.07, 0.5 ), loc='center', borderaxespad=0.,fontsize=9,handletextpad=0.03,labelspacing=0.02,ncol=1,columnspacing=0.4)
ax[3].legend(bbox_to_anchor=(1.07, 0.5 ), loc='center', borderaxespad=0.,fontsize=9,handletextpad=0.03,labelspacing=0.02,ncol=1,columnspacing=0.4)
ax[4].legend(bbox_to_anchor=(1.07, 0.5 ), loc='center', borderaxespad=0.,fontsize=9,handletextpad=0.03,labelspacing=0.02,ncol=1,columnspacing=0.4)
ax[5].legend(bbox_to_anchor=(1.07, 0.5 ), loc='center', borderaxespad=0.,fontsize=9,handletextpad=0.03,labelspacing=0.02,ncol=1,columnspacing=0.4)


#ax[1].label_params(labeltop='off', labelright='off')
#ax[2].label_params(labeltop='off', labelright='off')
#ax[3].label_params(labeltop='off', labelright='off')
#ax[4].label_params(labeltop='off', labelright='off')
#ax[5].label_params(labeltop='off', labelright='off')
#ax[0].legend(bbox_to_anchor=(.8, 0.9), loc=2, borderaxespad=0.,fontsize=9,handletextpad=0.13,labelspacing=0.05)
#ax[1].legend(bbox_to_anchor=(.8, 0.85), loc=2, borderaxespad=0.,fontsize=9,handletextpad=0.13,labelspacing=0.05)
#ax[2].legend(bbox_to_anchor=(.03, 0.85), loc=2, borderaxespad=0.,fontsize=8,handletextpad=0.13,labelspacing=0.05)
#ax[3].legend(bbox_to_anchor=(.77, 0.99 ), loc=2, borderaxespad=0.,fontsize=8,handletextpad=0.03,labelspacing=0.02,ncol=2,columnspacing=0.4)
#ax[4].legend(bbox_to_anchor=(.8, 0.7), loc=2, borderaxespad=0.,fontsize=8,handletextpad=0.03,labelspacing=0.02,ncol=2,columnspacing=0.4)#title='CM below surface')
#plt.setp(ax[3].get_legend().get_title(), fontsize='8') 
#ax[4].legend(bbox_to_anchor=(.8, 0.9 ), loc=2, borderaxespad=0.,fontsize=9,handletextpad=0.13,labelspacing=0.05)

ax[0].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
ax[1].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
ax[2].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
ax[3].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
ax[4].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
ax[5].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
ax[6].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')

ax[5].xaxis.set_major_formatter(mdates.DateFormatter('%b/%d'))
ax[6].set_xlabel('DATE')
#plt.xticks(rotation=45)
plt.show(block=False)



fig.savefig('figure/plot_stanwell.png', format='png', dpi=600)
#    plt.close()
