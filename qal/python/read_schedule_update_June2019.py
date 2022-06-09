import operator
import sensorfun
import json
py_compile.compile(os.environ['pyduino']+'/python/post_processing/sensorfun.py')
import sensorfun
reload(sensorfun)
py_compile.compile(os.environ['pyduino']+'/python/post_processing/figlib.py')
import datetime
import figlib
import wafo.interpolate as wf
reload(figlib)
lw=5
ms=8
mew=3
grid_width=2
y_fontsize=20


with open('schedule.json') as f:
    schedule = json.load(f) #, object_pairs_hook=OrderedDict)

schedule['average_dry_density']=float(schedule['average_dry_density'])
schedule['specific_gravity']=float(schedule['specific_gravity'])
schedule['porosity']=0.53#1-schedule['average_dry_density']/schedule['specific_gravity']

            
sp_sch={}
plot_interpolate=False
#plot_interpolate=True
for line in open("schedule.ipt"):
    li=line.strip()
    if not li.startswith("#"):
        line_content=[x.strip() for x in li.split(',')]
        sch_name=line_content[2]
        sp_sch[sch_name]=pandas_scale.concat_data_roof(pd.datetime.strptime(line_content[0],'%Y/%b/%d %H:%M'),
            pd.datetime.strptime(line_content[1],'%Y/%b/%d %H:%M'),dt_s );
        sp_sch[sch_name].df.index=sp_sch[sch_name].df['date_time']

        sp_sch[sch_name].start_dt=pd.datetime.strptime(line_content[0],'%Y/%b/%d %H:%M')
        sp_sch[sch_name].end_dt=pd.datetime.strptime(line_content[1],'%Y/%b/%d %H:%M')

        sp_sch[sch_name].surface_area  =float(line_content[4])

        
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['tmp0']   ,plot=plot_interpolate  ,coef=5e-10)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['tmp1']   ,plot=plot_interpolate  ,coef=5e-10)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['tmp2']   ,plot=plot_interpolate  ,coef=5e-10)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['tmp3']   ,plot=plot_interpolate  ,coef=5e-10)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['tmp4']   ,plot=plot_interpolate  ,coef=5e-10)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['tmp5']   ,plot=plot_interpolate  ,coef=5e-10)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['tmp6']   ,plot=plot_interpolate  ,coef=5e-10)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['tmp7']   ,plot=plot_interpolate  ,coef=5e-10)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['tmp8']   ,plot=plot_interpolate  ,coef=5e-10)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['tmp9']   ,plot=plot_interpolate  ,coef=5e-10)  # done

        time_start=np.datetime64('2018-09-23T09:40')

        #time_end=np.datetime64('2019-03-22T04:30')
        time_end=np.datetime64('2019-03-22T04:30')
        maskt=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
        sp_sch[sch_name].df['tmp4'].loc[time_start:]=sp_sch[sch_name].df['tmp5']*1.06
        sp_sch[sch_name].df['tmp4'][maskt].loc[sp_sch[sch_name].df['tmp4']<25]=sp_sch[sch_name].df['tmp4']*0.7
        sp_sch[sch_name].df['tmp3'].loc[time_start:]=sp_sch[sch_name].df['tmp5']*1.09
        sp_sch[sch_name].df['tmp2'].loc[time_start:]=sp_sch[sch_name].df['tmp5']*1.11
        sp_sch[sch_name].df['tmp1'].loc[time_start:]=sp_sch[sch_name].df['tmp9']*1.25
        sp_sch[sch_name].df['tmp0'].loc[time_start:]=sp_sch[sch_name].df['tmp9']*1.32
        
        time_start=np.datetime64('2019-01-25T08:40')
        sp_sch[sch_name].df['tmp7'].loc[time_start:]=sp_sch[sch_name].df['tmp6']*1.05


        sp_sch[sch_name].df['tmp6'].loc[sp_sch[sch_name].df['tmp6']>48]=sp_sch[sch_name].df['tmp6']*0.85

#---------------Suction sensor data------------------------------------------------------------------------------
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['su0']   ,plot=plot_interpolate  ,coef=5e-10)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['su1']   ,plot=plot_interpolate  ,coef=5e-10)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['su2']   ,plot=plot_interpolate  ,coef=5e-10)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['su3']   ,plot=plot_interpolate  ,coef=5e-10)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['su4']   ,plot=plot_interpolate  ,coef=5e-10)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['su5']   ,plot=plot_interpolate  ,coef=5e-10)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['su6']   ,plot=plot_interpolate  ,coef=5e-10)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['su7']   ,plot=plot_interpolate  ,coef=5e-10)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['su8']   ,plot=plot_interpolate  ,coef=5e-10)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['su9']   ,plot=plot_interpolate  ,coef=5e-10)  # done

	#aa=-1.1 #coef tested best
	##aa=-0.91 #coef tested best
	#bb=7 #coef tested best       

	#delta_t_su5_low_2_high=sorted(sp_sch[sch_name].df['su5'], key=float)
	#sp_sch[sch_name].df.delta_t_su5=sp_sch[sch_name].df['su5']
	#sp_sch[sch_name].max_delta_t_su5=np.average(delta_t_su5_low_2_high[-20:])
	#sp_sch[sch_name].min_delta_t_su5=np.average(delta_t_su5_low_2_high[-100:-20]) #np.average(delta_t_su5_low_2_high[0])
	#sp_sch[sch_name].df['norm_delta_t_su5'] =- (sp_sch[sch_name].min_delta_t_su5 -sp_sch[sch_name].df.delta_t_su5)/(sp_sch[sch_name].max_delta_t_su5-sp_sch[sch_name].min_delta_t_su5)
	#
	#delta_t_su6_low_2_high=sorted(sp_sch[sch_name].df['su6'], key=float)
	#sp_sch[sch_name].df.delta_t_su6 =sp_sch[sch_name].df['su6']
	#sp_sch[sch_name].max_delta_t_su6=np.average(delta_t_su6_low_2_high[-20:])
	#sp_sch[sch_name].min_delta_t_su6=np.average(delta_t_su6_low_2_high[0])
	#sp_sch[sch_name].df['norm_delta_t_su6'] =- (sp_sch[sch_name].min_delta_t_su6 -sp_sch[sch_name].df.delta_t_su6)/(sp_sch[sch_name].max_delta_t_su6-sp_sch[sch_name].min_delta_t_su6)
	#
	#delta_t_su8_low_2_high=sorted(sp_sch[sch_name].df['su8'], key=float)
	#sp_sch[sch_name].df.delta_t_su8 =sp_sch[sch_name].df['su8']
	#sp_sch[sch_name].max_delta_t_su8=np.average(delta_t_su8_low_2_high[-20:])
	#sp_sch[sch_name].min_delta_t_su8=np.average(delta_t_su8_low_2_high[:5])
	#sp_sch[sch_name].df['norm_delta_t_su8'] =- (sp_sch[sch_name].min_delta_t_su8 -sp_sch[sch_name].df.delta_t_su8)/(sp_sch[sch_name].max_delta_t_su8-sp_sch[sch_name].min_delta_t_su8)
	#
	#delta_t_su9_low_2_high=sorted(sp_sch[sch_name].df['su9'], key=float)
	#sp_sch[sch_name].df.delta_t_su9 =sp_sch[sch_name].df['su9']
	#sp_sch[sch_name].max_delta_t_su9=np.average(delta_t_su9_low_2_high[-20:])
	#sp_sch[sch_name].min_delta_t_su9=np.average(delta_t_su9_low_2_high[:5])
	#sp_sch[sch_name].df['norm_delta_t_su9'] =- (sp_sch[sch_name].min_delta_t_su9 -sp_sch[sch_name].df.delta_t_su9)/(sp_sch[sch_name].max_delta_t_su9-sp_sch[sch_name].min_delta_t_su9)
	#
	#
	#sp_sch[sch_name].df['suction5']=np.exp(-1.5*(sp_sch[sch_name].df['norm_delta_t_su5']**aa-bb))
	#sp_sch[sch_name].df['suction6']=np.exp(-1.5*(sp_sch[sch_name].df['norm_delta_t_su6']**aa-bb))
	#sp_sch[sch_name].df['suction8']=np.exp(-1.5*(sp_sch[sch_name].df['norm_delta_t_su8']**aa-bb))
	#sp_sch[sch_name].df['suction9']=np.exp(-1.5*(sp_sch[sch_name].df['norm_delta_t_su9']**aa-bb))

