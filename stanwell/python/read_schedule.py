import operator
import sensorfun
py_compile.compile(os.environ['pyduino']+'/python/post_processing/sensorfun.py')
import sensorfun
reload(sensorfun)
py_compile.compile(os.environ['pyduino']+'/python/post_processing/figlib.py')
import json
import figlib
import wafo.interpolate as wf
import datetime
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
#schedule['porosity']=1-schedule['average_dry_density']/schedule['specific_gravity']

xl_file = pd.ExcelFile( schedule['manual_excel'])
daily_data_manual = xl_file.parse(index_col='date_time')



sp_sch={}
plot_interpolate=False
#plot_interpolate=True
coef_dict={}
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
        sp_sch[sch_name].merge_data(df=data.df, keys=['pre1']   ,plot=plot_interpolate  ,coef=5e-15)  # original coef=5e-15
        sp_sch[sch_name].merge_data(df=data.df, keys=['pre0']   ,plot=plot_interpolate  ,coef=5e-15)  # done
        sp_sch[sch_name].merge_data(df=data.df, keys=['tmp1']   ,plot=plot_interpolate  ,coef=5e-13, new_keys=['ir_up_newpower'] )  #UV data ir_up from 20/09/2019
        sp_sch[sch_name].merge_data(df=data.df, keys=['tmp7']   ,plot=plot_interpolate  ,coef=5e-13, new_keys=['ir_down_newpower'] )  #UV data ir_down from 20/09/2019
        #-------------surface settlement----------------- 
        sp_sch[sch_name].merge_data(df=data_settlement.df, keys=['settlement_mm']   ,plot=plot_interpolate  ,coef=5e-15)  # this is to merge datetime in data of surface settlement in accordant with the moisture porfiles
 
        initial_heightm=1.2 #initial height of material which is the same as the height of column on the roof of Building 50 in UQ
        actual_heightm=1.2-sp_sch[sch_name].df['settlement_mm']*constants.mm2m #actual height of material in column after settlement
        sp_sch[sch_name].df['newavg_dry_density']=schedule['average_dry_density']*(initial_heightm/actual_heightm)
        sp_sch[sch_name].df['porosity']=1-sp_sch[sch_name].df['newavg_dry_density']/schedule['specific_gravity']
        #-------------------------------------------------
        time_end_ec0=np.datetime64('2019-03-01T00:00')
        sp_sch[sch_name].df['ec0'].loc[time_end_ec0:]=np.nan
        sp_sch[sch_name].df['Pre0']=(sp_sch[sch_name].df['pre0'].values-1005.35)*10.
        sp_sch[sch_name].df['Pre1']=(sp_sch[sch_name].df['pre1'].values-1005.35)*10.

        time_start = np.datetime64('2018-02-27T08:00')
        time_end   = np.datetime64('2018-04-09T00:00')
        ##https://stackoverflow.com/questions/31617845/how-to-select-rows-in-a-dataframe-between-two-values-in-python-pandas/31617974
        mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
        sp_sch[sch_name].df['tmp2'][mask]=np.random.random(len(mask))*50+710
        #sp_sch[sch_name].df.loc[mask,'tmp2']=np.random.random(len(mask))*50+710
        sp_sch[sch_name].df['ec2']=sp_sch[sch_name].df['tmp2']

        coef_modified=0.85
        time_top_chopped=np.datetime64('2019-03-15T00:00')
        sp_sch[sch_name].df['ec2'].loc[time_top_chopped:]*=coef_modified
        sp_sch[sch_name].df['Pre1'].loc[time_top_chopped:]*=coef_modified


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
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['tmp9']   ,plot=plot_interpolate  ,coef=5e-10)  # done35

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
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['mo0']   ,plot=plot_interpolate  ,coef=5e-14)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['mo1']   ,plot=plot_interpolate  ,coef=5e-14)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['mo2']   ,plot=plot_interpolate  ,coef=5e-14)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['mo3']   ,plot=plot_interpolate  ,coef=5e-14)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['mo4']   ,plot=plot_interpolate  ,coef=5e-14)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['mo5']   ,plot=plot_interpolate  ,coef=5e-14)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['mo6']   ,plot=plot_interpolate  ,coef=5e-14)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['mo7']   ,plot=plot_interpolate  ,coef=5e-14)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['mo8']   ,plot=plot_interpolate  ,coef=5e-14)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['mo9']   ,plot=plot_interpolate  ,coef=5e-14)  # done


        time_start=np.datetime64('2018-08-29T13:00')
        time_end=np.datetime64('2018-09-14T17:00')
        mask_output=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
        mask_input=data_mo_su.df['date_time'].between(time_start,time_end)
        #sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['mo0']   ,plot=plot_interpolate  ,coef=5e-7,mask=mask_input) 
        sp_sch[sch_name].merge_data2(df=data_mo_su.df, keys=['mo0']   ,plot=plot_interpolate  ,coef=1e-16, start_time=time_start,end_time=time_end)
        sp_sch[sch_name].merge_data2(df=data_mo_su.df, keys=['mo1']   ,plot=plot_interpolate  ,coef=1e-16, start_time=time_start,end_time=time_end)
        sp_sch[sch_name].merge_data2(df=data_mo_su.df, keys=['mo2']   ,plot=plot_interpolate  ,coef=1e-16, start_time=time_start,end_time=time_end)
        sp_sch[sch_name].merge_data2(df=data_mo_su.df, keys=['mo4']   ,plot=plot_interpolate  ,coef=1e-16, start_time=time_start,end_time=time_end)
        sp_sch[sch_name].merge_data2(df=data_mo_su.df, keys=['mo5']   ,plot=plot_interpolate  ,coef=1e-16, start_time=time_start,end_time=time_end)
        sp_sch[sch_name].merge_data2(df=data_mo_su.df, keys=['mo6']   ,plot=plot_interpolate  ,coef=1e-16, start_time=time_start,end_time=time_end)
        sp_sch[sch_name].merge_data2(df=data_mo_su.df, keys=['mo7']   ,plot=plot_interpolate  ,coef=1e-16, start_time=time_start,end_time=time_end)
        sp_sch[sch_name].merge_data2(df=data_mo_su.df, keys=['mo8']   ,plot=plot_interpolate  ,coef=1e-16, start_time=time_start,end_time=time_end)
        sp_sch[sch_name].merge_data2(df=data_mo_su.df, keys=['mo9']   ,plot=plot_interpolate  ,coef=1e-16, start_time=time_start,end_time=time_end)
        #sp_sch[sch_name].merge_data2(df=data.df, keys=['ec0']   ,plot=plot_interpolate  ,coef=1e-16, start_time=time_start,end_time=time_end)
        #sp_sch[sch_name].merge_data2(df=data.df, keys=['ec2']   ,plot=plot_interpolate  ,coef=1e-16, start_time=time_start,end_time=time_end)
        sp_sch[sch_name].merge_data(df=data_weather_camellia.df, keys=['tc']  ,plot=plot_interpolate  ,coef=5e-08)  # done
        sp_sch[sch_name].merge_data(df=data_weather_fromUQ.df, keys=['Temp_Mean(deg)']  ,plot=plot_interpolate  ,coef=5e-08)
        time_start_weatherUQ=np.datetime64('2020-02-05T10:40')

        #sp_sch[sch_name].df['tc'].loc[ sp_sch[sch_name].df['tc']<7  ]=np.nan
        sp_sch[sch_name].df['tc'].loc[time_start_weatherUQ:]=0 #had lost data of weather station on the roof since that time, so I used data from UQ weather station since then. Making values be zero is to merge data from two sources by using addition 
        sp_sch[sch_name].df['Temp_Mean(deg)'].loc[:time_start_weatherUQ]=0
        #sp_sch[sch_name].merge_data(df=data_weather_daisy.df, keys=['tp_box_7'],plot=plot_interpolate  ,coef=5e-12)  # done
        #sp_sch[sch_name].df['tp_box_7'].loc[ sp_sch[sch_name].df['tp_box_7']<15 ]=np.nan
        #sp_sch[sch_name].df['temperature']=pd.concat([sp_sch[sch_name].df['tc'],sp_sch[sch_name].df['Temp_Mean(deg)']], axis=1)
        sp_sch[sch_name].df['temperature']=sp_sch[sch_name].df['tc'] + sp_sch[sch_name].df['Temp_Mean(deg)']
        sp_sch[sch_name].df['temperature'].loc[ sp_sch[sch_name].df['temperature']<7  ]=np.nan 
        # TO181205 soil sensor failed to work during 829 and 914, make evt zero. so air temperature was put in
        time_surface_switch1=np.datetime64('2018-10-14T03:40') #sp_sch[sch_name].df['tmp1'] is NaN after this time
        time_surface_switch2=np.datetime64('2019-03-14T23:40') #values of sp_sch[sch_name].df['tmp2'],['tmp3'],['tmp4'],['tmp5'] had been invalid after this time.
        sp_sch[sch_name].df['tmp_soil_surf'] =  sp_sch[sch_name].df['tmp1']
        sp_sch[sch_name].df['tmp_soil_surf'].loc[:time_surface_switch1] =  sp_sch[sch_name].df['tmp1'] 
        sp_sch[sch_name].df['tmp_soil_surf'].loc[time_surface_switch1:time_surface_switch2] =  sp_sch[sch_name].df['tmp2']
        sp_sch[sch_name].df['tmp_soil_surf'].loc[time_surface_switch2:] =  sp_sch[sch_name].df['tmp6']*1.2
        sp_sch[sch_name].df['tmp_soil_surf'].loc[mask_output]=  sp_sch[sch_name].df['tc'].loc[mask_output] 

        '''
        plt.figure()
        plt.plot(sp_sch[sch_name].df.index,sp_sch[sch_name].df['tmp_soil_surf'])
        '''



        time_start_newraspi0=np.datetime64('2018-11-13T00:40')
        time_end_newraspi0=np.datetime64('2019-03-30T00:40')
        mask=sp_sch[sch_name].df['date_time'].between(time_start_newraspi0,time_end_newraspi0)
        coef=-3.1 # been a while
        coef=-1.8 
        coef=-4.5 
        coef=-5.0 
        coef=-7.0 
        #coef=-2.1
        sp_sch[sch_name].df['mmo0']=(550.0**coef-sp_sch[sch_name].df['mo0']**coef)/(550.**coef-260**coef)*sp_sch[sch_name].df['porosity']#schedule['porosity']
        sp_sch[sch_name].df['mmo1']=(550.0**coef-sp_sch[sch_name].df['mo1']**coef)/(550.**coef-270**coef)*sp_sch[sch_name].df['porosity']#schedule['porosity']
        sp_sch[sch_name].df['mmo2']=(550.0**coef-sp_sch[sch_name].df['mo2']**coef)/(570.**coef-265**coef)*sp_sch[sch_name].df['porosity']#schedule['porosity']
        sp_sch[sch_name].df['mmo3']=(452.0**coef-sp_sch[sch_name].df['mo3']**coef)/(452.**coef-278**coef)*sp_sch[sch_name].df['porosity']#schedule['porosity']
        sp_sch[sch_name].df['mmo4']=(450.0**coef-sp_sch[sch_name].df['mo4']**coef)/(450.**coef-270**coef)*sp_sch[sch_name].df['porosity']#schedule['porosity']
        #sp_sch[sch_name].df['mmo4']=(570.0**coef-sp_sch[sch_name].df['mo4']**coef)/(550.**coef-285**coef)*schedule['porosity']
        sp_sch[sch_name].df['mmo5']=(550.0**coef-sp_sch[sch_name].df['mo5']**coef)/(550.**coef-265**coef)*sp_sch[sch_name].df['porosity']#schedule['porosity']
        #sp_sch[sch_name].df['mmo5']=(570.0**coef-sp_sch[sch_name].df['mo5']**coef)/(550.**coef-285**coef)*schedule['porosity']
        sp_sch[sch_name].df['mmo6']=(550.0**coef-sp_sch[sch_name].df['mo6']**coef)/(550.**coef-280**coef)*sp_sch[sch_name].df['porosity']#schedule['porosity']
        sp_sch[sch_name].df['mmo7']=(550.0**coef-sp_sch[sch_name].df['mo7']**coef)/(550.**coef-277**coef)*sp_sch[sch_name].df['porosity']#schedule['porosity']
        sp_sch[sch_name].df['mmo8']=(570.0**coef-sp_sch[sch_name].df['mo8']**coef)/(570.**coef-282**coef)*sp_sch[sch_name].df['porosity']#schedule['porosity']
        sp_sch[sch_name].df['mmo9']=(570.0**coef-sp_sch[sch_name].df['mo9']**coef)/(570.**coef-282**coef)*sp_sch[sch_name].df['porosity']#schedule['porosity']

        time_start_mmo2=np.datetime64('2018-10-31T14:00')
        mask_mmo2=sp_sch[sch_name].df['date_time'].between(time_start_mmo2,sp_sch[sch_name].end_dt)
        sp_sch[sch_name].df['mmo2'].loc[mask_mmo2]=np.nan

        #coef_modified=0.88
        sp_sch[sch_name].df['mmo4'].loc[time_top_chopped:]=sp_sch[sch_name].df['mmo4']*coef_modified
        sp_sch[sch_name].df['mmo5'].loc[time_top_chopped:]=sp_sch[sch_name].df['mmo5']*coef_modified
        sp_sch[sch_name].df['mmo6'].loc[time_top_chopped:]=sp_sch[sch_name].df['mmo6']*coef_modified
        sp_sch[sch_name].df['mmo7'].loc[time_top_chopped:]=sp_sch[sch_name].df['mmo7']*coef_modified
        sp_sch[sch_name].df['mmo8'].loc[time_top_chopped:]=sp_sch[sch_name].df['mmo8']*coef_modified
        sp_sch[sch_name].df['mmo9'].loc[time_top_chopped:]=sp_sch[sch_name].df['mmo9']*coef_modified

        sp_sch[sch_name].df['mmo5'].loc[sp_sch[sch_name].df['mmo5']>sp_sch[sch_name].df['porosity']]=np.nan
        sp_sch[sch_name].df['mmo6'].loc[sp_sch[sch_name].df['mmo6']>sp_sch[sch_name].df['porosity']]=sp_sch[sch_name].df['porosity']
        sp_sch[sch_name].df['mmo7'].loc[sp_sch[sch_name].df['mmo7']>sp_sch[sch_name].df['porosity']]=sp_sch[sch_name].df['porosity']

        time_start_mmo8=np.datetime64('2019-01-10T14:00')
        time_end_mmo8=np.datetime64('2019-03-25T14:00')
        mask=sp_sch[sch_name].df['date_time'].between(time_start_mmo8,time_end_mmo8)
        sp_sch[sch_name].df['mmo8'].loc[mask]=sp_sch[sch_name].df['mmo9']*0.95
        # this was in 20180522
        #sp_sch[sch_name].merge_data(df=data_weather_daisy.df, keys=['rainmm']   ,plot=plot_interpolate  ,coef=5e-08)  # done 
        # below was working in 20181023
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
 

        # this is done because the sensors are made upside down later, also, some of the weather stations needs to make updates

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

        #plt.figure()
        #plt.plot(sp_sch[sch_name].df['date_time'],sp_sch[sch_name].df['ir_up_concat'])


        
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

        #time_start=np.datetimetime_start_Pre1nan:time_end_Pre1nan#time_end=np.datetime64('2018-03-02T15:00')
        #mask=data_weather_camellia.df['date_time'].between(time_start,time_end)
        #data_weather_camellia.df['rh_box_7'].loc[mask]=np.nan


        #------------modify tmp3&tmp7----------------------
        time_start=np.datetime64('2018-12-22T01:00')
        time_end=np.datetime64('2019-03-04T06:30')
        mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
        sp_sch[sch_name].df['tmp4']=sp_sch[sch_name].df['tmp3']-0.72
        sp_sch[sch_name].df['tmp7']=sp_sch[sch_name].df['tmp6']-0.45

        time_start=np.datetime64('2018-08-29T13:00')
        time_end=np.datetime64('2018-10-23T17:00')
        mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
