
prof['compacted_redmud']['data'].df['2896_begin_97'].loc[prof['compacted_redmud']['data'].df['2896_begin_97']<10]=np.nan
prof['compacted_redmud']['data'].df['2896_peak_117'].loc[prof['compacted_redmud']['data'].df['2896_peak_117']<10]=np.nan
prof['compacted_redmud']['data'].df['2896_end_139'].loc[prof['compacted_redmud']['data'].df['2896_end_139']<10]=np.nan
prof['compacted_redmud']['data'].df['2896_deltat_heat']=prof['compacted_redmud']['data'].df['2896_peak_117']-prof['compacted_redmud']['data'].df['2896_begin_97']
prof['compacted_redmud']['data'].df['2870_begin_51'].loc[prof['compacted_redmud']['data'].df['2870_begin_51']<10]=np.nan
prof['compacted_redmud']['data'].df['2870_peak_71'].loc[prof['compacted_redmud']['data'].df['2870_peak_71']<10]=np.nan
prof['compacted_redmud']['data'].df['2870_end_91'].loc[prof['compacted_redmud']['data'].df['2870_end_91']<10]=np.nan
prof['compacted_redmud']['data'].df['2870_deltat_heat']=prof['compacted_redmud']['data'].df['2870_peak_71']-prof['compacted_redmud']['data'].df['2870_begin_51']

