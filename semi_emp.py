import numpy as np
import pandas as pd
import rainflow

def LinDeg_Generic(socpr):

# Assuming you have the 'rainflow' function implemented in Python
# If not, you'll need to implement it or find an equivalent library
C = rainflow(socpr.iloc[:, 1], socpr.iloc[:, 0])

for DD, SC, N, i_start, i_end in rainflow.extract_cycles(socpr.iloc[:, 1]): 
    #print(DD, SC, N, i_start, i_end) 

    DoD = DD / 100
    SoC = SC / 100
    Crate = 1

    T = np.mean(socpr.iloc[:, 2])
    t = np.max(socpr.iloc[:, 0])  # hours
  

    # SoC stress model
    k_soc = 1.039  # SoC stress model coefficient
    SoC_ref = 0.6  # reference cycle average SoC
    d_SoC = np.exp(k_soc * (SoC - SoC_ref))

    # DoD stress model (Ecker model)
    k1 = 0.2 / (1325 * 2.28)
    k2 = 1.62
    d_DoD = k1 * DoD ** k2

    # C-rate effect (neglected in this version)
    d_Crate = 1

    # Cell temperature effect
    k_t = 0.0693
    T_ref = 25  # reference temperature in Celsius
    d_temp = np.exp(k_t * (T - T_ref) * (273 + T_ref) / (273 + T))

    # Total cycle ageing
    d_cycle = np.sum(d_DoD * d_SoC * d_Crate * d_temp * N)

    # Calendar ageing
    k_soc_cal = k_soc
    k_cal = 3.31e-9 / 8
    SoC_ref = 0.6

    SoC_avg = np.mean(SoC)
    T_avg = np.mean(T)

    d_cal = k_cal * np.exp(k_soc_cal * (SoC_avg - SoC_ref)) * t * \
        np.exp(k_t * (T_avg - T_ref) * (273 + T_ref) / (273 + T_avg))

    # Total linearized degradation
    d = d_cycle + d_cal

    return d
    