#        sp_sch[sch_name].df[].loc[mask,'pre1']=np.nan
        sp_sch[sch_name].df.loc[mask,'pre1']=np.nan
        time_start_Pre1nan=np.datetime64('2019-05-10T00:00')
        time_end_Pre1nan=np.datetime64('2019-10-15T00:00')
        sp_sch[sch_name].df['Pre1'].loc[time_start_Pre1nan:time_end_Pre1nan]=np.nan

        # 100
        time_start=np.datetime64('2018-07-16T13:00')
        time_end=np.datetime64('2018-10-23T17:00')
        mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
        sp_sch[sch_name].df.loc[mask,'pre0']=np.nan
        time_end_pre0=np.datetime64('2018-12-01T00:00')
        sp_sch[sch_name].df
        
        sp_sch[sch_name].merge_data(df=data_weather_camellia.df, keys=['rh']   ,plot=plot_interpolate  ,coef=5e-08)  # done
        sp_sch[sch_name].merge_data(df=data_weather_fromUQ.df, keys=['RH_Mean(%)']   ,plot=plot_interpolate  ,coef=5e-08)  # done
        sp_sch[sch_name].df['rh']*=0.01
        sp_sch[sch_name].df['RH_Mean(%)']*=0.01       
        time_start_weatherUQ=np.datetime64('2020-02-05T10:40')
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


