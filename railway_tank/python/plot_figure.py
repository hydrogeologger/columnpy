import re
import os
import gc
import pandas as pd
import numpy as np
from tqdm import tqdm
import matplotlib
import matplotlib.image as image
import matplotlib.pylab as pylab
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

current_path=os.getcwd()


color_list = ['red','orange','maroon','gold','darkblue','olive','blue','violet']
moisture_label_list = ['5 cm (M1)','15 cm (M2)','15 cm (M3)',
              '25 cm (M4)','25 cm (M5)','35 cm (M6)','35 cm (M7)']
selected_suction_list = ['suctionb3','suctionc3','suctionf0','suctionh1']
suction_label_list = ['5 cm (S1)','15 cm (S2)','25 cm (S4)','35 cm (S5)']

#vwc_suction_list = ['suctiona0_vwc','suctionb0_vwc','suctiond0_vwc','suctione0_vwc','suctiong0_vwc','suctionh0_vwc']

vwc_suction_list = ['suctiona0_vwc','suctionb0_vwc','suctiond0_vwc','suctione0_vwc','suctionf0_vwc','suctiong0_vwc','suctionh0_vwc']
vwc_suction_label_list = ['5 cm (S1)','15 cm (S2)','15 cm (S3)',
              '25 cm (S4)','25 cm (S5)','35 cm (S6)','35 cm (S7)']

#raw_temperature_list = ['temp_a','temp_b','temp_c','temp_d','temp_e','temp_f','temp_g','temp_h']
raw_temperature_list = ['temp_a','temp_b','temp_d','temp_e','temp_f','temp_g','temp_h']
temperature_label_list = ['5 cm (S1)','15 cm (S2)','15 cm (S3)',
              '25 cm (S4)','25 cm (S5)','35 cm (S6)','35 cm (S7)']

moisture_color_dict = dict(zip(moisture_list,color_list))
moisture_label_dict = dict(zip(moisture_list,moisture_label_list))
suction_label_dict = dict(zip(selected_suction_list,suction_label_list))
vwc_label_dict = dict(zip(vwc_suction_list,vwc_suction_label_list))
temperature_label_dict = dict(zip(raw_temperature_list,temperature_label_list))
#sns.set_style('whitegrid')
params = {'legend.fontsize': 4,
          #'figure.figsize': (10, 5),
         'axes.labelsize': '15',
         'axes.linewidth':'3', 
         'axes.titlesize':'15',
         'xtick.labelsize':'15',
         'ytick.labelsize':'15',
         'font.weight':'bold',
         #'font.sans-serif':'Arial',
         'axes.labelweight':'bold',
         'lines.linewidth':2}
lw=3
ms=6
mew=2
grid_width=2
y_fontsize=15
pylab.rcParams.update(params)

#grid = plt.GridSpec(4, 1, wspace=0.3, hspace=0.1)
#fig = plt.figure(figsize=(90, 50)) #120,60
#ax_0 = fig.add_subplot(grid[0, 0])
#ax_1 = fig.add_subplot(grid[1, 0], sharex=ax_0)
#ax_2 = fig.add_subplot(grid[2, 0], sharex=ax_0)
#ax_3 = fig.add_subplot(grid[3, 0], sharex=ax_0)

fig, ax = plt.subplots(4,sharex=True,figsize=(13,15))
#fig, ax = plt.subplots(3,sharex=True,figsize=(10,10))
fig.subplots_adjust(hspace=.10)
fig.subplots_adjust(left=0.15, right=0.79, top=0.97, bottom=0.05)

for idx,i in enumerate(moisture_list):
  ax[0].plot(
      sp_sch[sch_name].df.index,
      sp_sch[sch_name].df[i],
      '-',
      color = color_list[idx],
      markersize = ms,
      markeredgewidth = mew,
      fillstyle = 'full',
      label = moisture_label_dict[i]
  )
for idx, i in enumerate(selected_suction_list):
  ax[1].semilogy(
      sp_sch[sch_name].df.index,
      sp_sch[sch_name].df[i],
      '-',
      color = color_list[idx],
      markeredgewidth = mew,
      fillstyle = 'full',
      label = suction_label_dict[i]    
  )
for idx,i in enumerate(vwc_suction_list):
  ax[2].semilogy(
      sp_sch[sch_name].df.index,
      sp_sch[sch_name].df[i],
      '-',
      color = color_list[idx],
      markeredgewidth = mew,
      fillstyle = 'full',
      label = vwc_label_dict[i]   
  )  
for idx,i in enumerate(raw_temperature_list):
  ax[3].plot(
      sp_sch[sch_name].df.index,
      sp_sch[sch_name].df[i],
      '-',
      color = color_list[idx],
      markeredgewidth = mew,
      fillstyle = 'full',
      label = temperature_label_dict[i]   
  )

ax[0].set_ylabel('DEG. OF SAT.', fontsize=y_fontsize, labelpad=20)
#ax_0.grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
ax[0].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
ax[0].set_ylim([0,1])
ax[0].set_xlim([sp_sch[sch_name].df.index[0],sp_sch[sch_name].df.index[-1]])
ax[0].legend(bbox_to_anchor=(1.01, 0.5 ),
            loc='center left', borderaxespad=0.,
            fontsize=y_fontsize,handletextpad=0.03,
            labelspacing=0.02,ncol=1,columnspacing=0.4)
ax[0].set_title('(A)',x=0.02,y=0.05, fontsize=15)
ax[1].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
ax[1].set_ylabel('SUCTION (kPa)\nIN EMBANKMENT', fontsize=y_fontsize, labelpad=20)
ax[1].set_ylim([10,10e5])
ax[1].legend(bbox_to_anchor=(1.01, 0.5 ), 
            loc='center left', borderaxespad=0.,
            fontsize=y_fontsize,handletextpad=0.03,
            labelspacing=0.02,ncol=1,columnspacing=0.4)
ax[1].set_title('(B)',x=0.02,y=0.9,fontsize=15)
ax[2].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
ax[2].set_ylabel('SUCTION (kPa)\nIN SUBGRADE', fontsize=y_fontsize, labelpad=20)
#ax_2.set_xlabel('DATE', fontsize=y_fontsize,labelpad=3)
ax[2].set_ylim([10**2.4,3e6])
ax[2].legend(bbox_to_anchor=(1.01, 0.5),
            loc='center left', borderaxespad=0.,
            fontsize=y_fontsize,handletextpad=0.03,
            labelspacing=0.02,ncol=1,columnspacing=0.4)
ax[2].set_title('(C)',x=0.02,y=0.9,fontsize=15)
ax[3].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
ax[3].set_ylabel('TEMPERATURE\n($^\circ$C)', fontsize=y_fontsize, labelpad=20)
ax[3].set_xlabel('DATE', fontsize=y_fontsize,labelpad=3)
ax[3].set_ylim([20,42])
ax[3].legend(bbox_to_anchor=(1.01, 0.5), loc='center left', 
            borderaxespad=0.,fontsize=y_fontsize,
            handletextpad=0.03,labelspacing=0.02,
            ncol=1,columnspacing=0.4)
ax[3].set_title('(D)',x=0.02,y=0.9,fontsize=15)
ax[3].xaxis.set_major_formatter(mdates.DateFormatter('%d/%b'))
#plt.show(block=True)
#plt.show(block=False)

#plt.savefig(current_path+'/test.jpg')
plt.savefig(current_path+'/test_with_M5.jpg')
