import glob

from PIL import Image
def get_date_taken(path):
        from datetime import datetime
        return datetime.strptime(Image.open(path)._getexif()[36867],'%Y:%m:%d %H:%M:%S')


#schedule['photo_path']='/home/chenming/Projects/tailings/column_qal/photo/'
files_nobact = filter(os.path.isfile, glob.glob(schedule['photo_path'] + "*.jpg"))
files_nobact.sort(key=lambda x: get_date_taken(x))
file_name_nobact=[i.split('/')[-1] for i in files_nobact]
photo_taken_time_nobact=[get_date_taken(i) for i in files_nobact]
ta['evap']=(ta['ir_up_concat']-254)/20.512*0.007


#data_mo_su.df.loc[mask,'mo1']=443+np.random.rand(np.sum(mask))*20


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

#for ii in [file_name_nobact[-1]]:
#for ii in file_name_nobact[::20]:
#for ii in file_name_nobact[::3]:
for ii in file_name_nobact[::1]:
    im_nobact=image.imread(schedule['photo_path']+ii)
    im_time_nobact=get_date_taken(schedule['photo_path']+ii)
    idx_im, min_value = min(enumerate( abs(ta.index-im_time_nobact)), key=operator.itemgetter(1))
    idx_settlement, min_value = min(enumerate( abs(daily_data_manual.index-im_time_nobact)), key=operator.itemgetter(1))

    fig, ax = plt.subplots(7,2,sharex=True,figsize=(13,9))
    fig.subplots_adjust(hspace=.10)
    fig.subplots_adjust(left=0.11, right=0.99, top=0.97, bottom=0.05)
    fig.subplots_adjust(wspace=.2)
    
    ax_mo = plt.subplot2grid((2, 5), (1,3))
    ax_mo.set_position([0.61,0.05,0.15,0.45])
    #
    ax_mo.set_xlabel('VOLUMETRIC\nMOISTURE CONTENT')
    ax_mo.set_ylabel('DEPTH FROM COLUMN TOP(cm)')
    #ax_img.axis('off')
    ax_temp = plt.subplot2grid((2, 5), (1,4))
    ax_temp.set_position([0.91,0.05,0.15,0.45])
    #
    ax_temp.set_xlabel('TEMPERATURE ($^\circ$C)')
    ax_temp.set_ylabel('DEPTH FROM COLUMN TOP (cm)')
    
    ax_img = plt.subplot2grid((2, 2), (0,1))
    #
    ax_img.set_position([0.61,0.55,0.38,0.45])
    #ax_img.set_position([0.53,0.25,0.45,0.48])
    #ax_img.axis('off')
    
    
    #fig, ax = plt.subplots(6,sharex=True,figsize=(6,8))
    mkevy=4
    
    depth_y=np.array([1,5,8,13,20,28,38,48,70,85])
    #depth_y_temp=np.array([1,5,8,13,20,28,38,48,70,85])
    depth_y_temp=np.array([1,5,8,13,20,38,48,85])
    mo_x=ta.iloc[idx_im][['mmo0','mmo1','mmo2','mmo3','mmo4','mmo5','mmo6','mmo7','mmo8','mmo9']].tolist()
    #temp_x=ta.iloc[idx_im][['tmp0','tmp1','tmp2','tmp3','tmp4','tmp5','tmp6','tmp7','tmp8','tmp9']].tolist()
    #temp_x=ta.iloc[idx_im][['tmp0','tmp1','tmp2','tmp3','tmp4','tmp5','tmp6','tmp7','tmp9']].tolist()
    temp_x=ta.iloc[idx_im][['tmp0','tmp1','tmp2','tmp3','tmp4','tmp6','tmp7','tmp9']].tolist()
    ax_mo.plot(mo_x,depth_y,'-',color='maroon')
    ax_mo.set_ylim([90,0])
    ax_mo.set_xlim([-0.05,1.05])

    ax_temp.plot(temp_x,depth_y_temp,'-',color='maroon')
    ax_temp.set_ylim([90,0])
    ax_temp.set_xlim([0,50])
    
    ax_mo.set_position([0.63,0.09,0.15,0.45])
    ax_temp.set_position([0.84,0.09,0.15,0.45])


    for axis in ['top','bottom','left','right']:
        ax_mo.spines[axis].set_linewidth(2)
        ax_temp.spines[axis].set_linewidth(2)

    for i in ax:
        for j in i:
          for axis in ['top','bottom','left','right']:
            j.spines[axis].set_linewidth(2)

    ax_img.imshow(im_nobact)   
    ax_img.axis('off')
    ax[0][0].plot(ta.index[:idx_im], ta['rainmm'][:idx_im], '-',color='maroon',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Dielectric suction A')
    ax[0][0].set_ylim([-0.5,20])
    
    ax[1][0].plot(ta.index[:idx_im], ta['evap'][:idx_im], '-',color='maroon',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Dielectric suction A')
    ax[1][0].set_ylim([-0.100,9])
    
    ax[2][0].plot(ta.index[:idx_im], ta['pre0'][:idx_im], '-',color='maroon',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='maroon',label='50 cm')
    ax[2][0].plot(ta.index[:idx_im], ta['pre1'][:idx_im], '-',color='olive',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='olive',label='100 cm')
    ax[2][0].set_ylim([-100,1300])
    
    ax[3][0].plot(ta.index[:idx_im][::mkevy].values, ta['tmp0'][:idx_im][::mkevy].values, '-' ,color='maroon',linewidth=lw,markersize=ms           ,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='2 cm',markevery=mkevy)
    ax[3][0].plot(ta.index[:idx_im][::mkevy].values, ta['tmp1'][:idx_im][::mkevy].values, '-' ,color='olive',linewidth=lw,markersize=ms           ,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='5 cm',markevery=mkevy)
    ax[3][0].plot(ta.index[:idx_im][::mkevy].values, ta['tmp2'][:idx_im][::mkevy].values, '-' ,color='peru',linewidth=lw,markersize=ms           ,markeredgewidth=mew,fillstyle='full', markeredgecolor='b',label='8 cm',markevery=mkevy)
    ax[3][0].plot(ta.index[:idx_im][::mkevy].values, ta['tmp3'][:idx_im][::mkevy].values, '-' ,color='pink',linewidth=lw,markersize=ms           ,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='13cm',markevery=mkevy)
    ax[3][0].plot(ta.index[:idx_im][::mkevy].values, ta['tmp4'][:idx_im][::mkevy].values, '-' ,color='gold',linewidth=lw,markersize=ms           ,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='20cm',markevery=mkevy)
    ax[3][0].plot(ta.index[:idx_im][::mkevy].values, ta['tmp5'][:idx_im][::mkevy].values, '-' ,color='lightgreen',linewidth=lw,markersize=ms           ,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='28cm',markevery=mkevy)
    ax[3][0].plot(ta.index[:idx_im][::mkevy].values, ta['tmp6'][:idx_im][::mkevy].values, '-' ,color='lightblue'  ,linewidth=lw,markerfacecolor='brown' ,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='38cm',markevery=mkevy)
    ax[3][0].plot(ta.index[:idx_im][::mkevy].values, ta['tmp7'][:idx_im][::mkevy].values, '-' ,color='cyan' ,linewidth=lw,markerfacecolor='yellow',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='yellow',label='48cm',markevery=mkevy)
    #ax[3][0].plot(ta.index[:idx_im][::mkevy].values, ta['tmp8'][:idx_im][::mkevy].values, '-' ,color='royalblue',linewidth=lw,markerfacecolor='orange',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='orange',label='70cm',markevery=mkevy)
    ax[3][0].plot(ta.index[:idx_im][::mkevy].values, ta['tmp9'][:idx_im][::mkevy].values, '-' ,color='darkblue'   ,linewidth=lw,markerfacecolor='grey'  ,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='grey',label='85cm',markevery=mkevy)
    ax[3][0].set_ylim([4,45])
    
    mkevy=24
    
    ax[4][0].plot(ta.index[:idx_im][::mkevy], ta['mmo0'][:idx_im][::mkevy], '-',color='maroon',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='2 cm',markevery=mkevy)
    ax[4][0].plot(ta.index[:idx_im][::mkevy], ta['mmo1'][:idx_im][::mkevy], '-',color='olive',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='5 cm',markevery=mkevy)
    ax[4][0].plot(ta.index[:idx_im][::mkevy], ta['mmo2'][:idx_im][::mkevy], '-',color='peru',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='b',label='8 cm',markevery=mkevy)
    ax[4][0].plot(ta.index[:idx_im][::mkevy], ta['mmo3'][:idx_im][::mkevy], '-',color='pink',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='13cm',markevery=mkevy)
    ax[4][0].plot(ta.index[:idx_im][::mkevy], ta['mmo4'][:idx_im][::mkevy], '-',color='gold',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='20cm',markevery=mkevy)
    ax[4][0].plot(ta.index[:idx_im][::mkevy], ta['mmo5'][:idx_im][::mkevy], '-',color='lightgreen',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='28cm',markevery=mkevy)
    ax[4][0].plot(ta.index[:idx_im][::mkevy], ta['mmo6'][:idx_im][::mkevy], '-' ,color='lightblue',linewidth=lw ,markerfacecolor='brown' ,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='38cm',markevery=mkevy)
    ax[4][0].plot(ta.index[:idx_im][::mkevy], ta['mmo7'][:idx_im][::mkevy], '-' ,color='cyan',linewidth=lw, markerfacecolor='yellow' ,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='yellow',label='48cm',markevery=mkevy)
    ax[4][0].plot(ta.index[:idx_im][::mkevy], ta['mmo8'][:idx_im][::mkevy], '-' ,color='royalblue',linewidth=lw,markerfacecolor='crimson' ,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='crimson',label='70cm',markevery=mkevy)
    ax[4][0].plot(ta.index[:idx_im][::mkevy], ta['mmo9'][:idx_im][::mkevy], '-' ,color='darkblue',linewidth=lw,markerfacecolor='pink' ,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='pink',label='85cm',markevery=mkevy)
    ax[4][0].set_ylim([-0.1,0.8])
    
    ax[5][0].plot(ta.index[:idx_im], ta['ec0'][:idx_im]/1000., '-',color='maroon',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='5 cm')
    ax[5][0].plot(ta.index[:idx_im], ta['ec2'][:idx_im]/1000., '-',color='royalblue',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='60cm')
    ax[5][0].set_ylim([-0.2,1.7])
    
    ax[6][0].plot(daily_data_manual.index[:idx_settlement], daily_data_manual['settlement_mm'][:idx_settlement]/10, '-',color='maroon',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='5 cm')
    ax[6][0].set_ylim([-0.1,10.1])
    
    
    ax[0][0].set_ylabel('DAILY\nACCUMULATED\nRAINFALL (mm)', fontsize=y_fontsize, labelpad=10)
    ax[1][0].set_ylabel('POTENTIAL\nEVAPORATION\nRATE\n(mm/Day)', fontsize=y_fontsize, labelpad=25)
    ax[2][0].set_ylabel('WATER\nPRESSURE\n(mm)', fontsize=y_fontsize, labelpad=5)
    ax[3][0].set_ylabel('TEMPERATURE\nBELOW COLUMN\nSURFACE\n($^\circ$C)', fontsize=y_fontsize, labelpad=13)
    ax[4][0].set_ylabel('VOL. MOIST.\n CONTENT\nBELOW SOIL\nSURFACE', fontsize=y_fontsize, labelpad=7)
    ax[5][0].set_ylabel('ELECTRICAL\nCONDUCTIVITY\nBELOW SOIL\nSURFACE \n(mS/cm)', fontsize=y_fontsize, labelpad=15)
    ax[6][0].set_ylabel('SURFACE \n SETTLEMENT\n(cm)', fontsize=y_fontsize, labelpad=15)
    
    ax[0][0].set_title('(A)',x=0.04,y=0.7,fontweight='bold')
    ax[1][0].set_title('(B)',x=0.04,y=0.7,fontweight='bold')
    ax[2][0].set_title('(C)',x=0.04,y=0.7,fontweight='bold')
    ax[3][0].set_title('(D)',x=0.04,y=0.7,fontweight='bold')
    ax[4][0].set_title('(E)',x=0.04,y=0.7,fontweight='bold')
    ax[5][0].set_title('(F)',x=0.04,y=0.7,fontweight='bold')
    ax[6][0].set_title('(G)',x=0.04,y=0.7,fontweight='bold')
    ax_mo.set_title('(H)',x=0.08,y=0.93,fontweight='bold')
    ax_temp.set_title('(I)',x=0.08,y=0.93,fontweight='bold')

    ax[0][0].set_axisbelow(True)
    ax[1][0].set_axisbelow(True)
    ax[2][0].set_axisbelow(True)
    ax[3][0].set_axisbelow(True)
    ax[4][0].set_axisbelow(True)
    ax[5][0].set_axisbelow(True)
    ax[2][0].legend(bbox_to_anchor=(1.10, 0.5 ), title="(C)",loc='center', borderaxespad=0.,fontsize=10,handletextpad=0.23,labelspacing=0.22,ncol=1,columnspacing=0.4)
    ax[3][0].legend(bbox_to_anchor=(1.09, 0.1 ),title="(D,E)", loc='center', borderaxespad=0.,fontsize=10,handletextpad=0.23,labelspacing=0.22,ncol=1,columnspacing=0.4)
    #ax[4][0].legend(bbox_to_anchor=(1.09, 0.5 ), loc='center', borderaxespad=0.,fontsize=9,handletextpad=0.03,labelspacing=0.02,ncol=1,columnspacing=0.4)
    ax[5][0].legend(bbox_to_anchor=(1.09, 0.5 ),  title="(F)",loc='center', borderaxespad=0.,fontsize=10,handletextpad=0.23,labelspacing=0.22,ncol=1,columnspacing=0.4)
    
    
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
    
    ax[0][0].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[1][0].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[2][0].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[3][0].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[4][0].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[5][0].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[6][0].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax_mo.grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax_temp.grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    #ax[2].plot(ta.index, ta['su5'], 'ro',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Dielectric suction A')
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
    
    ax[6][0].xaxis.set_major_formatter(mdates.DateFormatter('%b/%d'))
    ax[6][0].set_xlabel('DATE')
    #plt.xticks(rotation=45)
    plt.show(block=False)



    xlim=[ta.index[0],ta.index[-1]]
    ax[0][0].set_xlim(xlim)
    ax[1][0].set_xlim(xlim)
    ax[2][0].set_xlim(xlim)
    ax[3][0].set_xlim(xlim)
    ax[4][0].set_xlim(xlim)
    ax[5][0].set_xlim(xlim)
    fig.savefig('figure/plot_'+sch_name+ii+'.png', format='png', dpi=100)
    plt.close()
