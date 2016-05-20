% this script transfers data from raw readings to specific schedules
for i =1 :length(sched)
    % for dt85g. raw here means the direct extraction of data from datalogger.
    dt85g_mask=dt85g.time_digi>sched(i).start_digi&dt85g.time_digi<sched(i).end_digi;
    sched(i).raw.dt85g.time_digi=dt85g.time_digi(dt85g_mask);
    sched(i).raw.dt85g.pres_pt1 =dt85g.pres_pt1(dt85g_mask);
    sched(i).raw.dt85g.temp_pt1 =dt85g.temp_pt1(dt85g_mask);
    sched(i).raw.dt85g.pres_pt2 =dt85g.pres_pt2(dt85g_mask);
    sched(i).raw.dt85g.temp_pt2 =dt85g.temp_pt2(dt85g_mask);
    sched(i).raw.dt85g.pres_pt3 =dt85g.pres_pt3(dt85g_mask);
    sched(i).raw.dt85g.temp_pt3 =dt85g.temp_pt3(dt85g_mask);
    sched(i).raw.dt85g.pres_pt4 =dt85g.pres_pt4(dt85g_mask);
    sched(i).raw.dt85g.temp_pt4 =dt85g.temp_pt4(dt85g_mask);
    % for em50
    em50_mask=em50.time_digi>sched(i).start_digi&em50.time_digi<sched(i).end_digi;
    sched(i).raw.em50.time_digi=em50.time_digi(em50_mask);
    sched(i).raw.em50.vwc_pt1 = em50.vwc_pt1(em50_mask);
    sched(i).raw.em50.vwc_pt2 = em50.vwc_pt2(em50_mask);
    sched(i).raw.em50.vwc_pt3 = em50.vwc_pt3(em50_mask);
    sched(i).raw.em50.rh_pt4 = em50.rh_pt4(em50_mask);
    sched(i).raw.em50.temp_pt4 = em50.temp_pt4(em50_mask);
    sched(i).raw.em50.rh_pt5 = em50.rh_pt5(em50_mask);
    sched(i).raw.em50.temp_pt5 = em50.temp_pt5(em50_mask);
    % for scale
    scale_mask=scale.time_digi>sched(i).start_digi&scale.time_digi<sched(i).end_digi;
    sched(i).raw.scale.time_digi=scale.time_digi(scale_mask);
    sched(i).raw.scale.water_loss=scale.weight(scale_mask);
    sched(i).raw.scale.water_loss_m=(sched(i).raw.scale.water_loss(1)-sched(i).raw.scale.water_loss)...
        *c.g2kg/c.rhow_pure_water/sched(i).surface_area;

    sched(i).time_day_ay=0:c.second2day*sched(i).dt:sched(i).duration_days;
    %sched(i).time_day_ay2=0:c.second2day*10*120:sched(i).duration_days;
    
    sched(i).accu_evap=csaps(sched(i).raw.scale.time_digi-sched(i).start_digi,...
        sched(i).raw.scale.water_loss_m,...
        0.8,sched(i).time_day_ay);

