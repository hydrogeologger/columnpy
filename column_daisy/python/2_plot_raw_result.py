
###################################################################################################
sp=1
del sp
sp=pandas_scale.concat_data_roof(pd.Timestamp('2017-10-04 04:03:07'),  pd.Timestamp('2017-08-15 01:40:01'),dt_s)
plot_switch=False
sp.merge_data( df=data.df, keys=['saltrh_2_rh'] ,plot=plot_switch ,coef=5e-10)
sp.merge_data( df=data.df, keys=['saltrh_11_rh'],plot=plot_switch ,coef=5e-10)
sp.merge_data( df=data.df, keys=['t_2896_begin'],plot=plot_switch ,coef=5e-10)
sp.merge_data( df=data.df, keys=['t_19_begin']  ,plot=plot_switch ,coef=5e-10)
sp.merge_data( df=data.df, keys=['t_14_begin']  ,plot=plot_switch ,coef=5e-10)

sp.merge_data( df=data.df, keys=['t_2896_peak'] ,plot=plot_switch ,coef=5e-10)
sp.merge_data( df=data.df, keys=['t_19_peak']   ,plot=plot_switch ,coef=5e-10)
sp.merge_data( df=data.df, keys=['t_14_peak']   ,plot=plot_switch ,coef=5e-10)

sp.merge_data( df=data.df, keys=['t_2896_end']  ,plot=plot_switch ,coef=5e-10)
sp.merge_data( df=data.df, keys=['t_19_end']    ,plot=plot_switch ,coef=5e-10)
sp.merge_data( df=data.df, keys=['t_14_end']    ,plot=plot_switch ,coef=5e-10)

sp.merge_data( df=data.df, keys=['saltrh_11_t'] ,plot=plot_switch ,coef=5e-10)
sp.merge_data( df=data.df, keys=['saltrh_2_t']  ,plot=plot_switch ,coef=5e-10)

sp.merge_data( df=data.df, keys=['mo_7']        ,plot=plot_switch  ,coef=5e-10)
sp.merge_data( df=data.df, keys=['mo_8']        ,plot=plot_switch  ,coef=5e-10)
sp.merge_data( df=data.df, keys=['mo_9']        ,plot=plot_switch  ,coef=5e-10)
sp.merge_data( df=data.df, keys=['mo_10']       ,plot=plot_switch  ,coef=5e-10)

sp.merge_data( df=data.df, keys=['te']          ,plot=plot_switch  ,coef=5e-10)
sp.merge_data( df=data.df, keys=['commercial']  ,plot=plot_switch  ,coef=5e-10)


sp.df['deltat_2896_heat']=sp.df['t_2896_peak']-sp.df['t_2896_begin']
sp.df['deltat_2896_cool']=sp.df['t_2896_peak']-sp.df['t_2896_end']
sp.df['deltat_19_heat']  =sp.df['t_19_peak']  -sp.df['t_19_begin']
sp.df['deltat_19_cool']  =sp.df['t_19_peak']  -sp.df['t_19_end']
sp.df['deltat_14_heat']  =sp.df['t_14_peak']  -sp.df['t_14_begin']
sp.df['deltat_14_cool']  =sp.df['t_14_peak']  -sp.df['t_14_end']



sp.df=sp.df.reset_index(drop=True)
## add new column
## http://stackoverflow.com/questions/12555323/adding-new-column-to-existing-dataframe-in-python-pandas
sp.df=sp.df.assign(
    time_days=[(sp.df['date_time'][x]-sp.df['date_time'][0]).total_seconds()/86400
            for x in range(len(sp.df['date_time']))])





# this script is used for calibrating load cells
import matplotlib.pylab as pylab
params = {'legend.fontsize': 'x-large',
          'figure.figsize': (10, 5),
         'axes.labelsize': 10,
         'axes.titlesize':'large',
         'xtick.labelsize':'12',
         'ytick.labelsize':'12'}
#         'axes.grid':'linewidth=grid_width,color = '0.5''}
#         'linewidth':lw,'markers.size':ms,'markers.edgewidth':mew}
pylab.rcParams.update(params)

