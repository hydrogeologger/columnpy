import operator
sp_sch={}
for line in open("schedule.ipt"):
    li=line.strip()
    if not li.startswith("#"):
        line_content=[x.strip() for x in li.split(',')]
        sch_name=line_content[2]
        sp_sch[sch_name]=pandas_scale.concat_data_roof(pd.datetime.strptime(line_content[0],'%Y/%b/%d %H:%M'),
            pd.datetime.strptime(line_content[1],'%Y/%b/%d %H:%M'),dt_s );
        sp_sch[sch_name].start_dt=pd.datetime.strptime(line_content[0],'%Y/%b/%d %H:%M')
        sp_sch[sch_name].end_dt=pd.datetime.strptime(line_content[1],'%Y/%b/%d %H:%M')
        plot_interpolate=False
        sp_sch[sch_name].merge_data(df=data.df, keys=['saltrh_2_rh']   ,plot=plot_interpolate  ,coef=5e-10)
        sp_sch[sch_name].merge_data( df=data.df, keys=['saltrh_11_rh'] ,plot=plot_interpolate  ,coef=5e-10)
        sp_sch[sch_name].merge_data( df=data.df, keys=['t_2896_begin'] ,plot=plot_interpolate  ,coef=5e-10)
        sp_sch[sch_name].merge_data( df=data.df, keys=['t_19_begin']   ,plot=plot_interpolate  ,coef=5e-10)
        sp_sch[sch_name].merge_data( df=data.df, keys=['t_14_begin']   ,plot=plot_interpolate  ,coef=5e-10)
        
        sp_sch[sch_name].merge_data( df=data.df, keys=['t_2896_peak']  ,plot=plot_interpolate  ,coef=5e-10)
        sp_sch[sch_name].merge_data( df=data.df, keys=['t_19_peak']    ,plot=plot_interpolate  ,coef=5e-10)
        sp_sch[sch_name].merge_data( df=data.df, keys=['t_14_peak']    ,plot=plot_interpolate  ,coef=5e-10)
        
        sp_sch[sch_name].merge_data( df=data.df, keys=['t_2896_end']   ,plot=plot_interpolate  ,coef=5e-10)
        sp_sch[sch_name].merge_data( df=data.df, keys=['t_19_end']     ,plot=plot_interpolate  ,coef=5e-10)
        sp_sch[sch_name].merge_data( df=data.df, keys=['t_14_end']     ,plot=plot_interpolate  ,coef=5e-10)
        
        sp_sch[sch_name].merge_data( df=data.df, keys=['saltrh_11_t']  ,plot=plot_interpolate  ,coef=5e-10)
        sp_sch[sch_name].merge_data( df=data.df, keys=['saltrh_2_t']   ,plot=plot_interpolate  ,coef=5e-10)
        
        sp_sch[sch_name].merge_data( df=data.df, keys=['mo_7']         ,plot=plot_interpolate  ,coef=5e-10)
        sp_sch[sch_name].merge_data( df=data.df, keys=['mo_8']         ,plot=plot_interpolate  ,coef=5e-10)
        sp_sch[sch_name].merge_data( df=data.df, keys=['mo_9']         ,plot=plot_interpolate  ,coef=5e-10)
        sp_sch[sch_name].merge_data( df=data.df, keys=['mo_10']        ,plot=plot_interpolate  ,coef=5e-10)
        
        sp_sch[sch_name].merge_data( df=data.df, keys=['te']           ,plot=plot_interpolate  ,coef=5e-13)
        sp_sch[sch_name].merge_data( df=data.df, keys=['tas606']       ,plot=plot_interpolate  ,coef=5e-10)
        sp_sch[sch_name].merge_data( df=data.df, keys=['commercial']   ,plot=plot_interpolate  ,coef=5e-10)

        sp_sch[sch_name].water_level   =float(line_content[3])
        sp_sch[sch_name].surface_area  =float(line_content[4])
        sp_sch[sch_name].soil_thickness=float(line_content[5])
        sp_sch[sch_name].time_surface_emerge = pd.datetime.strptime(line_content[10],'%Y/%b/%d %H:%M')

        sp_sch[sch_name].por=float(line_content[6])
        sp_sch[sch_name].te_coef=float(line_content[8])
        sp_sch[sch_name].tas606_coef=float(line_content[9])
        min_index, min_value = min(enumerate( abs(data.df['date_time']-sp_sch[sch_name].start_dt)), key=operator.itemgetter(1))
        sp_sch[sch_name].start_ind=min_index
        min_index, min_value = min(enumerate( abs(data.df['date_time']-sp_sch[sch_name].end_dt)), key=operator.itemgetter(1))
        sp_sch[sch_name].end_ind=min_index
        #sp_sch[sch_name].df.=data.df[sp_sch[sch_name]['start_ind']:sp_sch[sch_name]['end_ind']]
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

        sp_sch[sch_name].df['cum_evap_te']=(sp_sch[sch_name].df['te'][0]-sp_sch[sch_name].df['te']
            )*constants.g2kg/sp_sch[sch_name].surface_area/constants.rhow_pure_water/sp_sch[sch_name].te_coef  
        sp_sch[sch_name].df['evap_rate_te']=np.append(np.diff(sp_sch[sch_name].df['cum_evap_te'] ),np.nan)/dt_s
        sp_sch[sch_name].df['cum_evap_tas606']=(sp_sch[sch_name].df['tas606'][0]-sp_sch[sch_name].df['tas606']
            )*constants.g2kg/sp_sch[sch_name].surface_area/constants.rhow_pure_water/sp_sch[sch_name].tas606_coef  
        sp_sch[sch_name].df['evap_rate_tas606']=np.append(np.diff(sp_sch[sch_name].df['cum_evap_tas606'] ),np.nan)/dt_s

        sp_sch[sch_name].df['cum_evap_commercial']=(sp_sch[sch_name].df['commercial'][0]-sp_sch[sch_name].df['commercial']
            )*constants.g2kg/sp_sch[sch_name].surface_area/constants.rhow_pure_water
        sp_sch[sch_name].df['evap_rate_commercial']=np.append(np.diff(sp_sch[sch_name].df['cum_evap_commercial'] ),np.nan)/dt_s
        
        # calculate saturaturation based on commercial balance
        total_water_depth=sp_sch[sch_name].por*sp_sch[sch_name].soil_thickness
        sp_sch[sch_name].df['sat_commercial']=(total_water_depth-(
            sp_sch[sch_name].df['cum_evap_commercial']-sp_sch[sch_name].df['cum_evap_commercial'][sp_sch[sch_name].idx_surface_emerge])
            )/total_water_depth


        sp_sch[sch_name].df['sat_commercial'][sp_sch[sch_name].df['sat_commercial']>1]=1


