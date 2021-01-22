# linear fitting for moisture 
dp=np.linspace(250,530,num=30)
alpha_1=-4.8
#alpha_2=-10.1
#Galpha_3=-10.1
#sch_name='bacteria_first'
sp_sch[sch_name].moa1_fit1     = np.polyfit(sp_sch[sch_name].df['moa1'],sp_sch[sch_name].df ['sat_scale1'],1)
sp_sch[sch_name].moa1_fit1_str = 'y = '+"{0:0.3f}".format( sp_sch[sch_name].moa1_fit1[0]  ) + ' x ' + "{0:0.2f}".format( sp_sch[sch_name].moa1_fit1[1]  )
sp_sch[sch_name].moa1_fit2     = np.polyfit(sp_sch[sch_name].df['moa1'],sp_sch[sch_name].df ['sat_scale1'],2)
#sp_sch[sch_name].mo0_fit_twopoint=[360,290,alpha_1]
sp_sch[sch_name].moa1_fit_twopoint=[394,252,-7.1]#alpha_1]
sp_sch[sch_name].moa1_dp= (dp**sp_sch[sch_name].moa1_fit_twopoint[2]-sp_sch[sch_name].moa1_fit_twopoint[0]**sp_sch[sch_name].moa1_fit_twopoint[2])/(sp_sch[sch_name].moa1_fit_twopoint[1]**sp_sch[sch_name].moa1_fit_twopoint[2]-sp_sch[sch_name].moa1_fit_twopoint[0]**sp_sch[sch_name].moa1_fit_twopoint[2])
sp_sch[sch_name].moa1_text='y = (x$^{-10.1}$-290$^{-10.1}$)/(530$^{-10.1}$-290$^{-10.1}$)'

sp_sch[sch_name].moa3_fit1     = np.polyfit(sp_sch[sch_name].df['moa3'],sp_sch[sch_name].df ['sat_scale1'],1)
sp_sch[sch_name].moa3_fit1_str = 'y = '+"{0:0.3f}".format( sp_sch[sch_name].moa3_fit1[0]  ) + ' x ' + "{0:0.2f}".format( sp_sch[sch_name].moa3_fit1[1]  )
sp_sch[sch_name].moa3_fit2     = np.polyfit(sp_sch[sch_name].df['moa3'],sp_sch[sch_name].df ['sat_scale1'],2)
#sp_sch[sch_name].mo1_fit_twopoint=[380,290,alpha_1]
sp_sch[sch_name].moa3_fit_twopoint=[543,283,-2.8]#alpha_1]
sp_sch[sch_name].moa3_dp= (dp**sp_sch[sch_name].moa3_fit_twopoint[2]-sp_sch[sch_name].moa3_fit_twopoint[0]**sp_sch[sch_name].moa3_fit_twopoint[2])/(sp_sch[sch_name].moa3_fit_twopoint[1]**sp_sch[sch_name].moa3_fit_twopoint[2]-sp_sch[sch_name].moa3_fit_twopoint[0]**sp_sch[sch_name].moa3_fit_twopoint[2])
sp_sch[sch_name].moa3_text='y = (x$^{-10.1}$-275$^{-10.1}$)/(530$^{-10.1}$-275$^{-10.1}$)'

sp_sch[sch_name].mob1_fit1     = np.polyfit(sp_sch[sch_name].df['mob1'],sp_sch[sch_name].df ['sat_scale1'],1)
sp_sch[sch_name].mob1_fit1_str = 'y = '+"{0:0.3f}".format( sp_sch[sch_name].mob1_fit1[0]  ) + ' x ' + "{0:0.2f}".format( sp_sch[sch_name].mob1_fit1[1]  )
sp_sch[sch_name].mob1_fit2     = np.polyfit(sp_sch[sch_name].df['mob1'],sp_sch[sch_name].df ['sat_scale1'],2)
#sp_sch[sch_name].mo2_fit_twopoint=[530,305,alpha_1]

sp_sch[sch_name].mob1_fit_twopoint=[455,277,alpha_1]
sp_sch[sch_name].mob1_dp= (dp**sp_sch[sch_name].mob1_fit_twopoint[2]-sp_sch[sch_name].mob1_fit_twopoint[0]**sp_sch[sch_name].mob1_fit_twopoint[2])/(sp_sch[sch_name].mob1_fit_twopoint[1]**sp_sch[sch_name].mob1_fit_twopoint[2]-sp_sch[sch_name].mob1_fit_twopoint[0]**sp_sch[sch_name].mob1_fit_twopoint[2])
sp_sch[sch_name].mob1_text='y = (x$^{-10.1}$-290$^{-10.1}$)/(530$^{-10.1}$-290$^{-10.1}$)'

