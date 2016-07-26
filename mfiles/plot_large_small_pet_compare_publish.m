i1=find(strcmpi({sched.tag},'arcylic_large_pet_chop_stg1'));
i2=find(strcmpi({sched.tag},'arcylic_small_pet'));
iv=1;


file_name=strcat('compare_large_small_evt_publish.fig');
h=figure('Name',file_name,'Position', [100, 100, 1049, 895]);

a.left =  0.08;
a.bot  =  0.78;
a.width= 0.85;
a.w_interval=0.45;
a.width2=0.45;
a.height= 0.18;
a.height2= 0.49;
a.h_interval=0.23;
a.h_interval2=0.4;
a.lw=2;
a.fs_ylabel=14;
stage.days_12=4;
stage.days_23=8;
stage.days_34=13;

a.fig_id=0;


sp=subplot('position',[a.left,a.bot-a.fig_id*a.h_interval,a.width,a.height]);
set(sp,'linewidth',3)
plot(sched(i1).time_day_ay(1:iv:end),sched(i1).evap(1:iv:end)*c.ms2mmday,'bo','displayname','PET8','linewidth',a.lw);hold on
plot(sched(i2).time_day_ay(1:iv:end),sched(i2).evap(1:iv:end)*c.ms2mmday,'ro','displayname','PET6','linewidth',a.lw);hold on
text(0.2,9.7,'(a)','fontweight','bold','fontsize',a.fs_ylabel)

set(gca,'FontSize',12,'FontWeight','bold','linewidth',2)
xlabel('Time(day)','fontweight','bold','fontsize',a.fs_ylabel)
ylabel('Evap. rate (mm/day)','fontweight','bold','fontsize',a.fs_ylabel)
grid on

a.fig_id=a.fig_id+1;
subplot('position',[a.left,a.bot-a.fig_id*a.h_interval,a.width,a.height]);
plot(sched(i1).dt85g.vwc_pt1,sched(i1).evap*c.ms2mmday,'bo','displayname','PET8','linewidth',a.lw);hold on
plot(sched(i2).dt85g.vwc_pt1,sched(i2).evap*c.ms2mmday,'ro','displayname','PET6','linewidth',a.lw);hold on
set(gca,'FontSize',12,'FontWeight','bold','linewidth',2)
xlabel('Degree of sat. (-)','fontweight','bold','fontsize',a.fs_ylabel)
ylabel('Evap. rate (mm/day)','fontweight','bold','fontsize',a.fs_ylabel)
text(-0.19,9.5,'(b)','fontweight','bold','fontsize',a.fs_ylabel)
grid on


a.fig_id=a.fig_id+1;
subplot('position',[a.left,a.bot-a.fig_id*a.h_interval,a.width,a.height]);
plot(sched(i1).accu_evap*c.m2mm,sched(i1).evap*c.ms2mmday,'bo','displayname','PET8','linewidth',a.lw);hold on
plot(sched(i2).accu_evap*c.m2mm,sched(i2).evap*c.ms2mmday,'ro','displayname','PET6','linewidth',a.lw);hold on
set(gca,'FontSize',12,'FontWeight','bold','linewidth',2)
ylabel('Evap. rate (mm/day)','fontweight','bold','fontsize',a.fs_ylabel)
xlabel('Cumulative evap. (mm)','fontweight','bold','fontsize',a.fs_ylabel)

text(1,9.5,'(c)','fontweight','bold','fontsize',a.fs_ylabel)
grid on

a.fig_id=a.fig_id+1;
subplot('position',[a.left,a.bot-a.fig_id*a.h_interval,a.width,a.height]);

plot(sched(i1).dt85g.vwc_pt1,sched(i1).accu_evap*c.m2mm,'bo','displayname','PET8','linewidth',a.lw);hold on
plot(sched(i2).dt85g.vwc_pt1,sched(i2).accu_evap*c.m2mm,'ro','displayname','PET6','linewidth',a.lw);hold on
xlabel('Degree of sat.(-)');ylabel('accu. evap. (mm/day)')
ylabel('Accu. evap. (mm)','fontweight','bold','fontsize',a.fs_ylabel)
set(gca,'FontSize',12,'FontWeight','bold','linewidth',2)
text(-0.19,115,'(d)','fontweight','bold','fontsize',a.fs_ylabel)
grid on
savefig(h,file_name)
