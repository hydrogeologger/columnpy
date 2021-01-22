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



current_path=os.getcwd()+'/Redmud_infiltration_test'
column1_back_photo = current_path+'/photos/column1_back/'
column2_back_photo = current_path+'/photos/column2_back/'
column1_front_photo = current_path+'/photos/column1_front/'
column2_front_photo = current_path+'/photos/column2_front/'
photo_path = current_path+'/photos/'

photo_dir_list = [column1_back_photo,column2_back_photo,
            column1_front_photo,column2_front_photo]

data_file_path = current_path+'/data/'

data = pd.read_csv(data_file_path+'result.csv')
data['date_time'] = pd.to_datetime(data['date_time'],format='%Y-%m-%d %H:%M:%S.%f')
data.set_index("date_time", inplace=True)

# create pic_dict_keys
key_list = ['column1_front','column2_front',
                'column1_back','column2_back']

pic_dict = { x: {} for x in key_list}

# I really cant find a better way to do this.. 
# if you can plz change these shit
# the purpose for these shit is to identify the pic name 
# and put the date:path to the empty dict

for i in photo_dir_list: # four folder in this path
    for name in os.listdir(i): # path name
        if name[-3:] == 'jpg':
            for ii in key_list: # get the keywords
                if ii in name: # identify which keyword should this pic locate
                    path = os.path.join(i,name)
                    pic_idx = pd.to_datetime(''.join(re.findall(r'\d+',path))[2:],
                        format=('%Y%m%d%H%M%S')).strftime('%Y-%m-%d %H:%M:%S')
                    pic_dict[ii][pic_idx]=path # put the date:path to the big nested dict

            #if 'column1_front' in name:
            #    path = os.path.join(output_figure_path,name)
            #    pic_idx = pd.to_datetime(''.join(re.findall(r'\d+',path))[1:],
            #            format=('%Y%m%d%H%M%S')).strftime('%Y-%m-%d %H:%M:%S')
            #    pic_dict['column1_front'][pic_idx]=path
            
def pic_of_closest_date(column_name,date):
  time_diff = abs(pd.to_datetime(list(pic_dict[f'{column_name}'].keys()))-date)
  min_idx = np.asarray(np.where(time_diff==min(time_diff))).flatten()
  return pic_dict[f'{column_name}'][list(pic_dict[f'{column_name}'].keys())[min_idx[0]]]


  color_list = ['red','blue']

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


grid = fig.add_gridspec(nrows=5, ncols=4)
fig = plt.figure(figsize=(50, 40)) #120,60
ax_0 = fig.add_subplot(grid[-2,:])
ax_1 = fig.add_subplot(grid[0:3,0])
ax_2 = fig.add_subplot(grid[0:3,1])
ax_3 = fig.add_subplot(grid[0:3,2])
ax_4 = fig.add_subplot(grid[0:3,3])

#ax_1.axis('off')
#ax_2.axis('off')
#ax_3.axis('off')
#ax_4.axis('off')

df_column_list = ['scale1','scale2']

for idx,i in enumerate(df_column_list):
  ax_0.plot(
      data.index,
      data[i],
      '-',
      color = color_list[idx],
      markersize = ms,
      markeredgewidth = mew,
      fillstyle = 'full',
      label = df_column_list[idx]
  )

ax_0.set_ylabel('Weight', fontsize=y_fontsize, labelpad=20)
ax_0.grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
ax_0.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m'))
#ax_0.set_ylim([0,1])
ax_0.set_xlim([data.index[0],data.index[-1]])
ax_0.set_xlabel('DATE', fontsize=y_fontsize,labelpad=3)
ax_0.legend(bbox_to_anchor=(0, 0.5 ),
            loc='center left', borderaxespad=0.,
            fontsize=40,handletextpad=0.03,
            labelspacing=0.02,ncol=1,columnspacing=0.4)

ax_1.set_xticks([], minor=False)
ax_1.get_yaxis().set_visible(False)
ax_2.set_xticks([], minor=False)
ax_2.get_yaxis().set_visible(False)
ax_3.set_xticks([], minor=False)
ax_3.get_yaxis().set_visible(False)
ax_4.set_xticks([], minor=False)
ax_4.get_yaxis().set_visible(False)


ax_1.set_xlabel('column1_front',fontsize=y_fontsize)
ax_2.set_xlabel('column1_back',fontsize=y_fontsize,labelpad=5)
ax_3.set_xlabel('column2_front',fontsize=y_fontsize,labelpad=5)
ax_4.set_xlabel('column2_back',fontsize=y_fontsize,labelpad=5)



for date_idx,date_i in enumerate(tqdm(data.index[::10][:],ncols = 100)):
    
    I = plt.imread(pic_of_closest_date('column1_front',date_i))
    ax_1.imshow(I)
    I = plt.imread(pic_of_closest_date('column1_back',date_i))
    ax_2.imshow(I)
    I = plt.imread(pic_of_closest_date('column2_front',date_i))
    ax_3.imshow(I)
    I = plt.imread(pic_of_closest_date('column2_back',date_i))
    ax_4.imshow(I)

    line_0 = ax_0.axvline(date_i,color="red")

    plt.savefig(current_path+'/output_figure/{}.jpg'.format(date_i))
    line_0.remove()
    




