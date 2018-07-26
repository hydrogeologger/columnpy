## linear fitting for moisture 
#dp=np.linspace(sp_sch[sch_name].lb,sp_sch[sch_name].ub,num=30)
dp=np.linspace(0.01,1.,num=30)
#sch_name='Marandoo_first'
#sp_sch[sch_name].su1_fit= np.polyfit(sp_sch[sch_name].df['norm_t_1']  ,  np.log(sp_sch[sch_name].df ['suc_scale1'])  ,2)
#sp_sch[sch_name].su1_fit3=np.polyfit(sp_sch[sch_name].df['norm_t_1']  ,  np.log(sp_sch[sch_name].df ['suc_scale1'])  ,3)
#sp_sch[sch_name].su1_fit4=np.polyfit(sp_sch[sch_name].df['norm_t_1']  ,  np.log(sp_sch[sch_name].df ['suc_scale1'])  ,4)
#sp_sch[sch_name].su2_fit =np.polyfit(sp_sch[sch_name].df['norm_t_2']  ,  np.log(sp_sch[sch_name].df ['suc_scale2'])  ,2)
#sp_sch[sch_name].su3_fit =np.polyfit(sp_sch[sch_name].df['norm_t_3']  ,  np.log(sp_sch[sch_name].df ['suc_scale3'])  ,2)
#sch_name='Marandoo_second'
#sp_sch[sch_name].su2_fit =np.polyfit(sp_sch[sch_name].df['norm_t_2']  ,  np.log(sp_sch[sch_name].df ['suc_scale2'])  ,2)
#sp_sch[sch_name].su3_fit =np.polyfit(sp_sch[sch_name].df['norm_t_3']  ,  np.log(sp_sch[sch_name].df ['suc_scale3'])  ,2)
#sch_name='Marandoo_third'
#sp_sch[sch_name].su1_fit =np.polyfit(sp_sch[sch_name].df['norm_t_1']  ,  np.log(sp_sch[sch_name].df ['suc_scale1'])  ,2)

sch_name='Marandoo_first'
sp_sch[sch_name].su1_fit1=np.polyfit(sp_sch[sch_name].df['norm_t_1']  ,  np.log(sp_sch[sch_name].df ['suc_scale1'])  ,1)
sp_sch[sch_name].su1_fit1_str='y = '+"{0:0.2f}".format( sp_sch[sch_name].su1_fit1[0]  ) + ' x + ' + "{0:0.2f}".format( sp_sch[sch_name].su1_fit1[1]  )
sp_sch[sch_name].su2_fit1=np.polyfit(sp_sch[sch_name].df['norm_t_2']  ,  np.log(sp_sch[sch_name].df ['suc_scale2'])  ,1)
sp_sch[sch_name].su2_fit1_str='y = '+"{0:0.2f}".format( sp_sch[sch_name].su2_fit1[0]  ) + ' x + ' + "{0:0.2f}".format( sp_sch[sch_name].su2_fit1[1]  )
sp_sch[sch_name].su3_fit1=np.polyfit(sp_sch[sch_name].df['norm_t_3']  ,  np.log(sp_sch[sch_name].df ['suc_scale3'])  ,1)
sp_sch[sch_name].su3_fit1_str='y = '+"{0:0.2f}".format( sp_sch[sch_name].su3_fit1[0]  ) + ' x + ' + "{0:0.2f}".format( sp_sch[sch_name].su3_fit1[1]  )
sch_name='Marandoo_third'
sp_sch[sch_name].su1_fit1=np.polyfit(sp_sch[sch_name].df['norm_t_1']  ,  np.log(sp_sch[sch_name].df ['suc_scale1'])  ,1)
sp_sch[sch_name].su1_fit1_str='y = '+"{0:0.2f}".format( sp_sch[sch_name].su1_fit1[0]  ) + ' x + ' + "{0:0.2f}".format( sp_sch[sch_name].su1_fit1[1]  )