#-------------------------------------------------------------------------------------------------
        #time_start=np.datetime64('2018-01-29T09:40')
        #time_switch=np.datetime64('2018-04-09T18:03')
        time_start=np.datetime64('2018-12-20T16:40')
        time_switch=np.datetime64('2019-05-01T00:40')
        #time_end=np.datetime64('2019-03-22T11:40')
        time_end=np.datetime64('2019-06-18T12:40')#date time of data updated
        #mask=sp_sch[sch_name].df['date_time'].between(time_start,time_switch)
        #mask1=sp_sch[sch_name].df['date_time'].between(time_switch,time_end)
        mask=sp_sch[sch_name].df['date_time'].between(time_start,time_switch) #date time of data updated
        mask2=sp_sch[sch_name].df['date_time'].between(time_switch,time_end)
        #sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['mo0']   ,plot=plot_interpolate  ,coef=5e-12, start_time=time_switch,end_time=time_end)  # done coef=5e-7
        #sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['mo1']   ,plot=plot_interpolate  ,coef=5e-12, start_time=time_switch,end_time=time_end)  # done coef=5e-14
        #sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['mo2']   ,plot=plot_interpolate  ,coef=5e-12, start_time=time_switch,end_time=time_end)  # done coef=5e-14
        #sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['mo3']   ,plot=plot_interpolate  ,coef=5e-13, start_time=time_switch,end_time=time_end)  # done coef=5e-14
        #sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['mo4']   ,plot=plot_interpolate  ,coef=5e-12, start_time=time_switch,end_time=time_end)  # done coef=5e-14
        #sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['mo5']   ,plot=plot_interpolate  ,coef=5e-12, start_time=time_switch,end_time=time_end)  # done coef=5e-14
        #sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['mo6']   ,plot=plot_interpolate  ,coef=5e-12, start_time=time_switch,end_time=time_end)  # done coef=5e-14
        #sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['mo7']   ,plot=plot_interpolate  ,coef=5e-12, start_time=time_switch,end_time=time_end)  # done coef=5e-14 
        #sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['mo8']   ,plot=plot_interpolate  ,coef=5e-12, start_time=time_switch,end_time=time_end)  # done coef=5e-14
        #sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['mo9']   ,plot=plot_interpolate  ,coef=5e-12, start_time=time_switch,end_time=time_end)  # done coef=5e-14

        #if sch_name=="qal":
        #sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['mo0']   ,plot=plot_interpolate  ,coef=5e-7, start_time=time_start,end_time=time_switch)  # done
        sp_sch[sch_name].merge_data2(df=data_mo_su.df, keys=['mo0']   ,plot=plot_interpolate  ,coef=5e-12)  # done 5e-7
        #sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['mo1']   ,plot=plot_interpolate  ,coef=5e-10, start_time=time_start,end_time=time_switch)  # done
        sp_sch[sch_name].merge_data2(df=data_mo_su.df, keys=['mo1']   ,plot=plot_interpolate  ,coef=5e-14)  # done 5e-10

        sp_sch[sch_name].merge_data2(df=data_mo_su.df, keys=['mo2']   ,plot=plot_interpolate  ,coef=5e-14)  # done 5e-10
        sp_sch[sch_name].merge_data2(df=data_mo_su.df, keys=['mo3']   ,plot=plot_interpolate  ,coef=5e-14)  # done 5e-10
        sp_sch[sch_name].merge_data2(df=data_mo_su.df, keys=['mo4']   ,plot=plot_interpolate  ,coef=5e-14)  # done 5e-10
        sp_sch[sch_name].merge_data2(df=data_mo_su.df, keys=['mo5']   ,plot=plot_interpolate  ,coef=5e-14)  # done 5e-10
        sp_sch[sch_name].merge_data2(df=data_mo_su.df, keys=['mo6']   ,plot=plot_interpolate  ,coef=5e-14)  # done 5e-10
        sp_sch[sch_name].merge_data2(df=data_mo_su.df, keys=['mo7']   ,plot=plot_interpolate  ,coef=5e-12)  # done 5e-10
        sp_sch[sch_name].merge_data2(df=data_mo_su.df, keys=['mo8']   ,plot=plot_interpolate  ,coef=5e-14)  # done 5e-10
        sp_sch[sch_name].merge_data2(df=data_mo_su.df, keys=['mo9']   ,plot=plot_interpolate  ,coef=5e-14)  # done 5e-10

#------------Special treatment for readings from moisture sensors----------------------------
        sp_sch[sch_name].df['mo0'][mask]=sp_sch[sch_name].df['mo0']*0.85
        sp_sch[sch_name].df['mo1'][mask]=sp_sch[sch_name].df['mo1']*0.85
        sp_sch[sch_name].df['mo2'][mask]=sp_sch[sch_name].df['mo2']*0.85
        sp_sch[sch_name].df['mo3'][mask]=sp_sch[sch_name].df['mo3']*0.85
        sp_sch[sch_name].df['mo4'][mask]=sp_sch[sch_name].df['mo4']*0.85
        sp_sch[sch_name].df['mo5'][mask]=sp_sch[sch_name].df['mo5']*0.85
        sp_sch[sch_name].df['mo6'][mask]=sp_sch[sch_name].df['mo6']*0.85
        sp_sch[sch_name].df['mo7'][mask]=sp_sch[sch_name].df['mo7']*0.85
        sp_sch[sch_name].df['mo8'][mask]=sp_sch[sch_name].df['mo8']*0.85
        sp_sch[sch_name].df['mo9'][mask]=sp_sch[sch_name].df['mo9']*0.85

 
        sp_sch[sch_name].df['mo0'][mask2]=sp_sch[sch_name].df['mo0']*0.86
        sp_sch[sch_name].df['mo1'][mask2]=sp_sch[sch_name].df['mo1']*0.86
        sp_sch[sch_name].df['mo2'][mask2]=sp_sch[sch_name].df['mo2']*0.86
        sp_sch[sch_name].df['mo3'][mask2]=sp_sch[sch_name].df['mo3']*0.86
        sp_sch[sch_name].df['mo4'][mask2]=sp_sch[sch_name].df['mo4']*0.86
        sp_sch[sch_name].df['mo5'][mask2]=sp_sch[sch_name].df['mo5']*0.86
        sp_sch[sch_name].df['mo6'][mask2]=sp_sch[sch_name].df['mo6']*0.86
        sp_sch[sch_name].df['mo7'][mask2]=sp_sch[sch_name].df['mo7']*0.86
        sp_sch[sch_name].df['mo8'][mask2]=sp_sch[sch_name].df['mo8']*0.85
        sp_sch[sch_name].df['mo9'][mask2]=sp_sch[sch_name].df['mo9']*0.85
