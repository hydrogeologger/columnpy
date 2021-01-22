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
        sp_sch[sch_name]=pandas_scale.concat_data_roof(pd.datetime.strptime(line_content[0],'%Y/%b/%d %H:%M'),pd.datetime.strptime(line_content[1],'%Y/%b/%d %H:%M'),dt_s );

        sp_sch[sch_name].start_dt=pd.datetime.strptime(line_content[0],'%Y/%b/%d %H:%M')
        sp_sch[sch_name].end_dt=pd.datetime.strptime(line_content[1],'%Y/%b/%d %H:%M')
       #hum is temperature and tmp is humidity
        
        sp_sch[sch_name].surface_area=float(line_content[4])
        sp_sch[sch_name].por=float(line_content[6])
        sp_sch[sch_name].time_surface_emerge = pd.datetime.strptime(line_content[10],'%Y/%b/%d %H:%M')
        #sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['hum_dht22']   ,plot=plot_interpolate  ,coef=5e-10)  # done
       # sp_sch[sch_name].merge_data(df=data.df, keys=['hum4']   ,plot=plot_interpolate  ,coef=5e-10)  # done
       # sp_sch[sch_name].merge_data(df=data.df, keys=['hum5']   ,plot=plot_interpolate  ,coef=5e-10)  # done
       # sp_sch[sch_name].merge_data(df=data.df, keys=['hum6']   ,plot=plot_interpolate  ,coef=5e-10)  # done
       # sp_sch[sch_name].merge_data(df=data.df, keys=['scale1']   ,plot=plot_interpolate  ,coef=5e-10) # done
        #sp_sch[sch_name].merge_data(df=data.df, keys=['scale1']   ,plot=plot_interpolate  ,coef=5e-7) # done
        #sp_sch[sch_name].merge_data(df=data.df, keys=['scale1']   ,plot=plot_interpolate  ,coef=5e-12) # done
        #if sch_name=='basin_test':
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['scale1']   ,plot=plot_interpolate  ,coef=5e-15) # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['scale2']   ,plot=plot_interpolate  ,coef=5e-15)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['scale3']   ,plot=plot_interpolate  ,coef=5e-19)  # done
        #if sch_name=='basin_b':
        #    sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['scale1']   ,plot=plot_interpolate  ,coef=5e-15) # done
        #    sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['scale2']   ,plot=plot_interpolate  ,coef=5e-15)  # done
        #    sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['scale3']   ,plot=plot_interpolate  ,coef=5e-15)  # done
        #if sch_name=='basin_c':
        #    sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['scale1']   ,plot=plot_interpolate  ,coef=5e-10) # done
        #    sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['scale2']   ,plot=plot_interpolate  ,coef=5e-10)  # done
        #    sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['scale3']   ,plot=plot_interpolate  ,coef=5e-10)  # done

        #sp_sch[sch_name].merge_data(df=data.df, keys=['tmp3']   ,plot=plot_interpolate  ,coef=5e-10)  # done
        #sp_sch[sch_name].merge_data(df=data.df, keys=['tmp4']   ,plot=plot_interpolate  ,coef=5e-10)  # done
        #sp_sch[sch_name].merge_data(df=data.df, keys=['tmp5']   ,plot=plot_interpolate  ,coef=5e-10)  # done
        #sp_sch[sch_name].merge_data(df=data.df, keys=['tmp6']   ,plot=plot_interpolate  ,coef=5e-10)  # d
        #sp_sch[sch_name].df['pre0']=(sp_sch[sch_name].df['pre0'].values-1005.35)*10.
        #sp_sch[sch_name].df['pre1']=(sp_sch[sch_name].df['pre1'].values-1005.35)*10.

        #time_start = np.datetime64('2018-03-02T08:00')
        #time_end   = np.datetime64('2018-05-29T00:00')
        ##https://stackoverflow.com/questions/31617845/how-to-select-rows-in-a-dataframe-between-two-values-in-python-pandas/31617974
        #mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
        #sp_sch[sch_name].df['tmp2'][mask]=np.random.random(len(mask))*50+710
        #sp_sch[sch_name].df['ec2']=sp_sch[sch_name].df['tmp2']

        #sp_sch[sch_name].merge_data2(df=data_mo_su.df, keys=['mo0']   ,plot=plot_interpolate  ,coef=5e-7)  # done
        #sp_sch[sch_name].merge_data2(df=data_mo_su.df, keys=['mo0']   ,plot=plot_interpolate  ,coef=5e-16,
        #        start_time=np.datetime64('2018-02-21T00:00'),end_time=np.datetime64('2018-03-09T00:00'))
        #sp_sch[sch_name].merge_data2(df=data_mo_su.df, keys=['mo0']   ,plot=plot_interpolate  ,coef=5e-19,
        #        start_time=np.datetime64('2018-02-20T00:00'),end_time=np.datetime64('2018-03-06T00:00'))
        ## the new method has already considered the boundary effect
        #sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['tempa0']   ,plot=plot_interpolate  ,coef=5e-13)  # done
        #sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['tempa1']   ,plot=plot_interpolate  ,coef=5e-13)  # done
        #sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['tempa2']   ,plot=plot_interpolate  ,coef=5e-13)  # done
        #sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['tempa3']   ,plot=plot_interpolate  ,coef=5e-13)  # done
        #sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['tempa4']   ,plot=plot_interpolate  ,coef=5e-13)  # done
        #sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['tempa5']   ,plot=plot_interpolate  ,coef=5e-13)  # done
        #sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['tempb0']   ,plot=plot_interpolate  ,coef=5e-13)  # done
        #sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['tempb1']   ,plot=plot_interpolate  ,coef=5e-13)  # done
        #sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['tempb2']   ,plot=plot_interpolate  ,coef=5e-13)  # done
        #sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['tempb3']   ,plot=plot_interpolate  ,coef=5e-13)  # done
        #sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['tempb4']   ,plot=plot_interpolate  ,coef=5e-13)  # done
        #sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['tempb5']   ,plot=plot_interpolate  ,coef=5e-13)  # done
        #sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['tmp0']   ,plot=plot_interpolate  ,coef=5e-10)  # done
        #sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['tmp1']   ,plot=plot_interpolate  ,coef=5e-10)  # done
        #sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['tmp2']   ,plot=plot_interpolate  ,coef=5e-10)  # done 

        aa=-1.1 #coef tested best
        #aa=-0.91 #coef tested best
        bb=10 #coef tested best       
        
        #if sch_name=='basin_test':
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['sua1']   ,plot=plot_interpolate  ,coef=5e-15)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['sua2']   ,plot=plot_interpolate  ,coef=5e-15)  # done non ideal data
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['sua3']   ,plot=plot_interpolate  ,coef=5e-15)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['sub1']   ,plot=plot_interpolate  ,coef=5e-15)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['sub2']   ,plot=plot_interpolate  ,coef=5e-15)  # done null
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['sub3']   ,plot=plot_interpolate  ,coef=5e-15)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['suc1']   ,plot=plot_interpolate  ,coef=5e-15)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['suc2']   ,plot=plot_interpolate  ,coef=5e-15)  # done null
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['suc3']   ,plot=plot_interpolate  ,coef=5e-15)  # done

            #sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['su3']   ,plot=plot_interpolate  ,coef=5e-13)  # done
            #sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['su4']   ,plot=plot_interpolate  ,coef=5e-13)  # done
            #sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['su5']   ,plot=plot_interpolate  ,coef=5e-13)  # done
        
        
        delta_t_sua1_low_2_high=sorted(sp_sch[sch_name].df['sua1'], key=float)
        sp_sch[sch_name].df.delta_t_sua1=sp_sch[sch_name].df['sua1']
        sp_sch[sch_name].max_delta_t_sua1=np.average(delta_t_sua1_low_2_high[-20:])
        sp_sch[sch_name].min_delta_t_sua1=np.average(delta_t_sua1_low_2_high[0])
        sp_sch[sch_name].df['norm_delta_t_sua1'] =- (sp_sch[sch_name].min_delta_t_sua1 -sp_sch[sch_name].df.delta_t_sua1)/(sp_sch[sch_name].max_delta_t_sua1-sp_sch[sch_name].min_delta_t_sua1)
                
        delta_t_sua2_low_2_high=sorted(sp_sch[sch_name].df['sua2'], key=float)
        sp_sch[sch_name].df.delta_t_sua2 =sp_sch[sch_name].df['sua2']
        sp_sch[sch_name].max_delta_t_sua2=np.average(delta_t_sua2_low_2_high[-20:])
        sp_sch[sch_name].min_delta_t_sua2=np.average(delta_t_sua2_low_2_high[0])
        sp_sch[sch_name].df['norm_delta_t_sua2'] =- (sp_sch[sch_name].min_delta_t_sua2 -sp_sch[sch_name].df.delta_t_sua2)/(sp_sch[sch_name].max_delta_t_sua2-sp_sch[sch_name].min_delta_t_sua2)

        delta_t_sua3_low_2_high=sorted(sp_sch[sch_name].df['sua3'], key=float)
        sp_sch[sch_name].df.delta_t_sua3 =sp_sch[sch_name].df['sua3']
        sp_sch[sch_name].max_delta_t_sua3=np.average(delta_t_sua3_low_2_high[-20:])
        sp_sch[sch_name].min_delta_t_sua3=np.average(delta_t_sua3_low_2_high[:5])
        sp_sch[sch_name].df['norm_delta_t_sua3'] =- (sp_sch[sch_name].min_delta_t_sua3 -sp_sch[sch_name].df.delta_t_sua3)/(sp_sch[sch_name].max_delta_t_sua3-sp_sch[sch_name].min_delta_t_sua3)
       
        delta_t_sub1_low_2_high=sorted(sp_sch[sch_name].df['sub1'], key=float)
        sp_sch[sch_name].df.delta_t_sub1 =sp_sch[sch_name].df['sub1']
        sp_sch[sch_name].max_delta_t_sub1=np.average(delta_t_sub1_low_2_high[-20:])
        sp_sch[sch_name].min_delta_t_sub1=np.average(delta_t_sub1_low_2_high[0])
        sp_sch[sch_name].df['norm_delta_t_sub1'] =- (sp_sch[sch_name]  .min_delta_t_sub1 -sp_sch[sch_name].df.delta_t_sub1)/(sp_sch[sch_name].max_delta_t_sub1-sp_sch[sch_name].min_delta_t_sub1)
        
        delta_t_sub2_low_2_high=sorted(sp_sch[sch_name].df['sub2'], key=float)
        sp_sch[sch_name].df.delta_t_sub2 =sp_sch[sch_name].df['sub2']
        sp_sch[sch_name].max_delta_t_sub2=np.average(delta_t_sub2_low_2_high[-20:])
        sp_sch[sch_name].min_delta_t_sub2=np.average(delta_t_sub2_low_2_high[0])
        sp_sch[sch_name].df['norm_delta_t_sub2'] =- (sp_sch[sch_name]  .min_delta_t_sub2 -sp_sch[sch_name].df.delta_t_sub2)/(sp_sch[sch_name].max_delta_t_sub2-sp_sch[sch_name].min_delta_t_sub2)

        delta_t_sub3_low_2_high=sorted(sp_sch[sch_name].df['sub3'], key=float)
        sp_sch[sch_name].df.delta_t_sub3 =sp_sch[sch_name].df['sub3']
        sp_sch[sch_name].max_delta_t_sub3=np.average(delta_t_sub3_low_2_high[-20:])
        sp_sch[sch_name].min_delta_t_sub3=np.average(delta_t_sub3_low_2_high[0])
        sp_sch[sch_name].df['norm_delta_t_sub3'] =- (sp_sch[sch_name].min_delta_t_sub3 -sp_sch[sch_name].df.delta_t_sub3)/(sp_sch[sch_name].max_delta_t_sub3-sp_sch[sch_name].min_delta_t_sub3)

        delta_t_suc1_low_2_high=sorted(sp_sch[sch_name].df['suc1'], key=float)
        sp_sch[sch_name].df.delta_t_suc1 =sp_sch[sch_name].df['suc1']
        sp_sch[sch_name].max_delta_t_suc1=np.average(delta_t_suc1_low_2_high[-30:])
        sp_sch[sch_name].min_delta_t_suc1=np.average(delta_t_suc1_low_2_high[0])
        sp_sch[sch_name].df['norm_delta_t_suc1'] =- (sp_sch[sch_name].min_delta_t_suc1 -sp_sch[sch_name].df.delta_t_suc1)/(sp_sch[sch_name].max_delta_t_suc1-sp_sch[sch_name].min_delta_t_suc1)

        delta_t_suc2_low_2_high=sorted(sp_sch[sch_name].df['suc2'], key=float)
        sp_sch[sch_name].df.delta_t_suc2 =sp_sch[sch_name].df['suc2']
        sp_sch[sch_name].max_delta_t_suc2=np.average(delta_t_suc2_low_2_high[-30:])
        sp_sch[sch_name].min_delta_t_suc2=np.average(delta_t_suc2_low_2_high[0])
        sp_sch[sch_name].df['norm_delta_t_suc2'] =- (sp_sch[sch_name].min_delta_t_suc2 -sp_sch[sch_name].df.delta_t_suc2)/(sp_sch[sch_name].max_delta_t_suc2-sp_sch[sch_name].min_delta_t_suc2)

        delta_t_suc3_low_2_high=sorted(sp_sch[sch_name].df['suc3'], key=float)
        sp_sch[sch_name].df.delta_t_suc3 =sp_sch[sch_name].df['suc3']
        sp_sch[sch_name].max_delta_t_suc3=np.average(delta_t_suc3_low_2_high[-30:])
        sp_sch[sch_name].min_delta_t_suc3=np.average(delta_t_suc3_low_2_high[0])
        sp_sch[sch_name].df['norm_delta_t_suc3'] =- (sp_sch[sch_name].min_delta_t_suc3 -sp_sch[sch_name].df.delta_t_suc3)/(sp_sch[sch_name].max_delta_t_suc3-sp_sch[sch_name].min_delta_t_suc3)


        #delta_t_su3_low_2_high=sorted(sp_sch[sch_name].df['su3'], key=float)
        #sp_sch[sch_name].df.delta_t_su3 =sp_sch[sch_name].df['su3']
        #sp_sch[sch_name].max_delta_t_su3=np.average(delta_t_su3_low_2_high[-30:])
        #sp_sch[sch_name].min_delta_t_su3=np.average(delta_t_su3_low_2_high[:30])
        #sp_sch[sch_name].df['norm_delta_t_su3'] =- (sp_sch[sch_name].min_delta_t_su3 -sp_sch[sch_name].df.delta_t_su3
        #    )/(sp_sch[sch_name].max_delta_t_su3-sp_sch[sch_name].min_delta_t_su3)

        #delta_t_su4_low_2_high=sorted(sp_sch[sch_name].df['su4'], key=float)
        #sp_sch[sch_name].df.delta_t_su4 =sp_sch[sch_name].df['su4']
        #sp_sch[sch_name].max_delta_t_su4=np.average(delta_t_su4_low_2_high[-30:])
        #sp_sch[sch_name].min_delta_t_su4=np.average(delta_t_su4_low_2_high[:30])
        #sp_sch[sch_name].df['norm_delta_t_su4'] =- (sp_sch[sch_name].min_delta_t_su4 -sp_sch[sch_name].df.delta_t_su4
        #    )/(sp_sch[sch_name].max_delta_t_su4-sp_sch[sch_name].min_delta_t_su4)

        #delta_t_su5_low_2_high=sorted(sp_sch[sch_name].df['su5'], key=float)
        #sp_sch[sch_name].df.delta_t_su5 =sp_sch[sch_name].df['su5']
        #sp_sch[sch_name].max_delta_t_su5=np.average(delta_t_su5_low_2_high[-30:])
        #sp_sch[sch_name].min_delta_t_su5=np.average(delta_t_su5_low_2_high[:30])
        #sp_sch[sch_name].df['norm_delta_t_su5'] =- (sp_sch[sch_name].min_delta_t_su5 -sp_sch[sch_name].df.delta_t_su5
        #    )/(sp_sch[sch_name].max_delta_t_su5-sp_sch[sch_name].min_delta_t_su5)

        sp_sch[sch_name].df['suctiona1']=np.exp(-1.5*(sp_sch[sch_name].df['norm_delta_t_sua1']**aa-bb))
        sp_sch[sch_name].df['suctiona2']=np.exp(-1.5*(sp_sch[sch_name].df['norm_delta_t_sua2']**aa-bb))
        sp_sch[sch_name].df['suctiona3']=np.exp(-1.5*(sp_sch[sch_name].df['norm_delta_t_sua3']**aa-bb))
        sp_sch[sch_name].df['suctionb1']=np.exp(-1.5*(sp_sch[sch_name].df['norm_delta_t_sub1']**aa-bb))
        sp_sch[sch_name].df['suctionb2']=np.exp(-1.5*(sp_sch[sch_name].df['norm_delta_t_sub2']**aa-bb))
        sp_sch[sch_name].df['suctionb3']=np.exp(-1.5*(sp_sch[sch_name].df['norm_delta_t_sub3']**aa-bb))
        sp_sch[sch_name].df['suctionc1']=np.exp(-1.5*(sp_sch[sch_name].df['norm_delta_t_suc1']**aa-bb))
        sp_sch[sch_name].df['suctionc2']=np.exp(-1.5*(sp_sch[sch_name].df['norm_delta_t_suc2']**aa-bb))
        sp_sch[sch_name].df['suctionc3']=np.exp(-1.5*(sp_sch[sch_name].df['norm_delta_t_suc3']**aa-bb))
 
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['moa1']   ,plot=plot_interpolate  ,coef=5e-15)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['moa2']   ,plot=plot_interpolate  ,coef=5e-15)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['moa3']   ,plot=plot_interpolate  ,coef=5e-15)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['mob1']   ,plot=plot_interpolate  ,coef=5e-15)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['mob2']   ,plot=plot_interpolate  ,coef=5e-15)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['mob3']   ,plot=plot_interpolate  ,coef=5e-15)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['moc1']   ,plot=plot_interpolate  ,coef=5e-15)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['moc2']   ,plot=plot_interpolate  ,coef=5e-15)  # done
        sp_sch[sch_name].merge_data(df=data_mo_su.df, keys=['moc3']   ,plot=plot_interpolate  ,coef=5e-15)  # done



        sp_sch[sch_name].df['cum_evap_scale1']=(sp_sch[sch_name].df['scale1'][1]-sp_sch[sch_name].df['scale1']
            )*constants.g2kg/sp_sch[sch_name].surface_area/constants.rhow_pure_water
        sp_sch[sch_name].df['evap_rate_scale1']=np.append(np.diff(sp_sch[sch_name].df['cum_evap_scale1'] ),np.nan)/dt_s
        sp_sch[sch_name].df['cum_evap_scale2']=(sp_sch[sch_name].df['scale2'][0]-sp_sch[sch_name].df['scale2']
            )*constants.g2kg/sp_sch[sch_name].surface_area/constants.rhow_pure_water
        sp_sch[sch_name].df['evap_rate_scale2']=np.append(np.diff(sp_sch[sch_name].df['cum_evap_scale2'] ),np.nan)/dt_s
        sp_sch[sch_name].df['cum_evap_scale3']=((sp_sch[sch_name].df['scale3'][0]-sp_sch[sch_name].df['scale3']
            )*constants.g2kg/sp_sch[sch_name].surface_area/constants.rhow_pure_water)*2.5
        sp_sch[sch_name].df['evap_rate_scale3']=np.append(np.diff(sp_sch[sch_name].df['cum_evap_scale3'] ),np.nan)/dt_s

        dry_index, min_value = min(enumerate( abs(sp_sch[sch_name].df['date_time']- sp_sch[sch_name].time_surface_emerge)), key=operator.itemgetter(1))
        sp_sch[sch_name].idx_surface_emerge = dry_index

        sp_sch[sch_name].df['sat_scale1']=-((sp_sch[sch_name].df['cum_evap_scale1'] -sp_sch[sch_name].df['cum_evap_scale1'].iloc[-1]))/(sp_sch[sch_name].df['cum_evap_scale1'].iloc[-1]-sp_sch[sch_name].df['cum_evap_scale1'].iloc[dry_index])
        sp_sch[sch_name].df['sat_scale2']=-((sp_sch[sch_name].df['cum_evap_scale2']-sp_sch[sch_name].df['cum_evap_scale2'].iloc[-1]))/(sp_sch[sch_name].df['cum_evap_scale2'].iloc[-1]-sp_sch[sch_name].df['cum_evap_scale2'].iloc[dry_index])
        sp_sch[sch_name].df['sat_scale3']=-((sp_sch[sch_name].df['cum_evap_scale3']-sp_sch[sch_name].df['cum_evap_scale3'].iloc[-1]))/(sp_sch[sch_name].df['cum_evap_scale3'].iloc[-1]-sp_sch[sch_name].df['cum_evap_scale3'].iloc[dry_index])
        moist_minimum=0.15

        sp_sch[sch_name].df['sat_scale1']= (sp_sch[sch_name].df['sat_scale1']-1)*(1-moist_minimum)+1
        sp_sch[sch_name].df['sat_scale2']= (sp_sch[sch_name].df['sat_scale2']-1)*(1-moist_minimum)+1
        sp_sch[sch_name].df['sat_scale3']= (sp_sch[sch_name].df['sat_scale3']-1)*(1-moist_minimum)+1 
   
        sp_sch[sch_name].df['sat_scale1'].loc[ sp_sch[sch_name].df['sat_scale1']>1]=1
        sp_sch[sch_name].df['sat_scale2'].loc[ sp_sch[sch_name].df['sat_scale2']>1]=1
        sp_sch[sch_name].df['sat_scale3'].loc[ sp_sch[sch_name].df['sat_scale3']>1]=1

        sp_sch[sch_name].df['suc_scale1']=constants.swcc_reverse_fredlund_xing_1994(nf=1.2,mf=0.19,af=3.8,vwc=sp_sch[sch_name].df.sat_scale1*sp_sch[sch_name].por,por=0.40)
        sp_sch[sch_name].df['suc_scale2']=constants.swcc_reverse_fredlund_xing_1994(nf=1.2,mf=0.19,af=3.8,vwc=sp_sch[sch_name].df.sat_scale2*sp_sch[sch_name].por,por=0.402)
        sp_sch[sch_name].df['suc_scale3']=constants.swcc_reverse_fredlund_xing_1994(nf=1.2,mf=0.19,af=3.8,vwc=sp_sch[sch_name].df.sat_scale3*sp_sch[sch_name].por,por=0.482)


