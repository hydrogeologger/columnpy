
# this script is used for calibrating load cells


params = {'legend.fontsize': 13,
          'figure.figsize': (10, 5),
         'axes.labelsize': 12,
         'axes.titlesize':'x-large',
         'xtick.labelsize':'20',
         'ytick.labelsize':'20',
#         'ytick.labelweight':'bold',
          'axes.labelsize': 16,
           'axes.labelweight':'bold'}
#         'axes.grid':'linewidth=grid_width,color = '0.5''}
#         'linewidth':lw,'markers.size':ms,'markers.edgewidth':mew}
plt.rcParams["font.weight"] = "bold"
plt.rcParams["axes.labelweight"] = "bold"
pylab.rcParams.update(params)



fig = plt.figure(figsize=(12,12))

fig.subplots_adjust(left=0.18, right=0.98, top=0.99, bottom=0.15)
lw=4
ms=12
mew=4
grid_width=2
y_fontsize=25


ax = fig.add_subplot(111)
for axis in ['top','bottom','left','right']:
  ax.spines[axis].set_linewidth(2) 

sp_sch[sch_name].te_fit=np.polyfit(sp_sch[sch_name].df['commercial'],sp_sch[sch_name].df['te'],1)
legend_string_second_te="%.3e" % sp_sch[sch_name].te_fit[0] + ' * x +' "%.3e" % sp_sch[sch_name].te_fit[1]
legend_string_first_te="%.3e" % sp_sch[sch_name].te_fit[0] + ' * x +' "%.3e" % sp_sch[sch_name].te_fit[1]


plt.plot(sp_sch['redmud_first'].df['commercial']*sp_sch[sch_name].te_fit[0]
    +sp_sch[sch_name].te_fit[1], sp_sch['redmud_first'].df['commercial']  ,'r-',linewidth=lw,label=legend_string_second_te)
plt.plot(sp_sch['redmud_first'].df['te'],sp_sch['redmud_first'].df['commercial'], 'ko',mfc='none',markeredgecolor='brown',
    linewidth=lw,markersize=ms,markeredgewidth=mew,label='Red mud experiment 1')
plt.plot(sp_sch['redmud_second'].df['te'],sp_sch['redmud_second'].df['commercial'] ,'kx',
    linewidth=lw,markersize=ms,markeredgewidth=mew,label='Red mud experiment 2')


# show grid with gray color
plt.grid(linewidth=grid_width,color = '0.5')
plt.xlabel('RAW READING FROM LOAD CELLS', fontsize=y_fontsize, labelpad=15)
plt.ylabel('READING FROM COMMERCIAL BALANCE (g)', fontsize=y_fontsize, labelpad=15)
plt.legend(bbox_to_anchor=(.02, 0.90), loc=2, borderaxespad=0.,fontsize=25)
plt.show(block=False)


fig.savefig('plot_calibrate_scales.png', format='png', dpi=300)