#--------------------------------------------------------------------------------------------- 
       
        #sp_sch[sch_name].df['mo1'].loc[sp_sch[sch_name].df['mo1']<260]=260
        #sp_sch[sch_name].df['mo2'].loc[sp_sch[sch_name].df['mo2']<260]=260
        #sp_sch[sch_name].df['mo3'].loc[sp_sch[sch_name].df['mo3']>550]=550
        #sp_sch[sch_name].df['mo3'].loc[sp_sch[sch_name].df['mo3']<260]=260      
        #sp_sch[sch_name].df['mo3'].loc[sp_sch[sch_name].df['mo3']<280]=260
        #sp_sch[sch_name].df['mmo0']=(550.0-sp_sch[sch_name].df['mo0'])/(550.-270)
        #sp_sch[sch_name].df['mmo1']=(550.0-sp_sch[sch_name].df['mo1'])/(550.-270)
        #sp_sch[sch_name].df['mmo2']=(550.0-sp_sch[sch_name].df['mo2'])/(550.-270)
        #sp_sch[sch_name].df['mmo3']=(550.0-sp_sch[sch_name].df['mo3'])/(550.-270)
        #sp_sch[sch_name].df['mmo4']=(550.0-sp_sch[sch_name].df['mo4'])/(550.-270)
        #sp_sch[sch_name].df['mmo5']=(550.0-sp_sch[sch_name].df['mo5'])/(550.-270)
        #sp_sch[sch_name].df['mmo6']=(550.0-sp_sch[sch_name].df['mo6'])/(550.-270)
        #sp_sch[sch_name].df['mmo7']=(550.0-sp_sch[sch_name].df['mo7'])/(550.-270)
        #sp_sch[sch_name].df['mmo8']=(550.0-sp_sch[sch_name].df['mo8'])/(550.-270)
        #sp_sch[sch_name].df['mmo9']=(550.0-sp_sch[sch_name].df['mo9'])/(550.-270)
        #sp_sch[sch_name].merge_data(df=data_weather_daisy.df, keys=['ir_up']   ,plot=plot_interpolate  ,coef=5e-4, start_time=time_start,end_time=time_switch)
        #sp_sch[sch_name].merge_data(df=data_weather_daisy.df, keys=['ir_down']   ,plot=plot_interpolate  ,coef=5e-4, start_time=time_start,end_time=time_switch)
        #sp_sch[sch_name].merge_data(df=data_weather_daisy.df, keys=['rainmm']   ,plot=plot_interpolate  ,coef=5e-08, start_time=time_start,end_time=time_switch)  # done
        #elif sch_name=="qal1807":
        #coef=-7.0
        #sp_sch[sch_name].df['mmo0_p1']=(580.0**coef-sp_sch[sch_name].df['mo0'][mask]**coef)/(580.**coef-252**coef)*schedule['porosity']
        #sp_sch[sch_name].df['mmo1_p1']=(570.0**coef-sp_sch[sch_name].df['mo1'][mask]**coef)/(550.**coef-270**coef)*schedule['porosity']
        #sp_sch[sch_name].df['mmo1_p1']=(520.0**coef-sp_sch[sch_name].df['mo1'][mask]**coef)/(520.**coef-270**coef)*schedule['porosity']
        #sp_sch[sch_name].df['mmo2_p1']=(570.0**coef-sp_sch[sch_name].df['mo2'][mask]**coef)/(550.**coef-270**coef)*schedule['porosity']
        #sp_sch[sch_name].df['mmo2_p1']=(545.0**coef-sp_sch[sch_name].df['mo2'][mask]**coef)/(545.**coef-255**coef)*schedule['porosity']
        #sp_sch[sch_name].df['mmo3_p1']=(570.0**coef-sp_sch[sch_name].df['mo3'][mask]**coef)/(550.**coef-280**coef)*schedule['porosity']
        #sp_sch[sch_name].df['mmo3_p1']=(550.0**coef-sp_sch[sch_name].df['mo3'][mask]**coef)/(550.**coef-260**coef)*schedule['porosity']
        #sp_sch[sch_name].df['mmo4_p1']=(570.0**coef-sp_sch[sch_name].df['mo4'][mask]**coef)/(550.**coef-270**coef)*schedule['porosity']
        #sp_sch[sch_name].df['mmo4_p1']=(550.0**coef-sp_sch[sch_name].df['mo4'][mask]**coef)/(550.**coef-260**coef)*schedule['porosity']
        #sp_sch[sch_name].df['mmo5_p1']=(570.0**coef-sp_sch[sch_name].df['mo5'][mask]**coef)/(550.**coef-270**coef)*schedule['porosity']
        #sp_sch[sch_name].df['mmo5_p1']=(560.0**coef-sp_sch[sch_name].df['mo5'][mask]**coef)/(560.**coef-270**coef)*schedule['porosity']
        #sp_sch[sch_name].df['mmo6_p1']=(570.0**coef-sp_sch[sch_name].df['mo6'][mask]**coef)/(550.**coef-280**coef)*schedule['porosity']
        #sp_sch[sch_name].df['mmo6_p1']=(550.0**coef-sp_sch[sch_name].df['mo6'][mask]**coef)/(550.**coef-275**coef)*schedule['porosity']
        #sp_sch[sch_name].df['mmo7_p1']=(570.0**coef-sp_sch[sch_name].df['mo7'][mask]**coef)/(550.**coef-275**coef)*schedule['porosity']
        #sp_sch[sch_name].df['mmo7_p1']=(520.0**coef-sp_sch[sch_name].df['mo7'][mask]**coef)/(520.**coef-273**coef)*schedule['porosity']
        #sp_sch[sch_name].df['mmo8_p1']=(570.0**coef-sp_sch[sch_name].df['mo8'][mask]**coef)/(550.**coef-285**coef)*schedule['porosity']
        #sp_sch[sch_name].df['mmo8_p1']=(350.0**coef-sp_sch[sch_name].df['mo8'][mask]**coef)/(350.**coef-291**coef)*schedule['porosity']
        #sp_sch[sch_name].df['mmo9_p1']=(570.0**coef-sp_sch[sch_name].df['mo9'][mask]**coef)/(550.**coef-285**coef)*schedule['porosity']
        #sp_sch[sch_name].df['mmo9_p1']=(355.0**coef-sp_sch[sch_name].df['mo9'][mask]**coef)/(355.**coef-277**coef)*schedule['porosity']


        #alpha=-7.0
        alpha=-7.0
        #sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['mo0']   ,plot=plot_interpolate  ,coef=5e-10, start_time=time_switch,end_time=time_end)  # done coef=5e-7
        #sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['mo2']   ,plot=plot_interpolate  ,coef=5e-12, start_time=time_switch,end_time=time_end)  # done coef=5e-14
        #sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['mo3']   ,plot=plot_interpolate  ,coef=5e-12, start_time=time_switch,end_time=time_end)  # done coef=5e-14
        #sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['mo4']   ,plot=plot_interpolate  ,coef=5e-12, start_time=time_switch,end_time=time_end)  # done coef=5e-14
        #sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['mo5']   ,plot=plot_interpolate  ,coef=5e-12, start_time=time_switch,end_time=time_end)  # done coef=5e-14
        #sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['mo6']   ,plot=plot_interpolate  ,coef=5e-12, start_time=time_switch,end_time=time_end)  # done coef=5e-14
        #sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['mo7']   ,plot=plot_interpolate  ,coef=5e-12, start_time=time_switch,end_time=time_end)  # done coef=5e-14 
        #sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['mo8']   ,plot=plot_interpolate  ,coef=5e-12, start_time=time_switch,end_time=time_end)  # done coef=5e-14
        #sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['mo9']   ,plot=plot_interpolate  ,coef=5e-12, start_time=time_switch,end_time=time_end)  # done coef=5e-14


        #------------------------------Degree of saturation in cover soil----------------------------------------
        sp_sch[sch_name].df['sat0']=(310.0**alpha-sp_sch[sch_name].df['mo0']**alpha)/(310.**alpha-265**alpha) # 1 cm
        #sp_sch[sch_name].df['sat0']=(310.0**alpha-sp_sch[sch_name].df['mo0']**alpha)/(310.**alpha-270**alpha)  # 1 cm
        #sp_sch[sch_name].df['mmo0']=(310.0**alpha-sp_sch[sch_name].df['mo0']**alpha)/(310.**alpha-270**alpha)*porosity_cover #schedule['porosity']   # 1 cm
        sp_sch[sch_name].df['sat1']=(380.0**alpha-sp_sch[sch_name].df['mo1']**alpha)/(380.**alpha-270**alpha) # 5 cm
        #sp_sch[sch_name].df['sat1']=(350.0**alpha-sp_sch[sch_name].df['mo1']**alpha)/(350.**alpha-284**alpha) # 5 cm
        #sp_sch[sch_name].df['sat1']=(550.0**alpha-sp_sch[sch_name].df['mo1']**alpha)/(550.**alpha-270**alpha) # 5 cm
        #sp_sch[sch_name].df['mmo1']=(350.0**alpha-sp_sch[sch_name].df['mo1']**alpha)/(350.**alpha-284**alpha)*porosity_cover #schedule['porosity']   # 5 cm
        sp_sch[sch_name].df['sat2']=(550.0**alpha-sp_sch[sch_name].df['mo2']**alpha)/(550.**alpha-265**alpha) # 8 cm 
        #sp_sch[sch_name].df['sat2']=(340.0**alpha-sp_sch[sch_name].df['mo2']**alpha)/(340.**alpha-273**alpha) # 8 cm 
        #sp_sch[sch_name].df['sat2']=(550.0**alpha-sp_sch[sch_name].df['mo2']**alpha)/(550.**alpha-265**alpha) # 8 cm 
        #sp_sch[sch_name].df['mmo2']=(340.0**alpha-sp_sch[sch_name].df['mo2']**alpha)/(340.**alpha-273**alpha)*porosity_cover #schedule['porosity']   # 8 cm 
        sp_sch[sch_name].df['sat3']=(550.0**alpha-sp_sch[sch_name].df['mo3']**alpha)/(550.0**alpha-270**alpha) # 13cm
        #sp_sch[sch_name].df['sat3']=(340.0**alpha-sp_sch[sch_name].df['mo3']**alpha)/(340.0**alpha-272**alpha) # 13cm
        #sp_sch[sch_name].df['sat3']=(550.0**alpha-sp_sch[sch_name].df['mo3']**alpha)/(550.0**alpha-265**alpha) # 13cm
        #sp_sch[sch_name].df['mmo3']=(340.0**alpha-sp_sch[sch_name].df['mo3']**alpha)/(340.0**alpha-272**alpha)*porosity_cover #schedule['porosity']   # 13cm
        sp_sch[sch_name].df['sat4']=(550.0**alpha-sp_sch[sch_name].df['mo4']**alpha)/(550.**alpha-265**alpha)  # 20cm
        #sp_sch[sch_name].df['sat4']=(350.0**alpha-sp_sch[sch_name].df['mo4']**alpha)/(350.**alpha-273**alpha)  # 20cm
        #sp_sch[sch_name].df['sat4']=(550.0**alpha-sp_sch[sch_name].df['mo4']**alpha)/(550.**alpha-260**alpha)  # 20cm
        #sp_sch[sch_name].df['mmo4']=(350.0**alpha-sp_sch[sch_name].df['mo4']**alpha)/(350.**alpha-273**alpha)*porosity_cover #schedule['porosity']   # 20cm
        sp_sch[sch_name].df['sat5']=(550.0**alpha-sp_sch[sch_name].df['mo5']**alpha)/(550.**alpha-278**alpha)  # 28cm
        #sp_sch[sch_name].df['sat5']=(340.0**alpha-sp_sch[sch_name].df['mo5']**alpha)/(340.**alpha-280**alpha)  # 28cm
        #sp_sch[sch_name].df['sat5']=(550.0**alpha-sp_sch[sch_name].df['mo5']**alpha)/(550.**alpha-275**alpha)  # 28cm
        #sp_sch[sch_name].df['mmo5']=(340.0**alpha-sp_sch[sch_name].df['mo5']**alpha)/(340.**alpha-280**alpha)*porosity_cover #schedule['porosity']   # 28cm
        sp_sch[sch_name].df['sat6']=(550.0**alpha-sp_sch[sch_name].df['mo6']**alpha)/(550.**alpha-275**alpha)  # 38cm
        #sp_sch[sch_name].df['sat6']=(340.0**alpha-sp_sch[sch_name].df['mo6']**alpha)/(340.**alpha-276**alpha)  # 38cm
        #sp_sch[sch_name].df['mmo6']=(340.0**alpha-sp_sch[sch_name].df['mo6']**alpha)/(340.**alpha-276**alpha)*porosity_cover #schedule['porosity']   # 38cm
        sp_sch[sch_name].df['sat7']=(400.0**alpha-sp_sch[sch_name].df['mo7']**alpha)/(400.**alpha-275**alpha)  # 48cm
        #sp_sch[sch_name].df['sat7']=(380.0**alpha-sp_sch[sch_name].df['mo7']**alpha)/(380.**alpha-297**alpha)  # 48cm
        #sp_sch[sch_name].df['sat7']=(550.0**alpha-sp_sch[sch_name].df['mo7']**alpha)/(550.**alpha-275**alpha)  # 48cm
        #sp_sch[sch_name].df['mmo7']=(380.0**alpha-sp_sch[sch_name].df['mo7']**alpha)/(380.**alpha-297**alpha)*porosity_cover #schedule['porosity']   # 48cm
        #--------------------------------Degrees of saturation in red mud-----------------------------------
        sp_sch[sch_name].df['sat8']=(550.0**alpha-sp_sch[sch_name].df['mo8']**alpha)/(550.**alpha-286**alpha)  # 70cm
        #sp_sch[sch_name].df['mmo8']=(400.0**alpha-sp_sch[sch_name].df['mo8']**alpha)/(400.**alpha-288**alpha)   # 70cm
        sp_sch[sch_name].df['sat9']=(550.0**alpha-sp_sch[sch_name].df['mo9']**alpha)/(550.**alpha-276**alpha)  # 85cm 
        #sp_sch[sch_name].df['mmo9']=(400.0**alpha-sp_sch[sch_name].df['mo9']**alpha)/(400.**alpha-280**alpha)   # 85cm

        sp_sch[sch_name].df['sat0'].loc[sp_sch[sch_name].df['sat0']<0] = 0.0

        sp_sch[sch_name].df['sat0'].loc[sp_sch[sch_name].df['sat0']>1.01] = 1.0
        sp_sch[sch_name].df['sat1'].loc[sp_sch[sch_name].df['sat1']>1.01] = 1.0
        sp_sch[sch_name].df['sat2'].loc[sp_sch[sch_name].df['sat2']>1.01] = 1.0
        sp_sch[sch_name].df['sat3'].loc[sp_sch[sch_name].df['sat3']>1.01] = 1.0
        sp_sch[sch_name].df['sat4'].loc[sp_sch[sch_name].df['sat4']>1.01] = 1.0
        sp_sch[sch_name].df['sat5'].loc[sp_sch[sch_name].df['sat5']>1.01] = 1.0
        sp_sch[sch_name].df['sat6'].loc[sp_sch[sch_name].df['sat6']>1.01] = 1.0
        sp_sch[sch_name].df['sat7'].loc[sp_sch[sch_name].df['sat7']>1.01] = 1.0
        sp_sch[sch_name].df['sat8'].loc[sp_sch[sch_name].df['sat8']>1.01] = 1.0
        sp_sch[sch_name].df['sat9'].loc[sp_sch[sch_name].df['sat9']>1.01] = 1.0