# linear fitting for moisture 
dp=np.linspace(260,530,num=30)
alpha_1=-4.8
#alpha_2=-10.1
#Galpha_3=-10.1
#sch_name='bacteria_first'
sp_sch[sch_name].moa1_fit1     = np.polyfit(sp_sch[sch_name].df['moa1'],sp_sch[sch_name].df ['sat_scale1'],1)
sp_sch[sch_name].moa1_fit1_str = 'y = '+"{0:0.3f}".format( sp_sch[sch_name].moa1_fit1[0]  ) + ' x ' + "{0:0.2f}".format( sp_sch[sch_name].moa1_fit1[1]  )
sp_sch[sch_name].moa1_fit2     = np.polyfit(sp_sch[sch_name].df['moa1'],sp_sch[sch_name].df ['sat_scale1'],2)
#sp_sch[sch_name].mo0_fit_twopoint=[360,290,alpha_1]
sp_sch[sch_name].moa1_fit_twopoint=[550,150,alpha_1]
sp_sch[sch_name].moa1_dp= (dp**sp_sch[sch_name].moa1_fit_twopoint[2]-sp_sch[sch_name].moa1_fit_twopoint[0]**sp_sch[sch_name].moa1_fit_twopoint[2])/(sp_sch[sch_name].moa1_fit_twopoint[1]**sp_sch[sch_name].moa1_fit_twopoint[2]-sp_sch[sch_name].moa1_fit_twopoint[0]**sp_sch[sch_name].moa1_fit_twopoint[2])
sp_sch[sch_name].moa1_text='y = (x$^{-10.1}$-290$^{-10.1}$)/(530$^{-10.1}$-290$^{-10.1}$)'