fig, ax = plt.subplots(2,sharex=False)
sch_name='redmud_first'
ax[1].plot(sp_sch[sch_name].df ['sat_commercial'], sp_sch[sch_name].df  ['mo_7'],'r+') 
ax[1].plot(sp_sch[sch_name].df ['sat_commercial'], sp_sch[sch_name].df  ['mo_8'],'g+') 
ax[0].plot(sp_sch[sch_name].df ['sat_commercial'], sp_sch[sch_name].df  ['mo_9'],'b+') 
ax[0].plot(sp_sch[sch_name].df ['sat_commercial'], sp_sch[sch_name].df  ['mo_10'],'c+') 
sch_name='redmud_second'
ax[1].plot(sp_sch[sch_name].df ['sat_commercial'], sp_sch[sch_name].df  ['mo_7'] ,'ro') 
ax[1].plot(sp_sch[sch_name].df ['sat_commercial'], sp_sch[sch_name].df  ['mo_8'] ,'go') 
ax[0].plot(sp_sch[sch_name].df ['sat_commercial'], sp_sch[sch_name].df  ['mo_9'] ,'bo') 
ax[0].plot(sp_sch[sch_name].df ['sat_commercial'], sp_sch[sch_name].df  ['mo_10'],'co') 
plt.show(block=False)
#
#
# evaporation rate and potential evaporation, time as x axis
xfmt = mdates.DateFormatter('%y-%m-%d %H:%M')
fig, ax = plt.subplots(2,sharex=False)
ax[0].plot(sp_sch['redmud_first'].df ['date_time'], sp_sch['redmud_first'].df  ['cum_evap_te']*constants.m2mm,'r+') 
ax[0].plot(sp_sch['redmud_second'].df['date_time'], sp_sch['redmud_second'].df ['cum_evap_te']*constants.m2mm,'g+') 
ax[0].plot(sp_sch['redmud_first'].df ['date_time'], sp_sch['redmud_first'].df  ['cum_evap_commercial']*constants.m2mm,'ro') 
ax[0].plot(sp_sch['redmud_second'].df['date_time'], sp_sch['redmud_second'].df ['cum_evap_commercial']*constants.m2mm,'go') 
ax[0].xaxis.set_major_formatter(xfmt)

ax[1].plot(sp_sch['redmud_first'].df ['date_time'], sp_sch['redmud_first'].df  ['evap_rate_te']*constants.ms2mmday,'r+') 
ax[1].plot(sp_sch['redmud_second'].df['date_time'], sp_sch['redmud_second'].df ['evap_rate_te']*constants.ms2mmday,'g+') 
ax[1].plot(sp_sch['redmud_first'].df ['date_time'], sp_sch['redmud_first'].df  ['evap_rate_commercial']*constants.ms2mmday,'ro') 
ax[1].plot(sp_sch['redmud_second'].df['date_time'], sp_sch['redmud_second'].df ['evap_rate_commercial']*constants.ms2mmday,'go') 
ax[1].xaxis.set_major_formatter(xfmt)
plt.show(block=False)


# evaporation rate and potential evaporation, all start from zero
fig, ax = plt.subplots(2,sharex=False)
ax[0].plot(sp_sch['redmud_first'].df ['time_days'], sp_sch['redmud_first']. df ['cum_evap_te']*constants.m2mm,'r+',markevery=2) 
ax[0].plot(sp_sch['redmud_second'].df['time_days'], sp_sch['redmud_second'].df ['cum_evap_te']*constants.m2mm,'g+',markevery=2) 
ax[0].plot(sp_sch['redmud_first'].df['time_days'], sp_sch['redmud_first'].  df  ['cum_evap_commercial']*constants.m2mm,'rv',markevery=2) 
ax[0].plot(sp_sch['redmud_second'].df['time_days'], sp_sch['redmud_second'].df ['cum_evap_commercial']*constants.m2mm,'gv',markevery=2) 

ax[1].plot(sp_sch['redmud_first'].df ['time_days'], sp_sch['redmud_first'].df  ['evap_rate_te']*constants.ms2mmday,'r+',markevery=2) 
ax[1].plot(sp_sch['redmud_second'].df['time_days'], sp_sch['redmud_second'].df ['evap_rate_te']*constants.ms2mmday,'g+',markevery=2) 
ax[1].plot(sp_sch['redmud_first'].df ['time_days'], sp_sch['redmud_first'].df  ['evap_rate_commercial']*constants.ms2mmday,'rv',markevery=2) 
ax[1].plot(sp_sch['redmud_second'].df['time_days'], sp_sch['redmud_second'].df ['evap_rate_commercial']*constants.ms2mmday,'gv',markevery=2) 
plt.show(block=False)
