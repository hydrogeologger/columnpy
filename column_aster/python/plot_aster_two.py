import matplotlib
import matplotlib.image as image


lw=2
ms=0.5
mew=3
grid_width=2
y_fontsize=12

params = {'legend.fontsize': 'x-large',
          'figure.figsize': (10, 5),
         'axes.labelsize': 11,
         'axes.titlesize':'11',
         'xtick.labelsize':'11',
         'ytick.labelsize':'11',
         'font.weight':'bold',
         'axes.labelweight':'bold',
         'lines.linewidth':2}#,
#         'title.fontweight':'bold'}

#         'axes.grid':'linewidth=grid_width,color = '0.5''}
#         'linewidth':lw,'markers.size':ms,'markers.edgewidth':mew}
pylab.rcParams.update(params)

lw=2
ms=6
mew=2
grid_width=2
y_fontsize=11
fig, ax = plt.subplots(5,sharex=True,figsize=(8,9))
fig.subplots_adjust(hspace=.10)
fig.subplots_adjust(left=0.18, right=0.98, top=0.97, bottom=0.08)


for i in ax:
  for axis in ['top','bottom','left','right']:
    i.spines[axis].set_linewidth(2)

ta=sp_sch['Aster_two'].df

ax[0].plot(ta['time_days'],ta['cum_evap_m']*constants.m2mm,'r-'   ,linewidth=lw,markersize=ms,markeredgewidth=mew, markeredgecolor='k',label='load cell')
ax[1].plot(ta['time_days'],ta['evap_rate']*constants.ms2mmday,'r-',linewidth=lw,markersize=ms,markeredgewidth=mew, markeredgecolor='k',label='load cell')
ax[1].set_ylim([-2,19])


ax[2].plot(ta['time_days'], ta['mom_27'], 'r-',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='4 cm')
ax[2].plot(ta['time_days'], ta['mom_23'], 'g-',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='8 cm')
ax[2].plot(ta['time_days'], ta['mom_24'], 'b-',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='13cm')
ax[2].plot(ta['time_days'], ta['mom_26'], 'c-',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='20cm')
ax[2].plot(ta['time_days'], ta['mom_28'], 'm-',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='30cm')
ax[2].plot(ta['time_days'], ta['mom_25'], 'k-',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='b',label='45cm')
ax[2].plot(ta['time_days'], ta['mom_30'], '-' ,linewidth=lw,color='brown',markerfacecolor='brown' ,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='60cm')
ax[2].set_ylim([-0.1,1.3])

#ax[2].plot(ta['time_days'], ta['mom_23'], 'r-',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='10cm')
#ax[2].plot(ta['time_days'], ta['mom_24'], 'g-',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='10cm')
#ax[2].plot(ta['time_days'], ta['mom_25'], 'b-',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='b',label='10cm')
#ax[2].plot(ta['time_days'], ta['mom_26'], 'c-',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='10cm')
#ax[2].plot(ta['time_days'], ta['mom_27'], 'm-',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='10cm')
#ax[2].plot(ta['time_days'], ta['mom_28'], 'k-',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='10cm')
#ax[2].plot(ta['time_days'], ta['mom_30'], '-' ,linewidth=lw,markerfacecolor='brown' ,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='10cm')


ax[3].semilogy(ta['time_days'], ta['su_5_kpa'], 'r-',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='20cm')
ax[3].semilogy(ta['time_days'], ta['su_6_kpa'], 'g-',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='30cm')
ax[3].semilogy(ta['time_days'], ta['su_7_kpa'], 'b-',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='b',label='45cm')
ax[3].semilogy(ta['time_days'], ta['su_8_kpa'], 'c-',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='60cm')
ax[3].set_ylim([5,2e2])


ax[4].plot(ta['time_days'], ta['temp_suc1'], 'r-',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='4 cm')
ax[4].plot(ta['time_days'], ta['temp_suc2'], 'g-',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='8 cm')
ax[4].plot(ta['time_days'], ta['temp_suc3'], 'b-',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='b',label='13cm')
ax[4].plot(ta['time_days'], ta['temp_suc4'], 'c-',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='20cm')
ax[4].plot(ta['time_days'], ta['temp_suc5'], 'm-',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='30cm')
ax[4].plot(ta['time_days'], ta['temp_suc6'], 'k-',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='45cm')
ax[4].plot(ta['time_days'], ta['temp_suc7'], '-',color='brown',linewidth=lw,markerfacecolor='brown' ,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='85cm')


#plt.xticks(rotation=45)
plt.show(block=False)


