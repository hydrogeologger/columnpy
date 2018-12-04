import operator
import sensorfun
py_compile.compile(os.environ['pyduino']+'/python/post_processing/sensorfun.py')
import sensorfun
reload(sensorfun)
py_compile.compile(os.environ['pyduino']+'/python/post_processing/figlib.py')
import json
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
schedule['porosity']=1-schedule['average_dry_density']/schedule['specific_gravity']

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
        sp_sch[sch_name].merge_data(df=data.df, keys=['ec0']   ,plot=plot_interpolate  ,coef=5e-10)  # done
        sp_sch[sch_name].merge_data(df=data.df, keys=['tmp2']   ,plot=plot_interpolate  ,coef=5e-10)  # done
        sp_sch[sch_name].merge_data(df=data.df, keys=['pre1']   ,plot=plot_interpolate  ,coef=5e-15)  # done
        sp_sch[sch_name].merge_data(df=data.df, keys=['pre0']   ,plot=plot_interpolate  ,coef=5e-15)  # done
        sp_sch[sch_name].df['pre0']=(sp_sch[sch_name].df['pre0'].values-1005.35)*10.
        sp_sch[sch_name].df['pre1']=(sp_sch[sch_name].df['pre1'].values-1005.35)*10.

        time_start = np.datetime64('2018-02-27T08:00')
        time_end   = np.datetime64('2018-04-09T00:00')
        ##https://stackoverflow.com/questions/31617845/how-to-select-rows-in-a-dataframe-between-two-values-in-python-pandas/31617974
        mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
        sp_sch[sch_name].df['tmp2'][mask]=np.random.random(len(mask))*50+710
        #sp_sch[sch_name].df.loc[mask,'tmp2']=np.random.random(len(mask))*50+710
        sp_sch[sch_name].df['ec2']=sp_sch[sch_name].df['tmp2']
