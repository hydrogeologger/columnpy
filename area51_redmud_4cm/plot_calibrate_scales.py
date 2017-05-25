
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
y_fontsize=25
#fig, ax = plt.subplots(2,sharex=True,figsize=(15,15))
import matplotlib.pylab as pylab
params = {'legend.fontsize': 'x-large',
          'figure.figsize': (10, 5),
         'axes.labelsize': 10,
         'axes.titlesize':'large',
         'xtick.labelsize':'20',
         'ytick.labelsize':'20'}
#         'axes.grid':'linewidth=grid_width,color = '0.5''}
#         'linewidth':lw,'markers.size':ms,'markers.edgewidth':mew}
pylab.rcParams.update(params)
fig = plt.figure(figsize=(15,15))



for i in ax:
  for axis in ['top','bottom','left','right']:
    i.spines[axis].set_linewidth(2)

sp.te_fit=np.polyfit(sp.df['commercial'],sp.df['te'],1)
legend_string_second_te="%.3e" % sp.te_fit[0] + ' * x +' "%.3e" % sp.te_fit[1]
legend_string_first_te="%.3e" % sp.te_fit[0] + ' * x +' "%.3e" % sp.te_fit[1]


plt.plot(sp_sch['redmud_first'].df['commercial']*sp.te_fit[0]
    +sp.te_fit[1], sp_sch['redmud_first'].df['commercial']  ,'r-',linewidth=lw,label=legend_string_second_te)
plt.plot(sp_sch['redmud_first'].df['te'],sp_sch['redmud_first'].df['commercial'], 'kx',
    linewidth=lw,markersize=ms,markeredgewidth=mew,label='Experiment 1')
plt.plot(sp_sch['redmud_second'].df['te'],sp_sch['redmud_second'].df['commercial'] ,'k+',
    linewidth=lw,markersize=ms,markeredgewidth=mew,label='Experiment 2')


# show grid with gray color
plt.grid(linewidth=grid_width,color = '0.5')
plt.xlabel('RAW READING FROM LOAD CELL A', fontsize=y_fontsize, labelpad=15)
plt.ylabel('READING FROM COMMERCIAL BALANCE (G)', fontsize=y_fontsize, labelpad=15)
plt.legend(bbox_to_anchor=(.02, 0.90), loc=2, borderaxespad=0.)
plt.show(block=False)


fig.savefig('plot_calibrate_scales.png', format='png', dpi=500)
