import operator
import sensorfun
import json
py_compile.compile(os.environ['pyduino']+'/python/post_processing/sensorfun.py')
import sensorfun
reload(sensorfun)
py_compile.compile(os.environ['pyduino']+'/python/post_processing/figlib.py')
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


        #time_start=np.datetime64('2018-01-29T09:40')
        #time_switch=np.datetime64('2018-04-09T18:03')
        time_start=np.datetime64('2018-12-20T16:40')
        time_switch=np.datetime64('2019-05-01T00:40')
        #time_end=np.datetime64('2019-03-22T11:40')
        time_end=np.datetime64('2019-06-17T23:00')#date time of data updated
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
        


        sp_sch[sch_name].df['mmo0']=(310.0**alpha-sp_sch[sch_name].df['mo0']**alpha)/(310.**alpha-266**alpha)*schedule['porosity']   # 1 cm
        #sp_sch[sch_name].df['mmo0']=(295.0**alpha-sp_sch[sch_name].df['mo0']**alpha)/(295.**alpha-270**alpha)   # 1 cm
        sp_sch[sch_name].df['mmo1']=(345.0**alpha-sp_sch[sch_name].df['mo1']**alpha)/(345.**alpha-280**alpha)*schedule['porosity']   # 5 cm
        #sp_sch[sch_name].df['mmo1']=(550.0**alpha-sp_sch[sch_name].df['mo1']**alpha)/(550.**alpha-270**alpha)   # 5 cm
        sp_sch[sch_name].df['mmo2']=(310.0**alpha-sp_sch[sch_name].df['mo2']**alpha)/(310.**alpha-270**alpha)*schedule['porosity']   # 8 cm 
        #sp_sch[sch_name].df['mmo2']=(295.0**alpha-sp_sch[sch_name].df['mo2']**alpha)/(295.**alpha-270**alpha)   # 8 cm 
        sp_sch[sch_name].df['mmo3']=(300.0**alpha-sp_sch[sch_name].df['mo3']**alpha)/(300.0**alpha-270**alpha)*schedule['porosity']   # 13cm
        #sp_sch[sch_name].df['mmo3']=(295.0**alpha-sp_sch[sch_name].df['mo3']**alpha)/(295.**alpha-270**alpha)   # 13cm
        #sp_sch[sch_name].df['mmo4']=(295.0**alpha-sp_sch[sch_name].df['mo4']**alpha)/(295.**alpha-270**alpha)   # 20cm
        sp_sch[sch_name].df['mmo4']=(320.0**alpha-sp_sch[sch_name].df['mo4']**alpha)/(320.**alpha-270**alpha)*schedule['porosity']   # 20cm
        sp_sch[sch_name].df['mmo5']=(310.0**alpha-sp_sch[sch_name].df['mo5']**alpha)/(310.**alpha-280**alpha)*schedule['porosity']   # 28cm
        #sp_sch[sch_name].df['mmo5']=(295.0**alpha-sp_sch[sch_name].df['mo5']**alpha)/(295.**alpha-275**alpha)   # 28cm
        sp_sch[sch_name].df['mmo6']=(320.0**alpha-sp_sch[sch_name].df['mo6']**alpha)/(320.**alpha-276**alpha)*schedule['porosity']   # 38cm
        #sp_sch[sch_name].df['mmo6']=(550.0**alpha-sp_sch[sch_name].df['mo6']**alpha)/(550.**alpha-270**alpha)   # 38cm
        sp_sch[sch_name].df['mmo7']=(540.0**alpha-sp_sch[sch_name].df['mo7']**alpha)/(540.**alpha-275**alpha)*schedule['porosity']   # 48cm
        #sp_sch[sch_name].df['mmo7']=(550.0**alpha-sp_sch[sch_name].df['mo7']**alpha)/(530.**alpha-270**alpha)   # 48cm
        sp_sch[sch_name].df['mmo8']=(540.0**alpha-sp_sch[sch_name].df['mo8']**alpha)/(540.**alpha-285**alpha)*schedule['porosity']   # 70cm
        #sp_sch[sch_name].df['mmo8']=(550.0**alpha-sp_sch[sch_name].df['mo8']**alpha)/(550.**alpha-285**alpha)   # 70cm
        sp_sch[sch_name].df['mmo9']=(540.0**alpha-sp_sch[sch_name].df['mo9']**alpha)/(540.**alpha-276**alpha)*schedule['porosity']   # 85cm 
        #sp_sch[sch_name].df['mmo9']=(550.0**alpha-sp_sch[sch_name].df['mo9']**alpha)/(550.**alpha-275**alpha)   # 85cm

        #sp_sch[sch_name].df['mmo0']=sp_sch[sch_name].df['mmo0_p1'].fillna(0)+sp_sch[sch_name].df['mmo0_p2'].fillna(0)    # 1 cm
        #sp_sch[sch_name].df['mmo1']=sp_sch[sch_name].df['mmo1_p1'].fillna(0)+sp_sch[sch_name].df['mmo1_p2'].fillna(0)    # 5 cm
        #sp_sch[sch_name].df['mmo2']=sp_sch[sch_name].df['mmo2_p1'].fillna(0)+sp_sch[sch_name].df['mmo2_p2'].fillna(0)    # 8 cm
        #sp_sch[sch_name].df['mmo3']=sp_sch[sch_name].df['mmo3_p1'].fillna(0)+sp_sch[sch_name].df['mmo3_p2'].fillna(0)    # 13 cm
        #sp_sch[sch_name].df['mmo4']=sp_sch[sch_name].df['mmo4_p1'].fillna(0)+sp_sch[sch_name].df['mmo4_p2'].fillna(0)    # 20 cm
        #sp_sch[sch_name].df['mmo5']=sp_sch[sch_name].df['mmo5_p1'].fillna(0)+sp_sch[sch_name].df['mmo5_p2'].fillna(0)    # 28 cm
        #sp_sch[sch_name].df['mmo6']=sp_sch[sch_name].df['mmo6_p1'].fillna(0)+sp_sch[sch_name].df['mmo6_p2'].fillna(0)    # 38 cm
        #sp_sch[sch_name].df['mmo7']=sp_sch[sch_name].df['mmo7_p1'].fillna(0)+sp_sch[sch_name].df['mmo7_p2'].fillna(0)    # 48 cm
        #sp_sch[sch_name].df['mmo8']=sp_sch[sch_name].df['mmo8_p1'].fillna(0)+sp_sch[sch_name].df['mmo8_p2'].fillna(0)    # 70 cm
        #sp_sch[sch_name].df['mmo9']=sp_sch[sch_name].df['mmo9_p1'].fillna(0)+sp_sch[sch_name].df['mmo9_p2'].fillna(0)    # 85 cm

        sp_sch[sch_name].merge_data(df=data_weather_daisy.df, keys=['ir_up']   ,plot=plot_interpolate  ,coef=5e-4)
        sp_sch[sch_name].merge_data(df=data_weather_daisy.df, keys=['ir_down']   ,plot=plot_interpolate  ,coef=5e-4)
        sp_sch[sch_name].merge_data(df=data_weather_camellia.df, keys=['dlyrainmm']   ,plot=plot_interpolate  ,coef=5e-08)  # done
        #sp_sch[sch_name].df['rainmm']= sp_sch[sch_name].df['dlyrainmm']
        #time_start=np.datetime64('2018-04-20T10:00')
        #time_end=np.datetime64('2018-04-20T23:00')
        #mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
        #sp_sch[sch_name].df.loc[mask,'rainmm']=np.linspace(0.93,15,np.sum(mask) )
        #sp_sch[sch_name].df['mmo0'].loc[ sp_sch[sch_name].df['mmo0']>0.53]=0.53
        #sp_sch[sch_name].df['mmo1'].loc[ sp_sch[sch_name].df['mmo1']>0.53]=0.53
        #sp_sch[sch_name].df['mmo2'].loc[ sp_sch[sch_name].df['mmo2']>0.53]=0.53
        #sp_sch[sch_name].df['mmo3'].loc[ sp_sch[sch_name].df['mmo3']>0.53]=0.53
        #sp_sch[sch_name].df['mmo4'].loc[ sp_sch[sch_name].df['mmo4']>0.53]=0.53
        #sp_sch[sch_name].df['mmo5'].loc[ sp_sch[sch_name].df['mmo5']>0.53]=0.53
        #sp_sch[sch_name].df['mmo6'].loc[ sp_sch[sch_name].df['mmo6']>0.53]=0.53
        sp_sch[sch_name].df['mmo7'].loc[ sp_sch[sch_name].df['mmo7']>0.53]=0.53
        #sp_sch[sch_name].df['mmo8'].loc[ sp_sch[sch_name].df['mmo8']>0.53]=0.53
        #sp_sch[sch_name].df['mmo9'].loc[ sp_sch[sch_name].df['mmo9']>0.53]=0.53
        
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

        #time_start=np.datetime64('2018-02-23T15:00')
        #time_end=np.datetime64('2018-03-02T15:00')
        #mask=data_weather_camellia.df['date_time'].between(time_start,time_end)
        #data_weather_camellia.df['rh_box_7'].loc[mask]=np.nan


        sp_sch[sch_name].merge_data(df=data_weather_camellia.df, keys=['rh']   ,plot=plot_interpolate  ,coef=5e-08)  # done
        sp_sch[sch_name].df['rh']*=0.01
        sp_sch[sch_name].df['rh'].loc[ sp_sch[sch_name].df['rh']>100  ]=np.nan
        sp_sch[sch_name].df['rh'].loc[ sp_sch[sch_name].df['rh']<0  ]=np.nan
       
        #sp_sch[sch_name].merge_data(df=data_weather_camellia.df, keys=['rh_box_7'],plot=plot_interpolate  ,coef=5e-12)  # done
        #time_start=np.datetime64('2018-01-27T15:00')
        #time_end=np.datetime64('2018-01-30T10:00')
        #https://stackoverflow.com/questions/31617845/how-to-select-rows-in-a-dataframe-between-two-values-in-python-pandas/31617974
        #mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
        #sp_sch[sch_name].df['rh'].loc[mask]=np.nan

        #time_start=np.datetime64('2018-02-24T15:00')
        #time_end=np.datetime64('2018-03-01T15:00')
        #mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
        #sp_sch[sch_name].df['rh'].loc[mask]=np.nan

 
        #----------------modify relative humidity of June--------------
        time_start=np.datetime64('2018-06-01T10:00')
        time_end=np.datetime64('2018-06-30T10:00')
        mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
        sp_sch[sch_name].df['rh'][mask].fillna(0.45).loc[ sp_sch[sch_name].df['rh']>0.8 ]=sp_sch[sch_name].df['rh']*0.45
        sp_sch[sch_name].df['rh'][mask].fillna(0.45).loc[ sp_sch[sch_name].df['rh']<0.2  ]=sp_sch[sch_name].df['rh']*4


        sp_sch[sch_name].df['rh'][mask].loc[ sp_sch[sch_name].df['rh']>0.8 ]=np.nan
        sp_sch[sch_name].df['rh'][mask].loc[ sp_sch[sch_name].df['rh']<0.1 ]=np.nan
        
        time_start=np.datetime64('2018-06-08T18:40')
        time_end=np.datetime64('2018-06-09T05:40')
        sp_sch[sch_name].df['rh'].loc[time_start:time_end]=sp_sch[sch_name].df['rh']*0.7

        time_start=np.datetime64('2018-06-12T23:40')
        time_end=np.datetime64('2018-06-13T06:40')
        sp_sch[sch_name].df['rh'].loc[time_start:time_end]=sp_sch[sch_name].df['rh']*0.7

        time_start=np.datetime64('2018-06-21T23:40')
        time_end=np.datetime64('2018-06-22T05:40')
        sp_sch[sch_name].df['rh'].loc[time_start:time_end]=sp_sch[sch_name].df['rh']*0.7

        time_start=np.datetime64('2018-06-23T16:40')
        time_end=np.datetime64('2018-06-24T03:40')
        sp_sch[sch_name].df['rh'].loc[time_start:time_end]=sp_sch[sch_name].df['rh']*0.7

        time_start=np.datetime64('2018-06-26T16:40')
        time_end=np.datetime64('2018-06-28T22:40')
        sp_sch[sch_name].df['rh'].loc[time_start:time_end]=sp_sch[sch_name].df['rh']*0.5

        #-------------------------------------------------------------------------------

        #sp_sch[sch_name].df['rh_box_7'][mask]=np.nan
        sp_sch[sch_name].merge_data(df=data_weather_camellia.df, keys=['wdspdkphavg2m']   ,plot=plot_interpolate  ,coef=5e-08)  # done
        time_start=np.datetime64('2018-02-24T00:00')
        sp_sch[sch_name].df['wdspdkphavg2m'].loc[mask]=np.nan
        sp_sch[sch_name].df['wdspdkphavg2m'].loc[ sp_sch[sch_name].df['wdspdkphavg2m']>12  ]=np.nan
        sp_sch[sch_name].df['wdspdkphavg2m'].loc[ sp_sch[sch_name].df['wdspdkphavg2m']<0  ]=np.nan

        sp_sch[sch_name].merge_data(df=data_weather_camellia.df, keys=['wdgstkph10m']   ,plot=plot_interpolate  ,coef=5e-08)  # done
        #time_start=np.datetime64('2018-02-24T00:00')
        #sp_sch[sch_name].df['wdgstkph10m'][mask]=np.nan
        sp_sch[sch_name].df['wdgstkph10m'].loc[ sp_sch[sch_name].df['wdgstkph10m']<0.  ]=np.nan



        #time_start=np.datetime64('2018-02-03T15:00')
        #time_end=np.datetime64('2018-02-05T15:00')
        #mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
        #sp_sch[sch_name].df['rh'].loc[mask]=np.nan
        #sp_sch[sch_name].df['rh'].loc[ sp_sch[sch_name].df['rh']>100  ]=np.nan
        #sp_sch[sch_name].df['rh'].loc[ sp_sch[sch_name].df['rh']<0  ]=np.nan



        sp_sch[sch_name].merge_data(df=data_weather_camellia.df, keys=['tc']  ,plot=plot_interpolate  ,coef=5e-08)  # done
        #sp_sch[sch_name].merge_data(df=data_weather_daisy.df, keys=['tp_box_7'],plot=plot_interpolate  ,coef=5e-12)  # done
        sp_sch[sch_name].df['tc'].loc[ sp_sch[sch_name].df['tc']<9  ]=np.nan
        #sp_sch[sch_name].df['tp_box_7'].loc[ sp_sch[sch_name].df['tp_box_7']<15 ]=np.nan
        
        sp_sch[sch_name].df['tmp_soil_surf'] =  sp_sch[sch_name].df['tmp1']
        #sp_sch[sch_name].df['tmp_soil_surf'] =  data.df['gstmp0']*1.1
        #sp_sch[sch_name].df['tmp_soil_surf'].loc[mask_output]=  sp_sch[sch_name].df['tc'].loc[mask_output]


        # this was in 20180522
        #sp_sch[sch_name].merge_data(df=data_weather_daisy.df, keys=['rainmm']   ,plot=plot_interpolate  ,coef=5e-08)  # done

        # below was working in 20181023
        sp_sch[sch_name].merge_data(df=data_weather_camellia.df, keys=['dlyrainmm']   ,plot=plot_interpolate  ,coef=5e-08)  # done
        sp_sch[sch_name].df['rainmm']= sp_sch[sch_name].df['dlyrainmm']
        #time_start=np.datetime64('2018-04-20T10:00')
        #time_end=np.datetime64('2018-04-20T23:59')
        #mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
        #sp_sch[sch_name].df.loc[mask,'rainmm']=np.linspace(0.93,18,np.sum(mask) )
        #sp_sch[sch_name].df['rainmm'].loc[sp_sch[sch_name].df['rainmm']<0]=0
        #sp_sch[sch_name].df['rainmm'].loc[sp_sch[sch_name].df['rainmm']>40]=0.5

        # this is done because the sensors are made upside down later, also, some of the weather stations needs to make updates

        sp_sch[sch_name].merge_data(df=data_weather_daisy.df, keys=['ir_up']   ,plot=plot_interpolate  ,coef=5e-4,new_keys=['ir_up_daisy'])
        sp_sch[sch_name].merge_data(df=data_weather_daisy.df, keys=['ir_down']   ,plot=plot_interpolate  ,coef=5e-4,new_keys=['ir_down_daisy'])
        sp_sch[sch_name].merge_data(df=data_weather_camellia.df, keys=['ir_down']   ,plot=plot_interpolate  ,coef=5e-4,new_keys=['ir_up_camellia'])


        #sp_sch[sch_name].df['ir_up_daisy'].loc[sp_sch[sch_name].df['ir_up_daisy']>19512]=np.nan
        sp_sch[sch_name].df['ir_up_daisy'].loc[sp_sch[sch_name].df['ir_up_daisy']>1000]=sp_sch[sch_name].df['ir_up_daisy']*0.2
        sp_sch[sch_name].df['ir_up_daisy'].loc[sp_sch[sch_name].df['ir_up_daisy']<252]=252   # if it is given as np.nan, there will be breaking points
        sp_sch[sch_name].df['ir_up_camellia'].loc[sp_sch[sch_name].df['ir_up_camellia']<252]=252
        sp_sch[sch_name].df['ir_up_camellia'].loc[sp_sch[sch_name].df['ir_up_camellia']>19512]=np.nan
        # the correction here is to ensure camellia shows same value as daisy
        sp_sch[sch_name].df['ir_up_camellia_cor'] = (sp_sch[sch_name].df['ir_up_camellia']-252) *1.17+252


        #--------modify the 'ir_up_daisy' data value during the night to 252
        sp_sch[sch_name].df['ir_up_daisy'].loc[np.datetime64('2018-06-08T00:40'):np.datetime64('2018-06-08T06:40')]=252
        sp_sch[sch_name].df['ir_up_daisy'].loc[np.datetime64('2018-06-08T18:40'):np.datetime64('2018-06-08T23:40')]=252
        sp_sch[sch_name].df['ir_up_daisy'].loc[np.datetime64('2018-06-09T00:40'):np.datetime64('2018-06-09T06:40')]=252
        sp_sch[sch_name].df['ir_up_daisy'].loc[np.datetime64('2018-06-09T18:40'):np.datetime64('2018-06-09T23:40')]=252
        sp_sch[sch_name].df['ir_up_daisy'].loc[np.datetime64('2018-06-10T00:40'):np.datetime64('2018-06-10T06:40')]=252
        sp_sch[sch_name].df['ir_up_daisy'].loc[np.datetime64('2018-06-10T18:40'):np.datetime64('2018-06-10T23:40')]=252
        sp_sch[sch_name].df['ir_up_daisy'].loc[np.datetime64('2018-06-11T00:40'):np.datetime64('2018-06-11T06:40')]=252
        sp_sch[sch_name].df['ir_up_daisy'].loc[np.datetime64('2018-06-11T18:40'):np.datetime64('2018-06-11T23:40')]=252
        sp_sch[sch_name].df['ir_up_daisy'].loc[np.datetime64('2018-06-12T00:40'):np.datetime64('2018-06-12T06:40')]=252
        sp_sch[sch_name].df['ir_up_daisy'].loc[np.datetime64('2018-06-12T18:40'):np.datetime64('2018-06-12T23:40')]=252
        sp_sch[sch_name].df['ir_up_daisy'].loc[np.datetime64('2018-06-13T00:40'):np.datetime64('2018-06-13T06:40')]=252
        sp_sch[sch_name].df['ir_up_daisy'].loc[np.datetime64('2018-06-13T18:40'):np.datetime64('2018-06-13T23:40')]=252
        sp_sch[sch_name].df['ir_up_daisy'].loc[np.datetime64('2018-06-14T00:40'):np.datetime64('2018-06-14T06:40')]=252
        sp_sch[sch_name].df['ir_up_daisy'].loc[np.datetime64('2018-06-14T18:40'):np.datetime64('2018-06-14T23:40')]=252
        sp_sch[sch_name].df['ir_up_daisy'].loc[np.datetime64('2018-06-15T00:40'):np.datetime64('2018-06-15T06:40')]=252
        sp_sch[sch_name].df['ir_up_daisy'].loc[np.datetime64('2018-06-15T18:40'):np.datetime64('2018-06-15T23:40')]=252
        sp_sch[sch_name].df['ir_up_daisy'].loc[np.datetime64('2018-06-16T00:40'):np.datetime64('2018-06-16T06:40')]=252
        sp_sch[sch_name].df['ir_up_daisy'].loc[np.datetime64('2018-06-16T18:40'):np.datetime64('2018-06-16T23:40')]=252
        sp_sch[sch_name].df['ir_up_daisy'].loc[np.datetime64('2018-06-17T00:40'):np.datetime64('2018-06-17T06:40')]=252
        sp_sch[sch_name].df['ir_up_daisy'].loc[np.datetime64('2018-06-17T18:40'):np.datetime64('2018-06-17T23:40')]=252
        sp_sch[sch_name].df['ir_up_daisy'].loc[np.datetime64('2018-06-18T00:40'):np.datetime64('2018-06-18T06:40')]=252
        sp_sch[sch_name].df['ir_up_daisy'].loc[np.datetime64('2018-06-18T18:40'):np.datetime64('2018-06-18T23:40')]=252
        sp_sch[sch_name].df['ir_up_daisy'].loc[np.datetime64('2018-06-19T00:40'):np.datetime64('2018-06-19T06:40')]=252
        sp_sch[sch_name].df['ir_up_daisy'].loc[np.datetime64('2018-06-19T18:40'):np.datetime64('2018-06-19T23:40')]=252
        sp_sch[sch_name].df['ir_up_daisy'].loc[np.datetime64('2018-06-20T00:40'):np.datetime64('2018-06-20T06:40')]=252
        sp_sch[sch_name].df['ir_up_daisy'].loc[np.datetime64('2018-06-20T18:40'):np.datetime64('2018-06-20T23:40')]=252
        sp_sch[sch_name].df['ir_up_daisy'].loc[np.datetime64('2018-06-21T00:40'):np.datetime64('2018-06-21T06:40')]=252
        sp_sch[sch_name].df['ir_up_daisy'].loc[np.datetime64('2018-06-21T18:40'):np.datetime64('2018-06-21T23:40')]=252
        sp_sch[sch_name].df['ir_up_daisy'].loc[np.datetime64('2018-06-22T00:40'):np.datetime64('2018-06-22T06:40')]=252
        sp_sch[sch_name].df['ir_up_daisy'].loc[np.datetime64('2018-06-22T18:40'):np.datetime64('2018-06-22T23:40')]=252
        sp_sch[sch_name].df['ir_up_daisy'].loc[np.datetime64('2018-06-23T00:40'):np.datetime64('2018-06-23T06:40')]=252
        sp_sch[sch_name].df['ir_up_daisy'].loc[np.datetime64('2018-06-23T18:40'):np.datetime64('2018-06-23T23:40')]=252
        sp_sch[sch_name].df['ir_up_daisy'].loc[np.datetime64('2018-06-24T00:40'):np.datetime64('2018-06-24T06:40')]=252
        sp_sch[sch_name].df['ir_up_daisy'].loc[np.datetime64('2018-06-24T18:40'):np.datetime64('2018-06-24T23:40')]=252
        sp_sch[sch_name].df['ir_up_daisy'].loc[np.datetime64('2018-06-25T00:40'):np.datetime64('2018-06-25T06:40')]=252
        sp_sch[sch_name].df['ir_up_daisy'].loc[np.datetime64('2018-06-25T18:40'):np.datetime64('2018-06-25T23:40')]=252
        sp_sch[sch_name].df['ir_up_daisy'].loc[np.datetime64('2018-06-26T00:40'):np.datetime64('2018-06-26T06:40')]=252
        sp_sch[sch_name].df['ir_up_daisy'].loc[np.datetime64('2018-06-26T18:40'):np.datetime64('2018-06-26T23:40')]=252
        sp_sch[sch_name].df['ir_up_daisy'].loc[np.datetime64('2018-06-27T00:40'):np.datetime64('2018-06-27T06:40')]=252
        sp_sch[sch_name].df['ir_up_daisy'].loc[np.datetime64('2018-06-27T18:40'):np.datetime64('2018-06-27T23:40')]=252
        sp_sch[sch_name].df['ir_up_daisy'].loc[np.datetime64('2018-06-28T00:40'):np.datetime64('2018-06-28T06:40')]=252
        sp_sch[sch_name].df['ir_up_daisy'].loc[np.datetime64('2018-06-28T18:40'):np.datetime64('2018-06-28T23:40')]=252




        # the script below uses early results from daisy while later results from camellia. 
        time_start=np.datetime64('2018-06-29T13:00')
        time_end=np.datetime64('2018-10-21T17:00')
        mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
        #--------modify the plot of daily evaporation----------------------------
        #time_start=np.datetime64('2018-01-29T09:40')
        #time_start_ir_up_daisy=np.datetime64('2018-04-09T18:30')
        time_end_ir_up_daisy=np.datetime64('2018-06-29T13:00')
        #time_end=np.datetime64('2019-03-22T04:30')
        #mask1=sp_sch[sch_name].df['date_time'].between(time_start,time_end_ir_up_daisy)
        #mask2=sp_sch[sch_name].df['date_time'].between(time_end_ir_up_daisy,time_end)
        #sp_sch[sch_name].df['ir_up_daisy'][mask2]=0
        #sp_sch[sch_name].df['ir_up_camellia'][mask1]=0
        #sp_sch[sch_name].df['ir_up_daisy'].loc[:time_start_ir_up_daisy]=0
        sp_sch[sch_name].df['ir_up_daisy'].loc[time_end_ir_up_daisy:]=0
        #sp_sch[sch_name].df['ir_up_camellia'].loc[time_start_ir_up_daisy:time_end_ir_up_daisy]=0
        sp_sch[sch_name].df['ir_up_camellia'].loc[:time_end_ir_up_daisy]=0


        #time_start_ir_up_camellia=np.datetime64('2018-06-29T13:00')
        #sp_sch[sch_name].df['ir_up_daisy'].loc[time_end_ir_up_daisy:]=0
        #sp_sch[sch_name].df['ir_up_camellia'].loc[:time_start_ir_up_camellia]=0
        #-------------------------------------------------------------------------
        #sp_sch[sch_name].df['ir_up_concat']=sp_sch[sch_name].df['ir_up_daisy']
        sp_sch[sch_name].df['ir_up_concat']=sp_sch[sch_name].df['ir_up_camellia']
        sp_sch[sch_name].df.loc[mask,'ir_up_concat']=      sp_sch[sch_name].df.loc[mask,'ir_up_camellia_cor']
       

        time_start=np.datetime64('2018-06-01T00:00')
        time_end=np.datetime64('2018-08-01T00:00')
        mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)

        sp_sch[sch_name].df['mmo_surf']=sp_sch[sch_name].df['mmo0']


        #sp_sch[sch_name].merge_data(df=data_weather_daisy.df, keys=['p']   ,plot=plot_interpolate  ,coef=5e-08)  # done
        sp_sch[sch_name].merge_data(df=data_weather_camellia.df, keys=['p']   ,plot=plot_interpolate  ,coef=5e-08)  # done
        sp_sch[sch_name].df['p'].iloc[sp_sch[sch_name].df['p'].values<100000]=np.nan
        sp_sch[sch_name].df['p'].iloc[sp_sch[sch_name].df['p'].values>150000]=np.nan
        #sp_sch[sch_name].merge_data(df=data.df, keys=['dhthum0'],plot=plot_interpolate  ,coef=5e-12)  # done

        #sp_sch[sch_name].merge_data(df=data_weather_daisy.df, keys=['rh']   ,plot=plot_interpolate  ,coef=5e-08)  # done



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
        


        time_start=np.datetime64('2018-04-20T00:00')
        time_end=np.datetime64('2018-04-25T15:00')
        mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
        sp_sch[sch_name].df['p'].loc[mask]=np.nan
        sp_sch[sch_name].df['tc'].loc[mask]=np.nan
        sp_sch[sch_name].df['wdspdkphavg2m'].loc[mask]=np.nan
        sp_sch[sch_name].df['wdgstkph10m'].loc[mask]=np.nan
        sp_sch[sch_name].df['rh'].loc[mask]=np.nan




        time_start=np.datetime64('2018-05-04T00:00')
        time_end=np.datetime64('2018-05-07T15:00')
        mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
        sp_sch[sch_name].df['p'].loc[mask]=np.nan
        sp_sch[sch_name].df['tc'].loc[mask]=np.nan
        sp_sch[sch_name].df['wdspdkphavg2m'].loc[mask]=np.nan
        sp_sch[sch_name].df['wdgstkph10m'].loc[mask]=np.nan
        sp_sch[sch_name].df['rh'].loc[mask]=np.nan


        time_start=np.datetime64('2018-05-29T00:00')
        time_end=np.datetime64('2018-05-31T15:00')
        mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
        sp_sch[sch_name].df['p'].loc[mask]=np.nan
        sp_sch[sch_name].df['tc'].loc[mask]=np.nan
        sp_sch[sch_name].df['wdspdkphavg2m'].loc[mask]=np.nan
        sp_sch[sch_name].df['wdgstkph10m'].loc[mask]=np.nan
        sp_sch[sch_name].df['rh'].loc[mask]=np.nan
        sp_sch[sch_name].df['rainmm'].loc[mask]=np.nan

        time_start=np.datetime64('2018-05-29T00:00')
        time_end=np.datetime64('2018-06-07T15:00')
        mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
        sp_sch[sch_name].df['ir_up_concat'].loc[mask]=np.nan

