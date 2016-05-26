i=find(strcmpi({sched.tag},'arcylic_large_pet_chop_stg1'));
iv=1;


file_name=strcat(sched(i).tag,'_publish.fig');
h=figure('Name',file_name,'Position', [100, 100, 1049, 895]);

a.left =  0.08;
a.bot  =  0.75;
a.width= 0.85;
a.w_interval=0.45;
a.width2=0.45;
a.height= 0.2;
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
plot([stage.days_12,stage.days_12],[20,45],'Color',[0 0 0]+0.5,'linewidth',3);hold on;
plot([stage.days_23,stage.days_23],[20,45],'Color',[0 0 0]+0.5,'linewidth',3);hold on;
plot([stage.days_34,stage.days_34],[20,45],'Color',[0 0 0]+0.5,'linewidth',3);hold on;
h1=plot(sched(i).time_day_ay(1:iv:end),sched(i).em50.temp_pt4(1:iv:end),...
    'ko','displayname','soil surface','linewidth',a.lw);hold on
h2=plot(sched(i).time_day_ay(1:iv:end),sched(i).dt85g.temp_pt2(1:iv:end),...
    'ro','displayname','8cm below surface','linewidth',a.lw);hold on
h3=plot(sched(i).time_day_ay(1:iv:end),sched(i).dt85g.temp_pt4(1:iv:end),...
    'go','displayname','14cm below surface','linewidth',a.lw);hold on
h4=plot(sched(i).time_day_ay(1:iv:end),sched(i).dt85g.temp_pt1(1:iv:end),...
    'bo','displayname','30cm below surface','linewidth',a.lw);hold on
h5=plot(sched(i).time_day_ay(1:iv:end),sched(i).dt85g.temp_pt3(1:iv:end),...
    'co','displayname','50cm below surface','linewidth',a.lw);hold on
text(stage.days_12/2,45-1,'I','fontweight','bold','fontsize',a.fs_ylabel)
text((stage.days_12+stage.days_23)/2,45-1,'II','fontweight','bold','fontsize',a.fs_ylabel)
text((stage.days_34+stage.days_23)/2,45-1,'III','fontweight','bold','fontsize',a.fs_ylabel)
text((stage.days_34+60)/2,45-1,'IIV','fontweight','bold','fontsize',a.fs_ylabel)
text(0.2,44,'(a)','fontweight','bold','fontsize',a.fs_ylabel)

set(gca,'FontSize',12,'FontWeight','bold','linewidth',2)
ylabel('Temperature (celsius)','fontweight','bold','fontsize',a.fs_ylabel)
legend([h1,h2,h3,h4,h5],'soil surface','8cm below surface','14cm below surface',...
	'14cm below surface','30cm below surface','50cm below surface','location','east')
grid on

a.fig_id=a.fig_id+1;
subplot('position',[a.left,a.bot-a.fig_id*a.h_interval,a.width,a.height]);
plot([stage.days_12,stage.days_12],[-0.2,1.2],'Color',[0 0 0]+0.5,'linewidth',3);hold on;
plot([stage.days_23,stage.days_23],[-0.2,1.2],'Color',[0 0 0]+0.5,'linewidth',3);hold on;
plot([stage.days_34,stage.days_34],[-0.2,1.2],'Color',[0 0 0]+0.5,'linewidth',3);hold on;
h1=plot(sched(i).time_day_ay(1:iv:end),sched(i).dt85g.vwc_pt1(1:iv:end),...
    'ko','displayname','3cm below surface','linewidth',a.lw);hold on
h2=plot(sched(i).time_day_ay(1:iv:end),sched(i).dt85g.vwc_pt6(1:iv:end),...
    'ro','displayname','8cm below surface','linewidth',a.lw);hold on
h3=plot(sched(i).time_day_ay(1:iv:end),sched(i).dt85g.vwc_pt2(1:iv:end),...
    'go','displayname','16cm below surface','linewidth',a.lw);hold on
set(gca,'FontSize',12,'FontWeight','bold','linewidth',2)
ylabel('Degree of sat. (-)','fontweight','bold','fontsize',a.fs_ylabel)
%legend('show','location','northeast')
text(0.2,1.15,'(b)','fontweight','bold','fontsize',a.fs_ylabel)
legend([h1,h2,h3],'3cm below surface','8cm below surface','16cm below surface','location','northeast')
grid on


a.fig_id=a.fig_id+1;
subplot('position',[a.left,a.bot-a.fig_id*a.h_interval,a.width,a.height]);
plot([stage.days_12,stage.days_12],[0,120],'Color',[0 0 0]+0.5,'linewidth',3);hold on;
plot([stage.days_23,stage.days_23],[0,120],'Color',[0 0 0]+0.5,'linewidth',3);hold on;
plot([stage.days_34,stage.days_34],[0,120],'Color',[0 0 0]+0.5,'linewidth',3);hold on;
plot(sched(i).time_day_ay(1:iv:end),...
	sched(i).accu_evap(1:iv:end)*c.m2mm,'ko','linewidth',a.lw);hold on
set(gca,'FontSize',12,'FontWeight','bold','linewidth',2)
ylabel('Cumulative evap. (mm)','fontweight','bold','fontsize',a.fs_ylabel)

text(0.2,115,'(c)','fontweight','bold','fontsize',a.fs_ylabel)
grid on

a.fig_id=a.fig_id+1;
subplot('position',[a.left,a.bot-a.fig_id*a.h_interval,a.width,a.height]);
plot([stage.days_12,stage.days_12],[0,10],'Color',[0 0 0]+0.5,'linewidth',3);hold on;
plot([stage.days_23,stage.days_23],[0,10],'Color',[0 0 0]+0.5,'linewidth',3);hold on;
plot([stage.days_34,stage.days_34],[0,10],'Color',[0 0 0]+0.5,'linewidth',3);hold on;
plot(sched(i).time_day_ay(1:iv:end),sched(i).evap(1:iv:end)*c.ms2mmday,'ko','linewidth',a.lw);hold on
xlabel('Time(day)','fontweight','bold','fontsize',a.fs_ylabel);
ylabel('Evap. rate (mm/day)','fontweight','bold','fontsize',a.fs_ylabel)
set(gca,'FontSize',12,'FontWeight','bold','linewidth',2)
text(0.2,9.5,'(d)','fontweight','bold','fontsize',a.fs_ylabel)
grid on
savefig(h,file_name)
