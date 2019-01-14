import glob
import collections

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
         'lines.linewidth':2}
pylab.rcParams.update(params)

lw=2
ms=6
mew=2
grid_width=2
y_fontsize=11

sp=prof['grange_a_moisture_suction']['data'].df

with open('input/plot_profile.json') as f:
        plt_profile = json.load(f,object_pairs_hook=collections.OrderedDict)

for i in plt_profile['time']:
   plt_profile['time64'][i]  =pd.to_datetime(plt_profile['time'][i])
   plt_profile['time_idx'][i], min_value = min(enumerate( abs(sp.index-   plt_profile['time64'][i] )), key=operator.itemgetter(1))
   plt_profile['moisture'][i]=sp.iloc[ plt_profile['time_idx'][i] ][['mmo0','mmo1','mmo2','mmo3','mmo4','mmo5','mmo6','mmo7','mmo8','mmo9']].tolist()
   plt_profile['legend'][i]= plt_profile['time64'][i].strftime('%b/%d') + ', Day '+str((plt_profile['time64'][i]- plt_profile['time64'].values()[0] ).days)+'/ 40 Days'


fig, ax = plt.subplots(1,2,sharex=True,figsize=(9,6))

fig.subplots_adjust(hspace=.10)
fig.subplots_adjust(left=0.11, right=0.99, top=0.97, bottom=0.1)
fig.subplots_adjust(wspace=.2)

ax[0].set_xlabel('VOLUMETRIC\nMOISTURE CONTENT')
ax[1].set_xlabel('VOLUMETRIC\nMOISTURE CONTENT')
ax[0].set_ylabel('DEPTH FROM COLUMN TOP (cm)')
ax[1].set_ylabel('DEPTH FROM COLUMN TOP (cm)')
ax[0].set_title('(A)',x=0.06,y=0.94,fontweight='bold')
ax[1].set_title('(B)',x=0.06,y=0.94,fontweight='bold')

depth_y=np.array([1,5,8,13,20,28,38,48,70,85])
#depth_y_temp=np.array([1,5,8,13,20,38,48,85])
#mo_x=ta.iloc[idx_im][['mmo0','mmo1','mmo2','mmo3','mmo4','mmo5','mmo6','mmo7','mmo8','mmo9']].tolist()
#temp_x=ta.iloc[idx_im][['tmp0','tmp1','tmp2','tmp3','tmp4','tmp6','tmp7','tmp9']].tolist()

for i in plt_profile['time']:
    ax[0].plot(plt_profile['moisture'][i],depth_y,'-',color=plt_profile['color'][i],label=plt_profile['legend'][i])

ax[0].set_ylim([90,0])
ax[0].set_xlim([-0.05,1.05])

#--------------------------------------------------
#with open('input/plot_profile2.json') as f:
#        plt_profile_2 = json.load(f,object_pairs_hook=collections.OrderedDict)
#
#for i in plt_profile_2['time']:
#   plt_profile_2['time64'][i]  =pd.to_datetime(plt_profile_2['time'][i])
#   plt_profile_2['time_idx'][i], min_value = min(enumerate( abs(ta.index-   plt_profile_2['time64'][i] )), key=operator.itemgetter(1))
#   plt_profile_2['moisture'][i]=ta.iloc[ plt_profile_2['time_idx'][i] ][['mmo0','mmo1','mmo2','mmo3','mmo4','mmo5','mmo6','mmo7','mmo8','mmo9']].tolist()
#   plt_profile_2['legend'][i]= plt_profile_2['time64'][i].strftime('%b/%d') + ' Day '+str((plt_profile_2['time64'][i]- plt_profile_2['time64'].values()[0] ).days)+ '/'
#
#for i in plt_profile_2['time']:
#    ax[1].plot(plt_profile_2['moisture'][i],depth_y,'-',color=plt_profile_2['color'][i],label=plt_profile_2['legend'][i] )


ax[1].set_ylim([90,0])
#ax[1].set_xlim([4,50])
ax[1].set_xlim([-0.05,1.05])

ax[0].legend(bbox_to_anchor=(0.010, 0.01 ), loc='lower left', borderaxespad=0.,fontsize=10,handletextpad=0.23,labelspacing=0.22,ncol=1,columnspacing=0.4)
ax[1].legend(bbox_to_anchor=(0.010, 0.01 ), loc='lower left', borderaxespad=0.,fontsize=10,handletextpad=0.23,labelspacing=0.22,ncol=1,columnspacing=0.4)
for i in ax:
      for axis in ['top','bottom','left','right']:
        i.spines[axis].set_linewidth(2)

ax[0].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
ax[1].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')

fig.savefig('figure/plot_profile.png', format='png', dpi=100)
#plt.close()
