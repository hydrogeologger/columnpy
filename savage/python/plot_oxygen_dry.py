import matplotlib
import matplotlib.image as image

# Force matplotlib to not use any Xwindows backend.
#matplotlib.use('Agg')
import matplotlib.pyplot as plt

import glob, os
#os.chdir("/home/chenming/Projects/tailings/area_51_redmud_4cm_photo/")
#img_list=glob.glob('/home/chenming/Projects/tailings/area_51_redmud_4cm_photo/*.jpg')
#for file in glob.glob("*.jpg"):
#    print(file)
sch_name='oxygen_dry'


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

lw=2
ms=6
mew=2
grid_width=2
y_fontsize=10
fig, ax = plt.subplots(6,sharex=True,figsize=(8.5,9))
fig.subplots_adjust(hspace=.10)
fig.subplots_adjust(left=0.15, right=0.95, top=0.93, bottom=0.08)
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


sp=prof['grange_a_electrochem_o2']['data'].df[::48]
sp_lo=prof['grange_a_luo2']['data'].df[::48]

#ax[0].plot(sp_sch[sch_name].df.time_days, sp_sch[sch_name].df.ir_up/100.0,'-',color='r'       ,markersize=ms-7,markeredgewidth=mew, markeredgecolor='brown',label='up',markevery=1)
#ax[0].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.ir_down[:idx_im],'o',color='k'       ,markersize=ms,markeredgewidth=mew, markeredgecolor='k',label='down',markevery=3)
mark_every=128
iv=5
ax[0].plot(   sp.index[::iv],      sp.dox6_c[::iv],'-',color='royalblue',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='0.5m',markevery=mark_every,ms=12)
ax[0].plot(sp_lo.index[::iv],    sp_lo.wluo6[::iv],'-',color='lightblue',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='b',label='1.0m',markevery=mark_every,ms=12)
ax[0].plot(sp_lo.index[::iv],    sp_lo.wluo5[::iv],'-',color='limegreen',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='1.5m',markevery=mark_every,ms=12)
ax[0].plot(   sp.index[::iv],      sp.dox3_c[::iv],'-',color='olive'    ,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='2.0m',markevery=mark_every,ms=12)
ax[0].plot(   sp.index[::iv],      sp.dox2_c[::iv],'-',color='gold'     ,markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='2.5m',markevery=mark_every,ms=12)
ax[0].plot(   sp.index[::iv],      sp.dox1_c[::iv],'-',color='peru'     ,markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='3.0m',ms=12,markevery=mark_every)
ax[0].plot(   sp.index[::iv],      sp.dox0_c[::iv],'-',color='maroon'   ,markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='3.5m',markevery=mark_every)

#ax[0].plot(sp.index,      sp.dox0_c,'-',color='maroon'   ,markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='4 cm',markevery=mark_every)
#ax[0].plot(sp.index,      sp.dox1_c,'-',color='peru'     ,markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='8 cm',ms=12,markevery=mark_every)
#ax[0].plot(sp.index,      sp.dox2_c,'-',color='gold'     ,markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='13cm',markevery=mark_every,ms=12)
#ax[0].plot(sp.index,      sp.dox3_c,'-',color='olive'    ,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='20cm',markevery=mark_every,ms=12)
#ax[0].plot(sp_lo.index, sp_lo.wluo5,'-',color='limegreen',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='30cm',markevery=mark_every,ms=12)
#ax[0].plot(sp_lo.index, sp_lo.wluo6,'-',color='lightblue',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='b',label='60cm',markevery=mark_every,ms=12)
#ax[0].plot(sp.index,      sp.dox6_c,'-',color='royalblue',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='85cm',markevery=mark_every,ms=12)


