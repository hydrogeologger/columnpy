% read dt85g em50 scale based on the schedule time.ipt
% cali.ipt saves the calibrated data for each sensors applied
% time.ipt saves the information of each sinario, including start time, end time, heat input, water level and soil type
% this file is writtent by Chenming Zhang in 2012
%clear all
%tic
%% some constants

% water density
col=zeros(7,3);
col(2,:)=[0 1 0]; % g
col(4,:)=[0 1 1]; % c
col(5,:)=[1 0 1]; % m
%col(6,:)=[1 1 0]; % y
col(6,:)=[0 0 0]; % k
col(7,:)=[0 0 0]; % k
col(9,:)=[1 0 0]; % r
rholw=1000;
% m/s to mm/day
ms2mmd=3600*24*1000;
% (C)ross (S)ection (A)rea of the (6)0cm column (m2)
%csa6=3.1415926*0.055^2;
%csa9=3.1415926*0.085^2;
%% ---------read file---------------
% the ',' is delimiter
dt85g=importdata('dt85g.csv',',');
%% obtain calibration parameters from file cali.inp
%cali=importdata('cali_Medium.ipt');
% (C)alibration (P)arameter for (M)oisture (C)ontent at DT(8)5G (C) Channel [cmc8c]
%cmc8c=cali.data(1,:)';
%cmc8d=cali.data(2,:)';
%cmc8e=cali.data(3,:)';
%cmc8f=cali.data(4,:)';
% (C)alibration (P)arameter for (P)ressure at DT(8)5G (B) Channel [cp8b]
%cp8b=cali.data(5,:)';
%cp8g=cali.data(6,:)';
ec=struct;
ec5(1).full_sat_rs=844.6;ec5(1).zero_sat_rs=380;ec5(1).alpha=(1-0)/(ec5(1).full_sat_rs-ec5(1).zero_sat_rs);  ec5(1).beta=-ec5(1).zero_sat_rs/(ec5(1).full_sat_rs-ec5(1).zero_sat_rs);
ec5(2).full_sat_rs=819.4;ec5(2).zero_sat_rs=380;ec5(2).alpha=(1-0)/(ec5(2).full_sat_rs-ec5(2).zero_sat_rs);  ec5(2).beta=-ec5(2).zero_sat_rs/(ec5(2).full_sat_rs-ec5(2).zero_sat_rs);
ec5(3).full_sat_rs=0.03; ec5(3).zero_sat_rs=.05;ec5(3).alpha=(1-0)/(ec5(3).full_sat_rs-ec5(3).zero_sat_rs);  ec5(3).beta=-ec5(3).zero_sat_rs/(ec5(3).full_sat_rs-ec5(3).zero_sat_rs);
ec5(4).full_sat_rs=819.4;ec5(4).zero_sat_rs=380;ec5(4).alpha=(1-0)/(ec5(4).full_sat_rs-ec5(4).zero_sat_rs);  ec5(4).beta=-ec5(4).zero_sat_rs/(ec5(4).full_sat_rs-ec5(4).zero_sat_rs);
ec5(5).full_sat_rs=837.2;ec5(5).zero_sat_rs=380;ec5(5).alpha=(1-0)/(ec5(5).full_sat_rs-ec5(5).zero_sat_rs);  ec5(5).beta=-ec5(5).zero_sat_rs/(ec5(5).full_sat_rs-ec5(5).zero_sat_rs);
ec5(6).full_sat_rs=837.2;ec5(6).zero_sat_rs=500;ec5(6).alpha=(1-0)/(ec5(6).full_sat_rs-ec5(6).zero_sat_rs);  ec5(6).beta=-ec5(6).zero_sat_rs/(ec5(6).full_sat_rs-ec5(6).zero_sat_rs);
ec5(1).gama=1;
ec5(2).gama=1;
ec5(3).gama=1;
ec5(4).gama=1;
ec5(5).gama=1;
ec5(6).gama=1;




% 450

%% interpolate the result from dt85g
% for ec5 Moisture Content(MC)=Reading*A+B
% ec5c A=0.003846; B=-1.461538;
% ec5d A=0.00454545;B=-1.5;
% ec5e A=0.00333333;B=-1.5;
% ec5f A=0.00454545;B=-1.59090;
% ac=0.003846;bc=-1.461538;
% ad=0.00454545;bd=-1.5;
% ae=0.00333333;be=-1.5;
% af=0.00454545;bf=-1.59090;