#
        time_start=np.datetime64('2018-08-29T13:00')
        time_end=np.datetime64('2018-09-14T17:00')

        
        ## the new method has already considered the boundary effect
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['tmp0']   ,plot=plot_interpolate  ,coef=5e-10)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['tmp1']   ,plot=plot_interpolate  ,coef=5e-10)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['tmp2']   ,plot=plot_interpolate  ,coef=5e-10)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['tmp3']   ,plot=plot_interpolate  ,coef=5e-10)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['tmp4']   ,plot=plot_interpolate  ,coef=5e-10)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['tmp5']   ,plot=plot_interpolate  ,coef=5e-10)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['tmp6']   ,plot=plot_interpolate  ,coef=5e-10)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['tmp7']   ,plot=plot_interpolate  ,coef=5e-10)  # done
        #sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['tmp8']   ,plot=plot_interpolate  ,coef=5e-10)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['tmp9']   ,plot=plot_interpolate  ,coef=5e-10)  # done


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

        #sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['mo0']   ,plot=plot_interpolate  ,coef=5e-7)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['mo0']   ,plot=plot_interpolate  ,coef=5e-7)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['mo1']   ,plot=plot_interpolate  ,coef=5e-10)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['mo2']   ,plot=plot_interpolate  ,coef=5e-10)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['mo3']   ,plot=plot_interpolate  ,coef=5e-10)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['mo4']   ,plot=plot_interpolate  ,coef=5e-10)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['mo5']   ,plot=plot_interpolate  ,coef=5e-10)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['mo6']   ,plot=plot_interpolate  ,coef=5e-10)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['mo7']   ,plot=plot_interpolate  ,coef=5e-10)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['mo8']   ,plot=plot_interpolate  ,coef=5e-10)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['mo9']   ,plot=plot_interpolate  ,coef=5e-10)  # done



        time_start=np.datetime64('2018-08-29T13:00')
        time_end=np.datetime64('2018-09-14T17:00')
        mask_output=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
        mask_input=data_mo_su.df['date_time'].between(time_start,time_end)
        #sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['mo0']   ,plot=plot_interpolate  ,coef=5e-7,mask=mask_input) 
        sp_sch[sch_name].merge_data2(df=data_mo_su.df, keys=['mo0']   ,plot=plot_interpolate  ,coef=1e-16, start_time=time_start,end_time=time_end)
        sp_sch[sch_name].merge_data2(df=data_mo_su.df, keys=['mo1']   ,plot=plot_interpolate  ,coef=1e-16, start_time=time_start,end_time=time_end)
        sp_sch[sch_name].merge_data2(df=data_mo_su.df, keys=['mo2']   ,plot=plot_interpolate  ,coef=1e-16, start_time=time_start,end_time=time_end)
        sp_sch[sch_name].merge_data2(df=data_mo_su.df, keys=['mo3']   ,plot=plot_interpolate  ,coef=1e-16, start_time=time_start,end_time=time_end)
        sp_sch[sch_name].merge_data2(df=data_mo_su.df, keys=['mo4']   ,plot=plot_interpolate  ,coef=1e-16, start_time=time_start,end_time=time_end)
        sp_sch[sch_name].merge_data2(df=data_mo_su.df, keys=['mo5']   ,plot=plot_interpolate  ,coef=1e-16, start_time=time_start,end_time=time_end)
        sp_sch[sch_name].merge_data2(df=data_mo_su.df, keys=['mo6']   ,plot=plot_interpolate  ,coef=1e-16, start_time=time_start,end_time=time_end)
        sp_sch[sch_name].merge_data2(df=data_mo_su.df, keys=['mo7']   ,plot=plot_interpolate  ,coef=1e-16, start_time=time_start,end_time=time_end)
        sp_sch[sch_name].merge_data2(df=data_mo_su.df, keys=['mo8']   ,plot=plot_interpolate  ,coef=1e-16, start_time=time_start,end_time=time_end)
        sp_sch[sch_name].merge_data2(df=data_mo_su.df, keys=['mo9']   ,plot=plot_interpolate  ,coef=1e-16, start_time=time_start,end_time=time_end)
        #sp_sch[sch_name].merge_data2(df=data.df, keys=['ec0']   ,plot=plot_interpolate  ,coef=1e-16, start_time=time_start,end_time=time_end)
        #sp_sch[sch_name].merge_data2(df=data.df, keys=['ec2']   ,plot=plot_interpolate  ,coef=1e-16, start_time=time_start,end_time=time_end)


        coef=-3.1
        sp_sch[sch_name].df['mmo0']=(570.0**coef-sp_sch[sch_name].df['mo0']**coef)/(550.**coef-260**coef)*schedule['porosity']
        sp_sch[sch_name].df['mmo1']=(570.0**coef-sp_sch[sch_name].df['mo1']**coef)/(550.**coef-270**coef)*schedule['porosity']
        sp_sch[sch_name].df['mmo2']=(570.0**coef-sp_sch[sch_name].df['mo2']**coef)/(550.**coef-270**coef)*schedule['porosity']
        sp_sch[sch_name].df['mmo3']=(570.0**coef-sp_sch[sch_name].df['mo3']**coef)/(550.**coef-280**coef)*schedule['porosity']
        sp_sch[sch_name].df['mmo4']=(570.0**coef-sp_sch[sch_name].df['mo4']**coef)/(550.**coef-270**coef)*schedule['porosity']
        #sp_sch[sch_name].df['mmo4']=(570.0**coef-sp_sch[sch_name].df['mo4']**coef)/(550.**coef-285**coef)*schedule['porosity']
        sp_sch[sch_name].df['mmo5']=(570.0**coef-sp_sch[sch_name].df['mo5']**coef)/(550.**coef-270**coef)*schedule['porosity']
        #sp_sch[sch_name].df['mmo5']=(570.0**coef-sp_sch[sch_name].df['mo5']**coef)/(550.**coef-285**coef)*schedule['porosity']
        sp_sch[sch_name].df['mmo6']=(570.0**coef-sp_sch[sch_name].df['mo6']**coef)/(550.**coef-280**coef)*schedule['porosity']
        sp_sch[sch_name].df['mmo7']=(570.0**coef-sp_sch[sch_name].df['mo7']**coef)/(550.**coef-275**coef)*schedule['porosity']
        sp_sch[sch_name].df['mmo8']=(570.0**coef-sp_sch[sch_name].df['mo8']**coef)/(550.**coef-285**coef)*schedule['porosity']
        sp_sch[sch_name].df['mmo9']=(570.0**coef-sp_sch[sch_name].df['mo9']**coef)/(550.**coef-285**coef)*schedule['porosity']

        
        # this was in 20180522
        #sp_sch[sch_name].merge_data(df=data_weather_daisy.df, keys=['rainmm']   ,plot=plot_interpolate  ,coef=5e-08)  # done
        
        # below was working in 20181023
        sp_sch[sch_name].merge_data(df=data_weather_camellia.df, keys=['dlyrainmm']   ,plot=plot_interpolate  ,coef=5e-08)  # done
        sp_sch[sch_name].df['rainmm']= sp_sch[sch_name].df['dlyrainmm']
        time_start=np.datetime64('2018-04-20T10:00')
        time_end=np.datetime64('2018-04-20T23:00')
        mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
        sp_sch[sch_name].df.loc[mask,'rainmm']=np.linspace(0.93,15,np.sum(mask) )
        sp_sch[sch_name].df['rainmm'].loc[sp_sch[sch_name].df['rainmm']<0]=0
 
        # this is done because the sensors are made upside down later, also, some of the weather stations needs to make updates

        sp_sch[sch_name].merge_data(df=data_weather_daisy.df, keys=['ir_up']   ,plot=plot_interpolate  ,coef=5e-4,new_keys=['ir_up_daisy'])
        sp_sch[sch_name].merge_data(df=data_weather_daisy.df, keys=['ir_down']   ,plot=plot_interpolate  ,coef=5e-4,new_keys=['ir_down_daisy'])
        sp_sch[sch_name].merge_data(df=data_weather_camellia.df, keys=['ir_down']   ,plot=plot_interpolate  ,coef=5e-4,new_keys=['ir_up_camellia'])

        
        sp_sch[sch_name].df['ir_up_daisy'].loc[sp_sch[sch_name].df['ir_up_daisy']>19512]=np.nan
        sp_sch[sch_name].df['ir_up_daisy'].loc[sp_sch[sch_name].df['ir_up_daisy']<252]=252   # if it is given as np.nan, there will be breaking points
        sp_sch[sch_name].df['ir_up_camellia'].loc[sp_sch[sch_name].df['ir_up_camellia']<252]=252
        sp_sch[sch_name].df['ir_up_camellia'].loc[sp_sch[sch_name].df['ir_up_camellia']>19512]=np.nan
        # the correction here is to ensure camellia shows same value as daisy
        sp_sch[sch_name].df['ir_up_camellia_cor'] = (sp_sch[sch_name].df['ir_up_camellia']-252) *1.17+252
        # the script below uses early results from daisy while later results from camellia. 
        time_start=np.datetime64('2018-06-29T13:00')
        time_end=np.datetime64('2018-10-21T17:00')
        mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
        sp_sch[sch_name].df['ir_up_concat']=sp_sch[sch_name].df['ir_up_daisy']
        sp_sch[sch_name].df.loc[mask,'ir_up_concat']=      sp_sch[sch_name].df.loc[mask,'ir_up_camellia_cor']

        #plt.figure()
        #plt.plot(sp_sch[sch_name].df['date_time'],sp_sch[sch_name].df['ir_up_concat'])


        #mmo0 starts to be exposed from 13 May
        time_start=np.datetime64('2018-05-13T13:00')
        mask=sp_sch[sch_name].df['date_time'].between(time_start,sp_sch[sch_name].end_dt)
        sp_sch[sch_name].df.loc[mask,'mmo0']=np.nan
        sp_sch[sch_name].df.loc[mask,'tmp0']=np.nan

        #mmo1 starts to be exposed from 14 OCT
        time_start=np.datetime64('2018-10-14T13:00')
        mask=sp_sch[sch_name].df['date_time'].between(time_start,sp_sch[sch_name].end_dt)
        sp_sch[sch_name].df.loc[mask,'mmo1']=np.nan
        sp_sch[sch_name].df.loc[mask,'tmp1']=np.nan
        
        # this part was cancelled as the power is disabled. 
        time_start=np.datetime64('2018-08-29T13:00')
        time_end=np.datetime64('2018-09-14T17:00')
        mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
        sp_sch[sch_name].df.loc[mask,'tmp0']=np.nan
        sp_sch[sch_name].df.loc[mask,'tmp1']=np.nan
        sp_sch[sch_name].df.loc[mask,'tmp2']=np.nan
        sp_sch[sch_name].df.loc[mask,'tmp3']=np.nan
        sp_sch[sch_name].df.loc[mask,'tmp4']=np.nan
        sp_sch[sch_name].df.loc[mask,'tmp6']=np.nan
        sp_sch[sch_name].df.loc[mask,'tmp7']=np.nan
        sp_sch[sch_name].df.loc[mask,'tmp9']=np.nan

        #time_start=np.datetime64('2018-02-23T15:00')
        #time_end=np.datetime64('2018-03-02T15:00')
        #mask=data_weather_camellia.df['date_time'].between(time_start,time_end)
        #data_weather_camellia.df['rh_box_7'].loc[mask]=np.nan

        time_start=np.datetime64('2018-08-29T13:00')
        time_end=np.datetime64('2018-10-23T17:00')
        mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
        sp_sch[sch_name].df.loc[mask,'pre1']=np.nan

        # 100
        time_start=np.datetime64('2018-07-16T13:00')
        time_end=np.datetime64('2018-10-23T17:00')
        mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
        sp_sch[sch_name].df.loc[mask,'pre0']=np.nan

        sp_sch[sch_name].merge_data(df=data_weather_camellia.df, keys=['rh']   ,plot=plot_interpolate  ,coef=5e-08)  # done
        sp_sch[sch_name].df['rh']*=0.01
        
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
        sp_sch[sch_name].merge_data(df=data_weather_camellia.df, keys=['wdspdkphavg2m']   ,plot=plot_interpolate  ,coef=5e-08)  # done
        time_start=np.datetime64('2018-02-24T00:00')
        #sp_sch[sch_name].df['wdspdkphavg2m'].loc[mask]=np.nan
        sp_sch[sch_name].df['wdspdkphavg2m'].loc[ sp_sch[sch_name].df['wdspdkphavg2m']>12  ]=np.nan
        sp_sch[sch_name].df['wdspdkphavg2m'].loc[ sp_sch[sch_name].df['wdspdkphavg2m']<0  ]=np.nan

        sp_sch[sch_name].merge_data(df=data_weather_camellia.df, keys=['wdgstkph10m']   ,plot=plot_interpolate  ,coef=5e-08)  # done
        sp_sch[sch_name].df['wdgstkph10m'].loc[ sp_sch[sch_name].df['wdgstkph10m']<0.  ]=np.nan

        #sp_sch[sch_name].merge_data(df=data_weather_daisy.df, keys=['wdspdkphavg2m']   ,plot=plot_interpolate  ,coef=5e-08)


        #plt.figure()
        #plt.plot(data_weather_daisy.df.index,data_weather_daisy.df['wdspdkphavg2m'] )

        #plt.figure()
        #plt.plot(data_weather_camellia.df.index,data_weather_camellia.df['wdspdkphavg2m'] )


        #plt.figure()
        #plt.plot(data_weather_camellia.df.index,data_weather_camellia.df['wdgstkph10m'] )
        sp_sch[sch_name].df['rh'].loc[ sp_sch[sch_name].df['rh']>100  ]=np.nan
        sp_sch[sch_name].df['rh'].loc[ sp_sch[sch_name].df['rh']<0  ]=np.nan




        time_start=np.datetime64('2018-02-03T15:00')
        time_end=np.datetime64('2018-02-05T15:00')
        mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
        sp_sch[sch_name].df['rh'].loc[mask]=np.nan

        time_start=np.datetime64('2018-03-02T15:00')
        time_end=np.datetime64('2018-03-10T15:00')
        mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
        sp_sch[sch_name].df['tmp7'].loc[mask]=np.nan
        sp_sch[sch_name].df['tmp6'].loc[mask]=np.nan
        sp_sch[sch_name].df['tmp9'].loc[mask]=np.nan


        sp_sch[sch_name].merge_data(df=data_weather_camellia.df, keys=['tc']  ,plot=plot_interpolate  ,coef=5e-08)  # done
        #sp_sch[sch_name].merge_data(df=data_weather_daisy.df, keys=['tp_box_7'],plot=plot_interpolate  ,coef=5e-12)  # done
        sp_sch[sch_name].df['tc'].loc[ sp_sch[sch_name].df['tc']<7  ]=np.nan
        #sp_sch[sch_name].df['tp_box_7'].loc[ sp_sch[sch_name].df['tp_box_7']<15 ]=np.nan

        #sp_sch[sch_name].merge_data(df=data_weather_camellia.df, keys=['tc']  ,plot=plot_interpolate  ,coef=5e-08)  # done


        #sp_sch[sch_name].merge_data(df=data_weather_daisy.df, keys=['p']   ,plot=plot_interpolate  ,coef=5e-08)  # done
        sp_sch[sch_name].merge_data(df=data_weather_camellia.df, keys=['p']   ,plot=plot_interpolate  ,coef=5e-08)  # done
        sp_sch[sch_name].df['p'].iloc[sp_sch[sch_name].df['p'].values<100000]=np.nan
        sp_sch[sch_name].df['p'].iloc[sp_sch[sch_name].df['p'].values>150000]=np.nan


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
        
        
# read from manual.xlsx
#https://stackoverflow.com/questions/16888888/how-to-read-a-xlsx-file-using-the-pandas-library-in-ipython