#        sp_sch[sch_name].df['wdspdkphavg2m'].loc[ sp_sch[sch_name].df['wdspdkphavg2m']>12  ]=np.nan
#        sp_sch[sch_name].df['wdspdkphavg2m'].loc[ sp_sch[sch_name].df['wdspdkphavg2m']<0  ]=np.nan
        sp_sch[sch_name].df['wdspd2m'].loc[ sp_sch[sch_name].df['wdspd2m']>12  ]=np.nan
        sp_sch[sch_name].df['wdspd2m'].loc[ sp_sch[sch_name].df['wdspd2m']<0  ]=np.nan

        sp_sch[sch_name].merge_data(df=data_weather_camellia.df, keys=['wdgstkph10m']   ,plot=plot_interpolate  ,coef=5e-08)  # done
        sp_sch[sch_name].merge_data(df=data_weather_fromUQ.df,keys=['WindSpd_Max(km/h)']   ,plot=plot_interpolate  ,coef=5e-08)  # done)

        sp_sch[sch_name].df['wdgstkph10m'].loc[time_start_weatherUQ:]=0
        sp_sch[sch_name].df['WindSpd_Max(km/h)'].loc[:time_start_weatherUQ]=0
        sp_sch[sch_name].df['wdgst10m']= sp_sch[sch_name].df['wdgstkph10m'] + sp_sch[sch_name].df['WindSpd_Max(km/h)']
        sp_sch[sch_name].df['wdgst10m'].loc[ sp_sch[sch_name].df['wdgst10m']<0.  ]=np.nan 
        #sp_sch[sch_name].merge_data(df=data_weather_daisy.df, keys=['wdspdkphavg2m']   ,plot=plot_interpolate  ,coef=5e-08)


        #plt.figure()
        #plt.plot(data_weather_daisy.df.index,data_weather_daisy.df['wdspdkphavg2m'] )

        #plt.figure()
        #plt.plot(data_weather_camellia.df.index,data_weather_camellia.df['wdspdkphavg2m'] )


        #plt.figure()
        #plt.plot(data_weather_camellia.df.index,data_weather_camellia.df['wdgstkph10m'] )