lw=4
ms=3
mew=1.5
grid_width=2
y_fontsize=12
fig, ax = plt.subplots(5,sharex=True,figsize=(12,16))
fig.subplots_adjust(hspace=.15)


for i in ax:
  for axis in ['top','bottom','left','right']:
    i.spines[axis].set_linewidth(2)

ax[0].plot(sp.df.time_days, sp.df.te/8.5e-3-14000,'ko'       ,markersize=ms,markeredgewidth=mew, markeredgecolor='k',label='load cell')
ax[0].plot(sp.df.time_days, sp.df.commercial,'gx',markersize=ms,markeredgewidth=mew, markeredgecolor='g',label='commercial balance')

ax[1].plot(sp.df.time_days, sp.df.mo_7, 'ro',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Dielectric suction A')
ax[1].plot(sp.df.time_days, sp.df.mo_8, 'go',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='Dielectric suction B')
ax[1].plot(sp.df.time_days, sp.df.mo_9, 'bo',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='b',label='Moisture A')
ax[1].plot(sp.df.time_days, sp.df.mo_10,'ko',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='Moisture B')


ax[2].plot(sp.df.time_days, sp.df.t_2896_begin, 'ro',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Fred. Suc. A')
ax[2].plot(sp.df.time_days, sp.df.t_19_begin, 'go',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='Fred. Suc. B')
ax[2].plot(sp.df.time_days, sp.df.t_14_begin, 'bo',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='b',label='Fred. Suc. C')
ax[2].plot(sp.df.time_days, sp.df.saltrh_2_t, 'co',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='Temp.&Hum. A')
ax[2].plot(sp.df.time_days, sp.df.saltrh_11_t,'mo',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='Temp.&Hum. B')

ax[3].plot(sp.df.time_days, sp.df.deltat_2896_heat, 'ro',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Temp. rise of Fred. Suc. A')
ax[3].plot(sp.df.time_days, sp.df.deltat_19_heat, 'go',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='Temp. rise of Fred. Suc. B')
ax[3].plot(sp.df.time_days, sp.df.deltat_14_heat, 'bo',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='b',label='Temp. rise of Fred. Suc. C')

ax[4].plot(sp.df.time_days, sp.df.saltrh_2_rh, 'ro',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Temp.&Hum. A')
ax[4].plot(sp.df.time_days, sp.df.saltrh_11_rh,'go',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='Temp.&Hum. B')

#for sch in sp_sch:
#    sp_sch[sch]['te_fit']=np.polyfit(sp_sch[sch]['df']['commercial'],sp_sch[sch]['df']['te'],1)
#    sp_sch[sch]['tas606_fit']=np.polyfit(sp_sch[sch]['df']['commercial'],sp_sch[sch]['df']['tas606'],1)
#legend_string_second_te="%.3e" % sp_sch['coal_second']['te_fit'][0] + ' * x +' "%.3e" % sp_sch['coal_second']['te_fit'][1]
#legend_string_second_tas606="%.3e" % sp_sch['coal_second']['tas606_fit'][0] + ' * x +' "%.3e" % sp_sch['coal_second']['tas606_fit'][1]
#legend_string_third_te="%.3e" % sp_sch['coal_third']['te_fit'][0] + ' * x +' "%.3e" % sp_sch['coal_third']['te_fit'][1]
#legend_string_third_tas606="%.3e" % sp_sch['coal_third']['tas606_fit'][0] + ' * x +' "%.3e" % sp_sch['coal_third']['tas606_fit'][1]
#
#
#ax[0].plot(sp_sch['coal_second']['df']['commercial'], sp_sch['coal_second']['df']['commercial']*sp_sch['coal_second']['te_fit'][0]
#    +sp_sch['coal_second']['te_fit'][1]  ,'r-',linewidth=lw,label=legend_string_second_te)
#ax[0].plot(sp_sch['coal_third']['df']['commercial'], sp_sch['coal_third']['df']['commercial']*sp_sch['coal_third']['te_fit'][0]
#    +sp_sch['coal_third']['te_fit'][1]  ,'b-',linewidth=lw,label=legend_string_third_te)
#ax[0].plot(sp_sch['coal_second']['df']['commercial'], sp_sch['coal_second']['df']['te'],'k+',
#    linewidth=lw,markersize=ms,markeredgewidth=mew,label='experiment 2')
#ax[0].plot(sp_sch['coal_third']['df']['commercial'], sp_sch['coal_third']['df']['te'],'kx', 
#    linewidth=lw,markersize=ms,markeredgewidth=mew,label='experiment 3')
#ax[0].set_title('(A)',x=0.03,y=1.03)
#
#
#ax[1].plot(sp_sch['coal_second']['df']['commercial'], sp_sch['coal_second']['df']['commercial']*sp_sch['coal_second']['tas606_fit'][0]
#    +sp_sch['coal_second']['tas606_fit'][1]  ,'r-',linewidth=lw,label=legend_string_second_tas606)
#ax[1].plot(sp_sch['coal_third']['df']['commercial'], sp_sch['coal_third']['df']['commercial']*sp_sch['coal_third']['tas606_fit'][0]
#    +sp_sch['coal_third']['tas606_fit'][1]  ,'b-',linewidth=lw,label=legend_string_third_tas606)
#ax[1].plot(sp_sch['coal_second']['df']['commercial'], sp_sch['coal_second']['df']['tas606'],'k+', 
#    linewidth=lw,markersize=ms,markeredgewidth=mew,label='experiment 2')
#ax[1].plot(sp_sch['coal_third']['df']['commercial'], sp_sch['coal_third']['df']['tas606'],'kx', 
#    linewidth=lw,markersize=ms,markeredgewidth=mew,label='experiment 3')
## show grid with gray color
ax[0].grid(linewidth=grid_width,color = '0.5')
ax[1].grid(linewidth=grid_width,color = '0.5')
ax[2].grid(linewidth=grid_width,color = '0.5')
ax[3].grid(linewidth=grid_width,color = '0.5')
ax[4].grid(linewidth=grid_width,color = '0.5')

ax[2].set_ylim([6,30])
ax[4].set_ylim([50,105])
ax[0].set_ylabel('WEIGHT (G)', fontsize=y_fontsize, labelpad=10)
ax[1].set_ylabel('RAW READING FROM \n DIELECTRIC SENSORS ', fontsize=y_fontsize, labelpad=20)
ax[2].set_ylabel('TEMP. (CELSIUS) ', fontsize=y_fontsize, labelpad=30)
ax[3].set_ylabel('TEMP. DIFF. (CELSIUS) ', fontsize=y_fontsize, labelpad=30)
ax[4].set_ylabel('RELATIVE HUMIDITY', fontsize=y_fontsize, labelpad=23)
ax[4].set_xlabel('TIME (DAYS)', fontsize=y_fontsize,labelpad=3)
#ax[1].set_ylim([155000,230000])
ax[0].legend(bbox_to_anchor=(.75, 0.98), loc=2, borderaxespad=0.,fontsize=10)
ax[1].legend(bbox_to_anchor=(.75, 0.6), loc=2, borderaxespad=0.,fontsize=10)
ax[2].legend(bbox_to_anchor=(.8, 0.7), loc=2, borderaxespad=0.,fontsize=10)
ax[3].legend(bbox_to_anchor=(.7, 0.6 ), loc=2, borderaxespad=0.,fontsize=10)
ax[4].legend(bbox_to_anchor=(.01, 0.3), loc=2, borderaxespad=0.,fontsize=10)
ax[0].set_title('(A)',x=0.02,y=1.0)
ax[1].set_title('(B)',x=0.02,y=1.0)
ax[2].set_title('(C)',x=0.02,y=1.0)
ax[3].set_title('(D)',x=0.02,y=1.0)
ax[4].set_title('(E)',x=0.02,y=1.0)
plt.show(block=False)


fig.savefig('plot_raw_result.png', format='png', dpi=500)