ax[0].set_axisbelow(True)
ax[1].set_axisbelow(True)
ax[2].set_axisbelow(True)
ax[3].set_axisbelow(True)
ax[4].set_axisbelow(True)
ax[0].set_title('(A)',x=0.02,y=0.82,fontweight='bold')
ax[1].set_title('(B)',x=0.02,y=0.82,fontweight='bold')
ax[2].set_title('(C)',x=0.02,y=0.82,fontweight='bold')
ax[3].set_title('(D)',x=0.02,y=0.82,fontweight='bold')
ax[4].set_title('(E)',x=0.02,y=0.82,fontweight='bold')
ax[0].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
ax[1].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
ax[2].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
ax[3].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
ax[4].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
ax[0].set_xlim([-5,135])
ax[4].set_xlabel('TIME (Days)')
ax[0].set_ylabel('CUMULATIVE\nEVAPORATION\n(mm)', fontsize=y_fontsize, labelpad=10)
ax[1].set_ylabel('EVAPORATION\nRATE\n(mm/Day)', fontsize=y_fontsize, labelpad=25)
ax[2].set_ylabel('DEGREE OF\nSATURATION\nBELOW TAILINGS\nSURFACE', fontsize=y_fontsize, labelpad=12)
ax[3].set_ylabel('SUCTION\nBELOW TAILINGS\n SURFACE (kPa)', fontsize=y_fontsize, labelpad=12)
ax[4].set_ylabel('TEMPERATURE\nBELOW TAILINGS\nSURFACE\n($^\circ$C)', fontsize=y_fontsize, labelpad=19)
ax[2].legend(bbox_to_anchor=(.99, 0.95), loc=1, borderaxespad=0.,fontsize=8,handletextpad=0.13,labelspacing=0.05,ncol=7)
ax[3].legend(bbox_to_anchor=(.1, 0.95 ), loc=2, borderaxespad=0.,fontsize=8,handletextpad=0.03,labelspacing=0.02,ncol=5,columnspacing=0.4)
ax[4].legend(bbox_to_anchor=(.1, 0.95), loc=2, borderaxespad=0.,fontsize=8,handletextpad=0.03,labelspacing=0.02,ncol=7,columnspacing=0.4)#title='CM below surface')


fig.savefig('figure/plot_aster_two.png', format='png', dpi=600)
ta.to_csv('output_data/'+'Aster_two'+'.csv')
# Force matplotlib to not use any Xwindows backend.
#matplotlib.use('Agg')
#import matplotlib.pyplot as plt
#from PIL import Image
#def get_date_taken(path):
#    from datetime import datetime
#    return datetime.strptime(Image.open(path)._getexif()[36867],'%Y:%m:%d %H:%M:%S')
#
#import glob, os
##os.chdir("/home/chenming/Projects/tailings/area_51_redmud_4cm_photo/")
##img_list=glob.glob('/home/chenming/Projects/tailings/area_51_redmud_4cm_photo/*.jpg')
##for file in glob.glob("*.jpg"):
##    print(file)
#sch_name='redmud_second'
#path_im='/home/chenming/Projects/tailings/area_51_redmud_4cm_photo_'+sch_name+'/'
##import os
##for file in os.listdir("/home/chenming/Projects/tailings/area_51_redmud_4cm_photo/"):
##    if file.endswith(".jpg"):
##            print(os.path.join("/home/chenming/Projects/tailings/area_51_redmud_4cm_photo/", file))
##im=image.imread(img_list[0])
#
#files = filter(os.path.isfile, glob.glob(path_im + "*.jpg"))
#files.sort(key=lambda x: os.path.getmtime(x))
#file_name=[i.split('/')[-1] for i in files]