#-----------------Change the unit of degree of saturation to 100%-----------------------
        sp_sch[sch_name].df['dosat0'] = sp_sch[sch_name].df['sat0']*100
        sp_sch[sch_name].df['dosat1'] = sp_sch[sch_name].df['sat1']*100
        sp_sch[sch_name].df['dosat2'] = sp_sch[sch_name].df['sat2']*100
        sp_sch[sch_name].df['dosat3'] = sp_sch[sch_name].df['sat3']*100
        sp_sch[sch_name].df['dosat4'] = sp_sch[sch_name].df['sat4']*100
        sp_sch[sch_name].df['dosat5'] = sp_sch[sch_name].df['sat5']*100
        sp_sch[sch_name].df['dosat6'] = sp_sch[sch_name].df['sat6']*100
        sp_sch[sch_name].df['dosat7'] = sp_sch[sch_name].df['sat7']*100
        sp_sch[sch_name].df['dosat8'] = sp_sch[sch_name].df['sat8']*100
        sp_sch[sch_name].df['dosat9'] = sp_sch[sch_name].df['sat9']*100

       
        porosity_cover = 0.45 # This is the porosity of the cover soil got from the SWCC result
        #-------------------------------Moisture sensors in cover soil----------------------------------
        sp_sch[sch_name].df['mmo0']=sp_sch[sch_name].df['sat0']*porosity_cover #schedule['porosity']   # 1 cm
        #sp_sch[sch_name].df['mmo0']=(310.0**alpha-sp_sch[sch_name].df['mo0']**alpha)/(310.**alpha-270**alpha)*porosity_cover #schedule['porosity']   # 1 cm
        sp_sch[sch_name].df['mmo1']=sp_sch[sch_name].df['sat1']*porosity_cover #schedule['porosity']   # 5 cm
        #sp_sch[sch_name].df['mmo1']=(345.0**alpha-sp_sch[sch_name].df['mo1']**alpha)/(345.**alpha-284**alpha)*porosity_cover #schedule['porosity']   # 5 cm
        sp_sch[sch_name].df['mmo2']=sp_sch[sch_name].df['sat2']*porosity_cover #schedule['porosity']   # 8 cm 
        #sp_sch[sch_name].df['mmo2']=(310.0**alpha-sp_sch[sch_name].df['mo2']**alpha)/(310.**alpha-273**alpha)*porosity_cover #schedule['porosity']   # 8 cm 
        sp_sch[sch_name].df['mmo3']=sp_sch[sch_name].df['sat3']*porosity_cover #schedule['porosity']   # 13cm
        #sp_sch[sch_name].df['mmo3']=(300.0**alpha-sp_sch[sch_name].df['mo3']**alpha)/(300.0**alpha-272**alpha)*porosity_cover #schedule['porosity']   # 13cm
        sp_sch[sch_name].df['mmo4']=sp_sch[sch_name].df['sat4']*porosity_cover #schedule['porosity']   # 20cm
        #sp_sch[sch_name].df['mmo4']=(320.0**alpha-sp_sch[sch_name].df['mo4']**alpha)/(320.**alpha-273**alpha)*porosity_cover #schedule['porosity']   # 20cm
        sp_sch[sch_name].df['mmo5']=sp_sch[sch_name].df['sat5']*porosity_cover #schedule['porosity']   # 28cm
        #sp_sch[sch_name].df['mmo5']=(310.0**alpha-sp_sch[sch_name].df['mo5']**alpha)/(310.**alpha-280**alpha)*porosity_cover #schedule['porosity']   # 28cm
        sp_sch[sch_name].df['mmo6']=sp_sch[sch_name].df['sat6']*porosity_cover #schedule['porosity']   # 38cm
        #sp_sch[sch_name].df['mmo6']=(320.0**alpha-sp_sch[sch_name].df['mo6']**alpha)/(320.**alpha-276**alpha)*porosity_cover #schedule['porosity']   # 38cm
        sp_sch[sch_name].df['mmo7']=sp_sch[sch_name].df['sat7']*porosity_cover #schedule['porosity']   # 48cm
        #sp_sch[sch_name].df['mmo7']=(540.0**alpha-sp_sch[sch_name].df['mo7']**alpha)/(540.**alpha-297**alpha)*porosity_cover #schedule['porosity']   # 48cm
        #--------------------------------Moisture sensors in red mud-----------------------------------
        sp_sch[sch_name].df['mmo8']=sp_sch[sch_name].df['sat8']*schedule['porosity']   # 70cm
        #sp_sch[sch_name].df['mmo8']=(550.0**alpha-sp_sch[sch_name].df['mo8']**alpha)/(550.**alpha-285**alpha)   # 70cm
        sp_sch[sch_name].df['mmo9']=sp_sch[sch_name].df['sat9']*schedule['porosity']   # 85cm 
        #sp_sch[sch_name].df['mmo9']=(550.0**alpha-sp_sch[sch_name].df['mo9']**alpha)/(550.**alpha-275**alpha)   # 85cm

        sp_sch[sch_name].merge_data(df=data_weather_daisy.df, keys=['ir_up']   ,plot=plot_interpolate  ,coef=5e-4)
        sp_sch[sch_name].merge_data(df=data_weather_daisy.df, keys=['ir_down']   ,plot=plot_interpolate  ,coef=5e-4)
        sp_sch[sch_name].merge_data(df=data_weather_camellia.df, keys=['dlyrainmm']   ,plot=plot_interpolate  ,coef=5e-08)  # done

        #sp_sch[sch_name].df['mmo0'].loc[ sp_sch[sch_name].df['mmo0'] > porosity_cover] = porosity_cover 
        #sp_sch[sch_name].df['mmo1'].loc[ sp_sch[sch_name].df['mmo1'] > porosity_cover] = porosity_cover 
        #sp_sch[sch_name].df['mmo2'].loc[ sp_sch[sch_name].df['mmo2'] > porosity_cover] = porosity_cover 
        #sp_sch[sch_name].df['mmo3'].loc[ sp_sch[sch_name].df['mmo3'] > porosity_cover] = porosity_cover 
        #sp_sch[sch_name].df['mmo4'].loc[ sp_sch[sch_name].df['mmo4'] > porosity_cover] = porosity_cover
        #sp_sch[sch_name].df['mmo5'].loc[ sp_sch[sch_name].df['mmo5'] > porosity_cover] = porosity_cover
        #sp_sch[sch_name].df['mmo6'].loc[ sp_sch[sch_name].df['mmo6'] > porosity_cover] = porosity_cover
        #sp_sch[sch_name].df['mmo7'].loc[ sp_sch[sch_name].df['mmo7'] > porosity_cover] = porosity_cover
        #sp_sch[sch_name].df['mmo8'].loc[ sp_sch[sch_name].df['mmo8'] > schedule['porosity']] = schedule['porosity']
        #sp_sch[sch_name].df['mmo9'].loc[ sp_sch[sch_name].df['mmo9'] > schedule['porosity']] = schedule['porosity']

        
        sp_sch[sch_name].df['mmo2'].loc[ sp_sch[sch_name].df['mmo2']<0  ]=np.nan
        sp_sch[sch_name].df['mmo3'].loc[ sp_sch[sch_name].df['mmo3']<0  ]=np.nan
        sp_sch[sch_name].df['mmo4'].loc[ sp_sch[sch_name].df['mmo4']<0  ]=np.nan
        sp_sch[sch_name].df['mmo5'].loc[ sp_sch[sch_name].df['mmo5']<0  ]=np.nan

        #time_start=np.datetime64('2018-03-29T03:40')
        #sp_sch[sch_name].df['mmo0'].loc[:time_start]=sp_sch[sch_name].df['mmo0']*2.
        #sp_sch[sch_name].df['mmo1'].loc[:time_start]=sp_sch[sch_name].df['mmo1']*2.5

        time_start=np.datetime64('2018-06-01T00:00')
        time_end=np.datetime64('2018-08-01T00:00')
        mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
        sp_sch[sch_name].df['mmo0'][mask]=sp_sch[sch_name].df['mmo0']*0.7
        sp_sch[sch_name].df['mmo0'].loc[sp_sch[sch_name].df['mmo0']<0]=0
        
        
        #----calculating suction by using voumetric water content (SWCC)-------
        sp_sch[sch_name].df['su0_vwc']=constants.swcc_reverse_fredlund_xing_1994(nf=1.5,mf=0.15,af=3.8,vwc=sp_sch[sch_name].df['mmo0'])/1000 #convert Pa to kPa
        sp_sch[sch_name].df['su1_vwc']=constants.swcc_reverse_fredlund_xing_1994(nf=1.5,mf=0.15,af=3.8,vwc=sp_sch[sch_name].df['mmo1'])/1000
        sp_sch[sch_name].df['su2_vwc']=constants.swcc_reverse_fredlund_xing_1994(nf=1.5,mf=0.15,af=3.8,vwc=sp_sch[sch_name].df['mmo2'])/1000
        sp_sch[sch_name].df['su3_vwc']=constants.swcc_reverse_fredlund_xing_1994(nf=1.5,mf=0.15,af=3.8,vwc=sp_sch[sch_name].df['mmo3'])/1000
        sp_sch[sch_name].df['su4_vwc']=constants.swcc_reverse_fredlund_xing_1994(nf=1.5,mf=0.15,af=3.8,vwc=sp_sch[sch_name].df['mmo4'])/1000
        sp_sch[sch_name].df['su5_vwc']=constants.swcc_reverse_fredlund_xing_1994(nf=1.5,mf=0.15,af=3.8,vwc=sp_sch[sch_name].df['mmo5'])/1000
        sp_sch[sch_name].df['su6_vwc']=constants.swcc_reverse_fredlund_xing_1994(nf=1.5,mf=0.15,af=3.8,vwc=sp_sch[sch_name].df['mmo6'])/1000
        sp_sch[sch_name].df['su7_vwc']=constants.swcc_reverse_fredlund_xing_1994(nf=1.5,mf=0.15,af=3.8,vwc=sp_sch[sch_name].df['mmo7'])/1000
        sp_sch[sch_name].df['su8_vwc']=constants.swcc_reverse_fredlund_xing_1994(nf=1.5,mf=0.15,af=20,vwc=sp_sch[sch_name].df['mmo8'])/1000
        sp_sch[sch_name].df['su9_vwc']=constants.swcc_reverse_fredlund_xing_1994(nf=1.5,mf=0.15,af=20,vwc=sp_sch[sch_name].df['mmo9'])/1000



        
        #time_start=np.datetime64('2018-12-20T06:40')
        #time_end=np.datetime64('2019-03-22T04:30')
        #mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
        #sp_sch[sch_name].df['mmo0'][mask]=sp_sch[sch_name].df['mmo0']*3
        #sp_sch[sch_name].df['mmo1'][mask]=sp_sch[sch_name].df['mmo1']*2.9
        #sp_sch[sch_name].df['mmo2'][mask]=sp_sch[sch_name].df['mmo2']*3
        #sp_sch[sch_name].df['mmo3'][mask]=sp_sch[sch_name].df['mmo3']*3
        #sp_sch[sch_name].df['mmo4'][mask]=sp_sch[sch_name].df['mmo4']*3
        #sp_sch[sch_name].df['mmo5'][mask]=sp_sch[sch_name].df['mmo5']*3
        #sp_sch[sch_name].df['mmo6'][mask]=sp_sch[sch_name].df['mmo6']*2.8
        #sp_sch[sch_name].df['mmo7'][mask]=sp_sch[sch_name].df['mmo7']*2.8
        #sp_sch[sch_name].df['mmo8'][mask]=sp_sch[sch_name].df['mmo8']*2.7
        #sp_sch[sch_name].df['mmo9'][mask]=sp_sch[sch_name].df['mmo9']*2.7
        # below is to finding ways to exrapolate at small fractions

        #time_start=np.datetime64('2018-03-02T13:00')
        #time_end=np.datetime64('2018-03-03T17:00')
        #mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
        
        #time_start=np.datetime64('2018-03-02T13:00')
        #time_end=np.datetime64('2018-03-03T17:00')
        #mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
        #sp_sch[sch_name].df.loc[mask,'tmp0']=np.nan
        #sp_sch[sch_name].df.loc[mask,'tmp1']=np.nan
        #sp_sch[sch_name].df.loc[mask,'tmp2']=np.nan
        #sp_sch[sch_name].df.loc[mask,'tmp3']=np.nan
        #sp_sch[sch_name].df.loc[mask,'tmp4']=np.nan
        #sp_sch[sch_name].df.loc[mask,'tmp5']=np.nan
        #sp_sch[sch_name].df.loc[mask,'tmp6']=np.nan
        #sp_sch[sch_name].df.loc[mask,'tmp7']=np.nan
        #sp_sch[sch_name].df.loc[mask,'tmp8']=np.nan
        #sp_sch[sch_name].df.loc[mask,'tmp9']=np.nan

        time_start=np.datetime64('2018-07-10T13:00')
        time_end=np.datetime64('2018-07-12T12:00')
        mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
        sp_sch[sch_name].df.loc[mask,'tmp0']=np.nan
        sp_sch[sch_name].df.loc[mask,'tmp1']=np.nan
        sp_sch[sch_name].df.loc[mask,'tmp2']=np.nan
        sp_sch[sch_name].df.loc[mask,'tmp3']=np.nan
        sp_sch[sch_name].df.loc[mask,'tmp4']=np.nan
        sp_sch[sch_name].df.loc[mask,'tmp5']=np.nan
        sp_sch[sch_name].df.loc[mask,'tmp6']=np.nan
        sp_sch[sch_name].df.loc[mask,'tmp7']=np.nan
        sp_sch[sch_name].df.loc[mask,'tmp8']=np.nan
        sp_sch[sch_name].df.loc[mask,'tmp9']=np.nan

        time_start_weatherUQ=np.datetime64('2020-02-05T10:40') #The time when started using meteorological data from UQ weather station
        sp_sch[sch_name].merge_data(df=data_weather_camellia.df, keys=['dlyrainmm']   ,plot=plot_interpolate  ,coef=5e-08)  # done
        sp_sch[sch_name].merge_data2(df=data_weather_camellia.df, keys=['dlyrainmm']   ,plot=plot_interpolate  ,coef=5e-08, start_time=sp_sch[sch_name].start_dt,end_time=sp_sch[sch_name].end_dt )
        sp_sch[sch_name].merge_data2(df=data_weather_camellia.df, keys=['dlyrainmm']   ,plot=plot_interpolate  ,coef=5e-08, start_time=sp_sch[sch_name].start_dt,end_time=sp_sch[sch_name].end_dt )

        sp_sch[sch_name].merge_data(df=data_weather_fromUQ.df, keys=['Rain_Acc(mm)']   ,plot=plot_interpolate  ,coef=5e-08)
        #time_start_weatherUQ=np.datetime64('2020-02-05T10:40') 
        sp_sch[sch_name].df['dlyrainmm'].loc[time_start_weatherUQ:]=0
        sp_sch[sch_name].df['Rain_Acc(mm)'].loc[:time_start_weatherUQ]=0
        sp_sch[sch_name].df['rainmm']= sp_sch[sch_name].df['dlyrainmm'] + sp_sch[sch_name].df['Rain_Acc(mm)']
        time_start=np.datetime64('2018-04-20T10:00')
        time_end=np.datetime64('2018-04-20T23:59')
        mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
        sp_sch[sch_name].df.loc[mask,'rainmm']=np.linspace(0.93,18,np.sum(mask) )
        sp_sch[sch_name].df['rainmm'].loc[sp_sch[sch_name].df['rainmm']<0]=0

        #-------------------------Solar radiation--------------------------------------------
        sp_sch[sch_name].merge_data(df=data_weather_daisy.df, keys=['ir_up']   ,plot=plot_interpolate  ,coef=5e-4,new_keys=['ir_up_daisy'])
        sp_sch[sch_name].merge_data(df=data_weather_daisy.df, keys=['ir_down']   ,plot=plot_interpolate  ,coef=5e-4,new_keys=['ir_down_daisy'])
        sp_sch[sch_name].merge_data(df=data_weather_camellia.df, keys=['ir_down']   ,plot=plot_interpolate  ,coef=5e-4,new_keys=['ir_up_camellia'])
        sp_sch[sch_name].merge_data(df=data_weather_fromUQ.df, keys=['Solar_Mean(W/m2)']   ,plot=plot_interpolate  ,coef=5e-4)
        #sp_sch[sch_name].df['ir_up_daisy'].loc[sp_sch[sch_name].df['ir_up_daisy']>19512]=np.nan
        #sp_sch[sch_name].df['ir_up_daisy'].loc[sp_sch[sch_name].df['ir_up_daisy']<252]=252   # if it is given as np.nan, there will be breaking points
        #sp_sch[sch_name].df['ir_up_camellia'].loc[sp_sch[sch_name].df['ir_up_camellia']<252]=252
        #sp_sch[sch_name].df['ir_up_camellia'].loc[sp_sch[sch_name].df['ir_up_camellia']>19512]=np.nan
        # the correction here is to ensure camellia shows same value as daisy
        sp_sch[sch_name].df['ir_up_camellia_cor'] = (sp_sch[sch_name].df['ir_up_camellia']-252) *1.17+252
        # the script below uses early results from daisy while later results from camellia. 
        time_start=np.datetime64('2018-06-29T13:00')
        time_end=np.datetime64('2018-10-21T17:00')
        mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
        #--------modify the plot of daily evaporation----------------------------
        time_end_ir_up_daisy=np.datetime64('2018-06-29T13:00')
        sp_sch[sch_name].df['ir_up_daisy'].loc[time_end_ir_up_daisy:]=0
        sp_sch[sch_name].df['ir_up_camellia'].loc[:time_end_ir_up_daisy]=0
        time_start_ir_up_newpower=np.datetime64('2019-09-19T23:40')
        sp_sch[sch_name].df['ir_up_camellia'].loc[time_start_ir_up_newpower:]=0
        sp_sch[sch_name].df['Solar_Mean(W/m2)'].loc[:time_start_ir_up_newpower]=0
        #-------------------------------------------------------------------------
        #sp_sch[sch_name].df['ir_up_concat']=sp_sch[sch_name].df['ir_up_daisy']
        sp_sch[sch_name].df['ir_up_concat']=sp_sch[sch_name].df['ir_up_daisy'] + sp_sch[sch_name].df['ir_up_camellia'] + (sp_sch[sch_name].df['Solar_Mean(W/m2)']*19.512+254) #Because the default unit of solar data from UQ weather station is W/m2
        sp_sch[sch_name].df['ir_up_concat'].loc[sp_sch[sch_name].df['ir_up_concat']>19512]=np.nan
        sp_sch[sch_name].df['ir_up_concat'].loc[sp_sch[sch_name].df['ir_up_concat']<252]=252
        sp_sch[sch_name].df.loc[mask,'ir_up_concat']= sp_sch[sch_name].df.loc[mask,'ir_up_camellia_cor']
        #----------------------------------------------------------------------------------------------

        #------------------temperature from weather station and soil surface-----------------
        sp_sch[sch_name].merge_data(df=data_weather_camellia.df, keys=['tc']  ,plot=plot_interpolate  ,coef=5e-08)  # done
        sp_sch[sch_name].merge_data(df=data_weather_fromUQ.df, keys=['Temp_Mean(deg)']  ,plot=plot_interpolate  ,coef=5e-08)

        #sp_sch[sch_name].df['tc'].loc[ sp_sch[sch_name].df['tc']<7  ]=np.nan
        sp_sch[sch_name].df['tc'].loc[time_start_weatherUQ:]=0 #had lost data of weather station on the roof since that time, so I used data from UQ weather station since then. Making values be zero is to merge data from two sources by using addition 
        sp_sch[sch_name].df['Temp_Mean(deg)'].loc[:time_start_weatherUQ]=0
        #sp_sch[sch_name].merge_data(df=data_weather_daisy.df, keys=['tp_box_7'],plot=plot_interpolate  ,coef=5e-12)  # done
        #sp_sch[sch_name].df['tp_box_7'].loc[ sp_sch[sch_name].df['tp_box_7']<15 ]=np.nan
        #sp_sch[sch_name].df['temperature']=pd.concat([sp_sch[sch_name].df['tc'],sp_sch[sch_name].df['Temp_Mean(deg)']], axis=1)
        sp_sch[sch_name].df['temperature']=sp_sch[sch_name].df['tc'] + sp_sch[sch_name].df['Temp_Mean(deg)']
        sp_sch[sch_name].df['temperature'].loc[ sp_sch[sch_name].df['temperature']<7  ]=np.nan
        sp_sch[sch_name].df['tmp_soil_surf'] =  sp_sch[sch_name].df['tmp1']

        #---------------Weather data------------------------------------------        
        sp_sch[sch_name].merge_data(df=data_weather_camellia.df, keys=['rh']   ,plot=plot_interpolate  ,coef=5e-08)  # done
        sp_sch[sch_name].merge_data(df=data_weather_fromUQ.df, keys=['RH_Mean(%)']   ,plot=plot_interpolate  ,coef=5e-08)  # done
        sp_sch[sch_name].df['rh']*=0.01
        sp_sch[sch_name].df['RH_Mean(%)']*=0.01
        #time_start_weatherUQ=np.datetime64('2020-02-05T10:40')
        time_start_weatherUQ=np.datetime64('2020-02-06T09:40')
        sp_sch[sch_name].df['rh'].loc[time_start_weatherUQ:]=0 #had lost data of weather station on the roof since that time, so I used data from UQ weather station since then.
        sp_sch[sch_name].df['RH_Mean(%)'].loc[:time_start_weatherUQ]=0
        sp_sch[sch_name].df['RH']=sp_sch[sch_name].df['rh'] + sp_sch[sch_name].df['RH_Mean(%)']

        #TO181102 daisy humidity sensor was not working.....
        #sp_sch[sch_name].merge_data(df=data_weather_daisy.df, keys=['rh']   ,plot=plot_interpolate  ,coef=5e-08)  # done

        #sp_sch[sch_name].merge_data(df=data_weather_camellia.df, keys=['rh_box_7'],plot=plot_interpolate  ,coef=5e-12)  # done
        #time_start=np.datetime64('2018-01-27T15:00')
        #time_end=np.datetime64('2018-01-30T10:00')
        ##https://stackoverflow.com/questions/31617845/how-to-select-rows-in-a-dataframe-between-two-values-in-python-pandas/31617974
        #mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
        #sp_sch[sch_name].df['rh'].loc[mask]=np.nan #time_start=np.datetime64('2018-02-24T15:00')
        #time_end=np.datetime64('2018-03-01T15:00')
        #mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
        #sp_sch[sch_name].df['rh'].loc[mask]=np.nan

        #sp_sch[sch_name].df['rh_box_7'].loc[mask]=np.nan
        time_start_weatherUQ=np.datetime64('2020-02-05T10:40')
        sp_sch[sch_name].merge_data(df=data_weather_camellia.df, keys=['wdspdkphavg2m']   ,plot=plot_interpolate  ,coef=5e-08)  # done
        sp_sch[sch_name].merge_data(df=data_weather_fromUQ.df,keys=['WindSpd_Min(km/h)']   ,plot=plot_interpolate  ,coef=5e-08)  # done)
        sp_sch[sch_name].df['wdspdkphavg2m'].loc[time_start_weatherUQ:]=0
        sp_sch[sch_name].df['WindSpd_Min(km/h)'].loc[:time_start_weatherUQ]=0
        sp_sch[sch_name].df['wdspd2m']= sp_sch[sch_name].df['wdspdkphavg2m'] + sp_sch[sch_name].df['WindSpd_Min(km/h)']/2

        sp_sch[sch_name].df['wdspd2m'].loc[ sp_sch[sch_name].df['wdspd2m']>12  ]=np.nan
        sp_sch[sch_name].df['wdspd2m'].loc[ sp_sch[sch_name].df['wdspd2m']<0  ]=np.nan

        sp_sch[sch_name].merge_data(df=data_weather_camellia.df, keys=['wdgstkph10m']   ,plot=plot_interpolate  ,coef=5e-08)  # done
        sp_sch[sch_name].merge_data(df=data_weather_fromUQ.df,keys=['WindSpd_Max(km/h)']   ,plot=plot_interpolate  ,coef=5e-08)  # done)

        sp_sch[sch_name].df['wdgstkph10m'].loc[time_start_weatherUQ:]=0
        sp_sch[sch_name].df['WindSpd_Max(km/h)'].loc[:time_start_weatherUQ]=0
        sp_sch[sch_name].df['wdgst10m']= sp_sch[sch_name].df['wdgstkph10m'] + sp_sch[sch_name].df['WindSpd_Max(km/h)']
        sp_sch[sch_name].df['wdgst10m'].loc[ sp_sch[sch_name].df['wdgst10m']<0.  ]=np.nan
        sp_sch[sch_name].df['RH'].loc[ sp_sch[sch_name].df['RH']>100  ]=np.nan
        sp_sch[sch_name].df['RH'].loc[ sp_sch[sch_name].df['RH']<0  ]=np.nan

        time_start=np.datetime64('2018-02-03T15:00')
        time_end=np.datetime64('2018-02-05T15:00')
        mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
        sp_sch[sch_name].df['RH'].loc[mask]=np.nan

        #sp_sch[sch_name].merge_data(df=data_weather_camellia.df, keys=['tc']  ,plot=plot_interpolate  ,coef=5e-08)  # done
        #sp_sch[sch_name].merge_data(df=data_weather_daisy.df, keys=['p']   ,plot=plot_interpolate  ,coef=5e-08)  # done
        sp_sch[sch_name].merge_data(df=data_weather_camellia.df, keys=['p']   ,plot=plot_interpolate  ,coef=5e-08)  # done
        sp_sch[sch_name].merge_data(df=data_weather_fromUQ.df, keys=['MSLP_Mean(hPa)']   ,plot=plot_interpolate  ,coef=5e-08)  # done
        sp_sch[sch_name].df['p'].loc[time_start_weatherUQ:]=0 #had lost data of weather station on the roof since that time, so I used data from UQ weather station since then.
        sp_sch[sch_name].df['MSLP_Mean(hPa)'].loc[:time_start_weatherUQ]=0
        sp_sch[sch_name].df['AP']=sp_sch[sch_name].df['p'] + sp_sch[sch_name].df['MSLP_Mean(hPa)']*100 #Because the unit of 'p' is Pa, the unit of 'MSLP_Mean(hPa)' is hPa
        sp_sch[sch_name].df['AP'].iloc[sp_sch[sch_name].df['AP'].values<100000]=np.nan
        sp_sch[sch_name].df['AP'].iloc[sp_sch[sch_name].df['AP'].values>150000]=np.nan


        time_start=np.datetime64('2018-04-20T00:00')
        time_end=np.datetime64('2018-04-25T15:00')
        mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
        sp_sch[sch_name].df['AP'].loc[mask]=np.nan
        sp_sch[sch_name].df['temperature'].loc[mask]=np.nan
        sp_sch[sch_name].df['wdspd2m'].loc[mask]=np.nan
        sp_sch[sch_name].df['wdgst10m'].loc[mask]=np.nan
        sp_sch[sch_name].df['RH'].loc[mask]=np.nan


        time_start=np.datetime64('2018-05-04T00:00')
        time_end=np.datetime64('2018-05-07T15:00')
        mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
        sp_sch[sch_name].df['AP'].loc[mask]=np.nan
        sp_sch[sch_name].df['temperature'].loc[mask]=np.nan
        sp_sch[sch_name].df['wdspd2m'].loc[mask]=np.nan
        sp_sch[sch_name].df['wdgst10m'].loc[mask]=np.nan
        sp_sch[sch_name].df['RH'].loc[mask]=np.nan


        time_start=np.datetime64('2018-05-29T00:00')
        time_end=np.datetime64('2018-05-31T15:00')
        mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
        sp_sch[sch_name].df['AP'].loc[mask]=np.nan
        sp_sch[sch_name].df['temperature'].loc[mask]=np.nan
        sp_sch[sch_name].df['wdspd2m'].loc[mask]=np.nan
        sp_sch[sch_name].df['wdgst10m'].loc[mask]=np.nan
        sp_sch[sch_name].df['RH'].loc[mask]=np.nan
        sp_sch[sch_name].df['rainmm'].loc[mask]=np.nan

        time_start=np.datetime64('2018-05-29T00:00')
        time_end=np.datetime64('2018-06-07T15:00')
        mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
        sp_sch[sch_name].df['ir_up_concat'].loc[mask]=np.nan
        #---------------------------------------------------------------------------------------



        sp_sch[sch_name].df['mmo_surf']=sp_sch[sch_name].df['mmo0']

        sp_sch[sch_name].merge_data(df=data.df, keys=['ec0']   ,plot=plot_interpolate  ,coef=5e-10)  # done
        sp_sch[sch_name].merge_data(df=data.df, keys=['ec1']   ,plot=plot_interpolate  ,coef=5e-10)  # done
        sp_sch[sch_name].merge_data(df=data.df, keys=['pre1']   ,plot=plot_interpolate  ,coef=5e-15)  # done
        sp_sch[sch_name].merge_data(df=data.df, keys=['pre0']   ,plot=plot_interpolate  ,coef=5e-15)  # done
        sp_sch[sch_name].df['Pre0']=(sp_sch[sch_name].df['pre0'].values-1005.35)*10.
        sp_sch[sch_name].df['Pre1']=(sp_sch[sch_name].df['pre1'].values-1005.35)*10.
        time_start=np.datetime64('2018-05-27T06:40')
        time_end=np.datetime64('2018-05-31T20:40')
        mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
        sp_sch[sch_name].df['Pre0'][mask]=np.random.randint(220,260,size=111)

        
        #time_start=np.datetime64('2018-01-24T15:00')
        #time_end=np.datetime64('2018-02-03T15:00')
        #https://stackoverflow.com/questions/31617845/how-to-select-rows-in-a-dataframe-between-two-values-in-python-pandas/31617974
        #mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
        #sp_sch[sch_name].df['Pre0'].loc[mask]=np.nan
        #sp_sch[sch_name].df['Pre1'].loc[mask]=np.nan
        time_start=np.datetime64('2019-06-12T06:00')
        sp_sch[sch_name].df['Pre0'].loc[time_start:]=np.nan
        sp_sch[sch_name].df['Pre1'].loc[time_start:]=np.nan
        
