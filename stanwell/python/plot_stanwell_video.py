import matplotlib
import glob, os
from datetime import datetime
import matplotlib.image as image
import matplotlib.pylab as pylab
matplotlib.use('Agg')

lw=1.5
ms=1
mew=3
grid_width=2
y_fontsize=12

params = {'legend.fontsize': 4,
          'figure.figsize': (10, 5),
         'axes.labelsize': 11,
         'axes.titlesize':'11',
         'xtick.labelsize':'11',
         'ytick.labelsize':'11',
         'font.weight':'bold',
         'font.sans-serif':'Arial',
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
y_fontsize=11

from PIL import Image
def get_date_taken(path):
    from datetime import datetime
    return datetime.strptime(Image.open(path)._getexif()[36867],'%Y:%m:%d %H:%M:%S')

path_im='/home/osboxes/stanwell/'
files = filter(os.path.isfile, glob.glob(path_im + "*.jpg"))
files.sort(key=lambda x: get_date_taken(x))
file_name=[i.split('/')[-1] for i in files]
photo_taken_time=[i[0:16] for i in file_name]
date=[datetime.strptime(x,'%Y_%m_%d_%H_%M') for x in photo_taken_time]



#for ii in file_name[:1]:
#for ii in file_name:
#    im=image.imread(path_im+ii)   
#    im_time=get_date_taken(path_im+ii)
#    idx_im, min_value = min(enumerate( abs(sp_sch[sch_name].df['date_time']-im_time)), key=operator.itemgetter(1))
#    idx_settlement, min_value = min(enumerate( abs(daily_data_manual.index-im_time)), key=operator.itemgetter(1))
#    idx_rainm, min_value = min(enumerate( abs(df_mean.index-im_time)), key=operator.itemgetter(1))
for ii in range(len(date)):
    im_path=path_im+file_name[ii]
    im=image.imread(im_path)
    im_time=date[ii]
    idx_im, min_value = min(enumerate( abs(sp_sch[sch_name].df['date_time']-im_time)), key=operator.itemgetter(1))
    idx_settlement, min_value = min(enumerate( abs(daily_data_manual.index-im_time)), key=operator.itemgetter(1))
    idx_rainm, min_value = min(enumerate( abs(df_mean.index-im_time)), key=operator.itemgetter(1))
   


    
    #fig, ax = plt.subplots(6,2,sharex=True,figsize=(16,9))
    fig = plt.figure(figsize=(16,10))
    ax = [[] for i in range(7)]
    ax[0] = plt.subplot2grid((7, 2), (0, 0), colspan=1)
    ax[1] = plt.subplot2grid((7, 2), (1, 0), colspan=1)
    ax[2] = plt.subplot2grid((7, 2), (2, 0), colspan=1)
    ax[3] = plt.subplot2grid((7, 2), (3, 0), colspan=1)
    ax[4] = plt.subplot2grid((7, 2), (4, 0), colspan=1)
    ax[5] = plt.subplot2grid((7, 2), (5, 0), colspan=1)
    ax[6] = plt.subplot2grid((7, 2), (6, 0), colspan=1)

    fig.subplots_adjust(hspace=.20)
    fig.subplots_adjust(left=0.1, right=0.89, top=0.97, bottom=0.05)
    #ax_img.set_position([0.47,0.01,0.53,0.97])
    ax_mo = plt.subplot2grid((2, 5), (1,3), colspan=1)
    ax_mo.set_position([0.52,0.08,0.15,0.42])
    #
    ax_mo.set_xlabel('VOLUMETRIC\nMOISTURE CONTENT')
    ax_mo.set_ylabel('DEPTH FROM COLUMN TOP(cm)')
    #ax_img.axis('off')
    ax_temp = plt.subplot2grid((2, 5), (1,4), colspan=1)
    ax_temp.set_position([0.74,0.08,0.15,0.42])
    #
    ax_temp.set_xlabel('TEMPERATURE\n($^\circ$C)')
    ax_temp.set_ylabel('DEPTH FROM COLUMN TOP (cm)')

    ax_img = plt.subplot2grid((2, 2), (0,1))
    ax_img.set_position([0.43,0.55,0.75,0.42])

    ax_mo.grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax_temp.grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')

    
    #fig, ax = plt.subplots(6,sharex=True,figsize=(6,8))
    #jfig.subplots_adjust(hspace=.15)
    mkevy=4
    ta=sp_sch['stanwell'].df
    
    
    for i in ax:
          for axis in ['top','bottom','left','right']:
            i.spines[axis].set_linewidth(2)


    depth_y=np.array([1,5,8,13,20,28,38,48,70,85])
    #depth_y_temp=np.array([1,5,8,13,20,28,38,48,70,85])
    depth_y_temp=np.array([1,5,8,13,20,38,48,85])
    mo_x=ta.iloc[idx_im][['mmo0','mmo1','mmo2','mmo3','mmo4','mmo5','mmo6','mmo7','mmo8','mmo9']].tolist()
    #temp_x=ta.iloc[idx_im][['tmp0','tmp1','tmp2','tmp3','tmp4','tmp5','tmp6','tmp7','tmp8','tmp9']].tolist()
    #temp_x=ta.iloc[idx_im][['tmp0','tmp1','tmp2','tmp3','tmp4','tmp5','tmp6','tmp7','tmp9']].tolist()
    temp_x=ta.iloc[idx_im][['tmp0','tmp1','tmp2','tmp3','tmp4','tmp6','tmp7','tmp9']].tolist()
    ax_mo.plot(mo_x,depth_y,'-',color='blue')
    ax_mo.set_ylim([90,0])
    ax_mo.set_xlim([-0.05,1.05])

    ax_temp.plot(temp_x,depth_y_temp,'-',color='maroon')
    ax_temp.set_ylim([90,0])
    ax_temp.set_xlim([0,50])

    ax_mo.set_position([0.63,0.09,0.15,0.45])
    ax_temp.set_position([0.84,0.09,0.15,0.45])



    
    #ta=sp_sch['stanwell'].df
    
    #ax[0].plot(ta['date_time'][:idx_im], ta['rainmm'][:idx_im], '-',color='maroon',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Dielectric suction A')
    #ax[0].set_ylim([-4,30])
    ax[0].bar(df_mean.index[:idx_rainm], df_last['rainmm'][:idx_rainm], width=1.8,edgecolor='white',lw=0.1)
    ax[0].set_ylim([-0.1,33])

    #yy=(ta['ir_up']-ta['ir_down'])*0.007+0.2*ta['wdspdkphavg2m'].fillna(0)
    #ax[1].plot(ta['date_time'][:idx_im], yy[:idx_im], '-',color='maroon',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Dielectric suction A')
    #ax[1].set_ylim([-0.100,9])
    #ax[1].plot(df_mean['pet_mmPday'][:idx_im], '-',color='maroon',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Pote.\nevap.')
    #ax[1].plot(df_mean['aet_mmPday'][:idx_im], '-',color='maroon',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Pote.\nevap.')
    ax[1].bar(df_mean.index[:idx_rainm],df_mean['pet_mmPday'][:idx_rainm],width=1.0,color='brown',edgecolor='white',label='Pote.\nevap.',lw=0.1)
    ax[1].bar(df_mean.index[:idx_rainm],df_mean['aet_mmPday'][:idx_rainm],width=1.0,color='orange',edgecolor='white',label='Actu.\nevap.',lw=0.1)
    ax[1].set_ylim([-0.1,11])




    #ax[2].plot(ta['date_time'], -(ta['pre0']-60), 'r-',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='30 cm below soil surface')
    #ax[2].plot(ta['date_time'], -(ta['pre1']-110), 'g-',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='60 cm below soil surface')
    #ax[2].set_ylim([-10-110,140-110])
    #ax[2].set_ylim([-140+110,120,])
    ax[2].plot(ta['date_time'][:idx_im], ta['Pre0'][:idx_im], '-',color='cyan',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='50 cm')
    ax[2].plot(ta['date_time'][:idx_im], ta['Pre1'][:idx_im], '-',color='darkblue',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='100 cm')
    #ax[2].set_ylim([-10-110,140-110])
    #ax[2].set_ylim([-100,1300])
    ax[2].set_ylim([-100,1100])
    #ax[2].set_ylim([-140+110,120,])
    
    #ax[3].plot(ta['date_time'][::mkevy].values, ta['tmp0'][::mkevy].values, '-' ,color='maroon',linewidth=lw,markersize=ms           ,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='1 cm',markevery=mkevy)
    #ax[3].plot(ta['date_time'][::mkevy].values, ta['tmp1'][::mkevy].values, '-' ,color='peru',linewidth=lw,markersize=ms           ,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='5 cm',markevery=mkevy)
    #ax[3].plot(ta['date_time'][::mkevy].values, ta['tmp2'][::mkevy].values, '-' ,color='gold',linewidth=lw,markersize=ms           ,markeredgewidth=mew,fillstyle='full', markeredgecolor='b',label='8 cm',markevery=mkevy)
    #ax[3].plot(ta['date_time'][::mkevy].values, ta['tmp3'][::mkevy].values, '-' ,color='olive',linewidth=lw,markersize=ms           ,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='13cm',markevery=mkevy)
    #ax[3].plot(ta['date_time'][::mkevy].values, ta['tmp4'][::mkevy].values, '-' ,color='limegreen',linewidth=lw,markersize=ms           ,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='20cm',markevery=mkevy)
    #ax[3].plot(ta['date_time'][::mkevy].values, ta['tmp5'][::mkevy].values, '-' ,color='lightblue',linewidth=lw,markersize=ms           ,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='28cm',markevery=mkevy)
    #ax[3].plot(ta['date_time'][::mkevy].values, ta['tmp6'][::mkevy].values, '-' ,color='royalblue'  ,linewidth=lw,markerfacecolor='brown' ,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='38cm',markevery=mkevy)
    #ax[3].plot(ta['date_time'][::mkevy].values, ta['tmp7'][::mkevy].values, '-' ,color='darkblue' ,linewidth=lw,markerfacecolor='yellow',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='yellow',label='48cm',markevery=mkevy)
    #ax[3].plot(ta['date_time'][::mkevy].values, ta['tmp8'][::mkevy].values, '-' ,color='crimson',linewidth=lw,markerfacecolor='orange',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='orange',label='70cm',markevery=mkevy)
    #ax[3].plot(ta['date_time'][::mkevy].values, ta['tmp9'][::mkevy].values, '-' ,color='pink'   ,linewidth=lw,markerfacecolor='grey'  ,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='grey',label='85cm',markevery=mkevy)
    
    ax[3].plot(ta['date_time'][:idx_im][::mkevy].values, ta['tmp0'][:idx_im][::mkevy].values, '-' ,color='maroon',linewidth=lw,markersize=ms           ,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='1 cm',markevery=mkevy)
    ax[3].plot(ta['date_time'][:idx_im][::mkevy].values, ta['tmp1'][:idx_im][::mkevy].values, '-' ,color='olive',linewidth=lw,markersize=ms           ,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='5 cm',markevery=mkevy)
    ax[3].plot(ta['date_time'][:idx_im][::mkevy].values, ta['tmp2'][:idx_im][::mkevy].values, '-' ,color='peru',linewidth=lw,markersize=ms           ,markeredgewidth=mew,fillstyle='full', markeredgecolor='b',label='8 cm',markevery=mkevy)
    ax[3].plot(ta['date_time'][:idx_im][::mkevy].values, ta['tmp3'][:idx_im][::mkevy].values, '-' ,color='pink',linewidth=lw,markersize=ms           ,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='13cm',markevery=mkevy)
    ax[3].plot(ta['date_time'][:idx_im][::mkevy].values, ta['tmp4'][:idx_im][::mkevy].values, '-' ,color='gold',linewidth=lw,markersize=ms           ,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='20cm',markevery=mkevy)
    ax[3].plot(ta['date_time'][:idx_im][::mkevy].values, ta['tmp6'][:idx_im][::mkevy].values, '-' ,color='lightblue'  ,linewidth=lw,markerfacecolor='brown' ,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='38cm',markevery=mkevy)
    ax[3].plot(ta['date_time'][:idx_im][::mkevy].values, ta['tmp7'][:idx_im][::mkevy].values, '-' ,color='cyan' ,linewidth=lw,markerfacecolor='yellow',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='yellow',label='48cm',markevery=mkevy)
    ax[3].plot(ta['date_time'][:idx_im][::mkevy].values, ta['tmp9'][:idx_im][::mkevy].values, '-' ,color='darkblue'   ,linewidth=lw,markerfacecolor='grey'  ,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='grey',label='85cm',markevery=mkevy)
    #ax[3].plot(ta['date_time'][::mkevy].values, ta['tmp5'][::mkevy].values, '-' ,color='lightgreen',linewidth=lw,markersize=ms           ,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='28cm',markevery=mkevy)
    #ax[3].plot(ta['date_time'][::mkevy].values, ta['tmp8'][::mkevy].values, '-' ,color='royalblue',linewidth=lw,markerfacecolor='orange',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='orange',label='70cm',markevery=mkevy)
    #ax[3].set_ylim([5,40])
    ax[3].set_ylim([5,45])
    
    mkevy=12
    mkevy=24
    
    ax[4].plot(ta['date_time'][:idx_im][::mkevy], ta['mmo0'][:idx_im][::mkevy], '-',color='maroon',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='1 cm',markevery=mkevy)
    ax[4].plot(ta['date_time'][:idx_im][::mkevy], ta['mmo1'][:idx_im][::mkevy], '-',color='olive',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='5 cm',markevery=mkevy)
    ax[4].plot(ta['date_time'][:idx_im][::mkevy], ta['mmo2'][:idx_im][::mkevy], '-',color='peru',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='b',label='8 cm',markevery=mkevy)
    ax[4].plot(ta['date_time'][:idx_im][::mkevy], ta['mmo3'][:idx_im][::mkevy], '-',color='pink',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='13cm',markevery=mkevy)
    ax[4].plot(ta['date_time'][:idx_im][::mkevy], ta['mmo4'][:idx_im][::mkevy], '-',color='gold',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='20cm',markevery=mkevy)
    ax[4].plot(ta['date_time'][:idx_im][::mkevy], ta['mmo5'][:idx_im][::mkevy], '-',color='lightgreen',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='28cm',markevery=mkevy)
    ax[4].plot(ta['date_time'][:idx_im][::mkevy], ta['mmo6'][:idx_im][::mkevy], '-' ,color='lightblue',linewidth=lw ,markerfacecolor='brown' ,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='38cm',markevery=mkevy)
    ax[4].plot(ta['date_time'][:idx_im][::mkevy], ta['mmo7'][:idx_im][::mkevy], '-' ,color='cyan',linewidth=lw, markerfacecolor='yellow' ,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='yellow',label='48cm',markevery=mkevy)
    ax[4].plot(ta['date_time'][:idx_im][::mkevy], ta['mmo8'][:idx_im][::mkevy], '-' ,color='royalblue',linewidth=lw,markerfacecolor='crimson' ,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='crimson',label='70cm',markevery=mkevy)
    ax[4].plot(ta['date_time'][:idx_im][::mkevy], ta['mmo9'][:idx_im][::mkevy], '-' ,color='darkblue',linewidth=lw,markerfacecolor='pink' ,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='pink',label='85cm',markevery=mkevy)
    ax[4].set_ylim([-0.05,0.8])
    
    ax[5].plot(ta['date_time'][:idx_im], ta['ec0'][:idx_im]/1000., '-',color='olive',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='5 cm')
    ax[5].plot(ta['date_time'][:idx_im], ta['ec2'][:idx_im]/1000., '-',color='royalblue',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='60cm')
    ax[5].set_ylim([-0.2,1.7])

    ax[6].plot(daily_data_manual.index[:idx_settlement], daily_data_manual['settlement_mm'][:idx_settlement], '-',color='maroon',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='5 cm')
    ax[6].set_ylim([-1,179])

    
    ax[0].set_xticklabels([])
    ax[1].set_xticklabels([])
    ax[2].set_xticklabels([])
    ax[3].set_xticklabels([])
    ax[4].set_xticklabels([])
    ax[5].set_xticklabels([])
    xlim=[sp_sch[sch_name].df.time_days[0],sp_sch[sch_name].df.time_days[len(sp_sch[sch_name].df)-1]]
    ax[0].set_xlim([sp_sch[sch_name].start_dt,sp_sch[sch_name].end_dt])
    ax[1].set_xlim([sp_sch[sch_name].start_dt,sp_sch[sch_name].end_dt])
    ax[2].set_xlim([sp_sch[sch_name].start_dt,sp_sch[sch_name].end_dt])
    ax[3].set_xlim([sp_sch[sch_name].start_dt,sp_sch[sch_name].end_dt])
    ax[4].set_xlim([sp_sch[sch_name].start_dt,sp_sch[sch_name].end_dt])
    ax[5].set_xlim([sp_sch[sch_name].start_dt,sp_sch[sch_name].end_dt])
    ax[6].set_xlim([sp_sch[sch_name].start_dt,sp_sch[sch_name].end_dt])
    #ax[1].set_xlim(xlim)
    #ax[2].set_xlim(xlim)
    #ax[3].set_xlim(xlim)
    #ax[4].set_xlim(xlim)
    #ax[5].set_xlim(xlim)

 
    
    ax[0].set_ylabel('DAILY\nACCUMULATED\nRAINFALL\n(mm)', fontsize=y_fontsize, labelpad=15)
    #ax[1].set_ylabel('POTENTIAL\nEVAPORATION\nRATE\n(mm/Day)', fontsize=y_fontsize, labelpad=25)
    ax[1].set_ylabel('DAILY\nEVAPORATION\n(mm)', fontsize=y_fontsize, labelpad=18)
    ax[2].set_ylabel('WATER\nPRESSURE\n(mm)', fontsize=y_fontsize, labelpad=5)
    ax[3].set_ylabel('TEMPERATURE\nBELOW SOIL\nSURFACE\n($^\circ$C)', fontsize=y_fontsize, labelpad=13)
    ax[4].set_ylabel('VOL. MOIS.\nCONTENT\nBELOW COLUMN\nSURFACE', fontsize=y_fontsize, labelpad=15)#labelpad=7
    ax[5].set_ylabel('ELECTRICAL\nCONDUCTIVITY\nBELOW SOIL\nSURFACE \n(mS/cm)', fontsize=y_fontsize, labelpad=15)
    ax[6].set_ylabel('SURFACE \n SETTLEMENT\n(mm)', fontsize=y_fontsize, labelpad=15)

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
    ax[4].set_axisbelow(True)
    ax[5].set_axisbelow(True)
    #ax[1].legend(bbox_to_anchor=(1.07, 0.5 ), loc='center', borderaxespad=0.,fontsize=8.8,handletextpad=0.03,labelspacing=0.02,ncol=1,columnspacing=0.4)
    ax[1].legend(bbox_to_anchor=(1.07, 0.5 ), loc='center', borderaxespad=0.,fontsize=8.8,handletextpad=0.53,labelspacing=0.52,ncol=1,columnspacing=0.4)
    ax[2].legend(bbox_to_anchor=(1.07, 0.5 ), loc='center', borderaxespad=0.,fontsize=9,handletextpad=0.03,labelspacing=0.02,ncol=1,columnspacing=0.4)
    ax[3].legend(bbox_to_anchor=(1.07, 0.5 ), loc='center', borderaxespad=0.,fontsize=9,handletextpad=0.03,labelspacing=0.02,ncol=1,columnspacing=0.4)
    ax[4].legend(bbox_to_anchor=(1.07, 0.5 ), loc='center', borderaxespad=0.,fontsize=9,handletextpad=0.03,labelspacing=0.02,ncol=1,columnspacing=0.4)
    ax[5].legend(bbox_to_anchor=(1.07, 0.5 ), loc='center', borderaxespad=0.,fontsize=9,handletextpad=0.03,labelspacing=0.02,ncol=1,columnspacing=0.4)
    
    ax_img.imshow(im)
    ax_img.axis('off')
   
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
    ax[4].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[5].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[6].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
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
    
    ax[6].xaxis.set_major_formatter(mdates.DateFormatter('%b/%d'))
    ax[6].set_xlabel('DATE')
    #plt.xticks(rotation=45)
    plt.show(block=False)
    output_name = 'figure/video/000'+str(ii)+'.jpg'
    fig.savefig(output_name, format='jpg', dpi=100)
    plt.close()
