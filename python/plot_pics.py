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
output_path = current_path+'/finalselected/'
output_figure_path = current_path+'/output_figure/'

list_path = os.listdir(output_path)
pic_dict = {}
for old_name in list_path[:]:
  if old_name[-3:]=='jpg':
    old_name = os.path.join(output_path, old_name)
    #print('old_name:', old_name)
    #new_name = src_output_pathpath + '/' + ''.join(i for i in re.findall(r"\d+",old_name))[:11] +'.jpg'
    pic_idx = pd.to_datetime(''.join(re.findall(r"\d+",old_name))[:],format = ('%Y%m%d%H%M%S')).strftime('%Y-%m-%d %H:%M:%S')
    #pic_path = 
    pic_dict[pic_idx]=old_name
    #print(os.listdir(output_path)[1])
#print(pic_dict)
pic_dict_keys = list(pic_dict.keys())

# plot the pic which has the cloeset date of the data
def pic_of_closest_date(date):
  time_diff = abs(pd.to_datetime(pic_dict_keys)-date)
  min_idx = np.asarray(np.where(time_diff==min(time_diff))).flatten()
  return pic_dict[pic_dict_keys[min_idx[0]]]


color_list = ['red','orange','maroon','gold','darkblue','olive','blue','violet']
moisture_label_list = ['5 cm (M1)','15 cm (M2)','15 cm (M3)',
              '25 cm (M4)','25 cm (M5)','35 cm (M6)','35 cm (M7)']
selected_suction_list = ['suctionb3','suctionc3','suctionf0','suctionh1']
suction_label_list = ['5 cm (S1)','15 cm (S2)','25 cm (S4)','35 cm (S5)']

vwc_suction_list = ['suctiona0_vwc','suctionb0_vwc','suctiond0_vwc','suctione0_vwc','suctiong0_vwc','suctionh0_vwc']
vwc_suction_label_list = ['5 cm (S1)','15 cm (S2)','15 cm (S3)',
              '25 cm (S4)','25 cm (S5)','35 cm (S6)']

raw_temperature_list = ['temp_a','temp_b','temp_c','temp_d','temp_e','temp_f','temp_g','temp_h']
temperature_label_list = ['5 cm (S1)','5 cm (S2)','15 cm (S3)','15 cm (S4)',
              '25 cm (S5)','25 cm (S6)','35 cm (S7)','35 cm (S8)']

moisture_color_dict = dict(zip(moisture_list,color_list))
moisture_label_dict = dict(zip(moisture_list,moisture_label_list))
suction_label_dict = dict(zip(selected_suction_list,suction_label_list))
vwc_label_dict = dict(zip(vwc_suction_list,vwc_suction_label_list))
temperature_label_dict = dict(zip(raw_temperature_list,temperature_label_list))
#sns.set_style('whitegrid')
params = {'legend.fontsize': 4,
          #'figure.figsize': (10, 5),
         'axes.labelsize': '25',
         'axes.linewidth':'2',
         'axes.titlesize':'20',
         'xtick.labelsize':'50',
         'ytick.labelsize':'50',
         'font.weight':'bold',
         #'font.sans-serif':'Arial',
         'axes.labelweight':'bold',
         'lines.linewidth':10,}
lw=2
ms=6
mew=2
grid_width=5
y_fontsize=50
pylab.rcParams.update(params)