#        sp_sch[sch_name].df['rh'].loc[ sp_sch[sch_name].df['rh']>100  ]=np.nan
#        sp_sch[sch_name].df['rh'].loc[ sp_sch[sch_name].df['rh']<0  ]=np.nan
        sp_sch[sch_name].df['RH'].loc[ sp_sch[sch_name].df['RH']>100  ]=np.nan
        sp_sch[sch_name].df['RH'].loc[ sp_sch[sch_name].df['RH']<0  ]=np.nan




        time_start=np.datetime64('2018-02-03T15:00')
        time_end=np.datetime64('2018-02-05T15:00')
        mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
#        sp_sch[sch_name].df['rh'].loc[mask]=np.nan
        sp_sch[sch_name].df['RH'].loc[mask]=np.nan

        time_start=np.datetime64('2018-03-02T15:00')
        time_end=np.datetime64('2018-03-10T15:00')
        mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
        sp_sch[sch_name].df['tmp7'].loc[mask]=np.nan
        sp_sch[sch_name].df['tmp6'].loc[mask]=np.nan
        sp_sch[sch_name].df['tmp9'].loc[mask]=np.nan



        #sp_sch[sch_name].merge_data(df=data_weather_camellia.df, keys=['tc']  ,plot=plot_interpolate  ,coef=5e-08)  # done


        #sp_sch[sch_name].merge_data(df=data_weather_daisy.df, keys=['p']   ,plot=plot_interpolate  ,coef=5e-08)  # done
        sp_sch[sch_name].merge_data(df=data_weather_camellia.df, keys=['p']   ,plot=plot_interpolate  ,coef=5e-08)  # done
        sp_sch[sch_name].merge_data(df=data_weather_fromUQ.df, keys=['MSLP_Mean(hPa)']   ,plot=plot_interpolate  ,coef=5e-08)  # done
        sp_sch[sch_name]
        sp_sch[sch_name].df['p'].loc[time_start_weatherUQ:]=0 #had lost data of weather station on the roof since that time, so I used data from UQ weather station since then.
        sp_sch[sch_name].df['MSLP_Mean(hPa)'].loc[:time_start_weatherUQ]=0
        sp_sch[sch_name].df['AP']=sp_sch[sch_name].df['p'] + sp_sch[sch_name].df['MSLP_Mean(hPa)']*100 #Because the unit of 'p' is Pa, the unit of 'MSLP_Mean(hPa)' is hPa
#        sp_sch[sch_name].df['p'].iloc[sp_sch[sch_name].df['p'].values<100000]=np.nan
#        sp_sch[sch_name].df['p'].iloc[sp_sch[sch_name].df['p'].values>150000]=np.nan
        sp_sch[sch_name].df['AP'].iloc[sp_sch[sch_name].df['AP'].values<100000]=np.nan
        sp_sch[sch_name].df['AP'].iloc[sp_sch[sch_name].df['AP'].values>150000]=np.nan


        time_start=np.datetime64('2018-04-20T00:00')
        time_end=np.datetime64('2018-04-25T15:00')
        mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
#        sp_sch[sch_name].df['p'].loc[mask]=np.nan
#        sp_sch[sch_name].df['tc'].loc[mask]=np.nan
#        sp_sch[sch_name].df['wdspdkphavg2m'].loc[mask]=np.nan
#        sp_sch[sch_name].df['wdgstkph10m'].loc[mask]=np.nan
#        sp_sch[sch_name].df['rh'].loc[mask]=np.nan
        sp_sch[sch_name].df['AP'].loc[mask]=np.nan
        sp_sch[sch_name].df['temperature'].loc[mask]=np.nan
        sp_sch[sch_name].df['wdspd2m'].loc[mask]=np.nan
        sp_sch[sch_name].df['wdgst10m'].loc[mask]=np.nan
        sp_sch[sch_name].df['RH'].loc[mask]=np.nan




        time_start=np.datetime64('2018-05-04T00:00')
        time_end=np.datetime64('2018-05-07T15:00')
        mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
