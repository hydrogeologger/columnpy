import matplotlib
import matplotlib.image as image
from matplotlib.ticker import MultipleLocator
import numpy as np
# Force matplotlib to not use any Xwindows backend.
#matplotlib.use('Agg')
import matplotlib.pyplot as plt

import glob, os
#os.chdir("/home/chenming/Projects/tailings/area_51_redmud_4cm_photo/")
#img_list=glob.glob('/home/chenming/Projects/tailings/area_51_redmud_4cm_photo/*.jpg')
#for file in glob.glob("*.jpg"):
#    print(file)
sch_name='moisture_final'


import matplotlib.pylab as pylab
lw=2
ms=0.5
mew=3
grid_width=2

params = {'legend.fontsize': 6,
          'figure.figsize': (10, 6),
         'axes.labelsize': 11,
         'axes.titlesize':'11',
         'xtick.labelsize':'11',
         'ytick.labelsize':'11',
         'font.weight':'bold',
         'axes.labelweight':'bold',
         'lines.linewidth':2}#,
#         'title.fontweight':'bold'}

#         'axes.grid':'linewidth=grid_width,color = '0.5''}
#         'linewidth':lw,'markers.size':ms,'markers.edgewidth':mew}
pylab.rcParams.update(params)

#lw=2
#ms=6
#mew=2
#grid_width=2
y_fontsize=10
x_fontsize=12



fig, ax = plt.subplots(6,sharex=True,figsize=(8.5,9))
fig.subplots_adjust(hspace=.15)
fig.subplots_adjust(left=0.16, right=0.95, top=0.93, bottom=0.08)
#ax2=ax[1].twinx()
    
for i in ax:
  for axis in ['top','bottom','left','right']:
    i.spines[axis].set_linewidth(2)
    i.set_axisbelow(True)

#sp=solar['solar']['df']
#ax[0].bar(sp.index, sp['Daily global solar exposure (KWh/m*m)'],color='maroon',edgecolor='maroon')
#
#sp=rain['rain']['df']
#
#ax[1].bar(sp.index, sp['Rainfall amount (millimetres)'],color='royalblue',edgecolor='royalblue')
#ax2.plot(sp.index, sp['rain_cumsum'],color='darkblue')

sp=prof['grange_a_moisture_suction']['data'].df#[::24]

mark_every=128
iv=30
ax[0].plot(sp.index[::iv], sp.mo7_c[::iv],'-',color='darkblue',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='0.5m',markevery=mark_every,ms=12)
ax[0].plot(sp.index[::iv], sp.mo6_c[::iv],'-',color='royalblue',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='1.0m',markevery=mark_every,ms=12)
ax[0].plot(sp.index[::iv], sp.mo5_c[::iv],'-',color='lightblue',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='b',label='1.5m',markevery=mark_every,ms=12)
ax[0].plot(sp.index[::iv], sp.mo4_c[::iv],'-',color='limegreen',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='2.0m',markevery=mark_every,ms=12)
ax[0].plot(sp.index[::iv], sp.mo3_c[::iv],'-',color='olive',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='2.5m',markevery=mark_every,ms=12)
ax[0].plot(sp.index[::iv], sp.mo2_c[::iv],'-',color='gold',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='3.0m',markevery=mark_every,ms=12)
ax[0].plot(sp.index[::iv], sp.mo1_c[::iv],'-',color='peru',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='3.5m',ms=12,markevery=mark_every)
ax[0].plot(sp.index[::iv], sp.mo0_c[::iv],'-',color='maroon',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='4.0m',markevery=mark_every)


