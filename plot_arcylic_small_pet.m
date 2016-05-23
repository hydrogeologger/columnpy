i=find(strcmpi({sched.tag},'arcylic_small_pet'));


file_name=strcat(sched(i).tag,'_evt.fig');
h=figure('Name',file_name);
subplot(3,1,1);
plot(sched(i).time_day_ay,sched(i).accu_evap,'ro');hold on
plot( sched(i).raw.scale.time_digi-sched(i).start_digi,...
    sched(i).raw.scale.water_loss_m,'go')
title(strcat(sched(i).tag,'_evt conducted during ',sched(i).start_str,' and' ,sched(i).end_str)...
	,'interpreter','none')


%plot(sched(i).time_day_ay,sched(i).accu_evap,'ro');hold on
%plot( sched(i).raw.scale.time_digi,...
%    sched(i).raw.scale.water_loss,'go')
%    datetick('x','DD/mmm')

xlabel('Time(day)');ylabel('cumulative evaporation (mm)')
%plot(sched(i).time_day_ay-sched(i).start_digi,sched(i).accu_evap,'go');hold on

subplot(3,1,2);
plot(sched(i).time_day_ay,sched(i).evap*c.ms2mmday,'ro');hold on
xlabel('Time(day)');ylabel('evaporation rate (mm/day)')
%plot(sched(i).time_day_ay2,sched(i).evap_sp2*c.ms2mmday,'go');hold on
%plot(sched(i).time_day_ay2,sched(i).evap_sp3*c.ms2mmday,'bo');hold on
%plot(sched(i).scale.time_digi-sched(i).start_digi,sched(i).scale.evap*c.ms2mmday,'go');hold on
subplot(3,1,3);
plot(sched(i).raw.scale.time_digi-sched(i).raw.scale.time_digi(1),...
sched(i).raw.scale.water_loss_m,'r-','displayname','raw');hold on
%plot(sched(i).time_day_ay,sched(i).accu_evap,'g-','displayname','0.8');hold on
%plot(sched(i).time_day_ay,sched(i).accu_evap6,'b-','displayname','0.6');hold on
%plot(sched(i).time_day_ay,sched(i).accu_evap1,'g-','displayname','0.1');hold on
%plot(sched(i).time_day_ay,sched(i).accu_evap05,'c-','displayname','0.05');hold on
%plot(sched(i).time_day_ay,sched(i).accu_evap01,'m-','displayname','0.01');hold on
%plot(sched(i).time_day_ay,sched(i).accu_evap005,'k-','displayname','0.005');hold on
%plot(sched(i).time_day_ay,sched(i).accu_evap001,'k-','displayname','0.001');hold on
xlabel('Time(day)');ylabel('raw_water_loss (m)')
savefig(h,file_name);



file_name=[sched(i).tag,'_sensor.fig'];
h=figure('name',file_name); 
subplot(5,1,1)

plot(sched(i).time_day_ay,sched(i).dt85g.pres_pt1,...
    'ro','displayname','pres-pt1');hold on
plot(sched(i).time_day_ay,sched(i).dt85g.pres_pt2,...
    'go','displayname','pres-pt2');hold on
plot(sched(i).time_day_ay,sched(i).dt85g.pres_pt3,...
    'bo','displayname','pres-pt3');hold on
plot(sched(i).time_day_ay,sched(i).dt85g.pres_pt4,...
    'co','displayname','pres-pt4');hold on
xlabel('time (day)')
ylabel('pressure (pa)')
legend('show','location','southeast')
title(strcat(sched(i).tag,'_sensor conducted during ',sched(i).start_str,' and' ,sched(i).end_str)...
	,'interpreter','none')
%
subplot(5,1,2);
plot(sched(i).time_day_ay,sched(i).dt85g.temp_pt1,...
    'ro','displayname','dt85-pt1');hold on
plot(sched(i).time_day_ay,sched(i).dt85g.temp_pt2,...
    'go','displayname','dt85-pt2');hold on
plot(sched(i).time_day_ay,sched(i).dt85g.temp_pt3,...
    'bo','displayname','dt85-pt3');hold on
