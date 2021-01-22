import matplotlib
import glob, os

import matplotlib.image as image
import matplotlib.pylab as pylab

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

path_im='/home/chenming/Dropbox/photo_stanwell/'
files = filter(os.path.isfile, glob.glob(path_im + "*.jpg"))
files.sort(key=lambda x: get_date_taken(x))
file_name=[i.split('/')[-1] for i in files]



#for ii in file_name[:1]:
for ii in file_name:
   
    im=image.imread(path_im+ii)   
    im_time=get_date_taken(path_im+ii)
    idx_im, min_value = min(enumerate( abs(sp_sch[sch_name].df['date_time']-im_time)), key=operator.itemgetter(1))
    


    
    #fig, ax = plt.subplots(6,2,sharex=True,figsize=(16,9))
    fig = plt.figure(figsize=(16,9))
    ax = [[] for i in range(6)]
    ax[0] = plt.subplot2grid((6, 2), (0, 0), colspan=1)
    ax[1] = plt.subplot2grid((6, 2), (1, 0), colspan=1)
    ax[2] = plt.subplot2grid((6, 2), (2, 0), colspan=1)
    ax[3] = plt.subplot2grid((6, 2), (3, 0), colspan=1)
    ax[4] = plt.subplot2grid((6, 2), (4, 0), colspan=1)
    ax[5] = plt.subplot2grid((6, 2), (5, 0), colspan=1)

    fig.subplots_adjust(hspace=.20)
    fig.subplots_adjust(left=0.1, right=0.89, top=0.97, bottom=0.05)
    #ax_img.set_position([0.47,0.01,0.53,0.97])
    
    
    #fig, ax = plt.subplots(6,sharex=True,figsize=(6,8))
    #jfig.subplots_adjust(hspace=.15)
    mkevy=4
    
    
    for i in ax:
          for axis in ['top','bottom','left','right']:
            i.spines[axis].set_linewidth(2)
    ax_img = plt.subplot2grid((1, 3), (0,2))
    ax_img.set_position([0.53,0.39,0.45,0.58])
    
    ta=sp_sch['stanwell'].df
    
    ax[0].plot(ta['date_time'][:idx_im], ta['rainmm'][:idx_im], '-',color='maroon',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Dielectric suction A')
    ax[0].set_ylim([-4,30])
    
    yy=(ta['ir_up']-ta['ir_down'])*0.007+0.2*ta['wdspdkphavg2m'].fillna(0)
    ax[1].plot(ta['date_time'][:idx_im], yy[:idx_im], '-',color='maroon',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Dielectric suction A')
    ax[1].set_ylim([-0.100,9])
    
    #ax[2].plot(ta['date_time'], -(ta['pre0']-60), 'r-',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='30 cm below soil surface')
    #ax[2].plot(ta['date_time'], -(ta['pre1']-110), 'g-',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='60 cm below soil surface')
    #ax[2].set_ylim([-10-110,140-110])
    #ax[2].set_ylim([-140+110,120,])
    ax[2].plot(ta['date_time'][:idx_im], ta['pre0'][:idx_im], '-',color='cyan',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='50 cm')
    ax[2].plot(ta['date_time'][:idx_im], ta['pre1'][:idx_im], '-',color='darkblue',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='100 cm')
    #ax[2].set_ylim([-10-110,140-110])
    ax[2].set_ylim([-100,1300])
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
    ax[3].set_ylim([5,40])
    
    mkevy=12
    
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
    ax[4].set_ylim([-0.1,1.1])
    
    ax[5].plot(ta['date_time'][:idx_im], ta['ec0'][:idx_im]/1000., '-',color='olive',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='5 cm')
    ax[5].plot(ta['date_time'][:idx_im], ta['ec2'][:idx_im]/1000., '-',color='royalblue',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='60cm')
    ax[5].set_ylim([-0.2,1.7])
    
    ax[0].set_xticklabels([])
    ax[1].set_xticklabels([])
    ax[2].set_xticklabels([])
    ax[3].set_xticklabels([])
    ax[4].set_xticklabels([])
    xlim=[sp_sch[sch_name].df.time_days[0],sp_sch[sch_name].df.time_days[len(sp_sch[sch_name].df)-1]]
    ax[0].set_xlim([sp_sch[sch_name].start_dt,sp_sch[sch_name].end_dt])
    ax[1].set_xlim([sp_sch[sch_name].start_dt,sp_sch[sch_name].end_dt])
    ax[2].set_xlim([sp_sch[sch_name].start_dt,sp_sch[sch_name].end_dt])
    ax[3].set_xlim([sp_sch[sch_name].start_dt,sp_sch[sch_name].end_dt])
    ax[4].set_xlim([sp_sch[sch_name].start_dt,sp_sch[sch_name].end_dt])
    ax[5].set_xlim([sp_sch[sch_name].start_dt,sp_sch[sch_name].end_dt])
    #ax[1].set_xlim(xlim)
    #ax[2].set_xlim(xlim)
    #ax[3].set_xlim(xlim)
    #ax[4].set_xlim(xlim)
    #ax[5].set_xlim(xlim)

 
    
    ax[0].set_ylabel('DAILY\nACCUMULATED\nRAINFALL (mm)', fontsize=y_fontsize, labelpad=10)
    ax[1].set_ylabel('POTENTIAL\nEVAPORATION\nRATE\n(mm/Day)', fontsize=y_fontsize, labelpad=25)
    ax[2].set_ylabel('WATER\nPRESSURE\n(mm)', fontsize=y_fontsize, labelpad=5)
    ax[3].set_ylabel('TEMPERATURE\nBELOW SOIL\nSURFACE\n($^\circ$C)', fontsize=y_fontsize, labelpad=13)
    ax[4].set_ylabel('DEGREE OF\nSATURATION\nBELOW SOIL\nSURFACE', fontsize=y_fontsize, labelpad=7)
    ax[5].set_ylabel('ELECTRICAL\nCONDUCTIVITY\nBELOW SOIL\nSURFACE \n(mS/cm)', fontsize=y_fontsize, labelpad=15)
    
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
    
    ax[5].xaxis.set_major_formatter(mdates.DateFormatter('%b/%d'))
    ax[5].set_xlabel('DATE')
    #plt.xticks(rotation=45)
    #plt.show(block=False)
    
    fig.savefig('figure/plot_stanwell'+ii+'.png', format='png', dpi=100)
    plt.close()