sp_sch[sch_name].moa2_fit1     = np.polyfit(sp_sch[sch_name].df['moa2'],sp_sch[sch_name].df ['sat_scale1'],1)
sp_sch[sch_name].moa2_fit1_str = 'y = '+"{0:0.3f}".format( sp_sch[sch_name].moa1_fit1[0]  ) + ' x ' + "{0:0.2f}".format( sp_sch[sch_name].moa2_fit1[1]  )
sp_sch[sch_name].moa2_fit2     = np.polyfit(sp_sch[sch_name].df['moa2'],sp_sch[sch_name].df ['sat_scale1'],2)
#sp_sch[sch_name].mo0_fit_twopoint=[360,290,alpha_1]
sp_sch[sch_name].moa2_fit_twopoint=[580,220,alpha_1]
sp_sch[sch_name].moa2_dp= (dp**sp_sch[sch_name].moa2_fit_twopoint[2]-sp_sch[sch_name].moa2_fit_twopoint[0]**sp_sch[sch_name].moa2_fit_twopoint[2])/(sp_sch[sch_name].moa2_fit_twopoint[1]**sp_sch[sch_name].moa2_fit_twopoint[2]-sp_sch[sch_name].moa2_fit_twopoint[0]**sp_sch[sch_name].moa2_fit_twopoint[2])
sp_sch[sch_name].moa2_text='y = (x$^{-10.1}$-290$^{-10.1}$)/(530$^{-10.1}$-290$^{-10.1}$)'

sp_sch[sch_name].moa3_fit1     = np.polyfit(sp_sch[sch_name].df['moa3'],sp_sch[sch_name].df ['sat_scale1'],1)
sp_sch[sch_name].moa3_fit1_str = 'y = '+"{0:0.3f}".format( sp_sch[sch_name].moa3_fit1[0]  ) + ' x ' + "{0:0.2f}".format( sp_sch[sch_name].moa3_fit1[1]  )
sp_sch[sch_name].moa3_fit2     = np.polyfit(sp_sch[sch_name].df['moa3'],sp_sch[sch_name].df ['sat_scale1'],2)
#sp_sch[sch_name].mo1_fit_twopoint=[380,290,alpha_1]
sp_sch[sch_name].moa3_fit_twopoint=[580,210,alpha_1]
sp_sch[sch_name].moa3_dp= (dp**sp_sch[sch_name].moa3_fit_twopoint[2]-sp_sch[sch_name].moa3_fit_twopoint[0]**sp_sch[sch_name].moa3_fit_twopoint[2])/(sp_sch[sch_name].moa3_fit_twopoint[1]**sp_sch[sch_name].moa3_fit_twopoint[2]-sp_sch[sch_name].moa3_fit_twopoint[0]**sp_sch[sch_name].moa3_fit_twopoint[2])
sp_sch[sch_name].moa3_text='y = (x$^{-10.1}$-275$^{-10.1}$)/(530$^{-10.1}$-275$^{-10.1}$)'

