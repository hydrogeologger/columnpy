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
   plt_profile_2['time_idx_c1_e'][i], min_value = min(enumerate( abs(prof['grange_a_electrochem_o2']['data'].df.index- plt_profile_2['time64'][i] )), key=operator.itemgetter(1))
   plt_profile_2['time_idx_c1_lo'][i], min_value = min(enumerate( abs(prof['grange_a_luo2']['data'].df.index- plt_profile_2['time64'][i] )), key=operator.itemgetter(1))
   plt_profile_2['time_idx_c2_e'][i], min_value = min(enumerate( abs(prof['grange_b_electrochem_o2']['data'].df.index- plt_profile_2['time64'][i] )), key=operator.itemgetter(1))
   plt_profile_2['time_idx_c2_lo'][i], min_value = min(enumerate( abs(prof['grange_b_luo2']['data'].df.index- plt_profile_2['time64'][i] )), key=operator.itemgetter(1))
   plt_profile_2['time_idx_c3_e'][i], min_value = min(enumerate( abs(prof['grange_d_electrochem_o2']['data'].df.index- plt_profile_2['time64'][i] )), key=operator.itemgetter(1))
   plt_profile_2['time_idx_c3_lo'][i], min_value = min(enumerate( abs(prof['grange_d_luo2']['data'].df.index- plt_profile_2['time64'][i] )), key=operator.itemgetter(1))
   #plt_profile_2['time_idx'][i], idx_c1_mo=prof['grange_a_moisture_suction']['data'].df.index.get_loc(plt_profile_2['time64'][i], method='nearest')
   plt_profile_2['oxygen_dry_c1_e'][i]=prof['grange_a_electrochem_o2']['data'].df.iloc[ plt_profile_2['time_idx_c1_e'][i] ][['dox6_c','dox3_c','dox2_c','dox1_c','dox0_c']].tolist()
   #plt_profile_2['oxygen_dry_c1_lo'][i]=prof['grange_a_luo2']['data'].df.iloc[ plt_profile_2['time_idx_c1_lo'][i] ][['wluo6','wluo5']].tolist()
   plt_profile_2['oxygen_dry_c2_e'][i]=prof['grange_b_electrochem_o2']['data'].df.iloc[ plt_profile_2['time_idx_c2_e'][i] ][['dox7_c','dox6_c','dox5_c','dox3_c','dox1_c','dox0_c']].tolist()
   plt_profile_2['oxygen_dry_c2_lo'][i]=prof['grange_b_luo2']['data'].df.iloc[ plt_profile_2['time_idx_c2_lo'][i] ][['dluo4','dluo2']].tolist()
   plt_profile_2['oxygen_dry_c3_e'][i]=prof['grange_d_electrochem_o2']['data'].df.iloc[ plt_profile_2['time_idx_c3_e'][i] ][['dox6_c','dox4_c','dox2_c','dox1_c','dox0_c']].tolist()
   plt_profile_2['oxygen_dry_c3_lo'][i]=prof['grange_d_luo2']['data'].df.iloc[ plt_profile_2['time_idx_c3_lo'][i] ][['dluo7','dluo5']].tolist()
   #plt_profile_2['oxygen_dry_c1'][i]= np.array(plt_profile_2['oxygen_dry_c1_e'][i]).astype(np.double)
   #plt_profile_2['oxygen_dry_c2'][i]= np.array(plt_profile_2['oxygen_dry_c2_e'][i][:3]+[plt_profile_2['oxygen_dry_c2_lo'][i][0]]+[plt_profile_2['oxygen_dry_c2_e'][i][3]]+[plt_profile_2['oxygen_dry_c2_lo'][i][1]]+plt_profile_2['oxygen_dry_c2_e'][i][4:]).astype(np.double)
   #plt_profile_2['oxygen_dry_c3'][i]= np.array([plt_profile_2['oxygen_dry_c3_lo'][i][0]]+[plt_profile_2['oxygen_dry_c3_e'][i][0]]+[plt_profile_2['oxygen_dry_c3_lo'][i][1]]+plt_profile_2['oxygen_dry_c3_e'][i][1:]).astype(np.double)
   plt_profile_2['oxygen_dry_c1'][i]= plt_profile_2['oxygen_dry_c1_e'][i]
   plt_profile_2['oxygen_dry_c2'][i]= plt_profile_2['oxygen_dry_c2_e'][i][:3]+[plt_profile_2['oxygen_dry_c2_lo'][i][0]]+[plt_profile_2['oxygen_dry_c2_e'][i][3]]+[plt_profile_2['oxygen_dry_c2_lo'][i][1]]+plt_profile_2['oxygen_dry_c2_e'][i][4:]
   plt_profile_2['oxygen_dry_c3'][i]= [plt_profile_2['oxygen_dry_c3_lo'][i][0]]+[plt_profile_2['oxygen_dry_c3_e'][i][0]]+[plt_profile_2['oxygen_dry_c3_lo'][i][1]]+plt_profile_2['oxygen_dry_c3_e'][i][1:]
   #mask_a = np.isfinite(plt_profile_2['oxygen_dry_c1'][i])
   #mask_b = np.isfinite(plt_profile_2['oxygen_dry_c2'][i])
   #mask_d = np.isfinite(plt_profile_2['oxygen_dry_c3'][i])
   plt_profile_2['legend'][i]= plt_profile_2['time64'][i].strftime('%y-%m-%d') + ' Day '+str((plt_profile_2['time64'][i]- plt_profile_2['time64'].values()[0] ).days)
    


