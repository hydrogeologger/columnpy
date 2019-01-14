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

#sp_sch={}
prof={}

plot_interpolate=False
for line in open("schedule.ipt"):
    li=line.strip()
    if not li.startswith("#"):
        line_content=[x.strip() for x in li.split(',')]
        sch_name=line_content[2]
        prof[sch_name]=pandas_scale.concat_data_roof(pd.datetime.strptime(line_content[0],'%Y/%b/%d %H:%M'),
            pd.datetime.strptime(line_content[1],'%Y/%b/%d %H:%M'),dt_s );
        #prof[sch_name].df.index=sp_sch[sch_name].df['date_time']

        prof[sch_name].start_dt=pd.datetime.strptime(line_content[0],'%Y/%b/%d %H:%M')
        prof[sch_name].end_dt=pd.datetime.strptime(line_content[1],'%Y/%b/%d %H:%M')

        #if sch_name=='grange_d':            
        ## applymap is the case to apply for all .
        #prof['grange_d_electrochem_o2']['data'].df= prof['grange_d_electrochem_o2']['data'].df.applymap(lambda x: float(x.strip('"') ) if type(x) is str else None)
        #prof['grange_d_type_moisture_suction']['data'].df=prof['grange_d_type_moisture_suction']['data'].df.drop(columns=['temp'])
        ##prof['grange_d_type_moisture_suction']['data'].df= prof['grange_d_type_moisture_suction']['data'].df.applymap(lambda x: 0 ) if x.isdigit() is False else None)
        #prof['grange_d_type_moisture_suction']['data'].df= prof['grange_d_type_moisture_suction']['data'].df.applymap(lambda x: float(x.strip('"') ) if type(x) is str else None)
      
        if sch_name=='grange_a':
            prof[sch_name].merge_data(df=data.df, keys=['dox0'],plot=plot_interpolate ,coef=5e-10)
            sp_sch[sch_name].merge_data(df=data.df, keys=['dox1'],plot=plot_interpolate ,coef=5e-10)
            sp_sch[sch_name].merge_data(df=data.df, keys=['dox2'],plot=plot_interpolate ,coef=5e-10)
            sp_sch[sch_name].merge_data(df=data.df, keys=['dox3'],plot=plot_interpolate ,coef=5e-10)
            sp_sch[sch_name].merge_data(df=data.df, keys=['dox6'],plot=plot_interpolate ,coef=5e-10)
            sp_sch[sch_name].merge_data(df=data.df, keys=['wluo6'],plot=plot_interpolate ,coef=5e-10)
            sp_sch[sch_name].merge_data(df=data.df, keys=['wluo5'],plot=plot_interpolate ,coef=5e-10)

            sp_sch[sch_name].merge_data(df=data.df, keys=['dtp6'],plot=plot_interpolate ,coef=5e-10)
            sp_sch[sch_name].merge_data(df=data.df, keys=['wlut6'],plot=plot_interpolate ,coef=5e-10)
            sp_sch[sch_name].merge_data(df=data.df, keys=['wlut5'],plot=plot_interpolate ,coef=5e-10)
            sp_sch[sch_name].merge_data(df=data.df, keys=['dtp3'],plot=plot_interpolate ,coef=5e-10)
            sp_sch[sch_name].merge_data(df=data.df, keys=['dtp2'],plot=plot_interpolate ,coef=5e-10)
            sp_sch[sch_name].merge_data(df=data.df, keys=['dtp1'],plot=plot_interpolate ,coef=5e-10)
            sp_sch[sch_name].merge_data(df=data.df, keys=['dtp0'],plot=plot_interpolate ,coef=5e-10)
            
            sp_sch[sch_name].merge_data(df=data.df, keys=['mo7'],plot=plot_interpolate ,coef=5e-10)
            sp_sch[sch_name].merge_data(df=data.df, keys=['mo6'],plot=plot_interpolate ,coef=5e-10)
            sp_sch[sch_name].merge_data(df=data.df, keys=['mo5'],plot=plot_interpolate ,coef=5e-10)
            sp_sch[sch_name].merge_data(df=data.df, keys=['mo4'],plot=plot_interpolate ,coef=5e-10)
            sp_sch[sch_name].merge_data(df=data.df, keys=['mo3'],plot=plot_interpolate ,coef=5e-10)
            sp_sch[sch_name].merge_data(df=data.df, keys=['mo2'],plot=plot_interpolate ,coef=5e-10)
            sp_sch[sch_name].merge_data(df=data.df, keys=['mo1'],plot=plot_interpolate ,coef=5e-10)
            sp_sch[sch_name].merge_data(df=data.df, keys=['mo0'],plot=plot_interpolate ,coef=5e-10)

            sp_sch[sch_name].df['mo7'].loc[sp_sch[sch_name].df['mo7']<=10]=np.nan
            sp_sch[sch_name].df['mo6'].loc[sp_sch[sch_name].df['mo7']<=10]=np.nan
            sp_sch[sch_name].df['mo5'].loc[sp_sch[sch_name].df['mo7']<=10]=np.nan
            sp_sch[sch_name].df['mo4'].loc[sp_sch[sch_name].df['mo7']<=10]=np.nan
            sp_sch[sch_name].df['mo3'].loc[sp_sch[sch_name].df['mo7']<=10]=np.nan
            sp_sch[sch_name].df['mo2'].loc[sp_sch[sch_name].df['mo7']<=10]=np.nan
            sp_sch[sch_name].df['mo1'].loc[sp_sch[sch_name].df['mo7']<=10]=np.nan
            sp_sch[sch_name].df['mo0'].loc[sp_sch[sch_name].df['mo7']<=10]=np.nan

            sp_sch[sch_name].df['mo7'].loc[sp_sch[sch_name].df['mo7']>=600]=np.nan
            sp_sch[sch_name].df['mo6'].loc[sp_sch[sch_name].df['mo7']>=600]=np.nan
            sp_sch[sch_name].df['mo5'].loc[sp_sch[sch_name].df['mo7']>=600]=np.nan
            sp_sch[sch_name].df['mo4'].loc[sp_sch[sch_name].df['mo7']>=600]=np.nan
            sp_sch[sch_name].df['mo3'].loc[sp_sch[sch_name].df['mo7']>=600]=np.nan
            sp_sch[sch_name].df['mo2'].loc[sp_sch[sch_name].df['mo7']>=600]=np.nan
            sp_sch[sch_name].df['mo1'].loc[sp_sch[sch_name].df['mo7']>=600]=np.nan
            sp_sch[sch_name].df['mo0'].loc[sp_sch[sch_name].df['mo7']>=600]=np.nan

            alpha_0=1.0
            sp_sch[sch_name].df['dox0_c'] = (sp_sch[sch_name].df['dox0']**alpha_0  -1.0**alpha_0)/(550.0**alpha_0-1.0**alpha_0)*21.
            sp_sch[sch_name].df['dox1_c'] = (sp_sch[sch_name].df['dox1']**alpha_0  -1.0**alpha_0)/(550.0**alpha_0-1.0**alpha_0)*21.
            sp_sch[sch_name].df['dox2_c'] = (sp_sch[sch_name].df['dox2']**alpha_0  -1.0**alpha_0)/(550.0**alpha_0-1.0**alpha_0)*21.
            sp_sch[sch_name].df['dox3_c'] = (sp_sch[sch_name].df['dox3']**alpha_0  -1.0**alpha_0)/(300.0**alpha_0-1.0**alpha_0)*21.
            sp_sch[sch_name].df['dox6_c'] = (sp_sch[sch_name].df['dox6']**alpha_0  -1.0**alpha_0)/(550.0**alpha_0-1.0**alpha_0)*21.
        
            alpha_mo=-5.0
            sp_sch[sch_name].df['mo0_c'] = -(sp_sch[sch_name].df['mo0']**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-350.**alpha_mo)
            sp_sch[sch_name].df['mo1_c'] = -(sp_sch[sch_name].df['mo1']**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-350.**alpha_mo)
            sp_sch[sch_name].df['mo2_c'] = -(sp_sch[sch_name].df['mo2']**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-350.**alpha_mo)
            sp_sch[sch_name].df['mo3_c'] = -(sp_sch[sch_name].df['mo3']**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-350.**alpha_mo)
            sp_sch[sch_name].df['mo4_c'] = -(sp_sch[sch_name].df['mo4']**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-350.**alpha_mo)
            sp_sch[sch_name].df['mo5_c'] = -(sp_sch[sch_name].df['mo5']**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-350.**alpha_mo)
            sp_sch[sch_name].df['mo6_c'] = -(sp_sch[sch_name].df['mo6']**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-350.**alpha_mo)
            sp_sch[sch_name].df['mo7_c'] = -(sp_sch[sch_name].df['mo7']**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-350.**alpha_mo)
        
        if sch_name=='grange_b':
            sp_sch[sch_name].merge_data(df=data.df, keys=['dox0'],plot=plot_interpolate ,coef=5e-10)
            sp_sch[sch_name].merge_data(df=data.df, keys=['dox1'],plot=plot_interpolate ,coef=5e-10)
            sp_sch[sch_name].merge_data(df=data.df, keys=['dox3'],plot=plot_interpolate ,coef=5e-10)
            sp_sch[sch_name].merge_data(df=data.df, keys=['dox5'],plot=plot_interpolate ,coef=5e-10)
            sp_sch[sch_name].merge_data(df=data.df, keys=['dox6'],plot=plot_interpolate ,coef=5e-10)
            sp_sch[sch_name].merge_data(df=data.df, keys=['dox7'],plot=plot_interpolate ,coef=5e-10)
            sp_sch[sch_name].merge_data(df=data.df, keys=['dox6'],plot=plot_interpolate ,coef=5e-10)

            sp_sch[sch_name].merge_data(df=data.df, keys=['dluo4'],plot=plot_interpolate ,coef=5e-10)
            sp_sch[sch_name].merge_data(df=data.df, keys=['dluo2'],plot=plot_interpolate ,coef=5e-10)

            sp_sch[sch_name].merge_data(df=data.df, keys=['dtp7'],plot=plot_interpolate ,coef=5e-10)
            sp_sch[sch_name].merge_data(df=data.df, keys=['dlut4'],plot=plot_interpolate ,coef=5e-10)
            sp_sch[sch_name].merge_data(df=data.df, keys=['dlut2'],plot=plot_interpolate ,coef=5e-10)
            sp_sch[sch_name].merge_data(df=data.df, keys=['dtp6'],plot=plot_interpolate ,coef=5e-10)
            sp_sch[sch_name].merge_data(df=data.df, keys=['dtp5'],plot=plot_interpolate ,coef=5e-10)
            sp_sch[sch_name].merge_data(df=data.df, keys=['dtp1'],plot=plot_interpolate ,coef=5e-10)
            sp_sch[sch_name].merge_data(df=data.df, keys=['dtp0'],plot=plot_interpolate ,coef=5e-10)

            sp_sch[sch_name].merge_data(df=data.df, keys=['mo7'],plot=plot_interpolate ,coef=5e-10)
            sp_sch[sch_name].merge_data(df=data.df, keys=['mo6'],plot=plot_interpolate ,coef=5e-10)
            sp_sch[sch_name].merge_data(df=data.df, keys=['mo5'],plot=plot_interpolate ,coef=5e-10)
            sp_sch[sch_name].merge_data(df=data.df, keys=['mo4'],plot=plot_interpolate ,coef=5e-10)
            sp_sch[sch_name].merge_data(df=data.df, keys=['mo3'],plot=plot_interpolate ,coef=5e-10)
            sp_sch[sch_name].merge_data(df=data.df, keys=['mo2'],plot=plot_interpolate ,coef=5e-10)
            sp_sch[sch_name].merge_data(df=data.df, keys=['mo1'],plot=plot_interpolate ,coef=5e-10)
            sp_sch[sch_name].merge_data(df=data.df, keys=['mo0'],plot=plot_interpolate ,coef=5e-10)

            sp_sch[sch_name].df['mo7'].loc[sp_sch[sch_name].df['mo7']<=10]=np.nan
            sp_sch[sch_name].df['mo6'].loc[sp_sch[sch_name].df['mo7']<=10]=np.nan
            sp_sch[sch_name].df['mo5'].loc[sp_sch[sch_name].df['mo7']<=10]=np.nan
            sp_sch[sch_name].df['mo4'].loc[sp_sch[sch_name].df['mo7']<=10]=np.nan
            sp_sch[sch_name].df['mo3'].loc[sp_sch[sch_name].df['mo7']<=10]=np.nan
            sp_sch[sch_name].df['mo2'].loc[sp_sch[sch_name].df['mo7']<=10]=np.nan
            sp_sch[sch_name].df['mo1'].loc[sp_sch[sch_name].df['mo7']<=10]=np.nan
            sp_sch[sch_name].df['mo0'].loc[sp_sch[sch_name].df['mo7']<=10]=np.nan

            sp_sch[sch_name].df['mo7'].loc[sp_sch[sch_name].df['mo7']>=600]=np.nan
            sp_sch[sch_name].df['mo6'].loc[sp_sch[sch_name].df['mo7']>=600]=np.nan
            sp_sch[sch_name].df['mo5'].loc[sp_sch[sch_name].df['mo7']>=600]=np.nan
            sp_sch[sch_name].df['mo4'].loc[sp_sch[sch_name].df['mo7']>=600]=np.nan
            sp_sch[sch_name].df['mo3'].loc[sp_sch[sch_name].df['mo7']>=600]=np.nan
            sp_sch[sch_name].df['mo2'].loc[sp_sch[sch_name].df['mo7']>=600]=np.nan
            sp_sch[sch_name].df['mo1'].loc[sp_sch[sch_name].df['mo7']>=600]=np.nan
            sp_sch[sch_name].df['mo0'].loc[sp_sch[sch_name].df['mo7']>=600]=np.nan
        
            alpha_0=1.0
            sp_sch[sch_name].df['dox0_c'] = (sp_sch[sch_name].df['dox0']**alpha_0  -1.0**alpha_0)/(550.0**alpha_0-1.0**alpha_0)*21.
            sp_sch[sch_name].df['dox1_c'] = (sp_sch[sch_name].df['dox1']**alpha_0  -1.0**alpha_0)/(550.0**alpha_0-1.0**alpha_0)*21.
            sp_sch[sch_name].df['dox2_c'] = (sp_sch[sch_name].df['dox2']**alpha_0  -1.0**alpha_0)/(550.0**alpha_0-1.0**alpha_0)*21.
            sp_sch[sch_name].df['dox3_c'] = (sp_sch[sch_name].df['dox3']**alpha_0  -1.0**alpha_0)/(300.0**alpha_0-1.0**alpha_0)*21.
            sp_sch[sch_name].df['dox6_c'] = (sp_sch[sch_name].df['dox6']**alpha_0  -1.0**alpha_0)/(550.0**alpha_0-1.0**alpha_0)*21.

            alpha_mo=-5.0
            sp_sch[sch_name].df['mo0_c'] = -(sp_sch[sch_name].df['mo0']**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-350.**alpha_mo)
            sp_sch[sch_name].df['mo1_c'] = -(sp_sch[sch_name].df['mo1']**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-350.**alpha_mo)
            sp_sch[sch_name].df['mo2_c'] = -(sp_sch[sch_name].df['mo2']**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-350.**alpha_mo)
            sp_sch[sch_name].df['mo3_c'] = -(sp_sch[sch_name].df['mo3']**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-350.**alpha_mo)
            sp_sch[sch_name].df['mo4_c'] = -(sp_sch[sch_name].df['mo4']**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-350.**alpha_mo)
            sp_sch[sch_name].df['mo5_c'] = -(sp_sch[sch_name].df['mo5']**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-350.**alpha_mo)
            sp_sch[sch_name].df['mo6_c'] = -(sp_sch[sch_name].df['mo6']**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-350.**alpha_mo)
            sp_sch[sch_name].df['mo7_c'] = -(sp_sch[sch_name].df['mo7']**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-350.**alpha_mo)

            
        prof['grange_a_moisture_suction']['data'].df['mo7'].loc [   prof['grange_a_moisture_suction']['data'].df['mo7'] <=10] =np.nan
        prof['grange_a_moisture_suction']['data'].df['mo6'].loc [   prof['grange_a_moisture_suction']['data'].df['mo6'] <=10] =np.nan
        prof['grange_a_moisture_suction']['data'].df['mo5'].loc [   prof['grange_a_moisture_suction']['data'].df['mo5'] <=10] =np.nan
        prof['grange_a_moisture_suction']['data'].df['mo4'].loc [   prof['grange_a_moisture_suction']['data'].df['mo4'] <=10] =np.nan
        prof['grange_a_moisture_suction']['data'].df['mo3'].loc [   prof['grange_a_moisture_suction']['data'].df['mo3'] <=10] =np.nan
        prof['grange_a_moisture_suction']['data'].df['mo2'].loc [   prof['grange_a_moisture_suction']['data'].df['mo2'] <=10] =np.nan
        prof['grange_a_moisture_suction']['data'].df['mo1'].loc [   prof['grange_a_moisture_suction']['data'].df['mo1'] <=10] =np.nan
        prof['grange_a_moisture_suction']['data'].df['mo0'].loc [   prof['grange_a_moisture_suction']['data'].df['mo0'] <=10] =np.nan
        
        prof['grange_a_moisture_suction']['data'].df['mo7'].loc [   prof['grange_a_moisture_suction']['data'].df['mo7'] >=600] =np.nan
        prof['grange_a_moisture_suction']['data'].df['mo6'].loc [   prof['grange_a_moisture_suction']['data'].df['mo6'] >=600] =np.nan
        prof['grange_a_moisture_suction']['data'].df['mo5'].loc [   prof['grange_a_moisture_suction']['data'].df['mo5'] >=600] =np.nan
        prof['grange_a_moisture_suction']['data'].df['mo4'].loc [   prof['grange_a_moisture_suction']['data'].df['mo4'] >=600] =np.nan
        prof['grange_a_moisture_suction']['data'].df['mo3'].loc [   prof['grange_a_moisture_suction']['data'].df['mo3'] >=600] =np.nan
        prof['grange_a_moisture_suction']['data'].df['mo2'].loc [   prof['grange_a_moisture_suction']['data'].df['mo2'] >=600] =np.nan
        prof['grange_a_moisture_suction']['data'].df['mo1'].loc [   prof['grange_a_moisture_suction']['data'].df['mo1'] >=600] =np.nan
        prof['grange_a_moisture_suction']['data'].df['mo0'].loc [   prof['grange_a_moisture_suction']['data'].df['mo0'] >=600] =np.nan
        
        prof['grange_d_type_moisture_suction']['data'].df['mo7'].loc [   prof['grange_d_type_moisture_suction']['data'].df['mo7'] <=10] =np.nan
        prof['grange_d_type_moisture_suction']['data'].df['mo6'].loc [   prof['grange_d_type_moisture_suction']['data'].df['mo6'] <=10] =np.nan
        prof['grange_d_type_moisture_suction']['data'].df['mo5'].loc [   prof['grange_d_type_moisture_suction']['data'].df['mo5'] <=10] =np.nan
        prof['grange_d_type_moisture_suction']['data'].df['mo4'].loc [   prof['grange_d_type_moisture_suction']['data'].df['mo4'] <=10] =np.nan
        prof['grange_d_type_moisture_suction']['data'].df['mo3'].loc [   prof['grange_d_type_moisture_suction']['data'].df['mo3'] <=10] =np.nan
        prof['grange_d_type_moisture_suction']['data'].df['mo2'].loc [   prof['grange_d_type_moisture_suction']['data'].df['mo2'] <=10] =np.nan
        prof['grange_d_type_moisture_suction']['data'].df['mo1'].loc [   prof['grange_d_type_moisture_suction']['data'].df['mo1'] <=10] =np.nan
        prof['grange_d_type_moisture_suction']['data'].df['mo0'].loc [   prof['grange_d_type_moisture_suction']['data'].df['mo0'] <=10] =np.nan
        
        prof['grange_5_mo_su']['data'].df=prof['grange_5_mo_su']['data'].df[pd.Timestamp('2018-2-06 21:50:53.445'):]
        prof['grange_5_mo_su']['data'].df['mo7'].loc [   prof['grange_5_mo_su']['data'].df['mo7'] <=10] =np.nan
        prof['grange_5_mo_su']['data'].df['mo6'].loc [   prof['grange_5_mo_su']['data'].df['mo6'] <=10] =np.nan
        prof['grange_5_mo_su']['data'].df['mo5'].loc [   prof['grange_5_mo_su']['data'].df['mo5'] <=10] =np.nan
        prof['grange_5_mo_su']['data'].df['mo4'].loc [   prof['grange_5_mo_su']['data'].df['mo4'] <=10] =np.nan
        prof['grange_5_mo_su']['data'].df['mo3'].loc [   prof['grange_5_mo_su']['data'].df['mo3'] <=10] =np.nan
        prof['grange_5_mo_su']['data'].df['mo2'].loc [   prof['grange_5_mo_su']['data'].df['mo2'] <=10] =np.nan
        prof['grange_5_mo_su']['data'].df['mo1'].loc [   prof['grange_5_mo_su']['data'].df['mo1'] <=10] =np.nan
        prof['grange_5_mo_su']['data'].df['mo0'].loc [   prof['grange_5_mo_su']['data'].df['mo0'] <=10] =np.nan
        
        prof['grange_3_mo_su']['data'].df=prof['grange_3_mo_su']['data'].df[pd.Timestamp('2018-2-06 21:50:53.445'):]
        prof['grange_4_mo_su']['data'].df=prof['grange_4_mo_su']['data'].df[pd.Timestamp('2018-2-06 21:50:53.445'):]
        sp=prof['grange_b_electrochem_o2']['data'].df
        sp['dox0_c'] = (sp.dox0**alpha_0  -1.0**alpha_0)/(450.0**alpha_0-1.0**alpha_0)*21.
        sp['dox1_c'] = (sp.dox1**alpha_0  -1.0**alpha_0)/(420.0**alpha_0-1.0**alpha_0)*21.
        #sp['dox2_c'] = (sp.dox2**alpha_0  -1.0**alpha_0)/(550.0**alpha_0-1.0**alpha_0)*21.
        sp['dox3_c'] = (sp.dox3**alpha_0  -1.0**alpha_0)/(550.0**alpha_0-1.0**alpha_0)*21.
        #sp['dox4_c'] = (sp.dox4**alpha_0  -1.0**alpha_0)/(550.0**alpha_0-1.0**alpha_0)*21.
        sp['dox5_c'] = (sp.dox5**alpha_0  -1.0**alpha_0)/(450.0**alpha_0-1.0**alpha_0)*21.
        sp['dox6_c'] = (sp.dox6**alpha_0  -1.0**alpha_0)/(450.0**alpha_0-1.0**alpha_0)*21.
        sp['dox7_c'] = (sp.dox7**alpha_0  -1.0**alpha_0)/(550.0**alpha_0-1.0**alpha_0)*21.
        
        
        sp=prof['grange_d_electrochem_o2']['data'].df
        #  https://stackoverflow.com/questions/22847304/exception-handling-in-pandas-apply-function
        # below does not update the result
        #sp['dox0'].apply(lambda x: float(x.strip('"') ) if type(x) is str else None) 
        # this is the best
        #sp['dox0']= sp['dox0'].apply(lambda x: float(x.strip('"') ) if type(x) is str else None) 
        #sp= sp.applymap(lambda x: float(x.strip('"') ) if type(x) is str else None) 
        
        #sp.assign('dox0'=lambda x: float(x.strip('"') ) if type(x) is str else None)
        
        #only after this time is used as before that, the data was shown as string
        #sp=prof['grange_d_electrochem_o2']['data'].df[pd.Timestamp('2017-12-13 21:50:53.445'):]
        #2017-12-13 21:29
        #sp.ix[sp.index.indexer_between_time(pd.timestamp('2017-12-13 14:03:00') ,pd.timestamp('2017-12-13 21:03:00')) ] ,  datetime.datetime(2017,12,13,21,30))]
        #sp.ix[ sp[:pd.Timestamp('2018-1-13 14:50:53.445')] ]
        #sp=sp[pd.Timestamp('2017-12-13 21:50:53.445'):]
        sp['dox0_c'] = (sp.dox0**alpha_0  -1.0**alpha_0)/(450.0**alpha_0-1.0**alpha_0)*21.
        sp['dox1_c'] = (sp.dox1**alpha_0  -1.0**alpha_0)/(420.0**alpha_0-1.0**alpha_0)*21.
        sp['dox2_c'] = (sp.dox2**alpha_0  -1.0**alpha_0)/(550.0**alpha_0-1.0**alpha_0)*21.
        sp['dox3_c'] = (sp.dox3**alpha_0  -1.0**alpha_0)/(550.0**alpha_0-1.0**alpha_0)*21.
        sp['dox4_c'] = (sp.dox4**alpha_0  -1.0**alpha_0)/(550.0**alpha_0-1.0**alpha_0)*21.
        #sp['dox5_c'] = (sp.dox5**alpha_0  -1.0**alpha_0)/(450.0**alpha_0-1.0**alpha_0)*21.
        sp['dox6_c'] = (sp.dox6**alpha_0  -1.0**alpha_0)/(450.0**alpha_0-1.0**alpha_0)*21.
        #sp['dox7_c'] = (sp.dox7**alpha_0  -1.0**alpha_0)/(550.0**alpha_0-1.0**alpha_0)*21.
        
        
        prof['grange_b_luo2']['data'].df['dluo2'].loc [   prof['grange_b_luo2']['data'].df['dluo2'] <=0.0] =np.nan
        prof['grange_b_luo2']['data'].df['dluo4'].loc [   prof['grange_b_luo2']['data'].df['dluo4'] <=0.0] =np.nan
        
        
        prof['grange_3_luo2_dry']['data'].df['dluo0'].loc[ prof['grange_3_luo2_dry']['data'].df['dluo0']<=0 ] =np.nan
        prof['grange_3_luo2_dry']['data'].df['dluo0'].loc[ prof['grange_3_luo2_dry']['data'].df['dluo0']<=0 ] =np.nan
        
        prof['grange_3_mo_su']['data'].df['dluo7'].loc[prof['grange_3_mo_su']['data'].df['dluo7']<=0.0] =np.nan
        prof['grange_3_mo_su']['data'].df['tmp7'].loc[prof['grange_3_mo_su']['data'].df['tmp7']<=0.0] =np.nan
        prof['grange_4_mo_su']['data'].df['tmp7'].loc[prof['grange_4_mo_su']['data'].df['tmp7']<=0.0] =np.nan
        prof['grange_5_mo_su']['data'].df['tmp7'].loc[prof['grange_5_mo_su']['data'].df['tmp7']<=0.0] =np.nan
        
        
        prof['grange_d_electrochem_o2']['data'].df['dtp4'].loc[ prof['grange_d_electrochem_o2']['data'].df['dtp4'] <=0 ] =np.nan
        
        
        prof['grange_5_luo2_dry']['data'].df['dluo0'].loc[ prof['grange_5_luo2_dry']['data'].df['dluo0']<=0 ] =np.nan
        prof['grange_5_luo2_dry']['data'].df['dluo1'].loc[ prof['grange_5_luo2_dry']['data'].df['dluo1']<=0 ] =np.nan
        prof['grange_5_luo2_dry']['data'].df['dluo2'].loc[ prof['grange_5_luo2_dry']['data'].df['dluo2']<=0 ] =np.nan
        prof['grange_5_luo2_dry']['data'].df['dluo3'].loc[ prof['grange_5_luo2_dry']['data'].df['dluo3']<=0 ] =np.nan
        prof['grange_5_luo2_dry']['data'].df['dluo4'].loc[ prof['grange_5_luo2_dry']['data'].df['dluo4']<=0 ] =np.nan
        prof['grange_5_luo2_dry']['data'].df['dluo5'].loc[ prof['grange_5_luo2_dry']['data'].df['dluo5']<=0 ] =np.nan
        prof['grange_5_luo2_dry']['data'].df['dluo6'].loc[ prof['grange_5_luo2_dry']['data'].df['dluo6']<=0 ] =np.nan
        
        prof['grange_5_mo_su']['data'].df['dluo7'].loc[prof['grange_5_mo_su']['data'].df['dluo7']<=0.0] =np.nan
        
        
        
        
        alpha_mo=-5.0
        sp=prof['grange_a_moisture_suction']['data'].df
        sp['mo0_c'] = -(sp.mo0**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-350.**alpha_mo)
        sp['mo1_c'] = -(sp.mo1**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-350.**alpha_mo)
        sp['mo2_c'] = -(sp.mo2**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-350.**alpha_mo)
        sp['mo3_c'] = -(sp.mo3**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-350.**alpha_mo)
        sp['mo4_c'] = -(sp.mo4**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-350.**alpha_mo)
        sp['mo5_c'] = -(sp.mo5**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-350.**alpha_mo)
        sp['mo6_c'] = -(sp.mo6**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-350.**alpha_mo)
        sp['mo7_c'] = -(sp.mo7**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-350.**alpha_mo)
        
        sp=prof['grange_b_moisture_suction']['data'].df
        sp['mo0_c'] = -(sp.mo0**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-330.**alpha_mo)
        sp['mo1_c'] = -(sp.mo1**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-330.**alpha_mo)
        sp['mo2_c'] = -(sp.mo2**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-330.**alpha_mo)
        sp['mo3_c'] = -(sp.mo3**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-330.**alpha_mo)
        sp['mo4_c'] = -(sp.mo4**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-330.**alpha_mo)
        sp['mo5_c'] = -(sp.mo5**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-330.**alpha_mo)
        sp['mo6_c'] = -(sp.mo6**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-330.**alpha_mo)
        sp['mo7_c'] = -(sp.mo7**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-330.**alpha_mo)
        
        sp=prof['grange_d_type_moisture_suction']['data'].df
        sp['mo0_c'] = -(sp.mo0**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-350.**alpha_mo)
        sp['mo1_c'] = -(sp.mo1**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-350.**alpha_mo)
        sp['mo2_c'] = -(sp.mo2**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-350.**alpha_mo)
        sp['mo3_c'] = -(sp.mo3**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-350.**alpha_mo)
        sp['mo4_c'] = -(sp.mo4**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-350.**alpha_mo)
        sp['mo5_c'] = -(sp.mo5**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-350.**alpha_mo)
        sp['mo6_c'] = -(sp.mo6**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-350.**alpha_mo)
        sp['mo7_c'] = -(sp.mo7**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-350.**alpha_mo)
        
        
        sp=prof['grange_3_mo_su']['data'].df
        sp['mo0_c'] = -(sp.mo0**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-297.**alpha_mo)
        sp['mo1_c'] = -(sp.mo1**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-297.**alpha_mo)
        sp['mo2_c'] = -(sp.mo2**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-297.**alpha_mo)
        sp['mo3_c'] = -(sp.mo3**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-297.**alpha_mo)
        sp['mo4_c'] = -(sp.mo4**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-297.**alpha_mo)
        sp['mo5_c'] = -(sp.mo5**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-297.**alpha_mo)
        sp['mo6_c'] = -(sp.mo6**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-297.**alpha_mo)
        sp['mo7_c'] = -(sp.mo7**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-297.**alpha_mo)
        
        sp=prof['grange_4_mo_su']['data'].df
        sp['mo0_c'] = -(sp.mo0**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-297.**alpha_mo)
        sp['mo1_c'] = -(sp.mo1**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-297.**alpha_mo)
        sp['mo2_c'] = -(sp.mo2**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-297.**alpha_mo)
        sp['mo3_c'] = -(sp.mo3**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-297.**alpha_mo)
        sp['mo4_c'] = -(sp.mo4**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-297.**alpha_mo)
        sp['mo5_c'] = -(sp.mo5**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-297.**alpha_mo)
        sp['mo6_c'] = -(sp.mo6**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-297.**alpha_mo)
        sp['mo7_c'] = -(sp.mo7**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-297.**alpha_mo)
        
        sp=prof['grange_5_mo_su']['data'].df
        sp['mo0_c'] = -(sp.mo0**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-297.**alpha_mo)
        sp['mo1_c'] = -(sp.mo1**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-297.**alpha_mo)
        sp['mo2_c'] = -(sp.mo2**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-297.**alpha_mo)
        sp['mo3_c'] = -(sp.mo3**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-297.**alpha_mo)
        sp['mo4_c'] = -(sp.mo4**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-297.**alpha_mo)
        sp['mo5_c'] = -(sp.mo5**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-297.**alpha_mo)
        sp['mo6_c'] = -(sp.mo6**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-297.**alpha_mo)
        sp['mo7_c'] = -(sp.mo7**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-297.**alpha_mo)