sp=prof['grange_b_moisture_suction']['data'].df#[::24]
mark_every=24
iv=30
ax[1].plot(sp.index[::iv], sp.mo7_c[::iv],'-',color='darkblue',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='0.5m',markevery=mark_every,ms=12)
ax[1].plot(sp.index[::iv], sp.mo6_c[::iv],'-',color='royalblue',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='1.0m',markevery=mark_every,ms=12)
ax[1].plot(sp.index[::iv], sp.mo5_c[::iv],'-',color='lightblue',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='b',label='1.5m',markevery=mark_every,ms=12)
ax[1].plot(sp.index[::iv], sp.mo4_c[::iv],'-',color='limegreen',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='2.0m',markevery=mark_every,ms=12)
ax[1].plot(sp.index[::iv], sp.mo3_c[::iv],'-',color='olive',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='2.5m',markevery=mark_every,ms=12)
ax[1].plot(sp.index[::iv], sp.mo2_c[::iv],'-',color='gold',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='3.0m',markevery=mark_every,ms=12)
ax[1].plot(sp.index[::iv], sp.mo1_c[::iv],'-',color='peru',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='3.5m',ms=12,markevery=mark_every)
ax[1].plot(sp.index[::iv], sp.mo0_c[::iv],'-',color='maroon',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='4.0m',markevery=mark_every)


sp=prof['grange_d_type_moisture_suction']['data'].df#[::24]
mark_every=48
iv=30

ax[2].plot(sp.index[::iv], sp.mo7_c[::iv],'-',color='darkblue',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='0.5m',markevery=mark_every,ms=12)
ax[2].plot(sp.index[::iv], sp.mo6_c[::iv],'-',color='royalblue',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='1.0m',markevery=mark_every,ms=12)
ax[2].plot(sp.index[::iv], sp.mo5_c[::iv],'-',color='lightblue',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='b',label='1.5m',markevery=mark_every,ms=12)
ax[2].plot(sp.index[::iv], sp.mo4_c[::iv],'-',color='limegreen',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='2.0m',markevery=mark_every,ms=12)
ax[2].plot(sp.index[::iv], sp.mo3_c[::iv],'-',color='olive',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='2.5m',markevery=mark_every,ms=12)
ax[2].plot(sp.index[::iv], sp.mo2_c[::iv],'-',color='gold',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='3.0m',markevery=mark_every,ms=12)
ax[2].plot(sp.index[::iv], sp.mo1_c[::iv],'-',color='peru',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='3.5m',ms=12,markevery=mark_every)
ax[2].plot(sp.index[::iv], sp.mo0_c[::iv],'-',color='maroon',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='4.0m',markevery=mark_every)




