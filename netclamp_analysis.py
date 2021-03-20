import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks
from analyse import analyse

def netclamp_analyse(channel, GIDs, multiplier, make_plots = False):
    threshold = -30 #mV

    directory = "C:/Users/spand/OneDrive - University of Toronto/Year 4/Skinner Lab/Spiking Data/network_clamp_results/"
    directory += (channel + '/' + multiplier)

    file_list = []

    for gid in GIDs:
        file_list.append(directory + '/' + multiplier + '_mytrace_' + \
                         gid + '_soma.dat')

    freq_data = np.zeros((len(file_list), 4))
    isi_data = np.zeros((len(file_list), 4))

    if make_plots == True:
        fig, ax = plt.subplots(len(file_list), 1, sharex=True, sharey=True)
        fig.suptitle(channel + ': ' + multiplier)
        plt.ylabel('Voltage (mV)')
        plt.xlabel('Time (ms)')

    for i in range(len(file_list)):
        x, y = np.loadtxt(file_list[i], unpack=True, skiprows=1)
        if make_plots == True:
            ax[i].plot(x, y)
            ax[i].plot(x, x*0 + threshold, 'r')
        # print (x,y)
        F, T = analyse(x, y)
        freq_data[i] = F
        isi_data[i] = T

    avg_freq_data = np.zeros(4)
    avg_isi_data = np.zeros(4)

    for i in range(4):
        avg_freq_data[i] = np.mean(freq_data[:, i])
        avg_isi_data[i] = np.mean(isi_data[:, i])

    print('f1 \t f2 \t f_avg \t f_sd')
    print(freq_data)
    print(avg_freq_data)
    print('t1 \t t2 \t t_avg \t t_sd')
    print(isi_data)
    print(avg_isi_data)

    if make_plots == True:
        plt.show()

channel = 'g_HCN'
GIDs = ['29097', '36884', '52458', '68032', '83606']
multiplier = '10x' #input decimal as underscore (eg. 0_1x)

netclamp_analyse(channel, GIDs, multiplier)