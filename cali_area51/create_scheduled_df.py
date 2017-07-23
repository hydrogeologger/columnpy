import operator
py_compile.compile('/home/chenming/Dropbox/scripts/github/pyduino/python/post_processing/sensorfun.py')
import sensorfun 
reload( sensorfun)

py_compile.compile('/home/chenming/Dropbox/scripts/github/pyduino/python/post_processing/figlib.py')
import figlib 
reload( figlib)
sp_sch={}

swcc_coef={'por':0.37,'af':2.1,'nf':1.8,'mf':0.7,'hr':1.e5 }
mo_7_coef={'x_offset':410,'x_scale':25.0,'y_scale':-20,'y_offset':12.1,'lamb':3.0} # only x_offset and y_offset needs to be configured
mo_8_coef={'x_offset':430,'x_scale':15.0,'y_scale':-20,'y_offset':17.1,'lamb':0.75} # only x_offset and y_offset needs to be configured
mo_9_coef={'x_offset':336,'x_scale':5.,'y_scale':1,'y_offset':0,'lamb':1.05} # only x_offset and y_offset needs to be configured
mo_10_coef={'x_offset':331,'x_scale':5.,'y_scale':1,'y_offset':0,'lamb':1.05} # only x_offset and y_offset needs to be configured

for line in open("schedule.ipt"):
    li=line.strip()
    if not li.startswith("#"):
        line_content=[x.strip() for x in li.split(',')]
        sch_name=line_content[2]
        sp_sch[sch_name]=pandas_scale.concat_data_roof(pd.datetime.strptime(line_content[0],'%Y/%b/%d %H:%M'),
            pd.datetime.strptime(line_content[1],'%Y/%b/%d %H:%M'),dt_s );
        sp_sch[sch_name].start_dt=pd.datetime.strptime(line_content[0],'%Y/%b/%d %H:%M')
        sp_sch[sch_name].end_dt=pd.datetime.strptime(line_content[1],'%Y/%b/%d %H:%M')

        sp_sch[sch_name].water_level   =float(line_content[3])
        sp_sch[sch_name].surface_area  =float(line_content[4])
        sp_sch[sch_name].soil_thickness=float(line_content[5])
        sp_sch[sch_name].time_surface_emerge = pd.datetime.strptime(line_content[10],'%Y/%b/%d %H:%M')

        sp_sch[sch_name].por=float(line_content[6])
        sp_sch[sch_name].te_coef=float(line_content[8])
        sp_sch[sch_name].tas606_coef=float(line_content[9])
        min_index, min_value = min(enumerate( abs(sp.df['date_time']-sp_sch[sch_name].start_dt)), key=operator.itemgetter(1))
        sp_sch[sch_name].start_ind=min_index
        min_index, min_value = min(enumerate( abs(sp.df['date_time']-sp_sch[sch_name].end_dt)), key=operator.itemgetter(1))
        sp_sch[sch_name].end_ind=min_index
        #sp_sch[sch_name]['df']=sp.df[sp_sch[sch_name].start_ind:sp_sch[sch_name].end_ind]
        ## reset index
        sp_sch[sch_name].df=sp_sch[sch_name].df.reset_index(drop=True)
        ## add new column
        ## http://stackoverflow.com/questions/12555323/adding-new-column-to-existing-dataframe-in-python-pandas
        sp_sch[sch_name].df=sp_sch[sch_name].df.assign(
            time_days=[(sp_sch[sch_name].df['date_time'][x]-sp_sch[sch_name].df['date_time'][0]).total_seconds()/86400
                    for x in range(len(sp_sch[sch_name].df['date_time']))])

        min_index, min_value = min(enumerate( abs(sp_sch[sch_name].df['date_time']- sp_sch[sch_name].time_surface_emerge 
            )), key=operator.itemgetter(1))
        sp_sch[sch_name].idx_surface_emerge = min_index 

        plot_switch=False
        sp_sch[sch_name].merge_data( df=scale.df, keys=['tas606']            ,plot=plot_switch ,coef=5e-16)
        sp_sch[sch_name].merge_data( df=scale.df, keys=['te']                ,plot=plot_switch ,coef=5e-16)
        sp_sch[sch_name].merge_data( df=sensors.df, keys=['saltrh_2_rh']     ,plot=plot_switch ,coef=5e-10)
        sp_sch[sch_name].merge_data( df=sensors.df, keys=['saltrh_3_rh']     ,plot=plot_switch ,coef=5e-10)
        sp_sch[sch_name].merge_data( df=sensors.df, keys=['suht_28e5_begin'] ,plot=plot_switch ,coef=5e-10)
        sp_sch[sch_name].merge_data( df=sensors.df, keys=['suht_2847_begin'] ,plot=plot_switch ,coef=5e-10)
        
        sp_sch[sch_name].merge_data( df=sensors.df, keys=['suht_28e5_peak']  ,plot=plot_switch ,coef=5e-10)
        sp_sch[sch_name].merge_data( df=sensors.df, keys=['suht_2847_peak']  ,plot=plot_switch ,coef=5e-10)
        
        sp_sch[sch_name].merge_data( df=sensors.df, keys=['suht_28e5_end']   ,plot=plot_switch ,coef=5e-10)
        sp_sch[sch_name].merge_data( df=sensors.df, keys=['suht_2847_end']   ,plot=plot_switch ,coef=5e-10)
        sp_sch[sch_name].merge_data( df=sensors.df, keys=['saltrh_3_tp']     ,plot=plot_switch ,coef=5e-10)
        sp_sch[sch_name].merge_data( df=sensors.df, keys=['saltrh_2_tp']     ,plot=plot_switch ,coef=5e-10)
        
        sp_sch[sch_name].merge_data( df=sensors.df, keys=['mo_7']            ,plot=plot_switch ,coef=5e-15)
        sp_sch[sch_name].merge_data( df=sensors.df, keys=['mo_8']            ,plot=plot_switch ,coef=5e-15)
        sp_sch[sch_name].merge_data( df=sensors.df, keys=['mo_9']            ,plot=plot_switch ,coef=5e-15)
        sp_sch[sch_name].merge_data( df=sensors.df, keys=['mo_10']           ,plot=plot_switch ,coef=5e-15)
        sp_sch[sch_name].merge_data( df=balance.df, keys=['commercial']      ,plot=plot_switch ,coef=5e-15)

        # get delta t
        sp_sch[sch_name].df.delta_t_28e5_heat =sp_sch[sch_name].df['suht_28e5_peak']- sp_sch[sch_name].df['suht_28e5_begin'] 
        sp_sch[sch_name].df.delta_t_28e5_cool =sp_sch[sch_name].df['suht_28e5_peak']- sp_sch[sch_name].df['suht_28e5_end'] 
        sp_sch[sch_name].df.delta_t_2847_heat =sp_sch[sch_name].df['suht_2847_peak']- sp_sch[sch_name].df['suht_2847_begin'] 
        sp_sch[sch_name].df.delta_t_2847_cool =sp_sch[sch_name].df['suht_2847_peak']- sp_sch[sch_name].df['suht_2847_end'] 
        delta_t_28e5_low_2_high=sorted(sp_sch[sch_name].df.delta_t_28e5_heat, key=float)
        sp_sch[sch_name].max_delta_t_28e5=np.average(delta_t_28e5_low_2_high[-10:])
        sp_sch[sch_name].min_delta_t_28e5=np.average(delta_t_28e5_low_2_high[:10])
        delta_t_2847_low_2_high=sorted(sp_sch[sch_name].df.delta_t_2847_heat, key=float)
        sp_sch[sch_name].max_delta_t_2847=np.average(delta_t_2847_low_2_high[-10:])
        sp_sch[sch_name].min_delta_t_2847=np.average(delta_t_2847_low_2_high[:10])
        sp_sch[sch_name].df['norm_delta_t_28e5_heat'] = (sp_sch[sch_name].max_delta_t_28e5 -sp_sch[sch_name].df.delta_t_28e5_heat
            )/(sp_sch[sch_name].max_delta_t_28e5-sp_sch[sch_name].min_delta_t_28e5)
        sp_sch[sch_name].df['norm_delta_t_2847_heat']= (sp_sch[sch_name].max_delta_t_2847 -sp_sch[sch_name].df.delta_t_2847_heat
            )/(sp_sch[sch_name].max_delta_t_2847-sp_sch[sch_name].min_delta_t_2847)

        # get fitting coefficient for thermo suction sensor


        sp_sch[sch_name].df['cum_evap_te']=(sp_sch[sch_name].df['te'][0]-sp_sch[sch_name].df['te']
            )*constants.g2kg/sp_sch[sch_name].surface_area/constants.rhow_pure_water/sp_sch[sch_name].te_coef  
        sp_sch[sch_name].df['evap_rate_te']=np.append(np.diff(sp_sch[sch_name].df['cum_evap_te'] ),np.nan)/dt_s
        sp_sch[sch_name].df['cum_evap_tas606']=(sp_sch[sch_name].df['tas606'][0]-sp_sch[sch_name].df['tas606']
            )*constants.g2kg/sp_sch[sch_name].surface_area/constants.rhow_pure_water/sp_sch[sch_name].tas606_coef  
        sp_sch[sch_name].df['evap_rate_tas606']=np.append(np.diff(sp_sch[sch_name].df['cum_evap_tas606'] ),np.nan)/dt_s

        sp_sch[sch_name].df['cum_evap_commercial']=(sp_sch[sch_name].df['commercial'][0]-sp_sch[sch_name].df['commercial']
            )*constants.g2kg/sp_sch[sch_name].surface_area/constants.rhow_pure_water
        sp_sch[sch_name].df['evap_rate_commercial']=np.append(np.diff(sp_sch[sch_name].df['cum_evap_commercial'] ),np.nan)/dt_s
        
        total_water_depth=sp_sch[sch_name].por*sp_sch[sch_name].soil_thickness
        sp_sch[sch_name].df['sat_commercial']=(total_water_depth-(
            sp_sch[sch_name].df['cum_evap_commercial']-sp_sch[sch_name].df['cum_evap_commercial'][sp_sch[sch_name].idx_surface_emerge])
            )/total_water_depth

        sp_sch[sch_name].df['sat_commercial'][sp_sch[sch_name].df['sat_commercial']>1]=1

        sp_sch[sch_name].df['saltrh_2_suction']=-np.log(0.01*sp_sch[sch_name].df['saltrh_2_rh'])*constants.R*(constants.kelvin+sp_sch[sch_name].df['saltrh_2_tp']
           )/constants.g/constants.molecular_weight_water     
        sp_sch[sch_name].df['saltrh_3_suction']=-np.log(0.01*sp_sch[sch_name].df['saltrh_3_rh'])*constants.R*(constants.kelvin+sp_sch[sch_name].df['saltrh_3_tp']
           )/constants.g/constants.molecular_weight_water     



        sp_sch[sch_name].df['suc_commercial']=constants.swcc_reverse_fredlund_xing_1994(vwc=sp_sch[sch_name].df.sat_commercial*sp_sch[sch_name].por,**swcc_coef)
        sp_sch[sch_name].df['mo_7_suction']=sensorfun.dielectric_suction_fit(x=sp_sch[sch_name].df  ['mo_7'],**mo_7_coef)
        sp_sch[sch_name].df['mo_8_suction']=sensorfun.dielectric_suction_fit(x=sp_sch[sch_name].df  ['mo_8'],**mo_8_coef)
        sp_sch[sch_name].df['mo_9_moisture']=sensorfun.dielectric_moisture_fit(x=sp_sch[sch_name].df  ['mo_9'],**mo_9_coef)
        sp_sch[sch_name].df['mo_10_moisture']=sensorfun.dielectric_moisture_fit(x=sp_sch[sch_name].df  ['mo_10'],**mo_10_coef)
        
        
        if sch_name=='coal_third':  # do only at the third
            x_inp=np.concatenate([np.array(sp_sch['coal_third'].df['norm_delta_t_2847_heat']),np.array(sp_sch['coal_second'].df['norm_delta_t_2847_heat'])])
            y_inp=np.log(np.concatenate([np.array(sp_sch['coal_third'].df['suc_commercial']),np.array(sp_sch['coal_second'].df['suc_commercial'])]))
            idx = np.isfinite(x_inp) & np.isfinite(y_inp)
            
            c=np.polyfit(x_inp[idx],y_inp[idx],1)
            thermal_suction_2847_norm_temp=np.arange(0,1,0.02)
            thermal_suction_2847_suction=np.exp(c[0]*thermal_suction_2847_norm_temp+c[1])
        c=np.array([-13.70,13.76])
        sp_sch[sch_name].df['suht_2847_suction']=np.exp(c[0]*sp_sch[sch_name].df['norm_delta_t_2847_heat']+c[1])
        sp_sch[sch_name].df['suht_28e5_suction']=np.exp(c[0]*sp_sch[sch_name].df['norm_delta_t_28e5_heat']+c[1])