#sp_wlo=prof['grange_3_luo2_wet']['data'].df
#sp_dlo=prof['grange_3_luo2_dry']['data'].df
#sp_moi=prof['grange_3_mo_su']['data'].df
#mark_every=48
#ax[3].plot(sp_moi.index, sp_moi.wluo7,'-',color='darkblue',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='0.5m',markevery=mark_every,ms=12)
#ax[3].plot(sp_wlo.index, sp_wlo.wluo6,'-',color='royalblue',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='1.0m',markevery=mark_every,ms=12)
#ax[3].plot(sp_wlo.index, sp_wlo.wluo5,'-',color='lightblue',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='b',label='1.5m',markevery=mark_every,ms=12)
#ax[3].plot(sp_wlo.index, sp_wlo.wluo4,'-',color='limegreen',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='2.0m',markevery=mark_every,ms=12)
#ax[3].plot(sp_wlo.index, sp_wlo.wluo3,'-',color='olive',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='2.5m',markevery=mark_every,ms=12)
#ax[3].plot(sp_wlo.index, sp_wlo.wluo2,'-',color='gold',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='3.0m',markevery=mark_every,ms=12)
#ax[3].plot(sp_wlo.index, sp_wlo.wluo1,'-',color='peru',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='3.5m',ms=12,markevery=mark_every)
#ax[3].plot(sp_wlo.index, sp_wlo.wluo0,'-',color='maroon',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='4.0m',markevery=mark_every)
#
#
#sp_wlo=prof['grange_4_luo2_wet']['data'].df
#sp_dlo=prof['grange_4_luo2_dry']['data'].df
#sp_moi=prof['grange_4_mo_su']['data'].df
#mark_every=48
#ax[4].plot(sp_moi.index, sp_moi.wluo7,'-',color='darkblue',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='0.5m',markevery=mark_every,ms=12)
#ax[4].plot(sp_wlo.index, sp_wlo.wluo6,'-',color='royalblue',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='1.0m',markevery=mark_every,ms=12)
#ax[4].plot(sp_wlo.index, sp_wlo.wluo5,'-',color='lightblue',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='b',label='1.5m',markevery=mark_every,ms=12)
#ax[4].plot(sp_wlo.index, sp_wlo.wluo4,'-',color='limegreen',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='2.0m',markevery=mark_every,ms=12)
#ax[4].plot(sp_wlo.index, sp_wlo.wluo3,'-',color='olive',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='2.5m',markevery=mark_every,ms=12)
#ax[4].plot(sp_wlo.index, sp_wlo.wluo2,'-',color='gold',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='3.0m',markevery=mark_every,ms=12)
#ax[4].plot(sp_wlo.index, sp_wlo.wluo1,'-',color='peru',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='3.5m',ms=12,markevery=mark_every)
#ax[4].plot(sp_wlo.index, sp_wlo.wluo0,'-',color='maroon',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='4.0m',markevery=mark_every)
#
#
#sp_wlo=prof['grange_5_luo2_wet']['data'].df
#sp_dlo=prof['grange_5_luo2_dry']['data'].df
#sp_moi=prof['grange_5_mo_su']['data'].df
#mark_every=48
#ax[5].plot(sp_moi.index, sp_moi.wluo7,'-',color='darkblue',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='0.5m',markevery=mark_every,ms=12)
#ax[5].plot(sp_wlo.index, sp_wlo.wluo6,'-',color='royalblue',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='1.0m',markevery=mark_every,ms=12)
#ax[5].plot(sp_wlo.index, sp_wlo.wluo5,'-',color='lightblue',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='b',label='1.5m',markevery=mark_every,ms=12)
#ax[5].plot(sp_wlo.index, sp_wlo.wluo4,'-',color='limegreen',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='2.0m',markevery=mark_every,ms=12)
#ax[5].plot(sp_wlo.index, sp_wlo.wluo3,'-',color='olive',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='2.5m',markevery=mark_every,ms=12)
#ax[5].plot(sp_wlo.index, sp_wlo.wluo2,'-',color='gold',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='3.0m',markevery=mark_every,ms=12)
#ax[5].plot(sp_wlo.index, sp_wlo.wluo1,'-',color='peru',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='3.5m',ms=12,markevery=mark_every)
#ax[5].plot(sp_wlo.index, sp_wlo.wluo0,'-',color='maroon',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='4.0m',markevery=mark_every)