sch_name='Marandoo_second'
sp_sch[sch_name].su2_fit1=np.polyfit(sp_sch[sch_name].df['norm_t_2']  ,  np.log(sp_sch[sch_name].df ['suc_scale2'])  ,1)
sp_sch[sch_name].su2_fit1_str='y = '+"{0:0.2f}".format( sp_sch[sch_name].su2_fit1[0]  ) + ' x + ' + "{0:0.2f}".format( sp_sch[sch_name].su2_fit1[1]  )
sp_sch[sch_name].su3_fit1=np.polyfit(sp_sch[sch_name].df['norm_t_3']  ,  np.log(sp_sch[sch_name].df ['suc_scale3'])  ,1)
sp_sch[sch_name].su3_fit1_str='y = '+"{0:0.2f}".format( sp_sch[sch_name].su3_fit1[0]  ) + ' x + ' + "{0:0.2f}".format( sp_sch[sch_name].su3_fit1[1]  )
        



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
    fig.subplots_adjust(hspace=.12)
    fig.subplots_adjust(left=0.15, right=0.98, top=0.97, bottom=0.08)
    for i in ax:
      for j in i:
        for axis in ['top','bottom','left','right']:
          j.spines[axis].set_linewidth(4)

    
    sch_name='Marandoo_first'
    #aa=1.e-10
    #aa=20.
    #aa=-20.
    #aa=-1.5
    #aa=-2.5
    #aa=-2.9
    #aa=-3.0
    nonlinear_str='y = -1.5(x$^{-0.5}$-10)'
    #$e^{\sin(\omega\phi)}$
    aa=-0.5
    bb=0.01
    bb=0.01
    ax[0][0].plot(sp_sch[sch_name].df['norm_t_1'], np.log(sp_sch[sch_name].df ['suc_scale1']),   'o',mfc='none' ,markeredgecolor='r',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Experiment',markevery=2) 
    #sp_sch[sch_name].su1_fit[1]=25.0
    #ax[0][0].plot(dp, sp_sch[sch_name].su1_fit[0]*dp**2+sp_sch[sch_name].su1_fit[1]*dp+sp_sch[sch_name].su1_fit[2],color='r',linewidth=lw,label='bb') 
    ax[0][0].plot(dp, sp_sch[sch_name].su1_fit1[0]*dp+sp_sch[sch_name].su1_fit1[1],color='r',linewidth=lw,label=sp_sch[sch_name].su1_fit1_str) 
    #ax[0][0].plot(dp, sp_sch[sch_name].su1_fit3[0]*dp**3+sp_sch[sch_name].su1_fit3[1]*dp**2+sp_sch[sch_name].su1_fit3[2]*dp+sp_sch[sch_name].su1_fit3[3],color='r',linewidth=lw,label='bb') 
    #ax[0][0].plot(dp, sp_sch[sch_name].su1_fit4[0]*dp**4+sp_sch[sch_name].su1_fit4[1]*dp**3+sp_sch[sch_name].su1_fit4[2]*dp**2+sp_sch[sch_name].su1_fit4[3]*dp+sp_sch[sch_name].su1_fit4[4],color='r',linewidth=lw,label='bb') 
    #ax[0][0].plot(dp, (dp**aa-bb**aa)/(1.**aa-bb**aa)*13.5,color='r',linewidth=lw,label='Non-linear', linestyle='--')
    ax[0][0].plot(dp, -1.5*(dp**aa-10),color='r',linewidth=lw,label=nonlinear_str, linestyle='--')

    ax[0][1].plot(sp_sch[sch_name].df['norm_t_2'],np.log(sp_sch[sch_name].df ['suc_scale2']),    's',mfc='none' ,markeredgecolor='g',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Experiment',markevery=2) 
    #ax[0][1].plot(dp, sp_sch[sch_name].vw2_fit_a*dp+sp_sch[sch_name].vw2_fit_b,color='g',linewidth=lw,label='bb') 
    ax[0][1].plot(dp, sp_sch[sch_name].su2_fit1[0]*dp+sp_sch[sch_name].su2_fit1[1],color='g',linewidth=lw,label=sp_sch[sch_name].su2_fit1_str) 
    ax[0][1].plot(dp, (dp**aa-bb**aa)/(1.**aa-bb**aa)*13.5,color='g',linewidth=lw,label=nonlinear_str, linestyle='--')

    ax[1][0].plot(sp_sch[sch_name].df['norm_t_3'],np.log(sp_sch[sch_name].df ['suc_scale3']),    'v',mfc='none' ,markeredgecolor='c',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Experiment',markevery=2) 
    ax[1][0].plot(dp, sp_sch[sch_name].su3_fit1[0]*dp+sp_sch[sch_name].su3_fit1[1],color='c',linewidth=lw,label=sp_sch[sch_name].su3_fit1_str) 
    ax[1][0].plot(dp, (dp**aa-bb**aa)/(1.**aa-bb**aa)*13.5,color='c',linewidth=lw,label=nonlinear_str, linestyle='--')

    #ax[1][0].plot(dp, sp_sch[sch_name].vw3_fit_a*dp+sp_sch[sch_name].vw3_fit_b,color='c',linewidth=lw,label='bb') 
    sch_name='Marandoo_third'
    ax[1][1].plot(sp_sch[sch_name].df['norm_t_1'],np.log(sp_sch[sch_name].df ['suc_scale1']),    'x',mfc='none' ,markeredgecolor='brown',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Experiment',markevery=2) 
    ax[1][1].plot(dp, sp_sch[sch_name].su1_fit1[0]*dp+sp_sch[sch_name].su1_fit1[1],color='brown',linewidth=lw,label=sp_sch[sch_name].su1_fit1_str) 
    ax[1][1].plot(dp, (dp**aa-bb**aa)/(1.**aa-bb**aa)*13.5,color='brown',linewidth=lw,label=nonlinear_str, linestyle='--')

    #ax[1][1].plot(dp, sp_sch[sch_name].vw1_fit_a*dp+sp_sch[sch_name].vw1_fit_b,color='brown',linewidth=lw,label='bb') 
    sch_name='Marandoo_second'
    ax[2][0].plot(sp_sch[sch_name].df['norm_t_2'],np.log(sp_sch[sch_name].df ['suc_scale2']),    '^',mfc='none' ,markeredgecolor='k',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Experiment',markevery=2) 
    ax[2][0].plot(dp, sp_sch[sch_name].su2_fit1[0]*dp+sp_sch[sch_name].su2_fit1[1],color='k',linewidth=lw,label=sp_sch[sch_name].su2_fit1_str) 
    ax[2][0].plot(dp, (dp**aa-bb**aa)/(1.**aa-bb**aa)*13.5,color='k',linewidth=lw,label=nonlinear_str, linestyle='--')
    #ax[2][0].plot(dp, sp_sch[sch_name].vw2_fit_a*dp+sp_sch[sch_name].vw2_fit_b,color='k',linewidth=lw,label='bb') 
    ax[2][1].plot(sp_sch[sch_name].df['norm_t_3'],np.log(sp_sch[sch_name].df ['suc_scale3']),    'd',mfc='none' ,markeredgecolor='b',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Experiment',markevery=2) 
    ax[2][1].plot(dp, sp_sch[sch_name].su3_fit1[0]*dp+sp_sch[sch_name].su3_fit1[1],color='b',linewidth=lw,label=sp_sch[sch_name].su3_fit1_str) 
    #ax[2][1].plot(dp, (dp**aa-bb**aa)/(1.**aa-bb**aa)*13.5,color='b',linewidth=lw,label='non-linear', linestyle='--')
    ax[2][1].plot(dp, (dp**aa-10)/(-9)*13.5,color='b',linewidth=lw,label=nonlinear_str, linestyle='--')
    #ax[2][1].plot(dp, sp_sch[sch_name].vw3_fit_a*dp+sp_sch[sch_name].vw3_fit_b,color='b',linewidth=lw,label='bb') 

    ax[0][0].set_title('(A) Suction sensor 1',x=0.02,y=0.9,fontweight='bold',horizontalalignment='left')
    ax[0][1].set_title('(B) Suction sensor 2',x=0.02,y=0.9,fontweight='bold',horizontalalignment='left')
    ax[1][0].set_title('(C) Suction sensor 3',x=0.02,y=0.9,fontweight='bold',horizontalalignment='left')
    ax[1][1].set_title('(D) Suction sensor 4',x=0.02,y=0.9,fontweight='bold',horizontalalignment='left')
    ax[2][0].set_title('(E) Suction sensor 5',x=0.02,y=0.9,fontweight='bold',horizontalalignment='left')
    ax[2][1].set_title('(F) Suction sensor 6',x=0.02,y=0.9,fontweight='bold',horizontalalignment='left')
    ax[0][0].set_xlim([-0.1,1.1])
    ax[0][1].set_xlim([-0.1,1.1])
    ax[1][0].set_xlim([-0.1,1.1])
    ax[1][1].set_xlim([-0.1,1.1])
    ax[2][0].set_xlim([-0.1,1.1])
    ax[2][1].set_xlim([-0.1,1.1])
    ax[0][0].set_ylim([-1,15.9])
    ax[0][1].set_ylim([-1,15.9])
    ax[1][0].set_ylim([-1,15.9])
    ax[1][1].set_ylim([-1,15.9])
    ax[2][0].set_ylim([-1,15.9])
    ax[2][1].set_ylim([-1,15.9])
    ax[0][0].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[0][1].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[1][0].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[1][1].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[2][0].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[2][1].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    
    ax[0][0].set_ylabel('ln(SUCTION) (kPa)', fontsize=y_fontsize, labelpad=20)
    ax[1][0].set_ylabel('ln(SUCTION) (kPa)', fontsize=y_fontsize, labelpad=20)
    ax[2][0].set_ylabel('ln(SUCTION) (kPa)', fontsize=y_fontsize, labelpad=20)
    ax[2][0].set_xlabel('NORM. RISE OF TEMP.', fontsize=y_fontsize, labelpad=20)
    ax[2][1].set_xlabel('NORM. RISE OF TEMP.', fontsize=y_fontsize, labelpad=20)

    ax[0][0].legend(bbox_to_anchor=(.4  , 0.3 ), loc=2, borderaxespad=0.,fontsize=18,handletextpad=0.73,labelspacing=0.35)
    ax[0][1].legend(bbox_to_anchor=(.4  , 0.3 ), loc=2, borderaxespad=0.,fontsize=18,handletextpad=0.73,labelspacing=0.35)
    ax[1][0].legend(bbox_to_anchor=(.4  , 0.3 ), loc=2, borderaxespad=0.,fontsize=18,handletextpad=0.73,labelspacing=0.35)
    ax[1][1].legend(bbox_to_anchor=(.4  , 0.3 ), loc=2, borderaxespad=0.,fontsize=18,handletextpad=0.73,labelspacing=0.35)
    ax[2][0].legend(bbox_to_anchor=(.4  , 0.3 ), loc=2, borderaxespad=0.,fontsize=18,handletextpad=0.73,labelspacing=0.35)
    ax[2][1].legend(bbox_to_anchor=(.4  , 0.3 ), loc=2, borderaxespad=0.,fontsize=18,handletextpad=0.73,labelspacing=0.35)

    
    plt.show(block=False)
    
    fig.savefig('figure/plot_suction_calibration_normalised.png', format='png', dpi=300)
    plt.close()  # it is all caused by pywafo. 
    
    
#sp_sch[sch_name].df['suc_commercial']=constants.swcc_reverse_fredlund_xing_1994(vwc=sp_sch[sch_name].df.sat_commercial*sp_sch[sch_name].por,por=0.5,
#        nf=0.9311,mf=0.1229,hr=238968.16,af=2.7090)
#
#
#
#
#[vwc_fred_xing,suction_fred_xing_kpa]=constants.swcc_fredlund_xing_1994(plot=True,por=0.5,nf=0.9311,mf=0.1229,hr=238968.16,af=2.7090)




