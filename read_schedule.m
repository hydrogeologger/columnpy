%

    time=importdata('schedule.ipt');
    sched=struct;
 
    % [h]ead [n]umber
    time.head_number=size(time.textdata,1)-size(time.data,1);
    
    %time.head_number=10;
    % (N)umber of (S)schedule
    time.number_session=size(time.data,1);


for i=1: time.number_session
    time.start_time_str=time.textdata((time.head_number+1):size(time.textdata,1),1); 
    time.end_time_str=time.textdata((time.head_number+1):size(time.textdata,1),2); 
    % (C)omments of (S)essions
    time.comments=time.textdata((time.number_session+1):size(time.textdata,1),3); 
    %(S)tart (D)ate (T)ime in (D)igit form [sdtd] the first sequence indicates the sequence of the time interval 
    time.start_time_digi=datenum(time.start_time_str,'yyyy/mmm/dd HH:MM');
    %(E)nd (D)ate (T)ime in (D)igit form [edtd] the first sequence indicates the sequence of the time interval 
    time.end_time_digi=datenum(time.end_time_str,'yyyy/mmm/dd HH:MM');
    
    
    sched(i).start_str=time.textdata(time.head_number+i,1); 
    sched(i).end_str=time.textdata(time.head_number+i,2); 
    % (C)omments of (S)essions
    sched(i).comments=time.textdata(time.head_number+i,3); 
    %(S)tart (D)ate (T)ime in (D)igit form [sdtd] the first sequence indicates the sequence of the time interval 
    sched(i).start_digi=datenum(sched(i).start_str,'yyyy/mmm/dd HH:MM');
    %(E)nd (D)ate (T)ime in (D)igit form [edtd] the first sequence indicates the sequence of the time interval 
    sched(i).end_digi=datenum(sched(i).end_str,'yyyy/mmm/dd HH:MM');
    sched(i).duration_days=sched(i).end_digi-sched(i).start_digi;
    sched(i).surface_area=time.data(i,2);
    sched(i).dt=time.data(i,3);
    sched(i).scale_no=time.data(i,4);

end