#        sp_sch[sch_name].df['p'].loc[mask]=np.nan
#        sp_sch[sch_name].df['tc'].loc[mask]=np.nan
#        sp_sch[sch_name].df['wdspdkphavg2m'].loc[mask]=np.nan
#        sp_sch[sch_name].df['wdgstkph10m'].loc[mask]=np.nan
#        sp_sch[sch_name].df['rh'].loc[mask]=np.nan
        sp_sch[sch_name].df['AP'].loc[mask]=np.nan
        sp_sch[sch_name].df['temperature'].loc[mask]=np.nan
        sp_sch[sch_name].df['wdspd2m'].loc[mask]=np.nan
        sp_sch[sch_name].df['wdgst10m'].loc[mask]=np.nan
        sp_sch[sch_name].df['RH'].loc[mask]=np.nan




        time_start=np.datetime64('2018-05-29T00:00')
        time_end=np.datetime64('2018-05-31T15:00')
        mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
#        sp_sch[sch_name].df['p'].loc[mask]=np.nan
#        sp_sch[sch_name].df['tc'].loc[mask]=np.nan
#        sp_sch[sch_name].df['wdspdkphavg2m'].loc[mask]=np.nan
#        sp_sch[sch_name].df['wdgstkph10m'].loc[mask]=np.nan
#        sp_sch[sch_name].df['rh'].loc[mask]=np.nan
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
        
        time_start=np.datetime64('2019-10-03T14:00')
        time_end=np.datetime64('2019-10-09T14:00')
        mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
        sp_sch[sch_name].df['ir_up_concat'].loc[mask]=np.nan

        #----------------this part is to calculate the moisture of soil surface for larer evp calculation------------------------
        #mmo_surf is the surface moisture content, which is lateron used for surface resistance
        sp_sch[sch_name].df['mmo_surf']=sp_sch[sch_name].df['mmo0']

        #mmo0 starts to be exposed from 13 May
        time_start_mmo0=np.datetime64('2018-05-13T13:00')
        mask_mmo0=sp_sch[sch_name].df['date_time'].between(time_start_mmo0,sp_sch[sch_name].end_dt)
        sp_sch[sch_name].df.loc[mask_mmo0,'mmo0']=np.nan
        sp_sch[sch_name].df.loc[mask_mmo0,'tmp0']=np.nan

        #mmo1 starts to be exposed from 14 OCT
        time_start_mmo1=np.datetime64('2018-10-14T13:00')
        mask_mmo1=sp_sch[sch_name].df['date_time'].between(time_start_mmo1,sp_sch[sch_name].end_dt)
        sp_sch[sch_name].df.loc[mask_mmo1,'mmo1']=np.nan
        sp_sch[sch_name].df.loc[mask_mmo1,'tmp1']=np.nan
        
        time_start_mmo3=np.datetime64('2018-12-10T14:00') #This is the time when 'mmo3' was used as the moisture of soil surface to calculate the evaporation rate
        #mmo3 started to be exposed from 14/03/2019
        #mmo4 started to be exposed from 16/12/2019
        time_end_mmo3=np.datetime64('2019-03-14T22:40')
        #time_start_mmo4=np.datetime64('2019-09-01T00:00')#this is the time when soil surface settled to the top of mmo4
        time_start_mmo4=np.datetime64('2019-05-19T14:00')
        time_end_mmo4=np.datetime64('2019-12-11T14:00')
        sp_sch[sch_name].df.loc[time_end_mmo3:,'mmo3']=np.nan
        sp_sch[sch_name].df.loc[time_end_mmo4:,'mmo4']=np.nan
        sp_sch[sch_name].df['mmo4'].loc[sp_sch[sch_name].df['mmo4']>sp_sch[sch_name].df['porosity']]=np.nan  
 
        mask_surf_mmo1=sp_sch[sch_name].df['date_time'].between(time_start_mmo0,time_start_mmo1)
        sp_sch[sch_name].df['mmo_surf'].loc[mask_surf_mmo1]= sp_sch[sch_name].df['mmo1']

        #mask_surf_mmo2=sp_sch[sch_name].df['date_time'].between(time_start_mmo1,sp_sch[sch_name].end_dt)
        #sp_sch[sch_name].df['mmo_surf'].loc[mask_surf_mmo2]= sp_sch[sch_name].df['mmo2'].loc[mask_surf_mmo2]
        
        settlement_time_end_mmo1 = 0.074  #Unit is m
        settlement_time_end_mmo3 = 0.169 #Unit is m
        settlement_time_end_mmo4 =0.227 #Unit is m
        settlement_time_end = 0.305     #Unit is m 
        sp_sch[sch_name].df['settle_ratio_mmo3']=(settlement_time_end_mmo3 - sp_sch[sch_name].df['settlement_mm']*constants.mm2m)/(settlement_time_end_mmo3 - settlement_time_end_mmo1)
        sp_sch[sch_name].df['settle_ratio_mmo4']=(settlement_time_end_mmo4 - sp_sch[sch_name].df['settlement_mm']*constants.mm2m)/(settlement_time_end_mmo4 - settlement_time_end_mmo3)
        sp_sch[sch_name].df['settle_ratio_mmo5']=(settlement_time_end - sp_sch[sch_name].df['settlement_mm']*constants.mm2m)/(settlement_time_end - settlement_time_end_mmo4)

        #mask_surf_mmo3_trans=sp_sch[sch_name].df['date_time'].between(time_start_mmo1,time_start_mmo3) 
        mask_surf_mmo3=sp_sch[sch_name].df['date_time'].between(time_start_mmo1,time_end_mmo3)
        #mask_surf_mmo4_trans=sp_sch[sch_name].df['date_time'].between(time_end_mmo3,time_start_mmo4)
        mask_surf_mmo4=sp_sch[sch_name].df['date_time'].between(time_end_mmo3,time_end_mmo4)
        mask_surf_mmo5=sp_sch[sch_name].df['date_time'].between(time_end_mmo4,sp_sch[sch_name].end_dt)

        #coef_dict={}
        #beta=np.arange(0.0,1,0.01)
        sigma=np.arange(47,51,0.1)
        for coef_trans in sigma:
            
        #sp_sch[sch_name].df['mmo_surf'].loc[mask_surf_mmo3]= sp_sch[sch_name].df['mmo3']
            #sp_sch[sch_name].df['mmo_surf'].loc[mask_surf_mmo3]= sp_sch[sch_name].df['mmo3']*coef_trans
            #sp_sch[sch_name].df['mmo_surf'].loc[mask_surf_mmo3_trans]= sp_sch[sch_name].df['mmo3']*np.exp(-(settlement_time_end_mmo3 - sp_sch[sch_name].df['settlement_mm']*constants.mm2m)*coef_trans/0.20)
            sp_sch[sch_name].df['mmo_surf'].loc[mask_surf_mmo3]= sp_sch[sch_name].df['mmo3']#*np.exp(-(settlement_time_end_mmo3 - sp_sch[sch_name].df['settlement_mm']*constants.mm2m)*coef_trans)
        #sp_sch[sch_name].df['mmo_surf'].loc[mask_surf_mmo3]= sp_sch[sch_name].df['mmo3']*np.exp(-sp_sch[sch_name].df['settle_ratio_mmo3'])-0.21*sp_sch[sch_name].df['settle_ratio_mmo3'] #0.21 is rs1994_param 
        #sp_sch[sch_name].df['mmo_surf'].loc[mask_surf_mmo3]= sp_sch[sch_name].df['mmo3']*(1-sp_sch[sch_name].df['porosity']/(1+sp_sch[sch_name].df['porosity']))
        #mask_surf_mmo4_start=sp_sch[sch_name].df['date_time'].between(time_end_mmo3,time_start_mmo4)               
        #sp_sch[sch_name].df['mmo_surf'].loc[mask_surf_mmo4_start]= sp_sch[sch_name].df['mmo4']*0.7    
            #sp_sch[sch_name].df['mmo_surf'].loc[mask_surf_mmo4]= sp_sch[sch_name].df['mmo4']*coef_trans
            sp_sch[sch_name].df['mmo_surf'].loc[mask_surf_mmo4]= sp_sch[sch_name].df['mmo4']*np.exp(-(settlement_time_end_mmo4 - sp_sch[sch_name].df['settlement_mm']*constants.mm2m)*coef_trans)
            #sp_sch[sch_name].df['mmo_surf'].loc[mask_surf_mmo4]= sp_sch[sch_name].df['mmo4']
        #sp_sch[sch_name].df['mmo_surf'].loc[mask_surf_mmo4]= sp_sch[sch_name].df['mmo4']*np.exp(-sp_sch[sch_name].df['settle_ratio_mmo4'])-0.21*sp_sch[sch_name].df['settle_ratio_mmo4']
        #sp_sch[sch_name].df['mmo_surf'].loc[mask_surf_mmo4]= sp_sch[sch_name].df['mmo4']*((1-sp_sch[sch_name].df['porosity'])/(1+sp_sch[sch_name].df['porosity']))
            #sp_sch[sch_name].df['mmo_surf'].loc[mask_surf_mmo5]= sp_sch[sch_name].df['mmo5'].fillna(sp_sch[sch_name].df['mmo6'])*coef_trans
            sp_sch[sch_name].df['mmo_surf'].loc[mask_surf_mmo5]= sp_sch[sch_name].df['mmo5'].fillna(0)*np.exp(-(settlement_time_end - sp_sch[sch_name].df['settlement_mm']*constants.mm2m)*coef_trans)
        #sp_sch[sch_name].df['mmo_surf'].loc[mask_surf_mmo5]= sp_sch[sch_name].df['mmo5'].fillna(sp_sch[sch_name].df['mmo6'])*np.exp(-sp_sch[sch_name].df['settle_ratio_mmo5'])-0.21*sp_sch[sch_name].df['settle_ratio_mmo5']
        #sp_sch[sch_name].df['mmo_surf'].loc[mask_surf_mmo5]= sp_sch[sch_name].df['mmo5'].fillna(sp_sch[sch_name].df['mmo6'])*((1-sp_sch[sch_name].df['porosity'])/(1+sp_sch[sch_name].df['porosity']))




            #----- below is to calculate penman monteith potential evaporation-----
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
            sp_sch[sch_name].df['Rn_wPm2']=    (sp_sch[sch_name].df['ir_up_concat']-252.)/20.512
            sp_sch[sch_name].df['ra_sPm']=np.log(2/0.000001) **2.0 /0.41**2.0/sp_sch[sch_name].df['wdspdkphavg2m_0']
            #sp_sch[sch_name].df['rs_sPm']=constants.rs1994(sp_sch[sch_name].df['mmo_surf'],1.0)
            #rs1994_para=0.22;rs1994_param2=35.63 # good 
            rs1994_param=0.18;rs1994_param2=35.63 # good 
            rs1994_param=0.21;rs1994_param2=35.63 # good 
            #rs1994_param_1=0.5;rs1994_param2_1=35.63
            #rs1994_param_2=0.35;rs1994_param2_2=35.63
            
            
            
            #time_start=np.datetime64('2018-03-27 19:00')
            #time_switch=np.datetime64('2018-11-01 00:00')
            #time_end=np.datetime64('2019-03-04T06:30')
            #mask1=sp_sch[sch_name].df['date_time'].between(time_start,time_switch)
            #mask2=sp_sch[sch_name].df['date_time'].between(time_switch,time_end)
            
            
            sp_sch[sch_name].df['rs_sPm']=10.*np.exp(rs1994_param2*(rs1994_param- sp_sch[sch_name].df['mmo_surf']  ))
            #sp_sch[sch_name].df['rs_sPm'].loc[mask_surf_mmo4]=10.*np.exp(rs1994_param2*(rs1994_param+(250-sp_sch[sch_name].df['settlement_mm'])/250- sp_sch[sch_name].df['mmo_surf']  ))
            #sp_sch[sch_name].df['rs_sPm'].loc[mask_surf_mmo5]=10.*np.exp(rs1994_param2*(rs1994_param+(325-sp_sch[sch_name].df['settlement_mm'])/325- sp_sch[sch_name].df['mmo_surf']  ))
            
            
            #sp_sch[sch_name].df['rs_sPm'].loc[mask_surf_mmo3]=10.*np.exp(rs1994_param2_2*(rs1994_param_2- sp_sch[sch_name].df['mmo_surf']  ))
            #sp_sch[sch_name].df['rs_sPm'].loc[mask_surf_mmo4]=10.*np.exp(rs1994_param2_1*(rs1994_param_1- sp_sch[sch_name].df['mmo_surf']  ))
            #sp_sch[sch_name].df['rs_sPm'].loc[mask_surf_mmo5]=10.*np.exp(rs1994_param2_2*(rs1994_param_2- sp_sch[sch_name].df['mmo_surf']  ))
            
            
            
            
            
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
#-----------------below is to calculate water mass balance---------------
            df_mean = sp_sch['stanwell'].df.resample('D').mean()
            df_max = sp_sch['stanwell'].df.resample('D').max()
            df_last = sp_sch['stanwell'].df.resample('D').last()

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
            
            time_start_mmo3 = datetime.datetime(2018,10,14,12,00)
            time_end_mmo3 = datetime.datetime(2019,03,14,12,00)
            time_end_mmo4 = datetime.datetime(2019,12,12,12,00)
            time_end = datetime.datetime(2020,04,20,12,00)
            mask_mmo3=df_mean['date_time'].between(time_start_mmo3,time_end_mmo3)
            mask_mmo4=df_mean['date_time'].between(time_end_mmo3,time_end_mmo4)
            mask_mmo5=df_mean['date_time'].between(time_end_mmo4,time_end)
            settlement_time_end_mmo3 = 0.169 #Unit is mm
            cum_responsible_depth_above_mmo4 = 0.190 #Unit is mm
            settlement_time_end_mmo4 = 0.227 #Unit is mm
            cum_responsible_depth_above_mmo5 = 0.270 #Unit is mm
            settlement_time_end = 0.305 #Unit is mm
            cum_responsible_depth_above_mmo6 = 0.370 #Unit is mm
            
            df_mean['total_moisture_cm'].loc[mask_mmo3]=df_mean['mmo_surf'].fillna(0)*(settlement_time_end_mmo3-df_mean['settlement_mm']*constants.mm2m) * 100 \
                +df_mean['mmo3'].fillna(0)*(cum_responsible_depth_above_mmo4 - settlement_time_end_mmo3)*100 \
                +df_mean['mmo4'].fillna(0)*responsible_depth_cm[4] \
                +df_mean['mmo5'].fillna(0)*responsible_depth_cm[5] \
                +df_mean['mmo6'].fillna(0)*responsible_depth_cm[6] \
                +df_mean['mmo7'].fillna(0)*responsible_depth_cm[7] \
                +df_mean['mmo8'].fillna(0)*responsible_depth_cm[8] \
                +df_mean['mmo9'].fillna(0)*responsible_depth_cm[9]
            
            df_mean['total_moisture_cm'].loc[mask_mmo4]=df_mean['mmo_surf'].fillna(0)*(settlement_time_end_mmo4-df_mean['settlement_mm']*constants.mm2m)*100 \
                +df_mean['mmo4'].fillna(0)*(cum_responsible_depth_above_mmo5 - settlement_time_end_mmo4)/10 \
                +df_mean['mmo5'].fillna(0)*responsible_depth_cm[5] \
                +df_mean['mmo6'].fillna(0)*responsible_depth_cm[6] \
                +df_mean['mmo7'].fillna(0)*responsible_depth_cm[7] \
                +df_mean['mmo8'].fillna(0)*responsible_depth_cm[8] \
                +df_mean['mmo9'].fillna(0)*responsible_depth_cm[9]
            
            df_mean['total_moisture_cm'].loc[mask_mmo5]=df_mean['mmo_surf'].fillna(0)*(settlement_time_end - df_mean['settlement_mm']*constants.mm2m)*100 \
                +df_mean['mmo5'].fillna(0)*(cum_responsible_depth_above_mmo6 - settlement_time_end)*10 \
                +df_mean['mmo6'].fillna(0)*responsible_depth_cm[6] \
                +df_mean['mmo7'].fillna(0)*responsible_depth_cm[7] \
                +df_mean['mmo8'].fillna(0)*responsible_depth_cm[8] \
                +df_mean['mmo9'].fillna(0)*responsible_depth_cm[9]
            
            time_start_ponding1 = datetime.datetime(2019,03,28,12,00)
            time_end_ponding1 = datetime.datetime(2019,04,02,12,00)
            time_start_ponding2 = datetime.datetime(2020,01,18,12,00)
            time_end_ponding2 = datetime.datetime(2020,01,31,12,00)
            time_start_ponding3 = datetime.datetime(2020,02,06,12,00)
            time_end_ponding3 = datetime.datetime(2020,03,10,12,00)
            mask1=df_mean['date_time'].between(time_start_ponding1,time_end_ponding1)#the first time period when the column was obviously filled with ponding water above soil surface
            mask2=df_mean['date_time'].between(time_start_ponding2,time_end_ponding2)#the second time period when the column was obviously filled with ponding water above soil surface
            mask3=df_mean['date_time'].between(time_start_ponding3,time_end_ponding3)#the third time period when the column was obviously filled with ponding water above soil surface
            
            #df_mean['aet_mmPday'].loc[mask1]=0
            #df_mean['aet_mmPday'].loc[mask2]=0
            #df_mean['aet_mmPday'].loc[mask3]=0
            
            
            df_mean['total_water_out_m']=np.cumsum(df_mean['aet_mmPday'])*constants.mPmm
            df_last['total_water_in_m']=np.cumsum(df_last['rainmm'].fillna(0))*constants.mPmm
            #df_mean['net_water_pos_out_mPday']=(df_mean['aet_mmPday'].fillna(0)-list(df_last['rainmm'].fillna(0))) * constants.mPmm
            #df_mean['cumsum_net_water_pos_out_m']=np.cumsum(df_mean['net_water_pos_out_mPday'])
             
            #df_last['total_water_in_m'].loc[datetime.datetime(2019,03,18)]=df_last['total_water_in_m'].loc[datetime.datetime(2019,03,17)] + 0.4
            #df_last['total_water_in_m'].loc[datetime.datetime(2019,03,28)]=df_last['total_water_in_m'].loc[datetime.datetime(2019,03,27)] + 0.02
            #df_last['total_water_in_m'].loc[datetime.datetime(2020,01,18,12,00)]=df_last['total_water_in_m'].loc[datetime.datetime(2020,01,18)] + 0.07
            #df_last['total_water_in_m'].loc[datetime.datetime(2020,02,06,12,00)]=df_last['total_water_in_m'].loc[datetime.datetime(2020,02,05)] + 0.14
            
            
            
            df_mean['net_water_storage_mPday']=(list(df_last['rainmm'].fillna(0))-df_mean['aet_mmPday'].fillna(0)) * constants.mPmm
            df_mean['cumsum_net_water_storage_m']=np.cumsum(df_mean['net_water_storage_mPday'])

            df_mean['cumsum_net_water_storage_m'].loc[datetime.datetime(2019,03,18,12,00):]=df_mean['cumsum_net_water_storage_m'] + 0.35
            df_mean['cumsum_net_water_storage_m'].loc[datetime.datetime(2019,03,28,12,00):]=df_mean['cumsum_net_water_storage_m'] + 0.02
            df_mean['cumsum_net_water_storage_m'].loc[datetime.datetime(2020,01,18,12,00):]=df_mean['cumsum_net_water_storage_m'] + 0.07
            df_mean['cumsum_net_water_storage_m'].loc[datetime.datetime(2020,02,06,12,00):]=df_mean['cumsum_net_water_storage_m'] + 0.135


            waterMass_from_weather_station = df_mean['cumsum_net_water_storage_m']*1000+900 #Change unit from 'cm' to 'mm'
            waterMass_from_moisture_profile = df_mean['total_moisture_cm']*0.01*1000-20 #Change unit from 'cm' to 'mm'
            Mass_1 = list(waterMass_from_weather_station)[::10]
            Mass_2 = list(waterMass_from_moisture_profile)[::10]
            n=len(Mass_1)
            summation = 0
            for i in range(0,n):
                difference = Mass_1[i] - Mass_2[i]
                sqred_difference = difference**2
                summation += sqred_difference
            MSE = summation/n #mean square error 
            coef_dict[coef_trans]=MSE
                
        coef_trans_mois=coef_dict.keys()
        MSE_mass_balance=coef_dict.values()
        coef_optimal=[key for (key, value) in coef_dict.items() if value == min(MSE_mass_balance)] #to find the key in coef_dict that corresponds the minimum value of MSE
        for coef_trans in coef_optimal:
            pEt= df_mean['pet_mmPday']
            aEt= df_mean['aet_mmPday']
            watermass_from_weather_station = waterMass_from_weather_station
            watermass_from_moisture_profile = waterMass_from_moisture_profile
            df_mean['cumsum_rainmm']=np.cumsum(df_last['rainmm'])

            pEt.loc[df_mean['pet_mmPday']>11]=11
            aEt.loc[df_mean['aet_mmPday']>11]=11