## this script is used for calibrating load cells
#import matplotlib.pylab as pylab
#params = {'legend.fontsize': 16,
#          'figure.figsize': (10, 5),
#         'axes.labelsize': 12,
#         'axes.titlesize':'18',
#         'xtick.labelsize':'15',
#         'ytick.labelsize':'15',
##         'ytick.labelweight':'bold',
#          'axes.labelsize': 18,
#           'axes.labelweight':'bold'}
##         'axes.grid':'linewidth=grid_width,color = '0.5''}
##         'linewidth':lw,'markers.size':ms,'markers.edgewidth':mew}
#plt.rcParams["font.weight"] = "bold"
#plt.rcParams["axes.labelweight"] = "bold"
#pylab.rcParams.update(params)
##plt.rcParams['axes.labelsize'] = 16
##plt.rcParams['axes.labelweight'] = 'bold'
#
#lw=4
#ms=9
#mew=4
#grid_width=2
#y_fontsize=17
## the bad thing in using subplot is that all graph will be generated in the first place
##fig, ax = plt.subplots(8,sharex=True,figsize=(12,18))
##fig, ax = plt.subplots(ncols=2,nrows=8,figsize=(12,12))
#for ii in file_name[-2:]:
##for ii in file_name[:3]:
##for ii in file_name:
#    im=image.imread(path_im+ii)   
#    im_time=get_date_taken(path_im+ii)
#    idx_im, min_value = min(enumerate( abs(sp_sch[sch_name].df['date_time']-im_time)), key=operator.itemgetter(1))
#    im=np.rot90(im,-1)
#
#    
#    #fig=plt.figure
#    fig=plt.figure(figsize=(8,9.8)) # this is the best to put in the GEC template
#    fig.subplots_adjust(left=0.09, right=0.99, top=0.99, bottom=0.08)
#    ax = [[] for i in range(3)]
#    ax[0] = plt.subplot2grid((3, 2), (0, 0), colspan=1)
#    ax[1] = plt.subplot2grid((3, 2), (1, 0), colspan=1)
#    ax[2] = plt.subplot2grid((3, 2), (2, 0), colspan=1)
#    fig.subplots_adjust(hspace=.05,wspace=0.3)
#    
#    
#    #fig.subplots_adjust(hspace = .5, wspace=.001)
#    
#    #ax = ax.ravel()
#    for i in ax:
#      for axis in ['top','bottom','left','right']:
#        i.spines[axis].set_linewidth(2)
#    
#    ax_img = plt.subplot2grid((9, 7), (8, 6))
##    ax_img.bplot([0.7,0.7,0.1,0.1])
#    ax_img.set_position([0.52,0.01,0.53,0.97])
#    
#    #ax[0].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.cum_evap_commercial[:idx_im]*constants.m2mm,'o',color='brown'       ,markersize=ms,markeredgewidth=mew, markeredgecolor='brown',label='load cell')
#    
#    ax[0].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.evap_rate_commercial[:idx_im]*constants.ms2mmday,'o',color='c'       ,markersize=ms,markeredgewidth=mew, markeredgecolor='c',label='load cell',markevery=3)
#    
#    ax[1].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.sat_commercial[:idx_im]*sp_sch[sch_name].por,'o',color='c',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='Balance',markevery=6)
#    ax[1].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.mo_9_vwc[:idx_im] ,'kx',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='VWC A',ms=10,markevery=6)
#    ax[1].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.mo_10_vwc[:idx_im],'+',color='brown',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='VWC B',markevery=6,ms=12)
#    
#
#    ax[2].semilogy(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.suc_commercial[:idx_im],'o',color='c',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='Balance\n& SWCC',markevery=7)
#    ax[2].semilogy(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.mo_7_suction[:idx_im], 'o',markersize=ms,markeredgewidth=mew,fillstyle='none', markeredgecolor='brown',label='DS A',markevery=9)
#    ax[2].semilogy(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.mo_8_suction[:idx_im], 'x',color='pink',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='pink',label='DS B',markevery=7,ms=12)
#    ax[2].semilogy(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.suht_2896_suction[:idx_im], '+',color='orange',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='orange',label='TS C',markevery=5,ms=12)
#    
#    #ax[5].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.t_2896_begin[:idx_im], 'o',color='brown',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='Fred. Suc. A')
#    #
#    #ax[6].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.norm_deltat_2896_heat[:idx_im], 'o',color='brown',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='Fred. Suc. A')
#    #
#    #ax[7].semilogy(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.saltrh_2_suction[:idx_im], 'o',color='brown',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='Temp.&Hum. A')
#    #ax[7].semilogy(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.saltrh_11_suction[:idx_im],'ko',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='Temp.&Hum. B')
#    
#    ax[0].set_axisbelow(True)
#    ax[1].set_axisbelow(True)
#    ax[2].set_axisbelow(True)
#    ax[0].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
#    ax[1].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
#    ax[2].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
#    #ax[3].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
#    #ax[4].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
#    #ax[5].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
#    #ax[6].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
#    #ax[7].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
#    
#    #ax[2].set_ylim([6,30])
#    #ax[4].set_ylim([50,105])
#    #ax[0].set_ylabel('CUMULATIVE\nEVAPORATION\n(mm)', fontsize=y_fontsize, labelpad=20)
#    ax[0].set_ylabel('EVAPORATION RATE\n(mm/day)', fontsize=y_fontsize, labelpad=10)
#    ax[1].set_ylabel('VOLUMETRIC WATER\nCONTENT', fontsize=y_fontsize, labelpad=10)
#    #ax[2].set_ylabel('DEGREE OF SAT.\nBY DIELECTRIC\nMOISTURE\nSENSOR', fontsize=y_fontsize, labelpad=10)
#    ax[2].set_ylabel('SUCTION (kPa)', fontsize=y_fontsize, labelpad=10)
#    #ax[5].set_ylabel('TEMPERATURE\n($^\circ$c)', fontsize=y_fontsize, labelpad=20)
#    #ax[6].set_ylabel('NORMALIZED\nRISE OF\nTEMPERATURE', fontsize=y_fontsize, labelpad=10)
#    #ax[7].set_ylabel('SUCTION BY\nTEMPERATURE\nHUMIDITY\n SENSOR (m)', fontsize=y_fontsize, labelpad=10)
#    
#    ax[2].set_xlabel('TIME (days)', fontsize=y_fontsize,labelpad=3)
#    #ax[0].set_ylim([-0.2,35])
#    ax[0].set_ylim([-1,13])
#    ax[1].set_ylim([-0.09,0.64])
#    #ax[2].set_ylim([200,650])
#    ax[2].set_ylim([1e-0,1e8])
#    #ax[5].set_ylim([8,27])
#    #ax[6].set_ylim([-0.1,1.1])
#    #ax[7].set_ylim([9,40000])
#    ax[1].legend(bbox_to_anchor=(.71, 0.95), loc=2, borderaxespad=0.)
#    ax[2].legend(bbox_to_anchor=(.71, 0.55 ), loc=2, borderaxespad=0.)
#    #ax[7].legend(bbox_to_anchor=(.1, 0.55 ), loc=2, borderaxespad=0.)
#    ax[0].set_title('(A)',x=0.04,y=0.85,fontweight='bold')
#    ax[1].set_title('(B)',x=0.04,y=0.85,fontweight='bold')
#    ax[2].set_title('(C)',x=0.04,y=0.85,fontweight='bold')
#    #ax[3].set_title('(D)',x=0.04,y=0.75,fontweight='bold')
#    #ax[4].set_title('(E)',x=0.03,y=0.75,fontweight='bold')
#    #ax[5].set_title('(F)',x=0.03,y=0.75,fontweight='bold')
#    #ax[6].set_title('(G)',x=0.03,y=0.75,fontweight='bold')
#    #ax[7].set_title('(H)',x=0.03,y=0.75,fontweight='bold')
#    xlim=[sp_sch[sch_name].df.time_days[0],sp_sch[sch_name].df.time_days[len(sp_sch[sch_name].df)-1]]
#    ax[0].set_xlim(xlim)
#    ax[1].set_xlim(xlim)
#    ax[2].set_xlim(xlim)
#    #ax[3].set_xlim(xlim)
#    #ax[4].set_xlim(xlim)
#    #ax[5].set_xlim(xlim)
#    #ax[6].set_xlim(xlim)
#    #ax[7].set_xlim(xlim)
#    ax[0].set_xticklabels([])
#    ax[1].set_xticklabels([])
#    #ax[2].set_xticklabels([])
#    #ax[3].set_xticklabels([])
#    #ax[4].set_xticklabels([])
#    #ax[5].set_xticklabels([])
#    #ax[6].set_xticklabels([])
#    #plt.text(0.5, 0.5, 's', fontsize=18)
#    #plt.text(-100,1000, 'Moisture\nsensor 1', fontsize=18,color='b')
#    #ax_img.annotate('Moisture\nsensor A',
#    #            xy=(300, 1000),
#    #            xytext=(0.51, 0.6),    # fraction, fraction
#    #            textcoords='figure fraction',
#    #            arrowprops=dict(facecolor='yellow', shrink=0.05),
#    #            horizontalalignment='left',
#    #            verticalalignment='bottom',fontsize=18
#    #            )
#    #ax_img.annotate('Moisture\nsensor B',
#    #            xy=(200, 1200),
#    #            xytext=(0.51, 0.5),    # fraction, fraction
#    #            textcoords='figure fraction',
#    #            arrowprops=dict(facecolor='yellow', shrink=0.05),
#    #            horizontalalignment='left',
#    #            verticalalignment='bottom',fontsize=18
#    #            )
#    #ax_img.annotate('Suction\nsensor A',
#    #            xy=(300, 1400),
#    #            xytext=(0.51, 0.4),    # fraction, fraction
#    #            textcoords='figure fraction',
#    #            arrowprops=dict(facecolor='yellow', shrink=0.05),
#    #            horizontalalignment='left',
#    #            verticalalignment='bottom',fontsize=18
#    #            )
#    #ax_img.annotate('Suction\nsensor B',
#    #            xy=(400, 1600),
#    #            xytext=(0.51, 0.3),    # fraction, fraction
#    #            textcoords='figure fraction',
#    #            arrowprops=dict(facecolor='yellow', shrink=0.05),
#    #            horizontalalignment='left',
#    #            verticalalignment='bottom',fontsize=18
#    #            )
#
#    ax_img.imshow(im)
#    ax_img.axis('off')
#    
#    #plt.show(block=False)
#    
#    
#    fig.savefig('plot_calibrated_result'+sch_name+ii+'.png', format='png', dpi=100)
#    plt.close()