% (M)oisture (C)ontent from dt(8)5g, channel (C) (mcc)
% mc8c=dt85g.data(:,8)*ac+bc;
% mc8d=dt85g.data(:,9)*ad+bd;
% mc8e=dt85g.data(:,10)*ae+be;
% mc8f=dt85g.data(:,11)*af+bf;

% % --- convert electrical conductivity to moisture content based on linearized fitting
% mc8c=dt85g.data(:,16)*cmc8c(1)+cmc8c(2);
% % mc8d=dt85g.data(:,17)*cmc8d(1)+cmc8d(2);
% mc8e=dt85g.data(:,18)*cmc8e(1)+cmc8e(2);
% mc8f=dt85g.data(:,19)*cmc8f(1)+cmc8f(2);
% 
% % --- convert electrical conductivity to moisture content based on Two point alpha mixing model
% mc8d= (dt85g.data(:,17).^cmc8d(5)-cmc8d(4)^cmc8d(5) )  /  ( cmc8d(3)^cmc8d(5) -cmc8d(4)^cmc8d(5));


% --- convert electrical conductivity to moisture content based on linearized fitting
%if cmc8c(1)==1
%mc8c=dt85g.data(:,16)*cmc8c(2)+cmc8c(3);
%elseif cmc8c(1)==2
%mc8c= (dt85g.data(:,16).^cmc8c(6)-cmc8c(5)^cmc8c(6) )  /  ( cmc8c(4)^cmc8c(6) -cmc8c(5)^cmc8c(6));
%end
%    
%if cmc8d(1)==1
%mc8d=dt85g.data(:,17)*cmc8d(2)+cmc8d(3);
%elseif cmc8d(1)==2
%% --- convert electrical conductivity to moisture content based on Two point alpha mixing model
%mc8d= (dt85g.data(:,17).^cmc8d(6)-cmc8d(5)^cmc8d(6) )  /  ( cmc8d(4)^cmc8d(6) -cmc8d(5)^cmc8d(6));
%end
%
%
%if cmc8e(1)==1
%mc8e=dt85g.data(:,18)*cmc8e(2)+cmc8e(3);
%elseif cmc8e(1)==2
%mc8e= (dt85g.data(:,18).^cmc8e(6)-cmc8e(5)^cmc8e(6) )  /  ( cmc8e(4)^cmc8e(6) -cmc8e(5)^cmc8e(6));
%end
%
%if cmc8f(1)==1
%mc8f=dt85g.data(:,19)*cmc8f(2)+cmc8f(3);
%elseif cmc8f(1)==2
%mc8f= (dt85g.data(:,19).^cmc8f(6)-cmc8f(5)^cmc8f(6) )  /  ( cmc8f(4)^cmc8f(6) -cmc8f(5)^cmc8f(6));
%end

%  for T5 Tensiometer(T)=reading*A+B
% ab=-0.00031373;bb=190.67;
% ag=-0.00031320;bg=180.83;  % g here means the g-th channel
% Pressure from dt(8)5g tensiometer, channel (B) (p8b)
% p8b=dt85g.data(:,2)*ab+bb;
% p8g=dt85g.data(:,7)*ag+bg;

%p8b=dt85g.data(:,10)*cp8b(1)+cp8b(2);
%p8g=dt85g.data(:,15)*cp8g(1)+cp8g(2);

% ts stores all of the (D)ate and (T)ime at DT(8)5G in (S)tring t8s form
dt85g.time_str=dt85g.textdata(2:size(dt85g.textdata,1),1);
% td stores all of the time in digital form
dt85g.time_digi=datenum(dt85g.time_str,'yyyy/mm/dd HH:MM:SS');
% (N)umber of (R)eadings at DT(8)5g
%nr8=size(dt8d,1);
dt85g.pres_pt1=dt85g.data(:,1);
dt85g.temp_pt1=dt85g.data(:,2);
dt85g.pres_pt2=dt85g.data(:,3);
dt85g.temp_pt2=dt85g.data(:,4);
dt85g.pres_pt3=dt85g.data(:,5);
dt85g.temp_pt3=dt85g.data(:,6);
dt85g.pres_pt4=dt85g.data(:,7);
dt85g.temp_pt4=dt85g.data(:,8);
dt85g.vwc_pt1=dt85g.data(:,15);
dt85g.vwc_pt2=dt85g.data(:,16);
dt85g.vwc_pt3=dt85g.data(:,17);
dt85g.vwc_pt4=dt85g.data(:,18);
dt85g.vwc_pt5=dt85g.data(:,19);
dt85g.vwc_pt6=dt85g.data(:,20);


