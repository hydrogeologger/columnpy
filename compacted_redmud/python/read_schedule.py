import operator
import sensorfun
py_compile.compile(os.environ['pyduino']+'/python/post_processing/sensorfun.py')
import sensorfun
reload(sensorfun)
py_compile.compile(os.environ['pyduino']+'/python/post_processing/figlib.py')
import figlib
reload(figlib)
lw=5
ms=8
mew=3
grid_width=2
y_fontsize=20


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

        sp_sch[sch_name].start_dt=pd.datetime.strptime(line_content[0],'%Y/%b/%d %H:%M')
        sp_sch[sch_name].end_dt=pd.datetime.strptime(line_content[1],'%Y/%b/%d %H:%M')

        sp_sch[sch_name].surface_area  =float(line_content[4])
        sp_sch[sch_name].por=float(line_content[6])
        sp_sch[sch_name].soil_thickness=float(line_content[5])
        sp_sch[sch_name].time_surface_emerge = pd.datetime.strptime(line_content[10],'%Y/%b/%d %H:%M')

        
        sp_sch[sch_name].merge_data(df=prof['compacted_redmud']['data'].df, keys=['scale']   ,plot=plot_interpolate  ,coef=5e-12)  # done
        sp_sch[sch_name].merge_data(df=prof['compacted_redmud']['data'].df, keys=['gs3_2_salt']   ,plot=plot_interpolate  ,coef=5e-12)  # salt
        sp_sch[sch_name].merge_data(df=prof['compacted_redmud']['data'].df, keys=['gs3_2_tp']   ,plot=plot_interpolate  ,coef=5e-12)  # salt
        sp_sch[sch_name].merge_data(df=prof['compacted_redmud']['data'].df, keys=['gs3_2_dp']   ,plot=plot_interpolate  ,coef=5e-12)  # salt
        sp_sch[sch_name].merge_data(df=prof['compacted_redmud']['data'].df, keys=['gs3_1_salt']   ,plot=plot_interpolate  ,coef=5e-12)  # salt
        sp_sch[sch_name].merge_data(df=prof['compacted_redmud']['data'].df, keys=['gs3_1_tp']   ,plot=plot_interpolate  ,coef=5e-12)  # salt
        sp_sch[sch_name].merge_data(df=prof['compacted_redmud']['data'].df, keys=['gs3_1_dp']   ,plot=plot_interpolate  ,coef=5e-12)  # salt
        sp_sch[sch_name].merge_data(df=prof['compacted_redmud']['data'].df, keys=['2896_begin_97']   ,plot=plot_interpolate  ,coef=5e-12)  # salt
        sp_sch[sch_name].merge_data(df=prof['compacted_redmud']['data'].df, keys=['2896_peak_117']   ,plot=plot_interpolate  ,coef=5e-12)  # salt
        sp_sch[sch_name].merge_data(df=prof['compacted_redmud']['data'].df, keys=['2896_deltat_heat']   ,plot=plot_interpolate  ,coef=5e-16)  # salt
        sp_sch[sch_name].merge_data(df=prof['compacted_redmud']['data'].df, keys=['2870_begin_51']   ,plot=plot_interpolate  ,coef=5e-12)  # salt
        sp_sch[sch_name].merge_data(df=prof['compacted_redmud']['data'].df, keys=['2870_peak_71']   ,plot=plot_interpolate  ,coef=5e-12)  # salt
        sp_sch[sch_name].merge_data(df=prof['compacted_redmud']['data'].df, keys=['2870_deltat_heat']   ,plot=plot_interpolate  ,coef=5e-16)  # salt
        sp_sch[sch_name].merge_data(df=prof['compacted_redmud']['data'].df, keys=['humi_1']   ,plot=plot_interpolate  ,coef=5e-14)  # salt
        sp_sch[sch_name].merge_data(df=prof['compacted_redmud']['data'].df, keys=['humi_2']   ,plot=plot_interpolate  ,coef=5e-14)  # salt
        sp_sch[sch_name].merge_data(df=prof['compacted_redmud']['data'].df, keys=['mo7']   ,plot=plot_interpolate  ,coef=5e-14)  # salt
        sp_sch[sch_name].merge_data(df=prof['compacted_redmud']['data'].df, keys=['mo8']   ,plot=plot_interpolate  ,coef=5e-14)  # salt
        sp_sch[sch_name].merge_data(df=prof['compacted_redmud']['data'].df, keys=['mo9']   ,plot=plot_interpolate  ,coef=5e-14)  # salt
        sp_sch[sch_name].merge_data(df=prof['compacted_redmud']['data'].df, keys=['mo10']   ,plot=plot_interpolate  ,coef=5e-14)  # salt
        sp_sch[sch_name].df['cum_evap']=(sp_sch[sch_name].df['scale'][0]-sp_sch[sch_name].df['scale']
                            )*constants.g2kg/sp_sch[sch_name].surface_area/constants.rhow_pure_water
        sp_sch[sch_name].df['evap_rate']=np.append(np.diff(sp_sch[sch_name].df['cum_evap'] ),np.nan)/dt_s


        min_index, min_value = min(enumerate( abs(sp_sch[sch_name].df['date_time']- sp_sch[sch_name].time_surface_emerge
            )), key=operator.itemgetter(1))
        sp_sch[sch_name].idx_surface_emerge = min_index

        # calculate saturaturation based on commercial balance
        total_water_depth=sp_sch[sch_name].por*sp_sch[sch_name].soil_thickness
        sp_sch[sch_name].df['sat']=(total_water_depth-(
            sp_sch[sch_name].df['cum_evap']-sp_sch[sch_name].df['cum_evap'][sp_sch[sch_name].idx_surface_emerge])
            )/total_water_depth
        sp_sch[sch_name].df['sat'][sp_sch[sch_name].df['sat']>1]=1



        alpha=-5.
        wet1=500.0
        sp_sch[sch_name].df['mmo9']=(wet1**alpha-sp_sch[sch_name].df['mo9']**alpha)/ (wet1**alpha-270**alpha)   # 1 cm
        sp_sch[sch_name].df['mmo10']=(wet1**alpha-sp_sch[sch_name].df['mo10']**alpha)/(wet1**alpha-280**alpha)   # 5 cm