sp_sch[sch_name].mob1_fit1     = np.polyfit(sp_sch[sch_name].df['mob1'],sp_sch[sch_name].df ['sat_scale1'],1)
sp_sch[sch_name].mob1_fit1_str = 'y = '+"{0:0.3f}".format( sp_sch[sch_name].mob1_fit1[0]  ) + ' x ' + "{0:0.2f}".format( sp_sch[sch_name].mob1_fit1[1]  )
sp_sch[sch_name].mob1_fit2     = np.polyfit(sp_sch[sch_name].df['mob1'],sp_sch[sch_name].df ['sat_scale1'],2)
#sp_sch[sch_name].mo2_fit_twopoint=[530,305,alpha_1]
sp_sch[sch_name].mob1_fit_twopoint=[580,230,alpha_1]
sp_sch[sch_name].mob1_dp= (dp**sp_sch[sch_name].mob1_fit_twopoint[2]-sp_sch[sch_name].mob1_fit_twopoint[0]**sp_sch[sch_name].mob1_fit_twopoint[2])/(sp_sch[sch_name].mob1_fit_twopoint[1]**sp_sch[sch_name].mob1_fit_twopoint[2]-sp_sch[sch_name].mob1_fit_twopoint[0]**sp_sch[sch_name].mob1_fit_twopoint[2])
sp_sch[sch_name].mob1_text='y = (x$^{-10.1}$-290$^{-10.1}$)/(530$^{-10.1}$-290$^{-10.1}$)'

sp_sch[sch_name].mob2_fit1     = np.polyfit(sp_sch[sch_name].df['mob2'],sp_sch[sch_name].df ['sat_scale2'],1)
sp_sch[sch_name].mob2_fit1_str = 'y = '+"{0:0.3f}".format( sp_sch[sch_name].mob2_fit1[0]  ) + ' x ' + "{0:0.2f}".format( sp_sch[sch_name].mob2_fit1[1]  )
sp_sch[sch_name].mob2_fit2     = np.polyfit(sp_sch[sch_name].df['mob2'],sp_sch[sch_name].df ['sat_scale2'],2)
#sp_sch[sch_name].mo3_fit_twopoint=[380,300,alpha_1]
sp_sch[sch_name].mob2_fit_twopoint=[570,250,alpha_1]
sp_sch[sch_name].mob2_dp= (dp**sp_sch[sch_name].mob2_fit_twopoint[2]-sp_sch[sch_name].mob2_fit_twopoint[0]**sp_sch[sch_name].mob2_fit_twopoint[2])/(sp_sch[sch_name].mob2_fit_twopoint[1]**sp_sch[sch_name].mob2_fit_twopoint[2]-sp_sch[sch_name].mob2_fit_twopoint[0]**sp_sch[sch_name].mob2_fit_twopoint[2])
sp_sch[sch_name].mob2_text='y = (x$^{-10.1}$-292$^{-10.1}$)/(535$^{-10.1}$-292$^{-10.1}$)'

sp_sch[sch_name].mob3_fit1     = np.polyfit(sp_sch[sch_name].df['mob3'],sp_sch[sch_name].df ['sat_scale2'],1)
sp_sch[sch_name].mob3_fit1_str = 'y = '+"{0:0.3f}".format( sp_sch[sch_name].mob3_fit1[0]  ) + ' x ' + "{0:0.2f}".format( sp_sch[sch_name].mob3_fit1[1]  )
sp_sch[sch_name].mob3_fit2     = np.polyfit(sp_sch[sch_name].df['mob3'],sp_sch[sch_name].df ['sat_scale2'],2)
#sp_sch[sch_name].mo4_fit_twopoint=[530,295,alpha_1]
sp_sch[sch_name].mob3_fit_twopoint=[570,210,alpha_1]
sp_sch[sch_name].mob3_dp= (dp**sp_sch[sch_name].mob3_fit_twopoint[2]-sp_sch[sch_name].mob3_fit_twopoint[0]**sp_sch[sch_name].mob3_fit_twopoint[2])/(sp_sch[sch_name].mob3_fit_twopoint[1]**sp_sch[sch_name].mob3_fit_twopoint[2]-sp_sch[sch_name].mob3_fit_twopoint[0]**sp_sch[sch_name].mob3_fit_twopoint[2])
sp_sch[sch_name].mob3_text='y = (x$^{-10.1}$-286$^{-10.1}$)/(530$^{-7.1}$-286$^{-10.1}$)'

sp_sch[sch_name].moc1_fit1     = np.polyfit(sp_sch[sch_name].df['moc1'],sp_sch[sch_name].df ['sat_scale3'],1)
sp_sch[sch_name].moc1_fit1_str = 'y = '+"{0:0.3f}".format( sp_sch[sch_name].moc1_fit1[0]  ) + ' x ' + "{0:0.2f}".format( sp_sch[sch_name].moc1_fit1[1]  )
sp_sch[sch_name].moc1_fit2     = np.polyfit(sp_sch[sch_name].df['moc1'],sp_sch[sch_name].df ['sat_scale3'],2)
#sp_sch[sch_name].mo5_fit_twopoint=[530,285,alpha_1]
sp_sch[sch_name].moc1_fit_twopoint=[580,240,alpha_1]
sp_sch[sch_name].moc1_dp= (dp**sp_sch[sch_name].moc1_fit_twopoint[2]-sp_sch[sch_name].moc1_fit_twopoint[0]**sp_sch[sch_name].moc1_fit_twopoint[2])/(sp_sch[sch_name].moc1_fit_twopoint[1]**sp_sch[sch_name].moc1_fit_twopoint[2]-sp_sch[sch_name].moc1_fit_twopoint[0]**sp_sch[sch_name].moc1_fit_twopoint[2])
sp_sch[sch_name].moc1_text='y = (x$^{-10.1}$-273$^{-10.1}$)/(530$^{-10.1}$-273$^{-10.1}$)'

sp_sch[sch_name].moc2_fit1     = np.polyfit(sp_sch[sch_name].df['moc2'],sp_sch[sch_name].df ['sat_scale3'],1)
sp_sch[sch_name].moc2_fit1_str = 'y = '+"{0:0.3f}".format( sp_sch[sch_name].moc2_fit1[0]  ) + ' x ' + "{0:0.2f}".format( sp_sch[sch_name].moc2_fit1[1]  )
sp_sch[sch_name].moc2_fit2     = np.polyfit(sp_sch[sch_name].df['moc2'],sp_sch[sch_name].df ['sat_scale3'],2)
#sp_sch[sch_name].mo5_fit_twopoint=[530,285,alpha_1]
sp_sch[sch_name].moc2_fit_twopoint=[600,260,alpha_1]
sp_sch[sch_name].moc2_dp= (dp**sp_sch[sch_name].moc2_fit_twopoint[2]-sp_sch[sch_name].moc2_fit_twopoint[0]**sp_sch[sch_name].moc2_fit_twopoint[2])/(sp_sch[sch_name].moc2_fit_twopoint[1]**sp_sch[sch_name].moc2_fit_twopoint[2]-sp_sch[sch_name].moc2_fit_twopoint[0]**sp_sch[sch_name].moc2_fit_twopoint[2])
sp_sch[sch_name].moc2_text='y = (x$^{-10.1}$-273$^{-10.1}$)/(530$^{-10.1}$-273$^{-10.1}$)'

sp_sch[sch_name].moc3_fit1     = np.polyfit(sp_sch[sch_name].df['moc3'],sp_sch[sch_name].df ['sat_scale3'],1)
sp_sch[sch_name].moc3_fit1_str = 'y = '+"{0:0.3f}".format( sp_sch[sch_name].moc3_fit1[0]  ) + ' x ' + "{0:0.2f}".format( sp_sch[sch_name].moc3_fit1[1]  )
sp_sch[sch_name].moc3_fit2     = np.polyfit(sp_sch[sch_name].df['moc3'],sp_sch[sch_name].df ['sat_scale3'],2)
#sp_sch[sch_name].mo5_fit_twopoint=[530,285,alpha_1]
sp_sch[sch_name].moc3_fit_twopoint=[580,170,alpha_1]
sp_sch[sch_name].moc3_dp= (dp**sp_sch[sch_name].moc3_fit_twopoint[2]-sp_sch[sch_name].moc3_fit_twopoint[0]**sp_sch[sch_name].moc3_fit_twopoint[2])/(sp_sch[sch_name].moc3_fit_twopoint[1]**sp_sch[sch_name].moc3_fit_twopoint[2]-sp_sch[sch_name].moc3_fit_twopoint[0]**sp_sch[sch_name].moc3_fit_twopoint[2])
sp_sch[sch_name].moc3_text='y = (x$^{-10.1}$-273$^{-10.1}$)/(530$^{-10.1}$-273$^{-10.1}$)'