sp=prof['grange_5_mo_su']['data'].df
mark_every=24
iv=30
#ax[3].plot(sp_moi.index, sp_moi.tmp7,'-',color='darkblue',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='0.5m',markevery=mark_every,ms=12)
#ax[3].plot(sp_dlo.index, sp_dlo.dlut6,'-',color='royalblue',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='1.0m',markevery=mark_every,ms=12)
#ax[3].plot(sp_dlo.index, sp_dlo.dlut5,'-',color='lightblue',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='b',label='1.5m',markevery=mark_every,ms=12)
#ax[3].plot(sp_dlo.index, sp_dlo.dlut4,'-',color='limegreen',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='2.0m',markevery=mark_every,ms=12)
#ax[3].plot(sp_dlo.index, sp_dlo.dlut3,'-',color='olive',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='2.5m',markevery=mark_every,ms=12)
#ax[3].plot(sp_dlo.index, sp_dlo.dlut2,'-',color='gold',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='3.0m',markevery=mark_every,ms=12)
#ax[3].plot(sp_dlo.index, sp_dlo.dlut1,'-',color='peru',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='3.5m',ms=12,markevery=mark_every)
#ax[3].plot(sp_dlo.index, sp_dlo.dlut0,'-',color='maroon',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='4.0m',markevery=mark_every)
ax[3].plot(sp.index[::iv], sp.mo7_c[::iv],'-',color='darkblue',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='0.5m',markevery=mark_every,ms=12)
ax[3].plot(sp.index[::iv], sp.mo6_c[::iv],'-',color='royalblue',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='1.0m',markevery=mark_every,ms=12)
ax[3].plot(sp.index[::iv], sp.mo5_c[::iv],'-',color='lightblue',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='b',label='1.5m',markevery=mark_every,ms=12)
ax[3].plot(sp.index[::iv], sp.mo4_c[::iv],'-',color='limegreen',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='2.0m',markevery=mark_every,ms=12)
ax[3].plot(sp.index[::iv], sp.mo3_c[::iv],'-',color='olive',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='2.5m',markevery=mark_every,ms=12)
ax[3].plot(sp.index[::iv], sp.mo2_c[::iv],'-',color='gold',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='3.0m',markevery=mark_every,ms=12)
ax[3].plot(sp.index[::iv], sp.mo1_c[::iv],'-',color='peru',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='3.5m',ms=12,markevery=mark_every)
ax[3].plot(sp.index[::iv], sp.mo0_c[::iv],'-',color='maroon',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='4.0m',markevery=mark_every)



sp=prof['grange_3_mo_su']['data'].df
mark_every=24
iv=30
#ax[4].plot(sp_moi.index, sp_moi.tmp7,'-',color='darkblue',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='0.5m',markevery=mark_every,ms=12)
#ax[4].plot(sp_dlo.index, sp_dlo.dlut6,'-',color='royalblue',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='1.0m',markevery=mark_every,ms=12)
#ax[4].plot(sp_dlo.index, sp_dlo.dlut5,'-',color='lightblue',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='b',label='1.5m',markevery=mark_every,ms=12)
#ax[4].plot(sp_dlo.index, sp_dlo.dlut4,'-',color='limegreen',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='2.0m',markevery=mark_every,ms=12)
#ax[4].plot(sp_dlo.index, sp_dlo.dlut3,'-',color='olive',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='2.5m',markevery=mark_every,ms=12)
#ax[4].plot(sp_dlo.index, sp_dlo.dlut2,'-',color='gold',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='3.0m',markevery=mark_every,ms=12)
#ax[4].plot(sp_dlo.index, sp_dlo.dlut1,'-',color='peru',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='3.5m',ms=12,markevery=mark_every)
#ax[4].plot(sp_dlo.index, sp_dlo.dlut0,'-',color='maroon',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='4.0m',markevery=mark_every)
ax[4].plot(sp.index[::iv], sp.mo7_c[::iv],'-',color='darkblue',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='0.5m',markevery=mark_every,ms=12)
ax[4].plot(sp.index[::iv], sp.mo6_c[::iv],'-',color='royalblue',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='1.0m',markevery=mark_every,ms=12)
ax[4].plot(sp.index[::iv], sp.mo5_c[::iv],'-',color='lightblue',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='b',label='1.5m',markevery=mark_every,ms=12)
ax[4].plot(sp.index[::iv], sp.mo4_c[::iv],'-',color='limegreen',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='2.0m',markevery=mark_every,ms=12)
ax[4].plot(sp.index[::iv], sp.mo3_c[::iv],'-',color='olive',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='2.5m',markevery=mark_every,ms=12)
ax[4].plot(sp.index[::iv], sp.mo2_c[::iv],'-',color='gold',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='3.0m',markevery=mark_every,ms=12)
ax[4].plot(sp.index[::iv], sp.mo1_c[::iv],'-',color='peru',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='3.5m',ms=12,markevery=mark_every)
ax[4].plot(sp.index[::iv], sp.mo0_c[::iv],'-',color='maroon',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='4.0m',markevery=mark_every)