# below is to calculate penman monteith potential evaporation---------------------------
# tc0_k removes all na to 25 degree as this way will fill many gaps
sp_sch[sch_name].df['tc0_k']=sp_sch[sch_name].df['tc'].fillna(25.0) +constants.kelvin
sp_sch[sch_name].df['wdspdkphavg2m_0']=sp_sch[sch_name].df['wdspdkphavg2m'].fillna(1.0)

sp_sch[sch_name].df['drhowv_sat_dt']=constants.dsvp_dtk( sp_sch[sch_name].df['tc0_k'] )
sp_sch[sch_name].df['latent_heat_JPkg']=constants.lhv(sp_sch[sch_name].df['tc0_k'])

# TO181205 during the large block of time tmp1 
sp_sch[sch_name].df['sat_vapor_pressure_soil_pa'] = constants.svp(sp_sch[sch_name].df['tmp_soil_surf']+constants.kelvin)
sp_sch[sch_name].df['vapor_pressure_air_pa'] = constants.svp(sp_sch[sch_name].df['tc0_k'])*sp_sch[sch_name].df['rh']
sp_sch[sch_name].df['Rn_wPm2']=  (sp_sch[sch_name].df['ir_up_daisy']-254)*1.28+ (sp_sch[sch_name].df['ir_up_concat']-252.)/20.512
time_end_ir_up_daisy=np.datetime64('2018-06-29T13:00')
sp_sch[sch_name].df['Rn_wPm2'].loc[:time_end_ir_up_daisy]=(sp_sch[sch_name].df['ir_up_daisy']-254)*1.28
#sp_sch[sch_name].df['Rn_wPm2_part1']=(sp_sch[sch_name].df['ir_up_daisy'].loc[:time_end_ir_up_daisy]-254)*1.28
#sp_sch[sch_name].df['Rn_wPm2_part1'].loc[sp_sch[sch_name].df['Rn_wPm2_part1']<0]=0
sp_sch[sch_name].df['Rn_wPm2'].loc[time_end_ir_up_daisy:]=(sp_sch[sch_name].df['ir_up_concat']-252.)/20.512
#sp_sch[sch_name].df['Rn_wPm2'].loc[sp_sch[sch_name].df['Rn_wPm2']<0]=np.nan
#sp_sch[sch_name].df['Rn_wPm2_part2']=(sp_sch[sch_name].df['ir_up_concat'].loc[time_end_ir_up_daisy:]-252.)/20.512
#sp_sch[sch_name].df['Rn_wPm2_part2'].loc[sp_sch[sch_name].df['Rn_wPm2_part2']<0]=0
#sp_sch[sch_name].df['Rn_wPm2']=sp_sch[sch_name].df['Rn_wPm2_part1']+sp_sch[sch_name].df['Rn_wPm2_part2']
#sp_sch[sch_name].df['Rn_wPm2']=  (sp_sch[sch_name].df['ir_up_daisy']-254)*1.18+ (sp_sch[sch_name].df['ir_up_concat']-252.)/20.512

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
#time_start=np.datetime64('2018-03-27 19:00')
#time_switch=np.datetime64('2018-11-01 00:00')
#time_end=np.datetime64('2019-03-04T06:30')
#mask1=sp_sch[sch_name].df['date_time'].between(time_start,time_switch)
#mask2=sp_sch[sch_name].df['date_time'].between(time_switch,time_end)

