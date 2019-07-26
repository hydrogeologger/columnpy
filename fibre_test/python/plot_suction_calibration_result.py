## linear fitting for moisture 
#dp=np.linspace(sp_sch[sch_name].lb,sp_sch[sch_name].ub,num=30)
dp=np.linspace(0.01,1.,num=30)
#dp_rise=np.linspace(14,25,num=30)

sch_name='basin_test'
sp_sch[sch_name].sua1_fit1=np.polyfit(sp_sch[sch_name].df['norm_delta_t_sua1']  ,  np.log(sp_sch[sch_name].df ['suc_scale1'])  ,1)
#sp_sch[sch_name].su0_fit1_str='y = exp('+"{0:0.2f}".format( sp_sch[sch_name].su0_fit1[0]  ) + ' (x-0.24)/0.81 + ' + "{0:0.2f}".format( sp_sch[sch_name].su0_fit1[1]  )+')'
sp_sch[sch_name].sua1_fit1_str='y = '+"{0:0.2f}".format( sp_sch[sch_name].sua1_fit1[0]  ) + ' x + ' + "{0:0.2f}".format( sp_sch[sch_name].sua1_fit1[1]  )
sp_sch[sch_name].sua2_fit1=np.polyfit(sp_sch[sch_name].df['norm_delta_t_sua2']  ,  np.log(sp_sch[sch_name].df ['suc_scale1'])  ,1)
#sp_sch[sch_name].su1_fit1_str='y = exp('+"{0:0.2f}".format( sp_sch[sch_name].su1_fit1[0]  ) + ' (x-0.30)/0.89 + ' + "{0:0.2f}".format( sp_sch[sch_name].su1_fit1[1]  )+')'
sp_sch[sch_name].sua2_fit1_str='y = '+"{0:0.2f}".format( sp_sch[sch_name].sua2_fit1[0]  ) + ' x + ' + "{0:0.2f}".format( sp_sch[sch_name].sua2_fit1[1]  )
sp_sch[sch_name].sua3_fit1=np.polyfit(sp_sch[sch_name].df['norm_delta_t_sua3']  ,  np.log(sp_sch[sch_name].df ['suc_scale1'])  ,1)
#sp_sch[sch_name].su2_fit1_str='y = exp('+"{0:0.2f}".format( sp_sch[sch_name].su2_fit1[0]  ) + ' (x-0.34)/0.90 + ' + "{0:0.2f}".format( sp_sch[sch_name].su2_fit1[1]  )+')'
sp_sch[sch_name].sua3_fit1_str='y = '+"{0:0.2f}".format( sp_sch[sch_name].sua3_fit1[0]  ) + ' x + ' + "{0:0.2f}".format( sp_sch[sch_name].sua3_fit1[1]  )
sp_sch[sch_name].sub1_fit1=np.polyfit(sp_sch[sch_name].df['norm_delta_t_sub1']  ,  np.log(sp_sch[sch_name].df ['suc_scale2'])  ,1)
#sp_sch[sch_name].su3_fit1_str='y = exp('+"{0:0.2f}".format( sp_sch[sch_name].su3_fit1[0]  ) + ' (x-0.34)/0.82 + ' + "{0:0.2f}".format( sp_sch[sch_name].su3_fit1[1]  )+')'
sp_sch[sch_name].sub1_fit1_str='y = '+"{0:0.2f}".format( sp_sch[sch_name].sub1_fit1[0]  ) + ' x + ' + "{0:0.2f}".format( sp_sch[sch_name].sub1_fit1[1]  )
sp_sch[sch_name].sub3_fit1=np.polyfit(sp_sch[sch_name].df['norm_delta_t_sub3']  ,  np.log(sp_sch[sch_name].df ['suc_scale2'])  ,1)
#sp_sch[sch_name].su4_fit1_str='y = exp('+"{0:0.2f}".format( sp_sch[sch_name].su4_fit1[0]  ) + ' (x-0.32)/0.86 + ' + "{0:0.2f}".format( sp_sch[sch_name].su4_fit1[1]  )+')'
sp_sch[sch_name].sub3_fit1_str='y = '+"{0:0.2f}".format( sp_sch[sch_name].sub3_fit1[0]  ) + ' x + ' + "{0:0.2f}".format( sp_sch[sch_name].sub3_fit1[1]  )
sp_sch[sch_name].suc1_fit1=np.polyfit(sp_sch[sch_name].df['norm_delta_t_suc1']  ,  np.log(sp_sch[sch_name].df ['suc_scale3'])  ,1)
#sp_sch[sch_name].su5_fit1_str='y = exp('+"{0:0.2f}".format( sp_sch[sch_name].su5_fit1[0]  ) + ' (x-0.30)/0.90 + ' + "{0:0.2f}".format( sp_sch[sch_name].su5_fit1[1]  )+')'
sp_sch[sch_name].suc1_fit1_str='y = '+"{0:0.2f}".format( sp_sch[sch_name].suc1_fit1[0]  ) + ' x + ' + "{0:0.2f}".format( sp_sch[sch_name].suc1_fit1[1]  )