sp=prof['grange_b_electrochem_o2']['data'].df
sp_lo=prof['grange_b_luo2']['data'].df
mark_every=124
iv=35
ax[1].plot(sp.index[::iv], sp.dox7_c[::iv],'-',color='darkblue',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='0.5m',markevery=mark_every,ms=12)
ax[1].plot(sp.index[::iv], sp.dox6_c[::iv],'-',color='royalblue',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='1.0m',markevery=mark_every,ms=12)
ax[1].plot(sp.index[::iv], sp.dox5_c[::iv],'-',color='lightblue',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='b',label='1.5m',markevery=mark_every,ms=12)
ax[1].plot(sp_lo.index[::iv], sp_lo.dluo4[::iv],'-',color='limegreen',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='2.0m',markevery=mark_every,ms=12)
ax[1].plot(sp.index[::iv], sp.dox3_c[::iv],'-',color='olive',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='2.5m',markevery=mark_every,ms=12)
ax[1].plot(sp_lo.index[::iv], sp_lo.dluo2[::iv],'-',color='gold',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='3.0m',markevery=mark_every,ms=12)
ax[1].plot(sp.index[::iv], sp.dox1_c[::iv],'-',color='peru',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='3.5m',ms=12,markevery=mark_every)
ax[1].plot(sp.index[::iv], sp.dox0_c[::iv],'-',color='maroon',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='4.0m',markevery=mark_every)


sp=prof['grange_d_electrochem_o2']['data'].df
sp_lo=prof['grange_d_luo2']['data'].df
mark_every=148
iv=50
ax[2].plot(sp_lo.index[::iv], sp_lo.dluo7[::iv],'-',color='darkblue',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='0.5m',markevery=mark_every,ms=12)
ax[2].plot(sp.index[::iv], sp.dox6_c[::iv],'-',color='royalblue',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='1.0m',markevery=mark_every,ms=12)
ax[2].plot(sp_lo.index[::iv], sp_lo.dluo5[::iv],'-',color='lightblue',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='b',label='1.5m',markevery=mark_every,ms=12)
ax[2].plot(sp.index[::iv], sp.dox4_c[::iv],'-',color='limegreen',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='2.0m',markevery=mark_every,ms=12)
ax[2].plot(sp.index[::iv], sp.dox3_c[::iv],'-',color='olive',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='2.5m',markevery=mark_every,ms=12)
ax[2].plot(sp.index[::iv], sp.dox2_c[::iv],'-',color='gold',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='3.0m',markevery=mark_every,ms=12)
ax[2].plot(sp.index[::iv], sp.dox1_c[::iv],'-',color='peru',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='3.5m',ms=12,markevery=mark_every)
ax[2].plot(sp.index[::iv], sp.dox0_c[::iv],'-',color='maroon',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='4.0m',markevery=mark_every)




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


sp_wlo=prof['grange_5_luo2_wet']['data'].df
sp_dlo=prof['grange_5_luo2_dry']['data'].df
sp_moi=prof['grange_5_mo_su']['data'].df
mark_every=24
iv=50
ax[3].plot(sp_moi.index[::iv], sp_moi.dluo7[::iv],'-',color='darkblue',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='0.5m',markevery=mark_every,ms=12)
ax[3].plot(sp_dlo.index[::iv], sp_dlo.dluo6[::iv],'-',color='royalblue',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='1.0m',markevery=mark_every,ms=12)
ax[3].plot(sp_dlo.index[::iv], sp_dlo.dluo5[::iv],'-',color='lightblue',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='b',label='1.5m',markevery=mark_every,ms=12)
ax[3].plot(sp_dlo.index[::iv], sp_dlo.dluo4[::iv],'-',color='limegreen',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='2.0m',markevery=mark_every,ms=12)
ax[3].plot(sp_dlo.index[::iv], sp_dlo.dluo3[::iv],'-',color='olive',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='2.5m',markevery=mark_every,ms=12)
ax[3].plot(sp_dlo.index[::iv], sp_dlo.dluo2[::iv],'-',color='gold',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='3.0m',markevery=mark_every,ms=12)
ax[3].plot(sp_dlo.index[::iv], sp_dlo.dluo1[::iv],'-',color='peru',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='3.5m',ms=12,markevery=mark_every)
ax[3].plot(sp_dlo.index[::iv], sp_dlo.dluo0[::iv],'-',color='maroon',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='4.0m',markevery=mark_every)



