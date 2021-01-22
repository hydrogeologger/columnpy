

a.iv=12;
a.ivy=2;
a.fs=15;

a.left =  0.08;
a.bot  =  0.80;
a.width= 0.9;
a.width2=0.823;
a.height= 0.15;
a.h_interval=0.15;
a.lw=2;


figure;
subplot(3,1,1)
plot(scale.time_digi,scale.weight,'ro');hold on
datetick('x','DD/MM','keepticks') 
xlabel('Time (day)','FontSize',a.fs);
ylab=ylabel('scale (g)','FontSize',a.fs);

%subplot(3,1,2)
%plot(em50.time_digi,em50.temp_pt4,'ro');hold on
%plot(em50.time_digi,em50.temp_pt5,'go');hold on
%xlabel('Time (day)','FontSize',a.fs);
%ylab=ylabel('temperature','FontSize',a.fs);
%
%datetick('x','DD','keepticks') 
%subplot(3,1,3)
%plot(em50.time_digi,em50.rh_pt4,'ro');hold on
%plot(em50.time_digi,em50.rh_pt5,'go');hold on
%datetick('x','DD','keepticks') 
%xlabel('Time (day)','FontSize',a.fs);
%ylab=ylabel('relativehumidity','FontSize',a.fs);