#time_start=np.datetime64('2018-11-11 00:00')
#time_end=np.datetime64('2018-11-12 00:00')
#mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
#sp_sch[sch_name].df['pet_mmPday'][mask]=sp_sch[sch_name].df['pet_mmPday']*0.5
#sp_sch[sch_name].df['aet_mmPday'][mask]=sp_sch[sch_name].df['aet_mmPday']*0.5
#
#
#time_start1=np.datetime64('2018-12-23 00:00')
#time_end1=np.datetime64('2018-12-24 00:00')
#mask1=sp_sch[sch_name].df['date_time'].between(time_start1,time_end1)
#sp_sch[sch_name].df['pet_mmPday'][mask1]=sp_sch[sch_name].df['pet_mmPday']*0.6
#sp_sch[sch_name].df['aet_mmPday'][mask1]=sp_sch[sch_name].df['aet_mmPday']*0.6

        #df_mean = sp_sch['stanwell'].df.resample('D').mean()
        #df_max = sp_sch['stanwell'].df.resample('D').max()
        #df_last = sp_sch['stanwell'].df.resample('D').last()

        #df_mean['cumsum_rainmm']=np.cumsum(df_last['rainmm'])
        #df_mean['ir_up_concat'].loc[datetime.datetime(2019,10,04):datetime.datetime(2019,10,9)]=np.nan

        #df_mean['pet_mmPday'].loc[df_mean['pet_mmPday']>11]=11
        #df_mean['aet_mmPday'].loc[df_mean['aet_mmPday']>11]=11