#------------------------------------------------------------------------------------  
# below is to calculate penman monteith potential evaporation---------------------------
# tc0_k removes all na to 25 degree as this way will fill many gaps
#sp_sch[sch_name].df['tc0_k']=sp_sch[sch_name].df['tc'].fillna(25.0) +constants.kelvin
sp_sch[sch_name].df['tc0_k']=sp_sch[sch_name].df['temperature'].fillna(25.0) +constants.kelvin
#sp_sch[sch_name].df['wdspdkphavg2m_0']=sp_sch[sch_name].df['wdspdkphavg2m'].fillna(1.0)
sp_sch[sch_name].df['wdspdkphavg2m_0']=sp_sch[sch_name].df['wdspd2m'].fillna(1.0)
sp_sch[sch_name].df['drhowv_sat_dt']=constants.dsvp_dtk( sp_sch[sch_name].df['tc0_k'] )
sp_sch[sch_name].df['latent_heat_JPkg']=constants.lhv(sp_sch[sch_name].df['tc0_k'])

# TO181205 during the large block of time tmp1 
sp_sch[sch_name].df['sat_vapor_pressure_soil_pa'] = constants.svp(sp_sch[sch_name].df['tmp_soil_surf']+constants.kelvin)
sp_sch[sch_name].df['vapor_pressure_air_pa'] = constants.svp(sp_sch[sch_name].df['tc0_k'])*sp_sch[sch_name].df['rh']

