import matplotlib
import matplotlib.image as image

# Force matplotlib to not use any Xwindows backend.
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from PIL import Image
def get_date_taken(path):
    from datetime import datetime
    return datetime.strptime(Image.open(path)._getexif()[36867],'%Y:%m:%d %H:%M:%S')

import glob, os
#os.chdir("/home/chenming/Projects/tailings/area_51_redmud_4cm_photo/")
img_list=glob.glob('/home/chenming/Projects/tailings/area_51_redmud_4cm_photo/*.jpg')
#for file in glob.glob("*.jpg"):
#    print(file)
path_im='/home/chenming/Projects/tailings/area_51_redmud_4cm_photo_1/'
#import os
#for file in os.listdir("/home/chenming/Projects/tailings/area_51_redmud_4cm_photo/"):
#    if file.endswith(".jpg"):
#            print(os.path.join("/home/chenming/Projects/tailings/area_51_redmud_4cm_photo/", file))
#im=image.imread(img_list[0])

files = filter(os.path.isfile, glob.glob(path_im + "*.jpg"))
files.sort(key=lambda x: os.path.getmtime(x))
file_name=[i.split('/')[-1] for i in files]


# this script is used for calibrating load cells
import matplotlib.pylab as pylab
params = {'legend.fontsize': 13,
          'figure.figsize': (10, 5),
         'axes.labelsize': 12,
         'axes.titlesize':'x-large',
         'xtick.labelsize':'14',
         'ytick.labelsize':'14',
#         'ytick.labelweight':'bold',
          'axes.labelsize': 16,
           'axes.labelweight':'bold'}
#         'axes.grid':'linewidth=grid_width,color = '0.5''}
#         'linewidth':lw,'markers.size':ms,'markers.edgewidth':mew}
plt.rcParams["font.weight"] = "bold"
plt.rcParams["axes.labelweight"] = "bold"
plt.rcParams["font.family"] = "Arial"
rcParams['axes.linewidth'] = 5

pylab.rcParams.update(params)
#plt.rcParams['axes.labelsize'] = 16
#plt.rcParams['axes.labelweight'] = 'bold'

lw=4
ms=7
mew=1.5
grid_width=2
y_fontsize=14
# the bad thing in using subplot is that all graph will be generated in the first place
#fig, ax = plt.subplots(8,sharex=True,figsize=(12,18))
#fig, ax = plt.subplots(ncols=2,nrows=8,figsize=(12,12))
sch_name='redmud_first'
#for ii in file_name[-5:]:
for ii in file_name[:3]:
#for ii in file_name:
    im=image.imread(path_im+ii)   
    im_time=get_date_taken(path_im+ii)
    idx_im, min_value = min(enumerate( abs(sp_sch[sch_name].df['date_time']-im_time)), key=operator.itemgetter(1))
    im=np.rot90(im,-1)

    
    #fig=plt.figure
    fig=plt.figure(figsize=(20,14))
    #fig=plt.ion(figsize=(16,12))
    fig.subplots_adjust(left=0.08, right=0.98, top=0.99, bottom=0.05)
    ax = [[] for i in range(8)]
    #ax[0] = plt.subplot2grid((9, 4), (5, 0), colspan=2)
    #ax[1] = plt.subplot2grid((9, 4), (5, 2), colspan=2)
    #ax[2] = plt.subplot2grid((9, 4), (6, 0), colspan=2)
    #ax[3] = plt.subplot2grid((9, 4), (6, 2), colspan=2)
    #ax[4] = plt.subplot2grid((9, 4), (7, 0), colspan=2)
    #ax[5] = plt.subplot2grid((9, 4), (7, 2), colspan=2)
    #ax[6] = plt.subplot2grid((9, 4), (8, 0), colspan=2)
    #ax[7] = plt.subplot2grid((9, 4), (8, 2), colspan=2)
    ax[0] = plt.subplot2grid((8, 2), (0, 0), colspan=1)
    ax[1] = plt.subplot2grid((8, 2), (1, 0), colspan=1)
    ax[2] = plt.subplot2grid((8, 2), (2, 0), colspan=1)
    ax[3] = plt.subplot2grid((8, 2), (3, 0), colspan=1)
    ax[4] = plt.subplot2grid((8, 2), (4, 0), colspan=1)
    ax[5] = plt.subplot2grid((8, 2), (5, 0), colspan=1)
    ax[6] = plt.subplot2grid((8, 2), (6, 0), colspan=1)
    ax[7] = plt.subplot2grid((8, 2), (7, 0), colspan=1)
    fig.subplots_adjust(hspace=.05,wspace=0.3)
    
    
    #fig.subplots_adjust(hspace = .5, wspace=.001)
    
    #ax = ax.ravel()
    for i in ax:
      for axis in ['top','bottom','left','right']:
        i.spines[axis].set_linewidth(2)
    
    ax_img = plt.subplot2grid((9, 7), (8, 6))