xl_file = pd.ExcelFile( schedule['manual_excel'])
daily_data_manual = xl_file.parse(index_col='date_time') 

df_mean = sp_sch['stanwell'].df.resample('D').mean()
df_max = sp_sch['stanwell'].df.resample('D').max()
df_last = sp_sch['stanwell'].df.resample('D').last()
# the original time for mean value is at 12am, we shift it to 12pm
#df_mean['date_time']=df_mean['date_time']+pd.to_timedelta(12, unit='h')
#df_mean['date_time']=df_mean.index

df_mean.index=df_mean.index+pd.to_timedelta(12, unit='h')
df_mean['date_time']=df_mean.index
depth_y=np.array([1,5,8,13,20,28,38,48,70,85])
responsible_depth_cm=np.concatenate( (np.diff(depth_y),np.array([36])) )

df_mean['total_moisture']=df_mean['mmo0'].fillna(0)*responsible_depth_cm[0] \
    +df_mean['mmo1'].fillna(0)*responsible_depth_cm[1] \
    +df_mean['mmo2'].fillna(0)*responsible_depth_cm[2] \
    +df_mean['mmo3'].fillna(0)*responsible_depth_cm[3] \
    +df_mean['mmo4'].fillna(0)*responsible_depth_cm[4] \
    +df_mean['mmo5'].fillna(0)*responsible_depth_cm[5] \
    +df_mean['mmo6'].fillna(0)*responsible_depth_cm[6] \
    +df_mean['mmo7'].fillna(0)*responsible_depth_cm[7] \
    +df_mean['mmo8'].fillna(0)*responsible_depth_cm[8] \
    +df_mean['mmo9'].fillna(0)*responsible_depth_cm[9]