sp_sch[sch_name].df['mmoa1']=(sp_sch[sch_name].moa1_fit_twopoint[0]**sp_sch[sch_name].moa1_fit_twopoint[2]-sp_sch[sch_name].df['moa1']**sp_sch[sch_name].moa1_fit_twopoint[2])/(sp_sch[sch_name].moa1_fit_twopoint[0]**sp_sch[sch_name].moa1_fit_twopoint[2]-sp_sch[sch_name].moa1_fit_twopoint[1]**sp_sch[sch_name].moa1_fit_twopoint[2])
sp_sch[sch_name].df['mmoa2']=(sp_sch[sch_name].moa2_fit_twopoint[0]**sp_sch[sch_name].moa2_fit_twopoint[2]-sp_sch[sch_name].df['moa2']**sp_sch[sch_name].moa2_fit_twopoint[2])/(sp_sch[sch_name].moa2_fit_twopoint[0]**sp_sch[sch_name].moa2_fit_twopoint[2]-sp_sch[sch_name].moa2_fit_twopoint[1]**sp_sch[sch_name].moa3_fit_twopoint[2])
sp_sch[sch_name].df['mmoa3']=(sp_sch[sch_name].moa3_fit_twopoint[0]**sp_sch[sch_name].moa3_fit_twopoint[2]-sp_sch[sch_name].df['moa3']**sp_sch[sch_name].moa3_fit_twopoint[2])/(sp_sch[sch_name].moa3_fit_twopoint[0]**sp_sch[sch_name].moa3_fit_twopoint[2]-sp_sch[sch_name].moa3_fit_twopoint[1]**sp_sch[sch_name].moa3_fit_twopoint[2])
sp_sch[sch_name].df['mmob1']=(sp_sch[sch_name].mob1_fit_twopoint[0]**sp_sch[sch_name].mob1_fit_twopoint[2]-sp_sch[sch_name].df['mob1']**sp_sch[sch_name].mob1_fit_twopoint[2])/(sp_sch[sch_name].mob1_fit_twopoint[0]**sp_sch[sch_name].mob1_fit_twopoint[2]-sp_sch[sch_name].mob1_fit_twopoint[1]**sp_sch[sch_name].mob1_fit_twopoint[2])
sp_sch[sch_name].df['mmob2']=(sp_sch[sch_name].mob2_fit_twopoint[0]**sp_sch[sch_name].mob2_fit_twopoint[2]-sp_sch[sch_name].df['mob2']**sp_sch[sch_name].mob2_fit_twopoint[2])/(sp_sch[sch_name].mob2_fit_twopoint[0]**sp_sch[sch_name].mob2_fit_twopoint[2]-sp_sch[sch_name].mob2_fit_twopoint[1]**sp_sch[sch_name].mob2_fit_twopoint[2])
sp_sch[sch_name].df['mmob3']=(sp_sch[sch_name].mob3_fit_twopoint[0]**sp_sch[sch_name].mob3_fit_twopoint[2]-sp_sch[sch_name].df['mob3']**sp_sch[sch_name].mob3_fit_twopoint[2])/(sp_sch[sch_name].mob3_fit_twopoint[0]**sp_sch[sch_name].mob3_fit_twopoint[2]-sp_sch[sch_name].mob3_fit_twopoint[1]**sp_sch[sch_name].mob3_fit_twopoint[2])
sp_sch[sch_name].df['mmoc1']=(sp_sch[sch_name].moc1_fit_twopoint[0]**sp_sch[sch_name].moc1_fit_twopoint[2]-sp_sch[sch_name].df['moc1']**sp_sch[sch_name].moc1_fit_twopoint[2])/(sp_sch[sch_name].moc1_fit_twopoint[0]**sp_sch[sch_name].moc1_fit_twopoint[2]-sp_sch[sch_name].moc1_fit_twopoint[1]**sp_sch[sch_name].moc1_fit_twopoint[2])
sp_sch[sch_name].df['mmoc2']=(sp_sch[sch_name].moc2_fit_twopoint[0]**sp_sch[sch_name].moc2_fit_twopoint[2]-sp_sch[sch_name].df['moc2']**sp_sch[sch_name].moc2_fit_twopoint[2])/(sp_sch[sch_name].moc2_fit_twopoint[0]**sp_sch[sch_name].moc2_fit_twopoint[2]-sp_sch[sch_name].moc2_fit_twopoint[1]**sp_sch[sch_name].moc2_fit_twopoint[2])
sp_sch[sch_name].df['mmoc3']=(sp_sch[sch_name].moc3_fit_twopoint[0]**sp_sch[sch_name].moc3_fit_twopoint[2]-sp_sch[sch_name].df['moc3']**sp_sch[sch_name].moc3_fit_twopoint[2])/(sp_sch[sch_name].moc3_fit_twopoint[0]**sp_sch[sch_name].moc3_fit_twopoint[2]-sp_sch[sch_name].moc3_fit_twopoint[1]**sp_sch[sch_name].moc3_fit_twopoint[2])


sp_sch[sch_name].df['mmoa1'].loc[sp_sch[sch_name].df['mmoa1']>1]=np.nan;
sp_sch[sch_name].df['mmoa2'].loc[sp_sch[sch_name].df['mmoa2']>1]=np.nan;
sp_sch[sch_name].df['mmoa3'].loc[sp_sch[sch_name].df['mmoa3']>1]=np.nan;
sp_sch[sch_name].df['mmob1'].loc[sp_sch[sch_name].df['mmob1']>1]=np.nan;
sp_sch[sch_name].df['mmob2'].loc[sp_sch[sch_name].df['mmob2']>1]=np.nan;
sp_sch[sch_name].df['mmob3'].loc[sp_sch[sch_name].df['mmob3']>1]=np.nan;
sp_sch[sch_name].df['mmoc1'].loc[sp_sch[sch_name].df['mmoc1']>1]=np.nan;
sp_sch[sch_name].df['mmoc2'].loc[sp_sch[sch_name].df['mmoc2']>1]=np.nan;
sp_sch[sch_name].df['mmoc3'].loc[sp_sch[sch_name].df['mmoc3']>1]=np.nan;