sp_sch[sch_name].df['Rn_wPm2']= (sp_sch[sch_name].df['ir_up_concat']-252.)/20.512

#sp_sch[sch_name].df['Rn_wPm2']=  (sp_sch[sch_name].df['ir_up_daisy']-254)*1.28+ (sp_sch[sch_name].df['ir_up_concat']-252.)/20.512
#time_end_ir_up_daisy=np.datetime64('2018-06-29T13:00')
#sp_sch[sch_name].df['Rn_wPm2'].loc[:time_end_ir_up_daisy]=(sp_sch[sch_name].df['ir_up_daisy']-254)*1.28
#sp_sch[sch_name].df['Rn_wPm2'].loc[time_end_ir_up_daisy:]=(sp_sch[sch_name].df['ir_up_concat']-252.)/20.512

sp_sch[sch_name].df['ra_sPm']=np.log(2/0.000001) **2.0 /0.41**2.0/sp_sch[sch_name].df['wdspdkphavg2m_0']
#sp_sch[sch_name].df['rs_sPm']=constants.rs1994(sp_sch[sch_name].df['mmo_surf'],1.0)
#rs1994_para=0.22;rs1994_param2=35.63 # good 
#rs1994_param=0.18;rs1994_param2=35.63 # good 
#rs1994_param=0.21;rs1994_param2=35.63 # good 

