
# this script is used for calibrating load cells
import matplotlib.pylab as pylab
params = {'legend.fontsize': 'x-large',
          'figure.figsize': (15, 5),
         'axes.labelsize': 'x-large',
         'axes.titlesize':'x-large',
         'xtick.labelsize':'x-large',
         'ytick.labelsize':'x-large'}
pylab.rcParams.update(params)

lw=4
ms=8
mew=1
grid_width=2
y_fontsize=18
fig, ax = plt.subplots(2,sharex=True,figsize=(15,15))

for i in ax:
  for axis in ['top','bottom','left','right']:
    i.spines[axis].set_linewidth(2)

for sch in sp_sch:
    sp_sch[sch]['te_fit']=np.polyfit(sp_sch[sch]['df']['commercial'],sp_sch[sch]['df']['te'],1)
    sp_sch[sch]['tas606_fit']=np.polyfit(sp_sch[sch]['df']['commercial'],sp_sch[sch]['df']['tas606'],1)
legend_string_second_te="%.3e" % sp_sch['coal_second']['te_fit'][0] + ' * x +' "%.3e" % sp_sch['coal_second']['te_fit'][1]
legend_string_second_tas606="%.3e" % sp_sch['coal_second']['tas606_fit'][0] + ' * x +' "%.3e" % sp_sch['coal_second']['tas606_fit'][1]
legend_string_third_te="%.3e" % sp_sch['coal_third']['te_fit'][0] + ' * x +' "%.3e" % sp_sch['coal_third']['te_fit'][1]
legend_string_third_tas606="%.3e" % sp_sch['coal_third']['tas606_fit'][0] + ' * x +' "%.3e" % sp_sch['coal_third']['tas606_fit'][1]


ax[0].plot(sp_sch['coal_second']['df']['commercial'], sp_sch['coal_second']['df']['commercial']*sp_sch['coal_second']['te_fit'][0]
    +sp_sch['coal_second']['te_fit'][1]  ,'r-',linewidth=lw,label=legend_string_second_te)
ax[0].plot(sp_sch['coal_third']['df']['commercial'], sp_sch['coal_third']['df']['commercial']*sp_sch['coal_third']['te_fit'][0]
    +sp_sch['coal_third']['te_fit'][1]  ,'b-',linewidth=lw,label=legend_string_third_te)
ax[0].plot(sp_sch['coal_second']['df']['commercial'], sp_sch['coal_second']['df']['te'],'k+',
    linewidth=lw,markersize=ms,markeredgewidth=mew,label='experiment 2')
ax[0].plot(sp_sch['coal_third']['df']['commercial'], sp_sch['coal_third']['df']['te'],'kx', 
    linewidth=lw,markersize=ms,markeredgewidth=mew,label='experiment 3')
ax[0].set_title('(A)',x=0.03,y=1.03)


ax[1].plot(sp_sch['coal_second']['df']['commercial'], sp_sch['coal_second']['df']['commercial']*sp_sch['coal_second']['tas606_fit'][0]
    +sp_sch['coal_second']['tas606_fit'][1]  ,'r-',linewidth=lw,label=legend_string_second_tas606)
ax[1].plot(sp_sch['coal_third']['df']['commercial'], sp_sch['coal_third']['df']['commercial']*sp_sch['coal_third']['tas606_fit'][0]
    +sp_sch['coal_third']['tas606_fit'][1]  ,'b-',linewidth=lw,label=legend_string_third_tas606)
ax[1].plot(sp_sch['coal_second']['df']['commercial'], sp_sch['coal_second']['df']['tas606'],'k+', 
    linewidth=lw,markersize=ms,markeredgewidth=mew,label='experiment 2')
ax[1].plot(sp_sch['coal_third']['df']['commercial'], sp_sch['coal_third']['df']['tas606'],'kx', 
    linewidth=lw,markersize=ms,markeredgewidth=mew,label='experiment 3')
# show grid with gray color
ax[0].grid(linewidth=grid_width,color = '0.5')
ax[1].grid(linewidth=grid_width,color = '0.5')
ax[0].set_ylabel('RAW READING FROM LOAD CELL A', fontsize=y_fontsize, labelpad=65)
ax[1].set_ylabel('RAW READING FROM LOAD CELL B', fontsize=y_fontsize, labelpad=30)
ax[1].set_xlabel('READING FROM COMMERCIAL BALANCE (G)', fontsize=y_fontsize,labelpad=20)
ax[1].set_ylim([155000,230000])
ax[0].legend(bbox_to_anchor=(.02, 0.90), loc=2, borderaxespad=0.)
ax[1].legend(bbox_to_anchor=(.02, 0.90), loc=2, borderaxespad=0.)
ax[1].set_title('(B)',x=0.03,y=1.03)
plt.show(block=False)


fig.savefig('plot_calibrate_scales.png', format='png', dpi=500)