#sch_name='bacteria_second'
#sp_sch[sch_name].mo0_fit1     = np.polyfit(sp_sch[sch_name].df['mo0'],sp_sch[sch_name].df ['sat_scale1'],1)
#sp_sch[sch_name].mo0_fit1_str = 'y = '+"{0:0.3f}".format( sp_sch[sch_name].mo0_fit1[0]  ) + ' x ' + "{0:0.2f}".format( sp_sch[sch_name].mo0_fit1[1]  )
#sp_sch[sch_name].mo0_fit2     = np.polyfit(sp_sch[sch_name].df['mo0'],sp_sch[sch_name].df ['sat_scale1'],2)
#sp_sch[sch_name].mo0_fit_twopoint=[360,300,alpha_1]
#sp_sch[sch_name].mo0_fit_twopoint=sp_sch['bacteria_first'].mo0_fit_twopoint
#sp_sch[sch_name].mo0_dp= (dp**sp_sch[sch_name].mo0_fit_twopoint[2]-sp_sch[sch_name].mo0_fit_twopoint[0]**sp_sch[sch_name].mo0_fit_twopoint[2])/(sp_sch[sch_name].mo0_fit_twopoint[1]**sp_sch[sch_name].mo0_fit_twopoint[2]-sp_sch[sch_name].mo0_fit_twopoint[0]**sp_sch[sch_name].mo0_fit_twopoint[2])
#sp_sch[sch_name].mo0_text='y = (x$^{-7.1}$-290$^{-7.1}$)/(360$^{-7.1}$-290$^{-7.1}$)'
#
#sp_sch[sch_name].mo1_fit1     = np.polyfit(sp_sch[sch_name].df['mo1'],sp_sch[sch_name].df ['sat_scale1'],1)
#sp_sch[sch_name].mo1_fit1_str = 'y = '+"{0:0.3f}".format( sp_sch[sch_name].mo1_fit1[0]  ) + ' x ' + "{0:0.2f}".format( sp_sch[sch_name].mo1_fit1[1]  )
#sp_sch[sch_name].mo1_fit_twopoint=sp_sch['bacteria_first'].mo1_fit_twopoint
#sp_sch[sch_name].mo1_fit_twopoint=[390,300,alpha_1]
#sp_sch[sch_name].mo1_fit2     = np.polyfit(sp_sch[sch_name].df['mo1'],sp_sch[sch_name].df ['sat_scale1'],2)
#sp_sch[sch_name].mo1_dp= (dp**sp_sch[sch_name].mo1_fit_twopoint[2]-sp_sch[sch_name].mo1_fit_twopoint[0]**sp_sch[sch_name].mo1_fit_twopoint[2])/(sp_sch[sch_name].mo1_fit_twopoint[1]**sp_sch[sch_name].mo1_fit_twopoint[2]-sp_sch[sch_name].mo1_fit_twopoint[0]**sp_sch[sch_name].mo1_fit_twopoint[2])
#sp_sch[sch_name].mo1_text='y = (x$^{-7.1}$-290$^{-7.1}$)/(380$^{-7.1}$-290$^{-7.1}$)'
#
#sp_sch[sch_name].mo2_fit1     = np.polyfit(sp_sch[sch_name].df['mo2'],sp_sch[sch_name].df ['sat_scale1'],1)
#sp_sch[sch_name].mo2_fit1_str = 'y = '+"{0:0.3f}".format( sp_sch[sch_name].mo2_fit1[0]  ) + ' x ' + "{0:0.2f}".format( sp_sch[sch_name].mo2_fit1[1]  )
#sp_sch[sch_name].mo2_fit_twopoint=sp_sch['bacteria_first'].mo2_fit_twopoint
#sp_sch[sch_name].mo2_fit_twopoint=[370,310,alpha_1]
#sp_sch[sch_name].mo2_fit2     = np.polyfit(sp_sch[sch_name].df['mo2'],sp_sch[sch_name].df ['sat_scale1'],2)
#sp_sch[sch_name].mo2_dp= (dp**sp_sch[sch_name].mo2_fit_twopoint[2]-sp_sch[sch_name].mo2_fit_twopoint[0]**sp_sch[sch_name].mo2_fit_twopoint[2])/(sp_sch[sch_name].mo2_fit_twopoint[1]**sp_sch[sch_name].mo2_fit_twopoint[2]-sp_sch[sch_name].mo2_fit_twopoint[0]**sp_sch[sch_name].mo2_fit_twopoint[2])
#sp_sch[sch_name].mo2_text='y = (x$^{-7.1}$-310$^{-7.1}$)/(365$^{-7.1}$-310$^{-7.1}$)'
#
#sp_sch[sch_name].mo3_fit1     = np.polyfit(sp_sch[sch_name].df['mo3'],sp_sch[sch_name].df ['sat_scale2'],1)
#sp_sch[sch_name].mo3_fit1_str = 'y = '+"{0:0.3f}".format( sp_sch[sch_name].mo3_fit1[0]  ) + ' x ' + "{0:0.2f}".format( sp_sch[sch_name].mo3_fit1[1]  )
#sp_sch[sch_name].mo3_fit_twopoint=sp_sch['bacteria_first'].mo3_fit_twopoint
#sp_sch[sch_name].mo3_fit_twopoint=[440,300,alpha_1]
#sp_sch[sch_name].mo3_fit2     = np.polyfit(sp_sch[sch_name].df['mo3'],sp_sch[sch_name].df ['sat_scale2'],2)
#sp_sch[sch_name].mo3_dp= (dp**sp_sch[sch_name].mo3_fit_twopoint[2]-sp_sch[sch_name].mo3_fit_twopoint[0]**sp_sch[sch_name].mo3_fit_twopoint[2])/(sp_sch[sch_name].mo3_fit_twopoint[1]**sp_sch[sch_name].mo3_fit_twopoint[2]-sp_sch[sch_name].mo3_fit_twopoint[0]**sp_sch[sch_name].mo3_fit_twopoint[2])
#sp_sch[sch_name].mo3_text='y = (x$^{-7.1}$-300$^{-7.1}$)/(430$^{-7.1}$-300$^{-7.1}$)'

