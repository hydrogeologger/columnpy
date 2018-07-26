# linear fitting for moisture 
dp=np.linspace(13,28,num=30)
sch_name='Marandoo_first'
sp_sch[sch_name].vw1_fit1     = np.polyfit(sp_sch[sch_name].df['vw_1'],sp_sch[sch_name].df ['sat_scale1'],1)
sp_sch[sch_name].vw1_fit1_str = 'y = '+"{0:0.3f}".format( sp_sch[sch_name].vw1_fit1[0]  ) + ' x ' + "{0:0.2f}".format( sp_sch[sch_name].vw1_fit1[1]  )
sp_sch[sch_name].vw1_fit2     = np.polyfit(sp_sch[sch_name].df['vw_1'],sp_sch[sch_name].df ['sat_scale1'],2)
sp_sch[sch_name].vw1_fit_twopoint=[14.7,26.5,2.5]
sp_sch[sch_name].vw1_dp= (dp**sp_sch[sch_name].vw1_fit_twopoint[2]-sp_sch[sch_name].vw1_fit_twopoint[0]**sp_sch[sch_name].vw1_fit_twopoint[2])/(sp_sch[sch_name].vw1_fit_twopoint[1]**sp_sch[sch_name].vw1_fit_twopoint[2]-sp_sch[sch_name].vw1_fit_twopoint[0]**sp_sch[sch_name].vw1_fit_twopoint[2])
sp_sch[sch_name].vw1_text='y = (x$^{2.5}$-14.7$^{2.5}$)/(26.5$^{2.5}$-14.7$^{2.5}$)'

sp_sch[sch_name].vw2_fit1     = np.polyfit(sp_sch[sch_name].df['vw_2'],sp_sch[sch_name].df ['sat_scale2'],1)
sp_sch[sch_name].vw2_fit1_str = 'y = '+"{0:0.3f}".format( sp_sch[sch_name].vw2_fit1[0]  ) + ' x ' + "{0:0.2f}".format( sp_sch[sch_name].vw2_fit1[1]  )
sp_sch[sch_name].vw2_fit2     = np.polyfit(sp_sch[sch_name].df['vw_2'],sp_sch[sch_name].df ['sat_scale2'],2)
sp_sch[sch_name].vw2_fit_twopoint=[17.8,27.0,2.5]
sp_sch[sch_name].vw2_dp= (dp**sp_sch[sch_name].vw2_fit_twopoint[2]-sp_sch[sch_name].vw2_fit_twopoint[0]**sp_sch[sch_name].vw2_fit_twopoint[2])/(sp_sch[sch_name].vw2_fit_twopoint[1]**sp_sch[sch_name].vw2_fit_twopoint[2]-sp_sch[sch_name].vw2_fit_twopoint[0]**sp_sch[sch_name].vw2_fit_twopoint[2])
sp_sch[sch_name].vw2_text='y = (x$^{2.5}$-'+ "{0:0.1f}".format(sp_sch[sch_name].vw2_fit_twopoint[0])+'$^{2.5}$)/('  + "{0:0.1f}".format(sp_sch[sch_name].vw2_fit_twopoint[1]) +'$^{2.5}$-' + "{0:0.1f}".format(sp_sch[sch_name].vw2_fit_twopoint[0]) +'$^{2.5}$)'