sp_sch[sch_name].df['rs_sPm']=10.*np.exp(rs1994_param2*(rs1994_param- sp_sch[sch_name].df['mmo_surf']  ))

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
depth_y=np.array([1,3,8,13,20,28,38,48,70,85]) #acordording to location sensor
depth_y=np.array([1,3,8,13,20,28,38,48,70,85])
responsible_depth_cm=np.concatenate( (np.diff(depth_y),np.array([36])) )

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

df_mean['evap_rate']=np.concatenate( (np.diff(df_mean['total_moisture_cm']),np.array([np.nan])))

df_mean['total_moisture_07_cm']=df_mean['mmo0'].fillna(0)*responsible_depth_cm[0] \
    +df_mean['mmo1'].fillna(0)*responsible_depth_cm[1] \
    +df_mean['mmo2'].fillna(0)*responsible_depth_cm[2] \
    +df_mean['mmo3'].fillna(0)*responsible_depth_cm[3] \
    +df_mean['mmo4'].fillna(0)*responsible_depth_cm[4] \
    +df_mean['mmo5'].fillna(0)*responsible_depth_cm[5] \
    +df_mean['mmo6'].fillna(0)*responsible_depth_cm[6] \
    +df_mean['mmo7'].fillna(0)*responsible_depth_cm[7]