%    sched(i).accu_evap_sp2=csaps(sched(i).scale.time_digi-sched(i).start_digi,...
%        sched(i).scale.water_loss_m,...
%        0.8,sched(i).time_day_ay2);

    %sched(i).evap_sp3=[diff(sched(i).accu_evap_sp2)/1200,nan];

    sched(i).evap=[diff(sched(i).accu_evap)/sched(i).dt,nan];
    sched(i).raw.scale.evap=[diff(sched(i).raw.scale.water_loss_m)'/sched(i).dt,nan];
    %sched(i).evap_sp2=csaps(sched(i).time_day_ay,sched(i).evap_sp,0.8,sched(i).time_day_ay2);
    sched(i).dt85g.pres_pt1 =csaps(sched(i).raw.dt85g.time_digi-sched(i).start_digi...
        ,sched(i).raw.dt85g.pres_pt1,0.8,sched(i).time_day_ay);
    sched(i).dt85g.temp_pt1 =csaps(sched(i).raw.dt85g.time_digi-sched(i).start_digi...
        ,sched(i).raw.dt85g.temp_pt1,0.8,sched(i).time_day_ay);
    sched(i).dt85g.pres_pt2 =csaps(sched(i).raw.dt85g.time_digi-sched(i).start_digi...
        ,sched(i).raw.dt85g.pres_pt2,0.8,sched(i).time_day_ay);
    sched(i).dt85g.temp_pt2 =csaps(sched(i).raw.dt85g.time_digi-sched(i).start_digi...
        ,sched(i).raw.dt85g.temp_pt2,0.8,sched(i).time_day_ay);
    sched(i).dt85g.pres_pt3 =csaps(sched(i).raw.dt85g.time_digi-sched(i).start_digi...
        ,sched(i).raw.dt85g.pres_pt3,0.8,sched(i).time_day_ay);
    sched(i).dt85g.temp_pt3 =csaps(sched(i).raw.dt85g.time_digi-sched(i).start_digi...
        ,sched(i).raw.dt85g.temp_pt3,0.8,sched(i).time_day_ay);
    sched(i).dt85g.pres_pt4 =csaps(sched(i).raw.dt85g.time_digi-sched(i).start_digi...
        ,sched(i).raw.dt85g.pres_pt4,0.8,sched(i).time_day_ay);
    sched(i).dt85g.temp_pt4 =csaps(sched(i).raw.dt85g.time_digi-sched(i).start_digi...
        ,sched(i).raw.dt85g.temp_pt4,0.8,sched(i).time_day_ay);
    % for em50
    sched(i).em50.vwc_pt1 = csaps(sched(i).raw.em50.time_digi-sched(i).start_digi...
        ,sched(i).raw.em50.vwc_pt1,0.8,sched(i).time_day_ay);
    sched(i).em50.vwc_pt2  = csaps(sched(i).raw.em50.time_digi-sched(i).start_digi...
        ,sched(i).raw.em50.vwc_pt2,0.8,sched(i).time_day_ay);
    sched(i).em50.vwc_pt3  = csaps(sched(i).raw.em50.time_digi-sched(i).start_digi...
        ,sched(i).raw.em50.vwc_pt3,0.8,sched(i).time_day_ay);
    sched(i).em50.rh_pt4   = csaps(sched(i).raw.em50.time_digi-sched(i).start_digi...
        ,sched(i).raw.em50.rh_pt4,0.8,sched(i).time_day_ay);
    sched(i).em50.temp_pt4 = csaps(sched(i).raw.em50.time_digi-sched(i).start_digi...
        ,sched(i).raw.em50.temp_pt4,0.8,sched(i).time_day_ay);
    sched(i).em50.rh_pt5   = csaps(sched(i).raw.em50.time_digi-sched(i).start_digi...
        ,sched(i).raw.em50.rh_pt5,0.8,sched(i).time_day_ay);
    sched(i).em50.temp_pt5 = csaps(sched(i).raw.em50.time_digi-sched(i).start_digi...
        ,sched(i).raw.em50.temp_pt5,0.8,sched(i).time_day_ay);
end


% check if spline interpolated evt is working
figure;
subplot(2,1,1);
plot(sched(i).time_day_ay,sched(i).accu_evap,'ro');hold on
%plot(sched(i).scale.time_digi-sched(i).start_digi,sched(i).scale.water_loss_m,'go');hold on
subplot(2,1,2);
plot(sched(i).time_day_ay,sched(i).evap*c.ms2mmday,'ro');hold on
%plot(sched(i).time_day_ay2,sched(i).evap_sp2*c.ms2mmday,'go');hold on
%plot(sched(i).time_day_ay2,sched(i).evap_sp3*c.ms2mmday,'bo');hold on
%plot(sched(i).scale.time_digi-sched(i).start_digi,sched(i).scale.evap*c.ms2mmday,'go');hold on

i=2;
figure; 
subplot(4,2,1)
plot(sched(i).time_day_ay,sched(i).dt85g.pres_pt1,...
    'ro','displayname','dt85-pt1');hold on
plot(sched(i).time_day_ay,sched(i).dt85g.pres_pt2,...
    'go','displayname','dt85-pt1');hold on
plot(sched(i).time_day_ay,sched(i).dt85g.pres_pt3,...
    'bo','displayname','dt85-pt3');hold on
plot(sched(i).time_day_ay,sched(i).dt85g.pres_pt3,...
    'co','displayname','dt85-pt4');hold on
xlabel('time (day)')
ylabel('pressure (pa)')
legend('show','location','southeast')

subplot(4,2,2);
plot(sched(i).time_day_ay,sched(i).dt85g.temp_pt1,...
    'ro','displayname','dt85-pt1');hold on
plot(sched(i).time_day_ay,sched(i).dt85g.temp_pt2,...
    'go','displayname','dt85-pt2');hold on
plot(sched(i).time_day_ay,sched(i).dt85g.temp_pt3,...
    'bo','displayname','dt85-pt3');hold on
plot(sched(i).time_day_ay,sched(i).dt85g.temp_pt4,...
    'co','displayname','dt85-pt4');hold on
plot(sched(i).time_day_ay,sched(i).em50.temp_pt4,...
    'ms','displayname','em50-pt4');hold on
plot(sched(i).time_day_ay,sched(i).em50.temp_pt5,...
    'ks','displayname','em50-pt5');hold on
xlabel('time (day)')
ylabel('Temperature (pa)')
legend('show','location','southeast')


subplot(4,2,3);
plot(sched(i).time_day_ay,sched(i).em50.rh_pt4,...
    'ro','displayname','em50-pt4');hold on
plot(sched(i).time_day_ay,sched(i).em50.rh_pt5,...
    'go','displayname','em50-pt5');hold on
xlabel('time (day)')
ylabel('RelativeHumidity (pa)')
legend('show','location','southeast')


subplot(4,2,4);
plot(sched(i).time_day_ay,sched(i).em50.vwc_pt1,...
    'ro','displayname','em50-pt1');hold on
plot(sched(i).time_day_ay,sched(i).em50.vwc_pt2,...
    'go','displayname','em50-pt2');hold on
plot(sched(i).time_day_ay,sched(i).em50.vwc_pt3,...
    'bo','displayname','em50-pt3');hold on
xlim([0,25]);
xlabel('time (day)')
ylabel('VWC (-)')
legend('show','location','southeast')


subplot(4,2,5);
plot(sched(i).time_day_ay,sched(i).accu_evap,...
    'ro','displayname','scale-pt1');hold on
xlabel('time (day)')
ylabel('scale (g)')
legend('show','location','southeast')


subplot(4,2,6);
plot(sched(i).time_day_ay,sched(i).evap*c.ms2mmday,...
    'ro','displayname','scale-pt1');hold on
xlabel('time (day)')
ylabel('scale (g)')
legend('show','location','southeast')
