# this script is used for showing the relation between 'degree of saturation' and 'suction'
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
         'font.sans-serif':'Arial',
         'axes.labelweight':'bold',
         'lines.linewidth':2}#,


pylab.rcParams.update(params)

lw=2
ms=6
mew=2
grid_width=2
y_fontsize=11
fig, ax = plt.subplots(1,sharex=True,figsize=(9,9))
fig.subplots_adjust(hspace=.10)
fig.subplots_adjust(left=0.15, right=0.79, top=0.97, bottom=0.05)


#for i in ax:
#  for axis in ['top','bottom','left','right']:
#    i.spines[axis].set_linewidth(2)

 
