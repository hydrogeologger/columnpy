import matplotlib
import glob, os
from datetime import datetime
import matplotlib.image as image
import matplotlib.pylab as pylab
matplotlib.use('Agg')

lw=2
ms=2
mew=3
grid_width=2
y_fontsize=12


params = {'legend.fontsize': 4,
          'figure.figsize': (10, 5),
         'axes.labelsize': 15,
         'axes.titlesize':'50',
         'xtick.labelsize':'15',
         'ytick.labelsize':'15',
         'font.weight':'bold',
         'font.sans-serif':'Arial',
         'axes.labelweight':'bold',
         'lines.linewidth':2,
         'title.fontweight':'bold'}

#         'axes.grid':'linewidth=grid_width,color = '0.5''}
#         'linewidth':lw,'markers.size':ms,'markers.edgewidth':mew}
#pylab.rcParams.update(params)

#lw=2
#ms=2
#mew=3
#grid_width=2
#y_fontsize=12

from PIL import Image
def get_date_taken(path):
    from datetime import datetime
    return datetime.strptime(Image.open(path)._getexif()[36867],'%Y:%m:%d %H:%M:%S')

path_im_basin_ab='/home/osboxes/basin_test/basin_a_b/'
files_basin_ab = filter(os.path.isfile, glob.glob(path_im_basin_ab + "*.jpg"))
#files_nobact.sort(key=lambda x: get_date_taken(x))
files_name_basin_ab=[i.split('/')[-1] for i in files_basin_ab]
files_name_basin_ab.sort()
#photo_taken_time_nobact=[get_date_taken(i) for i in files_nobact]
photo_taken_time_basin_ab=[i[14:-4] for i in files_name_basin_ab]
date=[datetime.strptime(x,'%Y_%m_%d_%H_%M') for x in photo_taken_time_basin_ab]


#path_im_bact='/home/cmzhang/hdrivexm/bact_first/'
path_im_basin_c='/home/osboxes/basin_test/basin_c/'
files_basin_c = filter(os.path.isfile, glob.glob(path_im_basin_c + "*.jpg"))
#files_bact.sort(key=lambda x: get_date_taken(x))
files_name_basin_c=[i.split('/')[-1] for i in files_basin_c]
files_name_basin_c.sort()
#photo_taken_time_bact=[get_date_taken(i) for i in files_bact]
photo_taken_time_basin_c=[i[7:-4] for i in files_name_basin_c]
date=[datetime.strptime(x,'%Y_%m_%d_%H_%M') for x in photo_taken_time_basin_c]

#for ii in file_name_bact[:1]:
#for ii in file_name_bact:

#for ii in file_name_bact[::10]:
#for ii in file_name_bact[::30]:
#for ii in file_name_bact[-3:-1]:
for ii in range(len(date)):
    im_path_basin_ab = path_im_basin_ab+files_name_basin_ab[ii]
    im_basin_ab=image.imread(im_path_basin_ab)
    im_path_basin_c = path_im_basin_c+files_name_basin_c[ii]
    im_basin_c=image.imread(im_path_basin_c)    
    im_time=date[ii]
    idx_im, min_value = min(enumerate( abs(sp_sch[sch_name].df['date_time']-im_time)), key=operator.itemgetter(1))

    #im_path_basin_c = path_im_basin_c+files_name_basin_c[ii]
    #im_basin_c=image.imread(im_path_basin_c)
    #im_time_basin_c=date[ii]
    #idx_basin_c, min_value = min(enumerate( abs(sp_sch[sch_name].df['date_time']-im_time)), key=operator.itemgetter(1))

        
   # im=image.imread(path_im+ii)   
   # im_time=get_date_taken(path_im+ii)
   # idx_im, min_value = min(enumerate( abs(sp_sch[sch_name].df['date_time']-im_time)), key=operator.itemgetter(1)) 
   