#sch_name='bacteria_second'
sp_sch[sch_name].suc2_fit1=np.polyfit(sp_sch[sch_name].df['norm_delta_t_suc2']  ,  np.log(sp_sch[sch_name].df ['suc_scale3'])  ,1)
#sp_sch[sch_name].su0_fit1_str='y = exp('+"{0:0.2f}".format( sp_sch[sch_name].su0_fit1[0]  ) + ' (x-0.24)/0.81 + ' + "{0:0.2f}".format( sp_sch[sch_name].su0_fit1[1]  )+')'
sp_sch[sch_name].suc2_fit1_str='y = '+"{0:0.2f}".format( sp_sch[sch_name].suc2_fit1[0]  ) + ' x + ' + "{0:0.2f}".format( sp_sch[sch_name].suc2_fit1[1]  )
sp_sch[sch_name].suc3_fit1=np.polyfit(sp_sch[sch_name].df['norm_delta_t_suc3']  ,  np.log(sp_sch[sch_name].df ['suc_scale3'])  ,1)
#sp_sch[sch_name].su1_fit1_str='y = exp('+"{0:0.2f}".format( sp_sch[sch_name].su1_fit1[0]  ) + ' (x-0.30)/0.89 + ' + "{0:0.2f}".format( sp_sch[sch_name].su1_fit1[1]  )+')'
sp_sch[sch_name].suc3_fit1_str='y = '+"{0:0.2f}".format( sp_sch[sch_name].suc3_fit1[0]  ) + ' x + ' + "{0:0.2f}".format( sp_sch[sch_name].suc3_fit1[1]  )
#sp_sch[sch_name].su2_fit1=np.polyfit(sp_sch[sch_name].df['norm_delta_t_su2']  ,  np.log(sp_sch[sch_name].df ['suc_scale1'])  ,1)
#sp_sch[sch_name].su2_fit1_str='y = exp('+"{0:0.2f}".format( sp_sch[sch_name].su2_fit1[0]  ) + ' (x-0.34)/0.90 + ' + "{0:0.2f}".format( sp_sch[sch_name].su2_fit1[1]  )+')'
#sp_sch[sch_name].su2_fit1_str='y = '+"{0:0.2f}".format( sp_sch[sch_name].su2_fit1[0]  ) + ' x + ' + "{0:0.2f}".format( sp_sch[sch_name].su2_fit1[1]  )
#sp_sch[sch_name].su3_fit1=np.polyfit(sp_sch[sch_name].df['norm_delta_t_su3']  ,  np.log(sp_sch[sch_name].df ['suc_scale2'])  ,1)
#sp_sch[sch_name].su3_fit1_str='y = exp('+"{0:0.2f}".format( sp_sch[sch_name].su3_fit1[0]  ) + ' (x-0.34)/0.82 + ' + "{0:0.2f}".format( sp_sch[sch_name].su3_fit1[1]  )+')'
#sp_sch[sch_name].su3_fit1_str='y = '+"{0:0.2f}".format( sp_sch[sch_name].su3_fit1[0]  ) + ' x + ' + "{0:0.2f}".format( sp_sch[sch_name].su3_fit1[1]  )
#sp_sch[sch_name].su4_fit1=np.polyfit(sp_sch[sch_name].df['norm_delta_t_su4']  ,  np.log(sp_sch[sch_name].df ['suc_scale2'])  ,1)
#sp_sch[sch_name].su4_fit1_str='y = exp('+"{0:0.2f}".format( sp_sch[sch_name].su4_fit1[0]  ) + ' (x-0.32)/0.86 + ' + "{0:0.2f}".format( sp_sch[sch_name].su4_fit1[1]  )+')'
#sp_sch[sch_name].su4_fit1_str='y = '+"{0:0.2f}".format( sp_sch[sch_name].su4_fit1[0]  ) + ' x + ' + "{0:0.2f}".format( sp_sch[sch_name].su4_fit1[1]  )
#sp_sch[sch_name].su5_fit1=np.polyfit(sp_sch[sch_name].df['norm_delta_t_su5']  ,  np.log(sp_sch[sch_name].df ['suc_scale2'])  ,1)
#sp_sch[sch_name].su5_fit1_str='y = exp('+"{0:0.2f}".format( sp_sch[sch_name].su5_fit1[0]  ) + ' (x-0.30)/0.90 + ' + "{0:0.2f}".format( sp_sch[sch_name].su5_fit1[1]  )+')'
#sp_sch[sch_name].su5_fit1_str='y = '+"{0:0.2f}".format( sp_sch[sch_name].su5_fit1[0]  ) + ' x + ' + "{0:0.2f}".format( sp_sch[sch_name].su5_fit1[1]  )

