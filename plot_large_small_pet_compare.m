i1=find(strcmpi({sched.tag},'arcylic_large_pet_chop_stg1'));
i2=find(strcmpi({sched.tag},'arcylic_small_pet'));

iv=1;

file_name=strcat('compare_large_small_evt.fig');
h=figure('Name',file_name,'Position', [100, 100, 1049, 895]);

%set(h,'Resize','off')
subplot(5,1,1);
plot(sched(i1).time_day_ay(1:iv:end)...
	,sched(i1).accu_evap(1:iv:end)*c.m2mm,'bo');hold on
plot(sched(i2).time_day_ay(1:iv:end)...
	,sched(i2).accu_evap(1:iv:end)*c.m2mm,'ro');hold on
title(file_name,'interpreter','none')
xlabel('Time(day)');ylabel('cumulative evaporation (mm)')

subplot(5,1,2);
plot(sched(i1).time_day_ay(1:iv:end),sched(i1).evap(1:iv:end)*c.ms2mmday,'bo');hold on
plot(sched(i2).time_day_ay(1:iv:end),sched(i2).evap(1:iv:end)*c.ms2mmday,'ro');hold on
xlabel('Time(day)');ylabel('evaporation rate (mm/day)')

subplot(5,1,3);
plot(sched(i1).dt85g.vwc_pt1,sched(i1).evap*c.ms2mmday,'bo','displayname','raw');hold on
plot(sched(i2).dt85g.vwc_pt1,sched(i2).evap*c.ms2mmday,'ro','displayname','raw');hold on
xlabel('degree of saturation(-)');ylabel('evaporation rate (mm/day)')

subplot(5,1,4);
plot(sched(i1).accu_evap*c.m2mm,sched(i1).evap*c.ms2mmday,'bo','displayname','raw');hold on
plot(sched(i2).accu_evap*c.m2mm,sched(i2).evap*c.ms2mmday,'ro','displayname','raw');hold on
xlabel('Accu. evap.(-)');ylabel('evaporation rate (mm/day)')

subplot(5,1,5);
plot(sched(i1).dt85g.vwc_pt1,sched(i1).accu_evap*c.m2mm,'bo','displayname','raw');hold on
plot(sched(i2).dt85g.vwc_pt1,sched(i2).accu_evap*c.m2mm,'bo','displayname','raw');hold on
xlabel('Saturation(-)');ylabel('accu. evap. (mm/day)')
savefig(h,file_name);


%file_name=[sched(i).tag,'_sensor.fig'];
%h=figure('name',file_name); 
%subplot(5,1,1)
%
%plot(sched(i).time_day_ay(1:iv:end),sched(i).dt85g.pres_pt1(1:iv:end),...
%    'ro','displayname','pres-pt1');hold on
%plot(sched(i).time_day_ay(1:iv:end),sched(i).dt85g.pres_pt2(1:iv:end),...
%    'go','displayname','pres-pt2');hold on
%plot(sched(i).time_day_ay(1:iv:end),sched(i).dt85g.pres_pt3(1:iv:end),...
%    'bo','displayname','pres-pt3');hold on
%plot(sched(i).time_day_ay(1:iv:end),sched(i).dt85g.pres_pt4(1:iv:end),...
%    'co','displayname','pres-pt4');hold on
%xlabel('time (day)')
%ylabel('pressure (pa)')
%legend('show','location','southeast')
%title(strcat(sched(i).tag,'_sensor conducted during ',sched(i).start_str,' and' ,sched(i).end_str)...
%	,'interpreter','none')
%%
subplot(5,1,2);
plot(sched(i1).time_day_ay(1:iv:end),sched(i).dt85g.temp_pt1(1:iv:end),...
    'ro','displayname','dt85-pt1');hold on
plot(sched(i1).time_day_ay(1:iv:end),sched(i).dt85g.temp_pt2(1:iv:end),...
    'go','displayname','dt85-pt2');hold on
plot(sched(i1).time_day_ay(1:iv:end),sched(i).dt85g.temp_pt3(1:iv:end),...
    'bo','displayname','dt85-pt3');hold on
plot(sched(i1).time_day_ay(1:iv:end),sched(i).dt85g.temp_pt4(1:iv:end),...
    'co','displayname','dt85-pt4');hold on
