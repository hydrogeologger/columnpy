#fig, ax = plt.subplots(3,3,sharex=True,figsize=(15,9))
#fig.subplots_adjust(hspace=.10)
#fig.subplots_adjust(left=0.11, right=0.99, top=0.97, bottom=0.05)
#fig.subplots_adjust(wspace=.2)
#ax_img = plt.subplot2grid((2, 2), (0,1))
#ax_img.set_position([0.53,0.49,0.53,0.50])
#ax_mo_3 = plt.subplot2grid((2, 6), (1,3))
#ax_mo_3.set_position([0.61,0.05,0.15,0.40])
#ax_mo_4 = plt.subplot2grid((2, 6), (1,5))
#ax_mo_4.set_position([0.81,0.05,0.15,0.40])
#ax_mo_5 = plt.subplot2grid((2, 6), (1,2))
#ax_mo_5.set_position([0.41,0.05,0.15,0.40])

#ax_img = plt.subplot2grid((1, 3), (0,2))
#ax_img.set_position([0.53,0.39,0.45,0.58])

im_path = path_im+file_name[ii]
im=image.imread(im_path)
im_time=date[ii]
#idx_im, min_value = min(enumerate( abs(sp_sch[sch_name].df['date_time']-im_time)), key=operator.itemgetter(1))
idx_im_a_e = prof['grange_a_electrochem_o2']['data'].df.index.get_loc(im_time, method='nearest')
idx_im_a_lo = prof['grange_a_luo2']['data'].df.index.get_loc(im_time, method='nearest')
idx_im_b_e = prof['grange_b_electrochem_o2']['data'].df.index.get_loc(im_time, method='nearest')
idx_im_b_lo = prof['grange_a_luo2']['data'].df.index.get_loc(im_time, method='nearest')
idx_im_d_e = prof['grange_d_electrochem_o2']['data'].df.index.get_loc(im_time, method='nearest')
idx_im_d_lo = prof['grange_d_luo2']['data'].df.index.get_loc(im_time, method='nearest')
idx_im_3_lo = prof['grange_3_luo2_dry']['data'].df.index.get_loc(im_time, method='nearest')
idx_im_4_lo = prof['grange_4_luo2_dry']['data'].df.index.get_loc(im_time, method='nearest')
idx_im_5_lo = prof['grange_5_luo2_dry']['data'].df.index.get_loc(im_time, method='nearest')
#idx_im_a_mo = prof['grange_a_moisture_suction']['data'].df.index.get_loc(im_time, method='nearest')
#idx_im_b_mo = prof['grange_b_moisture_suction']['data'].df.index.get_loc(im_time, method='nearest')
#idx_im_d_mo = prof['grange_d_type_moisture_suction']['data'].df.index.get_loc(im_time, method='nearest')
idx_im_3_mo = prof['grange_3_mo_su']['data'].df.index.get_loc(im_time, method='nearest')
idx_im_4_mo = prof['grange_4_mo_su']['data'].df.index.get_loc(im_time, method='nearest')
idx_im_5_mo = prof['grange_5_mo_su']['data'].df.index.get_loc(im_time, method='nearest')

fig, ax = plt.subplots(6,2,sharex=True,figsize=(15,10))
fig.subplots_adjust(hspace=.10)
fig.subplots_adjust(left=0.10, right=0.99, top=0.97, bottom=0.05)
fig.subplots_adjust(wspace=.2)

for i in ax:
    for j in i:
      for axis in ['top','bottom','left','right']:
        j.spines[axis].set_linewidth(2)

ax_ox_abd = plt.subplot2grid((2, 5), (1,3))
ax_ox_abd.set_position([0.60,0.05,0.15,0.40])

ax_ox_abd.set_xlabel('OXYGEN CONCENTRATION')
ax_ox_abd.set_ylabel('DEPTH FROM COLUMN TOP(m)')
#ax_img.axis('off')
ax_ox_345 = plt.subplot2grid((2, 5), (1,4))
ax_ox_345.set_position([0.80,0.05,0.15,0.40])

ax_ox_345.set_xlabel('OXYGEN CONCENTRATION')
ax_ox_345.set_ylabel('DEPTH FROM COLUMN TOP (m)')

ax_img = plt.subplot2grid((2, 2), (0,1))
ax_img.set_position([0.53,0.49,0.45,0.50])
#ax_img.set_position([0.53,0.25,0.45,0.48])
ax_img.imshow(im)
ax_img.axis('off')

depth_y_ae=np.array([0.5,1.0,1.5,2.0,2.5,3.0,3.5])
#depth_y_be=np.array([0.5,1.0,1.5,2.5,3.5,4.0])
#depth_y_alo=np.array([1.0,1.5])
#depth_y_blo=np.array([0.5,2.0])
#depth_y_de=np.array([1.0,2.0,2.5,3.5,4.0])
#depth_y_temp=np.array([0.5,2.0,2.5,3.0,3.5])
sp=prof['grange_a_electrochem_o2']['data'].df
sp_lo=prof['grange_a_luo2']['data'].df
ox_a_e=sp.iloc[idx_im_a_e][['dox6_c','dox3_c','dox2_c','dox1_c','dox0_c']].tolist()
ox_a_lo=prof['grange_a_luo2']['data'].df.iloc[idx_im_a_lo][['wluo6','wluo5']].tolist()
mergedlist = ox_a_e+ox_a_lo
#ox_b_e=prof['grange_b_electrochem_o2']['data'].df.iloc[idx_im_b_e][['dox7_c','dox6_c','dox5_c','dox3_c','dox1_c','dox0_c']].tolist()
#ox_b_lo=prof['grange_b_luo2']['data'].df.iloc[idx_im_a_lo][['dluo4','dluo2']].tolist()

ax_ox_abd.plot(mergedlist,depth_y_ae,'-',color='darkblue',label='Column_1')
#ax_ox_abd.plot(ox_a_lo,depth_y_alo,'-',color='darkblue',label='Column_1')
ax_ox_abd.set_ylim([4.5,0])
ax_ox_abd.set_xlim([0,25])

