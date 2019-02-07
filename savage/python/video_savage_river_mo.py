import matplotlib
import glob, os
from datetime import datetime
import matplotlib.image as image
import matplotlib.pylab as pylab
import re
matplotlib.use('Agg')
import pandas as pd

#params = {'legend.fontsize': 4,
#          'figure.figsize': (10, 5),
#         'axes.labelsize': 15,
#         'axes.titlesize':'50',
#         'xtick.labelsize':'15',
#         'ytick.labelsize':'15',
#         'font.weight':'bold',
#         'font.sans-serif':'Arial',
#         'axes.labelweight':'bold',
#         'lines.linewidth':2,
#         'title.fontweight':'bold'}

#         'axes.grid':'linewidth=grid_width,color = '0.5''}
#         'linewidth':lw,'markers.size':ms,'markers.edgewidth':mew}
#pylab.rcParams.update(params)

lw=2
ms=2
mew=3
grid_width=2
y_fontsize=11

#from PIL import Image
#def get_date_taken(path):
#    from datetime import datetime
#    return datetime.strptime(Image.open(path)._getexif()[36867],'%Y:%m:%d %H:%M:%S')

#path_im_nobact=os.environ['nobact_exp1']
#files_nobact = filter(os.path.isfile, glob.glob(path_im_nobact + "*.jpg"))
#files_nobact.sort(key=lambda x: get_date_taken(x))
#file_name_nobact=[i.split('/')[-1] for i in files_nobact]
#photo_taken_time_nobact=[get_date_taken(i) for i in files_nobact]


#path_im_bact='/home/cmzhang/hdrivexm/bact_first/'
#path_im_bact=os.environ['bact_exp1']
path_im='/media/sf_H_DRIVE/research_assistant/savage_river/grange_photo/'
files = filter(os.path.isfile, glob.glob(path_im + "*.png"))
#files.sort(key=lambda x: get_date_taken(x))
file_name=[i.split('/')[-1] for i in files]
file_name.sort()
photo_taken_time=[i[15:-4] for i in file_name]
date=[datetime.strptime(x,'%Y-%m-%d_%H%M') for x in photo_taken_time]


#for ii in file_name_bact[:1]:
#for ii in file_name_bact:

#for ii in file_name[::1]:
   
    #im=image.imread(path_im+ii)
