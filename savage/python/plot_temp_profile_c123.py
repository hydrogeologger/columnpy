import glob
import json
import collections
import operator
from operator import itemgetter
import matplotlib.pyplot as plt
import numpy as np


lw=1.5
ms=1
mew=3
grid_width=2
y_fontsize=12

params = {'legend.fontsize': 4,
          'figure.figsize': (10, 8),
         'axes.labelsize': 11,
         'axes.titlesize':'11',
         'xtick.labelsize':'10',
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


#depth_y_temp=np.array([1,5,8,13,20,38,48,85])
#mo_x=ta.iloc[idx_im][['mmo0','mmo1','mmo2','mmo3','mmo4','mmo5','mmo6','mmo7','mmo8','mmo9']].tolist()
#temp_x=ta.iloc[idx_im][['tmp0','tmp1','tmp2','tmp3','tmp4','tmp6','tmp7','tmp9']].tolist()


#--------------------------------------------------
with open('input/plot_profile2.json') as f:
        plt_profile_2 = json.load(f,object_pairs_hook=collections.OrderedDict)

for i in plt_profile_2['time']:
   plt_profile_2['time64'][i]  =pd.to_datetime(plt_profile_2['time'][i])
   plt_profile_2['time_idx_c1'][i], min_value = min(enumerate( abs(prof['grange_a_moisture_suction']['data'].df.index- plt_profile_2['time64'][i] )), key=operator.itemgetter(1))
   plt_profile_2['time_idx_c2'][i], min_value = min(enumerate( abs(prof['grange_b_moisture_suction']['data'].df.index- plt_profile_2['time64'][i] )), key=operator.itemgetter(1))
   plt_profile_2['time_idx_c3'][i], min_value = min(enumerate( abs(prof['grange_d_type_moisture_suction']['data'].df.index- plt_profile_2['time64'][i] )), key=operator.itemgetter(1))
   #plt_profile_2['time_idx'][i], idx_c1_mo=prof['grange_a_moisture_suction']['data'].df.index.get_loc(plt_profile_2['time64'][i], method='nearest')
   plt_profile_2['moisture_c1'][i]=prof['grange_a_moisture_suction']['data'].df.iloc[ plt_profile_2['time_idx_c1'][i] ][['mo7_c','mo6_c','mo5_c','mo4_c','mo3_c','mo2_c','mo1_c','mo0_c']].tolist()
   plt_profile_2['moisture_c2'][i]=prof['grange_b_moisture_suction']['data'].df.iloc[ plt_profile_2['time_idx_c2'][i] ][['mo7_c','mo6_c','mo5_c','mo4_c','mo3_c','mo2_c','mo1_c','mo0_c']].tolist()
   plt_profile_2['moisture_c3'][i]=prof['grange_d_type_moisture_suction']['data'].df.iloc[ plt_profile_2['time_idx_c3'][i] ][['mo7_c','mo6_c','mo5_c','mo4_c','mo3_c','mo2_c','mo1_c','mo0_c']].tolist()
   plt_profile_2['legend'][i]= plt_profile_2['time64'][i].strftime('%y-%m-%d') + ' Day '+str((plt_profile_2['time64'][i]- plt_profile_2['time64'].values()[0] ).days)


fig, ax = plt.subplots(1,3,sharex=True,figsize=(10,8))

#for i in ax:
#    for axis in ['top','bottom','left','right']:
      #plt.xticks(rotation=45)
fig.subplots_adjust(hspace=.10)
fig.subplots_adjust(left=0.10, right=0.90, top=0.85, bottom=0.1)
fig.subplots_adjust(wspace=.25)

ax[0].set_xlabel('VOLUMETRIC\nWATER CONTENT (-)')
ax[1].set_xlabel('VOLUMETRIC\nWATER CONTENT (-)')
ax[2].set_xlabel('VOLUMETRIC\nWATER CONTENT (-)')
ax[0].set_ylabel('DEPTH FROM COLUMN TOP (m)')
#ax[1].set_ylabel('DEPTH FROM COLUMN TOP (m)')
ax[2].yaxis.tick_right()
ax[2].set_ylabel('DEPTH FROM COLUMN TOP (m)')
ax[2].yaxis.set_label_position("right")
ax[0].set_title('Column1 (Type A)',x=0.35,y=0.94,fontweight='bold')
ax[1].set_title('Column2 (Type B)',x=0.35,y=0.94,fontweight='bold')
ax[2].set_title('Column3 (Type D)',x=0.35,y=0.94,fontweight='bold')

depth_y=np.array([0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0])

#plt.xticks(rotation=45)

for i in plt_profile_2['time']:
    ax[0].plot(plt_profile_2['moisture_c1'][i],depth_y,'-',color=plt_profile_2['color'][i],label=plt_profile_2['legend'][i] )
    ax[1].plot(plt_profile_2['moisture_c2'][i],depth_y,'-',color=plt_profile_2['color'][i],label=plt_profile_2['legend'][i] )
    ax[2].plot(plt_profile_2['moisture_c3'][i],depth_y,'-',color=plt_profile_2['color'][i],label=plt_profile_2['legend'][i] )
        
ax[0].set_ylim([4.1,0.2])
ax[1].set_ylim([4.1,0.2])
ax[2].set_ylim([4.1,0.2])
ax[0].set_xlim([-0.03,0.36])
ax[1].set_xlim([-0.03,0.36])
ax[2].set_xlim([-0.03,0.36])
ax[0].xaxis.set_major_locator(plt.MaxNLocator(5))
ax[1].xaxis.set_major_locator(plt.MaxNLocator(5))
ax[2].xaxis.set_major_locator(plt.MaxNLocator(5))


ax[1].legend(bbox_to_anchor=(0.5, 1.07 ), loc='center', borderaxespad=0.,fontsize=10,handletextpad=0.03,labelspacing=0.02,ncol=3,columnspacing=0.4)
#ax[1].legend(bbox_to_anchor=(0.99, 0.004 ), loc='lower right', borderaxespad=0.,fontsize=10,handletextpad=0.23,labelspacing=0.22,ncol=1,columnspacing=0.4)
#ax[2].legend(bbox_to_anchor=(0.99, 0.004 ), loc='lower right', borderaxespad=0.,fontsize=10,handletextpad=0.23,labelspacing=0.22,ncol=1,columnspacing=0.4)

for i in ax:
      for axis in ['top','bottom','left','right']:
        i.spines[axis].set_linewidth(2)
        i.set_axisbelow(True)

ax[0].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
ax[1].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
ax[2].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')

plt.show(block=False)
fig.savefig('figure/plot_profile_c123.png', format='png', dpi=100)
#plt.close()