sp_wlo=prof['grange_3_luo2_wet']['data'].df
sp_dlo=prof['grange_3_luo2_dry']['data'].df
sp_moi=prof['grange_3_mo_su']['data'].df
mark_every=24
iv=50
ax[4].plot(sp_moi.index[::iv], sp_moi.dluo7[::iv],'-',color='darkblue',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='0.5m',markevery=mark_every,ms=12)
ax[4].plot(sp_dlo.index[::iv], sp_dlo.dluo6[::iv],'-',color='royalblue',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='1.0m',markevery=mark_every,ms=12)
ax[4].plot(sp_dlo.index[::iv], sp_dlo.dluo5[::iv],'-',color='lightblue',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='b',label='1.5m',markevery=mark_every,ms=12)
ax[4].plot(sp_dlo.index[::iv], sp_dlo.dluo4[::iv],'-',color='limegreen',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='2.0m',markevery=mark_every,ms=12)
ax[4].plot(sp_dlo.index[::iv], sp_dlo.dluo3[::iv],'-',color='olive',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='2.5m',markevery=mark_every,ms=12)
ax[4].plot(sp_dlo.index[::iv], sp_dlo.dluo2[::iv],'-',color='gold',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='3.0m',markevery=mark_every,ms=12)
ax[4].plot(sp_dlo.index[::iv], sp_dlo.dluo1[::iv],'-',color='peru',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='3.5m',ms=12,markevery=mark_every)
ax[4].plot(sp_dlo.index[::iv], sp_dlo.dluo0[::iv],'-',color='maroon',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='4.0m',markevery=mark_every)


sp_wlo=prof['grange_4_luo2_wet']['data'].df
sp_dlo=prof['grange_4_luo2_dry']['data'].df
sp_moi=prof['grange_4_mo_su']['data'].df
mark_every=24
iv=50
ax[5].plot(sp_moi.index[::iv], sp_moi.dluo7[::iv],'-',color='darkblue',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='0.5m',markevery=mark_every,ms=12)
ax[5].plot(sp_dlo.index[::iv], sp_dlo.dluo6[::iv],'-',color='royalblue',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='1.0m',markevery=mark_every,ms=12)
ax[5].plot(sp_dlo.index[::iv], sp_dlo.dluo5[::iv],'-',color='lightblue',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='b',label='1.5m',markevery=mark_every,ms=12)
ax[5].plot(sp_dlo.index[::iv], sp_dlo.dluo4[::iv],'-',color='limegreen',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='2.0m',markevery=mark_every,ms=12)
ax[5].plot(sp_dlo.index[::iv], sp_dlo.dluo3[::iv],'-',color='olive',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='2.5m',markevery=mark_every,ms=12)
ax[5].plot(sp_dlo.index[::iv], sp_dlo.dluo2[::iv],'-',color='gold',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='3.0m',markevery=mark_every,ms=12)
ax[5].plot(sp_dlo.index[::iv], sp_dlo.dluo1[::iv],'-',color='peru',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='3.5m',ms=12,markevery=mark_every)
ax[5].plot(sp_dlo.index[::iv], sp_dlo.dluo0[::iv],'-',color='maroon',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='4.0m',markevery=mark_every)




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
ax[0].set_ylabel('OXYGEN CONC.\nCOLUMN 1\n A TYPE\n(%)', fontsize=y_fontsize, labelpad=10)
ax[1].set_ylabel('OXYGEN CONC.\nCOLUMN 2\n B TYPE\n(%)', fontsize=y_fontsize, labelpad=10)
ax[2].set_ylabel('OXYGEN CONC.\nCOLUMN 3\n D TYPE\n(%)', fontsize=y_fontsize, labelpad=10)
ax[3].set_ylabel('OXYGEN CONC.\nCOLUMN 4\n D + A TYPE\n(%)', fontsize=y_fontsize, labelpad=10)
ax[4].set_ylabel('OXYGEN CONC.\nCOLUMN 5\n D + B TYPE\n(%)', fontsize=y_fontsize, labelpad=10)
ax[5].set_ylabel('OXYGEN CONC.\nCOLUMN 6\n A + B + D\n(%)', fontsize=y_fontsize, labelpad=10)