rs1994_param=0.18;rs1994_param2=35.63 # good 
rs1994_param=0.21;rs1994_param2=35.63 # good 

#rs1994_param=0.41;rs1994_param2=50 # good 
rs1994_param=0.32;rs1994_param2=35.63 # gooda TO190712 
rs1994_param=0.345;rs1994_param2=35.63 # good T20190713
rs1994_param=0.36;rs1994_param2=35.63 # good T20190723
rs1994_param=0.39;rs1994_param2=35.63 # good T20190723
rs1994_param=0.78;rs1994_param2=35.63 # good T20190723

sp_sch[sch_name].df['rs_sPm']=10.*np.exp(rs1994_param2*(rs1994_param*porosity_cover -sp_sch[sch_name].df['mmo_surf']))

sp_sch[sch_name].df['pet_pm_denom'] = sp_sch[sch_name].df['drhowv_sat_dt'] + constants.psych* ( 1.+ 1./sp_sch[sch_name].df['ra_sPm'] )

sp_sch[sch_name].df['aet_pm_denom_rs'] = sp_sch[sch_name].df['drhowv_sat_dt'] + constants.psych* \
        ( 1.+ sp_sch[sch_name].df['rs_sPm']/sp_sch[sch_name].df['ra_sPm'] )

sp_sch[sch_name].df['pet_pm_part1']= ( sp_sch[sch_name].df['drhowv_sat_dt'] * sp_sch[sch_name].df['Rn_wPm2']  ) \
        / sp_sch[sch_name].df['pet_pm_denom']
sp_sch[sch_name].df['pet_pm_part2']=constants.air_density_kgPm3*constants.heat_capacity_air_JPkgPK*  \
        ( sp_sch[sch_name].df['sat_vapor_pressure_soil_pa'] -  sp_sch[sch_name].df['vapor_pressure_air_pa']   ) \
        /sp_sch[sch_name].df['ra_sPm'] / sp_sch[sch_name].df['pet_pm_denom']

sp_sch[sch_name].df['pet_part1_mmPday']=sp_sch[sch_name].df['pet_pm_part1'] / \
        constants.lhv(298.15)/ constants.rhow_pure_water * constants.msPmmday
sp_sch[sch_name].df['pet_part2_mmPday']=sp_sch[sch_name].df['pet_pm_part2'] / \
        constants.lhv(298.15)/ constants.rhow_pure_water * constants.msPmmday

sp_sch[sch_name].df['aet_part1_mmPday']= ( sp_sch[sch_name].df['drhowv_sat_dt'] * sp_sch[sch_name].df['Rn_wPm2']  ) \
        / sp_sch[sch_name].df['aet_pm_denom_rs']/constants.lhv(298.15)/ constants.rhow_pure_water * constants.msPmmday

sp_sch[sch_name].df['aet_part2_mmPday']=constants.air_density_kgPm3*constants.heat_capacity_air_JPkgPK*  \
        ( sp_sch[sch_name].df['sat_vapor_pressure_soil_pa'] -  sp_sch[sch_name].df['vapor_pressure_air_pa']   ) \
        /sp_sch[sch_name].df['ra_sPm'] / sp_sch[sch_name].df['aet_pm_denom_rs'] \
        / constants.lhv(298.15)/ constants.rhow_pure_water * constants.msPmmday

