# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 15:29:00 2020

@author: spand
"""

import os
import os.path as path

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

directory = 'C:/Users/spand/OneDrive - University of Toronto/Year 4/Skinner Lab/'
fname = 'test.txt'
fpath = directory + fname

def calc_freq(fpath):
    t, V_m = np.loadtxt(fpath, skiprows=2, unpack=True)
    
    plt.plot(t, V_m)
    
    spikes, _ = find_peaks(V_m, height=20)
    
    spike_times = t[spikes]
    
    spike_period = spike_times[1:] - spike_times[0:-1]
    
    f1 = np.mean(1/spike_period[:int((len(spike_period))/2)])*1000
    f2 = np.mean(1/spike_period[int((len(spike_period))/2):])*1000
    
    f_avg = (f1+f2)/2
    
    print(f1, f2, f_avg)
    return np.array[f1, f2, f_avg]

file_list = os.listdir(directory)
file_list = sorted([name for name in file_list if name.endswith('.txt')])

current = np.zeros_like(file_list)
f_data = np.array((len(file_list), 3))

for i in range(len(file_list)):
    current[i] = int(file_list[i].split('.')[0])
    fpath = directory + file_list[i]
    f_data[i] = calc_freq(fpath)

    
    