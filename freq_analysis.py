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

path_to_folder = 'C:/Users/spand/OneDrive - University of Toronto/Year 4/Skinner Lab/Spiking Data/gNav/'

folder = (
    'gNav_0_016/',
    #'gNav_0_0192/',
    'gNav_0_0224/',
    #'gNav_0_0256/',
    'gNav_0_0288/',
    'gNav_0_032/',
    'gNav_0_0352/',
    #'gNav_0_0384/',
    'gNav_0_0416/',
    #'gNav_0_0448/',
    'gNav_0_048/',
    )


def calc_freq(fpath):
    t, V_m = np.loadtxt(fpath, skiprows=2, unpack=True)
    
    #plt.plot(t, V_m)
    
    spikes, _ = find_peaks(V_m, height=10)
    
    if spikes.size <= 0:
        return [0,0,0]
    
    if spikes.size == 1:
        return [1,1,1]
    
    spike_times = t[spikes]
    
    spike_period = spike_times[1:] - spike_times[0:-1]
    
    #finds average frequency for each half, and average of the two
    f1 = np.mean(1/spike_period[:int((len(spike_period))/2)])*1000
    f2 = np.mean(1/spike_period[int((len(spike_period))/2):])*1000
    
    f_avg = (f1+f2)/2
    #print(f1, f2, f_avg)
    return [f1, f2, f_avg]

for j in range(len(folder)):
    
    directory = path_to_folder + folder[j]    
    #make a list of all .txt files in the directory
    file_list = os.listdir(directory)
    file_list = sorted([name for name in file_list if name.endswith('.txt')])
    
    #create empty arrays for storing current and frequency data
    current = np.zeros_like(file_list,dtype=int)
    f_data = np.zeros((len(file_list), 3))
    
    for i in range(len(file_list)):
        #this is dependent on saving the data as "<current>.txt"
        current[i] = int(file_list[i].split('.')[0])
        fpath = directory + file_list[i]
        f_data[i] = calc_freq(fpath)
        
    
    plt.plot(current, f_data[..., 2], label = folder[j])
    #plt.plot(current[-4:], f_data[..., 2][-4:])
    
plt.legend()


    
    