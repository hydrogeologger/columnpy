import matplotlib
import glob, os
from datetime import datetime
import matplotlib.image as image
import matplotlib.pylab as pylab
import re
matplotlib.use('Agg')


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
    #idx_im, min_value = min(enumerate( abs(sp_sch[sch_name].df['date_time']-im_time)), key=operator.itemgetter(1))
    idx_im_rain=rain['rain']['df'].index.get_loc(im_time, method='nearest')
    idx_im_solar=solar['solar']['df'].index.get_loc(im_time, method='nearest')
    idx_im_a_e = prof['grange_a_electrochem_o2']['data'].df.index.get_loc(im_time, method='nearest')
    idx_im_a_lo = prof['grange_a_luo2']['data'].df.index.get_loc(im_time, method='nearest')
    idx_im_b_e = prof['grange_b_electrochem_o2']['data'].df.index.get_loc(im_time, method='nearest')
    idx_im_b_lo = prof['grange_b_luo2']['data'].df.index.get_loc(im_time, method='nearest')
    idx_im_d_e = prof['grange_d_electrochem_o2']['data'].df.index.get_loc(im_time, method='nearest')
    idx_im_d_lo = prof['grange_d_luo2']['data'].df.index.get_loc(im_time, method='nearest')
    idx_im_3_lo = prof['grange_3_luo2_dry']['data'].df.index.get_loc(im_time, method='nearest')
    idx_im_4_lo = prof['grange_4_luo2_dry']['data'].df.index.get_loc(im_time, method='nearest')
    idx_im_5_lo = prof['grange_5_luo2_dry']['data'].df.index.get_loc(im_time, method='nearest')      
    idx_im_3_temp = prof['grange_3_mo_su']['data'].df.index.get_loc(im_time, method='nearest')
    idx_im_4_temp = prof['grange_4_mo_su']['data'].df.index.get_loc(im_time, method='nearest')
    idx_im_5_temp = prof['grange_5_mo_su']['data'].df.index.get_loc(im_time, method='nearest')

    fig, ax = plt.subplots(8,2,sharex=True,figsize=(17,12))
    fig.subplots_adjust(hspace=.10)
    fig.subplots_adjust(left=0.08, right=0.99, top=0.97, bottom=0.05)
    fig.subplots_adjust(wspace=.2)
    ax2=ax[1][0].twinx()

    for i in ax:
        for j in i:
          for axis in ['top','bottom','left','right']:
            j.spines[axis].set_linewidth(2)
            j.set_axisbelow(True)
    #fig, ax_mo = plt.subplots(6,2,sharex=True,figsize=(13,9))
    #fig.subplots_adjust(hspace=.10)
    #fig.subplots_adjust(left=0.10, right=0.99, top=0.97, bottom=0.05)
    #fig.subplots_adjust(wspace=.2)

    #for i in ax:
    #    for j in i:
    #      for axis in ['top','bottom','left','right']:
    #        j.spines[axis].set_linewidth(2)    fig, ax = plt.subplots(6,2,sharex=True,figsize=(13,9))
   
    
    ax_temp_abd = plt.subplot2grid((2, 5), (1,3))
    ax_temp_abd.set_position([0.62,0.05,0.15,0.40])
    
    ax_temp_abd.set_xlabel('TEMPERATURE ($^\circ$C)')
    ax_temp_abd.set_ylabel('DEPTH FROM COLUMN TOP(m)')
    #ax_img.axis('off')
    ax_temp_345 = plt.subplot2grid((2, 5), (1,4))
    ax_temp_345.set_position([0.78,0.05,0.15,0.40])
 
    ax_temp_345.set_xlabel('TEMPERATURE ($^\circ$C)')
    ax_temp_345.set_ylabel('DEPTH FROM COLUMN TOP (m)')

    ax_temp_345.yaxis.tick_right()
    ax_temp_345.yaxis.set_label_position("right")

    ax_img = plt.subplot2grid((2, 2), (0,1))
    ax_img.set_position([0.53,0.49,0.50,0.50])
    #ax_img.set_position([0.53,0.25,0.45,0.48])
    ax_img.imshow(im)
    ax_img.axis('off')
    
    ##fig, ax = plt.subplots(6,sharex=True,figsize=(6,8))
    #mkevy=4

    #depth_y=np.array([8,13,20,28,38,48,70,85])
    depth_y_a=np.array([1.0,1.5,2.0,2.5,3.0,3.5,4.0])
    depth_y=np.array([0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0])
    #depth_y=np.array([0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0])
    
    #depth_y_temp=np.array([1,5,8,13,20,28,38,48,70,85])
    #depth_y_temp=np.array([0.5,2.0,2.5,3.0,3.5])
    
    temp_x_a_e=prof['grange_a_electrochem_o2']['data'].df.iloc[idx_im_a_e][['dtp6','dtp3','dtp2','dtp1','dtp0']].tolist()
    temp_x_b_e=prof['grange_b_electrochem_o2']['data'].df.iloc[idx_im_b_e][['dtp7','dtp6','dtp5','dtp3','dtp1','dtp0']].tolist()
    temp_x_d_e=prof['grange_d_electrochem_o2']['data'].df.iloc[idx_im_d_e][['dtp6','dtp4','dtp3','dtp2','dtp1','dtp0']].tolist()
    temp_x_a_lo=prof['grange_a_luo2']['data'].df.iloc[idx_im_a_lo][['wlut6','wlut5']].tolist()
    temp_x_b_lo=prof['grange_b_luo2']['data'].df.iloc[idx_im_b_lo][['dlut4','dlut2']].tolist()
    temp_x_d_lo=prof['grange_d_luo2']['data'].df.iloc[idx_im_d_lo][['dlut7','dlut5']].tolist()
    mergedlist_a= np.array([temp_x_a_e[0]]+temp_x_a_lo+temp_x_a_e[1:])
    mergedlist_b= np.array(temp_x_b_e[:3]+[temp_x_a_lo[0]]+[temp_x_a_e[3]]+[temp_x_a_lo[-1]]+temp_x_b_e[4:])
    mergedlist_d= np.array([temp_x_d_lo[0]]+[temp_x_d_e[0]]+[temp_x_a_lo[-1]]+temp_x_a_e[0:])
    mask_a = np.isfinite(mergedlist_a)
    mask_b = np.isfinite(mergedlist_b)
    mask_d = np.isfinite(mergedlist_d)

    temp_x_3=prof['grange_3_mo_su']['data'].df.iloc[idx_im_3_temp][['tmp7']].tolist()
    temp_x_4=prof['grange_4_mo_su']['data'].df.iloc[idx_im_4_temp][['tmp7']].tolist()
    temp_x_5=prof['grange_5_mo_su']['data'].df.iloc[idx_im_5_temp][['tmp7']].tolist()          
    temp_x_3_lo=prof['grange_3_luo2_dry']['data'].df.iloc[idx_im_3_lo][['dlut6','dlut5','dlut4','dlut3','dlut2','dlut1','dlut0']].tolist()
    temp_x_4_lo=prof['grange_4_luo2_dry']['data'].df.iloc[idx_im_4_lo][['dlut6','dlut5','dlut4','dlut3','dlut2','dlut1','dlut0']].tolist()
    temp_x_5_lo=prof['grange_5_luo2_dry']['data'].df.iloc[idx_im_5_lo][['dlut6','dlut5','dlut4','dlut3','dlut2','dlut1','dlut0']].tolist()
    mergedlist_3=np.array(temp_x_3+temp_x_3_lo)
    mergedlist_4=np.array(temp_x_4+temp_x_4_lo)
    mergedlist_5=np.array(temp_x_5+temp_x_5_lo)
    mask_3 = np.isfinite(mergedlist_3)
    mask_4 = np.isfinite(mergedlist_4)
    mask_5 = np.isfinite(mergedlist_5)

    ax_temp_abd.plot(mergedlist_a[mask_a],depth_y_a[mask_a],'-',color='darkblue',label='Column_1')
    ax_temp_abd.plot(mergedlist_b[mask_b],depth_y[mask_b],'-',color='lightblue',label='Column_2')
    ax_temp_abd.plot(mergedlist_d[mask_d],depth_y[mask_d],'-',color='cyan',label='Column_3')
    ax_temp_abd.set_ylim([4.5,0.2])
    ax_temp_abd.set_xlim([-2,31])
    ax_temp_abd.xaxis.set_major_locator(plt.MaxNLocator(5))
   
    ax_temp_345.plot(mergedlist_5[mask_5],depth_y[mask_5],'-',color='maroon',label='Column_4') 
    ax_temp_345.plot(mergedlist_3[mask_3],depth_y[mask_3],'-',color='gold',label='Column_5')
    ax_temp_345.plot(mergedlist_4[mask_4],depth_y[mask_4],'-',color='peru',label='Column_6')
    ax_temp_345.set_ylim([4.5,0.2])
    ax_temp_345.set_xlim([-2,31])
    ax_temp_345.xaxis.set_major_locator(plt.MaxNLocator(5))


    sp=solar['solar']['df']  
    ax[0][0].bar(sp[:idx_im_solar+1].index, sp['Daily global solar exposure (KWh/m*m)'][:idx_im_solar+1],color='maroon',edgecolor='maroon')

    sp=rain['rain']['df']
    ax[1][0].bar(sp[:idx_im_rain+1].index, sp['Rainfall amount (millimetres)'][:idx_im_rain+1],color='royalblue',edgecolor='royalblue')
    ax2.plot(sp[:idx_im_rain+1].index, sp['rain_cumsum'][:idx_im_rain+1],color='darkblue')
    
    
    #sch_name='savage_river_oxygen'
    sp=prof['grange_a_electrochem_o2']['data'].df#[::48]
    sp_lo=prof['grange_a_luo2']['data'].df#[::48]
    mark_every=128
    iv=1
    ax[2][0].plot(   sp[:idx_im_a_e+1].index,      sp.dtp6[:idx_im_a_e+1],'-',color='royalblue',markevery=mark_every,markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='0.5m',ms=12)
    ax[2][0].plot(sp_lo[:idx_im_a_lo+1].index,    sp_lo.wlut6[:idx_im_a_lo+1],'-',color='lightblue',markevery=mark_every,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='b',label='1.0m',ms=12)
    ax[2][0].plot(sp_lo[:idx_im_a_lo+1].index,    sp_lo.wlut5[:idx_im_a_lo+1],'-',color='limegreen',markevery=mark_every,markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='1.5m',ms=12)
    ax[2][0].plot(   sp[:idx_im_a_e+1].index,      sp.dtp3[:idx_im_a_e+1],'-',color='olive'    ,markevery=mark_every,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='2.0m',ms=12)
    ax[2][0].plot(   sp[:idx_im_a_e+1].index,      sp.dtp2[:idx_im_a_e+1],'-',color='gold'     ,markevery=mark_every,markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='2.5m',ms=12)
    ax[2][0].plot(   sp[:idx_im_a_e+1].index,      sp.dtp1[:idx_im_a_e+1],'-',color='peru'     ,markevery=mark_every,markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='3.0m',ms=12)
    ax[2][0].plot(   sp[:idx_im_a_e+1].index,      sp.dtp0[:idx_im_a_e+1],'-',color='maroon'   ,markevery=mark_every,markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='3.5m',ms=12)
   
    sp=prof['grange_b_electrochem_o2']['data'].df
    sp_lo=prof['grange_b_luo2']['data'].df
    mark_every=24
    ax[3][0].plot(sp[:idx_im_b_e+1].index, sp.dtp7[:idx_im_b_e+1],'-',color='darkblue',markersize=ms+3,markeredgewidth=mew, markeredgecolor='m',label='0.5m',ms=12,markevery=mark_every,fillstyle='full')
    ax[3][0].plot(sp[:idx_im_b_e+1].index, sp.dtp6[:idx_im_b_e+1],'-',color='royalblue',markersize=ms+3,markeredgewidth=mew, markeredgecolor='m',label='1.0m',ms=12,markevery=mark_every,fillstyle='full')
    ax[3][0].plot(sp[:idx_im_b_e+1].index, sp.dtp5[:idx_im_b_e+1],'-',color='lightblue',markersize=ms,markeredgewidth=mew, markeredgecolor='b',label='1.5m',ms=12,markevery=mark_every,fillstyle='full')
    ax[3][0].plot(sp_lo[:idx_im_b_lo+1].index, sp_lo.dlut4[:idx_im_b_lo+1],'-',color='limegreen',markersize=ms-3,markeredgewidth=mew, markeredgecolor='g',label='2.0m',ms=12,markevery=mark_every,fillstyle='full')
    ax[3][0].plot(sp[:idx_im_b_e+1].index, sp.dtp3[:idx_im_b_e+1],'-',color='olive',markersize=ms,markeredgewidth=mew, markeredgecolor='r',label='2.5m',ms=12,markevery=mark_every,fillstyle='full')
    ax[3][0].plot(sp_lo[:idx_im_b_lo+1].index, sp_lo.dlut2[:idx_im_b_lo+1],'-',color='gold',markersize=ms+3,markeredgewidth=mew, markeredgecolor='brown',label='3.0m',ms=12,markevery=mark_every,fillstyle='full')
    ax[3][0].plot(sp[:idx_im_b_e+1].index, sp.dtp1[:idx_im_b_e+1],'-',color='peru',markersize=ms-3,markeredgewidth=mew, markeredgecolor='k',label='3.5m',ms=12,markevery=mark_every,fillstyle='full')
    ax[3][0].plot(sp[:idx_im_b_e+1].index, sp.dtp0[:idx_im_b_e+1],'-',color='maroon',markersize=ms-3,markeredgewidth=mew, markeredgecolor='c',label='4.0m',ms=12,markevery=mark_every,fillstyle='full')

    sp=prof['grange_d_electrochem_o2']['data'].df
    sp_lo=prof['grange_d_luo2']['data'].df
    mark_every=48    
    ax[4][0].plot(sp_lo[:idx_im_d_lo+1].index, sp_lo.dlut7[:idx_im_d_lo+1],'-',color='darkblue',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='0.5m',ms=12)
    ax[4][0].plot(sp[:idx_im_d_e+1].index, sp.dtp6[:idx_im_d_e+1],'-',color='royalblue',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='1.0m',ms=12)
    ax[4][0].plot(sp_lo[:idx_im_d_lo+1].index, sp_lo.dlut5[:idx_im_d_lo+1],'-',color='lightblue',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='b',label='1.5m',ms=12)
    ax[4][0].plot(sp[:idx_im_d_e+1].index, sp.dtp4[:idx_im_d_e+1],'-',color='limegreen',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='2.0m',ms=12)
    ax[4][0].plot(sp[:idx_im_d_e+1].index, sp.dtp3[:idx_im_d_e+1],'-',color='olive',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='2.5m',ms=12)
    ax[4][0].plot(sp[:idx_im_d_e+1].index, sp.dtp2[:idx_im_d_e+1],'-',color='gold',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='3.0m',ms=12)
    ax[4][0].plot(sp[:idx_im_d_e+1].index, sp.dtp1[:idx_im_d_e+1],'-',color='peru',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='3.5m',ms=12)
    ax[4][0].plot(sp[:idx_im_d_e+1].index, sp.dtp0[:idx_im_d_e+1],'-',color='maroon',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='4.0m',ms=12)

    sp_dlo=prof['grange_5_luo2_dry']['data'].df
    sp_moi=prof['grange_5_mo_su']['data'].df
    mark_every=24
    ax[5][0].plot(sp_moi[:idx_im_5_temp+1].index, sp_moi.tmp7[:idx_im_5_temp+1],'-',color='darkblue',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='0.5m',markevery=mark_every,ms=12)
    ax[5][0].plot(sp_dlo[:idx_im_5_lo+1].index, sp_dlo.dlut6[:idx_im_5_lo+1],'-',color='royalblue',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='1.0m',markevery=mark_every,ms=12)
    ax[5][0].plot(sp_dlo[:idx_im_5_lo+1].index, sp_dlo.dlut5[:idx_im_5_lo+1],'-',color='lightblue',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='b',label='1.5m',markevery=mark_every,ms=12)
    ax[5][0].plot(sp_dlo[:idx_im_5_lo+1].index, sp_dlo.dlut4[:idx_im_5_lo+1],'-',color='limegreen',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='2.0m',markevery=mark_every,ms=12)
    ax[5][0].plot(sp_dlo[:idx_im_5_lo+1].index, sp_dlo.dlut3[:idx_im_5_lo+1],'-',color='olive',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='2.5m',markevery=mark_every,ms=12)
    ax[5][0].plot(sp_dlo[:idx_im_5_lo+1].index, sp_dlo.dlut2[:idx_im_5_lo+1],'-',color='gold',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='3.0m',markevery=mark_every,ms=12)
    ax[5][0].plot(sp_dlo[:idx_im_5_lo+1].index, sp_dlo.dlut1[:idx_im_5_lo+1],'-',color='peru',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='3.5m',ms=12,markevery=mark_every)
    ax[5][0].plot(sp_dlo[:idx_im_5_lo+1].index, sp_dlo.dlut0[:idx_im_5_lo+1],'-',color='maroon',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='4.0m',ms=12,markevery=mark_every)
  
  
    sp_dlo=prof['grange_3_luo2_dry']['data'].df
    sp_moi=prof['grange_3_mo_su']['data'].df
    mark_every=24
    ax[6][0].plot(sp_moi[:idx_im_3_temp+1].index, sp_moi.tmp7[:idx_im_3_temp+1],'-',color='darkblue',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='0.5m',markevery=mark_every,ms=12)
    ax[6][0].plot(sp_dlo[:idx_im_3_lo+1].index, sp_dlo.dlut6[:idx_im_3_lo+1],'-',color='royalblue',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='1.0m',markevery=mark_every,ms=12)
    ax[6][0].plot(sp_dlo[:idx_im_3_lo+1].index, sp_dlo.dlut5[:idx_im_3_lo+1],'-',color='lightblue',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='b',label='1.5m',markevery=mark_every,ms=12)
    ax[6][0].plot(sp_dlo[:idx_im_3_lo+1].index, sp_dlo.dlut4[:idx_im_3_lo+1],'-',color='limegreen',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='2.0m',markevery=mark_every,ms=12)
    ax[6][0].plot(sp_dlo[:idx_im_3_lo+1].index, sp_dlo.dlut3[:idx_im_3_lo+1],'-',color='olive',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='2.5m',markevery=mark_every,ms=12)
    ax[6][0].plot(sp_dlo[:idx_im_3_lo+1].index, sp_dlo.dlut2[:idx_im_3_lo+1],'-',color='gold',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='3.0m',markevery=mark_every,ms=12)
    ax[6][0].plot(sp_dlo[:idx_im_3_lo+1].index, sp_dlo.dlut1[:idx_im_3_lo+1],'-',color='peru',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='3.5m',ms=12,markevery=mark_every)
    ax[6][0].plot(sp_dlo[:idx_im_3_lo+1].index, sp_dlo.dlut0[:idx_im_3_lo+1],'-',color='maroon',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='4.0m',markevery=mark_every)

    #sp_wlo=prof['grange_4_luo2_wet']['data'].df
    sp_dlo=prof['grange_4_luo2_dry']['data'].df
    sp_moi=prof['grange_4_mo_su']['data'].df
    mark_every=24
    ax[7][0].plot(sp_moi[:idx_im_4_temp+1].index, sp_moi.tmp7[:idx_im_4_temp+1],'-',color='darkblue',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='0.5m',markevery=mark_every,ms=12)
    ax[7][0].plot(sp_dlo[:idx_im_4_lo+1].index, sp_dlo.dlut6[:idx_im_4_lo+1],'-',color='royalblue',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='1.0m',markevery=mark_every,ms=12)
    ax[7][0].plot(sp_dlo[:idx_im_4_lo+1].index, sp_dlo.dlut5[:idx_im_4_lo+1],'-',color='lightblue',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='b',label='1.5m',markevery=mark_every,ms=12)
    ax[7][0].plot(sp_dlo[:idx_im_4_lo+1].index, sp_dlo.dlut4[:idx_im_4_lo+1],'-',color='limegreen',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='2.0m',markevery=mark_every,ms=12)
    ax[7][0].plot(sp_dlo[:idx_im_4_lo+1].index, sp_dlo.dlut3[:idx_im_4_lo+1],'-',color='olive',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='2.5m',markevery=mark_every,ms=12)
    ax[7][0].plot(sp_dlo[:idx_im_4_lo+1].index, sp_dlo.dlut2[:idx_im_4_lo+1],'-',color='gold',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='3.0m',markevery=mark_every,ms=12)
    ax[7][0].plot(sp_dlo[:idx_im_4_lo+1].index, sp_dlo.dlut1[:idx_im_4_lo+1],'-',color='peru',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='3.5m',ms=12,markevery=mark_every)
    ax[7][0].plot(sp_dlo[:idx_im_4_lo+1].index, sp_dlo.dlut0[:idx_im_4_lo+1],'-',color='maroon',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='4.0m',markevery=mark_every)
   
 
    
    #ax[0].set_xticklabels([])
    #ax[1].set_xticklabels([])
    #ax[2].set_xticklabels([])
    #ax[3].set_xticklabels([])
    #ax[4].set_xticklabels([])
    #ax[5].set_xticklabels([])
    #xlim=[sp_sch[sch_name].df.time_days[0],sp_sch[sch_name].df.time_days[len(sp_sch[sch_name].df)-1]]
    #xlim=[prof['grange_4_luo2_dry']['data'].df.index[0],prof['grange_4_luo2_dry']['data'].df.index[-1]]
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
    ax[2][0].set_ylabel('TEMPERATURE\nCOLUMN 1\n A TYPE ($^\circ$C)', fontsize=y_fontsize, labelpad=10)
    ax[3][0].set_ylabel('TEMPERATURE\nCOLUMN 2\n B TYPE ($^\circ$C)', fontsize=y_fontsize, labelpad=10)
    ax[4][0].set_ylabel('TEMPERATURE\nCOLUMN 3\n D TYPE ($^\circ$C)', fontsize=y_fontsize, labelpad=10)
    ax[5][0].set_ylabel('TEMPERATURE\nCOLUMN 4\n D+A TYPE ($^\circ$C)', fontsize=y_fontsize, labelpad=10)
    ax[6][0].set_ylabel('TEMPERATURE\nCOLUMN 5\n D+B TYPE ($^\circ$C)', fontsize=y_fontsize, labelpad=10)
    ax[7][0].set_ylabel('TEMPERATURE\nCOLUMN 6\n A+B+D ($^\circ$C)', fontsize=y_fontsize, labelpad=10)
    
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
    ax[5][0].legend(bbox_to_anchor=(1.07, 0.06 ), title="SOIL\nDEPTHS\n(C,D,E\nF,G,H)",loc='center', borderaxespad=0.,fontsize=10,handletextpad=0.23,labelspacing=0.22,ncol=1,columnspacing=0.4) 
    ax_temp_abd.legend(bbox_to_anchor=(0.99, 0.009), loc='lower right' , borderaxespad=0.,fontsize=10,handletextpad=0.03,labelspacing=0.02,ncol=1,columnspacing=0.4)
    ax_temp_345.legend(bbox_to_anchor=(0.99, 0.009), loc='lower right' , borderaxespad=0.,fontsize=10,handletextpad=0.03,labelspacing=0.02,ncol=1,columnspacing=0.4)

    ax[0][0].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[1][0].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[2][0].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[3][0].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[4][0].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[5][0].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[6][0].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[7][0].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax_temp_abd.grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax_temp_345.grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')

    ax[0][0].set_title('(A)',x=0.04,y=0.8,fontweight='bold')
    ax[1][0].set_title('(B)',x=0.04,y=0.8,fontweight='bold')
    ax[2][0].set_title('(C)',x=0.04,y=0.8,fontweight='bold')
    ax[3][0].set_title('(D)',x=0.04,y=0.8,fontweight='bold')
    ax[4][0].set_title('(E)',x=0.04,y=0.8,fontweight='bold')
    ax[5][0].set_title('(F)',x=0.04,y=0.8,fontweight='bold')
    ax[6][0].set_title('(G)',x=0.04,y=0.8,fontweight='bold')
    ax[7][0].set_title('(H)',x=0.04,y=0.8,fontweight='bold')
    ax_temp_abd.set_title('(I)',x=0.08,y=0.93,fontweight='bold')
    ax_temp_345.set_title('(J)',x=0.08,y=0.93,fontweight='bold')
    
 
    ax[7][0].xaxis.set_major_formatter(mdates.DateFormatter('%b')) 
    ax[7][0].set_xlabel('DATE', fontsize=y_fontsize,labelpad=3)
    ax[0][0].set_ylim([-0.5,10])
    ax[1][0].set_ylim([-2,60])
    ax2.set_ylim([-10,2500])
    ax[2][0].set_ylim([-2,31])
    ax[3][0].set_ylim([-2,31])
    ax[4][0].set_ylim([-2,31])
    ax[5][0].set_ylim([-2,31])
    ax[6][0].set_ylim([-2,31])
    ax[7][0].set_ylim([-2,31])  

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
    output_name = 'figure/plot_video_temperature/000'+str(ii)+'.png'
    fig.savefig(output_name, format='png', dpi=100)
    plt.close()