##particular sorting for case 1
#
#
sp_sch['coal_first'].df['sat_commercial']-=0.7

lw=4
ms=7
mew=4
grid_width=2
y_fontsize=20
# this script is used for calibrating load cells
import matplotlib.pylab as pylab
params = {'legend.fontsize': 13,
          'figure.figsize': (10, 5),
         'axes.labelsize': 12,
         'axes.titlesize':'x-large',
         'xtick.labelsize':'20',
         'ytick.labelsize':'20',
#         'ytick.labelweight':'bold',
          'axes.labelsize': 16,
           'axes.labelweight':'bold'}
#         'axes.grid':'linewidth=grid_width,color = '0.5''}
#         'linewidth':lw,'markers.size':ms,'markers.edgewidth':mew}
plt.rcParams["font.weight"] = "bold"
plt.rcParams["axes.labelweight"] = "bold"
pylab.rcParams.update(params)


plot_fredlund_calibration=True
plot_moisture_calibration=False
plot_temphum_calibration=False
plot_dielectric_suction_calibration=True
plot_moisture_calibration_onefig=True
plot_volumetric_content_vs_suction=True
plot_fredlund_calibration_suction=True

if plot_volumetric_content_vs_suction:
    

    fig=figlib.single_fig_initialise() 
    fig.subplots_adjust(left=0.2, right=0.98, top=0.99, bottom=0.17)

    #[vwc_fred_xing,suction_fred_xing_kpa]=constants.swcc_fredlund_xing_1994(plot=False,por=0.37,af=2.1,nf=1.8,mf=1.4,hr=2.e6) 
    [vwc_fred_xing,suction_fred_xing_kpa]=constants.swcc_fredlund_xing_1994(plot=False,**swcc_coef) 
    


    sch_name='coal_second'
    plt.semilogx(sp_sch[sch_name].df ['suht_2847_suction'],   sp_sch[sch_name].por*sp_sch[sch_name].df ['sat_commercial'], 'o',mfc='none' ,markeredgecolor='r',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Ther. suc. sen. A, coal tail. exp. 1') 
    plt.semilogx(sp_sch[sch_name].df ['suht_28e5_suction'], sp_sch[sch_name].por*sp_sch[sch_name].df ['sat_commercial'], 'o',mfc='none' ,markeredgecolor='b',markersize=ms,markeredgewidth=mew,fillstyle='full',label='Ther. suc. sen. B, coal tail. exp. 1') 
    plt.semilogx(sp_sch[sch_name].df ['mo_7_suction'],   sp_sch[sch_name].por*sp_sch[sch_name].df ['sat_commercial'], 'o',mfc='none' ,markeredgecolor='k',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Diel. suc. sen. A, coal tail. exp. 1') 
    plt.semilogx(sp_sch[sch_name].df ['mo_8_suction'] , sp_sch[sch_name].por*sp_sch[sch_name].df ['sat_commercial'], 'o',mfc='none' ,markeredgecolor='brown',markersize=ms,markeredgewidth=mew,fillstyle='full',label='Diel. suc. sen. B, coal tail. exp. 1') 

    sch_name='coal_third'
    plt.semilogx(sp_sch[sch_name].df ['suht_2847_suction'],   sp_sch[sch_name].por*sp_sch[sch_name].df ['sat_commercial'], 'x',mfc='none' ,markeredgecolor='r',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Ther. suc. sen. A, coal tail. exp. 2') 
    plt.semilogx(sp_sch[sch_name].df ['suht_28e5_suction'], sp_sch[sch_name].por*sp_sch[sch_name].df ['sat_commercial'], 'x',mfc='none' ,markeredgecolor='b',markersize=ms,markeredgewidth=mew,fillstyle='full',label='Ther. suc. sen. B, coal tail. exp. 2') 
    plt.semilogx(sp_sch[sch_name].df   ['mo_7_suction'] ,sp_sch[sch_name].por*sp_sch[sch_name].df ['sat_commercial'], 'x',mfc='none' ,markeredgecolor='k',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Diel. suc. sen. A, coal tail. exp. 2') 
    plt.semilogx(sp_sch[sch_name].df  ['mo_8_suction'], sp_sch[sch_name].por*sp_sch[sch_name].df ['sat_commercial'], 'x',mfc='none' ,markeredgecolor='brown',markersize=ms,markeredgewidth=mew,fillstyle='full',label='Diel. suc. sen. B, coal tail. exp. 2') 
    plt.semilogx(suction_fred_xing_kpa, vwc_fred_xing, 'c-',mfc='none' ,markeredgecolor='c',markersize=ms,markeredgewidth=mew,fillstyle='full',linewidth=lw,label='Fredlund SWCC device') 

    plt.ylabel('VOLUMETRIC WATER CONTENT\nFROM BALANCE', fontsize=y_fontsize, labelpad=10)
    plt.xlabel('SUCTION (kPa)', fontsize=y_fontsize, labelpad=10)

    plt.legend(bbox_to_anchor=(.4, 0.99), loc=2, borderaxespad=0.,fontsize=12)
    #plt.grid(linewidth=grid_width,color = '0.5')
    plt.grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')

    plt.xlim([1e-2,1e7])
    #plt.show(block=False)
    
    fig.savefig('plot_volumetric_content_vs_suction.png', format='png', dpi=300)
    
    plt.close()  # it is all caused by pywafo. 
    np.savetxt("plot_volumetric_content_vs_suction.csv", [sp_sch[sch_name].df  ['mo_7_suction'],sp_sch[sch_name].df ['sat_commercial'],  sp_sch[sch_name].df  ['mo_8_suction'],sp_sch[sch_name].df ['sat_commercial']]
    , delimiter=",")

    header = ["mo_7_suction", "mo_8_suction", "suc_commercial", "mo_7_suction","mo_7_suction"]
    sch_name='coal_second'
    sp_sch[sch_name].df.to_csv('plot_volumetric_content_vs_suction_'+sch_name+'.csv', columns = header)
    sch_name='coal_third'
    sp_sch[sch_name].df.to_csv('plot_volumetric_content_vs_suction_'+sch_name+'.csv', columns = header)

if plot_moisture_calibration_onefig:
    fig=figlib.single_fig_initialise() 
    sch_name='coal_second'
    i=25 # this is the best as tested
    c=np.polyfit(sp_sch[sch_name].df ['mo_9'],sp_sch[sch_name].por*sp_sch[sch_name].df ['sat_commercial'],i)
    y=0
    for ind,key in enumerate(c):
        y+=key*sp_sch[sch_name].df ['mo_9']**(i-ind)
    sp_sch[sch_name].df['mo_9_vwc']=y
    sch_name='coal_third'
    y=0
    for ind,key in enumerate(c):
        y+=key*sp_sch[sch_name].df ['mo_9']**(i-ind)
    sp_sch[sch_name].df['mo_9_vwc']=y
    sp_sch[sch_name].df['mo_9_vwc'][sp_sch[sch_name].df['mo_9_vwc']<0]=0
    sp_sch[sch_name].df['mo_9_vwc'][sp_sch[sch_name].df['mo_9_vwc']>sp_sch[sch_name].por]=sp_sch[sch_name].por
 


    sch_name='coal_second'
    ii=20 # this is the best as tested
    cc=np.polyfit(sp_sch[sch_name].df ['mo_10'],sp_sch[sch_name].por*sp_sch[sch_name].df ['sat_commercial'],ii)
    y=0
    for ind,key in enumerate(cc):
        y+=key*sp_sch[sch_name].df ['mo_10']**(ii-ind)
    sp_sch[sch_name].df['mo_10_vwc']=y
    sch_name='coal_third'
    y=0 
    for ind,key in enumerate(cc):
        y+=key*sp_sch[sch_name].df ['mo_10']**(ii-ind)
    sp_sch[sch_name].df['mo_10_vwc']=y
    sp_sch[sch_name].df['mo_10_vwc'][sp_sch[sch_name].df['mo_10_vwc']<0]=0
    sp_sch[sch_name].df['mo_10_vwc'][sp_sch[sch_name].df['mo_10_vwc']>sp_sch[sch_name].por]=sp_sch[sch_name].por
    
    #a=sp_sch[sch_name].df ['mo_9']
    #b=sp_sch[sch_name].por*sp_sch[sch_name].df ['sat_commercial']
    #aa=sp_sch[sch_name].df ['mo_10']
    #i=25 # this is the best as tested
    #c=np.polyfit(a,b,i)
    #y=0
    #for ind,key in enumerate(c):
    #    y+=key*a**(i-ind)
   
    #ii=20 # this is the best as tested
    #cc=np.polyfit(aa,b,ii)
    #yy=0
    #for ind,key in enumerate(cc):
    #    yy+=key*aa**(ii-ind)

    #plt.plot(a,y, 'c-',mfc='none' ,markeredgecolor='c',markersize=ms,markeredgewidth=mew,fillstyle='full',linewidth=lw,label='Fredlund SWCC device') 
    #plt.plot(aa,yy, 'k-',mfc='none' ,markeredgecolor='k',markersize=ms,markeredgewidth=mew,fillstyle='full',linewidth=lw,label='Fredlund SWCC device') 
    sch_name='coal_second'

    #plt.plot(sp_sch[sch_name].df ['mo_9'], sp_sch[sch_name].df ['mo_9_vwc'] ,'k-',mfc='none' ,markeredgecolor='c',markersize=ms,markeredgewidth=mew,fillstyle='full',linewidth=lw,label='Fredlund SWCC device') 
    #plt.plot(sp_sch[sch_name].df ['mo_10'], sp_sch[sch_name].df ['mo_10_vwc'] ,'m-',mfc='none' ,markeredgecolor='c',markersize=ms,markeredgewidth=mew,fillstyle='full',linewidth=lw,label='Fredlund SWCC device') 
    plt.plot(sp_sch[sch_name].df ['mo_9'], sp_sch[sch_name].df ['mo_9_moisture']*sp_sch[sch_name].por ,'-',color='k',mfc='none' ,markeredgecolor='c',markersize=ms,markeredgewidth=mew,fillstyle='full',linewidth=lw,label='Dielectric moisture sensor A, cali. curve,\ny = ((x-336.0)/5.0)^(-1.05)') 
    plt.plot(sp_sch[sch_name].df ['mo_10'], sp_sch[sch_name].df ['mo_10_moisture']*sp_sch[sch_name].por ,'-',color='brown',mfc='none' ,markeredgecolor='c',markersize=ms,markeredgewidth=mew,fillstyle='full',linewidth=lw,label='Dielectric moisture sensor B, cali. curve,\ny = ((x-330.0)/5.0)^(-1.05)') 
    plt.plot(sp_sch[sch_name].df ['mo_9'],   sp_sch[sch_name].por*sp_sch[sch_name].df ['sat_commercial'], 'o',mfc='none' ,markeredgecolor='k',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Dielectric moisture sensor A,\ncoal tailings experiment 1',markevery=4) 
    plt.plot(sp_sch[sch_name].df ['mo_10'] , sp_sch[sch_name].por*sp_sch[sch_name].df ['sat_commercial'], 'o',mfc='none' ,markeredgecolor='brown',markersize=ms,markeredgewidth=mew,fillstyle='full',label='Dielectric moisture sensor B,\ncoal tailings experiment 1',markevery=4) 

    #plt.plot(sp_sch[sch_name].df ['mo_9'], sp_sch[sch_name].df ['mo_9_moisture']*sp_sch[sch_name].por ,'c-',mfc='none' ,markeredgecolor='c',markersize=ms,markeredgewidth=mew,fillstyle='full',linewidth=lw,label='y = ((x-330.0)/5.0)^(-0.9)' ) 
    sch_name='coal_third'
    #plt.plot(sp_sch[sch_name].df ['mo_9'], sp_sch[sch_name].df ['mo_9_vwc'] ,'r-',mfc='none' ,markeredgecolor='c',markersize=ms,markeredgewidth=mew,fillstyle='full',linewidth=lw,label='Fredlund SWCC device') 
    #plt.plot(sp_sch[sch_name].df ['mo_10'], sp_sch[sch_name].df ['mo_10_vwc'] ,'b-',mfc='none' ,markeredgecolor='c',markersize=ms,markeredgewidth=mew,fillstyle='full',linewidth=lw,label='Fredlund SWCC device') 
    plt.plot(sp_sch[sch_name].df  ['mo_9'] ,sp_sch[sch_name].por*sp_sch[sch_name].df ['sat_commercial'], 'x',mfc='none' ,markeredgecolor='k',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Dielectric moisture sensor A,\ncoal tailings experiment 2') 
    plt.plot(sp_sch[sch_name].df  ['mo_10'], sp_sch[sch_name].por*sp_sch[sch_name].df ['sat_commercial'], 'x',mfc='none' ,markeredgecolor='brown',markersize=ms,markeredgewidth=mew,fillstyle='full',label='Dielectric moisture sensor B,\ncoal tailings experiment 2') 

    
    plt.ylabel('VOLUMETRIC WATER CONTENT\nFROM BALANCE', fontsize=y_fontsize, labelpad=10)
    plt.xlabel('RAW READING FROM \n DIELECTRIC MOISTURE SENSORS ', fontsize=y_fontsize, labelpad=10)
    plt.legend(bbox_to_anchor=(.3, 0.99), loc=2, borderaxespad=0.,fontsize=12)
    plt.grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    plt.ylim([-0.05,0.41])
    
    
    fig.savefig('plot_moisture_calibration.png', format='png', dpi=300)
    plt.close()  # it is all caused by pywafo. 
    
    
    header = ["mo_9", "mo_10", "sat_commercial"]
    sch_name='coal_second'
    sp_sch[sch_name].df.to_csv('plot_moisture_calibration_'+sch_name+'.csv', columns = header)
    sch_name='coal_third'
    sp_sch[sch_name].df.to_csv('plot_moisture_calibration_'+sch_name+'.csv', columns = header)

if plot_dielectric_suction_calibration:

    #i=25 # this is the best as tested
    #c=np.polyfit(sp_sch[sch_name].df ['mo_7'][97:],sp_sch[sch_name].por*sp_sch[sch_name].df ['suc_commercial'][97:],i)
    #y=0
    #for ind,key in enumerate(c):
    #    y+=key*sp_sch[sch_name].df ['mo_7']**(i-ind)
    #sp_sch[sch_name].df['mo_7_suction']=y
    #sch_name='coal_third'
    #y=0
    #for ind,key in enumerate(c):
    #    y+=key*sp_sch[sch_name].df ['mo_7']**(i-ind)
    #sp_sch[sch_name].df['mo_7_suction']=y
    ##sp_sch[sch_name].df['mo_7_suction'][sp_sch[sch_name].df['mo_7_suction']<0]=0
    ##sp_sch[sch_name].df['mo_7_suction'][sp_sch[sch_name].df['mo_7_suction']>1e7]=1e7
 


    #sch_name='coal_second'
    #ii=20 # this is the best as tested
    #cc=np.polyfit(sp_sch[sch_name].df ['mo_8'][97:],sp_sch[sch_name].por*sp_sch[sch_name].df ['suc_commercial'][97:],ii)
    #y=0
    #for ind,key in enumerate(cc):
    #    y+=key*sp_sch[sch_name].df ['mo_8']**(ii-ind)
    #sp_sch[sch_name].df['mo_8_suction']=y
    #sch_name='coal_third'
    #y=0 
    #for ind,key in enumerate(cc):
    #    y+=key*sp_sch[sch_name].df ['mo_8']**(ii-ind)
    #sp_sch[sch_name].df['mo_8_suction']=y
    #sp_sch[sch_name].df['mo_8_suction'][sp_sch[sch_name].df['mo_8_suction']<0]=0
    #sp_sch[sch_name].df['mo_8_suction'][sp_sch[sch_name].df['mo_8_suction']>sp_sch[sch_name].por]=sp_sch[sch_name].por
    fig=figlib.single_fig_initialise() 
    fig.subplots_adjust(left=0.15, right=0.98, top=0.98, bottom=0.12)
    
    sch_name='coal_second'
    plt.semilogy(sp_sch[sch_name].df  ['mo_7'] ,sp_sch[sch_name].df ['suc_commercial'], 'o',mfc='none' ,markeredgecolor='k',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Diel. suc. sen. A, coal tail. exp. 1') 
    plt.semilogy(sp_sch[sch_name].df  ['mo_8'], sp_sch[sch_name].df ['suc_commercial'], 'o',mfc='none' ,markeredgecolor='brown',markersize=ms,markeredgewidth=mew,fillstyle='full',label='Diel. suc. sen. B, coal tail. exp. 1') 
    plt.semilogy(sp_sch[sch_name].df  ['mo_7'], sp_sch[sch_name].df  ['mo_7_suction'] , 'k-',mfc='none' ,markeredgecolor='k',markersize=ms,markeredgewidth=mew,fillstyle='full',label='Diel. suc. sen. A, calibration curve',linewidth=lw) 
    sch_name='coal_third'
    plt.semilogy(sp_sch[sch_name].df  ['mo_7'] ,sp_sch[sch_name].df ['suc_commercial'], 'x',mfc='none' ,markeredgecolor='k',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Diel. suc. sen. A, coal tail. exp. 2') 
    plt.semilogy(sp_sch[sch_name].df  ['mo_8'], sp_sch[sch_name].df ['suc_commercial'], 'x',mfc='none' ,markeredgecolor='brown',markersize=ms,markeredgewidth=mew,fillstyle='full',label='Diel. suc. sen. A, coal tail. exp. 2') 
    plt.semilogy(sp_sch[sch_name].df  ['mo_8'], sp_sch[sch_name].df  ['mo_8_suction'] , '-',mfc='none' ,markeredgecolor='brown',color='brown',markersize=ms,markeredgewidth=mew,fillstyle='full',label='Diel. suc. sen. B, calibration curve',linewidth=lw) 
    
    #plt.semilogy(sp_sch[sch_name].df  ['mo_10'], np.exp(0.1*( sp_sch[sch_name].df  ['mo_10']-400 )), 'c-',mfc='none' ,markeredgecolor='c',markersize=ms,markeredgewidth=mew,fillstyle='full',label='Temp. Humi. B, experiment 2') 

    #plt.semilogx(sp_sch[sch_name].df  ['saltrh_2_suction'] ,sp_sch[sch_name].df ['sat_commercial'], 'x' ,markeredgecolor='k',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Temp. Humi. A, experiment 2') 
    #plt.semilogx(sp_sch[sch_name].df  ['saltrh_11_suction'] ,sp_sch[sch_name].df ['sat_commercial'], 'x' ,markeredgecolor='brown',markersize=ms,markeredgewidth=mew,fillstyle='full',label='Temp. Humi. B, experiment 2') 
    plt.xlabel('RAW READING (m)', fontsize=y_fontsize, labelpad=10)
    plt.ylabel('SUCTION (kPa)', fontsize=y_fontsize, labelpad=10)
    plt.legend(bbox_to_anchor=(.05, 0.98), loc=2, borderaxespad=0.,fontsize=12)
    #plt.grid(linewidth=grid_width,color = '0.5')
    plt.grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    plt.axhline(y=1000,xmin=-1,xmax=2,c='0.2',linewidth=3,zorder=0)
    plt.text(200, 2000, 'Air entry pressure\n10 bar', fontsize=15)

    plt.ylim([1,1e7])
    #plt.show(block=False)
    
    fig.savefig('plot_dielectric_suction_calibration.png', format='png', dpi=300)
    plt.close()  # it is all caused by pywafo. 
    
    header = ["mo_7", "mo_8", "suc_commercial", "mo_7_suction","mo_7_suction"]
    sch_name='coal_second'
    sp_sch[sch_name].df.to_csv('plot_dielectric_suction_calibration_'+sch_name+'.csv', columns = header)
    sch_name='coal_third'
    sp_sch[sch_name].df.to_csv('plot_dielectric_suction_calibration_'+sch_name+'.csv', columns = header)

if plot_temphum_calibration:
    fig = plt.figure(figsize=(12,10))
    lw=4
    ms=3
    mew=4
    grid_width=2
    y_fontsize=20

    ax = fig.add_subplot(111)

    # you can change each line separately, like:
    #ax.spines['right'].set_linewidth(0.5)
    # to change all, just write:
    
    for axis in ['top','bottom','left','right']:
      ax.spines[axis].set_linewidth(2) 
    
    sch_name='coal_first'
    plt.semilogy(sp_sch[sch_name].df ['sat_commercial'], sp_sch[sch_name].df  ['saltrh_2_suction'] ,'bo' ,markeredgecolor='b',markersize=ms,markeredgewidth=mew,fillstyle='full',markevery=2,label= 'Temp. Humi. A, experiment 1') 
    plt.semilogy(sp_sch[sch_name].df ['sat_commercial'], sp_sch[sch_name].df  ['saltrh_3_suction'] ,'ko' ,markeredgecolor='k',markersize=ms,markeredgewidth=mew,fillstyle='full',markevery=2,label='Temp. Humi. B, experiment 1') 
    sch_name='coal_second'
    plt.semilogy(sp_sch[sch_name].df ['sat_commercial'], sp_sch[sch_name].df  ['saltrh_2_suction'] ,'bs' ,markeredgecolor='b',markersize=ms,markeredgewidth=mew,fillstyle='full',markevery=2,label= 'Temp. Humi. A, experiment 2') 
    plt.semilogy(sp_sch[sch_name].df ['sat_commercial'], sp_sch[sch_name].df  ['saltrh_3_suction'] ,'ks' ,markeredgecolor='k',markersize=ms,markeredgewidth=mew,fillstyle='full',markevery=2,label='Temp. Humi. B, experiment 2') 
    sch_name='coal_third'
    plt.semilogy(sp_sch[sch_name].df ['sat_commercial'], sp_sch[sch_name].df  ['saltrh_2_suction'] ,'bv' ,markeredgecolor='b',markersize=ms,markeredgewidth=mew,fillstyle='full',markevery=2,label= 'Temp. Humi. A, experiment 3') 
    plt.semilogy(sp_sch[sch_name].df ['sat_commercial'], sp_sch[sch_name].df  ['saltrh_3_suction'] ,'kv' ,markeredgecolor='k',markersize=ms,markeredgewidth=mew,fillstyle='full',markevery=2,label='Temp. Humi. B, experiment 3') 
    plt.ylabel('SOIL SUCTION (M)', fontsize=y_fontsize, labelpad=10)
    plt.xlabel('DEGREE OF SATURATION (-)', fontsize=y_fontsize, labelpad=10)
    plt.legend(bbox_to_anchor=(.5, 0.98), loc=2, borderaxespad=0.,fontsize=15)
    #plt.grid(linewidth=grid_width,color = '0.5')
    plt.grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    plt.xlim([-0.05,1])
    plt.show(block=False)
    
    fig.savefig('plot_temperature_humidity_calibration.png', format='png', dpi=500)

if plot_fredlund_calibration_suction:
    
    fig=figlib.single_fig_initialise() 
    
    sch_name='coal_second'
    plt.semilogy(sp_sch[sch_name].df['norm_delta_t_2847_heat']   ,sp_sch[sch_name].df ['suc_commercial'], 'o',mfc='none' ,markeredgecolor='k',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Ther. suc. sensor A, coal tailings exp. 1') 
    plt.semilogy(sp_sch[sch_name].df['norm_delta_t_28e5_heat'] , sp_sch[sch_name].df ['suc_commercial'], 'o',mfc='none' ,markeredgecolor='brown',markersize=ms,markeredgewidth=mew,fillstyle='full',label='Ther. suc. sensor B, coal tailings exp. 1') 

    sch_name='coal_third'
    plt.semilogy(sp_sch[sch_name].df.norm_delta_t_2847_heat ,sp_sch[sch_name].df ['suc_commercial'], 'x',mfc='none' ,markeredgecolor='k',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Ther. suc. sensor A, coal tailings exp. 2') 
    plt.semilogy(sp_sch[sch_name].df.norm_delta_t_28e5_heat, sp_sch[sch_name].df ['suc_commercial'], 'x',mfc='none' ,markeredgecolor='brown',markersize=ms,markeredgewidth=mew,fillstyle='full',label='Ther. suc. sensor B, coal tailings exp. 2') 
    
    plt.semilogy(thermal_suction_2847_norm_temp,thermal_suction_2847_suction, 'c-',mfc='none' ,markeredgecolor='r',markersize=ms,markeredgewidth=mew,fillstyle='full',linewidth=lw,label='y = '+'%.2f' % c[0]+'x + '+'%.2f' % c[1]) 

    
    
    plt.xlabel('NORMALIZED TEMPERATURE (-)', fontsize=y_fontsize, labelpad=10)
    plt.ylabel('SUCTION (kPa)', fontsize=y_fontsize, labelpad=10)
    plt.legend(bbox_to_anchor=(.3, 0.98), loc=2, borderaxespad=0.,fontsize=12)
    plt.grid(linewidth=grid_width,c = '0.5')
    
    plt.axhline(y=50,xmin=-1,xmax=2,c='0.2',linewidth=3,zorder=0)
    plt.text(0.00, 70, 'Air entry pressure', fontsize=15)

    
    plt.show(block=False)
    plt.close()
    
    fig.savefig('plot_fredlund_calibration_suction.png', format='png', dpi=300)
    header = ["norm_delta_t_2847_heat", "norm_delta_t_28e5_heat", "suc_commercial"]
    sch_name='coal_second'
    sp_sch[sch_name].df.to_csv('plot_fredlund_calibration_suction_'+sch_name+'.csv', columns = header)
    sch_name='coal_third'
    sp_sch[sch_name].df.to_csv('plot_fredlund_calibration_suction_'+sch_name+'.csv', columns = header)

if plot_fredlund_calibration:

    fig = plt.figure(figsize=(12,12))
    ax = fig.add_subplot(111)
    #fig, ax = plt.subplots(2,sharex=True,figsize=(12,16))
    
    lw=4
    ms=7
    mew=4
    grid_width=2
    y_fontsize=20
    
    for axis in ['top','bottom','left','right']:
      ax.spines[axis].set_linewidth(2) 
    
    sch_name='coal_second'
    #ax[0].plot(sp_sch[sch_name].df ['sat_commercial'], sp_sch[sch_name].df  .norm_delta_t_28e5_heat ,'gs',markeredgecolor='g',markersize=ms,markeredgewidth=mew,fillstyle='full',label='Dielectric suction A, experiment 2') 
    plt.plot(sp_sch[sch_name].df ['sat_commercial'], sp_sch[sch_name].df  .norm_delta_t_2847_heat ,'o',color='brown',mfc='none' ,markeredgecolor='brown',markersize=ms,markeredgewidth=mew,fillstyle='full',label='Coal tailings experiment 1') 
    sch_name='coal_third'
    #ax[0].plot(sp_sch[sch_name].df ['sat_commercial'], sp_sch[sch_name].df  .norm_delta_t_28e5_heat ,'bv',markeredgecolor='b',markersize=ms,markeredgewidth=mew,fillstyle='full',label='Dielectric suction A, experiment 3') 
    plt.plot(sp_sch[sch_name].df ['sat_commercial'], sp_sch[sch_name].df  .norm_delta_t_2847_heat ,'x',markeredgecolor='k',markersize=ms,markeredgewidth=mew,fillstyle='full',label='Coal tailings experiment 2') 
    
    #ax[0].set_ylabel('NORMALIZED\nTEMPERATURE (-)', fontsize=y_fontsize, labelpad=10)
    plt.ylabel('NORMALIZED TEMPERATURE (-)', fontsize=y_fontsize, labelpad=10)
    plt.xlabel('DEGREE OF SATURATION (-)', fontsize=y_fontsize, labelpad=10)
    #ax[0].legend(bbox_to_anchor=(.5, 0.3), loc=2, borderaxespad=0.,fontsize=15)
    plt.legend(bbox_to_anchor=(.5, 0.3), loc=2, borderaxespad=0.,fontsize=15)
    #ax[0].set_title('(A)',x=0.02,y=1.0)
    #plt.title('(B)',x=0.02,y=1.0)
    #ax[0].grid(linewidth=grid_width,color = '0.5')
    plt.grid(linewidth=grid_width,color = '0.5')
    #ax[0].set_ylim(-0.1,1.1)
    plt.ylim(-0.1,1.1)
    #ax[0].set_ylim(-0.1,1.1)
    plt.ylim(-0.01,1.01)
    
    plt.show(block=False)
    plt.close()
    
    fig.savefig('normalized_temperature.png', format='png', dpi=500)
#    fig, ax = plt.subplots(2,sharex=True,figsize=(12,16))
#    
#    lw=4
#    ms=3
#    mew=4
#    grid_width=2
#    y_fontsize=20
#    
#    for i in ax:
#      for axis in ['top','bottom','left','right']:
#        i.spines[axis].set_linewidth(2)
#    
#    #sch_name='coal_first'
#    #ax[0].plot(sp_sch[sch_name].df ['sat_commercial'], sp_sch[sch_name].df  .norm_delta_t_28e5_heat ,'ro' ,markeredgecolor='r',markersize=ms,markeredgewidth=mew,fillstyle='full',label='Dielectric suction A, experiment 1') 
#    #ax[1].plot(sp_sch[sch_name].df ['sat_commercial'], sp_sch[sch_name].df  .norm_delta_t_2847_heat ,'ro' ,markeredgecolor='r',markersize=ms,markeredgewidth=mew,fillstyle='full',label='Dielectric suction B, experiment 1') 
#    sch_name='coal_second'
#    ax[0].plot(sp_sch[sch_name].df ['sat_commercial'], sp_sch[sch_name].df  .norm_delta_t_28e5_heat ,'gs',markeredgecolor='g',markersize=ms,markeredgewidth=mew,fillstyle='full',label='Dielectric suction A, experiment 2') 
#    ax[1].plot(sp_sch[sch_name].df ['sat_commercial'], sp_sch[sch_name].df  .norm_delta_t_2847_heat ,'gs',markeredgecolor='g',markersize=ms,markeredgewidth=mew,fillstyle='full',label='Dielectric suction B, experiment 2') 
#    sch_name='coal_third'
#    ax[0].plot(sp_sch[sch_name].df ['sat_commercial'], sp_sch[sch_name].df  .norm_delta_t_28e5_heat ,'bv',markeredgecolor='b',markersize=ms,markeredgewidth=mew,fillstyle='full',label='Dielectric suction A, experiment 3') 
#    ax[1].plot(sp_sch[sch_name].df ['sat_commercial'], sp_sch[sch_name].df  .norm_delta_t_2847_heat ,'bv',markeredgecolor='b',markersize=ms,markeredgewidth=mew,fillstyle='full',label='Dielectric suction B, experiment 3') 
#    
#    ax[0].set_ylabel('NORMALIZED\nTEMPERATURE (-)', fontsize=y_fontsize, labelpad=10)
#    ax[1].set_ylabel('NORMALIZED\nTEMPERATURE (-)', fontsize=y_fontsize, labelpad=10)
#    ax[1].set_xlabel('DEGREE OF SATURATION (-)', fontsize=y_fontsize, labelpad=10)
#    ax[0].legend(bbox_to_anchor=(.5, 0.3), loc=2, borderaxespad=0.,fontsize=15)
#    ax[1].legend(bbox_to_anchor=(.5, 0.3), loc=2, borderaxespad=0.,fontsize=15)
#    ax[0].set_title('(A)',x=0.02,y=1.0)
#    ax[1].set_title('(B)',x=0.02,y=1.0)
#    ax[0].grid(linewidth=grid_width,color = '0.5')
#    ax[1].grid(linewidth=grid_width,color = '0.5')
#    ax[0].set_ylim(-0.1,1.1)
#    ax[1].set_ylim(-0.1,1.1)
#    ax[0].set_ylim(-0.1,1.1)
#    ax[1].set_ylim(-0.01,1.01)
#    
#    plt.show(block=False)
#    
#    fig.savefig('normalized_temperature.png', format='png', dpi=500)
#fig, ax = plt.subplots(3,sharex=True,figsize=(12,16))
#
#lw=4
#ms=3
#mew=1.5
#grid_width=2
#y_fontsize=20
#
#for i in ax:
#  for axis in ['top','bottom','left','right']:
#    i.spines[axis].set_linewidth(2)
#
#sch_name='coal_first'
#ax[0].plot(sp_sch[sch_name].df ['sat_commercial'], sp_sch[sch_name].df  ['delta_t_28e5_heat'] ,'ro' ,markeredgecolor='r',markersize=ms,markeredgewidth=mew,fillstyle='full',label='Dielectric suction A, experiment 1') 
#ax[1].plot(sp_sch[sch_name].df ['sat_commercial'], sp_sch[sch_name].df  ['delta_t_2847_heat'] ,'go' ,markeredgecolor='g',markersize=ms,markeredgewidth=mew,fillstyle='full',label='Dielectric suction B, experiment 1') 
#sch_name='coal_second'
#ax[0].plot(sp_sch[sch_name].df ['sat_commercial'], sp_sch[sch_name].df  ['delta_t_28e5_heat'] ,'rs',markeredgecolor='r',markersize=ms,markeredgewidth=mew,fillstyle='full',label='Dielectric suction A, experiment 2') 
#ax[1].plot(sp_sch[sch_name].df ['sat_commercial'], sp_sch[sch_name].df  ['delta_t_2847_heat'] ,'gs',markeredgecolor='g',markersize=ms,markeredgewidth=mew,fillstyle='full',label='Dielectric suction B, experiment 2') 
#
#ax[0].set_ylabel('WEIGHT (G)', fontsize=y_fontsize, labelpad=10)
#ax[1].set_ylabel('RAW READING FROM \n DIELECTRIC SUCTION SENSORS ', fontsize=y_fontsize, labelpad=20)
#ax[2].set_xlabel('DEGREE OF SATURATION', fontsize=y_fontsize, labelpad=10)
#ax[0].legend(bbox_to_anchor=(.6, 0.98), loc=2, borderaxespad=0.,fontsize=15)
#ax[1].legend(bbox_to_anchor=(.02, 0.37), loc=2, borderaxespad=0.,fontsize=15)
#ax[0].set_title('(A)',x=0.02,y=1.0)
#ax[1].set_title('(B)',x=0.02,y=1.0)
#ax[0].grid(linewidth=grid_width,color = '0.5')
#ax[1].grid(linewidth=grid_width,color = '0.5')
#
#plt.show(block=False)


#
#
#
#
if plot_moisture_calibration:
    fig, ax = plt.subplots(2,sharex=False,figsize=(12,16))
    y_fontsize=20
    
    for i in ax:
      for axis in ['top','bottom','left','right']:
        i.spines[axis].set_linewidth(2)
    
    #sch_name='coal_first'
    #ax[1].plot(sp_sch[sch_name].df ['sat_commercial'], sp_sch[sch_name].df  ['mo_7'] ,'ro',markevery=2,markeredgecolor='r',markersize=ms,markeredgewidth=mew,fillstyle='full',label='Dielectric suction A, experiment 1') 
    #ax[1].plot(sp_sch[sch_name].df ['sat_commercial'], sp_sch[sch_name].df  ['mo_8'] ,'go',markevery=2,markeredgecolor='g',markersize=ms,markeredgewidth=mew,fillstyle='full',label='Dielectric suction B, experiment 1') 
    #ax[0].plot(sp_sch[sch_name].df ['sat_commercial'], sp_sch[sch_name].df  ['mo_9'] ,'bo',markevery=2,markeredgecolor='b',markersize=ms,markeredgewidth=mew,fillstyle='full',label='Moisture A, experiment 1') 
    #ax[0].plot(sp_sch[sch_name].df ['sat_commercial'], sp_sch[sch_name].df  ['mo_10'],'ko',markevery=2,markeredgecolor='k',markersize=ms,markeredgewidth=mew,fillstyle='full',label='Moisture B, experiment 1') 
    sch_name='coal_second'
    ax[1].plot(sp_sch[sch_name].df ['sat_commercial'], sp_sch[sch_name].df  ['mo_7'] ,'rs',markevery=2,markeredgecolor='r',markersize=ms,markeredgewidth=mew,fillstyle='full',label='Dielectric suction A, experiment 2') 
    ax[1].plot(sp_sch[sch_name].df ['sat_commercial'], sp_sch[sch_name].df  ['mo_8'] ,'gs',markevery=2,markeredgecolor='g',markersize=ms,markeredgewidth=mew,fillstyle='full',label='Dielectric suction B, experiment 2') 
    ax[0].plot(sp_sch[sch_name].df ['sat_commercial'], sp_sch[sch_name].df  ['mo_9'] ,'bs',markevery=2,markeredgecolor='b',markersize=ms,markeredgewidth=mew,fillstyle='full',label='Moisture A, experiment 2')
    ax[0].plot(sp_sch[sch_name].df ['sat_commercial'], sp_sch[sch_name].df  ['mo_10'],'ks',markevery=2,markeredgecolor='k',markersize=ms,markeredgewidth=mew,fillstyle='full',label='Moisture B, experiment 2')
    sch_name='coal_third'
    ax[1].plot(sp_sch[sch_name].df ['sat_commercial'], sp_sch[sch_name].df  ['mo_7'] ,'rv',markevery=2,markeredgecolor='r',markersize=ms,markeredgewidth=mew,fillstyle='full',label='Dielectric suction A, experiment 3') 
    ax[1].plot(sp_sch[sch_name].df ['sat_commercial'], sp_sch[sch_name].df  ['mo_8'] ,'gv',markevery=2,markeredgecolor='g',markersize=ms,markeredgewidth=mew,fillstyle='full',label='Dielectric suction B, experiment 3') 
    ax[0].plot(sp_sch[sch_name].df ['sat_commercial'], sp_sch[sch_name].df  ['mo_9'] ,'bv',markevery=2,markeredgecolor='b',markersize=ms,markeredgewidth=mew,fillstyle='full',label='Moisture A, experiment 3')
    ax[0].plot(sp_sch[sch_name].df ['sat_commercial'], sp_sch[sch_name].df  ['mo_10'],'kv',markevery=2,markeredgecolor='k',markersize=ms,markeredgewidth=mew,fillstyle='full',label='Moisture B, experiment 3')
    
    ax[0].set_ylabel('RAW READING FROM \n DIELECTRIC MOISTURE SENSORS ', fontsize=y_fontsize, labelpad=10)
    ax[1].set_ylabel('RAW READING FROM \n DIELECTRIC SUCTION SENSORS ', fontsize=y_fontsize, labelpad=20)
    ax[0].set_xlabel('DEGREE OF SATURATION', fontsize=y_fontsize, labelpad=10)
    ax[1].set_xlabel('DEGREE OF SATURATION', fontsize=y_fontsize, labelpad=10)
    ax[0].legend(bbox_to_anchor=(.6, 0.98), loc=2, borderaxespad=0.,fontsize=15)
    ax[1].legend(bbox_to_anchor=(.02, 0.37), loc=2, borderaxespad=0.,fontsize=15)
    ax[0].set_title('(A)',x=0.02,y=1.0)
    ax[1].set_title('(B)',x=0.02,y=1.0)
    ax[0].grid(linewidth=grid_width,color = '0.5')
    ax[1].grid(linewidth=grid_width,color = '0.5')
    
    plt.show(block=False)
    
    fig.savefig('plot_moisture_dielectric_suction_calibration.png', format='png', dpi=500)


#
## plot_delta_t_norm
#fig, ax = plt.subplots(2,sharex=False)
##sch_name='coal_first'
##ax[1].plot(sp_sch[sch_name].df ['sat_commercial'], sp_sch[sch_name].df  ['28e5_delta_t_norm'],'r+') 
##ax[1].plot(sp_sch[sch_name].df ['sat_commercial'], sp_sch[sch_name].df  ['2847_delta_t_norm'],'g+') 
#sch_name='coal_second' 
#ax[1].plot(sp_sch[sch_name].df ['sat_commercial'], sp_sch[sch_name].df  ['28e5_delta_t_norm'],'b+') 
#ax[1].plot(sp_sch[sch_name].df ['sat_commercial'], sp_sch[sch_name].df  ['2847_delta_t_norm'],'m+') 
#sch_name='coal_third' 
#ax[1].plot(sp_sch[sch_name].df ['sat_commercial'], sp_sch[sch_name].df  ['28e5_delta_t_norm'],'c+') 
#ax[1].plot(sp_sch[sch_name].df ['sat_commercial'], sp_sch[sch_name].df  ['2847_delta_t_norm'],'k+') 
#plt.show(block=False)


## plot_delta_t_norm
#fig, ax = plt.subplots(2,sharex=False)
#sch_name='coal_first'
#ax[1].plot(sp_sch[sch_name].df ['date_time'], sp_sch[sch_name].df  ['28e5_delta_t_norm'],'r+') 
#ax[1].plot(sp_sch[sch_name].df ['date_time'], sp_sch[sch_name].df  ['2847_delta_t_norm'],'g+') 
#sch_name='coal_second'                                                         
#ax[1].plot(sp_sch[sch_name].df ['date_time'], sp_sch[sch_name].df  ['28e5_delta_t_norm'],'r+') 
#ax[1].plot(sp_sch[sch_name].df ['date_time'], sp_sch[sch_name].df  ['2847_delta_t_norm'],'g+') 
#sch_name='coal_third'                                                          
#ax[1].plot(sp_sch[sch_name].df ['date_time'], sp_sch[sch_name].df  ['28e5_delta_t_norm'],'r+') 
#ax[1].plot(sp_sch[sch_name].df ['date_time'], sp_sch[sch_name].df  ['2847_delta_t_norm'],'g+') 
#plt.show(block=False)






## plot_delta_t
#fig, ax = plt.subplots(2,sharex=False)
#sch_name='coal_first'
#ax[1].plot(sp_sch[sch_name].df ['date_time'], sp_sch[sch_name].df  .delta_t_28e5_heat,'r+') 
#ax[1].plot(sp_sch[sch_name].df ['date_time'], sp_sch[sch_name].df  .delta_t_28e5_cool,'g+') 
#ax[1].plot(sp_sch[sch_name].df ['date_time'], sp_sch[sch_name].df  .delta_t_2847_heat,'bx') 
#ax[1].plot(sp_sch[sch_name].df ['date_time'], sp_sch[sch_name].df  .delta_t_2847_cool,'cx') 
#sch_name='coal_second'
#ax[1].plot(sp_sch[sch_name].df ['date_time'], sp_sch[sch_name].df  .delta_t_28e5_heat,'r+') 
#ax[1].plot(sp_sch[sch_name].df ['date_time'], sp_sch[sch_name].df  .delta_t_28e5_cool,'g+') 
#ax[1].plot(sp_sch[sch_name].df ['date_time'], sp_sch[sch_name].df  .delta_t_2847_heat,'bx') 
#ax[1].plot(sp_sch[sch_name].df ['date_time'], sp_sch[sch_name].df  .delta_t_2847_cool,'cx') 
#sch_name='coal_third'
#ax[1].plot(sp_sch[sch_name].df ['date_time'], sp_sch[sch_name].df  .delta_t_28e5_heat,'r+') 
#ax[1].plot(sp_sch[sch_name].df ['date_time'], sp_sch[sch_name].df  .delta_t_28e5_cool,'g+') 
#ax[1].plot(sp_sch[sch_name].df ['date_time'], sp_sch[sch_name].df  .delta_t_2847_heat,'bx') 
#ax[1].plot(sp_sch[sch_name].df ['date_time'], sp_sch[sch_name].df  .delta_t_2847_cool,'cx') 
#plt.show(block=False)




#sch_name='coal_first'
#ax[1].plot(sp_sch[sch_name].df ['sat_commercial'], sp_sch[sch_name].df  ['mo_7'],'r+') 
#ax[1].plot(sp_sch[sch_name].df ['sat_commercial'], sp_sch[sch_name].df  ['mo_8'],'g+') 
#ax[0].plot(sp_sch[sch_name].df ['sat_commercial'], sp_sch[sch_name].df  ['mo_9'],'b+') 
#ax[0].plot(sp_sch[sch_name].df ['sat_commercial'], sp_sch[sch_name].df  ['mo_10'],'c+') 
#sch_name='coal_second'
#ax[1].plot(sp_sch[sch_name].df ['sat_commercial'], sp_sch[sch_name].df  ['mo_7'] ,'ro') 
#ax[1].plot(sp_sch[sch_name].df ['sat_commercial'], sp_sch[sch_name].df  ['mo_8'] ,'go') 
#ax[0].plot(sp_sch[sch_name].df ['sat_commercial'], sp_sch[sch_name].df  ['mo_9'] ,'bo') 
#ax[0].plot(sp_sch[sch_name].df ['sat_commercial'], sp_sch[sch_name].df  ['mo_10'],'co') 
#sch_name='coal_third'
#ax[1].plot(sp_sch[sch_name].df ['sat_commercial'], sp_sch[sch_name].df  ['mo_7'] ,'rx') 
#ax[1].plot(sp_sch[sch_name].df ['sat_commercial'], sp_sch[sch_name].df  ['mo_8'] ,'gx') 
#ax[0].plot(sp_sch[sch_name].df ['sat_commercial'], sp_sch[sch_name].df  ['mo_9'] ,'bx') 
#ax[0].plot(sp_sch[sch_name].df ['sat_commercial'], sp_sch[sch_name].df  ['mo_10'],'cx') 
#plt.show(block=False)
##ax[0].plot(sp_sch['coal_second'].df['date_time'], sp_sch['coal_second'].df ['cum_evap_te']*constants.m2mm,'g+') 
##ax[0].plot(sp_sch['coal_third'].df ['date_time'], sp_sch['coal_third'].df  ['cum_evap_te']*constants.m2mm,'b+') 
#
#
#xfmt = mdates.DateFormatter('%y-%m-%d %H:%M')
#fig, ax = plt.subplots(2,sharex=False)
#ax[0].plot(sp_sch['coal_first'].df ['date_time'], sp_sch['coal_first'].df  ['cum_evap_te']*constants.m2mm,'r+') 
#ax[0].plot(sp_sch['coal_second'].df['date_time'], sp_sch['coal_second'].df ['cum_evap_te']*constants.m2mm,'g+') 
#ax[0].plot(sp_sch['coal_third'].df ['date_time'], sp_sch['coal_third'].df  ['cum_evap_te']*constants.m2mm,'b+') 
#ax[0].plot(sp_sch['coal_first'].df ['date_time'], sp_sch['coal_first'].df  ['cum_evap_tas606']*constants.m2mm,'ro') 
#ax[0].plot(sp_sch['coal_second'].df['date_time'], sp_sch['coal_second'].df ['cum_evap_tas606']*constants.m2mm,'go') 
#ax[0].plot(sp_sch['coal_third'].df ['date_time'], sp_sch['coal_third'].df  ['cum_evap_tas606']*constants.m2mm,'bo') 
#ax[0].plot(sp_sch['coal_second'].df['date_time'], sp_sch['coal_second'].df ['cum_evap_commercial']*constants.m2mm,'ko') 
#ax[0].plot(sp_sch['coal_third'].df ['date_time'], sp_sch['coal_third'].df  ['cum_evap_commercial']*constants.m2mm,'ko') 
#ax[0].xaxis.set_major_formatter(xfmt)
#
#ax[1].plot(sp_sch['coal_first'].df ['date_time'], sp_sch['coal_first'].df  ['evap_rate_te']*constants.ms2mmday,'r+') 
#ax[1].plot(sp_sch['coal_second'].df['date_time'], sp_sch['coal_second'].df ['evap_rate_te']*constants.ms2mmday,'g+') 
#ax[1].plot(sp_sch['coal_third'].df ['date_time'], sp_sch['coal_third'].df  ['evap_rate_te']*constants.ms2mmday,'b+') 
#ax[1].plot(sp_sch['coal_first'].df ['date_time'], sp_sch['coal_first'].df  ['evap_rate_tas606']*constants.ms2mmday,'ro') 
#ax[1].plot(sp_sch['coal_second'].df['date_time'], sp_sch['coal_second'].df ['evap_rate_tas606']*constants.ms2mmday,'go') 
#ax[1].plot(sp_sch['coal_third'].df ['date_time'], sp_sch['coal_third'].df  ['evap_rate_tas606']*constants.ms2mmday,'bo') 
#ax[1].plot(sp_sch['coal_second'].df['date_time'], sp_sch['coal_second'].df ['evap_rate_commercial']*constants.ms2mmday,'ko') 
#ax[1].plot(sp_sch['coal_third'].df ['date_time'], sp_sch['coal_third'].df  ['evap_rate_commercial']*constants.ms2mmday,'ko') 
#ax[1].xaxis.set_major_formatter(xfmt)
#plt.show(block=False)
#
#
#
#fig, ax = plt.subplots(2,sharex=False)
#ax[0].plot(sp_sch['coal_first'].df ['time_days'], sp_sch['coal_first'].df  ['cum_evap_te']*constants.m2mm,'r+',markevery=2) 
#ax[0].plot(sp_sch['coal_second'].df['time_days'], sp_sch['coal_second'].df ['cum_evap_te']*constants.m2mm,'g+',markevery=2) 
#ax[0].plot(sp_sch['coal_third'].df ['time_days'], sp_sch['coal_third'].df  ['cum_evap_te']*constants.m2mm,'b+',markevery=2) 
#ax[0].plot(sp_sch['coal_first'].df ['time_days'], sp_sch['coal_first'].df  ['cum_evap_tas606']*constants.m2mm,'ro',markevery=2) 
#ax[0].plot(sp_sch['coal_second'].df['time_days'], sp_sch['coal_second'].df ['cum_evap_tas606']*constants.m2mm,'go',markevery=2) 
#ax[0].plot(sp_sch['coal_third'].df ['time_days'], sp_sch['coal_third'].df  ['cum_evap_tas606']*constants.m2mm,'bo',markevery=2) 
#ax[0].plot(sp_sch['coal_second'].df['time_days'], sp_sch['coal_second'].df ['cum_evap_commercial']*constants.m2mm,'gv',markevery=2) 
#ax[0].plot(sp_sch['coal_third'].df ['time_days'], sp_sch['coal_third'].df  ['cum_evap_commercial']*constants.m2mm,'bv',markevery=2) 
#
#ax[1].plot(sp_sch['coal_first'].df ['time_days'], sp_sch['coal_first'].df  ['evap_rate_te']*constants.ms2mmday,'r+',markevery=2) 
#ax[1].plot(sp_sch['coal_second'].df['time_days'], sp_sch['coal_second'].df ['evap_rate_te']*constants.ms2mmday,'g+',markevery=2) 
#ax[1].plot(sp_sch['coal_third'].df ['time_days'], sp_sch['coal_third'].df  ['evap_rate_te']*constants.ms2mmday,'b+',markevery=2) 
#ax[1].plot(sp_sch['coal_first'].df ['time_days'], sp_sch['coal_first'].df  ['evap_rate_tas606']*constants.ms2mmday,'ro',markevery=2) 
#ax[1].plot(sp_sch['coal_second'].df['time_days'], sp_sch['coal_second'].df ['evap_rate_tas606']*constants.ms2mmday,'go',markevery=2) 
#ax[1].plot(sp_sch['coal_third'].df ['time_days'], sp_sch['coal_third'].df  ['evap_rate_tas606']*constants.ms2mmday,'bo',markevery=2) 
#ax[1].plot(sp_sch['coal_second'].df['time_days'], sp_sch['coal_second'].df ['evap_rate_commercial']*constants.ms2mmday,'gv',markevery=2) 
#ax[1].plot(sp_sch['coal_third'].df ['time_days'], sp_sch['coal_third'].df  ['evap_rate_commercial']*constants.ms2mmday,'bv',markevery=2) 
#plt.show(block=False)