sp=prof['grange_4_mo_su']['data'].df
mark_every=24
iv=30
#ax[5].plot(sp_moi.index, sp_moi.tmp7,'-',color='darkblue',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='0.5m',markevery=mark_every,ms=12)
#ax[5].plot(sp_dlo.index, sp_dlo.dlut6,'-',color='royalblue',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='1.0m',markevery=mark_every,ms=12)
#ax[5].plot(sp_dlo.index, sp_dlo.dlut5,'-',color='lightblue',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='b',label='1.5m',markevery=mark_every,ms=12)
#ax[5].plot(sp_dlo.index, sp_dlo.dlut4,'-',color='limegreen',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='2.0m',markevery=mark_every,ms=12)
#ax[5].plot(sp_dlo.index, sp_dlo.dlut3,'-',color='olive',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='2.5m',markevery=mark_every,ms=12)
#ax[5].plot(sp_dlo.index, sp_dlo.dlut2,'-',color='gold',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='3.0m',markevery=mark_every,ms=12)
#ax[5].plot(sp_dlo.index, sp_dlo.dlut1,'-',color='peru',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='3.5m',ms=12,markevery=mark_every)
#ax[5].plot(sp_dlo.index, sp_dlo.dlut0,'-',color='maroon',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='4.0m',markevery=mark_every)
ax[5].plot(sp.index[::iv], sp.mo7_c[::iv],'-',color='darkblue',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='0.5m',markevery=mark_every,ms=12)
ax[5].plot(sp.index[::iv], sp.mo6_c[::iv],'-',color='royalblue',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='1.0m',markevery=mark_every,ms=12)
ax[5].plot(sp.index[::iv], sp.mo5_c[::iv],'-',color='lightblue',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='b',label='1.5m',markevery=mark_every,ms=12)
ax[5].plot(sp.index[::iv], sp.mo4_c[::iv],'-',color='limegreen',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='2.0m',markevery=mark_every,ms=12)
#ax[5].plot(sp.index[::iv], sp.mo3_c[::iv],'-',color='olive',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='2.5m',markevery=mark_every,ms=12)
ax[5].plot(sp.index[::iv], sp.mo2_c[::iv],'-',color='gold',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='3.0m',markevery=mark_every,ms=12)
ax[5].plot(sp.index[::iv], sp.mo1_c[::iv],'-',color='peru',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='3.5m',ms=12,markevery=mark_every)
ax[5].plot(sp.index[::iv], sp.mo0_c[::iv],'-',color='maroon',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='4.0m',markevery=mark_every)




#
#ax[3].set_axisbelow(True)
ax[0].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
ax[1].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
ax[2].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
ax[3].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
ax[4].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
ax[5].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
#ax[6].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
#ax[7].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
#
#ax[0].set_ylabel('CUMULATIVE\nEVAPORATION\n(mm)', fontsize=y_fontsize, labelpad=20)
#ax[0].set_ylabel('GLOBAL\nSOLAR EXPOSURE\n(KWh/m*m)', fontsize=y_fontsize, labelpad=10)
#ax[1].set_ylabel('RAINFALL\n(mm)', fontsize=y_fontsize, labelpad=10)
#ax2.set_ylabel('CUMULATIVE RAINFALL\n(mm)', fontsize=y_fontsize, labelpad=10)
ax[0].set_ylabel('VOL.MOIST.\nCONTENT\nCOLUMN 1\n A', fontsize=y_fontsize, labelpad=10)
ax[1].set_ylabel('VOL.MOIST.\nCONTENT\nCOLUMN 2\n B', fontsize=y_fontsize, labelpad=10)
ax[2].set_ylabel('VOL.MOIST.\nCONTENT\nCOLUMN 3\n D', fontsize=y_fontsize, labelpad=10)
ax[3].set_ylabel('VOL.MOIST.\nCONTENT\nCOLUMN 4\n D + A', fontsize=y_fontsize, labelpad=10)
ax[4].set_ylabel('VOL.MOIST.\nCONTENT\nCOLUMN 5\n D + B', fontsize=y_fontsize, labelpad=10)
ax[5].set_ylabel('VOL.MOIST.\nCONTENT\nCOLUMN 6\n A + B + D', fontsize=y_fontsize, labelpad=10)