fig, ax = plt.subplots(1,3,sharex=True,figsize=(10,8))

#for i in ax:
 


#    for axis in ['top','bottom','left','right']:
      #plt.xticks(rotation=45)
fig.subplots_adjust(hspace=.10)
fig.subplots_adjust(left=0.10, right=0.90, top=0.85, bottom=0.1)
fig.subplots_adjust(wspace=.03)

ax[0].set_xlabel('OXYGEN\nCONCENTRATION (%)')
ax[1].set_xlabel('OXYGEN\nCONCENTRATION (%)')
ax[2].set_xlabel('OXYGEN\nCONCENTRATION (%)')
ax[0].set_ylabel('DEPTH FROM COLUMN TOP (m)')
#ax[1].set_ylabel('DEPTH FROM COLUMN TOP (m)')
ax[2].yaxis.tick_right()
ax[2].set_ylabel('DEPTH FROM COLUMN TOP (m)')
ax[2].yaxis.set_label_position("right")
ax[0].set_title('(A) Column1,type A',x=0.35,y=0.94,fontweight='bold')
ax[1].set_title('(B) Column2,type B',x=0.35,y=0.94,fontweight='bold')
ax[2].set_title('(C) Column3,type D',x=0.35,y=0.94,fontweight='bold')


depth_y_a=np.array([1.0,2.5,3.0,3.5,4.0])
depth_y_b=np.array([0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0])
depth_y_d=np.array([0.5,1.0,1.5,2.0,3.0,3.5,4.0])

#plt_profile_2['oxygen_dry_c1'][i]=np.arange(0, len(depth_y_a))
#plt_profile_2['oxygen_dry_c2'][i]=np.arange(0, len(depth_y_b))
#plt_profile_2['oxygen_dry_c3'][i]=np.arange(0, len(depth_y_b))
#mask_a = np.isfinite(plt_profile_2['oxygen_dry_c1'][i])
#mask_b = np.isfinite(plt_profile_2['oxygen_dry_c2'][i])
#mask_d = np.isfinite(plt_profile_2['oxygen_dry_c3'][i])
#
#line, = ax[0].plot(plt_profile_2['oxygen_dry_c1'][i][mask_a],depth_y_a[mask_a], ls="-",lw=1)
#line, = ax[1].plot(plt_profile_2['oxygen_dry_c2'][i][mask_b],depth_y_b[mask_b], ls="-",lw=1)
#line, = ax[2].plot(plt_profile_2['oxygen_dry_c3'][i][mask_d],depth_y_b[mask_d], ls="-",lw=1)

#plt.xticks(rotation=45)

for i in plt_profile_2['time']:
    #ax[0].plot(plt_profile_2['oxygen_dry_c1'][i],depth_y_a,'-',color=plt_profile_2['color'][i],label=plt_profile_2['legend'][i] )
    #ax[1].plot(plt_profile_2['oxygen_dry_c2'][i],depth_y_b,'-',color=plt_profile_2['color'][i],label=plt_profile_2['legend'][i] )
    #ax[2].plot(plt_profile_2['oxygen_dry_c3'][i],depth_y_b,'-',color=plt_profile_2['color'][i],label=plt_profile_2['legend'][i] )
    ax[0].plot(plt_profile_2['oxygen_dry_c1'][i],depth_y_a,'-',color=plt_profile_2['color'][i],label=plt_profile_2['legend'][i] )
    ax[1].plot(plt_profile_2['oxygen_dry_c2'][i],depth_y_b,'-',color=plt_profile_2['color'][i],label=plt_profile_2['legend'][i] )
    ax[2].plot(plt_profile_2['oxygen_dry_c3'][i],depth_y_d,'-',color=plt_profile_2['color'][i],label=plt_profile_2['legend'][i] )
    
ax[0].set_ylim([4.1,0.2])
ax[1].set_ylim([4.1,0.2])
ax[2].set_ylim([4.1,0.2])
ax[0].set_xlim([0,23])
ax[1].set_xlim([0,23])
ax[2].set_xlim([0,23])
ax[0].xaxis.set_major_locator(plt.MaxNLocator(5))
ax[1].xaxis.set_major_locator(plt.MaxNLocator(5))
ax[2].xaxis.set_major_locator(plt.MaxNLocator(5))
ax[1].yaxis.set_major_formatter(plt.NullFormatter())

ax[1].legend(bbox_to_anchor=(0.5, 1.07 ), loc='center', borderaxespad=0.,fontsize=10,handletextpad=0.03,labelspacing=0.02,ncol=2,columnspacing=0.4)
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
fig.savefig('figure/plot_oxdry_profile_c123.png', format='png', dpi=100)
#plt.close()