#    ax_img.bplot([0.7,0.7,0.1,0.1])
    ax_img.set_position([0.47,0.01,0.53,0.97])
    
    ax[0].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.cum_evap_commercial[:idx_im]*constants.m2mm,'o',color='brown'       ,markersize=ms,markeredgewidth=mew, markeredgecolor='brown',label='load cell')
    
    ax[1].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.evap_rate_commercial[:idx_im]*constants.ms2mmday,'o',color='brown'       ,markersize=ms,markeredgewidth=mew, markeredgecolor='brown',label='load cell')
    
    ax[2].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.sat_commercial[:idx_im],'o',color='brown',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='Moisture B')
    
    ax[3].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.mo_9[:idx_im] ,'ko',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='Moisture A')
    ax[3].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.mo_10[:idx_im],'o',color='brown',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='Moisture B')
    
    ax[4].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.mo_7[:idx_im], 'ko',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='Dielectric suction A')
    ax[4].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.mo_8[:idx_im], 'o',color='brown',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='Dielectric suction B')
    
    ax[5].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.t_2896_begin[:idx_im], 'o',color='brown',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='Fred. Suc. A')
    
    ax[6].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.norm_deltat_2896_heat[:idx_im], 'o',color='brown',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='Fred. Suc. A')
    
    ax[7].semilogy(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.saltrh_2_suction[:idx_im], 'o',color='brown',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='Temp.&Hum. A')
    ax[7].semilogy(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.saltrh_11_suction[:idx_im],'ko',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='Temp.&Hum. B')
    
    
    ax[0].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[1].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[2].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[3].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[4].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[5].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[6].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[7].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    
    #ax[2].set_ylim([6,30])
    #ax[4].set_ylim([50,105])
    ax[0].set_ylabel('CUMULATIVE\nEVAPORATION\n(mm)', fontsize=y_fontsize, labelpad=20)
    ax[1].set_ylabel('EVAPORATION\nRATE\n(mm/day)', fontsize=y_fontsize, labelpad=20)
    ax[2].set_ylabel('DEGREE\nOF\nSATURATION', fontsize=y_fontsize, labelpad=10)
    ax[3].set_ylabel('DIELECTRIC\nMOISTURE\nSENSOR', fontsize=y_fontsize, labelpad=10)
    ax[4].set_ylabel('DIELECTRIC\nSUCTION\nSENSOR', fontsize=y_fontsize, labelpad=10)
    ax[5].set_ylabel('TEMPERATURE\n($^\circ$c)', fontsize=y_fontsize, labelpad=20)
    ax[6].set_ylabel('NORMALIZED\nRISE OF\nTEMPERATURE', fontsize=y_fontsize, labelpad=10)
    ax[7].set_ylabel('SUCTION BY\nTEMPERATURE\nHUMIDITY\n SENSOR (m)', fontsize=y_fontsize, labelpad=10)
    
    ax[7].set_xlabel('TIME (days)', fontsize=y_fontsize,labelpad=3)
    ax[0].set_ylim([-0.2,35])
    ax[1].set_ylim([-1,13])
    ax[2].set_ylim([-0.1,1.1])
    ax[3].set_ylim([200,650])
    ax[4].set_ylim([290,580])
    ax[5].set_ylim([8,27])
    ax[6].set_ylim([-0.1,1.1])
    ax[7].set_ylim([9,40000])
    ax[3].legend(bbox_to_anchor=(.7, 0.6), loc=2, borderaxespad=0.)
    ax[4].legend(bbox_to_anchor=(.6, 0.6 ), loc=2, borderaxespad=0.)
    ax[7].legend(bbox_to_anchor=(.1, 0.55 ), loc=2, borderaxespad=0.)
    ax[0].set_title('(A)',x=0.03,y=0.75,fontweight='bold')
    ax[1].set_title('(B)',x=0.03,y=0.75,fontweight='bold')
    ax[2].set_title('(C)',x=0.03,y=0.75,fontweight='bold')
    ax[3].set_title('(D)',x=0.03,y=0.75,fontweight='bold')
    ax[4].set_title('(E)',x=0.03,y=0.75,fontweight='bold')
    ax[5].set_title('(F)',x=0.03,y=0.75,fontweight='bold')
    ax[6].set_title('(G)',x=0.03,y=0.75,fontweight='bold')
    ax[7].set_title('(H)',x=0.03,y=0.75,fontweight='bold')
    xlim=[sp_sch[sch_name].df.time_days[0],sp_sch[sch_name].df.time_days[len(sp_sch[sch_name].df)-1]]
    ax[0].set_xlim(xlim)
    ax[1].set_xlim(xlim)
    ax[2].set_xlim(xlim)
    ax[3].set_xlim(xlim)
    ax[4].set_xlim(xlim)
    ax[5].set_xlim(xlim)
    ax[6].set_xlim(xlim)
    ax[7].set_xlim(xlim)
    ax[0].set_xticklabels([])
    ax[1].set_xticklabels([])
    ax[2].set_xticklabels([])
    ax[3].set_xticklabels([])
    ax[4].set_xticklabels([])
    ax[5].set_xticklabels([])
    ax[6].set_xticklabels([])

    ax_img.imshow(im)
    ax_img.axis('off')
    
    #plt.show(block=False)
    
    
    fig.savefig('plot_calibrated_result'+sch_name+ii+'.png', format='png', dpi=100)
    plt.close()