% % (N)umber of (R)eading on (S)cale for each (S)ession
% nrss=zeros(ns,1);

% % (T)ime (L)ength for each (S)essions
% tls=zeros(ns,1);

% (P)ressure reading by DT(8)5g from (1)st sensor 
%p81=dt85g.data(:,1);
%p82=dt85g.data(:,3);
%p83=dt85g.data(:,5);
%p84=dt85g.data(:,7);
% (T)emperature reading by DT(8)5g from (1)st MPS2 sensor
%t81=dt85g.data(:,2);
%t82=dt85g.data(:,4);
%t83=dt85g.data(:,6);
%t84=dt85g.data(:,8);
%% read the result from em50
% (T)emperature from Em(5)0, channel (1)
%t51=em50.data(:,2);
% (T)emperature from EM(5)0, Channel (2)
%t52=em50.data(:,4);
% (T)emperature from Em(5)0, channel (1)
%t53=em50.data(:,6);
% (T)emperature from EM(5)0, Channel (2)
%t54=em50.data(:,8);
% (T)emperature from Em(5)0, channel (1)
%t55=em50.data(:,10);

% (R)elative (H)umidity from EM(5)0, Channel (1)
%rh51=em50.data(:,1);
%rh52=em50.data(:,3);
%rh53=em50.data(:,5);
%rh54=em50.data(:,7);
%rh55=em50.data(:,9);
%
%
%
%
%
%%% read scale.csv
%% (W)eight from (6)0cm (C)olumn
%w6c=scale.data(:,1);
%% (W)eight from (6)0cm (M)ariott bottle
%w6m=scale.data(:,2);
%% (W)eight from (9)0cm (C)olumn
%w9c=scale.data(:,3);
%% (W)eight from (9)0cm (M)ariott bottle
%w9m=scale.data(:,4);
%% (D)ate and (T)ime for (S)cale stored by (S)tring
%dtss=scale.textdata(2:size(scale.textdata,1),1);
%% (D)ate and (T)ime for (S)cale stored by (D)igits
%dtsd=datenum(dtss,'yyyy/mmm/dd HH:MM:SS');
%% (N)umber of (R)eadings at (S)cale
%nrs=size(dtsd,1);
%fprintf(1,'Read cali.ipt complete \n');
%%% read from time.ipt file
%% (S)tart (T)ime in (S)tring form
%time=importdata('time60.ipt');
%% [h]ead [n]umber
%hn=size(time.textdata,1)-size(time.data,1);
%% (N)umber of (S)essions
%ns=size(time.data,1);
%% (S)tart (T)ime (S)tring [sts]. the first sequence indicates the sequence of the time interval 
%sts=time.textdata((hn+1):size(time.textdata,1),1);
%% (E)nd (T)ime (S)tring [ets] the first sequence indicates the sequence of the time interval 
%ets=time.textdata((hn+1):size(time.textdata,1),2);
%
%% (C)omments of (S)essions
%cs=time.textdata((hn+1):size(time.textdata,1),3); 
%%(S)tart (D)ate (T)ime in (D)igit form [sdtd] the first sequence indicates the sequence of the time interval 
%sdtd=datenum(sts,'yyyy/mmm/dd HH:MM');
%%(E)nd (D)ate (T)ime in (D)igit form [edtd] the first sequence indicates the sequence of the time interval 
%edtd=datenum(ets,'yyyy/mmm/dd HH:MM');
%% (W)ater (L)evel [wl] the first sequence indicates the sequence of the time interval 
%wl=time.data(:,1);
%% (H)eat (I)nput of each session
%hi=time.data(:,2);
%% (S)oil (T)ype of each session
%st=time.data(:,3);
%% (S)with for (O)utput
%so=time.data(:,4);
%% (R)esistance for (A)erodynamic
%ra=time.data(:,6); 
%% (T)ranslation for (T)ime (C)oordinate (day)
%ttc=time.data(:,7); %zeros(ns,1) %[0;0.5;0;0.8;0.4;0.5];
%% (S)equence of (S)tart (T)ime for dt(8)5g (sst8) the first sequence indicates the sequence of the time interval 
%% (S)equence of (E)nd (T)ime for DT(8)5G (set8) the first sequence indicates the sequence of the time interval 
%sst8=zeros(ns,1);set8=zeros(ns,1);
%% (S)equence of (S)tart (T)ime for EM(5)0 (sst5)
%% (S)equence of (E)nd (T)ime for EM(5)0 (set5)
%sst5=zeros(ns,1);set5=zeros(ns,1);
%% (S)equence of (S)tart (T)ime for (S)cale (ssts)
%% (S)equence of (E)nd (T)ime for (S)cale (sets)
%ssts=zeros(ns,1);sets=zeros(ns,1);
%% (S)equence of (S)tart (T)ime for (B)arometer (sstb)
%% (S)equence of (E)nd (T)ime for (B)arometer (setb)
%sstb=zeros(ns,1);setb=zeros(ns,1);
%%(N)et (L)oss of (W)eight from (6)0mm (C)olumn [nlw6c]
%%(N)et (L)oss of (W)eight from (6)0mm mariotte bottle [nlw6m]
%nlw6c=zeros(ns,1);nlw6m=zeros(ns,1);
%%% initialize the average and standard derivation value
%%(A)verage result of (M)oisture (C)ontent from DT(8)5G, channel (C) [amc8c(1:ns,1)]
%%(A)verage result of (M)oisture (C)ontent from DT(8)5G, channel (D) [amc8d(1:ns,1)]
%%(A)verage result of (M)oisture (C)ontent from DT(8)5G, channel (E) [amc8e(1:ns,1)]
%%(A)verage result of (M)oisture (C)ontent from DT(8)5G, channel (F) [amc8f(1:ns,1)]
%amc8c=zeros(ns,1);amc8d=zeros(ns,1);
%amc8e=zeros(ns,1);amc8f=zeros(ns,1);
%%(A)verage result of (P)ressure from DT(8)5G, channel (B) [ap8b(1:ns,1)]
%%(A)verage result of (P)ressure from DT(8)5G, channel (G) [ap8g(1:ns,1)]
%ap8b=zeros(ns,1);ap8g=zeros(ns,1);
%%(A)verage result of (P)ressure from DT(8)5G, channel (1) [ap81(1:ns,1)]
%%(A)verage result of (P)ressure from DT(8)5G, channel (2) [ap82(1:ns,1)]
%ap81=zeros(ns,1);ap82=zeros(ns,1);ap83=zeros(ns,1);ap84=zeros(ns,1);
%%(A)verage result of (T)emperature from DT(8)5G, channel (1) [ap81(1:ns,1)]
%%(A)verage result of (T)emperature from DT(8)5G, channel (2) [ap82(1:ns,1)]
%at81=zeros(ns,1);at82=zeros(ns,1);at83=zeros(ns,1);at84=zeros(ns,1);
%%(A)verage result of (R)elative (H)umidity from EM(5)0, channel (1) [arh51(1:ns,1)]
%%(A)verage result of (R)elative (H)umidity from EM(5)0, channel (2) [arh52(1:ns,1)]
%arh51=zeros(ns,1);arh52=zeros(ns,1);arh53=zeros(ns,1);arh54=zeros(ns,1);arh55=zeros(ns,1);
%%(A)verage result of (T)emperature from EM(5)0, channel (A) [at51(1:ns,1)]
%at51=zeros(ns,1);at52=zeros(ns,1);at53=zeros(ns,1);at54=zeros(ns,1);at55=zeros(ns,1);
%%(S)tandard (D)erivation of (M)oisture (C)ontent from DT(8)5G, channel (C) [sdmc8c(1:ns,1)]
%%(S)tandard (D)erivation of (M)oisture (C)ontent from DT(8)5G, channel (D) [sdmc8d(1:ns,1)]
%%(S)tandard (D)erivation of (M)oisture (C)ontent from DT(8)5G, channel (E) [sdmc8e(1:ns,1)]
%%(S)tandard (D)erivation of (M)oisture (C)ontent from DT(8)5G, channel (F) [sdmc8f(1:ns,1)]
%sdmc8c=zeros(ns,1);sdmc8d=zeros(ns,1);sdmc8e=zeros(ns,1);sdmc8f=zeros(ns,1);
%%(S)tandard (D)erivation of (P)ressure from DT(8)5G, channel (B) [sdp8b(1:ns,1)]
%%(S)tandard (D)erivation of (P)ressure from DT(8)5G, channel (G) [sdp8g(1:ns,1)]
%sdp8b=zeros(ns,1);sdp8g=zeros(ns,1);
%%(S)tandard (D)erivation of (P)ressure from DT(8)5G, channel (1) [sdp81(1:ns,1)]
%%(S)tandard (D)erivation of (P)ressure from DT(8)5G, channel (2) [sdp82(1:ns,1)]
%sdp81=zeros(ns,1);sdp82=zeros(ns,1);sdp83=zeros(ns,1);sdp84=zeros(ns,1);
%%(S)tandard (D)erivation of (T)emperature from DT(8)5G, channel (1) [sdt81(1:ns,1)]
%%(S)tandard (D)erivation of (T)emperature from DT(8)5G, channel (2) [sdt82(1:ns,1)]
%sdt81=zeros(ns,1);sdt82=zeros(ns,1);sdt83=zeros(ns,1);sdt84=zeros(ns,1);
%%(S)tandard (D)erivation of (T)emperature from EM(5)0, channel (1) [sdt51(1:ns,1)]
%%(S)tandard (D)erivation of (T)emperature from EM(5)0, channel (2) [sdt52(1:ns,1)]
%sdt51=zeros(ns,1);sdt52=zeros(ns,1);sdt53=zeros(ns,1);sdt54=zeros(ns,1);sdt55=zeros(ns,1);
%%(S)tandard (D)erivation of (R)elative (H)umidity from EM(5)0, channel (1) [sdrh51(1:ns,1)]
%%(S)tandard (D)erivation of (R)elative (H)umidity from EM(5)0, channel (2) [sdrh52(1:ns,1)]
%sdrh51=zeros(ns,1);sdrh52=zeros(ns,1);sdrh53=zeros(ns,1);sdrh54=zeros(ns,1);sdrh55=zeros(ns,1);
% % (F)itting (E)vapora(T)ion by (M)arriott bottle
%fetm=zeros(ns,2);fetmc=zeros(ns,2);
%% (Z)ero (P)oint of (S)cale data (A)fter (T)ranslation
%zpsat=zeros(size(ttc,1),1);
%% (Z)ero (P)oint of DT(8)5G data (A)fter (T)ranslation
%zp8at=zeros(size(ttc,1),1);
%
%%% Finding out the start and the end of each session
%
%for it=1:ns  % No. of Sessions
%    if (so(it)==1||so(it)==3)
%%% Finding out the row numbers that is equal or greater than start time and end time in dt85g, em50 and scale
%for i=1:nr8
% if dt8d(i) >= sdtd(it)
%     sst8(it)=i;break
% end
%end
%for k=i:nrs
%  if dt8d(k)-dt8d(sst8(it))>ttc(it)
%      zp8at(it)=k;break
%  end
%end
%
%for j=i:nr8
% if dt8d(j) >= edtd(it)
%     set8(it)=j;break
% end
%end
%% pause the program if the end point is not found from the database
%if set8(it)==0
%    fprintf(1,'set8=0, program stops\n');pause
%end
%% calc the average results
%amc8c(it)=mean(mc8c(sst8(it):set8(it)));amc8d(it)=mean(mc8d(sst8(it):set8(it)));
%amc8e(it)=mean(mc8e(sst8(it):set8(it)));amc8f(it)=mean(mc8f(sst8(it):set8(it)));
%ap8b(it)=mean(p8b(sst8(it):set8(it)));ap8g(it)=mean(p8g(sst8(it):set8(it)));
%ap81(it)=mean(p81(sst8(it):set8(it)));ap82(it)=mean(p82(sst8(it):set8(it)));
%ap83(it)=mean(p83(sst8(it):set8(it)));ap84(it)=mean(p84(sst8(it):set8(it)));
%at81(it)=mean(t81(sst8(it):set8(it)));at82(it)=mean(t82(sst8(it):set8(it)));
%at83(it)=mean(t83(sst8(it):set8(it)));at84(it)=mean(t84(sst8(it):set8(it)));
%% calc the stand derivation value
%sdmc8c(it)=std(mc8c(sst8(it):set8(it)));sdmc8d(it)=std(mc8d(sst8(it):set8(it)));
%sdmc8e(it)=std(mc8e(sst8(it):set8(it)));sdmc8f(it)=std(mc8f(sst8(it):set8(it)));
%sdp8b(it)=std(p8b(sst8(it):set8(it)));sdp8g(it)=std(p8g(sst8(it):set8(it)));
%sdp8b(it)=std(p8b(sst8(it):set8(it)));sdp8g(it)=std(p8g(sst8(it):set8(it)));
%sdp81(it)=std(p81(sst8(it):set8(it)));sdp82(it)=std(p82(sst8(it):set8(it)));
%sdp83(it)=std(p83(sst8(it):set8(it)));sdp84(it)=std(p84(sst8(it):set8(it)));
%sdt81(it)=std(t81(sst8(it):set8(it)));sdt82(it)=std(t82(sst8(it):set8(it)));
%sdt83(it)=std(t83(sst8(it):set8(it)));sdt84(it)=std(t84(sst8(it):set8(it)));
%% for datalist of em50
%for i=1:nr5
% if dt5d(i) >= sdtd(it) 
%     sst5(it)=i;break
% end
%end
%for j=i:nr5
% if dt5d(j) >= edtd(it)
%     set5(it)=j;break
% end
%end
%% pause the program if the end point is not found from the database
%if set5(it)==0
%    fprintf(1,'set5=0, program stops\n');pause
%end
%% calc the average value
%at51(it)=mean(t51(sst5(it):set5(it)));at52(it)=mean(t52(sst5(it):set5(it)));
%at53(it)=mean(t53(sst5(it):set5(it)));at54(it)=mean(t54(sst5(it):set5(it)));
%at55(it)=mean(t55(sst5(it):set5(it)));
%arh51(it)=mean(rh51(sst5(it):set5(it)));arh52(it)=mean(rh52(sst5(it):set5(it)));
%arh53(it)=mean(rh53(sst5(it):set5(it)));arh54(it)=mean(rh54(sst5(it):set5(it)));
%arh55(it)=mean(rh55(sst5(it):set5(it)));
%
%% calc the standard derivation value
%sdt51(it)=std(t51(sst5(it):set5(it)));sdt52(it)=std(t52(sst5(it):set5(it)));
%sdt53(it)=std(t53(sst5(it):set5(it)));sdt54(it)=std(t54(sst5(it):set5(it)));
%sdt55(it)=std(t55(sst5(it):set5(it)));
%sdrh51(it)=std(rh51(sst5(it):set5(it)));sdrh52(it)=std(rh52(sst5(it):set5(it)));
%sdrh53(it)=std(rh53(sst5(it):set5(it)));sdrh54(it)=std(rh54(sst5(it):set5(it)));
%sdrh55(it)=std(rh55(sst5(it):set5(it)));
%
%% for datalist of scale
%for i=1:nrs
% if dtsd(i) >= sdtd(it) 
%     ssts(it)=i;break
% end
%end
%
%for k=i:nrs
%  if dtsd(k)-dtsd(ssts(it))>ttc(it)
%      zpsat(it)=k;break
%  end
%end
%
%for j=i:nrs
% if dtsd(j) >= edtd(it)
%     sets(it)=j;break
% end
%end
%% pause the program if the end point is not found from the database
%if sets(it)==0
%    fprintf(1,'sets=0, program stops\n');pause
%end
%
%    end  % (op(it)~=0)
%
%end
%%% finish the job
%% clear em50 scale baro hn
% fprintf(1,'JOB COMPLETE \n');
% toc
% 
% % Build0002 ...11-10-2012... the calibration value is obtained though cali.ipt
% % Build0003 ...11-10-2012... add inport from barometer
% % Build0004 ...01-11-2012... add heat input, sand type, input or not at time.ipt
% 