#sp_sch[sch_name].mo4_fit1     = np.polyfit(sp_sch[sch_name].df['mo4'],sp_sch[sch_name].df ['sat_scale2'],1)
#sp_sch[sch_name].mo4_fit1_str = 'y = '+"{0:0.3f}".format( sp_sch[sch_name].mo4_fit1[0]  ) + ' x ' + "{0:0.2f}".format( sp_sch[sch_name].mo4_fit1[1]  )
#sp_sch[sch_name].mo4_fit_twopoint=sp_sch['bacteria_first'].mo4_fit_twopoint
#sp_sch[sch_name].mo4_fit_twopoint=[350,285,alpha_1]
#sp_sch[sch_name].mo4_fit2     = np.polyfit(sp_sch[sch_name].df['mo4'],sp_sch[sch_name].df ['sat_scale2'],2)
#sp_sch[sch_name].mo4_dp= (dp**sp_sch[sch_name].mo4_fit_twopoint[2]-sp_sch[sch_name].mo4_fit_twopoint[0]**sp_sch[sch_name].mo4_fit_twopoint[2])/(sp_sch[sch_name].mo4_fit_twopoint[1]**sp_sch[sch_name].mo4_fit_twopoint[2]-sp_sch[sch_name].mo4_fit_twopoint[0]**sp_sch[sch_name].mo4_fit_twopoint[2])
#sp_sch[sch_name].mo4_text='y = (x$^{-7.1}$-285$^{-7.1}$)/(350$^{-7.1}$-285$^{-7.1}$)'
#
#sp_sch[sch_name].mo5_fit1     = np.polyfit(sp_sch[sch_name].df['mo5'],sp_sch[sch_name].df ['sat_scale2'],1)
#sp_sch[sch_name].mo5_fit1_str = 'y = '+"{0:0.3f}".format( sp_sch[sch_name].mo5_fit1[0]  ) + ' x ' + "{0:0.2f}".format( sp_sch[sch_name].mo5_fit1[1]  )
#sp_sch[sch_name].mo5_fit_twopoint=sp_sch['bacteria_first'].mo5_fit_twopoint
#sp_sch[sch_name].mo5_fit_twopoint=[330,280,alpha_1]
#sp_sch[sch_name].mo5_fit2     = np.polyfit(sp_sch[sch_name].df['mo5'],sp_sch[sch_name].df ['sat_scale2'],2)
#sp_sch[sch_name].mo5_dp= (dp**sp_sch[sch_name].mo5_fit_twopoint[2]-sp_sch[sch_name].mo5_fit_twopoint[0]**sp_sch[sch_name].mo5_fit_twopoint[2])/(sp_sch[sch_name].mo5_fit_twopoint[1]**sp_sch[sch_name].mo5_fit_twopoint[2]-sp_sch[sch_name].mo5_fit_twopoint[0]**sp_sch[sch_name].mo5_fit_twopoint[2])
#sp_sch[sch_name].mo5_text='y = (x$^{-7.1}$-273$^{-7.1}$)/(320$^{-7.1}$-273$^{-7.1}$)'
#
#sp_sch[sch_name].df['mmo0']=(sp_sch[sch_name].mo0_fit_twopoint[0]**sp_sch[sch_name].mo0_fit_twopoint[2]-sp_sch[sch_name].df['mo0']**sp_sch[sch_name].mo0_fit_twopoint[2])/(sp_sch[sch_name].mo0_fit_twopoint[0]**sp_sch[sch_name].mo0_fit_twopoint[2]-sp_sch[sch_name].mo0_fit_twopoint[1]**sp_sch[sch_name].mo0_fit_twopoint[2])
#sp_sch[sch_name].df['mmo1']=(sp_sch[sch_name].mo1_fit_twopoint[0]**sp_sch[sch_name].mo1_fit_twopoint[2]-sp_sch[sch_name].df['mo1']**sp_sch[sch_name].mo1_fit_twopoint[2])/(sp_sch[sch_name].mo1_fit_twopoint[0]**sp_sch[sch_name].mo1_fit_twopoint[2]-sp_sch[sch_name].mo1_fit_twopoint[1]**sp_sch[sch_name].mo1_fit_twopoint[2])
#sp_sch[sch_name].df['mmo2']=(sp_sch[sch_name].mo2_fit_twopoint[0]**sp_sch[sch_name].mo2_fit_twopoint[2]-sp_sch[sch_name].df['mo2']**sp_sch[sch_name].mo2_fit_twopoint[2])/(sp_sch[sch_name].mo2_fit_twopoint[0]**sp_sch[sch_name].mo2_fit_twopoint[2]-sp_sch[sch_name].mo2_fit_twopoint[1]**sp_sch[sch_name].mo2_fit_twopoint[2])
#sp_sch[sch_name].df['mmo3']=(sp_sch[sch_name].mo3_fit_twopoint[0]**sp_sch[sch_name].mo3_fit_twopoint[2]-sp_sch[sch_name].df['mo3']**sp_sch[sch_name].mo3_fit_twopoint[2])/(sp_sch[sch_name].mo3_fit_twopoint[0]**sp_sch[sch_name].mo3_fit_twopoint[2]-sp_sch[sch_name].mo3_fit_twopoint[1]**sp_sch[sch_name].mo3_fit_twopoint[2])
#sp_sch[sch_name].df['mmo4']=(sp_sch[sch_name].mo4_fit_twopoint[0]**sp_sch[sch_name].mo4_fit_twopoint[2]-sp_sch[sch_name].df['mo4']**sp_sch[sch_name].mo4_fit_twopoint[2])/(sp_sch[sch_name].mo4_fit_twopoint[0]**sp_sch[sch_name].mo4_fit_twopoint[2]-sp_sch[sch_name].mo4_fit_twopoint[1]**sp_sch[sch_name].mo4_fit_twopoint[2])
#sp_sch[sch_name].df['mmo5']=(sp_sch[sch_name].mo5_fit_twopoint[0]**sp_sch[sch_name].mo5_fit_twopoint[2]-sp_sch[sch_name].df['mo5']**sp_sch[sch_name].mo5_fit_twopoint[2])/(sp_sch[sch_name].mo5_fit_twopoint[0]**sp_sch[sch_name].mo5_fit_twopoint[2]-sp_sch[sch_name].mo5_fit_twopoint[1]**sp_sch[sch_name].mo5_fit_twopoint[2])
#
#
#
#sch_name='bacteria_third'
#sp_sch[sch_name].mo0_fit1     = np.polyfit(sp_sch[sch_name].df['mo0'],sp_sch[sch_name].df ['sat_scale1'],1)
#sp_sch[sch_name].mo0_fit1_str = 'y = '+"{0:0.3f}".format( sp_sch[sch_name].mo0_fit1[0]  ) + ' x ' + "{0:0.2f}".format( sp_sch[sch_name].mo0_fit1[1]  )
#sp_sch[sch_name].mo0_fit2     = np.polyfit(sp_sch[sch_name].df['mo0'],sp_sch[sch_name].df ['sat_scale1'],2)
##sp_sch[sch_name].mo0_fit_twopoint=sp_sch['bacteria_first'].mo0_fit_twopoint
#sp_sch[sch_name].mo0_fit_twopoint=[320,285,alpha_1]
#sp_sch[sch_name].mo0_dp= (dp**sp_sch[sch_name].mo0_fit_twopoint[2]-sp_sch[sch_name].mo0_fit_twopoint[0]**sp_sch[sch_name].mo0_fit_twopoint[2])/(sp_sch[sch_name].mo0_fit_twopoint[1]**sp_sch[sch_name].mo0_fit_twopoint[2]-sp_sch[sch_name].mo0_fit_twopoint[0]**sp_sch[sch_name].mo0_fit_twopoint[2])
#sp_sch[sch_name].mo0_text='y = (x$^{-7.1}$-280$^{-7.1}$)/(300$^{-7.1}$-280$^{-7.1}$)'
#
#sp_sch[sch_name].mo1_fit1     = np.polyfit(sp_sch[sch_name].df['mo1'],sp_sch[sch_name].df ['sat_scale1'],1)
#sp_sch[sch_name].mo1_fit1_str = 'y = '+"{0:0.3f}".format( sp_sch[sch_name].mo1_fit1[0]  ) + ' x ' + "{0:0.2f}".format( sp_sch[sch_name].mo1_fit1[1]  )
#sp_sch[sch_name].mo1_fit2     = np.polyfit(sp_sch[sch_name].df['mo1'],sp_sch[sch_name].df ['sat_scale1'],2)
##sp_sch[sch_name].mo1_fit_twopoint=sp_sch['bacteria_first'].mo1_fit_twopoint
#sp_sch[sch_name].mo1_fit_twopoint=[355,275,alpha_1]
#sp_sch[sch_name].mo1_dp= (dp**sp_sch[sch_name].mo1_fit_twopoint[2]-sp_sch[sch_name].mo1_fit_twopoint[0]**sp_sch[sch_name].mo1_fit_twopoint[2])/(sp_sch[sch_name].mo1_fit_twopoint[1]**sp_sch[sch_name].mo1_fit_twopoint[2]-sp_sch[sch_name].mo1_fit_twopoint[0]**sp_sch[sch_name].mo1_fit_twopoint[2])
#sp_sch[sch_name].mo1_text='y = (x$^{-3.1}$-270$^{-3.1}$)/(305$^{-3.1}$-270$^{-3.1}$)'
#
#sp_sch[sch_name].mo2_fit1     = np.polyfit(sp_sch[sch_name].df['mo2'],sp_sch[sch_name].df ['sat_scale1'],1)
#sp_sch[sch_name].mo2_fit1_str = 'y = '+"{0:0.3f}".format( sp_sch[sch_name].mo2_fit1[0]  ) + ' x ' + "{0:0.2f}".format( sp_sch[sch_name].mo2_fit1[1]  )
##sp_sch[sch_name].mo2_fit_twopoint=sp_sch['bacteria_first'].mo2_fit_twopoint
#sp_sch[sch_name].mo2_fit_twopoint=[310,290,alpha_1]
#sp_sch[sch_name].mo2_fit2     = np.polyfit(sp_sch[sch_name].df['mo2'],sp_sch[sch_name].df ['sat_scale1'],2)
#sp_sch[sch_name].mo2_dp= (dp**sp_sch[sch_name].mo2_fit_twopoint[2]-sp_sch[sch_name].mo2_fit_twopoint[0]**sp_sch[sch_name].mo2_fit_twopoint[2])/(sp_sch[sch_name].mo2_fit_twopoint[1]**sp_sch[sch_name].mo2_fit_twopoint[2]-sp_sch[sch_name].mo2_fit_twopoint[0]**sp_sch[sch_name].mo2_fit_twopoint[2])
#sp_sch[sch_name].mo2_text='y = (x$^{-7.1}$-284$^{-7.1}$)/(305$^{-7.1}$-284$^{-7.1}$)'
#
#sp_sch[sch_name].mo3_fit1     = np.polyfit(sp_sch[sch_name].df['mo3'],sp_sch[sch_name].df ['sat_scale2'],1)
#sp_sch[sch_name].mo3_fit1_str = 'y = '+"{0:0.3f}".format( sp_sch[sch_name].mo3_fit1[0]  ) + ' x ' + "{0:0.2f}".format( sp_sch[sch_name].mo3_fit1[1]  )
##sp_sch[sch_name].mo3_fit_twopoint=sp_sch['bacteria_first'].mo3_fit_twopoint
#sp_sch[sch_name].mo3_fit_twopoint=[320,290,alpha_1]
#sp_sch[sch_name].mo3_fit2     = np.polyfit(sp_sch[sch_name].df['mo3'],sp_sch[sch_name].df ['sat_scale2'],2)
#sp_sch[sch_name].mo3_dp= (dp**sp_sch[sch_name].mo3_fit_twopoint[2]-sp_sch[sch_name].mo3_fit_twopoint[0]**sp_sch[sch_name].mo3_fit_twopoint[2])/(sp_sch[sch_name].mo3_fit_twopoint[1]**sp_sch[sch_name].mo3_fit_twopoint[2]-sp_sch[sch_name].mo3_fit_twopoint[0]**sp_sch[sch_name].mo3_fit_twopoint[2])
#sp_sch[sch_name].mo3_text='y = (x$^{-7.1}$-285$^{-7.1}$)/(295$^{-7.1}$-285$^{-7.1}$)'
#
#sp_sch[sch_name].mo4_fit1     = np.polyfit(sp_sch[sch_name].df['mo4'],sp_sch[sch_name].df ['sat_scale2'],1)
#sp_sch[sch_name].mo4_fit1_str = 'y = '+"{0:0.3f}".format( sp_sch[sch_name].mo4_fit1[0]  ) + ' x ' + "{0:0.2f}".format( sp_sch[sch_name].mo4_fit1[1]  )
##sp_sch[sch_name].mo4_fit_twopoint=sp_sch['bacteria_first'].mo4_fit_twopoint
#sp_sch[sch_name].mo4_fit_twopoint=[320,275,alpha_1]
#sp_sch[sch_name].mo4_fit2     = np.polyfit(sp_sch[sch_name].df['mo4'],sp_sch[sch_name].df ['sat_scale2'],2)
#sp_sch[sch_name].mo4_dp= (dp**sp_sch[sch_name].mo4_fit_twopoint[2]-sp_sch[sch_name].mo4_fit_twopoint[0]**sp_sch[sch_name].mo4_fit_twopoint[2])/(sp_sch[sch_name].mo4_fit_twopoint[1]**sp_sch[sch_name].mo4_fit_twopoint[2]-sp_sch[sch_name].mo4_fit_twopoint[0]**sp_sch[sch_name].mo4_fit_twopoint[2])
#sp_sch[sch_name].mo4_text='y = (x$^{-7.1}$-265$^{-7.1}$)/(295$^{-7.1}$-265$^{-7.1}$)'
#
#sp_sch[sch_name].mo5_fit1     = np.polyfit(sp_sch[sch_name].df['mo5'],sp_sch[sch_name].df ['sat_scale2'],1)
#sp_sch[sch_name].mo5_fit1_str = 'y = '+"{0:0.3f}".format( sp_sch[sch_name].mo5_fit1[0]  ) + ' x ' + "{0:0.2f}".format( sp_sch[sch_name].mo5_fit1[1]  )
##sp_sch[sch_name].mo5_fit_twopoint=sp_sch['bacteria_first'].mo5_fit_twopoint
#sp_sch[sch_name].mo5_fit_twopoint=[300,265,alpha_1]
#sp_sch[sch_name].mo5_fit2     = np.polyfit(sp_sch[sch_name].df['mo5'],sp_sch[sch_name].df ['sat_scale2'],2)
#sp_sch[sch_name].mo5_dp= (dp**sp_sch[sch_name].mo5_fit_twopoint[2]-sp_sch[sch_name].mo5_fit_twopoint[0]**sp_sch[sch_name].mo5_fit_twopoint[2])/(sp_sch[sch_name].mo5_fit_twopoint[1]**sp_sch[sch_name].mo5_fit_twopoint[2]-sp_sch[sch_name].mo5_fit_twopoint[0]**sp_sch[sch_name].mo5_fit_twopoint[2])
#sp_sch[sch_name].mo5_text='y = (x$^{-7.1}$-260$^{-7.1}$)/(285$^{-7.1}$-260$^{-7.1}$)'
#
#sp_sch[sch_name].df['mmo0']=(sp_sch[sch_name].mo0_fit_twopoint[0]**sp_sch[sch_name].mo0_fit_twopoint[2]-sp_sch[sch_name].df['mo0']**sp_sch[sch_name].mo0_fit_twopoint[2])/(sp_sch[sch_name].mo0_fit_twopoint[0]**sp_sch[sch_name].mo0_fit_twopoint[2]-sp_sch[sch_name].mo0_fit_twopoint[1]**sp_sch[sch_name].mo0_fit_twopoint[2])
#sp_sch[sch_name].df['mmo1']=(sp_sch[sch_name].mo1_fit_twopoint[0]**sp_sch[sch_name].mo1_fit_twopoint[2]-sp_sch[sch_name].df['mo1']**sp_sch[sch_name].mo1_fit_twopoint[2])/(sp_sch[sch_name].mo1_fit_twopoint[0]**sp_sch[sch_name].mo1_fit_twopoint[2]-sp_sch[sch_name].mo1_fit_twopoint[1]**sp_sch[sch_name].mo1_fit_twopoint[2])
#sp_sch[sch_name].df['mmo2']=(sp_sch[sch_name].mo2_fit_twopoint[0]**sp_sch[sch_name].mo2_fit_twopoint[2]-sp_sch[sch_name].df['mo2']**sp_sch[sch_name].mo2_fit_twopoint[2])/(sp_sch[sch_name].mo2_fit_twopoint[0]**sp_sch[sch_name].mo2_fit_twopoint[2]-sp_sch[sch_name].mo2_fit_twopoint[1]**sp_sch[sch_name].mo2_fit_twopoint[2])
#sp_sch[sch_name].df['mmo3']=(sp_sch[sch_name].mo3_fit_twopoint[0]**sp_sch[sch_name].mo3_fit_twopoint[2]-sp_sch[sch_name].df['mo3']**sp_sch[sch_name].mo3_fit_twopoint[2])/(sp_sch[sch_name].mo3_fit_twopoint[0]**sp_sch[sch_name].mo3_fit_twopoint[2]-sp_sch[sch_name].mo3_fit_twopoint[1]**sp_sch[sch_name].mo3_fit_twopoint[2])
#sp_sch[sch_name].df['mmo4']=(sp_sch[sch_name].mo4_fit_twopoint[0]**sp_sch[sch_name].mo4_fit_twopoint[2]-sp_sch[sch_name].df['mo4']**sp_sch[sch_name].mo4_fit_twopoint[2])/(sp_sch[sch_name].mo4_fit_twopoint[0]**sp_sch[sch_name].mo4_fit_twopoint[2]-sp_sch[sch_name].mo4_fit_twopoint[1]**sp_sch[sch_name].mo4_fit_twopoint[2])
#sp_sch[sch_name].df['mmo5']=(sp_sch[sch_name].mo5_fit_twopoint[0]**sp_sch[sch_name].mo5_fit_twopoint[2]-sp_sch[sch_name].df['mo5']**sp_sch[sch_name].mo5_fit_twopoint[2])/(sp_sch[sch_name].mo5_fit_twopoint[0]**sp_sch[sch_name].mo5_fit_twopoint[2]-sp_sch[sch_name].mo5_fit_twopoint[1]**sp_sch[sch_name].mo5_fit_twopoint[2])


        #sp_sch[sch_name].merge_data(df=data_weather_daisy.df, keys=['ir_up']   ,plot=plot_interpolate  ,coef=5e-4)
        #sp_sch[sch_name].merge_data(df=data_weather_daisy.df, keys=['ir_down']   ,plot=plot_interpolate  ,coef=5e-4)
        #sp_sch[sch_name].merge_data(df=data_weather_daisy.df, keys=['rainmm']   ,plot=plot_interpolate  ,coef=5e-08)  # done
        
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


        #time_start=np.datetime64('2018-02-23T15:00')
        #time_end=np.datetime64('2018-03-02T15:00')
        #mask=data_weather_camellia.df['date_time'].between(time_start,time_end)
        #data_weather_camellia.df['rh_box_7'][mask]=np.nan


        #sp_sch[sch_name].merge_data(df=data_weather_camellia.df, keys=['rh']   ,plot=plot_interpolate  ,coef=5e-08)  # done
        #sp_sch[sch_name].merge_data(df=data_weather_camellia.df, keys=['rh_box_7'],plot=plot_interpolate  ,coef=5e-12)  # done
        #time_start=np.datetime64('2018-01-27T15:00')
        #time_end=np.datetime64('2018-01-30T10:00')
        ##https://stackoverflow.com/questions/31617845/how-to-select-rows-in-a-dataframe-between-two-values-in-python-pandas/31617974
        #mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
        #sp_sch[sch_name].df['rh'][mask]=np.nan #time_start=np.datetime64('2018-02-24T15:00')
        #time_end=np.datetime64('2018-03-01T15:00')
        #mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
        #sp_sch[sch_name].df['rh'][mask]=np.nan


        #sp_sch[sch_name].df['rh_box_7'][mask]=np.nan
        #sp_sch[sch_name].merge_data(df=data_weather_camellia.df, keys=['wdspdkphavg2m']   ,plot=plot_interpolate  ,coef=5e-08)  # done
        #time_start=np.datetime64('2018-02-24T00:00')
        #sp_sch[sch_name].df['wdspdkphavg2m'][mask]=np.nan
        #sp_sch[sch_name].df['wdspdkphavg2m'][ sp_sch[sch_name].df['wdspdkphavg2m']>12  ]=np.nan
        #sp_sch[sch_name].df['wdspdkphavg2m'][ sp_sch[sch_name].df['wdspdkphavg2m']<0  ]=np.nan

        #sp_sch[sch_name].merge_data(df=data_weather_camellia.df, keys=['wdgstkph10m']   ,plot=plot_interpolate  ,coef=5e-08)  # done
        #sp_sch[sch_name].df['wdgstkph10m'][ sp_sch[sch_name].df['wdgstkph10m']<0.  ]=np.nan



        #time_start=np.datetime64('2018-02-03T15:00')
        #time_end=np.datetime64('2018-02-05T15:00')
        #mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
        #sp_sch[sch_name].df['rh'][mask]=np.nan

        #time_start=np.datetime64('2018-03-02T15:00')
        #time_end=np.datetime64('2018-03-10T15:00')
        #mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
        #sp_sch[sch_name].df['tmp7'][mask]=np.nan
        #sp_sch[sch_name].df['tmp6'][mask]=np.nan
        #sp_sch[sch_name].df['tmp9'][mask]=np.nan


        #sp_sch[sch_name].merge_data(df=data_weather_daisy.df, keys=['tc']  ,plot=plot_interpolate  ,coef=5e-08)  # done
        #sp_sch[sch_name].merge_data(df=data_weather_daisy.df, keys=['tp_box_7'],plot=plot_interpolate  ,coef=5e-12)  # done
        #sp_sch[sch_name].df['tc'][ sp_sch[sch_name].df['tc']<9  ]=np.nan
        #sp_sch[sch_name].df['tp_box_7'][ sp_sch[sch_name].df['tp_box_7']<15 ]=np.nan



        #sp_sch[sch_name].merge_data(df=data_weather_daisy.df, keys=['p']   ,plot=plot_interpolate  ,coef=5e-08)  # done
        #sp_sch[sch_name].df['p'][sp_sch[sch_name].df['p'].values<88000]=np.nan
        #sp_sch[sch_name].merge_data(df=data.df, keys=['dhthum0'],plot=plot_interpolate  ,coef=5e-12)  # done

        #sp_sch[sch_name].merge_data(df=data_weather_daisy.df, keys=['rh']   ,plot=plot_interpolate  ,coef=5e-08)  # done



        #time_start=np.datetime64('2018-01-24T15:00')
        #time_end=np.datetime64('2018-02-03T15:00')
        ##https://stackoverflow.com/questions/31617845/how-to-select-rows-in-a-dataframe-between-two-values-in-python-pandas/31617974
        #mask=sp_sch[sch_name].df['date_time'].between(time_start,time_end)
        #sp_sch[sch_name].df['pre0'][mask]=np.nan
        #sp_sch[sch_name].df['pre1'][mask]=np.nan