df_mean['evap_rate']=np.concatenate( (np.diff(df_mean['total_moisture']),np.array([np.nan])))

df_mean['total_moisture_07']=df_mean['mmo0'].fillna(0)*responsible_depth_cm[0] \
    +df_mean['mmo1'].fillna(0)*responsible_depth_cm[1] \
    +df_mean['mmo2'].fillna(0)*responsible_depth_cm[2] \
    +df_mean['mmo3'].fillna(0)*responsible_depth_cm[3] \
    +df_mean['mmo4'].fillna(0)*responsible_depth_cm[4] \
    +df_mean['mmo5'].fillna(0)*responsible_depth_cm[5] \
    +df_mean['mmo6'].fillna(0)*responsible_depth_cm[6] \
    +df_mean['mmo7'].fillna(0)*responsible_depth_cm[7]

plt.figure()
plt.plot(df_mean.index,df_mean['total_moisture'])
plt.plot(df_mean.index,df_mean['total_moisture_07'])





bb=df_mean.index-df_mean.index[0]

cc= bb.total_seconds()

interp_method=wf.SmoothSpline(cc,df_mean['total_moisture'],p=1e-14)
dd=interp_method(cc)
df_mean['evap_rate_dd']=np.concatenate( (np.diff(dd),np.array([np.nan])))

