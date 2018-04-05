# linear fitting for moisture 
dp=np.linspace(13,28,num=30)
sch_name='Marandoo_first'
sp_sch[sch_name].vw1_fit_a,sp_sch[sch_name].vw1_fit_b=np.polyfit(sp_sch[sch_name].df['vw_1'],sp_sch[sch_name].df ['sat_scale1'],1)
sp_sch[sch_name].vw2_fit_a,sp_sch[sch_name].vw2_fit_b=np.polyfit(sp_sch[sch_name].df['vw_2'],sp_sch[sch_name].df ['sat_scale2'],1)
sp_sch[sch_name].vw3_fit_a,sp_sch[sch_name].vw3_fit_b=np.polyfit(sp_sch[sch_name].df['vw_3'],sp_sch[sch_name].df ['sat_scale3'],1)
sch_name='Marandoo_second'
sp_sch[sch_name].vw2_fit_a,sp_sch[sch_name].vw2_fit_b=np.polyfit(sp_sch[sch_name].df['vw_2'],sp_sch[sch_name].df ['sat_scale2'],1)
sp_sch[sch_name].vw3_fit_a,sp_sch[sch_name].vw3_fit_b=np.polyfit(sp_sch[sch_name].df['vw_3'],sp_sch[sch_name].df ['sat_scale3'],1)
sch_name='Marandoo_third'
sp_sch[sch_name].vw1_fit_a,sp_sch[sch_name].vw1_fit_b=np.polyfit(sp_sch[sch_name].df['vw_1'],sp_sch[sch_name].df ['sat_scale1'],1)

        



plot_moisture_calibration=True
if plot_moisture_calibration:
    params = {'legend.fontsize': 'x-large',
              'figure.figsize': (10, 5),
             'axes.labelsize': 22,
             'axes.titlesize':'22',
             'xtick.labelsize':'22',
             'ytick.labelsize':'22'}
    #         'axes.grid':'linewidth=grid_width,color = '0.5''}
    #         'linewidth':lw,'markers.size':ms,'markers.edgewidth':mew}
    pylab.rcParams.update(params)
    
    lw=4
    ms=10
    mew=3.5
    grid_width=2
    y_fontsize=22
    fig, ax = plt.subplots(3,2,sharex=False,figsize=(16,18))
    fig.subplots_adjust(hspace=.10)
    fig.subplots_adjust(left=0.15, right=0.98, top=0.97, bottom=0.08)
    for i in ax:
      for j in i:
        for axis in ['top','bottom','left','right']:
          j.spines[axis].set_linewidth(4)

    
    sch_name='Marandoo_first'
    ax[0][0].plot(sp_sch[sch_name].df['vw_1'], sp_sch[sch_name].df ['sat_scale1'],   'o',mfc='none' ,markeredgecolor='r',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Dielectric moisture sensor A,\nred mud experiment 1',markevery=2) 
    ax[0][0].plot(dp, sp_sch[sch_name].vw1_fit_a*dp+sp_sch[sch_name].vw1_fit_b,color='r',linewidth=lw,label='bb') 
    ax[0][1].plot(sp_sch[sch_name].df['vw_2'],sp_sch[sch_name].df ['sat_scale2'],    's',mfc='none' ,markeredgecolor='g',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Dielectric moisture sensor A,\nred mud experiment 1',markevery=2) 
    ax[0][1].plot(dp, sp_sch[sch_name].vw2_fit_a*dp+sp_sch[sch_name].vw2_fit_b,color='g',linewidth=lw,label='bb') 
    ax[1][0].plot(sp_sch[sch_name].df['vw_3'],sp_sch[sch_name].df ['sat_scale3'],    'v',mfc='none' ,markeredgecolor='c',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Dielectric moisture sensor A,\nred mud experiment 1',markevery=2) 
    ax[1][0].plot(dp, sp_sch[sch_name].vw3_fit_a*dp+sp_sch[sch_name].vw3_fit_b,color='c',linewidth=lw,label='bb') 
    sch_name='Marandoo_third'
    ax[1][1].plot(sp_sch[sch_name].df['vw_1'],sp_sch[sch_name].df ['sat_scale1'],    'x',mfc='none' ,markeredgecolor='brown',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Dielectric moisture sensor A,\nred mud experiment 1',markevery=2) 
    ax[1][1].plot(dp, sp_sch[sch_name].vw1_fit_a*dp+sp_sch[sch_name].vw1_fit_b,color='brown',linewidth=lw,label='bb') 
    sch_name='Marandoo_second'
    ax[2][0].plot(sp_sch[sch_name].df['vw_2'],sp_sch[sch_name].df ['sat_scale2'],    '^',mfc='none' ,markeredgecolor='k',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Dielectric moisture sensor A,\nred mud experiment 1',markevery=2) 
    ax[2][0].plot(dp, sp_sch[sch_name].vw2_fit_a*dp+sp_sch[sch_name].vw2_fit_b,color='k',linewidth=lw,label='bb') 
    ax[2][1].plot(sp_sch[sch_name].df['vw_3'],sp_sch[sch_name].df ['sat_scale3'],    'd',mfc='none' ,markeredgecolor='b',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Dielectric moisture sensor A,\nred mud experiment 1',markevery=2) 
    ax[2][1].plot(dp, sp_sch[sch_name].vw3_fit_a*dp+sp_sch[sch_name].vw3_fit_b,color='b',linewidth=lw,label='bb') 


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
    ax[0][0].set_ylabel('DEGREE OF SATURATION', fontsize=y_fontsize, labelpad=20)
    ax[1][0].set_ylabel('DEGREE OF SATURATION', fontsize=y_fontsize, labelpad=20)
    ax[2][0].set_ylabel('DEGREE OF SATURATION', fontsize=y_fontsize, labelpad=20)
    ax[2][0].set_xlabel('DIELECTRIC PERMITIVITY', fontsize=y_fontsize, labelpad=20)
    ax[2][1].set_xlabel('DIELECTRIC PERMITIVITY', fontsize=y_fontsize, labelpad=20)

    
    plt.show(block=False)
    
    fig.savefig('figure/plot_moisture_calibration.png', format='png', dpi=300)
    plt.close()  # it is all caused by pywafo. 
    
    

