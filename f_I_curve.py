# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 17:51:09 2020

@author: spand
"""

import numpy as np
import matplotlib.pyplot as plt

def plot(f, I, g):
    plt.plot(f_vec, I_vec, label = str(g))
    plt.xlabel('Current (pA)')
    plt.ylabel('Spiking Freq (Hz)')

#fname = 'f_I_curve.txt'
directory = 'C:/Users/spand/OneDrive - University of Toronto/Year 4/Skinner Lab/Spiking Plots/'

channel_name = 'gKvAdist' #gNav, gNavaxon, gKvA, gKvAdist, gKdr, gHCN

if channel_name == 'gKvA':
    directory = directory + channel_name + '/'
    for i in range(7):
        if i==0:
            fname = 'gKvA_0_0056.txt'
            f_vec, I_vec = np.loadtxt(directory+fname, skiprows = 1, unpack = True)
            plot(f_vec, I_vec, 0.0056)
        '''
        elif i==1:
            fname = 'gKvA_0_0064.txt'
            f_vec, I_vec = np.loadtxt(directory+fname, skiprows = 1, unpack = True)
            plot(f_vec, I_vec, 0.0064)
        elif i==2:
            fname = 'gKvA_0_0072.txt'
            f_vec, I_vec = np.loadtxt(directory+fname, skiprows = 1, unpack = True)
            plot(f_vec, I_vec, 0.0072)
        '''    
        if i==3:
            fname = 'gKvA_0_008.txt'
            f_vec, I_vec = np.loadtxt(directory+fname, skiprows = 1, unpack = True)
            plot(f_vec, I_vec, 0.008)
        '''
        elif i==4:
            fname = 'gKvA_0_0088.txt'
            f_vec, I_vec = np.loadtxt(directory+fname, skiprows = 1, unpack = True)
            plot(f_vec, I_vec, 0.0088)
        elif i==5:
            fname = 'gKvA_0_0096.txt'
            f_vec, I_vec = np.loadtxt(directory+fname, skiprows = 1, unpack = True)
            plot(f_vec, I_vec, 0.0096)
        '''
        if i==6:
            fname = 'gKvA_0_0104.txt'
            f_vec, I_vec = np.loadtxt(directory+fname, skiprows = 1, unpack = True)
            plot(f_vec, I_vec, 0.0104)
        
    plt.legend(title="gKvA (mho/cm$^2$)")

if channel_name == 'gKvAdist':
    directory = directory + channel_name + '/'
    for i in range(7):
        if i==0:
            fname = 'gKvAdist_0_0056.txt'
            f_vec, I_vec = np.loadtxt(directory+fname, skiprows = 1, unpack = True)
            plot(f_vec, I_vec, 0.0056)
        '''
        if i==1:
            fname = 'gKvAdist_0_0064.txt'
            f_vec, I_vec = np.loadtxt(directory+fname, skiprows = 1, unpack = True)
            plot(f_vec, I_vec, 0.0064)
        if i==2:
            fname = 'gKvAdist_0_0072.txt'
            f_vec, I_vec = np.loadtxt(directory+fname, skiprows = 1, unpack = True)
            plot(f_vec, I_vec, 0.0072)
        '''   
        if i==3:
            fname = 'gKvAdist_0_008.txt'
            f_vec, I_vec = np.loadtxt(directory+fname, skiprows = 1, unpack = True)
            plot(f_vec, I_vec, 0.008)
        '''
        if i==4:
            fname = 'gKvAdist_0_0088.txt'
            f_vec, I_vec = np.loadtxt(directory+fname, skiprows = 1, unpack = True)
            plot(f_vec, I_vec, 0.0088)
        if i==5:
            fname = 'gKvAdist_0_0096.txt'
            f_vec, I_vec = np.loadtxt(directory+fname, skiprows = 1, unpack = True)
            plot(f_vec, I_vec, 0.0096)
        '''
        if i==6:
            fname = 'gKvAdist_0_0104.txt'
            f_vec, I_vec = np.loadtxt(directory+fname, skiprows = 1, unpack = True)
            plot(f_vec, I_vec, 0.0104)
        
    plt.legend(title="gKvAdist (mho/cm$^2$)")

if channel_name == 'gNav':
    directory = directory + channel_name + '/'
    for i in range(8):
        if i==0:
            fname = 'gNav_0_0224.txt'
            f_vec, I_vec = np.loadtxt(directory+fname, skiprows = 1, unpack = True)
            plot(f_vec, I_vec, 0.0224)
        '''
        elif i==1:
            fname = 'gNav_0_0256.txt'
            f_vec, I_vec = np.loadtxt(directory+fname, skiprows = 1, unpack = True)
            plot(f_vec, I_vec, 0.0256)
        elif i==2:
            fname = 'gNav_0_0288.txt'
            f_vec, I_vec = np.loadtxt(directory+fname, skiprows = 1, unpack = True)
            plot(f_vec, I_vec, 0.0288)
        '''
        if i==3:
            fname = 'gNav_0_032.txt'
            f_vec, I_vec = np.loadtxt(directory+fname, skiprows = 1, unpack = True)
            plot(f_vec, I_vec, 0.032)
        '''
        elif i==4:
            fname = 'gNav_0_0352.txt'
            f_vec, I_vec = np.loadtxt(directory+fname, skiprows = 1, unpack = True)
            plot(f_vec, I_vec, 0.0352)
        elif i==5:
            fname = 'gNav_0_0384.txt'
            f_vec, I_vec = np.loadtxt(directory+fname, skiprows = 1, unpack = True)
            plot(f_vec, I_vec, 0.0384)
        '''
        if i==6:
            fname = 'gNav_0_0416.txt'
            f_vec, I_vec = np.loadtxt(directory+fname, skiprows = 1, unpack = True)
            plot(f_vec, I_vec, 0.0416)
        if i==7:
            fname = 'gNav_0_06.txt'
            f_vec, I_vec = np.loadtxt(directory+fname, skiprows = 1, unpack = True)
            plot(f_vec, I_vec, 0.06)
        
    plt.legend(title="gNav (mho/cm$^2$)")
    
if channel_name == 'gNavaxon':
    directory = directory + channel_name + '/'
    for i in range(7):
        if i==0:
            fname = 'gNavaxon_0_0448.txt'
            f_vec, I_vec = np.loadtxt(directory+fname, skiprows = 1, unpack = True)
            plot(f_vec, I_vec, 0.0448)
        '''
        elif i==1:
            fname = 'gNavaxon_0_0512.txt'
            f_vec, I_vec = np.loadtxt(directory+fname, skiprows = 1, unpack = True)
            plot(f_vec, I_vec, 0.0512)
        elif i==2:
            fname = 'gNavaxon_0_0576.txt'
            f_vec, I_vec = np.loadtxt(directory+fname, skiprows = 1, unpack = True)
            plot(f_vec, I_vec, 0.0576)
        '''
        if i==3:
            fname = 'gNavaxon_0_064.txt'
            f_vec, I_vec = np.loadtxt(directory+fname, skiprows = 1, unpack = True)
            plot(f_vec, I_vec, 0.064)
        '''
        elif i==4:
            fname = 'gNavaxon_0_0704.txt'
            f_vec, I_vec = np.loadtxt(directory+fname, skiprows = 1, unpack = True)
            plot(f_vec, I_vec, 0.0704)
        elif i==5:
            fname = 'gNavaxon_0_0768.txt'
            f_vec, I_vec = np.loadtxt(directory+fname, skiprows = 1, unpack = True)
            plot(f_vec, I_vec, 0.0768)
        '''
        if i==6:
            fname = 'gNavaxon_0_0832.txt'
            f_vec, I_vec = np.loadtxt(directory+fname, skiprows = 1, unpack = True)
            plot(f_vec, I_vec, 0.0832)
        
    plt.legend(title="gNavaxon (mho/cm$^2$)")

    
if channel_name == 'gKdr':
    directory = directory + channel_name + '/'
    for i in range(7):
        if i==0:
            fname = 'gKdr_0_0021.txt'
            f_vec, I_vec = np.loadtxt(directory+fname, skiprows = 1, unpack = True)
            plot(f_vec, I_vec, 0.0021)
        '''
        elif i==1:
            fname = 'gKdr_0_0024.txt'
            f_vec, I_vec = np.loadtxt(directory+fname, skiprows = 1, unpack = True)
            plot(f_vec, I_vec, 0.0024)
        elif i==2:
            fname = 'gKdr_0_0027.txt'
            f_vec, I_vec = np.loadtxt(directory+fname, skiprows = 1, unpack = True)
            plot(f_vec, I_vec, 0.0027)
        '''
        if i==3:
            fname = 'gKdr_0_003.txt'
            f_vec, I_vec = np.loadtxt(directory+fname, skiprows = 1, unpack = True)
            plot(f_vec, I_vec, 0.003)
        '''
        elif i==4:
            fname = 'gKdr_0_0033.txt'
            f_vec, I_vec = np.loadtxt(directory+fname, skiprows = 1, unpack = True)
            plot(f_vec, I_vec, 0.0033)
        elif i==5:
            fname = 'gKdr_0_0036.txt'
            f_vec, I_vec = np.loadtxt(directory+fname, skiprows = 1, unpack = True)
            plot(f_vec, I_vec, 0.0036)
        '''
        if i==6:
            fname = 'gKdr_0_0039.txt'
            f_vec, I_vec = np.loadtxt(directory+fname, skiprows = 1, unpack = True)
            plot(f_vec, I_vec, 0.0039)
        
    plt.legend(title="gKdr (mho/cm$^2$)")
    
if channel_name == 'gHCN':
    directory = directory + channel_name + '/'
    for i in range(6):
        if i==0:
            fname = 'gHCN_0_00042.txt'
            f_vec, I_vec = np.loadtxt(directory+fname, skiprows = 1, unpack = True)
            plot(f_vec, I_vec, 0.00042)
        '''
        elif i==1:
            fname = 'gHCN_0_00048.txt'
            f_vec, I_vec = np.loadtxt(directory+fname, skiprows = 1, unpack = True)
            plot(f_vec, I_vec, 0.00048)
        elif i==2:
            fname = 'gHCN_0_00054.txt'
            f_vec, I_vec = np.loadtxt(directory+fname, skiprows = 1, unpack = True)
            plot(f_vec, I_vec, 0.00054)
        '''
        if i==3:
            fname = 'gHCN_0_0006.txt'
            f_vec, I_vec = np.loadtxt(directory+fname, skiprows = 1, unpack = True)
            plot(f_vec, I_vec, 0.0006)
        '''
        elif i==4:
            fname = 'gHCN_0_00066.txt'
            f_vec, I_vec = np.loadtxt(directory+fname, skiprows = 1, unpack = True)
            plot(f_vec, I_vec, 0.00066)
        '''
        if i==5:
            fname = 'gHCN_0_00072.txt'
            f_vec, I_vec = np.loadtxt(directory+fname, skiprows = 1, unpack = True)
            plot(f_vec, I_vec, 0.00072)    
        
    plt.legend(title="gHCN (mho/cm$^2$)")
    
#plt.savefig(directory + 'f_I_curve.png')
plt.savefig(directory + 'f_I_curve_highlow.png')