for date_idx,date_i in enumerate(tqdm(sp_sch[sch_name].df.index[::4][0:10],ncols = 100)):
  grid = plt.GridSpec(4, 2, wspace=0.3, hspace=0.1)
  fig = plt.figure(figsize=(90, 40)) #120,60
  ax_0 = fig.add_subplot(grid[2:3, 0:1])
  ax_1 = fig.add_subplot(grid[2:3, 1:2], sharex=ax_0)
  ax_2 = fig.add_subplot(grid[3:4, 0:1], sharex=ax_0)
  ax_3 = fig.add_subplot(grid[3:4, 1:2], sharex=ax_0)
  ax_4 = fig.add_subplot(grid[0:2, 0:2])

  
  I = plt.imread(pic_of_closest_date(date_i))
  #pic_of_closest_date(sp_sch[sch_name].df.index[100])
  #print(pic_of_closest_date(date_i))
  ax_4.imshow(I)

  #plt.xlim(sp_sch[sch_name].df.index[0], sp_sch[sch_name].df.index[-1])
  #plt.xticks(rotation=45)

  for idx,i in enumerate(moisture_list):
    ax_0.plot(
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
    ax_1.semilogy(
        sp_sch[sch_name].df.index,
        sp_sch[sch_name].df[i],
        '-',
        color = color_list[idx],
        markeredgewidth = mew,
        fillstyle = 'full',
        label = suction_label_dict[i]    
    )

  for idx,i in enumerate(vwc_suction_list):
    ax_2.semilogy(
        sp_sch[sch_name].df.index,
        sp_sch[sch_name].df[i],
        '-',
        color = color_list[idx],
        markeredgewidth = mew,
        fillstyle = 'full',
        label = vwc_label_dict[i]   
    )  

  for idx,i in enumerate(raw_temperature_list):
    ax_3.plot(
        sp_sch[sch_name].df.index,
        sp_sch[sch_name].df[i],
        '-',
        color = color_list[idx],
        markeredgewidth = mew,
        fillstyle = 'full',
        label = temperature_label_dict[i]   
    )

  #for old_name in list_path[]:
    #old_name = os.path.join(src_path, old_name)
    #print('old_name:', old_name)
    #new_name = src_path + '/' + ''.join(i for i in re.findall(r"\d+",old_name))[:11] +'.jpg'
    #I = plt.imread(pic_dict[pic_idx])
    #ax_4.imshow(I)



  ax_0.set_ylabel('DEG. OF SAT.', fontsize=y_fontsize, labelpad=20)
  ax_0.grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
  ax_0.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m'))
  ax_0.set_ylim([0,1])
  ax_0.set_xlim([sp_sch[sch_name].df.index[0],sp_sch[sch_name].df.index[-1]])
  ax_0.legend(bbox_to_anchor=(1.01, 0.5 ),
              loc='center left', borderaxespad=0.,
              fontsize=40,handletextpad=0.03,
              labelspacing=0.02,ncol=1,columnspacing=0.4)
  ax_0.set_title('(A)',x=0.02,y=0.05, fontsize=50)

  ax_1.grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
  ax_1.set_ylabel('SUCTION (kPa)\nIN EMBANKMENT', fontsize=y_fontsize, labelpad=20)
  ax_1.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m'))
  ax_1.set_ylim([10,10e5])
  ax_1.legend(bbox_to_anchor=(1.01, 0.5 ), 
              loc='center left', borderaxespad=0.,
              fontsize=40,handletextpad=0.03,
              labelspacing=0.02,ncol=1,columnspacing=0.4)
  ax_1.set_title('(B)',x=0.02,y=0.9,fontsize=50)

  ax_2.grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
  ax_2.set_ylabel('SUCTION (kPa)\nIN SUBGRADE', fontsize=y_fontsize, labelpad=20)
  ax_2.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m'))
  ax_2.set_xlabel('DATE', fontsize=y_fontsize,labelpad=3)
  ax_2.set_ylim([10**2.4,3e4])
  ax_2.legend(bbox_to_anchor=(1.01, 0.5),
              loc='center left', borderaxespad=0.,
              fontsize=40,handletextpad=0.03,
              labelspacing=0.02,ncol=1,columnspacing=0.4)
  ax_2.set_title('(C)',x=0.02,y=0.9,fontsize=50)

  ax_3.grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
  ax_3.set_ylabel('TEMPERATURE\n($^\circ$C)', fontsize=y_fontsize, labelpad=20)
  ax_3.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m'))
  ax_3.set_xlabel('DATE', fontsize=y_fontsize,labelpad=3)
  ax_3.set_ylim([20,42])
  ax_3.legend(bbox_to_anchor=(1.01, 0.5), loc='center left', 
              borderaxespad=0.,fontsize=40,
              handletextpad=0.03,labelspacing=0.02,
              ncol=1,columnspacing=0.4)
  ax_3.set_title('(D)',x=0.02,y=0.9,fontsize=50)

  ax_0.axvline(date_i,color="red")
  ax_1.axvline(date_i,color="red")
  ax_2.axvline(date_i,color="red")
  ax_3.axvline(date_i,color="red")

  ax_4.axis('off')

  plt.savefig(output_figure_path+'{}.jpg'.format(date_i))
  #plt.clf()
  #plt.tight_layout()
  #plt.show()
  gc.collect()

  plt.close('all')
  #plt.close(fig)
  