for ii in range(len(date)):
    im_path = path_im+file_name[ii]
    im=image.imread(im_path)
    im_time=date[ii]
    idx_im_rain=rain['rain']['df'].index.get_loc(im_time, method='nearest')
    idx_im_solar=solar['solar']['df'].index.get_loc(im_time, method='nearest')
    #idx_im, min_value = min(enumerate( abs(sp_sch[sch_name].df['date_time']-im_time)), key=operator.itemgetter(1))
    #idx_im_a = prof['grange_a_electrochem_o2']['data'].df.index.get_loc(im_time, method='nearest')
    #idx_im_b = prof['grange_b_electrochem_o2']['data'].df.index.get_loc(im_time, method='nearest')
    #idx_im_d = prof['grange_d_electrochem_o2']['data'].df.index.get_loc(im_time, method='nearest')
    #idx_im_3 = prof['grange_3_luo2_dry']['data'].df.index.get_loc(im_time, method='nearest')
    #idx_im_4 = prof['grange_4_luo2_dry']['data'].df.index.get_loc(im_time, method='nearest')
    #idx_im_5 = prof['grange_5_luo2_dry']['data'].df.index.get_loc(im_time, method='nearest')  
    idx_im_a_mo = prof['grange_a_moisture_suction']['data'].df.index.get_loc(im_time, method='nearest')
    idx_im_b_mo = prof['grange_b_moisture_suction']['data'].df.index.get_loc(im_time, method='nearest')
    idx_im_d_mo = prof['grange_d_type_moisture_suction']['data'].df.index.get_loc(im_time, method='nearest')
    idx_im_3_mo = prof['grange_3_mo_su']['data'].df.index.get_loc(im_time, method='nearest')
    idx_im_4_mo = prof['grange_4_mo_su']['data'].df.index.get_loc(im_time, method='nearest')
    idx_im_5_mo = prof['grange_5_mo_su']['data'].df.index.get_loc(im_time, method='nearest')

    fig, ax = plt.subplots(8,2,sharex=True,figsize=(17,12))
    fig.subplots_adjust(hspace=.10)
    fig.subplots_adjust(left=0.08, right=0.99, top=0.97, bottom=0.05)
    fig.subplots_adjust(wspace=.2)
    ax2=ax[1][0].twinx()

    for i in ax:
        for j in i:
          for axis in ['top','bottom','left','right']:
            j.spines[axis].set_linewidth(2)

    #fig, ax_mo = plt.subplots(6,2,sharex=True,figsize=(13,9))
    #fig.subplots_adjust(hspace=.10)
    #fig.subplots_adjust(left=0.10, right=0.99, top=0.97, bottom=0.05)
    #fig.subplots_adjust(wspace=.2)

    #for i in ax:
    #    for j in i:
    #      for axis in ['top','bottom','left','right']:
    #        j.spines[axis].set_linewidth(2)    fig, ax = plt.subplots(6,2,sharex=True,figsize=(13,9))
   
    
    ax_mo_abd = plt.subplot2grid((2, 5), (1,3))
    ax_mo_abd.set_position([0.62,0.07,0.15,0.40])
    
    ax_mo_abd.set_xlabel('VOLUMETRIC\nWATER CONTENT (-)')
    ax_mo_abd.set_ylabel('DEPTH FROM COLUMN TOP(m)')
    #ax_img.axis('off')
    ax_mo_345 = plt.subplot2grid((2, 5), (1,4))
    ax_mo_345.set_position([0.78,0.07,0.15,0.40])
 
    ax_mo_345.set_xlabel('VOLUMETRIC\nWATER CONTENT (-)')
    ax_mo_345.set_ylabel('DEPTH FROM COLUMN TOP (m)')
    ax_mo_345.yaxis.tick_right()
    ax_mo_345.yaxis.set_label_position("right")
    ax_img = plt.subplot2grid((2, 2), (0,1))
    ax_img.set_position([0.53,0.49,0.50,0.50])
      
     #ax_img.set_position([0.53,0.25,0.45,0.48])
    ax_img.imshow(im)
    ax_img.axis('off')
    
    ##fig, ax = plt.subplots(6,sharex=True,figsize=(6,8))
    #mkevy=4

    #depth_y=np.array([8,13,20,28,38,48,70,85])
    depth_y=np.array([0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0])
    
    #depth_y_temp=np.array([1,5,8,13,20,28,38,48,70,85])
    depth_y_temp=np.array([0.5,2.0,2.5,3.0,3.5])
    
    mo_x_a=prof['grange_a_moisture_suction']['data'].df.iloc[idx_im_a_mo][['mo7_c','mo6_c','mo5_c','mo4_c','mo3_c','mo2_c','mo1_c','mo0_c']].tolist()
    mo_x_b=prof['grange_b_moisture_suction']['data'].df.iloc[idx_im_b_mo][['mo7_c','mo6_c','mo5_c','mo4_c','mo3_c','mo2_c','mo1_c','mo0_c']].tolist()
    mo_x_d=prof['grange_d_type_moisture_suction']['data'].df.iloc[idx_im_d_mo][['mo7_c','mo6_c','mo5_c','mo4_c','mo3_c','mo2_c','mo1_c','mo0_c']].tolist()
    mo_x_3=prof['grange_3_mo_su']['data'].df.iloc[idx_im_3_mo][['mo7_c','mo6_c','mo5_c','mo4_c','mo3_c','mo2_c','mo1_c','mo0_c']].tolist()
    mo_x_4=prof['grange_4_mo_su']['data'].df.iloc[idx_im_4_mo][['mo7_c','mo6_c','mo5_c','mo4_c','mo3_c','mo2_c','mo1_c','mo0_c']].tolist()
    mo_x_5=prof['grange_5_mo_su']['data'].df.iloc[idx_im_5_mo][['mo7_c','mo6_c','mo5_c','mo4_c','mo3_c','mo2_c','mo1_c','mo0_c']].tolist()          

    ax_mo_abd.plot(mo_x_a,depth_y,'-',color='darkblue',label='Column_1')
    ax_mo_abd.plot(mo_x_b,depth_y,'-',color='lightblue',label='Column_2')
    ax_mo_abd.plot(mo_x_d,depth_y,'-',color='cyan',label='Column_3')
    ax_mo_abd.set_ylim([4.5,0.2])
    ax_mo_abd.set_xlim([-0.03,0.36])
    ax_mo_abd.xaxis.set_major_locator(plt.MaxNLocator(5)) 

    ax_mo_345.plot(mo_x_5,depth_y,'-',color='maroon',label='Column_4') 
    ax_mo_345.plot(mo_x_3,depth_y,'-',color='gold',label='Column_5')
    ax_mo_345.plot(mo_x_4,depth_y,'-',color='peru',label='Column_6')
    ax_mo_345.set_ylim([4.5,0.2])
    ax_mo_345.set_xlim([-0.03,0.36])
    ax_mo_345.xaxis.set_major_locator(plt.MaxNLocator(5))
    #ax_temp.plot(temp_x_a,depth_y_temp,'-',color='maroon')
    #ax_temp.set_ylim([4.8,0])
    #ax_temp.set_xlim([0,50])

    #ax_mo.set_position([0.63,0.09,0.15,0.45])
    #ax_temp.set_position([0.84,0.09,0.15,0.45])

    #fig = plt.figure(figsize=(16,9))
    #ax = [[] for i in range
    #ax[0] = plt.subplot2grid((6, 2), (0, 0), colspan=1)
    #ax[1] = plt.subplot2grid((6, 2), (1, 0), colspan=1)
    #ax[2] = plt.subplot2grid((6, 2), (2, 0), colspan=1)
    #ax[3] = plt.subplot2grid((6, 2), (3, 0), colspan=1)
    #ax[4] = plt.subplot2grid((6, 2), (4, 0), colspan=1)
    #ax[5] = plt.subplot2grid((6, 2), (5, 0), colspan=1)
    #ax[6] = plt.subplot2grid((6, 2), (6, 0), colspan=1)
    #fig.subplots_adjust(hspace=.20)
    #fig.subplots_adjust(left=0.07, right=0.93, top=0.97, bottom=0.07)
    #ax_img.set_position([0.47,0.01,0.53,0.97])
    
    
    #fig, ax = plt.subplots(6,sharex=True,figsize=(6,8))
    #jfig.subplots_adjust(hspace=.15)
    
    #for axis in ['top','bottom','left','right']:
    #    ax_mo.spines[axis].set_linewidth(2)
    #    ax_temp.spines[axis].set_linewidth(2)

    #for i in ax:
    #    for j in i:
    #      for axis in ['top','bottom','left','right']:
    #        j.spines[axis].set_linewidth(2)
 
    #for i in ax:
    #      for axis in ['top','bottom','left','right']:
    #        i.spines[axis].set_linewidth(2)

    #ax_img = plt.subplot2grid((1, 3), (0,2))
    #ax_img.set_position([0.53,0.39,0.45,0.58])
    #ax_img = [[] for i in range(6)]
    #ax_img_nobact = plt.subplot2grid((3, 3), (0,1))
    #ax_img_nobact.set_position([0.03,0.39,0.45,0.58])
    sp=solar['solar']['df']
    ax[0][0].bar(sp[:idx_im_solar+1].index, sp['Daily global solar exposure (KWh/m*m)'][:idx_im_solar+1],color='maroon',edgecolor='maroon')
    
    sp=rain['rain']['df']
    
    ax[1][0].bar(sp[:idx_im_rain+1].index, sp['Rainfall amount (millimetres)'][:idx_im_rain+1],color='royalblue',edgecolor='royalblue')
    ax2.plot(sp[:idx_im_rain+1].index, sp['rain_cumsum'][:idx_im_rain+1],color='darkblue')
    
    #sch_name='savage_river_oxygen'
    sp=prof['grange_a_moisture_suction']['data'].df#[::48]
    #sp_lo=prof['grange_a_luo2']['data'].df#[::48]
    mark_every=128
    iv=50
    ax[2][0].plot(sp[:idx_im_a_mo+1].index[::iv],sp.mo7_c[:idx_im_a_mo+1][::iv],'-',color='darkblue',markevery=mark_every,markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='0.5m',ms=12)
    ax[2][0].plot(sp[:idx_im_a_mo+1].index[::iv],sp.mo6_c[:idx_im_a_mo+1][::iv],'-',color='royalblue',markevery=mark_every,markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='1.0m',ms=12)
    ax[2][0].plot(sp[:idx_im_a_mo+1].index[::iv],sp.mo5_c[:idx_im_a_mo+1][::iv],'-',color='lightblue',markevery=mark_every,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='b',label='1.5m',ms=12)
    ax[2][0].plot(sp[:idx_im_a_mo+1].index[::iv],sp.mo4_c[:idx_im_a_mo+1][::iv],'-',color='limegreen',markevery=mark_every,markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='2.0m',ms=12)
    ax[2][0].plot(sp[:idx_im_a_mo+1].index[::iv],sp.mo3_c[:idx_im_a_mo+1][::iv],'-',color='olive'    ,markevery=mark_every,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='2.5m',ms=12)
    ax[2][0].plot(sp[:idx_im_a_mo+1].index[::iv],sp.mo2_c[:idx_im_a_mo+1][::iv],'-',color='gold'     ,markevery=mark_every,markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='3.0m',ms=12)
    ax[2][0].plot(sp[:idx_im_a_mo+1].index[::iv],sp.mo1_c[:idx_im_a_mo+1][::iv],'-',color='peru'     ,markevery=mark_every,markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='3.5m',ms=12)
    ax[2][0].plot(sp[:idx_im_a_mo+1].index[::iv],sp.mo0_c[:idx_im_a_mo+1][::iv],'-',color='maroon'   ,markevery=mark_every,markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='4.0m',ms=12)
    
    sp=prof['grange_b_moisture_suction']['data'].df
    #sp_lo=prof['grange_b_luo2']['data'].df
    mark_every=24
    iv=50
    ax[3][0].plot(sp[:idx_im_b_mo+1].index[::iv], sp.mo7_c[:idx_im_b_mo+1][::iv],'-',color='darkblue',markersize=ms+3,markeredgewidth=mew, markeredgecolor='m',label='0.5m',ms=12,markevery=mark_every,fillstyle='full')
    ax[3][0].plot(sp[:idx_im_b_mo+1].index[::iv], sp.mo6_c[:idx_im_b_mo+1][::iv],'-',color='royalblue',markersize=ms+3,markeredgewidth=mew, markeredgecolor='m',label='1.0m',ms=12,markevery=mark_every,fillstyle='full')
    ax[3][0].plot(sp[:idx_im_b_mo+1].index[::iv], sp.mo5_c[:idx_im_b_mo+1][::iv],'-',color='lightblue',markersize=ms,markeredgewidth=mew, markeredgecolor='b',label='1.5m',ms=12,markevery=mark_every,fillstyle='full')
    ax[3][0].plot(sp[:idx_im_b_mo+1].index[::iv], sp.mo4_c[:idx_im_b_mo+1][::iv],'-',color='limegreen',markersize=ms-3,markeredgewidth=mew, markeredgecolor='g',label='2.0m',ms=12,markevery=mark_every,fillstyle='full')
    ax[3][0].plot(sp[:idx_im_b_mo+1].index[::iv], sp.mo3_c[:idx_im_b_mo+1][::iv],'-',color='olive',markersize=ms,markeredgewidth=mew, markeredgecolor='r',label='2.5m',ms=12,markevery=mark_every,fillstyle='full')
    ax[3][0].plot(sp[:idx_im_b_mo+1].index[::iv], sp.mo2_c[:idx_im_b_mo+1][::iv],'-',color='gold',markersize=ms+3,markeredgewidth=mew, markeredgecolor='brown',label='3.0m',ms=12,markevery=mark_every,fillstyle='full')
    ax[3][0].plot(sp[:idx_im_b_mo+1].index[::iv], sp.mo1_c[:idx_im_b_mo+1][::iv],'-',color='peru',markersize=ms-3,markeredgewidth=mew, markeredgecolor='k',label='3.5m',ms=12,markevery=mark_every,fillstyle='full')
    ax[3][0].plot(sp[:idx_im_b_mo+1].index[::iv], sp.mo0_c[:idx_im_b_mo+1][::iv],'-',color='maroon',markersize=ms-3,markeredgewidth=mew, markeredgecolor='c',label='4.0m',ms=12,markevery=mark_every,fillstyle='full')

    sp=prof['grange_d_type_moisture_suction']['data'].df
    #sp_lo=prof['grange_d_luo2']['data'].df
    mark_every=48   
    iv=50 
    ax[4][0].plot(sp[:idx_im_d_mo+1].index[::iv], sp.mo7_c[:idx_im_d_mo+1][::iv],'-',color='darkblue',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='0.5m',ms=12)
    ax[4][0].plot(sp[:idx_im_d_mo+1].index[::iv], sp.mo6_c[:idx_im_d_mo+1][::iv],'-',color='royalblue',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='1.0m',ms=12)
    ax[4][0].plot(sp[:idx_im_d_mo+1].index[::iv], sp.mo5_c[:idx_im_d_mo+1][::iv],'-',color='lightblue',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='b',label='1.5m',ms=12)
    ax[4][0].plot(sp[:idx_im_d_mo+1].index[::iv], sp.mo4_c[:idx_im_d_mo+1][::iv],'-',color='limegreen',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='2.0m',ms=12)
    ax[4][0].plot(sp[:idx_im_d_mo+1].index[::iv], sp.mo3_c[:idx_im_d_mo+1][::iv],'-',color='olive',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='2.5m',ms=12)
    ax[4][0].plot(sp[:idx_im_d_mo+1].index[::iv], sp.mo2_c[:idx_im_d_mo+1][::iv],'-',color='gold',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='3.0m',ms=12)
    ax[4][0].plot(sp[:idx_im_d_mo+1].index[::iv], sp.mo1_c[:idx_im_d_mo+1][::iv],'-',color='peru',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='3.5m',ms=12)
    ax[4][0].plot(sp[:idx_im_d_mo+1].index[::iv], sp.mo0_c[:idx_im_d_mo+1][::iv],'-',color='maroon',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='4.0m',ms=12)

    #sp_wlo=prof['grange_5_luo2_wet']['data'].df
    #sp_dlo=prof['grange_5_luo2_dry']['data'].df
    sp=prof['grange_5_mo_su']['data'].df
    mark_every=24
    iv=50
    ax[5][0].plot(sp[:idx_im_5_mo+1].index, sp.mo7_c[:idx_im_5_mo+1],'-',color='darkblue',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='0.5m',markevery=mark_every,ms=12)
    ax[5][0].plot(sp[:idx_im_5_mo+1].index, sp.mo6_c[:idx_im_5_mo+1],'-',color='royalblue',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='1.0m',markevery=mark_every,ms=12)
    ax[5][0].plot(sp[:idx_im_5_mo+1].index, sp.mo5_c[:idx_im_5_mo+1],'-',color='lightblue',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='b',label='1.5m',markevery=mark_every,ms=12)
    ax[5][0].plot(sp[:idx_im_5_mo+1].index, sp.mo4_c[:idx_im_5_mo+1],'-',color='limegreen',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='2.0m',markevery=mark_every,ms=12)
    ax[5][0].plot(sp[:idx_im_5_mo+1].index, sp.mo3_c[:idx_im_5_mo+1],'-',color='olive',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='2.5m',markevery=mark_every,ms=12)
    ax[5][0].plot(sp[:idx_im_5_mo+1].index, sp.mo2_c[:idx_im_5_mo+1],'-',color='gold',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='3.0m',markevery=mark_every,ms=12)
    ax[5][0].plot(sp[:idx_im_5_mo+1].index, sp.mo1_c[:idx_im_5_mo+1],'-',color='peru',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='3.5m',ms=12,markevery=mark_every)
    ax[5][0].plot(sp[:idx_im_5_mo+1].index, sp.mo0_c[:idx_im_5_mo+1],'-',color='maroon',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='4.0m',markevery=mark_every)
  
    #sp_wlo=prof['grange_3_luo2_wet']['data'].df
    #sp_dlo=prof['grange_3_luo2_dry']['data'].df
    sp=prof['grange_3_mo_su']['data'].df
    mark_every=24
    iv=50
    ax[6][0].plot(sp[:idx_im_3_mo+1].index[::iv], sp.mo7_c[:idx_im_3_mo+1][::iv],'-',color='darkblue',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='0.5m',markevery=mark_every,ms=12)
    ax[6][0].plot(sp[:idx_im_3_mo+1].index[::iv], sp.mo6_c[:idx_im_3_mo+1][::iv],'-',color='royalblue',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='1.0m',markevery=mark_every,ms=12)
    ax[6][0].plot(sp[:idx_im_3_mo+1].index[::iv], sp.mo5_c[:idx_im_3_mo+1][::iv],'-',color='lightblue',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='b',label='1.5m',markevery=mark_every,ms=12)
    ax[6][0].plot(sp[:idx_im_3_mo+1].index[::iv], sp.mo4_c[:idx_im_3_mo+1][::iv],'-',color='limegreen',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='2.0m',markevery=mark_every,ms=12)
    ax[6][0].plot(sp[:idx_im_3_mo+1].index[::iv], sp.mo3_c[:idx_im_3_mo+1][::iv],'-',color='olive',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='2.5m',markevery=mark_every,ms=12)
    ax[6][0].plot(sp[:idx_im_3_mo+1].index[::iv], sp.mo2_c[:idx_im_3_mo+1][::iv],'-',color='gold',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='3.0m',markevery=mark_every,ms=12)
    ax[6][0].plot(sp[:idx_im_3_mo+1].index[::iv], sp.mo1_c[:idx_im_3_mo+1][::iv],'-',color='peru',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='3.5m',ms=12,markevery=mark_every)
    ax[6][0].plot(sp[:idx_im_3_mo+1].index[::iv], sp.mo0_c[:idx_im_3_mo+1][::iv],'-',color='maroon',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='4.0m',markevery=mark_every)

    #sp_wlo=prof['grange_4_luo2_wet']['data'].df
    #sp_dlo=prof['grange_4_luo2_dry']['data'].df
    sp=prof['grange_4_mo_su']['data'].df
    mark_every=24
    iv=50
    ax[7][0].plot(sp[:idx_im_4_mo+1].index[::iv], sp.mo7_c[:idx_im_4_mo+1][::iv],'-',color='darkblue',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='0.5m',markevery=mark_every,ms=12)
    ax[7][0].plot(sp[:idx_im_4_mo+1].index[::iv], sp.mo6_c[:idx_im_4_mo+1][::iv],'-',color='royalblue',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='1.0m',markevery=mark_every,ms=12)
    ax[7][0].plot(sp[:idx_im_4_mo+1].index[::iv], sp.mo5_c[:idx_im_4_mo+1][::iv],'-',color='lightblue',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='b',label='1.5m',markevery=mark_every,ms=12)
    ax[7][0].plot(sp[:idx_im_4_mo+1].index[::iv], sp.mo4_c[:idx_im_4_mo+1][::iv],'-',color='limegreen',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='2.0m',markevery=mark_every,ms=12)
    ax[7][0].plot(sp[:idx_im_4_mo+1].index[::iv], sp.mo3_c[:idx_im_4_mo+1][::iv],'-',color='olive',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='2.5m',markevery=mark_every,ms=12)
    ax[7][0].plot(sp[:idx_im_4_mo+1].index[::iv], sp.mo2_c[:idx_im_4_mo+1][::iv],'-',color='gold',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='3.0m',markevery=mark_every,ms=12)
    ax[7][0].plot(sp[:idx_im_4_mo+1].index[::iv], sp.mo1_c[:idx_im_4_mo+1][::iv],'-',color='peru',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='3.5m',ms=12,markevery=mark_every)
    ax[7][0].plot(sp[:idx_im_4_mo+1].index[::iv], sp.mo0_c[:idx_im_4_mo+1][::iv],'-',color='maroon',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='4.0m',markevery=mark_every)
   
 
    
    #ax[0].set_xticklabels([])
    #ax[1].set_xticklabels([])
    #ax[2].set_xticklabels([])
    #ax[3].set_xticklabels([])
    #ax[4].set_xticklabels([])
    #ax[5].set_xticklabels([])
    #xlim=[sp_sch[sch_name].df.time_days[0],sp_sch[sch_name].df.time_days[len(sp_sch[sch_name].df)-1]]
    #xlim=[prof['grange_4_mo_su']['data'].df.index[0],prof['grange_4_mo_su']['data'].df.index[-1]]
    dates = pd.date_range(start='2017-12-22', periods=10, freq='D')
    
    
   # ax[0].set_xlim([sp_sch[sch_name].start_dt,sp_sch[sch_name].end_dt])
   # ax[1].set_xlim([sp_sch[sch_name].start_dt,sp_sch[sch_name].end_dt])
   # ax[2].set_xlim([sp_sch[sch_name].start_dt,sp_sch[sch_name].end_dt])
   # ax[3].set_xlim([sp_sch[sch_name].start_dt,sp_sch[sch_name].end_dt])
    #ax[4].set_xlim([sp_sch[sch_name].start_dt,sp_sch[sch_name].end_dt])
    #ax[5].set_xlim([sp_sch[sch_name].start_dt,sp_sch[sch_name].end_dt])
    #ax[0].set_xlim(xlim)
    #ax[1].set_xlim(xlim)
    #ax[2].set_xlim(xlim)
    #ax[3].set_xlim(xlim)
    #ax[4].set_xlim(xlim)
    ax[7][0].set_xlim(pd.Timestamp('2017-12-22'), pd.Timestamp('2019-01-01'))
    
    ax[0][0].set_ylabel('GLOBAL\nSOLAR EXPOSURE\n(KWh/m*m)', fontsize=y_fontsize, labelpad=10)
    ax[1][0].set_ylabel('RAINFALL\n(mm)', fontsize=y_fontsize, labelpad=10)
    ax2.set_ylabel('CUMULATIVE RAINFALL\n(mm)', fontsize=y_fontsize, labelpad=10)
    ax[2][0].set_ylabel('VOL.MOIST.\nCONTENT (-)\nCOLUMN 1\nTYPE A', fontsize=y_fontsize, labelpad=10)
    ax[3][0].set_ylabel('VOL.MOIST.\nCONTENT (-)\nCOLUMN 2\nTYPE B', fontsize=y_fontsize, labelpad=10)
    ax[4][0].set_ylabel('VOL.MOIST.\nCONTENT (-)\nCOLUMN 3\nTYPE D', fontsize=y_fontsize, labelpad=10)
    ax[5][0].set_ylabel('VOL.MOIST.\nCONTENT (-)\nCOLUMN 4\nTYPE A+D', fontsize=y_fontsize, labelpad=10)
    ax[6][0].set_ylabel('VOL.MOIST.\nCONTENT (-)\nCOLUMN 5\nTYPE D+B', fontsize=y_fontsize, labelpad=10)
    ax[7][0].set_ylabel('VOL.MOIST.\nCONTENT (-)\nCOLUMN 6\nTYPE A+B+D', fontsize=y_fontsize, labelpad=10)
    
    #ax[0].set_title('(A)',x=0.04,y=0.8,fontweight='bold')
    #ax[1].set_title('(B)',x=0.04,y=0.8,fontweight='bold')
    #ax[2].set_title('(C)',x=0.04,y=0.8,fontweight='bold')
    #ax[3].set_title('(D)',x=0.04,y=0.8,fontweight='bold')
    #ax[4].set_title('(E)',x=0.04,y=0.8,fontweight='bold')
    #ax[5].set_title('(F)',x=0.04,y=0.8,fontweight='bold')
    ax[0][0].set_axisbelow(True)
    ax[1][0].set_axisbelow(True)
    ax[2][0].set_axisbelow(True)
    ax[3][0].set_axisbelow(True)
    ax[4][0].set_axisbelow(True)
    ax[5][0].set_axisbelow(True)
    ax[6][0].set_axisbelow(True)
    ax[7][0].set_axisbelow(True)
    ax[5][0].legend(bbox_to_anchor=(1.07, 0.08 ), title="SOIL\nDEPTHS\n(C,D,E\nF,G,H)",loc='center', borderaxespad=0.,fontsize=10,handletextpad=0.23,labelspacing=0.22,ncol=1,columnspacing=0.4) 
    ax_mo_abd.legend(bbox_to_anchor=(0.993, 0.005), loc='lower right' , borderaxespad=0.,fontsize=10,handletextpad=0.03,labelspacing=0.02,ncol=1,columnspacing=0.4)
    ax_mo_345.legend(bbox_to_anchor=(0.993, 0.005), loc='lower right' , borderaxespad=0.,fontsize=10,handletextpad=0.03,labelspacing=0.02,ncol=1,columnspacing=0.4)

    ax[0][0].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[1][0].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[2][0].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[3][0].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[4][0].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[5][0].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[6][0].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[7][0].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax_mo_abd.grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax_mo_345.grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')

    ax[0][0].set_title('(A)',x=0.04,y=0.8,fontweight='bold')
    ax[1][0].set_title('(B)',x=0.04,y=0.8,fontweight='bold')
    ax[2][0].set_title('(C)',x=0.04,y=0.8,fontweight='bold')
    ax[3][0].set_title('(D)',x=0.04,y=0.8,fontweight='bold')
    ax[4][0].set_title('(E)',x=0.04,y=0.8,fontweight='bold')
    ax[5][0].set_title('(F)',x=0.04,y=0.8,fontweight='bold')
    ax[6][0].set_title('(G)',x=0.04,y=0.8,fontweight='bold')
    ax[7][0].set_title('(H)',x=0.04,y=0.8,fontweight='bold')
    ax_mo_abd.set_title('(I)',x=0.08,y=0.94,fontweight='bold')
    ax_mo_345.set_title('(J)',x=0.08,y=0.94,fontweight='bold')
    
 
    ax[7][0].xaxis.set_major_formatter(mdates.DateFormatter('%b')) 
    ax[7][0].set_xlabel('DATE', fontsize=y_fontsize,labelpad=3)
    ax[0][0].set_ylim([-0.5,10])
    ax[1][0].set_ylim([-2,60])
    ax2.set_ylim([-10,2500])
    ax[2][0].set_ylim([-0.03,0.36])
    ax[3][0].set_ylim([-0.03,0.36])
    ax[4][0].set_ylim([-0.03,0.36])
    ax[5][0].set_ylim([-0.03,0.36])
    ax[6][0].set_ylim([-0.03,0.36])
    ax[7][0].set_ylim([-0.03,0.36])  

    ax[1][0].tick_params('y', colors='royalblue')
    ax2.tick_params('y', colors='darkblue') 
    ax[0][0].yaxis.set_major_locator(plt.MaxNLocator(5))
    ax[1][0].yaxis.set_major_locator(plt.MaxNLocator(5))
    ax2.yaxis.set_major_locator(plt.MaxNLocator(5))
    ax[2][0].yaxis.set_major_locator(plt.MaxNLocator(5))
    ax[3][0].yaxis.set_major_locator(plt.MaxNLocator(5))
    ax[4][0].yaxis.set_major_locator(plt.MaxNLocator(5))
    ax[5][0].yaxis.set_major_locator(plt.MaxNLocator(5))
    ax[6][0].yaxis.set_major_locator(plt.MaxNLocator(5))
    ax[7][0].yaxis.set_major_locator(plt.MaxNLocator(5))
        

    #ax[5].set_xlabel('DATE', fontsize=y_fontsize,labelpad=3)
    #ax[1].xaxis.set_major_formatter(mdates.DateFormatter('%b/%d'))
    #ax[1].set_xlabel('TIME(DAYS)') 
    #ax[3].xaxis.set_major_formatter(mdates.DateFormatter('%b/%d'))
    #ax[3].set_xlabel('TIME(DAYS)')
    #ax[3].set_xlabel('TIME (DAYS)', fontsize=y_fontsize,labelpad=3)
    #plt.xticks(rotation=45)
    plt.show(block=False)
    #plt.show(block=True) 
    output_name = 'figure/plot_video_mo/000'+str(ii)+'.png'
    fig.savefig(output_name, format='png', dpi=100)
    plt.close()