sp_sch[sch_name].vw3_fit1     = np.polyfit(sp_sch[sch_name].df['vw_3'],sp_sch[sch_name].df ['sat_scale3'],1)
sp_sch[sch_name].vw3_fit1_str = 'y = '+"{0:0.3f}".format( sp_sch[sch_name].vw3_fit1[0]  ) + ' x ' + "{0:0.1f}".format( sp_sch[sch_name].vw3_fit1[1]  )
sp_sch[sch_name].vw3_fit2     = np.polyfit(sp_sch[sch_name].df['vw_3'],sp_sch[sch_name].df ['sat_scale3'],2)
sp_sch[sch_name].vw3_fit_twopoint=[16,27.0,2.5]
sp_sch[sch_name].vw3_dp= (dp**sp_sch[sch_name].vw3_fit_twopoint[2]-sp_sch[sch_name].vw3_fit_twopoint[0]**sp_sch[sch_name].vw3_fit_twopoint[2])/(sp_sch[sch_name].vw3_fit_twopoint[1]**sp_sch[sch_name].vw3_fit_twopoint[2]-sp_sch[sch_name].vw3_fit_twopoint[0]**sp_sch[sch_name].vw3_fit_twopoint[2])
sp_sch[sch_name].vw3_text='y = (x$^{2.5}$-'+ "{0:0.1f}".format(sp_sch[sch_name].vw3_fit_twopoint[0])+'$^{2.5}$)/('  + "{0:0.1f}".format(sp_sch[sch_name].vw3_fit_twopoint[1]) +'$^{2.5}$-' + "{0:0.1f}".format(sp_sch[sch_name].vw3_fit_twopoint[0]) +'$^{2.5}$)'

sch_name='Marandoo_third'
sp_sch[sch_name].vw1_fit1     = np.polyfit(sp_sch[sch_name].df['vw_1'],sp_sch[sch_name].df ['sat_scale1'],1)
sp_sch[sch_name].vw1_fit1_str = 'y = '+"{0:0.3f}".format( sp_sch[sch_name].vw1_fit1[0]  ) + ' x ' + "{0:0.2f}".format( sp_sch[sch_name].vw1_fit1[1]  )
sp_sch[sch_name].vw1_fit2     = np.polyfit(sp_sch[sch_name].df['vw_1'],sp_sch[sch_name].df ['sat_scale1'],2)
sp_sch[sch_name].vw1_fit_twopoint=[16,26.0,2.5]
sp_sch[sch_name].vw1_dp= (dp**sp_sch[sch_name].vw1_fit_twopoint[2]-sp_sch[sch_name].vw1_fit_twopoint[0]**sp_sch[sch_name].vw1_fit_twopoint[2])/(sp_sch[sch_name].vw1_fit_twopoint[1]**sp_sch[sch_name].vw1_fit_twopoint[2]-sp_sch[sch_name].vw1_fit_twopoint[0]**sp_sch[sch_name].vw1_fit_twopoint[2])
sp_sch[sch_name].vw1_text='y = (x$^{2.5}$-'+ "{0:0.1f}".format(sp_sch[sch_name].vw1_fit_twopoint[0])+'$^{2.5}$)/('  + "{0:0.1f}".format(sp_sch[sch_name].vw1_fit_twopoint[1]) +'$^{2.5}$-' + "{0:0.1f}".format(sp_sch[sch_name].vw1_fit_twopoint[0]) +'$^{2.5}$)'

sch_name='Marandoo_second'
sp_sch[sch_name].vw2_fit1     = np.polyfit(sp_sch[sch_name].df['vw_2'],sp_sch[sch_name].df ['sat_scale2'],1)
sp_sch[sch_name].vw2_fit1_str = 'y = '+"{0:0.3f}".format( sp_sch[sch_name].vw2_fit1[0]  ) + ' x ' + "{0:0.2f}".format( sp_sch[sch_name].vw2_fit1[1]  )
sp_sch[sch_name].vw2_fit2     = np.polyfit(sp_sch[sch_name].df['vw_2'],sp_sch[sch_name].df ['sat_scale2'],2)
sp_sch[sch_name].vw2_fit_twopoint=[18,27.0,2.5]
sp_sch[sch_name].vw2_dp= (dp**sp_sch[sch_name].vw2_fit_twopoint[2]-sp_sch[sch_name].vw2_fit_twopoint[0]**sp_sch[sch_name].vw2_fit_twopoint[2])/(sp_sch[sch_name].vw2_fit_twopoint[1]**sp_sch[sch_name].vw2_fit_twopoint[2]-sp_sch[sch_name].vw2_fit_twopoint[0]**sp_sch[sch_name].vw2_fit_twopoint[2])
sp_sch[sch_name].vw2_text='y = (x$^{2.5}$-'+ "{0:0.1f}".format(sp_sch[sch_name].vw2_fit_twopoint[0])+'$^{2.5}$)/('  + "{0:0.1f}".format(sp_sch[sch_name].vw2_fit_twopoint[1]) +'$^{2.5}$-' + "{0:0.1f}".format(sp_sch[sch_name].vw2_fit_twopoint[0]) +'$^{2.5}$)'