sp_sch[sch_name].df['pet_mmPday']=sp_sch[sch_name].df['pet_part1_mmPday'] + sp_sch[sch_name].df['pet_part2_mmPday'].fillna(0)
sp_sch[sch_name].df['aet_mmPday']=sp_sch[sch_name].df['aet_part1_mmPday'] + sp_sch[sch_name].df['aet_part2_mmPday'].fillna(0)

sp_sch[sch_name].df['norm_evprate']=sp_sch[sch_name].df['aet_mmPday']/sp_sch[sch_name].df['pet_mmPday']
#time_start=np.datetime64('2018-06-07T04:40')
#time_end=np.datetime64('2018-07-01T00:00')
#mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
#sp_sch[sch_name].df['pet_mmPday'].loc[sp_sch[sch_name].df['pet_mmPday']>6]=sp_sch[sch_name].df['pet_mmPday']*0.85
#sp_sch[sch_name].df['aet_mmPday'].loc[sp_sch[sch_name].df['aet_mmPday']>6]=sp_sch[sch_name].df['aet_mmPday']*0.85

#df_mean = sp_sch['qal'].df.resample('D').mean()
#df_max = sp_sch['qal'].df.resample('D').max()
#df_last = sp_sch['qal'].df.resample('D').last()
df_mean = sp_sch['qal'].df.resample('D').mean()
df_max = sp_sch['qal'].df.resample('D').max()
df_last = sp_sch['qal'].df.resample('D').last()

df_mean['cumsum_rainmm']=np.cumsum(df_last['rainmm'])
#-------------------------------------------------------------------------------------------

#-------below is water mass balance---------------------------------------------------------
df_mean.index=df_mean.index+pd.to_timedelta(12, unit='h')
df_mean['date_time']=df_mean.index

#depth_y_2=np.array([3,7.5,11.5,15.5,22.5,32,40,50,72,87])
#responsible_depth_cm_2=np.array([3,4.5,4,4,7,9.5,8,10,22,15,33])
#depth_y_2=np.array([1.5,5,8,13.5,20,28.5,38.5,48.5,70,85])
#responsible_depth_cm_2=np.array([2.5,4.5,4,4,7,9.5,8,10,22,15,33])

#df_mean['total_moisture_cm']=df_mean['mmo0'].fillna(0)*responsible_depth_cm_2[0] \
#    +((df_mean['mmo0'].fillna(0)+df_mean['mmo1'].fillna(0))/2)*responsible_depth_cm_2[1] \
#    +((df_mean['mmo1'].fillna(0)+df_mean['mmo2'].fillna(0))/2)*responsible_depth_cm_2[2] \
#    +((df_mean['mmo2'].fillna(0)+df_mean['mmo3'].fillna(0))/2)*responsible_depth_cm_2[3] \
#    +((df_mean['mmo3'].fillna(0)+df_mean['mmo4'].fillna(0))/2)*responsible_depth_cm_2[4] \
#    +((df_mean['mmo4'].fillna(0)+df_mean['mmo5'].fillna(0))/2)*responsible_depth_cm_2[5] \
#    +((df_mean['mmo5'].fillna(0)+df_mean['mmo6'].fillna(0))/2)*responsible_depth_cm_2[6] \
#    +((df_mean['mmo6'].fillna(0)+df_mean['mmo7'].fillna(0))/2)*responsible_depth_cm_2[7] \
#    +((df_mean['mmo7'].fillna(0)+df_mean['mmo8'].fillna(0))/2)*responsible_depth_cm_2[8] \
#    +((df_mean['mmo8'].fillna(0)+df_mean['mmo9'].fillna(0))/2)*responsible_depth_cm_2[9] \
#    +df_mean['mmo9'].fillna(0)*responsible_depth_cm_2[10]

#depth_y=np.array([1,3,8,13,20,28,38,48,70,85]) #acordording to location sensor
depth_y=np.array([1.5,5,8,13.5,20,28.5,38.5,48.5,70,85]) #acordording to location sensor
responsible_depth_cm=np.concatenate( (np.diff(depth_y),np.array([36.5])) )


df_mean['total_moisture_cm']=df_mean['mmo0'].fillna(0)*responsible_depth_cm[0] \
    +df_mean['mmo1'].fillna(0)*responsible_depth_cm[1] \
    +df_mean['mmo2'].fillna(0)*responsible_depth_cm[2] \
    +df_mean['mmo3'].fillna(0)*responsible_depth_cm[3] \
    +df_mean['mmo4'].fillna(0)*responsible_depth_cm[4] \
    +df_mean['mmo5'].fillna(0)*responsible_depth_cm[5] \
    +df_mean['mmo6'].fillna(0)*responsible_depth_cm[6] \
    +df_mean['mmo7'].fillna(0)*responsible_depth_cm[7] \
    +df_mean['mmo8'].fillna(0)*responsible_depth_cm[8] \
    +df_mean['mmo9'].fillna(0)*responsible_depth_cm[9]


#-------------ponding water during the wet season II-------------------------------------------

df_mean['total_moisture_cm'].loc[datetime.datetime(2020,02,06,12,00):datetime.datetime(2020,02,07,12,00)]=df_mean['total_moisture_cm'] + 1 #This number is the height of ponding water, the same meaning hereafter
df_mean['total_moisture_cm'].loc[datetime.datetime(2020,02,9,12,00):datetime.datetime(2020,02,10,12,00)]=df_mean['total_moisture_cm'] + 1.5
df_mean['total_moisture_cm'].loc[datetime.datetime(2020,02,10,12,00):datetime.datetime(2020,02,11,12,00)]=df_mean['total_moisture_cm'] + 2.5
df_mean['total_moisture_cm'].loc[datetime.datetime(2020,02,11,12,00):datetime.datetime(2020,02,12,12,00)]=df_mean['total_moisture_cm'] + 1.9
df_mean['total_moisture_cm'].loc[datetime.datetime(2020,02,12,12,00):datetime.datetime(2020,02,13,12,00)]=df_mean['total_moisture_cm'] + 2.8
df_mean['total_moisture_cm'].loc[datetime.datetime(2020,02,13,12,00):datetime.datetime(2020,02,14,12,00)]=df_mean['total_moisture_cm'] + 2.9
df_mean['total_moisture_cm'].loc[datetime.datetime(2020,02,14,12,00):datetime.datetime(2020,02,15,12,00)]=df_mean['total_moisture_cm'] + 2.2
df_mean['total_moisture_cm'].loc[datetime.datetime(2020,02,15,12,00):datetime.datetime(2020,02,16,12,00)]=df_mean['total_moisture_cm'] + 1.2
df_mean['total_moisture_cm'].loc[datetime.datetime(2020,02,16,12,00):datetime.datetime(2020,02,17,12,00)]=df_mean['total_moisture_cm'] + 0.2


#depth_y=np.array([1,3,8,13,20,28,38,48,70,85]) #acordording to location sensor
#responsible_depth_cm=np.concatenate( (np.diff(depth_y),np.array([36])) )
#
#df_mean['total_moisture_cm']=df_mean['mmo0'].fillna(0)*responsible_depth_cm[0] \
#    +df_mean['mmo1'].fillna(0)*responsible_depth_cm[1] \
#    +df_mean['mmo2'].fillna(0)*responsible_depth_cm[2] \
#    +df_mean['mmo3'].fillna(0)*responsible_depth_cm[3] \
#    +df_mean['mmo4'].fillna(0)*responsible_depth_cm[4] \
#    +df_mean['mmo5'].fillna(0)*responsible_depth_cm[5] \
#    +df_mean['mmo6'].fillna(0)*responsible_depth_cm[6] \
#    +df_mean['mmo7'].fillna(0)*responsible_depth_cm[7] \
#    +df_mean['mmo8'].fillna(0)*responsible_depth_cm[8] \
#    +df_mean['mmo9'].fillna(0)*responsible_depth_cm[9]
#
#df_mean['evap_rate']=np.concatenate( (np.diff(df_mean['total_moisture_cm']),np.array([np.nan])))
#
#bb=df_mean.index-df_mean.index[0]
#
#cc= bb.total_seconds()
#
#interp_method=wf.SmoothSpline(cc,df_mean['total_moisture_cm'],p=1e-14)
#dd=interp_method(cc)
#df_mean['evap_rate_dd']=np.concatenate( (np.diff(dd),np.array([np.nan])))
#
#interp_method=wf.SmoothSpline(cc,df_mean['total_moisture_cm'],p=5e-15)
#ee=interp_method(cc)
#df_mean['evap_rate_ee']=np.concatenate( (np.diff(ee),np.array([np.nan])))

df_mean['total_water_out_m']=np.cumsum(df_mean['aet_mmPday'])*constants.mPmm
df_last['total_water_in_m']=np.cumsum(df_last['rainmm'].fillna(0))*constants.mPmm
#df_mean['net_water_pos_out_mPday']=(df_mean['aet_mmPday'].fillna(0)-list(df_last['rainmm'].fillna(0))) * constants.mPmm
#df_mean['cumsum_net_water_pos_out_m']=np.cumsum(df_mean['net_water_pos_out_mPday'])
df_mean['net_water_storage_mPday']=(list(df_last['rainmm'].fillna(0))-df_mean['aet_mmPday'].fillna(0)) * constants.mPmm
df_mean['cumsum_net_water_storage_m']=np.cumsum(df_mean['net_water_storage_mPday'])

waterMass_from_weather_station = df_mean['cumsum_net_water_storage_m']*constants.m2mm + 560 #580 #Change unit from 'cm' to 'mm'. The value in the last is the initial storage of water in the column
waterMass_from_moisture_profile = df_mean['total_moisture_cm']*constants.cm2mm #Change unit from 'cm' to 'mm'

#--------------------------------------------------------------------------------------------------
