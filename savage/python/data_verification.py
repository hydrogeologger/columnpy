


sp=prof['grange_a_electrochem_o2']['data'].df
alpha_0=1.0
sp['dox0_c'] = (sp.dox0**alpha_0  -1.0**alpha_0)/(550.0**alpha_0-1.0**alpha_0)*21.
sp['dox1_c'] = (sp.dox1**alpha_0  -1.0**alpha_0)/(550.0**alpha_0-1.0**alpha_0)*21.
sp['dox2_c'] = (sp.dox2**alpha_0  -1.0**alpha_0)/(550.0**alpha_0-1.0**alpha_0)*21.
sp['dox3_c'] = (sp.dox3**alpha_0  -1.0**alpha_0)/(300.0**alpha_0-1.0**alpha_0)*21.
#sp['dox4_c'] = (sp.dox4**alpha_0  -1.0**alpha_0)/(550.0**alpha_0-1.0**alpha_0)
sp['dox6_c'] = (sp.dox6**alpha_0  -1.0**alpha_0)/(550.0**alpha_0-1.0**alpha_0)*21.


sp=prof['grange_b_electrochem_o2']['data'].df
sp['dox0_c'] = (sp.dox0**alpha_0  -1.0**alpha_0)/(450.0**alpha_0-1.0**alpha_0)*21.
sp['dox1_c'] = (sp.dox1**alpha_0  -1.0**alpha_0)/(420.0**alpha_0-1.0**alpha_0)*21.
#sp['dox2_c'] = (sp.dox2**alpha_0  -1.0**alpha_0)/(550.0**alpha_0-1.0**alpha_0)*21.
sp['dox3_c'] = (sp.dox3**alpha_0  -1.0**alpha_0)/(550.0**alpha_0-1.0**alpha_0)*21.
#sp['dox4_c'] = (sp.dox4**alpha_0  -1.0**alpha_0)/(550.0**alpha_0-1.0**alpha_0)*21.
sp['dox5_c'] = (sp.dox5**alpha_0  -1.0**alpha_0)/(450.0**alpha_0-1.0**alpha_0)*21.
sp['dox6_c'] = (sp.dox6**alpha_0  -1.0**alpha_0)/(450.0**alpha_0-1.0**alpha_0)*21.
sp['dox7_c'] = (sp.dox7**alpha_0  -1.0**alpha_0)/(550.0**alpha_0-1.0**alpha_0)*21.


# applymap is the case to apply for all .
prof['grange_d_electrochem_o2']['data'].df= prof['grange_d_electrochem_o2']['data'].df.applymap(lambda x: float(x.strip('"') ) if type(x) is str else None)

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


prof['grange_5_luo2_dry']['data'].df['dluo0'].loc[ prof['grange_5_luo2_dry']['data'].df['dluo0']<=0 ] =np.nan
prof['grange_5_luo2_dry']['data'].df['dluo1'].loc[ prof['grange_5_luo2_dry']['data'].df['dluo1']<=0 ] =np.nan
prof['grange_5_luo2_dry']['data'].df['dluo2'].loc[ prof['grange_5_luo2_dry']['data'].df['dluo2']<=0 ] =np.nan
prof['grange_5_luo2_dry']['data'].df['dluo3'].loc[ prof['grange_5_luo2_dry']['data'].df['dluo3']<=0 ] =np.nan
prof['grange_5_luo2_dry']['data'].df['dluo4'].loc[ prof['grange_5_luo2_dry']['data'].df['dluo4']<=0 ] =np.nan
prof['grange_5_luo2_dry']['data'].df['dluo5'].loc[ prof['grange_5_luo2_dry']['data'].df['dluo5']<=0 ] =np.nan
prof['grange_5_luo2_dry']['data'].df['dluo6'].loc[ prof['grange_5_luo2_dry']['data'].df['dluo6']<=0 ] =np.nan

prof['grange_5_mo_su']['data'].df['dluo7'].loc[prof['grange_5_mo_su']['data'].df['dluo7']<=0.0] =np.nan




