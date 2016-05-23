% this script transfers data from raw readings to specific schedules
for i =1 :length(sched)
%i=3;

%    % for dt85g. raw here means the direct extraction of data from datalogger.
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
    sched(i).raw.dt85g.vwc_pt1  =dt85g.vwc_pt1(dt85g_mask);
    sched(i).raw.dt85g.vwc_pt2  =dt85g.vwc_pt2(dt85g_mask);
    sched(i).raw.dt85g.vwc_pt3  =dt85g.vwc_pt3(dt85g_mask);
    sched(i).raw.dt85g.vwc_pt4  =dt85g.vwc_pt4(dt85g_mask);
    sched(i).raw.dt85g.vwc_pt5  =dt85g.vwc_pt5(dt85g_mask);
    sched(i).raw.dt85g.vwc_pt6  =dt85g.vwc_pt6(dt85g_mask);
    % for em50
    em50_mask=em50.time_digi>sched(i).start_digi&em50.time_digi<sched(i).end_digi;
    sched(i).raw.em50.time_digi=em50.time_digi(em50_mask);
    sched(i).raw.em50.rh_pt1 = em50.rh_pt1(em50_mask);
    sched(i).raw.em50.rh_pt2 = em50.rh_pt2(em50_mask);
    sched(i).raw.em50.rh_pt3 = em50.rh_pt3(em50_mask);
    sched(i).raw.em50.rh_pt4 = em50.rh_pt4(em50_mask);
    sched(i).raw.em50.rh_pt5 = em50.rh_pt5(em50_mask);
    sched(i).raw.em50.temp_pt1 = em50.temp_pt1(em50_mask);
    sched(i).raw.em50.temp_pt2 = em50.temp_pt2(em50_mask);
    sched(i).raw.em50.temp_pt3 = em50.temp_pt3(em50_mask);
    sched(i).raw.em50.temp_pt4 = em50.temp_pt4(em50_mask);
    sched(i).raw.em50.temp_pt5 = em50.temp_pt5(em50_mask);
    % for scale
    scale_mask=scale.time_digi>sched(i).start_digi&scale.time_digi<sched(i).end_digi;
    sched(i).raw.scale.time_digi=scale.time_digi(scale_mask);
    sched(i).raw.scale.water_loss=scale.weight(scale_mask,sched(i).scale_no);
       % clean data
     if strcmpi(sched(i).tag,'arcylic_large_pet')
     	sched(i).raw.scale.water_loss( sched(i).raw.scale.water_loss<1000  )=nan;
    end



    sched(i).raw.scale.water_loss_m=...
    	(sched(i).raw.scale.water_loss(1)-sched(i).raw.scale.water_loss)...
        *c.g2kg/c.rhow_pure_water/sched(i).surface_area;

    sched(i).time_day_ay=0:c.second2day*sched(i).dt:sched(i).duration_days;
    %sched(i).time_day_ay2=0:c.second2day*10*120:sched(i).duration_days;
    
    sched(i).accu_evap=csaps(sched(i).raw.scale.time_digi-sched(i).start_digi,...
        sched(i).raw.scale.water_loss_m,...
        0.8,sched(i).time_day_ay);



%    sched(i).accu_evap6=csaps(sched(i).raw.scale.time_digi-sched(i).start_digi,...
%        sched(i).raw.scale.water_loss_m,...
%        0.6,sched(i).time_day_ay);
%
%    sched(i).accu_evap1=csaps(sched(i).raw.scale.time_digi-sched(i).start_digi,...
%        sched(i).raw.scale.water_loss_m,...
%        0.1,sched(i).time_day_ay);
%    
%    sched(i).accu_evap05=csaps(sched(i).raw.scale.time_digi-sched(i).start_digi,...
%        sched(i).raw.scale.water_loss_m,...
%        0.05,sched(i).time_day_ay);
%
%    sched(i).accu_evap01=csaps(sched(i).raw.scale.time_digi-sched(i).start_digi,...
%        sched(i).raw.scale.water_loss_m,...
%        0.01,sched(i).time_day_ay);
%    sched(i).accu_evap005=csaps(sched(i).raw.scale.time_digi-sched(i).start_digi,...
%        sched(i).raw.scale.water_loss_m,...
%        0.005,sched(i).time_day_ay);
%    sched(i).accu_evap001=csaps(sched(i).raw.scale.time_digi-sched(i).start_digi,...
%        sched(i).raw.scale.water_loss_m,...
%        0.001,sched(i).time_day_ay);