sp_sch[sch_name].vw3_fit1     = np.polyfit(sp_sch[sch_name].df['vw_3'],sp_sch[sch_name].df ['sat_scale3'],1)
sp_sch[sch_name].vw3_fit1_str = 'y = '+"{0:0.3f}".format( sp_sch[sch_name].vw3_fit1[0]  ) + ' x ' + "{0:0.2f}".format( sp_sch[sch_name].vw3_fit1[1]  )
sp_sch[sch_name].vw3_fit2     = np.polyfit(sp_sch[sch_name].df['vw_3'],sp_sch[sch_name].df ['sat_scale3'],2)
sp_sch[sch_name].vw3_fit_twopoint=[18.5,25.0,2.5]
sp_sch[sch_name].vw3_dp= (dp**sp_sch[sch_name].vw3_fit_twopoint[2]-sp_sch[sch_name].vw3_fit_twopoint[0]**sp_sch[sch_name].vw3_fit_twopoint[2])/(sp_sch[sch_name].vw3_fit_twopoint[1]**sp_sch[sch_name].vw3_fit_twopoint[2]-sp_sch[sch_name].vw3_fit_twopoint[0]**sp_sch[sch_name].vw3_fit_twopoint[2])
sp_sch[sch_name].vw3_text='y = (x$^{2.5}$-'+ "{0:0.1f}".format(sp_sch[sch_name].vw3_fit_twopoint[0])+'$^{2.5}$)/('  + "{0:0.1f}".format(sp_sch[sch_name].vw3_fit_twopoint[1]) +'$^{2.5}$-' + "{0:0.1f}".format(sp_sch[sch_name].vw3_fit_twopoint[0]) +'$^{2.5}$)'

        



