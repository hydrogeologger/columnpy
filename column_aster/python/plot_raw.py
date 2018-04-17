#data.df.plot(x='date_time',y='temp_suc1',style='o');plt.show()
#data.df.plot(x='date_time',y='temp_suc2',style='o');plt.show()
#data.df.plot(x='date_time',y='temp_suc3',style='o');plt.show()
#data.df.plot(x='date_time',y='temp_suc4',style='o');plt.show()
#data.df.plot(x='date_time',y='temp_suc5',style='o');plt.show()
#data.df.plot(x='date_time',y='temp_suc6',style='o');plt.show()
#data.df.plot(x='date_time',y='temp_suc7',style='o');plt.show()
#data.df.plot(x='date_time',y='temp_suc8',style='o');plt.show()
##data.df.plot(x='date_time',y='moisture_28',style='o');plt.show()
##data.df.plot(x='date_time',y='moisture_22',style='o');plt.show()
##data.df.plot(x='date_time',y='moisture_23',style='o');plt.show()
##data.df.plot(x='date_time',y='moisture_24',style='o');plt.show()
##data.df.plot(x='date_time',y='moisture_26',style='o');plt.show()
##data.df.plot(x='date_time',y='moisture_27',style='o');plt.show()
##data.df.plot(x='date_time',y='moisture_25',style='o');plt.show()
##data.df.plot(x='date_time',y='moisture_31',style='o');plt.show()
#data.df.plot(x='date_time',y='mom_23',style='o');plt.show()
#data.df.plot(x='date_time',y='mom_24',style='o');plt.show()
#data.df.plot(x='date_time',y='mom_25',style='o');plt.show()
#data.df.plot(x='date_time',y='mom_26',style='o');plt.show()
#data.df.plot(x='date_time',y='mom_27',style='o');plt.show()
#data.df.plot(x='date_time',y='mom_28',style='o');plt.show()
#data.df.plot(x='date_time',y='mom_29',style='o');plt.show()
#data.df.plot(x='date_time',y='mom_30',style='o');plt.show()
#data.df.plot(x='date_time',y='mom_31',style='o');plt.show()
##data.df.plot(x='date_time',y='su1',style='o');plt.show()
##data.df.plot(x='date_time',y='su2',style='o');plt.show()
##data.df.plot(x='date_time',y='su3',style='o');plt.show()
#data.df.plot(x='date_time',y='su4',style='o');plt.show()
#data.df.plot(x='date_time',y='su5',style='o');plt.show()
#data.df.plot(x='date_time',y='su6',style='o');plt.show()
#data.df.plot(x='date_time',y='su7',style='o');plt.show()
#data.df.plot(x='date_time',y='su8',style='o');plt.show()


# post processing suction values
data.df['su5'][  data.df['su5'].values>5] =np.nan
data.df['su6'][  data.df['su6'].values>5] =np.nan
data.df['su7'][  data.df['su7'].values>5] =np.nan
data.df['su8'][  data.df['su8'].values>5] =np.nan
data.df['su5'][  data.df['su5'].values<-1] =np.nan
data.df['su6'][  data.df['su6'].values<-1] =np.nan
data.df['su7'][  data.df['su7'].values<-1] =np.nan
data.df['su8'][  data.df['su8'].values<-1] =np.nan
data.df['mom_27'][  data.df['mom_27'].values<300] =np.nan
data.df['temp_suc1'][  data.df['temp_suc1'].values<10] =np.nan
data.df['temp_suc1'][  data.df['temp_suc1'].values>100] =np.nan
data.df['temp_suc7'][  data.df['temp_suc7'].values<10] =np.nan
data.df['temp_suc7'][  data.df['temp_suc7'].values>100] =np.nan

#su1 su2 su3 su4 is not good
#data.df.plot(x='date_time',y=['su5','su6','su7','su8']);plt.ylim([-0.1,5]);plt.show()

#data.df.plot(x='date_time',y=['su1','su2','su3','su4','su5','su6','su7','su8']);plt.ylim([-0.1,5]);plt.show()



#data.df.plot(x='date_time',y=['su5','su6','su7','su8']);plt.ylim([-0.1,5]);plt.show(block=False)
#data.df.plot(x='date_time',y=['mom_23','mom_24','mom_25','mom_26','mom_27','mom_28','mom_30']);plt.show(block=False)
#data.df.plot(x='date_time',y='balance_bottom');plt.show(block=False)
#data.df.plot(x='date_time',y=['temp_suc1','temp_suc2','temp_suc3','temp_suc4','temp_suc5','temp_suc6',
#    'temp_suc7','temp_suc8'],fillstyle='full',linewidth=2,markevery=10);plt.ylim([10,50]);plt.show(block=False);



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
ms=1
mew=1.5
grid_width=2
y_fontsize=12
fig, ax = plt.subplots(4,sharex=True,figsize=(6,8))
fig.subplots_adjust(hspace=.15)


for i in ax:
  for axis in ['top','bottom','left','right']:
    i.spines[axis].set_linewidth(2)



ax[0].plot(data.df['date_time'],data.df['balance_bottom'],'ko'       ,markersize=ms,markeredgewidth=mew, markeredgecolor='k',label='load cell')


ax[1].plot(data.df['date_time'], data.df['mom_23'], 'ro',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Dielectric suction A')
ax[1].plot(data.df['date_time'], data.df['mom_24'], 'go',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='Dielectric suction B')
ax[1].plot(data.df['date_time'], data.df['mom_25'], 'bo',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='b',label='Moisture A')
ax[1].plot(data.df['date_time'], data.df['mom_26'], 'co',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='Moisture A')
ax[1].plot(data.df['date_time'], data.df['mom_27'], 'mo',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='Moisture A')
ax[1].plot(data.df['date_time'], data.df['mom_28'], 'ko',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='Moisture A')
ax[1].plot(data.df['date_time'], data.df['mom_30'], 'o' ,markerfacecolor='brown' ,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='Moisture A')



ax[2].plot(data.df['date_time'], data.df['su5'], 'ro',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Dielectric suction A')
ax[2].plot(data.df['date_time'], data.df['su6'], 'go',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='Dielectric suction B')
ax[2].plot(data.df['date_time'], data.df['su7'], 'bo',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='b',label='Moisture A')
ax[2].plot(data.df['date_time'], data.df['su8'], 'co',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='Moisture A')


ax[3].plot(data.df['date_time'], data.df['temp_suc1'], 'ro',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Dielectric suction A')
ax[3].plot(data.df['date_time'], data.df['temp_suc2'], 'go',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='Dielectric suction B')
ax[3].plot(data.df['date_time'], data.df['temp_suc3'], 'bo',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='b',label='Moisture A')
ax[3].plot(data.df['date_time'], data.df['temp_suc4'], 'co',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='Moisture A')
ax[3].plot(data.df['date_time'], data.df['temp_suc5'], 'mo',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='Moisture A')
ax[3].plot(data.df['date_time'], data.df['temp_suc6'], 'ko',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='Moisture A')
ax[3].plot(data.df['date_time'], data.df['temp_suc7'], 'o' ,markerfacecolor='brown' ,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='Moisture A')


plt.xticks(rotation=45)
plt.show(block=False)



fig.savefig('figure/plot_raw_result.png', format='png', dpi=600)