% a thorough analysis was performed and found that a coefficient 0.00005 is the best
    %if i==1
    if strcmpi(sched(i).tag,'consolidometer')
%  to obtain an accurate 
	    sched(i).accu_evap=csaps(sched(i).raw.scale.time_digi-sched(i).start_digi,...
        sched(i).raw.scale.water_loss_m,...
        0.000005,sched(i).time_day_ay);
    %elseif i==2
    elseif strcmpi(sched(i).tag,'arcylic_large_pet')
	sched(i).accu_evap=csaps(sched(i).raw.scale.time_digi-sched(i).start_digi,...
          sched(i).raw.scale.water_loss_m,...
           0.00005,sched(i).time_day_ay); %ok but a neg evt
           %0.0005,sched(i).time_day_ay); %ok but a neg evt
           %0.005,sched(i).time_day_ay); %ok but a neg evt
           %0.05,sched(i).time_day_ay); %bad
           %0.00001,sched(i).time_day_ay);
	   %0.005 ok for 
    elseif strcmpi(sched(i).tag,'arcylic_small_pet')
	sched(i).accu_evap=csaps(sched(i).raw.scale.time_digi-sched(i).start_digi,...
          sched(i).raw.scale.water_loss_m,...
           0.005,sched(i).time_day_ay);
   end

% very good results
%    sched(i).accu_evap=csaps(sched(i).raw.scale.time_digi-sched(i).start_digi,...
%        sched(i).raw.scale.water_loss_m,...
%        0.000005,sched(i).time_day_ay);
% good results
%    sched(i).accu_evap=csaps(sched(i).raw.scale.time_digi-sched(i).start_digi,...
%        sched(i).raw.scale.water_loss_m,...
%        0.00001,sched(i).time_day_ay);