#    im_bact=image.imread(path_im_bact+ii)
#    im_time_bact=get_date_taken(path_im_bact+ii)
#    idx_im, min_value = min(enumerate( abs(sp_sch[sch_name].df['date_time']-im_time_bact)), key=operator.itemgetter(1))
   

    #time_diff_nobact_bact=[ abs(i-im_time_bact) for i in photo_taken_time_bact]

    #idx_basin_c, min_value = min(enumerate( abs(np.array(photo_taken_time_basin_c)-im_time)), key=operator.itemgetter(1))
    #idx_basin_c, min_value = min(enumerate( abs(sp_sch[sch_name].df['date_time']-im_time)), key=operator.itemgetter(1))
    #im_basin_c=image.imread(path_im_basin_c+files_name_basin_c[idx_basin_c])
    #im1=image.imread(path_im1+ii)
    #im_time=get_date_taken(path_im1+ii)
    #idx_im, min_value = min(enumerate( abs(sp_sch[sch_name].df['date_time']-im_time)), key=operator.itemgetter(1))
 
    #fig, ax = plt.subplots(6,2,sharex=True,figsize=(16,9))
    fig = plt.figure(figsize=(18,9))
    ax = [[] for i in range(6)]
    ax[0] = plt.subplot2grid((5, 2), (3, 0), colspan=1)
    ax[1] = plt.subplot2grid((5, 2), (4, 0), colspan=1)
    ax[2] = plt.subplot2grid((5, 2), (3, 1), colspan=1)
    ax[3] = plt.subplot2grid((5, 2), (4, 1), colspan=1)
    #ax[4] = plt.subplot2grid((6, 2), (4, 0), colspan=1)
    #ax[5] = plt.subplot2grid((6, 2), (5, 0), colspan=1)

    fig.subplots_adjust(hspace=.20)
    fig.subplots_adjust(left=0.07, right=0.93, top=0.97, bottom=0.07)
    #ax_img.set_position([0.47,0.01,0.53,0.97])
    
    
    #fig, ax = plt.subplots(6,sharex=True,figsize=(6,8))
    #jfig.subplots_adjust(hspace=.15)
    
    
    #for i in ax:
    #      for axis in ['top','bottom','left','right']:
    #        i.spines[axis].set_linewidth(2)
    #ax_img = [[] for i in range(6)]
    ax_img_basin_c = plt.subplot2grid((3, 3), (0,1))
    ax_img_basin_c.set_position([0.05,0.45,0.43,0.5])
    ax_img_basin_ab = plt.subplot2grid((3, 3), (0,2))
    ax_img_basin_ab.set_position([0.52,0.45,0.43,0.5])

    #sch_name='basin_test'
    ax[0].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.cum_evap_scale1[:idx_im]*constants.m2mm,'-',color='brown'  ,markersize=ms,markeredgewidth=mew, markeredgecolor='brown'  ,label='A_Type',markevery=2)
    ax[0].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.cum_evap_scale2[:idx_im]*constants.m2mm,'-',color='orange',markersize=ms,markeredgewidth=mew, markeredgecolor='orange',label='B_Type',markevery=2)
    ax[0].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.cum_evap_scale3[:idx_im]*constants.m2mm,'-',color='greenyellow',markersize=ms,markeredgewidth=mew, markeredgecolor='greenyellow',label='D_Type',markevery=2)
    #sch_name='bacteria_second'
    #ax[0].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.cum_evap_scale1[:idx_im]*constants.m2mm,'o',color='brown',markersize=ms,markeredgewidth=mew, markeredgecolor='brown',markevery=1)
    #ax[0].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.cum_evap_scale2[:idx_im]*constants.m2mm,'s',color='orange',markersize=ms,markeredgewidth=mew, markeredgecolor='orange',markevery=2)
    #sch_name='bacteria_third'
    #ax[0].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.cum_evap_scale1[:idx_im]*constants.m2mm,'o',color='brown',markersize=ms,markeredgewidth=mew, markeredgecolor='brown',markevery=1)
    #ax[0].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.cum_evap_scale2[:idx_im]*constants.m2mm,'s',color='orange',markersize=ms,markeredgewidth=mew, markeredgecolor='orange',markevery=2) sch_name='bacteria_first'
    ax[1].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.evap_rate_scale1[:idx_im]*constants.ms2mmday,'-',color='brown'  ,markersize=ms,markeredgewidth=mew, markeredgecolor='brown'  ,label='A_Type',markevery=2)
    ax[1].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.evap_rate_scale2[:idx_im]*constants.ms2mmday,'-',color='orange',markersize=ms,markeredgewidth=mew, markeredgecolor='orange',label='B_Type',markevery=2)
    ax[1].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.evap_rate_scale3[:idx_im]*constants.ms2mmday,'-',color='greenyellow',markersize=ms,markeredgewidth=mew, markeredgecolor='greenyellow',label='D_Type',markevery=2)

    #sch_name='bacteria_second'
    #ax[1].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.evap_rate_scale1[:idx_im]*constants.ms2mmday,'o',color='brown',markersize=ms,markeredgewidth=mew, markeredgecolor='brown',markevery=1)
    #ax[1].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.evap_rate_scale2[:idx_im]*constants.ms2mmday,'s',color='orange',markersize=ms,markeredgewidth=mew, markeredgecolor='orange',markevery=2)
    #sch_name='bacteria_third'
    #ax[1].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.evap_rate_scale1[:idx_im]*constants.ms2mmday,'o',color='brown',markersize=ms,markeredgewidth=mew, markeredgecolor='brown',markevery=1)
    #ax[1].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.evap_rate_scale1[:idx_im]*constants.ms2mmday,'s',color='orange',markersize=ms,markeredgewidth=mew, markeredgecolor='orange',markevery=2)	
    
    #sch_name='bacteria_first'
    ax[2].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.mmoa1[:idx_im],'-',color='red',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='red',label='Moa1')
    ax[2].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.mmoa3[:idx_im],'-',color='green',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='green',label='Moa3')
    ax[2].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.mmob1[:idx_im],'-',color='cyan',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='cyan',label='Mob1')
    ax[2].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.mmob2[:idx_im],'-',color='gold',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='gold',label='Mob2')
    ax[2].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.mmob3[:idx_im],'-',color='black',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='black',label='Mob3')
    ax[2].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.mmoc1[:idx_im],'-',color='blue',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='blue',label='Moc1')
    ax[2].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.mmoc2[:idx_im],'-',color='purple',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='purple',label='Moc2')
    ax[2].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.mmoc3[:idx_im],'-',color='pink',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='pink',label='Moc3')

    ax[2].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.sat_scale1[:idx_im],'-',color='brown',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='A_Type',markevery=2)
    ax[2].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.sat_scale2[:idx_im],'-',color='orange',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='orange',label='B_Type',markevery=2)
    ax[2].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.sat_scale3[:idx_im],'-',color='greenyellow',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='greenyellow',label='D_Type',markevery=2)
    

    #sch_name='bacteria_second'
    #ax[2].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.mmo0[:idx_im],'o',color='red',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='red')
    #ax[2].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.mmo1[:idx_im],'o',color='green',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='green')
    #ax[2].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.mmo2[:idx_im],'o',color='cyan',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='cyan')
    #ax[2].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.mmo3[:idx_im],'o',color='brown',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown')
    #ax[2].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.mmo4[:idx_im],'o',color='black',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='black')
    #ax[2].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.mmo5[:idx_im],'o',color='blue',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='blue')
    #sch_name='bacteria_third'
    #ax[2].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.mmo0[:idx_im],'o',color='red',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='red')
    #ax[2].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.mmo1[:idx_im],'o',color='green',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='green')
    #ax[2].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.mmo2[:idx_im],'o',color='cyan',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='cyan')
    #ax[2].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.mmo3[:idx_im],'o',color='brown',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown')
    #ax[2].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.mmo4[:idx_im],'o',color='black',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='black')
    #ax[2].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.mmo5[:idx_im],'o',color='blue',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='blue')

    #sch_name='bacteria_first'
    ax[3].semilogy(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.suctiona1[:idx_im],'-',color='red',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='red',label='Sua1')
    ax[3].semilogy(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.suctiona2[:idx_im],'-',color='green',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='green',label='Sua2')
    ax[3].semilogy(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.suctiona3[:idx_im],'-',color='cyan',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='cyan',label='Sua3')
    ax[3].semilogy(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.suctionb1[:idx_im],'-',color='gold',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='gold',label='Sub1')
    ax[3].semilogy(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.suctionb3[:idx_im],'-',color='black',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='black',label='Sub3')
    ax[3].semilogy(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.suctionc1[:idx_im],'-',color='blue',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='blue',label='Suc1')
    ax[3].semilogy(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.suctionc2[:idx_im],'-',color='pink',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='pink',label='Suc2')
    ax[3].semilogy(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.suctionc3[:idx_im],'-',color='wheat',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='wheat',label='Suc3')

    ax[3].semilogy(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.suc_scale1[:idx_im],'-',color='brown',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='A_Type',markevery=2)
    ax[3].semilogy(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.suc_scale2[:idx_im],'-',color='orange',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='orange',label='B_Type',markevery=2)
    ax[3].semilogy(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.suc_scale3[:idx_im],'-',color='greenyellow',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='greenyellow',label='D_Type',markevery=2)
    #sch_name='bacteria_second'
    #ax[3].semilogy(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.suc_scale1[:idx_im],'o',color='brown',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown')
    #ax[3].semilogy(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.suc_scale2[:idx_im],'o',color='orange',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='orange')
    #sch_name='bacteria_third'
    #ax[3].semilogy(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.suc_scale1[:idx_im],'o',color='brown',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown')
    #ax[3].semilogy(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.suc_scale2[:idx_im],'o',color='orange',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='orange')

    
   # ta=sp_sch['bacteria'].df

   # ax[0].plot(ta['date_time'],ta['cum_evap_scale1']*constants.m2mm,'r-',linewidth=lw,markersize=ms,markeredgewidth=mew, markeredgecolor='g',label='scale 1',markevery=1)
   # ax[0].plot(ta['date_time'],ta['cum_evap_scale2']*constants.m2mm,'g-',linewidth=lw,markersize=ms,markeredgewidth=mew, markeredgecolor='r',label='scale 2',markevery=2)
   # ax[0].set_ylim([0,30])
   # 
   # ax[1].plot(ta['date_time'],ta['evap_rate_scale1']*constants.ms2mmday,'r-',linewidth=lw,markersize=ms,markeredgewidth=mew, markeredgecolor='g',label='scale 1',markevery=1)
   # ax[1].set_ylim([0,5.7])
   # ax[1].plot(ta['date_time'],ta['evap_rate_scale2']*constants.ms2mmday,'g-',linewidth=lw,markersize=ms,markeredgewidth=mew, markeredgecolor='r',label='scale 2',markevery=2)
   # ax[1].set_ylim([0,5.7])

   # ax[2].plot(ta['date_time'][::mkevy].values, ta['su0'][::mkevy].values, '-' ,color='maroon',linewidth=lw,markersize=ms           ,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Suction 1',markevery=mkevy)
   # ax[2].plot(ta['date_time'][::mkevy].values, ta['su1'][::mkevy].values, '-' ,color='olive',linewidth=lw,markersize=ms           ,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='Suction 2',markevery=mkevy)
   # ax[2].plot(ta['date_time'][::mkevy].values, ta['su2'][::mkevy].values, '-' ,color='peru',linewidth=lw,markersize=ms           ,markeredgewidth=mew,fillstyle='full', markeredgecolor='b',label='Suction 3',markevery=mkevy)
   # ax[2].plot(ta['date_time'][::mkevy].values, ta['su3'][::mkevy].values, '-' ,color='pink',linewidth=lw,markersize=ms           ,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='Suction 4',markevery=mkevy)
   # ax[2].plot(ta['date_time'][::mkevy].values, ta['su4'][::mkevy].values, '-' ,color='gold',linewidth=lw,markersize=ms           ,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='Suction 5',markevery=mkevy)
   # ax[2].plot(ta['date_time'][::mkevy].values, ta['su5'][::mkevy].values, '-' ,color='lightgreen',linewidth=lw,markersize=ms           ,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='Suction 6',markevery=mkevy)
   # ax[2].set_ylim([0,30])

   # mkevy=12

   # ax[3].plot(ta['date_time'][::mkevy], ta['mmo0'][::mkevy], '-',color='maroon',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Moisture 1',markevery=mkevy)
   # ax[3].plot(ta['date_time'][::mkevy], ta['mmo1'][::mkevy], '-',color='olive',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='Moisture 2',markevery=mkevy)
   # ax[3].plot(ta['date_time'][::mkevy], ta['mmo2'][::mkevy], '-',color='peru',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='b',label='Moisture 3',markevery=mkevy)
   # ax[3].plot(ta['date_time'][::mkevy], ta['mmo3'][::mkevy], '-',color='pink',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='Moisture 4',markevery=mkevy)
   # ax[3].plot(ta['date_time'][::mkevy], ta['mmo4'][::mkevy], '-',color='gold',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='Moisture 5',markevery=mkevy)
   # ax[3].plot(ta['date_time'][::mkevy], ta['mmo5'][::mkevy], '-',color='lightgreen',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='Moisture 6',markevery=mkevy)
   # ax[3].set_ylim([-0.1,1.1])    
   
   
   


    #ax[3].plot(ta['date_time'][::mkevy].values, ta['tmp5'][::mkevy].values, '-' ,color='lightgreen',linewidth=lw,markersize=ms           ,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='28cm',markevery=mkevy)
    #ax[3].plot(ta['date_time'][::mkevy].values, ta['tmp8'][::mkevy].values, '-' ,color='royalblue',linewidth=lw,markerfacecolor='orange',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='orange',label='70cm',markevery=mkevy)
    #ax[3].set_ylim([5,40])
    
    
    ax[0].set_xticklabels([])
    #ax[1].set_xticklabels([])
    ax[2].set_xticklabels([])
    #ax[3].set_xticklabels([])
    #ax[4].set_xticklabels([])
    xlim=[sp_sch[sch_name].df.time_days[0],sp_sch[sch_name].df.time_days[len(sp_sch[sch_name].df)-1]]
   # ax[0].set_xlim([sp_sch[sch_name].start_dt,sp_sch[sch_name].end_dt])
   # ax[1].set_xlim([sp_sch[sch_name].start_dt,sp_sch[sch_name].end_dt])
   # ax[2].set_xlim([sp_sch[sch_name].start_dt,sp_sch[sch_name].end_dt])
   # ax[3].set_xlim([sp_sch[sch_name].start_dt,sp_sch[sch_name].end_dt])
    #ax[4].set_xlim([sp_sch[sch_name].start_dt,sp_sch[sch_name].end_dt])
    #ax[5].set_xlim([sp_sch[sch_name].start_dt,sp_sch[sch_name].end_dt])
    ax[0].set_xlim(xlim)
    ax[1].set_xlim(xlim)
    ax[2].set_xlim(xlim)
    ax[3].set_xlim(xlim)
    
    ax[0].set_ylabel('CUMULATIVE\nEVAPORATION\n (mm)', fontsize=y_fontsize, labelpad=10)
    ax[1].set_ylabel('EVAPORATION\nRATE\n(mm/Day)', fontsize=y_fontsize, labelpad=10)
    ax[2].set_ylabel('DEGREE OF\nSATURATION', fontsize=y_fontsize, labelpad=10)
    ax[3].set_ylabel('SUCTION\n(kPa)', fontsize=y_fontsize, labelpad=10)
    #ax[4].set_ylabel('DEGREE OF\nSATURATION\nBELOW SOIL\nSURFACE', fontsize=y_fontsize, labelpad=7)
    #ax[5].set_ylabel('ELECTRICAL\nCONDUCTIVITY\nBELOW SOIL\nSURFACE \n(mS/cm)', fontsize=y_fontsize, labelpad=15)
    
    #ax[0].set_title('(A)',x=0.04,y=0.8,fontweight='bold')
    #ax[1].set_title('(B)',x=0.04,y=0.8,fontweight='bold')
    #ax[2].set_title('(C)',x=0.04,y=0.8,fontweight='bold')
    #ax[3].set_title('(D)',x=0.04,y=0.8,fontweight='bold')
    #ax[4].set_title('(E)',x=0.04,y=0.8,fontweight='bold')
    #ax[5].set_title('(F)',x=0.04,y=0.8,fontweight='bold')
    ax[0].set_axisbelow(True)
    ax[1].set_axisbelow(True)
    ax[2].set_axisbelow(True)
    ax[3].set_axisbelow(True)
    #ax[4].set_axisbelow(True)
    #ax[5].set_axisbelow(True)
    #ax[0].legend(bbox_to_anchor=(1.07, 0.5 ), loc='center', borderaxespad=0.,fontsize=9,handletextpad=0.03,labelspacing=0.02,ncol=1,columnspacing=0.4)
    #ax[1].legend(bbox_to_anchor=(1.07, 0.5 ), loc='center', borderaxespad=0.,fontsize=9,handletextpad=0.03,labelspacing=0.02,ncol=1,columnspacing=0.4)
    ax[2].legend(bbox_to_anchor=(1.09, 0.5 ), loc='center', borderaxespad=0.,fontsize=10,handletextpad=0.03,labelspacing=0.1,ncol=1,columnspacing=0.4)
    ax[3].legend(bbox_to_anchor=(1.09, 0.5 ), loc='center', borderaxespad=0.,fontsize=10,handletextpad=0.03,labelspacing=0.1,ncol=1,columnspacing=0.4)
    
    ax_img_basin_ab.imshow(im_basin_ab)
    ax_img_basin_ab.axis('off')
    ax_img_basin_c.imshow(im_basin_c)
    ax_img_basin_c.axis('off')
    ax_img_basin_ab.set_title('B_TYPE       A_TYPE',x=0.05,y=0.9,fontweight='bold',fontsize=40,color='white',loc='left')
    ax_img_basin_c.set_title('D_TYPE',x=0.05,y=0.9,fontweight='bold',fontsize=40,color='white',loc='left')

    #ax[1].label_params(labeltop='off', labelright='off')
    #ax[2].label_params(labeltop='off', labelright='off')
    #ax[3].label_params(labeltop='off', labelright='off')
    #ax[4].label_params(labeltop='off', labelright='off')
    #ax[5].label_params(labeltop='off', labelright='off')
    #ax[0].legend(bbox_to_anchor=(.8, 0.9), loc=2, borderaxespad=0.,fontsize=9,handletextpad=0.13,labelspacing=0.05)
    #ax[1].legend(bbox_to_anchor=(.8, 0.85), loc=2, borderaxespad=0.,fontsize=9,handletextpad=0.13,labelspacing=0.05)
    #ax[2].legend(bbox_to_anchor=(.03, 0.85), loc=2, borderaxespad=0.,fontsize=8,handletextpad=0.13,labelspacing=0.05)
    #ax[3].legend(bbox_to_anchor=(.77, 0.99 ), loc=2, borderaxespad=0.,fontsize=8,handletextpad=0.03,labelspacing=0.02,ncol=2,columnspacing=0.4)
    #ax[4].legend(bbox_to_anchor=(.8, 0.7), loc=2, borderaxespad=0.,fontsize=8,handletextpad=0.03,labelspacing=0.02,ncol=2,columnspacing=0.4)#title='CM below surface')
    #plt.setp(ax[3].get_legend().get_title(), fontsize='8') 
    #ax[4].legend(bbox_to_anchor=(.8, 0.9 ), loc=2, borderaxespad=0.,fontsize=9,handletextpad=0.13,labelspacing=0.05)
    
    ax[0].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[1].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[2].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[3].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    #ax[4].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    #ax[5].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    #ax[2].plot(ta['date_time'], ta['su5'], 'ro',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Dielectric suction A')
    #ax[2].plot(ta['date_time'], ta['su6'], 'go',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='Dielectric suction B')
    #ax[2].plot(ta['date_time'], ta['su7'], 'bo',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='b',label='Moisture A')
    #ax[2].plot(ta['date_time'], ta['su8'], 'co',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='Moisture A')
    #
    #
    #ax[3].plot(ta['date_time'], ta['temp_suc1'], 'ro',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Dielectric suction A')
    #ax[3].plot(ta['date_time'], ta['temp_suc2'], 'go',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='Dielectric suction B')
    #ax[3].plot(ta['date_time'], ta['temp_suc3'], 'bo',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='b',label='Moisture A')
    #ax[3].plot(ta['date_time'], ta['temp_suc4'], 'co',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='Moisture A')
    #ax[3].plot(ta['date_time'], ta['temp_suc5'], 'mo',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='Moisture A')
    #ax[3].plot(ta['date_time'], ta['temp_suc6'], 'ko',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='Moisture A')
    #ax[3].plot(ta['date_time'], ta['temp_suc7'], 'o' ,markerfacecolor='brown' ,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='Moisture A')
    ax[0].set_ylim([-0.4,10])
    ax[1].set_ylim([-0.2,5])
    ax[2].set_ylim([-0.1,1.1])
    ax[3].set_ylim([1,2.5e6])

    ax[1].set_xlabel('TIME (Days)', fontsize=y_fontsize,labelpad=3)
    #ax[1].xaxis.set_major_formatter(mdates.DateFormatter('%b/%d'))
    #ax[1].set_xlabel('TIME(DAYS)') 
    #ax[3].xaxis.set_major_formatter(mdates.DateFormatter('%b/%d'))
    #ax[3].set_xlabel('TIME(DAYS)')
    ax[3].set_xlabel('TIME (Days)', fontsize=y_fontsize,labelpad=3)
    #plt.xticks(rotation=45)
    plt.show(block=False)
    
    #fig.savefig('figure/plot_bacteria'+ii+'.png', format='png', dpi=100)
    output_name = 'figure/video/000'+str(ii)+'.jpg'
    fig.savefig(output_name, format='jpg', dpi=100)
    plt.close()