## applymap is the case to apply for all .
#prof['grange_d_electrochem_o2']['data'].df= prof['grange_d_electrochem_o2']['data'].df.applymap(lambda x: float(x.strip('"') ) if type(x) is str else None)
#prof['grange_d_type_moisture_suction']['data'].df=prof['grange_d_type_moisture_suction']['data'].df.drop(columns=['temp'])
##prof['grange_d_type_moisture_suction']['data'].df= prof['grange_d_type_moisture_suction']['data'].df.applymap(lambda x: 0 ) if x.isdigit() is False else None)
#prof['grange_d_type_moisture_suction']['data'].df= prof['grange_d_type_moisture_suction']['data'].df.applymap(lambda x: float(x.strip('"') ) if type(x) is str else None)
#
#
#
#sp=prof['grange_a_electrochem_o2']['data'].df
#alpha_0=1.0
#sp['dox0_c'] = (sp.dox0**alpha_0  -1.0**alpha_0)/(550.0**alpha_0-1.0**alpha_0)*21.
#sp['dox1_c'] = (sp.dox1**alpha_0  -1.0**alpha_0)/(550.0**alpha_0-1.0**alpha_0)*21.
#sp['dox2_c'] = (sp.dox2**alpha_0  -1.0**alpha_0)/(550.0**alpha_0-1.0**alpha_0)*21.
#sp['dox3_c'] = (sp.dox3**alpha_0  -1.0**alpha_0)/(300.0**alpha_0-1.0**alpha_0)*21.
##sp['dox4_c'] = (sp.dox4**alpha_0  -1.0**alpha_0)/(550.0**alpha_0-1.0**alpha_0)
#sp['dox6_c'] = (sp.dox6**alpha_0  -1.0**alpha_0)/(550.0**alpha_0-1.0**alpha_0)*21.
#
#
#
#prof['grange_a_moisture_suction']['data'].df['mo7'].loc [   prof['grange_a_moisture_suction']['data'].df['mo7'] <=10] =np.nan
#prof['grange_a_moisture_suction']['data'].df['mo6'].loc [   prof['grange_a_moisture_suction']['data'].df['mo6'] <=10] =np.nan
#prof['grange_a_moisture_suction']['data'].df['mo5'].loc [   prof['grange_a_moisture_suction']['data'].df['mo5'] <=10] =np.nan
#prof['grange_a_moisture_suction']['data'].df['mo4'].loc [   prof['grange_a_moisture_suction']['data'].df['mo4'] <=10] =np.nan
#prof['grange_a_moisture_suction']['data'].df['mo3'].loc [   prof['grange_a_moisture_suction']['data'].df['mo3'] <=10] =np.nan
#prof['grange_a_moisture_suction']['data'].df['mo2'].loc [   prof['grange_a_moisture_suction']['data'].df['mo2'] <=10] =np.nan
#prof['grange_a_moisture_suction']['data'].df['mo1'].loc [   prof['grange_a_moisture_suction']['data'].df['mo1'] <=10] =np.nan
#prof['grange_a_moisture_suction']['data'].df['mo0'].loc [   prof['grange_a_moisture_suction']['data'].df['mo0'] <=10] =np.nan
#
#prof['grange_a_moisture_suction']['data'].df['mo7'].loc [   prof['grange_a_moisture_suction']['data'].df['mo7'] >=600] =np.nan
#prof['grange_a_moisture_suction']['data'].df['mo6'].loc [   prof['grange_a_moisture_suction']['data'].df['mo6'] >=600] =np.nan
#prof['grange_a_moisture_suction']['data'].df['mo5'].loc [   prof['grange_a_moisture_suction']['data'].df['mo5'] >=600] =np.nan
#prof['grange_a_moisture_suction']['data'].df['mo4'].loc [   prof['grange_a_moisture_suction']['data'].df['mo4'] >=600] =np.nan
#prof['grange_a_moisture_suction']['data'].df['mo3'].loc [   prof['grange_a_moisture_suction']['data'].df['mo3'] >=600] =np.nan
#prof['grange_a_moisture_suction']['data'].df['mo2'].loc [   prof['grange_a_moisture_suction']['data'].df['mo2'] >=600] =np.nan
#prof['grange_a_moisture_suction']['data'].df['mo1'].loc [   prof['grange_a_moisture_suction']['data'].df['mo1'] >=600] =np.nan
#prof['grange_a_moisture_suction']['data'].df['mo0'].loc [   prof['grange_a_moisture_suction']['data'].df['mo0'] >=600] =np.nan
#
#prof['grange_d_type_moisture_suction']['data'].df['mo7'].loc [   prof['grange_d_type_moisture_suction']['data'].df['mo7'] <=10] =np.nan
#prof['grange_d_type_moisture_suction']['data'].df['mo6'].loc [   prof['grange_d_type_moisture_suction']['data'].df['mo6'] <=10] =np.nan
#prof['grange_d_type_moisture_suction']['data'].df['mo5'].loc [   prof['grange_d_type_moisture_suction']['data'].df['mo5'] <=10] =np.nan
#prof['grange_d_type_moisture_suction']['data'].df['mo4'].loc [   prof['grange_d_type_moisture_suction']['data'].df['mo4'] <=10] =np.nan
#prof['grange_d_type_moisture_suction']['data'].df['mo3'].loc [   prof['grange_d_type_moisture_suction']['data'].df['mo3'] <=10] =np.nan
#prof['grange_d_type_moisture_suction']['data'].df['mo2'].loc [   prof['grange_d_type_moisture_suction']['data'].df['mo2'] <=10] =np.nan
#prof['grange_d_type_moisture_suction']['data'].df['mo1'].loc [   prof['grange_d_type_moisture_suction']['data'].df['mo1'] <=10] =np.nan
#prof['grange_d_type_moisture_suction']['data'].df['mo0'].loc [   prof['grange_d_type_moisture_suction']['data'].df['mo0'] <=10] =np.nan
#
#prof['grange_5_mo_su']['data'].df=prof['grange_5_mo_su']['data'].df[pd.Timestamp('2018-2-06 21:50:53.445'):]
#prof['grange_5_mo_su']['data'].df['mo7'].loc [   prof['grange_5_mo_su']['data'].df['mo7'] <=10] =np.nan
#prof['grange_5_mo_su']['data'].df['mo6'].loc [   prof['grange_5_mo_su']['data'].df['mo6'] <=10] =np.nan
#prof['grange_5_mo_su']['data'].df['mo5'].loc [   prof['grange_5_mo_su']['data'].df['mo5'] <=10] =np.nan
#prof['grange_5_mo_su']['data'].df['mo4'].loc [   prof['grange_5_mo_su']['data'].df['mo4'] <=10] =np.nan
#prof['grange_5_mo_su']['data'].df['mo3'].loc [   prof['grange_5_mo_su']['data'].df['mo3'] <=10] =np.nan
#prof['grange_5_mo_su']['data'].df['mo2'].loc [   prof['grange_5_mo_su']['data'].df['mo2'] <=10] =np.nan
#prof['grange_5_mo_su']['data'].df['mo1'].loc [   prof['grange_5_mo_su']['data'].df['mo1'] <=10] =np.nan
#prof['grange_5_mo_su']['data'].df['mo0'].loc [   prof['grange_5_mo_su']['data'].df['mo0'] <=10] =np.nan
#
#prof['grange_3_mo_su']['data'].df=prof['grange_3_mo_su']['data'].df[pd.Timestamp('2018-2-06 21:50:53.445'):]
#prof['grange_4_mo_su']['data'].df=prof['grange_4_mo_su']['data'].df[pd.Timestamp('2018-2-06 21:50:53.445'):]
#sp=prof['grange_b_electrochem_o2']['data'].df
#sp['dox0_c'] = (sp.dox0**alpha_0  -1.0**alpha_0)/(450.0**alpha_0-1.0**alpha_0)*21.
#sp['dox1_c'] = (sp.dox1**alpha_0  -1.0**alpha_0)/(420.0**alpha_0-1.0**alpha_0)*21.
##sp['dox2_c'] = (sp.dox2**alpha_0  -1.0**alpha_0)/(550.0**alpha_0-1.0**alpha_0)*21.
#sp['dox3_c'] = (sp.dox3**alpha_0  -1.0**alpha_0)/(550.0**alpha_0-1.0**alpha_0)*21.
##sp['dox4_c'] = (sp.dox4**alpha_0  -1.0**alpha_0)/(550.0**alpha_0-1.0**alpha_0)*21.
#sp['dox5_c'] = (sp.dox5**alpha_0  -1.0**alpha_0)/(450.0**alpha_0-1.0**alpha_0)*21.
#sp['dox6_c'] = (sp.dox6**alpha_0  -1.0**alpha_0)/(450.0**alpha_0-1.0**alpha_0)*21.
#sp['dox7_c'] = (sp.dox7**alpha_0  -1.0**alpha_0)/(550.0**alpha_0-1.0**alpha_0)*21.
#
#
#sp=prof['grange_d_electrochem_o2']['data'].df
##  https://stackoverflow.com/questions/22847304/exception-handling-in-pandas-apply-function
## below does not update the result
##sp['dox0'].apply(lambda x: float(x.strip('"') ) if type(x) is str else None) 
## this is the best
##sp['dox0']= sp['dox0'].apply(lambda x: float(x.strip('"') ) if type(x) is str else None) 
##sp= sp.applymap(lambda x: float(x.strip('"') ) if type(x) is str else None) 
#
##sp.assign('dox0'=lambda x: float(x.strip('"') ) if type(x) is str else None)
#
##only after this time is used as before that, the data was shown as string
##sp=prof['grange_d_electrochem_o2']['data'].df[pd.Timestamp('2017-12-13 21:50:53.445'):]
##2017-12-13 21:29
##sp.ix[sp.index.indexer_between_time(pd.timestamp('2017-12-13 14:03:00') ,pd.timestamp('2017-12-13 21:03:00')) ] ,  datetime.datetime(2017,12,13,21,30))]
##sp.ix[ sp[:pd.Timestamp('2018-1-13 14:50:53.445')] ]
##sp=sp[pd.Timestamp('2017-12-13 21:50:53.445'):]
#sp['dox0_c'] = (sp.dox0**alpha_0  -1.0**alpha_0)/(450.0**alpha_0-1.0**alpha_0)*21.
#sp['dox1_c'] = (sp.dox1**alpha_0  -1.0**alpha_0)/(420.0**alpha_0-1.0**alpha_0)*21.
#sp['dox2_c'] = (sp.dox2**alpha_0  -1.0**alpha_0)/(550.0**alpha_0-1.0**alpha_0)*21.
#sp['dox3_c'] = (sp.dox3**alpha_0  -1.0**alpha_0)/(550.0**alpha_0-1.0**alpha_0)*21.
#sp['dox4_c'] = (sp.dox4**alpha_0  -1.0**alpha_0)/(550.0**alpha_0-1.0**alpha_0)*21.
##sp['dox5_c'] = (sp.dox5**alpha_0  -1.0**alpha_0)/(450.0**alpha_0-1.0**alpha_0)*21.
#sp['dox6_c'] = (sp.dox6**alpha_0  -1.0**alpha_0)/(450.0**alpha_0-1.0**alpha_0)*21.
##sp['dox7_c'] = (sp.dox7**alpha_0  -1.0**alpha_0)/(550.0**alpha_0-1.0**alpha_0)*21.
#
#
#prof['grange_b_luo2']['data'].df['dluo2'].loc [   prof['grange_b_luo2']['data'].df['dluo2'] <=0.0] =np.nan
#prof['grange_b_luo2']['data'].df['dluo4'].loc [   prof['grange_b_luo2']['data'].df['dluo4'] <=0.0] =np.nan
#
#
#prof['grange_3_luo2_dry']['data'].df['dluo0'].loc[ prof['grange_3_luo2_dry']['data'].df['dluo0']<=0 ] =np.nan
#prof['grange_3_luo2_dry']['data'].df['dluo0'].loc[ prof['grange_3_luo2_dry']['data'].df['dluo0']<=0 ] =np.nan
#
#prof['grange_3_mo_su']['data'].df['dluo7'].loc[prof['grange_3_mo_su']['data'].df['dluo7']<=0.0] =np.nan
#prof['grange_3_mo_su']['data'].df['tmp7'].loc[prof['grange_3_mo_su']['data'].df['tmp7']<=0.0] =np.nan
#prof['grange_4_mo_su']['data'].df['tmp7'].loc[prof['grange_4_mo_su']['data'].df['tmp7']<=0.0] =np.nan
#prof['grange_5_mo_su']['data'].df['tmp7'].loc[prof['grange_5_mo_su']['data'].df['tmp7']<=0.0] =np.nan
#
#
#prof['grange_d_electrochem_o2']['data'].df['dtp4'].loc[ prof['grange_d_electrochem_o2']['data'].df['dtp4'] <=0 ] =np.nan
#
#
#prof['grange_5_luo2_dry']['data'].df['dluo0'].loc[ prof['grange_5_luo2_dry']['data'].df['dluo0']<=0 ] =np.nan
#prof['grange_5_luo2_dry']['data'].df['dluo1'].loc[ prof['grange_5_luo2_dry']['data'].df['dluo1']<=0 ] =np.nan
#prof['grange_5_luo2_dry']['data'].df['dluo2'].loc[ prof['grange_5_luo2_dry']['data'].df['dluo2']<=0 ] =np.nan
#prof['grange_5_luo2_dry']['data'].df['dluo3'].loc[ prof['grange_5_luo2_dry']['data'].df['dluo3']<=0 ] =np.nan
#prof['grange_5_luo2_dry']['data'].df['dluo4'].loc[ prof['grange_5_luo2_dry']['data'].df['dluo4']<=0 ] =np.nan
#prof['grange_5_luo2_dry']['data'].df['dluo5'].loc[ prof['grange_5_luo2_dry']['data'].df['dluo5']<=0 ] =np.nan
#prof['grange_5_luo2_dry']['data'].df['dluo6'].loc[ prof['grange_5_luo2_dry']['data'].df['dluo6']<=0 ] =np.nan
#
#prof['grange_5_mo_su']['data'].df['dluo7'].loc[prof['grange_5_mo_su']['data'].df['dluo7']<=0.0] =np.nan
#
#
#
#
#alpha_mo=-5.0
#sp=prof['grange_a_moisture_suction']['data'].df
#sp['mo0_c'] = -(sp.mo0**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-350.**alpha_mo)
#sp['mo1_c'] = -(sp.mo1**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-350.**alpha_mo)
#sp['mo2_c'] = -(sp.mo2**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-350.**alpha_mo)
#sp['mo3_c'] = -(sp.mo3**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-350.**alpha_mo)
#sp['mo4_c'] = -(sp.mo4**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-350.**alpha_mo)
#sp['mo5_c'] = -(sp.mo5**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-350.**alpha_mo)
#sp['mo6_c'] = -(sp.mo6**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-350.**alpha_mo)
#sp['mo7_c'] = -(sp.mo7**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-350.**alpha_mo)
#
#sp=prof['grange_b_moisture_suction']['data'].df
#sp['mo0_c'] = -(sp.mo0**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-330.**alpha_mo)
#sp['mo1_c'] = -(sp.mo1**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-330.**alpha_mo)
#sp['mo2_c'] = -(sp.mo2**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-330.**alpha_mo)
#sp['mo3_c'] = -(sp.mo3**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-330.**alpha_mo)
#sp['mo4_c'] = -(sp.mo4**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-330.**alpha_mo)
#sp['mo5_c'] = -(sp.mo5**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-330.**alpha_mo)
#sp['mo6_c'] = -(sp.mo6**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-330.**alpha_mo)
#sp['mo7_c'] = -(sp.mo7**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-330.**alpha_mo)
#
#sp=prof['grange_d_type_moisture_suction']['data'].df
#sp['mo0_c'] = -(sp.mo0**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-350.**alpha_mo)
#sp['mo1_c'] = -(sp.mo1**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-350.**alpha_mo)
#sp['mo2_c'] = -(sp.mo2**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-350.**alpha_mo)
#sp['mo3_c'] = -(sp.mo3**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-350.**alpha_mo)
#sp['mo4_c'] = -(sp.mo4**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-350.**alpha_mo)
#sp['mo5_c'] = -(sp.mo5**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-350.**alpha_mo)
#sp['mo6_c'] = -(sp.mo6**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-350.**alpha_mo)
#sp['mo7_c'] = -(sp.mo7**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-350.**alpha_mo)
#
#
#sp=prof['grange_3_mo_su']['data'].df
#sp['mo0_c'] = -(sp.mo0**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-297.**alpha_mo)
#sp['mo1_c'] = -(sp.mo1**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-297.**alpha_mo)
#sp['mo2_c'] = -(sp.mo2**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-297.**alpha_mo)
#sp['mo3_c'] = -(sp.mo3**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-297.**alpha_mo)
#sp['mo4_c'] = -(sp.mo4**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-297.**alpha_mo)
#sp['mo5_c'] = -(sp.mo5**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-297.**alpha_mo)
#sp['mo6_c'] = -(sp.mo6**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-297.**alpha_mo)
#sp['mo7_c'] = -(sp.mo7**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-297.**alpha_mo)
#
#sp=prof['grange_4_mo_su']['data'].df
#sp['mo0_c'] = -(sp.mo0**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-297.**alpha_mo)
#sp['mo1_c'] = -(sp.mo1**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-297.**alpha_mo)
#sp['mo2_c'] = -(sp.mo2**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-297.**alpha_mo)
#sp['mo3_c'] = -(sp.mo3**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-297.**alpha_mo)
#sp['mo4_c'] = -(sp.mo4**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-297.**alpha_mo)
#sp['mo5_c'] = -(sp.mo5**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-297.**alpha_mo)
#sp['mo6_c'] = -(sp.mo6**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-297.**alpha_mo)
#sp['mo7_c'] = -(sp.mo7**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-297.**alpha_mo)
#
#sp=prof['grange_5_mo_su']['data'].df
#sp['mo0_c'] = -(sp.mo0**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-297.**alpha_mo)
#sp['mo1_c'] = -(sp.mo1**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-297.**alpha_mo)
#sp['mo2_c'] = -(sp.mo2**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-297.**alpha_mo)
#sp['mo3_c'] = -(sp.mo3**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-297.**alpha_mo)
#sp['mo4_c'] = -(sp.mo4**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-297.**alpha_mo)
#sp['mo5_c'] = -(sp.mo5**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-297.**alpha_mo)
#sp['mo6_c'] = -(sp.mo6**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-297.**alpha_mo)
#sp['mo7_c'] = -(sp.mo7**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-297.**alpha_mo)
#
