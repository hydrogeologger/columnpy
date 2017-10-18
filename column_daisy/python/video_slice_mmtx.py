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
#img_list=glob.glob('/home/chenming/Projects/tailings/area_51_redmud_4cm_photo/*.jpg')
#for file in glob.glob("*.jpg"):
#    print(file)
sch_name='column_daisy'
#path_im='/home/chenming/Projects/tailings/area_51_redmud_4cm_photo_'+sch_name+'/'
path_im='/home/chenming/Projects/tailings/column_daisy/15/'
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
params = {'legend.fontsize': 11,
          'figure.figsize': (10, 5),
         'axes.labelsize': 12,
         'axes.titlesize':'18',
         'xtick.labelsize':'15',
         'ytick.labelsize':'15',
#         'ytick.labelweight':'bold',
          'axes.labelsize': 18,
           'axes.labelweight':'bold'}
#         'axes.grid':'linewidth=grid_width,color = '0.5''}
#         'linewidth':lw,'markers.size':ms,'markers.edgewidth':mew}
plt.rcParams["font.weight"] = "bold"
plt.rcParams["axes.labelweight"] = "bold"
pylab.rcParams.update(params)
#plt.rcParams['axes.labelsize'] = 16
#plt.rcParams['axes.labelweight'] = 'bold'