%    sched(i).accu_evap_sp2=csaps(sched(i).scale.time_digi-sched(i).start_digi,...
%        sched(i).scale.water_loss_m,...
%        0.8,sched(i).time_day_ay2);

    %sched(i).evap_sp3=[diff(sched(i).accu_evap_sp2)/1200,nan];

    sched(i).evap=[diff(sched(i).accu_evap)/sched(i).dt,nan];
    sched(i).raw.scale.evap=[diff(sched(i).raw.scale.water_loss_m)'/sched(i).dt,nan];


    %sched(i).evap_sp2=csaps(sched(i).time_day_ay,sched(i).evap_sp,0.8,sched(i).time_day_ay2);

    %  dt85g
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
    sched(i).dt85g.vwc_pt1 =csaps(sched(i).raw.dt85g.time_digi-sched(i).start_digi...
        ,sched(i).raw.dt85g.vwc_pt1,0.8,sched(i).time_day_ay);
    sched(i).dt85g.vwc_pt2 =csaps(sched(i).raw.dt85g.time_digi-sched(i).start_digi...
        ,sched(i).raw.dt85g.vwc_pt2,0.8,sched(i).time_day_ay);
    sched(i).dt85g.vwc_pt3 =csaps(sched(i).raw.dt85g.time_digi-sched(i).start_digi...
        ,sched(i).raw.dt85g.vwc_pt3,0.8,sched(i).time_day_ay);
    sched(i).dt85g.vwc_pt4 =csaps(sched(i).raw.dt85g.time_digi-sched(i).start_digi...
        ,sched(i).raw.dt85g.vwc_pt4,0.8,sched(i).time_day_ay);
    sched(i).dt85g.vwc_pt5 =csaps(sched(i).raw.dt85g.time_digi-sched(i).start_digi...
        ,sched(i).raw.dt85g.vwc_pt5,0.8,sched(i).time_day_ay);
    sched(i).dt85g.vwc_pt6 =csaps(sched(i).raw.dt85g.time_digi-sched(i).start_digi...
        ,sched(i).raw.dt85g.vwc_pt6,0.8,sched(i).time_day_ay);

    % for em50
    sched(i).em50.rh_pt1 = csaps(sched(i).raw.em50.time_digi-sched(i).start_digi...
        ,sched(i).raw.em50.rh_pt1,0.8,sched(i).time_day_ay);
    sched(i).em50.rh_pt2  = csaps(sched(i).raw.em50.time_digi-sched(i).start_digi...
        ,sched(i).raw.em50.rh_pt2,0.8,sched(i).time_day_ay);
    sched(i).em50.rh_pt3  = csaps(sched(i).raw.em50.time_digi-sched(i).start_digi...
        ,sched(i).raw.em50.rh_pt3,0.8,sched(i).time_day_ay);
    sched(i).em50.temp_pt1 = csaps(sched(i).raw.em50.time_digi-sched(i).start_digi...
        ,sched(i).raw.em50.temp_pt1,0.8,sched(i).time_day_ay);
    sched(i).em50.temp_pt2  = csaps(sched(i).raw.em50.time_digi-sched(i).start_digi...
        ,sched(i).raw.em50.temp_pt2,0.8,sched(i).time_day_ay);
    sched(i).em50.temp_pt3  = csaps(sched(i).raw.em50.time_digi-sched(i).start_digi...
        ,sched(i).raw.em50.temp_pt3,0.8,sched(i).time_day_ay);
    sched(i).em50.rh_pt4   = csaps(sched(i).raw.em50.time_digi-sched(i).start_digi...
        ,sched(i).raw.em50.rh_pt4,0.8,sched(i).time_day_ay);
    sched(i).em50.temp_pt4 = csaps(sched(i).raw.em50.time_digi-sched(i).start_digi...
        ,sched(i).raw.em50.temp_pt4,0.8,sched(i).time_day_ay);
    %sched(i).em50.rh_pt5   = csaps(sched(i).raw.em50.time_digi-sched(i).start_digi...
    %    ,sched(i).raw.em50.rh_pt5,0.8,sched(i).time_day_ay);
    %sched(i).em50.temp_pt5 = csaps(sched(i).raw.em50.time_digi-sched(i).start_digi...
    %    ,sched(i).raw.em50.temp_pt5,0.8,sched(i).time_day_ay);
end
%% check if spline interpolated evt is working
%figure;
%%subplot(3,1,1);
%plot(sched(i).time_day_ay,sched(i).accu_evap,'ro');hold on
%plot( sched(i).raw.scale.time_digi-sched(i).start_digi,...
%    sched(i).raw.scale.water_loss_m,'go')
%%plot(sched(i).scale.time_digi-sched(i).start_digi,sched(i).scale.water_loss_m,'go');hold on
%
%
%figure;
%subplot(3,1,1);
%plot(sched(i).time_day_ay,sched(i).accu_evap,'ro');hold on
%plot( sched(i).raw.scale.time_digi-sched(i).start_digi,...
%    sched(i).raw.scale.water_loss_m,'go')
%
%
%%plot(sched(i).time_day_ay,sched(i).accu_evap,'ro');hold on
%%plot( sched(i).raw.scale.time_digi,...
%%    sched(i).raw.scale.water_loss,'go')
%%    datetick('x','DD/mmm')
%
%
%xlabel('Time(day)');ylabel('cumulative evaporation (mm)')
%%plot(sched(i).time_day_ay-sched(i).start_digi,sched(i).accu_evap,'go');hold on
%
%
%subplot(3,1,2);
%plot(sched(i).time_day_ay,sched(i).evap*c.ms2mmday,'ro');hold on
%xlabel('Time(day)');ylabel('evaporation rate (mm/day)')
%%plot(sched(i).time_day_ay2,sched(i).evap_sp2*c.ms2mmday,'go');hold on
%%plot(sched(i).time_day_ay2,sched(i).evap_sp3*c.ms2mmday,'bo');hold on
%%plot(sched(i).scale.time_digi-sched(i).start_digi,sched(i).scale.evap*c.ms2mmday,'go');hold on
%subplot(3,1,3);
%%figure;
%plot(sched(i).raw.scale.time_digi-sched(i).raw.scale.time_digi(1),...
%sched(i).raw.scale.water_loss_m,'r-','displayname','raw');hold on
%%plot(sched(i).time_day_ay,sched(i).accu_evap,'g-','displayname','0.8');hold on
%%plot(sched(i).time_day_ay,sched(i).accu_evap6,'b-','displayname','0.6');hold on
%%plot(sched(i).time_day_ay,sched(i).accu_evap1,'g-','displayname','0.1');hold on
%%plot(sched(i).time_day_ay,sched(i).accu_evap05,'c-','displayname','0.05');hold on
%%plot(sched(i).time_day_ay,sched(i).accu_evap01,'m-','displayname','0.01');hold on
%%plot(sched(i).time_day_ay,sched(i).accu_evap005,'k-','displayname','0.005');hold on
%%plot(sched(i).time_day_ay,sched(i).accu_evap001,'k-','displayname','0.001');hold on
%
%
%%i=2;
%figure; 
%subplot(5,1,1)
%plot(sched(i).time_day_ay,sched(i).dt85g.pres_pt1,...
%    'ro','displayname','pres-pt1');hold on
%plot(sched(i).time_day_ay,sched(i).dt85g.pres_pt2,...
%    'go','displayname','pres-pt2');hold on
%plot(sched(i).time_day_ay,sched(i).dt85g.pres_pt3,...
%    'bo','displayname','pres-pt3');hold on
%plot(sched(i).time_day_ay,sched(i).dt85g.pres_pt4,...
%    'co','displayname','pres-pt4');hold on
%xlabel('time (day)')
%ylabel('pressure (pa)')
%legend('show','location','southeast')
%%
%subplot(5,1,2);
%%figure
%plot(sched(i).time_day_ay,sched(i).dt85g.temp_pt1,...
%    'ro','displayname','dt85-pt1');hold on
%plot(sched(i).time_day_ay,sched(i).dt85g.temp_pt2,...
%    'go','displayname','dt85-pt2');hold on
%plot(sched(i).time_day_ay,sched(i).dt85g.temp_pt3,...
%    'bo','displayname','dt85-pt3');hold on
%plot(sched(i).time_day_ay,sched(i).dt85g.temp_pt4,...
%    'co','displayname','dt85-pt4');hold on
%%plot(sched(i).time_day_ay,sched(i).em50.temp_pt4,...
%%    'ms','displayname','em50-pt4');hold on
%%plot(sched(i).time_day_ay,sched(i).em50.temp_pt5,...
%%    'ks','displayname','em50-pt5');hold on
%xlabel('time (day)')
%ylabel('Temperature (pa)')
%legend('show','location','southeast')
%
%
%%figure
%subplot(5,1,3);
%plot(sched(i).time_day_ay,sched(i).dt85g.vwc_pt1,...
%    'ro','displayname','dt85-pt1');hold on
%plot(sched(i).time_day_ay,sched(i).dt85g.vwc_pt2,...
%    'go','displayname','dt85-pt2');hold on
%plot(sched(i).time_day_ay,sched(i).dt85g.vwc_pt3,...
%    'bo','displayname','dt85-pt3');hold on
%plot(sched(i).time_day_ay,sched(i).dt85g.vwc_pt4,...
%    'co','displayname','dt85-pt4');hold on
%plot(sched(i).time_day_ay,sched(i).dt85g.vwc_pt5,...
%    'mo','displayname','dt85-pt5');hold on
%plot(sched(i).time_day_ay,sched(i).dt85g.vwc_pt6,...
%    'ko','displayname','dt85-pt6');hold on
%xlabel('time (day)')
%ylabel('Volumetric Water content (-)')
%legend('show','location','southeast')
%
%%
%%
%subplot(5,1,4);
%plot(sched(i).time_day_ay,sched(i).em50.rh_pt1,...
%    'ro','displayname','em50-pt1');hold on
%plot(sched(i).time_day_ay,sched(i).em50.rh_pt2,...
%    'go','displayname','em50-pt2');hold on
%plot(sched(i).time_day_ay,sched(i).em50.rh_pt3,...
%    'bo','displayname','em50-pt3');hold on
%plot(sched(i).time_day_ay,sched(i).em50.rh_pt4,...
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
%plot(sched(i).time_day_ay,sched(i).em50.temp_pt1,...
%    'ro','displayname','em50-pt1');hold on
%plot(sched(i).time_day_ay,sched(i).em50.temp_pt2,...
%    'go','displayname','em50-pt2');hold on
%plot(sched(i).time_day_ay,sched(i).em50.temp_pt3,...
%    'bo','displayname','em50-pt3');hold on
%plot(sched(i).time_day_ay,sched(i).em50.temp_pt4,...
%    'co','displayname','em50-pt4');hold on
%%plot(sched(i).time_day_ay,sched(i).em50.temp_pt5,...
%%    'mo','displayname','em50-pt5');hold on
%xlabel('time (day)')
%ylabel('Temperature (celsius)')
%legend('show','location','southeast')
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