%plot(sched(i).time_day_ay,sched(i).em50.temp_pt4,...
%    'ms','displayname','em50-pt4');hold on
%plot(sched(i).time_day_ay,sched(i).em50.temp_pt5,...
%    'ks','displayname','em50-pt5');hold on
xlabel('time (day)')
ylabel('Temperature (pa)')
legend('show','location','southeast')
%
%subplot(5,1,3);
%plot(sched(i).time_day_ay(1:iv:end),sched(i).dt85g.vwc_pt1(1:iv:end),...
%    'ro','displayname','dt85-pt1');hold on
%plot(sched(i).time_day_ay(1:iv:end),sched(i).dt85g.vwc_pt2(1:iv:end),...
%    'go','displayname','dt85-pt2');hold on
%%plot(sched(i).time_day_ay,sched(i).dt85g.vwc_pt3,...
%%    'bo','displayname','dt85-pt3');hold on
%plot(sched(i).time_day_ay(1:iv:end),sched(i).dt85g.vwc_pt4(1:iv:end),...
%    'co','displayname','dt85-pt4');hold on
%%plot(sched(i).time_day_ay,sched(i).dt85g.vwc_pt5,...
%%    'mo','displayname','dt85-pt5');hold on
%plot(sched(i).time_day_ay(1:iv:end),sched(i).dt85g.vwc_pt6(1:iv:end),...
%    'ko','displayname','dt85-pt6');hold on
%xlabel('time (day)')
%ylabel('Volumetric Water content (-)')
%legend('show','location','southeast')
%
%subplot(5,1,4);
%plot(sched(i).time_day_ay(1:iv:end),sched(i).em50.rh_pt1(1:iv:end),...
%    'ro','displayname','em50-pt1');hold on
%plot(sched(i).time_day_ay(1:iv:end),sched(i).em50.rh_pt2(1:iv:end),...
%    'go','displayname','em50-pt2');hold on
%plot(sched(i).time_day_ay(1:iv:end),sched(i).em50.rh_pt3(1:iv:end),...
%    'bo','displayname','em50-pt3');hold on
%plot(sched(i).time_day_ay(1:iv:end),sched(i).em50.rh_pt4(1:iv:end),...
%    'co','displayname','em50-pt4');hold on
%%plot(sched(i).time_day_ay,sched(i).em50.rh_pt5,...
%%    'mo','displayname','em50-pt5');hold on
%xlabel('time (day)')
%ylabel('RelativeHumidity (pa)')
%legend('show','location','southeast')
%%
%%
%subplot(5,1,5);
%%plot(sched(i).time_day_ay,sched(i).em50.vwc_pt1,...
%%    'ro','displayname','em50-pt1');hold on
%%plot(sched(i).time_day_ay,sched(i).em50.vwc_pt2,...
%%    'go','displayname','em50-pt2');hold on
%%plot(sched(i).time_day_ay,sched(i).em50.vwc_pt3,...
%%    'bo','displayname','em50-pt3');hold on
%%xlim([0,25]);
%%xlabel('time (day)')
%%ylabel('VWC (-)')
%%legend('show','location','southeast')
%plot(sched(i).time_day_ay(1:iv:end),sched(i).em50.temp_pt1(1:iv:end),...
%    'ro','displayname','em50-pt1');hold on
%plot(sched(i).time_day_ay(1:iv:end),sched(i).em50.temp_pt2(1:iv:end),...
%    'go','displayname','em50-pt2');hold on
%plot(sched(i).time_day_ay(1:iv:end),sched(i).em50.temp_pt3(1:iv:end),...
%    'bo','displayname','em50-pt3');hold on
%plot(sched(i).time_day_ay(1:iv:end),sched(i).em50.temp_pt4(1:iv:end),...
%    'co','displayname','em50-pt4');hold on
%%plot(sched(i).time_day_ay,sched(i).em50.temp_pt5,...
%%    'mo','displayname','em50-pt5');hold on
%xlabel('time (day)')
%ylabel('Temperature (celsius)')
%legend('show','location','southeast')
%
%savefig(h,file_name)
%%
%%
%%subplot(4,2,5);
%%plot(sched(i).time_day_ay,sched(i).accu_evap,...
%%    'ro','displayname','scale-pt1');hold on
%%xlabel('time (day)')
%%ylabel('scale (g)')
%%legend('show','location','southeast')
%%
%%
%%subplot(4,2,6);
%%plot(sched(i).time_day_ay,sched(i).evap*c.ms2mmday,...
%%    'ro','displayname','scale-pt1');hold on
%%xlabel('time (day)')
%%ylabel('scale (g)')
%%legend('show','location','southeast')
