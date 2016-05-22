%

%    time=importdata('schedule.ipt');
    sched=struct;
 
    % [h]ead [n]umber
%    time.head_number=size(time.textdata,1)-size(time.data,1);
    
    %time.head_number=10;
    % (N)umber of (S)schedule
%    time.number_session=size(time.data,1);
fn = fopen('schedule.ipt');
tmp=getNextLine(fn,'criterion','without','keyword','#');
i=1;
while tmp~=-1
    tmp=strsplit(tmp,',');
    sched(i).start_str=tmp(1);
    sched(i).end_str  =tmp(2);
    % (C)omments of (S)essions
    % note that curved bracket is need to make it as string rather than cell
    sched(i).tag=strtrim(tmp{3});
    %(S)tart (D)ate (T)ime in (D)igit form [sdtd] the first sequence indicates the sequence of the time interval 
    sched(i).start_digi=datenum(sched(i).start_str,'yyyy/mmm/dd HH:MM');
    %(E)nd (D)ate (T)ime in (D)igit form [edtd] the first sequence indicates the sequence of the time interval 
    sched(i).end_digi=datenum(sched(i).end_str,'yyyy/mmm/dd HH:MM');

    sched(i).duration_days=sched(i).end_digi-sched(i).start_digi;
    sched(i).water_level_above=str2double(tmp(4));
    sched(i).surface_area=str2double(tmp(5));
    sched(i).dt=str2double(tmp(6));
    sched(i).scale_no=str2double(tmp(7));

    tmp=getNextLine(fn,'criterion','without','keyword','#');
    i=i+1;
end