plot(sched(i).time_day_ay,sched(i).dt85g.temp_pt4,...
    'co','displayname','dt85-pt4');hold on
%plot(sched(i).time_day_ay,sched(i).em50.temp_pt4,...
%    'ms','displayname','em50-pt4');hold on
%plot(sched(i).time_day_ay,sched(i).em50.temp_pt5,...
%    'ks','displayname','em50-pt5');hold on
xlabel('time (day)')
ylabel('Temperature (pa)')
legend('show','location','southeast')

subplot(5,1,3);
plot(sched(i).time_day_ay,sched(i).dt85g.vwc_pt1,...
    'ro','displayname','dt85-pt1');hold on
plot(sched(i).time_day_ay,sched(i).dt85g.vwc_pt2,...
    'go','displayname','dt85-pt2');hold on
%plot(sched(i).time_day_ay,sched(i).dt85g.vwc_pt3,...
%    'bo','displayname','dt85-pt3');hold on
plot(sched(i).time_day_ay,sched(i).dt85g.vwc_pt4,...
    'co','displayname','dt85-pt4');hold on
%plot(sched(i).time_day_ay,sched(i).dt85g.vwc_pt5,...
%    'mo','displayname','dt85-pt5');hold on
plot(sched(i).time_day_ay,sched(i).dt85g.vwc_pt6,...
    'ko','displayname','dt85-pt6');hold on
xlabel('time (day)')
ylabel('Volumetric Water content (-)')
legend('show','location','southeast')

subplot(5,1,4);
plot(sched(i).time_day_ay,sched(i).em50.rh_pt1,...
    'ro','displayname','em50-pt1');hold on
plot(sched(i).time_day_ay,sched(i).em50.rh_pt2,...
    'go','displayname','em50-pt2');hold on
plot(sched(i).time_day_ay,sched(i).em50.rh_pt3,...
    'bo','displayname','em50-pt3');hold on
plot(sched(i).time_day_ay,sched(i).em50.rh_pt4,...
    'co','displayname','em50-pt4');hold on
%plot(sched(i).time_day_ay,sched(i).em50.rh_pt5,...
%    'mo','displayname','em50-pt5');hold on
xlabel('time (day)')
ylabel('RelativeHumidity (pa)')
legend('show','location','southeast')
%
%
subplot(5,1,5);
%plot(sched(i).time_day_ay,sched(i).em50.vwc_pt1,...
%    'ro','displayname','em50-pt1');hold on
%plot(sched(i).time_day_ay,sched(i).em50.vwc_pt2,...
%    'go','displayname','em50-pt2');hold on
%plot(sched(i).time_day_ay,sched(i).em50.vwc_pt3,...
%    'bo','displayname','em50-pt3');hold on
%xlim([0,25]);
%xlabel('time (day)')
%ylabel('VWC (-)')
%legend('show','location','southeast')
plot(sched(i).time_day_ay,sched(i).em50.temp_pt1,...
    'ro','displayname','em50-pt1');hold on
plot(sched(i).time_day_ay,sched(i).em50.temp_pt2,...
    'go','displayname','em50-pt2');hold on
plot(sched(i).time_day_ay,sched(i).em50.temp_pt3,...
    'bo','displayname','em50-pt3');hold on
plot(sched(i).time_day_ay,sched(i).em50.temp_pt4,...
    'co','displayname','em50-pt4');hold on
%plot(sched(i).time_day_ay,sched(i).em50.temp_pt5,...
%    'mo','displayname','em50-pt5');hold on
xlabel('time (day)')
ylabel('Temperature (celsius)')
legend('show','location','southeast')

savefig(h,file_name)
%
%
%subplot(4,2,5);
%plot(sched(i).time_day_ay,sched(i).accu_evap,...
%    'ro','displayname','scale-pt1');hold on
%xlabel('time (day)')
%ylabel('scale (g)')
%legend('show','location','southeast')
%
%
%subplot(4,2,6);
%plot(sched(i).time_day_ay,sched(i).evap*c.ms2mmday,...
%    'ro','displayname','scale-pt1');hold on
%xlabel('time (day)')
%ylabel('scale (g)')
%legend('show','location','southeast')