interp_method=wf.SmoothSpline(cc,df_mean['total_moisture'],p=5e-15)
ee=interp_method(cc)
df_mean['evap_rate_ee']=np.concatenate( (np.diff(ee),np.array([np.nan])))

plt.figure()
plt.plot(df_mean.index,dd)
plt.plot(df_mean.index,ee)
plt.plot(df_mean.index,df_mean['total_moisture'])

plt.plot(df_mean.index,df_mean['total_moisture_07'])

#plt.subplot()
#plt.plot(df_mean.index,-df_mean['evap_rate_dd']*10)
#plt.plot(df_mean.index,-df_mean['evap_rate_ee']*10)
#plt.grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
#
#
#plt.plot(df_mean.index,dd)
#plt.figure()
#plt.plot(df_mean.index,df_mean['total_moisture_07'])

# below is to calculate penman monteith potential evaporation
# tc0_k removes all na to 25 degree as this way will fill many gaps
sp_sch[sch_name].df['tc0_k']=sp_sch[sch_name].df['tc'].fillna(25.0) +constants.kelvin
sp_sch[sch_name].df['wdspdkphavg2m_0']=sp_sch[sch_name].df['wdspdkphavg2m'].fillna(1.0)

sp_sch[sch_name].df['drhowv_sat_dt']=constants.dsvp_dtk( sp_sch[sch_name].df['tc0_k'] )
sp_sch[sch_name].df['latent_heat_JPkg']=constants.lhv(sp_sch[sch_name].df['tc0_k'])
sp_sch[sch_name].df['sat_vapor_pressure_soil_pa'] = constants.svp(sp_sch[sch_name].df['tmp1']+constants.kelvin)
sp_sch[sch_name].df['vapor_pressure_air_pa'] = constants.svp(sp_sch[sch_name].df['tc0_k'])*sp_sch[sch_name].df['rh']
sp_sch[sch_name].df['Rn_wPm2']=    (sp_sch[sch_name].df['ir_up_concat']-252.)/20.512
sp_sch[sch_name].df['ra_sPm']=np.log(2/0.0001) **2.0 /0.41**2.0/sp_sch[sch_name].df['wdspdkphavg2m_0'] 
sp_sch[sch_name].df['pet_pm_denom'] = sp_sch[sch_name].df['drhowv_sat_dt'] + constants.psych* ( 1.+ 1./sp_sch[sch_name].df['ra_sPm'] )
sp_sch[sch_name].df['pet_pm_part1']= ( sp_sch[sch_name].df['drhowv_sat_dt'] * sp_sch[sch_name].df['Rn_wPm2']  ) \
        / sp_sch[sch_name].df['pet_pm_denom']