bb=df_mean.index-df_mean.index[0]

cc= bb.total_seconds()

interp_method=wf.SmoothSpline(cc,df_mean['total_moisture_cm'],p=1e-14)
dd=interp_method(cc)
df_mean['evap_rate_dd']=np.concatenate( (np.diff(dd),np.array([np.nan])))

interp_method=wf.SmoothSpline(cc,df_mean['total_moisture_cm'],p=5e-15)
ee=interp_method(cc)
df_mean['evap_rate_ee']=np.concatenate( (np.diff(ee),np.array([np.nan])))

df_mean['total_water_out_m']=np.cumsum(df_mean['aet_mmPday'])*constants.mPmm
df_last['total_water_in_m']=np.cumsum(df_last['rainmm'].fillna(0))*constants.mPmm
#df_mean['net_water_pos_out_mPday']=(df_mean['aet_mmPday'].fillna(0)-list(df_last['rainmm'].fillna(0))) * constants.mPmm
#df_mean['cumsum_net_water_pos_out_m']=np.cumsum(df_mean['net_water_pos_out_mPday'])
df_mean['net_water_storage_mPday']=(list(df_last['rainmm'].fillna(0))-df_mean['aet_mmPday'].fillna(0)) * constants.mPmm
df_mean['cumsum_net_water_storage_m']=np.cumsum(df_mean['net_water_storage_mPday'])

#--------------------------------------------------------------------------------------------------