#            time_start=np.datetime64('2018-04-20T10:00')
#            time_end=np.datetime64('2018-04-20T23:00')
#            mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
#            sp_sch[sch_name].df.loc[mask,'rainmm']=np.linspace(0.93,15,np.sum(mask) )
#
#
#        
#        
#        time_start=np.datetime64('2018-03-02T13:00')
#        time_end=np.datetime64('2018-03-03T17:00')
#        mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
#        sp_sch[sch_name].df.loc[mask,'tmp0']=np.nan
#        sp_sch[sch_name].df.loc[mask,'tmp1']=np.nan
#        sp_sch[sch_name].df.loc[mask,'tmp2']=np.nan
#        sp_sch[sch_name].df.loc[mask,'tmp3']=np.nan
#        sp_sch[sch_name].df.loc[mask,'tmp4']=np.nan
#        sp_sch[sch_name].df.loc[mask,'tmp5']=np.nan
#        sp_sch[sch_name].df.loc[mask,'tmp6']=np.nan
#        sp_sch[sch_name].df.loc[mask,'tmp7']=np.nan
#        sp_sch[sch_name].df.loc[mask,'tmp8']=np.nan
#        sp_sch[sch_name].df.loc[mask,'tmp9']=np.nan
#
#        time_start=np.datetime64('2018-07-10T13:00')
#        time_end=np.datetime64('2018-07-12T12:00')
#        mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
#        sp_sch[sch_name].df.loc[mask,'tmp0']=np.nan
#        sp_sch[sch_name].df.loc[mask,'tmp1']=np.nan
#        sp_sch[sch_name].df.loc[mask,'tmp2']=np.nan
#        sp_sch[sch_name].df.loc[mask,'tmp3']=np.nan
#        sp_sch[sch_name].df.loc[mask,'tmp4']=np.nan
#        sp_sch[sch_name].df.loc[mask,'tmp5']=np.nan
#        sp_sch[sch_name].df.loc[mask,'tmp6']=np.nan
#        sp_sch[sch_name].df.loc[mask,'tmp7']=np.nan
#        sp_sch[sch_name].df.loc[mask,'tmp8']=np.nan
#        sp_sch[sch_name].df.loc[mask,'tmp9']=np.nan
#
#        time_start=np.datetime64('2018-02-23T15:00')
#        time_end=np.datetime64('2018-03-02T15:00')
#        mask=data_weather_camellia.df['date_time'].between(time_start,time_end)
#        data_weather_camellia.df['rh_box_7'].loc[mask]=np.nan
#
#
#        sp_sch[sch_name].merge_data(df=data_weather_camellia.df, keys=['rh']   ,plot=plot_interpolate  ,coef=5e-08)  # done
#        sp_sch[sch_name].merge_data(df=data_weather_camellia.df, keys=['rh_box_7'],plot=plot_interpolate  ,coef=5e-12)  # done
#        time_start=np.datetime64('2018-01-27T15:00')
#        time_end=np.datetime64('2018-01-30T10:00')
#        #https://stackoverflow.com/questions/31617845/how-to-select-rows-in-a-dataframe-between-two-values-in-python-pandas/31617974
#        mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
#        sp_sch[sch_name].df['rh'].loc[mask]=np.nan
#
#        time_start=np.datetime64('2018-02-24T15:00')
#        time_end=np.datetime64('2018-03-01T15:00')
#        mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
#        sp_sch[sch_name].df['rh'].loc[mask]=np.nan
#
#
#        #sp_sch[sch_name].df['rh_box_7'][mask]=np.nan
#        sp_sch[sch_name].merge_data(df=data_weather_camellia.df, keys=['wdspdkphavg2m']   ,plot=plot_interpolate  ,coef=5e-08)  # done
#        time_start=np.datetime64('2018-02-24T00:00')
#        sp_sch[sch_name].df['wdspdkphavg2m'].loc[mask]=np.nan
#        sp_sch[sch_name].df['wdspdkphavg2m'].loc[ sp_sch[sch_name].df['wdspdkphavg2m']>12  ]=np.nan
#        sp_sch[sch_name].df['wdspdkphavg2m'].loc[ sp_sch[sch_name].df['wdspdkphavg2m']<0  ]=np.nan
#
#        sp_sch[sch_name].merge_data(df=data_weather_camellia.df, keys=['wdgstkph10m']   ,plot=plot_interpolate  ,coef=5e-08)  # done
#        #time_start=np.datetime64('2018-02-24T00:00')
#        #sp_sch[sch_name].df['wdgstkph10m'][mask]=np.nan
#        sp_sch[sch_name].df['wdgstkph10m'].loc[ sp_sch[sch_name].df['wdgstkph10m']<0.  ]=np.nan
#
#
#
#        time_start=np.datetime64('2018-02-03T15:00')
#        time_end=np.datetime64('2018-02-05T15:00')
#        mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
#        sp_sch[sch_name].df['rh'].loc[mask]=np.nan
#
#
#        sp_sch[sch_name].merge_data(df=data_weather_daisy.df, keys=['tc']  ,plot=plot_interpolate  ,coef=5e-08)  # done
#        sp_sch[sch_name].merge_data(df=data_weather_daisy.df, keys=['tp_box_7'],plot=plot_interpolate  ,coef=5e-12)  # done
#        sp_sch[sch_name].df['tc'].loc[ sp_sch[sch_name].df['tc']<9  ]=np.nan
#        sp_sch[sch_name].df['tp_box_7'].loc[ sp_sch[sch_name].df['tp_box_7']<15 ]=np.nan
#
#
#
#        sp_sch[sch_name].merge_data(df=data_weather_daisy.df, keys=['p']   ,plot=plot_interpolate  ,coef=5e-08)  # done
#        sp_sch[sch_name].df['p'].loc[sp_sch[sch_name].df['p'].values<88000]=np.nan
#        #sp_sch[sch_name].merge_data(df=data.df, keys=['dhthum0'],plot=plot_interpolate  ,coef=5e-12)  # done
#
#        #sp_sch[sch_name].merge_data(df=data_weather_daisy.df, keys=['rh']   ,plot=plot_interpolate  ,coef=5e-08)  # done
#
#
#
#        sp_sch[sch_name].merge_data(df=data.df, keys=['ec0']   ,plot=plot_interpolate  ,coef=5e-10)  # done
#        sp_sch[sch_name].merge_data(df=data.df, keys=['ec1']   ,plot=plot_interpolate  ,coef=5e-10)  # done
#        sp_sch[sch_name].merge_data(df=data.df, keys=['pre1']   ,plot=plot_interpolate  ,coef=5e-15)  # done
#        sp_sch[sch_name].merge_data(df=data.df, keys=['pre0']   ,plot=plot_interpolate  ,coef=5e-15)  # done
#        sp_sch[sch_name].df['pre0']=(sp_sch[sch_name].df['pre0'].values-1005.35)*10.
#        sp_sch[sch_name].df['pre1']=(sp_sch[sch_name].df['pre1'].values-1005.35)*10.
#
#        time_start=np.datetime64('2018-01-24T15:00')
#        time_end=np.datetime64('2018-02-03T15:00')
#        #https://stackoverflow.com/questions/31617845/how-to-select-rows-in-a-dataframe-between-two-values-in-python-pandas/31617974
#        mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
#        sp_sch[sch_name].df['pre0'].loc[mask]=np.nan
#        sp_sch[sch_name].df['pre1'].loc[mask]=np.nan
#
#
#