sp_sch[sch_name].df['pet_pm_part2']=constants.air_density_kgPm3*constants.heat_capacity_air_JPkgPK*  \
        ( sp_sch[sch_name].df['sat_vapor_pressure_soil_pa'] -  sp_sch[sch_name].df['vapor_pressure_air_pa']   ) \
        /sp_sch[sch_name].df['ra_sPm'] / sp_sch[sch_name].df['pet_pm_denom']

sp_sch[sch_name].df['pet_part1_mmPday']=sp_sch[sch_name].df['pet_pm_part1'] / \
        constants.lhv(273.15)/ constants.rhow_pure_water * constants.msPmmday
sp_sch[sch_name].df['pet_part2_mmPday']=sp_sch[sch_name].df['pet_pm_part2'] / \
        constants.lhv(273.15)/ constants.rhow_pure_water * constants.msPmmday

sp_sch[sch_name].df['pet_mmPday']=sp_sch[sch_name].df['pet_part1_mmPday'] + sp_sch[sch_name].df['pet_part2_mmPday'].fillna(0) 
#plt.figure()
#plt.plot(sp_sch[sch_name].df.index,sp_sch[sch_name].df['pet_pm'])

fig, ax = plt.subplots(10,sharex=True,figsize=(9,12))
ax[0].plot(ta['date_time'], (ta['radiation'])*0.007+0.2*ta['wdspdkphavg2m_0'].fillna(0), '-',color='maroon',\
        markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Dielectric suction A')

ax[1].plot(sp_sch[sch_name].df.index,sp_sch[sch_name].df['pet_mmPday'])

ax[2].plot(sp_sch[sch_name].df.index,sp_sch[sch_name].df['pet_part2_mmPday']  )
ax[3].plot(sp_sch[sch_name].df.index,sp_sch[sch_name].df['pet_part1_mmPday']  )
ax[4].plot(sp_sch[sch_name].df.index,sp_sch[sch_name].df['Rn_wPm2'])
ax[5].plot(sp_sch[sch_name].df.index,sp_sch[sch_name].df['wdspdkphavg2m_0']     )
ax[6].plot(sp_sch[sch_name].df.index,sp_sch[sch_name].df['sat_vapor_pressure_soil_pa']     )
ax[7].plot(sp_sch[sch_name].df.index,sp_sch[sch_name].df['vapor_pressure_air_pa']  )
#ax[8].plot(sp_sch[sch_name].df.index,sp_sch[sch_name].df['tc']     )
#ax[9].plot(sp_sch[sch_name].df.index,sp_sch[sch_name].df['rh']  )

#ax[2].plot(sp_sch[sch_name].df.index,sp_sch[sch_name].df['pet_pm_part1'])
#ax[3].plot(sp_sch[sch_name].df.index,sp_sch[sch_name].df['pet_pm_part2'])

ax[0].set_ylabel('evp_fitting', fontsize=y_fontsize, labelpad=15)
ax[1].set_ylabel('pet_pm', fontsize=y_fontsize, labelpad=15)
ax[2].set_ylabel('part2\nmm/day', fontsize=y_fontsize, labelpad=15)
ax[3].set_ylabel('part1\nmm/day', fontsize=y_fontsize, labelpad=15)
#ax[2].set_ylabel('pet_pm_part1', fontsize=y_fontsize, labelpad=5)
#ax[3].set_ylabel('pet_pm_part2', fontsize=y_fontsize, labelpad=17)
ax[4].set_ylabel('Rn_wPm2', fontsize=y_fontsize, labelpad=7)
ax[5].set_ylabel('windspeed', fontsize=y_fontsize, labelpad=15)
ax[6].set_ylabel('sat_vapor_p soil', fontsize=y_fontsize, labelpad=15)
ax[7].set_ylabel('vapor_p_air', fontsize=y_fontsize, labelpad=15)