#sch_name='bacteria_third'
#sp_sch[sch_name].su0_fit1=np.polyfit(sp_sch[sch_name].df['norm_delta_t_su0']  ,  np.log(sp_sch[sch_name].df ['suc_scale1'])  ,1)
#sp_sch[sch_name].su0_fit1_str='y = exp('+"{0:0.2f}".format( sp_sch[sch_name].su0_fit1[0]  ) + ' (x-0.24)/0.81 + ' + "{0:0.2f}".format( sp_sch[sch_name].su0_fit1[1]  )+')'
#sp_sch[sch_name].su0_fit1_str='y = '+"{0:0.2f}".format( sp_sch[sch_name].su0_fit1[0]  ) + ' x + ' + "{0:0.2f}".format( sp_sch[sch_name].su0_fit1[1]  )
#sp_sch[sch_name].su1_fit1=np.polyfit(sp_sch[sch_name].df['norm_delta_t_su1']  ,  np.log(sp_sch[sch_name].df ['suc_scale1'])  ,1)
#sp_sch[sch_name].su1_fit1_str='y = exp('+"{0:0.2f}".format( sp_sch[sch_name].su1_fit1[0]  ) + ' (x-0.30)/0.89 + ' + "{0:0.2f}".format( sp_sch[sch_name].su1_fit1[1]  )+')'
#sp_sch[sch_name].su1_fit1_str='y = '+"{0:0.2f}".format( sp_sch[sch_name].su1_fit1[0]  ) + ' x + ' + "{0:0.2f}".format( sp_sch[sch_name].su1_fit1[1]  )
#sp_sch[sch_name].su2_fit1=np.polyfit(sp_sch[sch_name].df['norm_delta_t_su2']  ,  np.log(sp_sch[sch_name].df ['suc_scale1'])  ,1)
#sp_sch[sch_name].su2_fit1_str='y = exp('+"{0:0.2f}".format( sp_sch[sch_name].su2_fit1[0]  ) + ' (x-0.34)/0.90 + ' + "{0:0.2f}".format( sp_sch[sch_name].su2_fit1[1]  )+')'
#sp_sch[sch_name].su2_fit1_str='y = '+"{0:0.2f}".format( sp_sch[sch_name].su2_fit1[0]  ) + ' x + ' + "{0:0.2f}".format( sp_sch[sch_name].su2_fit1[1]  )
#sp_sch[sch_name].su3_fit1=np.polyfit(sp_sch[sch_name].df['norm_delta_t_su3']  ,  np.log(sp_sch[sch_name].df ['suc_scale2'])  ,1)
#sp_sch[sch_name].su3_fit1_str='y = exp('+"{0:0.2f}".format( sp_sch[sch_name].su3_fit1[0]  ) + ' (x-0.34)/0.82 + ' + "{0:0.2f}".format( sp_sch[sch_name].su3_fit1[1]  )+')'
#sp_sch[sch_name].su3_fit1_str='y = '+"{0:0.2f}".format( sp_sch[sch_name].su3_fit1[0]  ) + ' x + ' + "{0:0.2f}".format( sp_sch[sch_name].su3_fit1[1]  )
#sp_sch[sch_name].su4_fit1=np.polyfit(sp_sch[sch_name].df['norm_delta_t_su4']  ,  np.log(sp_sch[sch_name].df ['suc_scale2'])  ,1)
#sp_sch[sch_name].su4_fit1_str='y = exp('+"{0:0.2f}".format( sp_sch[sch_name].su4_fit1[0]  ) + ' (x-0.32)/0.86 + ' + "{0:0.2f}".format( sp_sch[sch_name].su4_fit1[1]  )+')'
#sp_sch[sch_name].su4_fit1_str='y = '+"{0:0.2f}".format( sp_sch[sch_name].su4_fit1[0]  ) + ' x + ' + "{0:0.2f}".format( sp_sch[sch_name].su4_fit1[1]  )
#sp_sch[sch_name].su5_fit1=np.polyfit(sp_sch[sch_name].df['norm_delta_t_su5']  ,  np.log(sp_sch[sch_name].df ['suc_scale2'])  ,1)
#sp_sch[sch_name].su5_fit1_str='y = exp('+"{0:0.2f}".format( sp_sch[sch_name].su5_fit1[0]  ) + ' (x-0.30)/0.90 + ' + "{0:0.2f}".format( sp_sch[sch_name].su5_fit1[1]  )+')'
#sp_sch[sch_name].su5_fit1_str='y = '+"{0:0.2f}".format( sp_sch[sch_name].su5_fit1[0]  ) + ' x + ' + "{0:0.2f}".format( sp_sch[sch_name].su5_fit1[1]  )

#sch_name='Marandoo_third'
#sp_sch[sch_name].su1_fit1=np.polyfit(sp_sch[sch_name].df['norm_t_1']  ,  np.log(sp_sch[sch_name].df ['suc_scale1'])  ,1)
#sp_sch[sch_name].su1_fit1_str='y = exp('+"{0:0.2f}".format( sp_sch[sch_name].su1_fit1[0]  ) + ' (x-0.8)/2.6 + ' + "{0:0.2f}".format( sp_sch[sch_name].su1_fit1[1]  )+')'
#
#sch_name='Marandoo_second'
#sp_sch[sch_name].su2_fit1=np.polyfit(sp_sch[sch_name].df['norm_t_2']  ,  np.log(sp_sch[sch_name].df ['suc_scale2'])  ,1)
#sp_sch[sch_name].su2_fit1_str='y = exp('+"{0:0.2f}".format( sp_sch[sch_name].su2_fit1[0]  ) + ' (x-0.8)/2.6 + ' + "{0:0.2f}".format( sp_sch[sch_name].su2_fit1[1]  )+')'
#sp_sch[sch_name].su3_fit1=np.polyfit(sp_sch[sch_name].df['norm_t_3']  ,  np.log(sp_sch[sch_name].df ['suc_scale3'])  ,1)
#sp_sch[sch_name].su3_fit1_str='y = exp('+"{0:0.2f}".format( sp_sch[sch_name].su3_fit1[0]  ) + ' (x-0.8)/2.6 + ' + "{0:0.2f}".format( sp_sch[sch_name].su3_fit1[1]  )+')'
        