##ax[2].set_ylabel('DEGREE OF SAT.\nBY DIELECTRIC\nMOISTURE\nSENSOR', fontsize=y_fontsize, labelpad=10)
#ax[2].set_ylabel('SUCTION (kPa)', fontsize=y_fontsize, labelpad=10)
#ax[3].set_ylabel('TEMPERATURE\n($^\circ$c)', fontsize=y_fontsize, labelpad=10)
##ax[5].set_ylabel('TEMPERATURE\n($^\circ$c)', fontsize=y_fontsize, labelpad=20)
##ax[6].set_ylabel('NORMALIZED\nRISE OF\nTEMPERATURE', fontsize=y_fontsize, labelpad=10)
##ax[7].set_ylabel('SUCTION BY\nTEMPERATURE\nHUMIDITY\n SENSOR (m)', fontsize=y_fontsize, labelpad=10)

ax[5].set_xlabel('DATE', fontsize=x_fontsize,labelpad=3)
ax[0].set_ylim([-0.03,0.36])
ax[1].set_ylim([-0.03,0.36])
ax[2].set_ylim([-0.03,0.36])
ax[3].set_ylim([-0.03,0.36])
ax[4].set_ylim([-0.03,0.36])
ax[5].set_ylim([-0.03,0.36])
#ax[6].set_ylim([0,1])
#ax[7].set_ylim([0,1])
#ax[7].legend(bbox_to_anchor=(.1, 0.55 ), loc=2, borderaxespad=0.)

#ax[0].set_axisbelow(True)
#ax[1].set_axisbelow(True)
#ax2.set_axisbelow(True)
#ax[2].set_axisbelow(True)
#ax[3].set_axisbelow(True)
#ax[4].set_axisbelow(True)
#ax[5].set_axisbelow(True)
#ax[6].set_axisbelow(True)
#ax[7].set_axisbelow(True)
#ax[0].set_title('(A)',x=0.02,y=0.7,fontweight='bold')
#ax[1].set_title('(B)',x=0.02,y=0.7,fontweight='bold')
#ax[2].set_title('(C)',x=0.02,y=0.7,fontweight='bold')
#ax[3].set_title('(D)',x=0.02,y=0.7,fontweight='bold')
#ax[4].set_title('(E)',x=0.02,y=0.7,fontweight='bold')
#ax[5].set_title('(F)',x=0.02,y=0.7,fontweight='bold')
#ax[6].set_title('(G)',x=0.02,y=0.7,fontweight='bold')
#ax[7].set_title('(H)',x=0.02,y=0.7,fontweight='bold')
#ax[3].legend(bbox_to_anchor=(1.10, 0.8),  loc='center' , borderaxespad=0.,fontsize=10,handletextpad=0.03,labelspacing=0.02,ncol=1,columnspacing=0.2,title="SOIL DEPTHS\n(A,B,C,D,E,F)")
ax[1].legend(bbox_to_anchor=(0.5, 2.45),  loc='center' , borderaxespad=0.,fontsize=10,handletextpad=0.03,labelspacing=0.02,ncol=8,columnspacing=0.4,title="SOIL DEPTHS")
#ax[2].legend(bbox_to_anchor=(1.09, 0.5 ), loc='center' , borderaxespad=0.,fontsize=12,handletextpad=0.03,labelspacing=0.02,ncol=1,columnspacing=0.4)