sp_sch[sch_name].mob2_fit1     = np.polyfit(sp_sch[sch_name].df['mob2'],sp_sch[sch_name].df ['sat_scale2'],1)
sp_sch[sch_name].mob2_fit1_str = 'y = '+"{0:0.3f}".format( sp_sch[sch_name].mob2_fit1[0]  ) + ' x ' + "{0:0.2f}".format( sp_sch[sch_name].mob2_fit1[1]  )
sp_sch[sch_name].mob2_fit2     = np.polyfit(sp_sch[sch_name].df['mob2'],sp_sch[sch_name].df ['sat_scale2'],2)
#sp_sch[sch_name].mo3_fit_twopoint=[380,300,alpha_1]

sp_sch[sch_name].mob2_fit_twopoint=[589,548,alpha_1]
sp_sch[sch_name].mob2_dp= (dp**sp_sch[sch_name].mob2_fit_twopoint[2]-sp_sch[sch_name].mob2_fit_twopoint[0]**sp_sch[sch_name].mob2_fit_twopoint[2])/(sp_sch[sch_name].mob2_fit_twopoint[1]**sp_sch[sch_name].mob2_fit_twopoint[2]-sp_sch[sch_name].mob2_fit_twopoint[0]**sp_sch[sch_name].mob2_fit_twopoint[2])
sp_sch[sch_name].mob2_text='y = (x$^{-10.1}$-292$^{-10.1}$)/(535$^{-10.1}$-292$^{-10.1}$)'

sp_sch[sch_name].mob3_fit1     = np.polyfit(sp_sch[sch_name].df['mob3'],sp_sch[sch_name].df ['sat_scale2'],1)
sp_sch[sch_name].mob3_fit1_str = 'y = '+"{0:0.3f}".format( sp_sch[sch_name].mob3_fit1[0]  ) + ' x ' + "{0:0.2f}".format( sp_sch[sch_name].mob3_fit1[1]  )
sp_sch[sch_name].mob3_fit2     = np.polyfit(sp_sch[sch_name].df['mob3'],sp_sch[sch_name].df ['sat_scale2'],2)
#sp_sch[sch_name].mo4_fit_twopoint=[530,295,alpha_1]
sp_sch[sch_name].mob3_fit_twopoint=[496,287,alpha_1]
sp_sch[sch_name].mob3_dp= (dp**sp_sch[sch_name].mob3_fit_twopoint[2]-sp_sch[sch_name].mob3_fit_twopoint[0]**sp_sch[sch_name].mob3_fit_twopoint[2])/(sp_sch[sch_name].mob3_fit_twopoint[1]**sp_sch[sch_name].mob3_fit_twopoint[2]-sp_sch[sch_name].mob3_fit_twopoint[0]**sp_sch[sch_name].mob3_fit_twopoint[2])
sp_sch[sch_name].mob3_text='y = (x$^{-10.1}$-286$^{-10.1}$)/(530$^{-7.1}$-286$^{-10.1}$)'

sp_sch[sch_name].moc1_fit1     = np.polyfit(sp_sch[sch_name].df['moc1'],sp_sch[sch_name].df ['sat_scale2'],1)
sp_sch[sch_name].moc1_fit1_str = 'y = '+"{0:0.3f}".format( sp_sch[sch_name].moc1_fit1[0]  ) + ' x ' + "{0:0.2f}".format( sp_sch[sch_name].moc1_fit1[1]  )
sp_sch[sch_name].moc1_fit2     = np.polyfit(sp_sch[sch_name].df['moc1'],sp_sch[sch_name].df ['sat_scale2'],2)
#sp_sch[sch_name].mo5_fit_twopoint=[530,285,alpha_1]
sp_sch[sch_name].moc1_fit_twopoint=[574,513,alpha_1]
sp_sch[sch_name].moc1_dp= (dp**sp_sch[sch_name].moc1_fit_twopoint[2]-sp_sch[sch_name].moc1_fit_twopoint[0]**sp_sch[sch_name].moc1_fit_twopoint[2])/(sp_sch[sch_name].moc1_fit_twopoint[1]**sp_sch[sch_name].moc1_fit_twopoint[2]-sp_sch[sch_name].moc1_fit_twopoint[0]**sp_sch[sch_name].moc1_fit_twopoint[2])
sp_sch[sch_name].moc1_text='y = (x$^{-10.1}$-273$^{-10.1}$)/(530$^{-10.1}$-273$^{-10.1}$)'

sp_sch[sch_name].moc2_fit1     = np.polyfit(sp_sch[sch_name].df['moc2'],sp_sch[sch_name].df ['sat_scale2'],1)
sp_sch[sch_name].moc2_fit1_str = 'y = '+"{0:0.3f}".format( sp_sch[sch_name].moc2_fit1[0]  ) + ' x ' + "{0:0.2f}".format( sp_sch[sch_name].moc2_fit1[1]  )
sp_sch[sch_name].moc2_fit2     = np.polyfit(sp_sch[sch_name].df['moc2'],sp_sch[sch_name].df ['sat_scale2'],2)
#sp_sch[sch_name].mo5_fit_twopoint=[530,285,alpha_1]
sp_sch[sch_name].moc2_fit_twopoint=[528,323,-2.8]#alpha_1]
sp_sch[sch_name].moc2_dp= (dp**sp_sch[sch_name].moc2_fit_twopoint[2]-sp_sch[sch_name].moc2_fit_twopoint[0]**sp_sch[sch_name].moc2_fit_twopoint[2])/(sp_sch[sch_name].moc2_fit_twopoint[1]**sp_sch[sch_name].moc2_fit_twopoint[2]-sp_sch[sch_name].moc2_fit_twopoint[0]**sp_sch[sch_name].moc2_fit_twopoint[2])
sp_sch[sch_name].moc2_text='y = (x$^{-10.1}$-273$^{-10.1}$)/(530$^{-10.1}$-273$^{-10.1}$)'

