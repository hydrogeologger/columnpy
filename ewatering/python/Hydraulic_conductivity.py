# -*- coding: utf-8 -*-
"""
Created on Wed May 19 14:18:59 2021

@author: s4680073
"""
# Calculate the hydraulic conductivity after saturation with fallin head method
def hy_cdt(H1,H2,L,T):
    import numpy as np
    K=(L/T)*np.log(H1/H2)
    return K
L=0.04;
H2=0.045;
H1=0.038-0.011+0.045;
T=47*60*60
K=hy_cdt(H1,H2,L,T)