plot_moisture_calibration=True
if plot_moisture_calibration:
    params = {'legend.fontsize': 'x-large',
              'figure.figsize': (10, 5),
             'axes.labelsize': 11,
             'axes.titlesize':'11',
             'xtick.labelsize':'11',
             'ytick.labelsize':'11',
             'font.weight':'bold',
             'axes.labelweight':'bold'}

    #         'axes.grid':'linewidth=grid_width,color = '0.5''}
    #         'linewidth':lw,'markers.size':ms,'markers.edgewidth':mew}
    pylab.rcParams.update(params)
    
    lw=2
    ms=6
    mew=2
    grid_width=2
    y_fontsize=11
    fig, ax = plt.subplots(3,2,sharex=False,figsize=(8,9))
    fig.subplots_adjust(hspace=.10)
    fig.subplots_adjust(left=0.15, right=0.98, top=0.97, bottom=0.08)
    for i in ax:
      for j in i:
        for axis in ['top','bottom','left','right']:
          j.spines[axis].set_linewidth(2)

    
    sch_name='Marandoo_first'
    ax[0][0].plot(sp_sch[sch_name].df['vw_1'], sp_sch[sch_name].df ['sat_scale1'],   'o',mfc='none' ,markeredgecolor='r',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Experiment',markevery=2) 
    ax[0][0].plot(dp, sp_sch[sch_name].vw1_fit1[0]*dp+sp_sch[sch_name].vw1_fit1[1],color='r',linewidth=lw,label=sp_sch[sch_name].vw1_fit1_str) 
    #ax[0][0].plot(dp, sp_sch[sch_name].vw1_fit2[0]*dp**2+sp_sch[sch_name].vw1_fit2[1]*dp+sp_sch[sch_name].vw1_fit2[2],color='k',linewidth=lw,label=sp_sch[sch_name].vw1_fit1_str) 
    ax[0][0].plot(dp, sp_sch[sch_name].vw1_dp  ,color='r',linewidth=lw,label=sp_sch[sch_name].vw1_text,linestyle='--') 


    ax[0][1].plot(sp_sch[sch_name].df['vw_2'],sp_sch[sch_name].df ['sat_scale2'],    's',mfc='none' ,markeredgecolor='g',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Experiment',markevery=2) 
    ax[0][1].plot(dp, sp_sch[sch_name].vw2_fit1[0]*dp+sp_sch[sch_name].vw2_fit1[1],color='g',linewidth=lw,label=sp_sch[sch_name].vw2_fit1_str) 
    #ax[0][1].plot(dp, sp_sch[sch_name].vw2_fit2[0]*dp**2+sp_sch[sch_name].vw2_fit2[1]*dp+sp_sch[sch_name].vw2_fit2[2],color='k',linewidth=lw,label=sp_sch[sch_name].vw2_fit1_str) 
    ax[0][1].plot(dp, sp_sch[sch_name].vw2_dp,color='g',linewidth=lw,label=sp_sch[sch_name].vw2_text,linestyle='--') 

    ax[1][0].plot(sp_sch[sch_name].df['vw_3'],sp_sch[sch_name].df ['sat_scale3'],    'v',mfc='none' ,markeredgecolor='c',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Experiment',markevery=2) 
    ax[1][0].plot(dp, sp_sch[sch_name].vw3_fit1[0]*dp+sp_sch[sch_name].vw3_fit1[1],color='c',linewidth=lw,label=sp_sch[sch_name].vw3_fit1_str) 
    ax[1][0].plot(dp, sp_sch[sch_name].vw3_dp,color='c',linewidth=lw,label=sp_sch[sch_name].vw3_text,linestyle='--') 

    sch_name='Marandoo_third'
    ax[1][1].plot(sp_sch[sch_name].df['vw_1'],sp_sch[sch_name].df ['sat_scale1'],    'x',mfc='none' ,markeredgecolor='brown',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Experiment',markevery=2) 
    ax[1][1].plot(dp, sp_sch[sch_name].vw1_fit1[0]*dp+sp_sch[sch_name].vw1_fit1[1],color='brown',linewidth=lw,label=sp_sch[sch_name].vw1_fit1_str) 
    ax[1][1].plot(dp, sp_sch[sch_name].vw1_dp,color='brown',linewidth=lw,label=sp_sch[sch_name].vw1_text,linestyle='--') 

    sch_name='Marandoo_second'
    ax[2][0].plot(sp_sch[sch_name].df['vw_2'],sp_sch[sch_name].df ['sat_scale2'],    '^',mfc='none' ,markeredgecolor='k',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Experiment',markevery=2) 
    ax[2][0].plot(dp, sp_sch[sch_name].vw2_fit1[0]*dp+sp_sch[sch_name].vw2_fit1[1],color='k',linewidth=lw,label=sp_sch[sch_name].vw2_fit1_str) 
    ax[2][0].plot(dp, sp_sch[sch_name].vw2_dp,color='k',linewidth=lw,label=sp_sch[sch_name].vw2_text,linestyle='--') 

    ax[2][1].plot(sp_sch[sch_name].df['vw_3'],sp_sch[sch_name].df ['sat_scale3'],    'd',mfc='none' ,markeredgecolor='b',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Experiment',markevery=2) 
    ax[2][1].plot(dp, sp_sch[sch_name].vw3_fit1[0]*dp+sp_sch[sch_name].vw3_fit1[1],color='b',linewidth=lw,label=sp_sch[sch_name].vw3_fit1_str) 
    ax[2][1].plot(dp, sp_sch[sch_name].vw3_dp,color='b',linewidth=lw,label=sp_sch[sch_name].vw3_text,linestyle='--') 


    ax[0][0].set_title('(A) Moisture sensor 1',x=0.02,y=0.9,fontweight='bold',horizontalalignment='left')
    ax[0][1].set_title('(B) Moisture sensor 2',x=0.02,y=0.9,fontweight='bold',horizontalalignment='left')
    ax[1][0].set_title('(C) Moisture sensor 3',x=0.02,y=0.9,fontweight='bold',horizontalalignment='left')
    ax[1][1].set_title('(D) Moisture sensor 4',x=0.02,y=0.9,fontweight='bold',horizontalalignment='left')
    ax[2][0].set_title('(E) Moisture sensor 5',x=0.02,y=0.9,fontweight='bold',horizontalalignment='left')
    ax[2][1].set_title('(F) Moisture sensor 6',x=0.02,y=0.9,fontweight='bold',horizontalalignment='left')
    ax[0][0].set_ylim([-0.1,1.1])
    ax[0][1].set_ylim([-0.1,1.1])
    ax[1][0].set_ylim([-0.1,1.1])
    ax[1][1].set_ylim([-0.1,1.1])
    ax[2][0].set_ylim([-0.1,1.1])
    ax[2][1].set_ylim([-0.1,1.1])
    ax[0][0].set_xlim([13,28])
    ax[0][1].set_xlim([13,28])
    ax[1][0].set_xlim([13,28])
    ax[1][1].set_xlim([13,28])
    ax[2][0].set_xlim([13,28])
    ax[2][1].set_xlim([13,28])
    ax[0][0].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[0][1].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[1][0].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[1][1].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[2][0].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[2][1].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[0][0].set_ylabel('DEGREE OF SATURATION', fontsize=y_fontsize, labelpad=5)
    ax[1][0].set_ylabel('DEGREE OF SATURATION', fontsize=y_fontsize, labelpad=5)
    ax[2][0].set_ylabel('DEGREE OF SATURATION', fontsize=y_fontsize, labelpad=5)
    ax[2][0].set_xlabel('DIELECTRIC PERMITIVITY', fontsize=y_fontsize, labelpad=5)
    ax[2][1].set_xlabel('DIELECTRIC PERMITIVITY', fontsize=y_fontsize, labelpad=5)

    
    ax[0][0].legend(bbox_to_anchor=(.02  , 0.9 ), loc=2, borderaxespad=0.,fontsize=8,handletextpad=0.73,labelspacing=0.35,handlelength=2.5)
    ax[0][1].legend(bbox_to_anchor=(.02  , 0.9 ), loc=2, borderaxespad=0.,fontsize=8,handletextpad=0.73,labelspacing=0.35,handlelength=2.5)
    ax[1][0].legend(bbox_to_anchor=(.02  , 0.9 ), loc=2, borderaxespad=0.,fontsize=8,handletextpad=0.73,labelspacing=0.35,handlelength=2.5)
    ax[1][1].legend(bbox_to_anchor=(.02  , 0.9 ), loc=2, borderaxespad=0.,fontsize=8,handletextpad=0.73,labelspacing=0.35,handlelength=2.5)
    ax[2][0].legend(bbox_to_anchor=(.02  , 0.9 ), loc=2, borderaxespad=0.,fontsize=8,handletextpad=0.73,labelspacing=0.35,handlelength=2.5)
    ax[2][1].legend(bbox_to_anchor=(.02  , 0.9 ), loc=2, borderaxespad=0.,fontsize=8,handletextpad=0.73,labelspacing=0.35,handlelength=2.5)
    
    
    plt.show(block=False)
    
    fig.savefig('figure/plot_moisture_calibration.png', format='png', dpi=300)
    fig.savefig('figure/plot_moisture_calibration_600.png', format='png', dpi=600)
    sp_sch["Marandoo_first"].df.to_csv("output_data/Marandoo_first.csv")
    plt.close()  # it is all caused by pywafo. 
    
    