sp_sch[sch_name].moc3_fit1     = np.polyfit(sp_sch[sch_name].df['moc3'],sp_sch[sch_name].df ['sat_scale2'],1)
sp_sch[sch_name].moc3_fit1_str = 'y = '+"{0:0.3f}".format( sp_sch[sch_name].moc3_fit1[0]  ) + ' x ' + "{0:0.2f}".format( sp_sch[sch_name].moc3_fit1[1]  )
sp_sch[sch_name].moc3_fit2     = np.polyfit(sp_sch[sch_name].df['moc3'],sp_sch[sch_name].df ['sat_scale2'],2)
#sp_sch[sch_name].mo5_fit_twopoint=[530,285,alpha_1]
sp_sch[sch_name].moc3_fit_twopoint=[486,274,alpha_1]
sp_sch[sch_name].moc3_dp= (dp**sp_sch[sch_name].moc3_fit_twopoint[2]-sp_sch[sch_name].moc3_fit_twopoint[0]**sp_sch[sch_name].moc3_fit_twopoint[2])/(sp_sch[sch_name].moc3_fit_twopoint[1]**sp_sch[sch_name].moc3_fit_twopoint[2]-sp_sch[sch_name].moc3_fit_twopoint[0]**sp_sch[sch_name].moc3_fit_twopoint[2])
sp_sch[sch_name].moc3_text='y = (x$^{-10.1}$-273$^{-10.1}$)/(530$^{-10.1}$-273$^{-10.1}$)'

#sp_sch[sch_name].vw2_fit1     = np.polyfit(sp_sch[sch_name].df['vw_2'],sp_sch[sch_name].df ['sat_scale2'],1)
#sp_sch[sch_name].vw2_fit1_str = 'y = '+"{0:0.3f}".format( sp_sch[sch_name].vw2_fit1[0]  ) + ' x ' + "{0:0.2f}".format( sp_sch[sch_name].vw2_fit1[1]  )
#sp_sch[sch_name].vw2_fit2     = np.polyfit(sp_sch[sch_name].df['vw_2'],sp_sch[sch_name].df ['sat_scale2'],2)
#sp_sch[sch_name].vw2_fit_twopoint=[17.8,27.0,2.5]
#sp_sch[sch_name].vw2_dp= (dp**sp_sch[sch_name].vw2_fit_twopoint[2]-sp_sch[sch_name].vw2_fit_twopoint[0]**sp_sch[sch_name].vw2_fit_twopoint[2])/(sp_sch[sch_name].vw2_fit_twopoint[1]**sp_sch[sch_name].vw2_fit_twopoint[2]-sp_sch[sch_name].vw2_fit_twopoint[0]**sp_sch[sch_name].vw2_fit_twopoint[2])
#sp_sch[sch_name].vw2_text='y = (x$^{2.5}$-'+ "{0:0.1f}".format(sp_sch[sch_name].vw2_fit_twopoint[0])+'$^{2.5}$)/('  + "{0:0.1f}".format(sp_sch[sch_name].vw2_fit_twopoint[1]) +'$^{2.5}$-' + "{0:0.1f}".format(sp_sch[sch_name].vw2_fit_twopoint[0]) +'$^{2.5}$)'
#
#sp_sch[sch_name].vw3_fit1     = np.polyfit(sp_sch[sch_name].df['vw_3'],sp_sch[sch_name].df ['sat_scale3'],1)
#sp_sch[sch_name].vw3_fit1_str = 'y = '+"{0:0.3f}".format( sp_sch[sch_name].vw3_fit1[0]  ) + ' x ' + "{0:0.1f}".format( sp_sch[sch_name].vw3_fit1[1]  )
#sp_sch[sch_name].vw3_fit2     = np.polyfit(sp_sch[sch_name].df['vw_3'],sp_sch[sch_name].df ['sat_scale3'],2)
#sp_sch[sch_name].vw3_fit_twopoint=[16,27.0,2.5]
#sp_sch[sch_name].vw3_dp= (dp**sp_sch[sch_name].vw3_fit_twopoint[2]-sp_sch[sch_name].vw3_fit_twopoint[0]**sp_sch[sch_name].vw3_fit_twopoint[2])/(sp_sch[sch_name].vw3_fit_twopoint[1]**sp_sch[sch_name].vw3_fit_twopoint[2]-sp_sch[sch_name].vw3_fit_twopoint[0]**sp_sch[sch_name].vw3_fit_twopoint[2])
#sp_sch[sch_name].vw3_text='y = (x$^{2.5}$-'+ "{0:0.1f}".format(sp_sch[sch_name].vw3_fit_twopoint[0])+'$^{2.5}$)/('  + "{0:0.1f}".format(sp_sch[sch_name].vw3_fit_twopoint[1]) +'$^{2.5}$-' + "{0:0.1f}".format(sp_sch[sch_name].vw3_fit_twopoint[0]) +'$^{2.5}$)'