#ax[0].set_title('(A) Column 1, A type',x=0.01,y=0.8,fontweight='bold',loc='left')
#ax[1].set_title('(B) Column 2, B type',x=0.01,y=0.8,fontweight='bold',loc='left')
#ax[2].set_title('(C) Column 3, D type',x=0.01,y=0.8,fontweight='bold',loc='left')
#ax[3].set_title('(D) Column 4, D + A type',x=0.01,y=0.8,fontweight='bold',loc='left')
#ax[4].set_title('(E) Column 5, D + B type',x=0.01,y=0.8,fontweight='bold',loc='left')
#ax[5].set_title('(F) Column 6, A +B + D type',x=0.01,y=0.8,fontweight='bold',loc='left')
#ax[3].set_title('(D)',x=0.04,y=0.75,fontweight='bold')
ax[3].xaxis.set_major_formatter(mdates.DateFormatter('%b-%d'))

#ax[4].set_title('(E)',x=0.03,y=0.75,fontweight='bold')
#ax[5].set_title('(F)',x=0.03,y=0.75,fontweight='bold')
#ax[6].set_title('(G)',x=0.03,y=0.75,fontweight='bold')
#ax[7].set_title('(H)',x=0.03,y=0.75,fontweight='bold')
#xlim=[sp_sch[sch_name].df.time_days[0],sp_sch[sch_name].df.time_days[len(sp_sch[sch_name].df)-1]]
#ax[0].set_xlim(xlim)
#ax[1].set_xlim(xlim)
#ax[2].set_xlim(xlim)
#ax[3].set_xlim(xlim)
#ax[4].set_xlim(xlim)
#ax[5].set_xlim(xlim)
#ax[6].set_xlim(xlim)
#ax[7].set_xlim(xlim)
#ax[0].set_xticklabels([])
#ax[1].set_xticklabels([])
#ax[2].set_xticklabels([])
#ax[3].set_xticklabels([])
#ax[4].set_xticklabels([])
#ax[5].set_xticklabels([])
#ax[6].set_xticklabels([])
#plt.text(0.5, 0.5, 's', fontsize=18)
#plt.text(-100,1000, 'Moisture\nsensor 1', fontsize=18,color='b')
#ax_img.annotate('Moisture\nsensor A',
#            xy=(300, 1000),
#            xytext=(0.51, 0.6),    # fraction, fraction
#            textcoords='figure fraction',
#            arrowprops=dict(facecolor='yellow', shrink=0.05),
#            horizontalalignment='left',
#            verticalalignment='bottom',fontsize=18
#            )
#ax_img.annotate('Moisture\nsensor B',
#            xy=(200, 1200),
#            xytext=(0.51, 0.5),    # fraction, fraction
#            textcoords='figure fraction',
#            arrowprops=dict(facecolor='yellow', shrink=0.05),
#            horizontalalignment='left',
#            verticalalignment='bottom',fontsize=18
#            )
#ax_img.annotate('Suction\nsensor A',
#            xy=(300, 1400),
#            xytext=(0.51, 0.4),    # fraction, fraction
#            textcoords='figure fraction',
#            arrowprops=dict(facecolor='yellow', shrink=0.05),
#            horizontalalignment='left',
#            verticalalignment='bottom',fontsize=18
#            )
#ax_img.annotate('Suction\nsensor B',
#            xy=(400, 1600),
#            xytext=(0.51, 0.3),    # fraction, fraction
#            textcoords='figure fraction',
#            arrowprops=dict(facecolor='yellow', shrink=0.05),
#            horizontalalignment='left',
#            verticalalignment='bottom',fontsize=18
#            )


plt.show(block=False)


fig.savefig('figure/plot_'+sch_name+'.png', format='png', dpi=600)
#plt.close()



#sp_sch[sch_name].df.to_csv('output_data/'+sch_name+'.csv', sep=',', encoding='utf-8')