plot_moisture_calibration=True
if plot_moisture_calibration:
    params = {'legend.fontsize': 'x-large',
              'figure.figsize': (10, 5),
             'axes.labelsize': 11,
             'axes.titlesize':'11',
             'xtick.labelsize':'11',
             'ytick.labelsize':'11'}
    #         'axes.grid':'linewidth=grid_width,color = '0.5''}
    #         'linewidth':lw,'markers.size':ms,'markers.edgewidth':mew}
    pylab.rcParams.update(params)
    
    lw=2
    ms=6
    mew=2
    grid_width=2
    y_fontsize=11
    fig, ax = plt.subplots(4,2,sharex=False,figsize=(8,9))
    fig.subplots_adjust(hspace=.10)
    fig.subplots_adjust(left=0.15, right=0.98, top=0.97, bottom=0.08)
    for i in ax:
      for j in i:
        for axis in ['top','bottom','left','right']:
          j.spines[axis].set_linewidth(2)

    
    #aa=1.e-10
    #aa=20.
    #aa=-20.
    #aa=-1.5
    #aa=-2.5
    #aa=-2.9
    #aa=-3.0
    #nonlinear_str='y = exp(-1.5(((x-0.8)/2.6)$^{-0.5}$-10))'
    #$e^{\sin(\omega\phi)}$

    sch_name='basin_test'
    ax[0][0].semilogy(sp_sch[sch_name].df['norm_delta_t_sua1'], sp_sch[sch_name].df ['suc_scale1'],   'o',mfc='none' ,markeredgecolor='r',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Basin_a',markevery=2) 
    #ax[0][0].semilogy(sp_sch[sch_name].df['su0'], sp_sch[sch_name].df ['suc_scale1'],   'o',mfc='none' ,markeredgecolor='r',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Experiment1',markevery=2) 
    #ax[0][0].plot(dp, np.exp(sp_sch[sch_name].su0_fit1[0]*dp+sp_sch[sch_name].su0_fit1[1]),color='r',linewidth=lw) 
    #ax[0][0].plot(dp_rise, np.exp(-1.5*(dp**aa-11)),color='r',linewidth=lw,label=nonlinear_str, linestyle='--')
    #ax[0][0].plot(dp, np.exp(-1.5*(dp**aa-bb)),color='r',linewidth=lw, linestyle='--')
    ax[0][0].semilogy(dp, np.exp(-1.5*(dp**aa-bb)),color='r',linewidth=lw, linestyle='--')

    ax[0][1].semilogy(sp_sch[sch_name].df['norm_delta_t_sua2'],sp_sch[sch_name].df ['suc_scale1'],    's',mfc='none' ,markeredgecolor='g',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Basin_a',markevery=2) 
    #ax[0][1].semilogy(sp_sch[sch_name].df['su1'],sp_sch[sch_name].df ['suc_scale1'],    's',mfc='none' ,markeredgecolor='r',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Experiment1',markevery=2)
    #ax[0][1].plot(dp_rise, np.exp(sp_sch[sch_name].su1_fit1[0]*dp+sp_sch[sch_name].su1_fit1[1]),color='r',linewidth=lw,label=sp_sch[sch_name].su1_fit1_str) 
    #ax[0][1].plot(dp_rise, np.exp((dp**aa-bb**aa)/(1.**aa-bb**aa)*13.5),color='r',linewidth=lw,label=nonlinear_str, linestyle='--')
    #ax[0][1].plot(dp_rise, np.exp(-1.5*(dp**aa-11)),color='r',linewidth=lw,label=nonlinear_str, linestyle='--')
    #ax[0][1].plot(dp, np.exp(-1.5*(dp**aa-bb)),color='r',linewidth=lw, linestyle='--')
    ax[0][1].semilogy(dp, np.exp(-1.5*(dp**aa-bb)),color='g',linewidth=lw, linestyle='--')

    ax[1][0].semilogy(sp_sch[sch_name].df['norm_delta_t_sua3'],sp_sch[sch_name].df ['suc_scale1'],    'v',mfc='none' ,markeredgecolor='y',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Basin_a',markevery=2) 
    #ax[1][0].semilogy(sp_sch[sch_name].df['su2'],sp_sch[sch_name].df ['suc_scale1'],    'v',mfc='none' ,markeredgecolor='r',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Experiment1',markevery=2)
    #ax[1][0].plot(dp_rise, np.exp(sp_sch[sch_name].su2_fit1[0]*dp+sp_sch[sch_name].su2_fit1[1]),color='r',linewidth=lw,label=sp_sch[sch_name].su2_fit1_str) 
    #ax[1][0].plot(dp_rise, np.exp((dp**aa-bb**aa)/(1.**aa-bb**aa)*13.5),color='r',linewidth=lw,label=nonlinear_str, linestyle='--')
    #ax[1][0].plot(dp_rise, np.exp(-1.5*(dp**aa-11)),color='r',linewidth=lw,label=nonlinear_str, linestyle='--')
    ax[1][0].semilogy(dp, np.exp(-1.5*(dp**aa-bb)),color='y',linewidth=lw, linestyle='--')    

    ax[1][1].semilogy(sp_sch[sch_name].df['norm_delta_t_sub1'], sp_sch[sch_name].df ['suc_scale2'],   'x',mfc='none' ,markeredgecolor='blue',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Basin_b',markevery=2)
    #ax[1][1].semilogy(sp_sch[sch_name].df['su3'],sp_sch[sch_name].df ['suc_scale2'],   'x',mfc='none' ,markeredgecolor='r',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Experiment1',markevery=2)
    #ax[1][1].plot(dp_rise, np.exp(sp_sch[sch_name].su3_fit1[0]*dp+sp_sch[sch_name].su3_fit1[1]),color='r',linewidth=lw,label=sp_sch[sch_name].su3_fit1_str) 
    #ax[1][1].plot(dp_rise, np.exp(-1.5*(dp**aa-11)),color='r',linewidth=lw,label=nonlinear_str, linestyle='--')
    ax[1][1].semilogy(dp, np.exp(-1.5*(dp**aa-bb)),color='blue',linewidth=lw,linestyle='--')

    ax[2][0].semilogy(sp_sch[sch_name].df['norm_delta_t_sub3'],sp_sch[sch_name].df ['suc_scale2'],    '^',mfc='none' ,markeredgecolor='gold',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Basin_b',markevery=2)       
    #ax[2][0].semilogy(sp_sch[sch_name].df['su4'],sp_sch[sch_name].df ['suc_scale2'],    '^',mfc='none' ,markeredgecolor='r',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Experiment1',markevery=2)
    #ax[2][0].plot(dp_rise, np.exp(sp_sch[sch_name].su4_fit1[0]*dp+sp_sch[sch_name].su4_fit1[1]),color='r',linewidth=lw,label=sp_sch[sch_name].su4_fit1_str) 
    #ax[2][0].plot(dp_rise, np.exp((dp**aa-bb**aa)/(1.**aa-bb**aa)*13.5),color='r',linewidth=lw,label=nonlinear_str, linestyle='--')
    #ax[2][0].plot(dp_rise, np.exp(-1.5*(dp**aa-11)),color='r',linewidth=lw,label=nonlinear_str, linestyle='--')   
    ax[2][0].semilogy(dp, np.exp(-1.5*(dp**aa-bb)),color='gold',linewidth=lw, linestyle='--') 

    ax[2][1].semilogy(sp_sch[sch_name].df['norm_delta_t_suc1'],sp_sch[sch_name].df ['suc_scale3'],    'd',mfc='none' ,markeredgecolor='black',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Basin_c',markevery=2)       
    #ax[2][0].semilogy(sp_sch[sch_name].df['su5'],sp_sch[sch_name].df ['suc_scale2'],    'd',mfc='none' ,markeredgecolor='r',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Experiment1',markevery=2)
    #ax[2][1].plot(dp_rise, np.exp(sp_sch[sch_name].su5_fit1[0]*dp+sp_sch[sch_name].su5_fit1[1]),color='r',linewidth=lw,label=sp_sch[sch_name].su5_fit1_str) 
    #ax[2][1].plot(dp_rise, np.exp((dp**aa-bb**aa)/(1.**aa-bb**aa)*13.5),color='r',linewidth=lw,label=nonlinear_str, linestyle='--')
    #ax[2][1].plot(dp_rise, np.exp(-1.5*(dp**aa-11)),color='r',linewidth=lw,label=nonlinear_str, linestyle='--')
    ax[2][1].semilogy(dp, np.exp(-1.5*(dp**aa-bb)),color='black',linewidth=lw, linestyle='--')

    #sch_name='bacteria_second'
    ax[3][0].semilogy(sp_sch[sch_name].df['norm_delta_t_suc2'],sp_sch[sch_name].df ['suc_scale3'],   'p',mfc='none' ,markeredgecolor='orange',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Basin_c',markevery=2)
    ##ax[0][0].plot(dp_rise, np.exp(sp_sch[sch_name].su0_fit1[0]*dp+sp_sch[sch_name].su0_fit1[1]),color='r',linewidth=lw,label=sp_sch[sch_name].su0_fit1_str) 
    ##ax[0][0].plot(dp_rise, np.exp(-1.5*(dp**aa-11)),color='r',linewidth=lw,label=nonlinear_str, linestyle='--')
    ax[3][0].semilogy(dp, np.exp(-1.5*(dp**aa-bb)),color='orange',linewidth=lw, linestyle='--')


 
    ax[3][1].semilogy(sp_sch[sch_name].df['norm_delta_t_suc3'],sp_sch[sch_name].df ['suc_scale3'],    '*',mfc='none' ,markeredgecolor='purple',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Basin_c',markevery=2)

    ax[3][1].semilogy(dp, np.exp(-1.5*(dp**aa-bb)),color='purple',linewidth=lw, linestyle='--')

    #ax[0][1].plot(sp_sch[sch_name].df['norm_delta_t_su1'], np.log(sp_sch[sch_name].df ['suc_scale1']),   's',mfc='none' ,markeredgecolor='g',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Experiment2',markevery=2)
    ##ax[0][1].plot(dp_rise, np.exp(sp_sch[sch_name].su1_fit1[0]*dp+sp_sch[sch_name].su1_fit1[1]),color='r',linewidth=lw,label=sp_sch[sch_name].su1_fit1_str) 
    ##ax[0][1].plot(dp_rise, np.exp((dp**aa-bb**aa)/(1.**aa-bb**aa)*13.5),color='r',linewidth=lw,label=nonlinear_str, linestyle='--')
    ##ax[0][1].plot(dp_rise, np.exp(-1.5*(dp**aa-11)),color='r',linewidth=lw,label=nonlinear_str, linestyle='--')

    #ax[1][0].semilogy(sp_sch[sch_name].df['norm_delta_t_su2'],sp_sch[sch_name].df ['suc_scale1'],    'v',mfc='none' ,markeredgecolor='g',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Experiment2',markevery=2)
    #ax[1][0].plot(sp_sch[sch_name].df['norm_delta_t_su2'], np.log(sp_sch[sch_name].df ['suc_scale1']),   'v',mfc='none' ,markeredgecolor='g',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Experiment2',markevery=2)
    ##ax[1][0].plot(dp_rise, np.exp(sp_sch[sch_name].su2_fit1[0]*dp+sp_sch[sch_name].su2_fit1[1]),color='r',linewidth=lw,label=sp_sch[sch_name].su2_fit1_str) 
    ##ax[1][0].plot(dp_rise, np.exp((dp**aa-bb**aa)/(1.**aa-bb**aa)*13.5),color='r',linewidth=lw,label=nonlinear_str, linestyle='--')
    ##ax[1][0].plot(dp_rise, np.exp(-1.5*(dp**aa-11)),color='r',linewidth=lw,label=nonlinear_str, linestyle='--')

    #ax[1][1].semilogy(sp_sch[sch_name].df['norm_delta_t_su3'], sp_sch[sch_name].df ['suc_scale2'],   'x',mfc='none' ,markeredgecolor='g',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Experiment2',markevery=2)
    #ax[1][1].plot(sp_sch[sch_name].df['norm_delta_t_su3'], np.log(sp_sch[sch_name].df ['suc_scale2']),   'x',mfc='none' ,markeredgecolor='g',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Experiment2',markevery=2)
    ##ax[1][1].plot(dp_rise, np.exp(sp_sch[sch_name].su3_fit1[0]*dp+sp_sch[sch_name].su3_fit1[1]),color='r',linewidth=lw,label=sp_sch[sch_name].su3_fit1_str) 
    ##ax[1][1].plot(dp_rise, np.exp(-1.5*(dp**aa-11)),color='r',linewidth=lw,label=nonlinear_str, linestyle='--')

    #ax[2][0].semilogy(sp_sch[sch_name].df['norm_delta_t_su4'],sp_sch[sch_name].df ['suc_scale2'],    '^',mfc='none' ,markeredgecolor='g',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Experiment2',markevery=2)
    #ax[2][0].plot(sp_sch[sch_name].df['norm_delta_t_su4'], np.log(sp_sch[sch_name].df ['suc_scale2']),   '^',mfc='none' ,markeredgecolor='g',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Experiment2',markevery=2)
    ##ax[2][0].plot(dp_rise, np.exp(sp_sch[sch_name].su4_fit1[0]*dp+sp_sch[sch_name].su4_fit1[1]),color='r',linewidth=lw,label=sp_sch[sch_name].su4_fit1_str) 
    ##ax[2][0].plot(dp_rise, np.exp((dp**aa-bb**aa)/(1.**aa-bb**aa)*13.5),color='r',linewidth=lw,label=nonlinear_str, linestyle='--')
    ##ax[2][0].plot(dp_rise, np.exp(-1.5*(dp**aa-11)),color='r',linewidth=lw,label=nonlinear_str, linestyle='--')

    #ax[2][1].semilogy(sp_sch[sch_name].df['norm_delta_t_su5'],sp_sch[sch_name].df ['suc_scale2'],    'd',mfc='none' ,markeredgecolor='g',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Experiment2',markevery=2)
    #ax[2][1].plot(sp_sch[sch_name].df['norm_delta_t_su5'], np.log(sp_sch[sch_name].df ['suc_scale2']),   'd',mfc='none' ,markeredgecolor='g',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Experiment2',markevery=2)
    ##ax[2][1].plot(dp_rise, np.exp(sp_sch[sch_name].su5_fit1[0]*dp+sp_sch[sch_name].su5_fit1[1]),color='r',linewidth=lw,label=sp_sch[sch_name].su5_fit1_str) 
    ##ax[2][1].plot(dp_rise, np.exp((dp**aa-bb**aa)/(1.**aa-bb**aa)*13.5),color='r',linewidth=lw,label=nonlinear_str, linestyle='--')
    ##ax[2][1].plot(dp_rise, np.exp(-1.5*(dp**aa-11)),color='r',linewidth=lw,label=nonlinear_str, linestyle='--')

    #sch_name='bacteria_third'
    #ax[0][0].semilogy(sp_sch[sch_name].df['norm_delta_t_su0'], sp_sch[sch_name].df ['suc_scale1'],   'o',mfc='none' ,markeredgecolor='c',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Experiment3',markevery=2)
    #ax[0][0].plot(sp_sch[sch_name].df['norm_delta_t_su0'], np.log(sp_sch[sch_name].df ['suc_scale1']),   'o',mfc='none' ,markeredgecolor='c',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Experiment3',markevery=2)
    ##ax[0][0].plot(dp_rise, np.exp(sp_sch[sch_name].su0_fit1[0]*dp+sp_sch[sch_name].su0_fit1[1]),color='r',linewidth=lw,label=sp_sch[sch_name].su0_fit1_str) 
    ##ax[0][0].plot(dp_rise, np.exp(-1.5*(dp**aa-11)),color='r',linewidth=lw,label=nonlinear_str, linestyle='--')

    #ax[0][1].semilogy(sp_sch[sch_name].df['norm_delta_t_su1'],sp_sch[sch_name].df ['suc_scale1'],    's',mfc='none' ,markeredgecolor='c',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Experiment3',markevery=2)
    #ax[0][1].plot(sp_sch[sch_name].df['norm_delta_t_su1'], np.log(sp_sch[sch_name].df ['suc_scale1']),   's',mfc='none' ,markeredgecolor='c',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Experiment3',markevery=2)
    ##ax[0][1].plot(dp_rise, np.exp(sp_sch[sch_name].su1_fit1[0]*dp+sp_sch[sch_name].su1_fit1[1]),color='r',linewidth=lw,label=sp_sch[sch_name].su1_fit1_str) 
    ##ax[0][1].plot(dp_rise, np.exp((dp**aa-bb**aa)/(1.**aa-bb**aa)*13.5),color='r',linewidth=lw,label=nonlinear_str, linestyle='--')
    ##ax[0][1].plot(dp_rise, np.exp(-1.5*(dp**aa-11)),color='r',linewidth=lw,label=nonlinear_str, linestyle='--')

    #ax[1][0].semilogy(sp_sch[sch_name].df['norm_delta_t_su2'],sp_sch[sch_name].df ['suc_scale1'],    'v',mfc='none' ,markeredgecolor='c',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Experiment3',markevery=2)
    #ax[1][0].plot(sp_sch[sch_name].df['norm_delta_t_su2'], np.log(sp_sch[sch_name].df ['suc_scale1']),   'v',mfc='none' ,markeredgecolor='c',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Experiment3',markevery=2)
    ##ax[1][0].plot(dp_rise, np.exp(sp_sch[sch_name].su2_fit1[0]*dp+sp_sch[sch_name].su2_fit1[1]),color='r',linewidth=lw,label=sp_sch[sch_name].su2_fit1_str) 
    ##ax[1][0].plot(dp_rise, np.exp((dp**aa-bb**aa)/(1.**aa-bb**aa)*13.5),color='r',linewidth=lw,label=nonlinear_str, linestyle='--')
    ##ax[1][0].plot(dp_rise, np.exp(-1.5*(dp**aa-11)),color='r',linewidth=lw,label=nonlinear_str, linestyle='--')

    #ax[1][1].semilogy(sp_sch[sch_name].df['norm_delta_t_su3'], sp_sch[sch_name].df ['suc_scale2'],   'x',mfc='none' ,markeredgecolor='c',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Experiment3',markevery=2)
    #ax[1][1].plot(sp_sch[sch_name].df['norm_delta_t_su3'], np.log(sp_sch[sch_name].df ['suc_scale2']),   'x',mfc='none' ,markeredgecolor='c',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Experiment3',markevery=2)
    ##ax[1][1].plot(dp_rise, np.exp(sp_sch[sch_name].su3_fit1[0]*dp+sp_sch[sch_name].su3_fit1[1]),color='r',linewidth=lw,label=sp_sch[sch_name].su3_fit1_str) 
    ##ax[1][1].plot(dp_rise, np.exp(-1.5*(dp**aa-11)),color='r',linewidth=lw,label=nonlinear_str, linestyle='--')

    #ax[2][0].semilogy(sp_sch[sch_name].df['norm_delta_t_su4'],sp_sch[sch_name].df ['suc_scale2'],    '^',mfc='none' ,markeredgecolor='c',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Experiment3',markevery=2)
    #ax[2][0].plot(sp_sch[sch_name].df['norm_delta_t_su4'], np.log(sp_sch[sch_name].df ['suc_scale2']),   '^',mfc='none' ,markeredgecolor='c',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Experiment3',markevery=2)
    ##ax[2][0].plot(dp_rise, np.exp(sp_sch[sch_name].su4_fit1[0]*dp+sp_sch[sch_name].su4_fit1[1]),color='r',linewidth=lw,label=sp_sch[sch_name].su4_fit1_str) 
    ##ax[2][0].plot(dp_rise, np.exp((dp**aa-bb**aa)/(1.**aa-bb**aa)*13.5),color='r',linewidth=lw,label=nonlinear_str, linestyle='--')
    ##ax[2][0].plot(dp_rise, np.exp(-1.5*(dp**aa-11)),color='r',linewidth=lw,label=nonlinear_str, linestyle='--')

    #ax[2][1].semilogy(sp_sch[sch_name].df['norm_delta_t_su5'],sp_sch[sch_name].df ['suc_scale2'],    'd',mfc='none' ,markeredgecolor='c',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Experiment3',markevery=2)
    #ax[2][1].plot(sp_sch[sch_name].df['norm_delta_t_su5'], np.log(sp_sch[sch_name].df ['suc_scale2']),   'd',mfc='none' ,markeredgecolor='c',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Experiment3',markevery=2)
    #ax[2][1].plot(dp_rise, np.exp(sp_sch[sch_name].su5_fit1[0]*dp+sp_sch[sch_name].su5_fit1[1]),color='r',linewidth=lw,label=sp_sch[sch_name].su5_fit1_str) 
    #ax[2][1].plot(dp_rise, np.exp((dp**aa-bb**aa)/(1.**aa-bb**aa)*13.5),color='r',linewidth=lw,label=nonlinear_str, linestyle='--')
    #ax[2][1].plot(dp_rise, np.exp(-1.5*(dp**aa-11)),color='r',linewidth=lw,label=nonlinear_str, linestyle='--')
    
    #sch_name='Marandoo_third'
    #ax[1][1].semilogy(sp_sch[sch_name].df['deltat_c_1'],sp_sch[sch_name].df ['suc_scale1'],    'x',mfc='none' ,markeredgecolor='brown',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Experiment',markevery=2) 
    #ax[1][1].plot(dp_rise, np.exp(sp_sch[sch_name].su1_fit1[0]*dp+sp_sch[sch_name].su1_fit1[1]),color='brown',linewidth=lw,label=sp_sch[sch_name].su1_fit1_str) 
    #ax[1][1].plot(dp_rise, np.exp((dp**aa-bb**aa)/(1.**aa-bb**aa)*13.5),color='brown',linewidth=lw,label=nonlinear_str, linestyle='--')

    #sch_name='Marandoo_second'
    #ax[2][0].semilogy(sp_sch[sch_name].df['deltat_c_2'],sp_sch[sch_name].df ['suc_scale2'],    '^',mfc='none' ,markeredgecolor='k',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Experiment',markevery=2) 
    #ax[2][0].plot(dp_rise, np.exp(sp_sch[sch_name].su2_fit1[0]*dp+sp_sch[sch_name].su2_fit1[1]),color='k',linewidth=lw,label=sp_sch[sch_name].su2_fit1_str) 
    #ax[2][0].plot(dp_rise, np.exp((dp**aa-bb**aa)/(1.**aa-bb**aa)*13.5),color='k',linewidth=lw,label=nonlinear_str, linestyle='--')

    #ax[2][1].semilogy(sp_sch[sch_name].df['deltat_c_3'],sp_sch[sch_name].df ['suc_scale3'],    'd',mfc='none' ,markeredgecolor='b',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Experiment',markevery=2) 
    #ax[2][1].plot(dp_rise, np.exp(sp_sch[sch_name].su3_fit1[0]*dp+sp_sch[sch_name].su3_fit1[1]),color='b',linewidth=lw,label=sp_sch[sch_name].su3_fit1_str) 
    #ax[2][1].plot(dp_rise, np.exp((dp**aa-10)/(-9)*13.5),color='b',linewidth=lw,label=nonlinear_str, linestyle='--')

    ax[0][0].set_title('(A) Suction sensor a1',x=0.02,y=0.9,fontweight='bold',horizontalalignment='left')
    ax[0][1].set_title('(B) Suction sensor a2',x=0.02,y=0.9,fontweight='bold',horizontalalignment='left')
    ax[1][0].set_title('(C) Suction sensor a3',x=0.02,y=0.9,fontweight='bold',horizontalalignment='left')
    ax[1][1].set_title('(D) Suction sensor b1',x=0.02,y=0.9,fontweight='bold',horizontalalignment='left')
    ax[2][0].set_title('(E) Suction sensor b3',x=0.02,y=0.9,fontweight='bold',horizontalalignment='left')
    ax[2][1].set_title('(F) Suction sensor c1',x=0.02,y=0.9,fontweight='bold',horizontalalignment='left')
    ax[3][0].set_title('(G) Suction sensor c2',x=0.02,y=0.9,fontweight='bold',horizontalalignment='left')
    ax[3][1].set_title('(H) Suction sensor c3',x=0.02,y=0.9,fontweight='bold',horizontalalignment='left')
    
    #ax[0][0].set_xlim([14,25])
    #ax[0][1].set_xlim([14,25])
    #ax[1][0].set_xlim([14,25])
    #ax[1][1].set_xlim([14,25])
    #ax[2][0].set_xlim([14,25])
    #ax[2][1].set_xlim([14,25])
    ax[0][0].set_xlim([-0.05,1.2])
    ax[0][1].set_xlim([-0.05,1.2])
    ax[1][0].set_xlim([-0.05,1.2])
    ax[1][1].set_xlim([-0.05,1.2])
    ax[2][0].set_xlim([-0.05,1.2])
    ax[2][1].set_xlim([-0.05,1.2])
    ax[3][0].set_xlim([-0.05,1.2])
    ax[3][1].set_xlim([-0.05,1.2])

    ax[0][0].set_ylim([1.0e0,1.0e7])
    ax[0][1].set_ylim([1.0e0,1.0e7])
    ax[1][0].set_ylim([1.0e0,1.0e7])
    ax[1][1].set_ylim([1.0e0,1.0e7])
    ax[2][0].set_ylim([1.0e0,1.0e7])
    ax[2][1].set_ylim([1.0e0,1.0e7])
    ax[3][0].set_ylim([1.0e0,1.0e7])
    ax[3][1].set_ylim([1.0e0,1.0e7])

    ax[0][0].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[0][1].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[1][0].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[1][1].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[2][0].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[2][1].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[3][0].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[3][1].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    
    ax[0][0].set_ylabel('SUCTION (kPa)', fontsize=y_fontsize, labelpad=5)
    ax[1][0].set_ylabel('SUCTION (kPa)', fontsize=y_fontsize, labelpad=5)
    ax[2][0].set_ylabel('SUCTION (kPa)', fontsize=y_fontsize, labelpad=5)
    ax[3][0].set_ylabel('SUCTION (kPa)', fontsize=y_fontsize, labelpad=5)
    ax[3][0].set_xlabel('NORMORIZED TEMP. (CELSIUS)', fontsize=y_fontsize, labelpad=5)
    ax[3][1].set_xlabel('NORMORIZED TEMP. (CELSIUS)', fontsize=y_fontsize, labelpad=5)

    ax[0][0].legend(bbox_to_anchor=(.6  , 0.3 ), loc=2, borderaxespad=0.,fontsize=8,handletextpad=0.73,labelspacing=0.35)
    ax[0][1].legend(bbox_to_anchor=(.6  , 0.3 ), loc=2, borderaxespad=0.,fontsize=8,handletextpad=0.73,labelspacing=0.35)
    ax[1][0].legend(bbox_to_anchor=(.6  , 0.3 ), loc=2, borderaxespad=0.,fontsize=8,handletextpad=0.73,labelspacing=0.35)
    ax[1][1].legend(bbox_to_anchor=(.6  , 0.3 ), loc=2, borderaxespad=0.,fontsize=8,handletextpad=0.73,labelspacing=0.35)
    ax[2][0].legend(bbox_to_anchor=(.6  , 0.3 ), loc=2, borderaxespad=0.,fontsize=8,handletextpad=0.73,labelspacing=0.35)
    ax[2][1].legend(bbox_to_anchor=(.6  , 0.3 ), loc=2, borderaxespad=0.,fontsize=8,handletextpad=0.73,labelspacing=0.35)
    ax[3][0].legend(bbox_to_anchor=(.6  , 0.3 ), loc=2, borderaxespad=0.,fontsize=8,handletextpad=0.73,labelspacing=0.35)
    ax[3][1].legend(bbox_to_anchor=(.6  , 0.3 ), loc=2, borderaxespad=0.,fontsize=8,handletextpad=0.73,labelspacing=0.35)

    
    plt.show(block=False)
    
    fig.savefig('figure/plot_suction_calibration.png', format='png', dpi=300)
    #plt.close()  # it is all caused by pywafo. 
    
    
#sp_sch[sch_name].df['suc_commercial']=constants.swcc_reverse_fredlund_xing_1994(vwc=sp_sch[sch_name].df.sat_commercial*sp_sch[sch_name].por,por=0.5,
#        nf=0.9311,mf=0.1229,hr=238968.16,af=2.7090)
#
#
#
#
#[vwc_fred_xing,suction_fred_xing_kpa]=constants.swcc_fredlund_xing_1994(plot=True,por=0.5,nf=0.9311,mf=0.1229,hr=238968.16,af=2.7090)