#sch_name='bacteria_second'
#sp_sch[sch_name].vw1_fit1     = np.polyfit(sp_sch[sch_name].df['vw_1'],sp_sch[sch_name].df ['sat_scale1'],1)
#sp_sch[sch_name].vw1_fit1_str = 'y = '+"{0:0.3f}".format( sp_sch[sch_name].vw1_fit1[0]  ) + ' x ' + "{0:0.2f}".format( sp_sch[sch_name].vw1_fit1[1]  )
#sp_sch[sch_name].vw1_fit2     = np.polyfit(sp_sch[sch_name].df['vw_1'],sp_sch[sch_name].df ['sat_scale1'],2)
#sp_sch[sch_name].vw1_fit_twopoint=[16,26.0,2.5]
#sp_sch[sch_name].vw1_dp= (dp**sp_sch[sch_name].vw1_fit_twopoint[2]-sp_sch[sch_name].vw1_fit_twopoint[0]**sp_sch[sch_name].vw1_fit_twopoint[2])/(sp_sch[sch_name].vw1_fit_twopoint[1]**sp_sch[sch_name].vw1_fit_twopoint[2]-sp_sch[sch_name].vw1_fit_twopoint[0]**sp_sch[sch_name].vw1_fit_twopoint[2])
#sp_sch[sch_name].vw1_text='y = (x$^{2.5}$-'+ "{0:0.1f}".format(sp_sch[sch_name].vw1_fit_twopoint[0])+'$^{2.5}$)/('  + "{0:0.1f}".format(sp_sch[sch_name].vw1_fit_twopoint[1]) +'$^{2.5}$-' + "{0:0.1f}".format(sp_sch[sch_name].vw1_fit_twopoint[0]) +'$^{2.5}$)'
#
#sch_name='bacteria_third'
#sp_sch[sch_name].vw2_fit1     = np.polyfit(sp_sch[sch_name].df['vw_2'],sp_sch[sch_name].df ['sat_scale2'],1)
#sp_sch[sch_name].vw2_fit1_str = 'y = '+"{0:0.3f}".format( sp_sch[sch_name].vw2_fit1[0]  ) + ' x ' + "{0:0.2f}".format( sp_sch[sch_name].vw2_fit1[1]  )
#sp_sch[sch_name].vw2_fit2     = np.polyfit(sp_sch[sch_name].df['vw_2'],sp_sch[sch_name].df ['sat_scale2'],2)
#sp_sch[sch_name].vw2_fit_twopoint=[18,27.0,2.5]
#sp_sch[sch_name].vw2_dp= (dp**sp_sch[sch_name].vw2_fit_twopoint[2]-sp_sch[sch_name].vw2_fit_twopoint[0]**sp_sch[sch_name].vw2_fit_twopoint[2])/(sp_sch[sch_name].vw2_fit_twopoint[1]**sp_sch[sch_name].vw2_fit_twopoint[2]-sp_sch[sch_name].vw2_fit_twopoint[0]**sp_sch[sch_name].vw2_fit_twopoint[2])
#sp_sch[sch_name].vw2_text='y = (x$^{2.5}$-'+ "{0:0.1f}".format(sp_sch[sch_name].vw2_fit_twopoint[0])+'$^{2.5}$)/('  + "{0:0.1f}".format(sp_sch[sch_name].vw2_fit_twopoint[1]) +'$^{2.5}$-' + "{0:0.1f}".format(sp_sch[sch_name].vw2_fit_twopoint[0]) +'$^{2.5}$)'
#
#sp_sch[sch_name].vw3_fit1     = np.polyfit(sp_sch[sch_name].df['vw_3'],sp_sch[sch_name].df ['sat_scale3'],1)
#sp_sch[sch_name].vw3_fit1_str = 'y = '+"{0:0.3f}".format( sp_sch[sch_name].vw3_fit1[0]  ) + ' x ' + "{0:0.2f}".format( sp_sch[sch_name].vw3_fit1[1]  )
#sp_sch[sch_name].vw3_fit2     = np.polyfit(sp_sch[sch_name].df['vw_3'],sp_sch[sch_name].df ['sat_scale3'],2)
#sp_sch[sch_name].vw3_fit_twopoint=[18.5,25.0,2.5]
#sp_sch[sch_name].vw3_dp= (dp**sp_sch[sch_name].vw3_fit_twopoint[2]-sp_sch[sch_name].vw3_fit_twopoint[0]**sp_sch[sch_name].vw3_fit_twopoint[2])/(sp_sch[sch_name].vw3_fit_twopoint[1]**sp_sch[sch_name].vw3_fit_twopoint[2]-sp_sch[sch_name].vw3_fit_twopoint[0]**sp_sch[sch_name].vw3_fit_twopoint[2])
#sp_sch[sch_name].vw3_text='y = (x$^{2.5}$-'+ "{0:0.1f}".format(sp_sch[sch_name].vw3_fit_twopoint[0])+'$^{2.5}$)/('  + "{0:0.1f}".format(sp_sch[sch_name].vw3_fit_twopoint[1]) +'$^{2.5}$-' + "{0:0.1f}".format(sp_sch[sch_name].vw3_fit_twopoint[0]) +'$^{2.5}$)'

        



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
    fig, ax = plt.subplots(4,2,sharex=False,figsize=(8,9))
    fig.subplots_adjust(hspace=.10)
    fig.subplots_adjust(left=0.15, right=0.98, top=0.97, bottom=0.08)
    for i in ax:
      for j in i:
        for axis in ['top','bottom','left','right']:
          j.spines[axis].set_linewidth(2)

    
    sch_name='basin_test'
    ax[0][0].plot(sp_sch[sch_name].df['moa1'], sp_sch[sch_name].df ['sat_scale1'],   'o',mfc='none' ,markeredgecolor='r',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Basin_a',markevery=2) 
    #ax[0][0].plot(dp, sp_sch[sch_name].mo0_fit1[0]*dp+sp_sch[sch_name].mo0_fit1[1],color='r',linewidth=lw,label=sp_sch[sch_name].mo0_fit1_str) 
    #ax[0][0].plot(dp, sp_sch[sch_name].vw1_fit2[0]*dp**2+sp_sch[sch_name].vw1_fit2[1]*dp+sp_sch[sch_name].vw1_fit2[2],color='k',linewidth=lw,label=sp_sch[sch_name].vw1_fit1_str) 
    #ax[0][0].plot(dp, sp_sch[sch_name].mo0_dp  ,color='r',linewidth=lw,label=sp_sch[sch_name].mo0_text,linestyle='--') 
    ax[0][0].plot(dp, sp_sch[sch_name].moa1_dp  ,color='r',linewidth=lw,linestyle='--')

    ax[0][1].plot(sp_sch[sch_name].df['moa3'],sp_sch[sch_name].df ['sat_scale1'],    's',mfc='none' ,markeredgecolor='g',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Basin_a',markevery=2) 
    #ax[0][1].plot(dp, sp_sch[sch_name].mo1_fit1[0]*dp+sp_sch[sch_name].mo1_fit1[1],color='r',linewidth=lw,label=sp_sch[sch_name].mo1_fit1_str) 
    #ax[0][1].plot(dp, sp_sch[sch_name].vw2_fit2[0]*dp**2+sp_sch[sch_name].vw2_fit2[1]*dp+sp_sch[sch_name].vw2_fit2[2],color='k',linewidth=lw,label=sp_sch[sch_name].vw2_fit1_str) 
    ax[0][1].plot(dp, sp_sch[sch_name].moa3_dp,color='g',linewidth=lw,linestyle='--') 
    #ax[0][1].plot(dp, sp_sch[sch_name].mo1_dp,color='r',linewidth=lw,label=sp_sch[sch_name].mo1_text,linestyle='--')

    
    ax[1][0].plot(sp_sch[sch_name].df['mob1'],sp_sch[sch_name].df ['sat_scale1'],    'v',mfc='none' ,markeredgecolor='y',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Basin_b',markevery=2) 
    #ax[1][0].plot(dp, sp_sch[sch_name].mo2_fit1[0]*dp+sp_sch[sch_name].mo2_fit1[1],color='r',linewidth=lw,label=sp_sch[sch_name].mo2_fit1_str) 
    ax[1][0].plot(dp, sp_sch[sch_name].mob1_dp,color='y',linewidth=lw,linestyle='--') 
#   ax[1][0].plot(dp, sp_sch[sch_name].mo2_dp,color='r',linewidth=lw,label=sp_sch[sch_name].mo2_text,linestyle='--')

#    sch_name='Marandoo_third'
    ax[1][1].plot(sp_sch[sch_name].df['mob2'],sp_sch[sch_name].df ['sat_scale2'],    'x',mfc='none' ,markeredgecolor='blue',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Basin_b',markevery=2) 
    #ax[1][1].plot(dp, sp_sch[sch_name].mo3_fit1[0]*dp+sp_sch[sch_name].mo3_fit1[1],color='r',linewidth=lw,label=sp_sch[sch_name].mo3_fit1_str) 
    ax[1][1].plot(dp, sp_sch[sch_name].mob2_dp,color='blue',linewidth=lw,linestyle='--') 
    #ax[1][1].plot(dp, sp_sch[sch_name].mo3_dp,color='r',linewidth=lw,label=sp_sch[sch_name].mo3_text,linestyle='--')   

#    sch_name='Marandoo_second'
    ax[2][0].plot(sp_sch[sch_name].df['mob3'],sp_sch[sch_name].df ['sat_scale2'],    '^',mfc='none' ,markeredgecolor='gold',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Basin_b',markevery=2) 
    #ax[2][0].plot(dp, sp_sch[sch_name].mo4_fit1[0]*dp+sp_sch[sch_name].mo4_fit1[1],color='r',linewidth=lw,label=sp_sch[sch_name].mo4_fit1_str) 
    ax[2][0].plot(dp, sp_sch[sch_name].mob3_dp,color='gold',linewidth=lw,linestyle='--') 
    #ax[2][0].plot(dp, sp_sch[sch_name].mo4_dp,color='r',linewidth=lw,label=sp_sch[sch_name].mo4_text,linestyle='--')

    ax[2][1].plot(sp_sch[sch_name].df['moc1'],sp_sch[sch_name].df ['sat_scale2'],    'd',mfc='none' ,markeredgecolor='black',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Basin_c',markevery=2) 
    #ax[2][1].plot(dp, sp_sch[sch_name].mo5_fit1[0]*dp+sp_sch[sch_name].mo5_fit1[1],color='r',linewidth=lw,label=sp_sch[sch_name].mo5_fit1_str) 
    ax[2][1].plot(dp, sp_sch[sch_name].moc1_dp,color='black',linewidth=lw,linestyle='--') 
    #ax[2][1].plot(dp, sp_sch[sch_name].mo5_dp,color='r',linewidth=lw,label=sp_sch[sch_name].mo5_text,linestyle='--')
#

    #sch_name='bacteria_second'
    ax[3][0].plot(sp_sch[sch_name].df['moc2'], sp_sch[sch_name].df ['sat_scale1'],   'p',mfc='none' ,markeredgecolor='orange',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Basin_c',markevery=2)
    #ax[0][0].plot(dp, sp_sch[sch_name].mo0_fit1[0]*dp+sp_sch[sch_name].mo0_fit1[1],color='g',linewidth=lw,label=sp_sch[sch_name].mo0_fit1_str)
    #ax[0][0].plot(dp, sp_sch[sch_name].vw1_fit2[0]*dp**2+sp_sch[sch_name].vw1_fit2[1]*dp+sp_sch[sch_name].vw1_fit2[2],color='k',linewidth=lw,label=sp_sch[sch_name].vw1_fit1_str) 
    ax[3][0].plot(dp, sp_sch[sch_name].moc2_dp,color='orange',linewidth=lw,linestyle='--')

    ax[3][1].plot(sp_sch[sch_name].df['moc3'],sp_sch[sch_name].df ['sat_scale1'],    '*',mfc='none' ,markeredgecolor='purple',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Basin_c',markevery=2)
    #ax[0][1].plot(dp, sp_sch[sch_name].mo1_fit1[0]*dp+sp_sch[sch_name].mo1_fit1[1],color='g',linewidth=lw,label=sp_sch[sch_name].mo1_fit1_str)
    #ax[0][1].plot(dp, sp_sch[sch_name].vw2_fit2[0]*dp**2+sp_sch[sch_name].vw2_fit2[1]*dp+sp_sch[sch_name].vw2_fit2[2],color='k',linewidth=lw,label=sp_sch[sch_name].vw2_fit1_str) 
    ax[3][1].plot(dp, sp_sch[sch_name].moc3_dp,color='purple',linewidth=lw,linestyle='--')
#
    #ax[1][0].plot(sp_sch[sch_name].df['mo2'],sp_sch[sch_name].df ['sat_scale1'],    'v',mfc='none' ,markeredgecolor='g',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Experiment2',markevery=2)
    #ax[1][0].plot(dp, sp_sch[sch_name].mo2_fit1[0]*dp+sp_sch[sch_name].mo2_fit1[1],color='g',linewidth=lw,label=sp_sch[sch_name].mo2_fit1_str)
    #ax[1][0].plot(dp, sp_sch[sch_name].mo2_dp,color='g',linewidth=lw,linestyle='--')
#
#    sch_name='Marandoo_third'
    #ax[1][1].plot(sp_sch[sch_name].df['mo3'],sp_sch[sch_name].df ['sat_scale2'],    'x',mfc='none' ,markeredgecolor='g',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Experiment2',markevery=2)
    #ax[1][1].plot(dp, sp_sch[sch_name].mo3_fit1[0]*dp+sp_sch[sch_name].mo3_fit1[1],color='g',linewidth=lw,label=sp_sch[sch_name].mo3_fit1_str)
    #ax[1][1].plot(dp, sp_sch[sch_name].mo3_dp,color='g',linewidth=lw,linestyle='--')
#
#    sch_name='Marandoo_second'
    #ax[2][0].plot(sp_sch[sch_name].df['mo4'],sp_sch[sch_name].df ['sat_scale2'],    '^',mfc='none' ,markeredgecolor='g',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Experiment2',markevery=2)
    #ax[2][0].plot(dp, sp_sch[sch_name].mo4_fit1[0]*dp+sp_sch[sch_name].mo4_fit1[1],color='g',linewidth=lw,label=sp_sch[sch_name].mo4_fit1_str)
    #ax[2][0].plot(dp, sp_sch[sch_name].mo4_dp,color='g',linewidth=lw,linestyle='--')
#
    #ax[2][1].plot(sp_sch[sch_name].df['mo5'],sp_sch[sch_name].df ['sat_scale2'],    'd',mfc='none' ,markeredgecolor='g',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Experiment2',markevery=2)
    #ax[2][1].plot(dp, sp_sch[sch_name].mo5_fit1[0]*dp+sp_sch[sch_name].mo5_fit1[1],color='g',linewidth=lw,label=sp_sch[sch_name].mo5_fit1_str)
    #ax[2][1].plot(dp, sp_sch[sch_name].mo5_dp,color='g',linewidth=lw,linestyle='--')

    #sch_name='bacteria_third'
    #ax[0][0].plot(sp_sch[sch_name].df['mo0'], sp_sch[sch_name].df ['sat_scale1'],   'o',mfc='none' ,markeredgecolor='c',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Experiment3',markevery=2)
    #ax[0][0].plot(dp, sp_sch[sch_name].mo0_fit1[0]*dp+sp_sch[sch_name].mo0_fit1[1],color='c',linewidth=lw,label=sp_sch[sch_name].mo0_fit1_str)
    #ax[0][0].plot(dp, sp_sch[sch_name].vw1_fit2[0]*dp**2+sp_sch[sch_name].vw1_fit2[1]*dp+sp_sch[sch_name].vw1_fit2[2],color='k',linewidth=lw,label=sp_sch[sch_name].vw1_fit1_str) 
    #ax[0][0].plot(dp, sp_sch[sch_name].mo0_dp,color='c',linewidth=lw,linestyle='--')


    #ax[0][1].plot(sp_sch[sch_name].df['mo1'],sp_sch[sch_name].df ['sat_scale1'],    's',mfc='none' ,markeredgecolor='c',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Experiment3',markevery=2)
    #ax[0][1].plot(dp, sp_sch[sch_name].mo1_fit1[0]*dp+sp_sch[sch_name].mo1_fit1[1],color='c',linewidth=lw,label=sp_sch[sch_name].mo1_fit1_str)
    #ax[0][1].plot(dp, sp_sch[sch_name].vw2_fit2[0]*dp**2+sp_sch[sch_name].vw2_fit2[1]*dp+sp_sch[sch_name].vw2_fit2[2],color='k',linewidth=lw,label=sp_sch[sch_name].vw2_fit1_str) 
    #ax[0][1].plot(dp, sp_sch[sch_name].mo1_dp,color='c',linewidth=lw,linestyle='--')
#
    #ax[1][0].plot(sp_sch[sch_name].df['mo2'],sp_sch[sch_name].df ['sat_scale1'],    'v',mfc='none' ,markeredgecolor='c',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Experiment3',markevery=2)
    #ax[1][0].plot(dp, sp_sch[sch_name].mo2_fit1[0]*dp+sp_sch[sch_name].mo2_fit1[1],color='c',linewidth=lw,label=sp_sch[sch_name].mo2_fit1_str)
    #ax[1][0].plot(dp, sp_sch[sch_name].mo2_dp,color='c',linewidth=lw,linestyle='--')
#
#   # sch_name='Marandoo_third'
    #ax[1][1].plot(sp_sch[sch_name].df['mo3'],sp_sch[sch_name].df ['sat_scale2'],    'x',mfc='none' ,markeredgecolor='c',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Experiment3',markevery=2)
    #ax[1][1].plot(dp, sp_sch[sch_name].mo3_fit1[0]*dp+sp_sch[sch_name].mo3_fit1[1],color='c',linewidth=lw,label=sp_sch[sch_name].mo3_fit1_str)
    #ax[1][1].plot(dp, sp_sch[sch_name].mo3_dp,color='c',linewidth=lw,linestyle='--')
#
#   # sch_name='Marandoo_second'
    #ax[2][0].plot(sp_sch[sch_name].df['mo4'],sp_sch[sch_name].df ['sat_scale2'],    '^',mfc='none' ,markeredgecolor='c',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Experiment3',markevery=2)
    #ax[2][0].plot(dp, sp_sch[sch_name].mo4_fit1[0]*dp+sp_sch[sch_name].mo4_fit1[1],color='c',linewidth=lw,label=sp_sch[sch_name].mo4_fit1_str)
    #ax[2][0].plot(dp, sp_sch[sch_name].mo4_dp,color='c',linewidth=lw,linestyle='--')
#
    #ax[2][1].plot(sp_sch[sch_name].df['mo5'],sp_sch[sch_name].df ['sat_scale2'],    'd',mfc='none' ,markeredgecolor='c',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Experiment3',markevery=2)
    #ax[2][1].plot(dp, sp_sch[sch_name].mo5_fit1[0]*dp+sp_sch[sch_name].mo5_fit1[1],color='c',linewidth=lw,label=sp_sch[sch_name].mo5_fit1_str)
    #ax[2][1].plot(dp, sp_sch[sch_name].mo5_dp,color='c',linewidth=lw,linestyle='--')

    ax[0][0].set_title('(A) Moisture sensor a1(33k)',x=0.35,y=0.88,fontweight='bold',horizontalalignment='left')
    ax[0][1].set_title('(B) Moisture sensor a3',x=0.35,y=0.88,fontweight='bold',horizontalalignment='left')
    ax[1][0].set_title('(C) Moisture sensor b1(10k)',x=0.35,y=0.88,fontweight='bold',horizontalalignment='left')
    ax[1][1].set_title('(D) Moisture sensor b2(33R)',x=0.35,y=0.88,fontweight='bold',horizontalalignment='left')
    ax[2][0].set_title('(E) Moisture sensor b3',x=0.35,y=0.88,fontweight='bold',horizontalalignment='left')
    ax[2][1].set_title('(F) Moisture sensor c1(160R)',x=0.35,y=0.88,fontweight='bold',horizontalalignment='left')
    ax[3][0].set_title('(E) Moisture sensor c2(3k3)',x=0.35,y=0.88,fontweight='bold',horizontalalignment='left')
    ax[3][1].set_title('(F) Moisture sensor c3',x=0.35,y=0.88,fontweight='bold',horizontalalignment='left')

    ax[0][0].set_ylim([-0.1,1.1])
    ax[0][1].set_ylim([-0.1,1.1])
    ax[1][0].set_ylim([-0.1,1.1])
    ax[1][1].set_ylim([-0.1,1.1])
    ax[2][0].set_ylim([-0.1,1.1])
    ax[2][1].set_ylim([-0.1,1.1])
    ax[3][0].set_ylim([-0.1,1.1])
    ax[3][1].set_ylim([-0.1,1.1])
    ax[0][0].set_xlim([250,600])
    ax[0][1].set_xlim([250,600])
    ax[1][0].set_xlim([250,600])
    ax[1][1].set_xlim([250,600])
    ax[2][0].set_xlim([250,600])
    ax[2][1].set_xlim([250,600])
    ax[3][0].set_xlim([250,600])
    ax[3][1].set_xlim([250,600])
    ax[0][0].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[0][1].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[1][0].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[1][1].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[2][0].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[2][1].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[3][0].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[3][1].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[0][0].set_ylabel('DEGREE OF SATURATION', fontsize=y_fontsize, labelpad=5)
    ax[1][0].set_ylabel('DEGREE OF SATURATION', fontsize=y_fontsize, labelpad=5)
    ax[2][0].set_ylabel('DEGREE OF SATURATION', fontsize=y_fontsize, labelpad=5)
    ax[3][0].set_ylabel('DEGREE OF SATURATION', fontsize=y_fontsize, labelpad=5)
    ax[3][0].set_xlabel('SENSOR VALUE', fontsize=y_fontsize, labelpad=5)
    ax[3][1].set_xlabel('SENSOR VALUE', fontsize=y_fontsize, labelpad=5)

    
    ax[0][0].legend(bbox_to_anchor=(0.6  , 0.9 ), loc=2, borderaxespad=0.,fontsize=8,handletextpad=0.73,labelspacing=0.35,handlelength=2.5)
    ax[0][1].legend(bbox_to_anchor=(0.6  , 0.9 ), loc=2, borderaxespad=0.,fontsize=8,handletextpad=0.73,labelspacing=0.35,handlelength=2.5)
    ax[1][0].legend(bbox_to_anchor=(0.6  , 0.9 ), loc=2, borderaxespad=0.,fontsize=8,handletextpad=0.73,labelspacing=0.35,handlelength=2.5)
    ax[1][1].legend(bbox_to_anchor=(0.6  , 0.9 ), loc=2, borderaxespad=0.,fontsize=8,handletextpad=0.73,labelspacing=0.35,handlelength=2.5)
    ax[2][0].legend(bbox_to_anchor=(0.6  , 0.9 ), loc=2, borderaxespad=0.,fontsize=8,handletextpad=0.73,labelspacing=0.35,handlelength=2.5)
    ax[2][1].legend(bbox_to_anchor=(0.6  , 0.9 ), loc=2, borderaxespad=0.,fontsize=8,handletextpad=0.73,labelspacing=0.35,handlelength=2.5)
    ax[3][0].legend(bbox_to_anchor=(0.6  , 0.9 ), loc=2, borderaxespad=0.,fontsize=8,handletextpad=0.73,labelspacing=0.35,handlelength=2.5)
    ax[3][1].legend(bbox_to_anchor=(0.6  , 0.9 ), loc=2, borderaxespad=0.,fontsize=8,handletextpad=0.73,labelspacing=0.35,handlelength=2.5)

    
    plt.show(block=False)
    
    fig.savefig('figure/plot_moisture_calibration.png', format='png', dpi=300)
    #fig.savefig('figure/plot_moisture_calibration_600.png', format='png', dpi=600)
    #sp_sch["Marandoo_first"].df.to_csv("output_data/Marandoo_first.csv")
    #plt.close()  # it is all caused by pywafo. 
    
    

