# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 13:59:24 2021

@author: s4680073
"""
e=0
r=1
t=2
SA2_water_depth_adjust=0.48
area_scale=1
pump_scale=1.31
plant_percentage1=0
plant_percentage2=plant_percentage1
cs451_scale=10**e
zom=0.0001/(10**r)
ir_scale=10*t
for e in range(1,10):
    # exec(open('C:\columnpy\columnpy\ewatering\python\calc_area.py').read())
    for r in range(0,6):
        for t in range(1,7):
            exec(open('C:\columnpy\columnpy\ewatering\python\\adjust_value.py').read())
            exec(open('C:\columnpy\columnpy\ewatering\python\get_data_py3.py').read())
            exec(open('C:\columnpy\columnpy\ewatering\python\calc_evap.py').read())
            exec(open('C:\columnpy\columnpy\ewatering\python\\adjust_pet_pond_falling_rate.py').read())
            print(f't={t}')

            # exec(open('C:\columnpy\columnpy\ewatering\python\\test.py').read())
exec(open('C:\columnpy\columnpy\ewatering\python\\read_pump_meter.py').read())
# plant_percentage1=0.28
# plant_percentage2=0.05
# plant_percentage1=0.25
# plant_percentage2=0.10
# plant_percentage1=0.0
# plant_percentage2=0.0
# plant_percentage1=0.15
# plant_percentage2=plant_percentage1
# area_scale=0.73
# plant_percentage1=0
exec(open('C:\columnpy\columnpy\ewatering\python\\compare_area_and _track.py').read())
#exec(open('C:\columnpy\columnpy\ewatering\python\compare_area_and _track.py').read())
# pump_scale=1
# t=10080 #202105241630
# t=804   #202103210900
area_scale=0.8
exec(open('C:\columnpy\columnpy\ewatering\python\calc_area.py').read())
exec(open('C:\columnpy\columnpy\ewatering\python\\read_pump_meter.py').read())
# pump_scale=1.31
# t=10080 #202105241630
# t=804   #202103210900
area_scale=0.9
exec(open('C:\columnpy\columnpy\ewatering\python\calc_area.py').read())
exec(open('C:\columnpy\columnpy\ewatering\python\\read_pump_meter.py').read())
# pump_scale=1.15
# t=10080 #202105241630
# t=804   #202103210900
area_scale=1.0
exec(open('C:\columnpy\columnpy\ewatering\python\calc_area.py').read())
exec(open('C:\columnpy\columnpy\ewatering\python\\read_pump_meter.py').read())
# pump_scale=1.5
# t=10080 #202105241630
# t=804   #202103210900
exec(open('C:\columnpy\columnpy\ewatering\python\\read_pump_meter.py').read())

area_scale=1
plant_percentage1=0
plant_percentage2=plant_percentage1
exec(open('C:\columnpy\columnpy\ewatering\python\calc_area.py').read())
exec(open('C:\columnpy\columnpy\ewatering\python\\read_pump_meter.py').read())
plant_percentage1=0.05
plant_percentage2=plant_percentage1
exec(open('C:\columnpy\columnpy\ewatering\python\calc_area.py').read())
exec(open('C:\columnpy\columnpy\ewatering\python\\read_pump_meter.py').read())
plant_percentage1=0.1
plant_percentage2=plant_percentage1
exec(open('C:\columnpy\columnpy\ewatering\python\calc_area.py').read())
exec(open('C:\columnpy\columnpy\ewatering\python\\read_pump_meter.py').read())
plant_percentage1=.15
plant_percentage2=plant_percentage1
exec(open('C:\columnpy\columnpy\ewatering\python\calc_area.py').read())
exec(open('C:\columnpy\columnpy\ewatering\python\\read_pump_meter.py').read())
plant_percentage1=0.2
plant_percentage2=plant_percentage1
exec(open('C:\columnpy\columnpy\ewatering\python\calc_area.py').read())
exec(open('C:\columnpy\columnpy\ewatering\python\\read_pump_meter.py').read())
plant_percentage1=0.24
plant_percentage2=plant_percentage1
exec(open('C:\columnpy\columnpy\ewatering\python\calc_area.py').read())
exec(open('C:\columnpy\columnpy\ewatering\python\\read_pump_meter.py').read())

area_scale=1
plant_percentage1=0
plant_percentage2=plant_percentage1
pump_scale=1
exec(open('C:\columnpy\columnpy\ewatering\python\get_data_py3.py').read())
exec(open('C:\columnpy\columnpy\ewatering\python\calc_evap.py').read())
exec(open('C:\columnpy\columnpy\ewatering\python\calc_area.py').read())
exec(open('C:\columnpy\columnpy\ewatering\python\\read_pump_meter.py').read())
area_scale=0.74
plant_percentage1=0
plant_percentage2=plant_percentage1
pump_scale=1
exec(open('C:\columnpy\columnpy\ewatering\python\get_data_py3.py').read())
exec(open('C:\columnpy\columnpy\ewatering\python\calc_evap.py').read())
exec(open('C:\columnpy\columnpy\ewatering\python\calc_area.py').read())
exec(open('C:\columnpy\columnpy\ewatering\python\\read_pump_meter.py').read())
area_scale=1
plant_percentage1=0
plant_percentage2=plant_percentage1
pump_scale=1.31
exec(open('C:\columnpy\columnpy\ewatering\python\get_data_py3.py').read())
exec(open('C:\columnpy\columnpy\ewatering\python\calc_evap.py').read())
exec(open('C:\columnpy\columnpy\ewatering\python\calc_area.py').read())
exec(open('C:\columnpy\columnpy\ewatering\python\\read_pump_meter.py').read())