##ax[2].set_ylabel('DEGREE OF SAT.\nBY DIELECTRIC\nMOISTURE\nSENSOR', fontsize=y_fontsize, labelpad=10)
#ax[2].set_ylabel('SUCTION (kPa)', fontsize=y_fontsize, labelpad=10)
#ax[3].set_ylabel('TEMPERATURE\n($^\circ$c)', fontsize=y_fontsize, labelpad=10)
##ax[5].set_ylabel('TEMPERATURE\n($^\circ$c)', fontsize=y_fontsize, labelpad=20)
##ax[6].set_ylabel('NORMALIZED\nRISE OF\nTEMPERATURE', fontsize=y_fontsize, labelpad=10)
##ax[7].set_ylabel('SUCTION BY\nTEMPERATURE\nHUMIDITY\n SENSOR (m)', fontsize=y_fontsize, labelpad=10)

ax[5].set_xlabel('DATE', fontsize=y_fontsize,labelpad=3)
#ax[0].set_ylim([0,10])
#ax[1].set_ylim([0,60])
#ax2.set_ylim([0,2500])
ax[0].set_ylim([-2,25])
ax[1].set_ylim([-2,25])
ax[2].set_ylim([-2,25])
ax[3].set_ylim([-2,25])
ax[4].set_ylim([-2,25])
ax[5].set_ylim([-2,25])
#ax[7].legend(bbox_to_anchor=(.1, 0.55 ), loc=2, borderaxespad=0.)
#ax[0].set_title('(A)',x=0.02,y=0.7,fontweight='bold')
#ax[1].set_title('(B)',x=0.02,y=0.7,fontweight='bold')
#ax[2].set_title('(C)',x=0.02,y=0.5,fontweight='bold')
#ax[3].set_title('(D)',x=0.02,y=0.5,fontweight='bold')
#ax[4].set_title('(E)',x=0.02,y=0.5,fontweight='bold')
#ax[5].set_title('(F)',x=0.02,y=0.7,fontweight='bold')
#ax[6].set_title('(G)',x=0.02,y=0.7,fontweight='bold')
#ax[7].set_title('(H)',x=0.02,y=0.7,fontweight='bold')
#ax[5].legend(bbox_to_anchor=(1.10, 0.06),  loc='center' , borderaxespad=0.,fontsize=10,handletextpad=0.03,labelspacing=0.02,ncol=1,columnspacing=0.4,title="SOIL DEPTHS\n(C,D,E,F,G,H)")
ax[1].legend(bbox_to_anchor=(0.5, 2.37),  loc='center' , borderaxespad=0.,fontsize=10,handletextpad=0.03,labelspacing=0.02,ncol=8,columnspacing=0.4,title="SOIL DEPTHS")
#ax[2].legend(bbox_to_anchor=(1.09, 0.5 ), loc='center' , borderaxespad=0.,fontsize=12,handletextpad=0.03,labelspacing=0.02,ncol=1,columnspacing=0.4)

#ax[0].set_title('(A) Column 1, A type',x=0.01,y=0.8,fontweight='bold',loc='left')
#ax[1].set_title('(B) Column 2, B type',x=0.01,y=0.8,fontweight='bold',loc='left')
#ax[2].set_title('(C) Column 3, D type',x=0.01,y=0.8,fontweight='bold',loc='left')
#ax[3].set_title('(D) Column 4, D + A type',x=0.01,y=0.8,fontweight='bold',loc='left')
#ax[4].set_title('(E) Column 5, D + B type',x=0.01,y=0.8,fontweight='bold',loc='left')
#ax[5].set_title('(F) Column 6, A +B + D type',x=0.01,y=0.8,fontweight='bold',loc='left')
#ax[3].set_title('(D)',x=0.04,y=0.75,fontweight='bold')
ax[3].xaxis.set_major_formatter(mdates.DateFormatter('%b/%y'))

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