lw=4
ms=9
mew=4
grid_width=2
y_fontsize=17
# the bad thing in using subplot is that all graph will be generated in the first place
#fig, ax = plt.subplots(8,sharex=True,figsize=(12,18))
#fig, ax = plt.subplots(ncols=2,nrows=8,figsize=(12,12))
#for ii in file_name[-1:]:
#for ii in file_name[:3]:
for ii in file_name:
    im=image.imread(path_im+ii)   
    im_time=get_date_taken(path_im+ii)
    idx_im, min_value = min(enumerate( abs(sp_sch[sch_name].df['date_time']-im_time)), key=operator.itemgetter(1))
    #im=np.rot90(im,-1)

    
    fig=plt.figure(figsize=(17.5,9.8)) # this is the best to put in the GEC template
    fig.subplots_adjust(left=0.09, right=0.99, top=0.99, bottom=0.08)
    ax = [[] for i in range(4)]
    ax[0] = plt.subplot2grid((3, 2), (0, 0), colspan=1)
    ax[1] = plt.subplot2grid((3, 2), (1, 0), colspan=1)
    ax[2] = plt.subplot2grid((3, 2), (2, 0), colspan=1)
    ax[3] = plt.subplot2grid((3, 2), (2, 1), colspan=1)
    fig.subplots_adjust(hspace=.05,wspace=0.2)
    
    
    
    for i in ax:
      for axis in ['top','bottom','left','right']:
        i.spines[axis].set_linewidth(2)
    
    ax_img = plt.subplot2grid((9, 7), (1, 6))
    ##ax_img.set_position([0.52,0.01,0.53,0.97])
    ax_img.set_position([0.53,0.42,0.48,0.6])
    
    
    ax[0].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.ir_up[:idx_im]/100.0,'-o',color='brown'       ,markersize=ms-7,markeredgewidth=mew, markeredgecolor='brown',label='up',markevery=1)
    #ax[0].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.ir_down[:idx_im],'o',color='k'       ,markersize=ms,markeredgewidth=mew, markeredgecolor='k',label='down',markevery=3)
    mark_every=20
    ax[1].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.mo1[:idx_im],'o',color='c',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='40mm',markevery=mark_every)
    ax[1].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.mo2[:idx_im],'ks',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='80mm',ms=12,markevery=mark_every)
    ax[1].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.mo3[:idx_im],'+',color='brown',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='130mm',markevery=mark_every,ms=12)
    ax[1].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.mo4[:idx_im],'x',color='r',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='200mm',markevery=mark_every,ms=12)
    ax[1].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.mo5[:idx_im],'^',color='g',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='300mm',markevery=mark_every,ms=12)
    ax[1].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.mo7[:idx_im],'x',color='b',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='b',label='600mm',markevery=mark_every,ms=12)
    ax[1].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.mo10[:idx_im],'+',color='m',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='850mm',markevery=mark_every,ms=12)
    

    ax[2].plot(sp_sch[sch_name].df.time_days[:idx_im], -sp_sch[sch_name].df.su3[:idx_im],'+',color='brown',markersize=ms+4,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='130mm',markevery=mark_every)
    ax[2].plot(sp_sch[sch_name].df.time_days[:idx_im], -sp_sch[sch_name].df.su2[:idx_im],'rx',markersize=ms+2,markeredgewidth=mew,fillstyle='none', markeredgecolor='r',label='200mm',markevery=mark_every)
    ax[2].plot(sp_sch[sch_name].df.time_days[:idx_im], -sp_sch[sch_name].df.su4[:idx_im],'^',color='green',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='green',label='300mm',markevery=mark_every,ms=12)
    ax[2].plot(sp_sch[sch_name].df.time_days[:idx_im], -sp_sch[sch_name].df.su1[:idx_im],'o',color='orange',markersize=ms-2,markeredgewidth=mew,fillstyle='full', markeredgecolor='orange',label='400mm',markevery=mark_every,ms=12)
    
    mark_every=1
    ax[3].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.tp3[:idx_im],'-',color='c',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='40mm',markevery=mark_every)
    ax[3].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.tp2[:idx_im],'-',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='80mm',ms=12,markevery=mark_every)
    ax[3].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.tp4[:idx_im],'-',color='brown',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='130mm',markevery=mark_every,ms=12)
    ax[3].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.tp1[:idx_im],'-',color='r',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='200mm',markevery=mark_every,ms=12)
    ax[3].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.tpa3[:idx_im],'-',color='g',markersize=ms-3,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='300mm',markevery=mark_every,ms=12)
    ax[3].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.tpf0[:idx_im],'-',color='b',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='b',label='600mm',markevery=mark_every,ms=12)
    ax[3].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.tc[:idx_im],':',color='m',markersize=ms+3,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='Weather Station',markevery=mark_every,ms=12)
    
    ax[0].set_axisbelow(True)
    ax[1].set_axisbelow(True)
    ax[2].set_axisbelow(True)
    ax[3].set_axisbelow(True)
    ax[0].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[1].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[2].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[3].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    #ax[3].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    #ax[4].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    #ax[5].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    #ax[6].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    #ax[7].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    
    ax[0].set_ylim([-1,11])
    ax[1].set_ylim([-0.1,1.1])
    ax[2].set_ylim([-50,580])
    ax[3].set_ylim([8,38])
    #ax[0].set_ylabel('CUMULATIVE\nEVAPORATION\n(mm)', fontsize=y_fontsize, labelpad=20)
    ax[0].set_ylabel('EVAPORATION RATE\nFROM WEATHER \nSTATION(mm/day)', fontsize=y_fontsize, labelpad=10)
    ax[1].set_ylabel('DEGREE OF\nSATURATION', fontsize=y_fontsize, labelpad=10)
    #ax[2].set_ylabel('DEGREE OF SAT.\nBY DIELECTRIC\nMOISTURE\nSENSOR', fontsize=y_fontsize, labelpad=10)
    ax[2].set_ylabel('SUCTION (kPa)', fontsize=y_fontsize, labelpad=10)
    ax[3].set_ylabel('TEMPERATURE\n(Celsius)', fontsize=y_fontsize, labelpad=10)
    #ax[5].set_ylabel('TEMPERATURE\n($^\circ$c)', fontsize=y_fontsize, labelpad=20)
    #ax[6].set_ylabel('NORMALIZED\nRISE OF\nTEMPERATURE', fontsize=y_fontsize, labelpad=10)
    #ax[7].set_ylabel('SUCTION BY\nTEMPERATURE\nHUMIDITY\n SENSOR (m)', fontsize=y_fontsize, labelpad=10)
    
    ax[2].set_xlabel('TIME (days)', fontsize=y_fontsize,labelpad=3)
    ax[3].set_xlabel('TIME (days)', fontsize=y_fontsize,labelpad=3)
    #ax[0].set_ylim([-0.2,35])
    #ax[0].set_ylim([-1,13])
    #ax[1].set_ylim([-0.09,0.64])
    ##ax[2].set_ylim([200,650])
    #ax[2].set_ylim([1e-0,1e8])
    #ax[5].set_ylim([8,27])
    #ax[6].set_ylim([-0.1,1.1])
    #ax[7].set_ylim([9,40000])
    ax[1].legend(bbox_to_anchor=(.01, 0.65), loc=2, borderaxespad=0.)
    ax[2].legend(bbox_to_anchor=(.01, 0.55 ), loc=2, borderaxespad=0.)
    ax[3].legend(bbox_to_anchor=(.01, 0.6 ), loc=2, borderaxespad=0.)
    #ax[7].legend(bbox_to_anchor=(.1, 0.55 ), loc=2, borderaxespad=0.)
    ax[0].set_title('(A)',x=0.04,y=0.85,fontweight='bold')
    ax[1].set_title('(B)',x=0.04,y=0.85,fontweight='bold')
    ax[2].set_title('(C)',x=0.04,y=0.85,fontweight='bold')
    ax[3].set_title('(D)',x=0.04,y=0.85,fontweight='bold')
    #ax[3].set_title('(D)',x=0.04,y=0.75,fontweight='bold')
    #ax[4].set_title('(E)',x=0.03,y=0.75,fontweight='bold')
    #ax[5].set_title('(F)',x=0.03,y=0.75,fontweight='bold')
    #ax[6].set_title('(G)',x=0.03,y=0.75,fontweight='bold')
    #ax[7].set_title('(H)',x=0.03,y=0.75,fontweight='bold')
    xlim=[sp_sch[sch_name].df.time_days[0],sp_sch[sch_name].df.time_days[len(sp_sch[sch_name].df)-1]]
    ax[0].set_xlim(xlim)
    ax[1].set_xlim(xlim)
    ax[2].set_xlim(xlim)
    ax[3].set_xlim(xlim)
    #ax[4].set_xlim(xlim)
    #ax[5].set_xlim(xlim)
    #ax[6].set_xlim(xlim)
    #ax[7].set_xlim(xlim)
    ax[0].set_xticklabels([])
    ax[1].set_xticklabels([])
    #ax[2].set_xticklabels([])
    #ax[3].set_xticklabels([])
    #ax[4].set_xticklabels([])
    #ax[5].set_xticklabels([])
    #ax[6].set_xticklabels([])
    #plt.text(0.5, 0.5, 's', fontsize=18)
    #plt.text(-100,1000, 'Moisture\nsensor 1', fontsize=18,color='b')
    #ax_img.annotate('Moisture\nsensor A',
    #            xy=(300, 1000),
    #            xytext=(0.51, 0.6),    # fraction, fraction
    #            textcoords='figure fraction',
    #            arrowprops=dict(facecolor='yellow', shrink=0.05),
    #            horizontalalignment='left',
    #            verticalalignment='bottom',fontsize=18
    #            )
    #ax_img.annotate('Moisture\nsensor B',
    #            xy=(200, 1200),
    #            xytext=(0.51, 0.5),    # fraction, fraction
    #            textcoords='figure fraction',
    #            arrowprops=dict(facecolor='yellow', shrink=0.05),
    #            horizontalalignment='left',
    #            verticalalignment='bottom',fontsize=18
    #            )
    #ax_img.annotate('Suction\nsensor A',
    #            xy=(300, 1400),
    #            xytext=(0.51, 0.4),    # fraction, fraction
    #            textcoords='figure fraction',
    #            arrowprops=dict(facecolor='yellow', shrink=0.05),
    #            horizontalalignment='left',
    #            verticalalignment='bottom',fontsize=18
    #            )
    #ax_img.annotate('Suction\nsensor B',
    #            xy=(400, 1600),
    #            xytext=(0.51, 0.3),    # fraction, fraction
    #            textcoords='figure fraction',
    #            arrowprops=dict(facecolor='yellow', shrink=0.05),
    #            horizontalalignment='left',
    #            verticalalignment='bottom',fontsize=18
    #            )

    ax_img.imshow(im)
    ax_img.axis('off')
    
    #plt.show(block=False)
    
    
    fig.savefig('plot_calibrated_result'+sch_name+ii+'.png', format='png', dpi=100)
    plt.close()
