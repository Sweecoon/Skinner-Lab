import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

def analyse(x, y, threshold = -30):
    '''
    :param x: (array) series of time points
    :param y: (array) time-dependent signal with spikes
    :return:
        [f1, f2, f_avg]: list containing mean spiking frequency for each half and entire period
        f_var: variance of spiking frequency
    '''
    spikes, _ = find_peaks(y, height= threshold)

    if spikes.size <= 0:
        return [0, 0, 0], 0

    if spikes.size == 1:
        return [1, 1, 1], 0

    spike_times = x[spikes]

    spike_period = spike_times[1:] - spike_times[0:-1]

    # finds average frequency for each half, and average of the two
    f1 = np.mean(1 / spike_period[:int((len(spike_period)) / 2)]) * 1000
    f2 = np.mean(1 / spike_period[int((len(spike_period)) / 2):]) * 1000

    # finds variance of spiking rate
    f_var = np.var(1 / spike_period)

    f_avg = (f1 + f2) / 2
    # print(f1, f2, f_avg, f_var)
    return [f1, f2, f_avg], f_var

#spiking_threshold
threshold = -30

# working directory
directory = "C:/Users/spand/OneDrive - University of Toronto/Year 4/Skinner Lab/\
Spiking Data/network_clamp_results/"
directory += "g_HCN/"

# files to compare
dat0 = "def_mytrace_29097_soma.dat"
dat1 = "006_mytrace_29097_soma.dat"
dat2 = "012_mytrace_29097_soma.dat"

# fname = ['','']
fname = ['', '', '']
fname[0] = directory + dat0
fname[1] = directory + dat1
fname[2] = directory + dat2

mean_freq = np.zeros((len(fname), 3))
var_freq = np.zeros(len(fname))

#create subplots for each conductance value
fig, ax = plt.subplots(len(fname), 1, sharex=True, sharey=True)
fig.suptitle("gid: 29097")
# plt.figure()
# plt.title("gid: 29097")
plt.ylabel('Voltage (mV)')
plt.xlabel('Time (ms)')

for i in range(len(fname)):
    x, y = np.loadtxt(fname[i], unpack=True, skiprows=1)
    ax[i].plot(x, y)
    ax[i].plot(x, x*0 + threshold, 'r')
    # print (x,y)
    f_mean, f_var = analyse(x, y)
    mean_freq[i] = f_mean
    var_freq[i] = f_var

print(mean_freq)
print(var_freq)

#gNav
# ax[0].set_title('gNavaxon = 0.064')
# ax[1].set_title('gNavaxon = 0.032')
# ax[2].set_title('gNavaxon= 0.096')
#gNavaxon
# ax[0].set_title('gNavaxon = 0.064')
# ax[1].set_title('gNavaxon = 0.032')
# ax[2].set_title('gNavaxon= 0.096')
#gKvA
#ax[0].set_title('gNavaxon = 0.064')
#ax[1].set_title('gNavaxon = 0.032')
#ax[2].set_title('gNavaxon= 0.096')
#gKdr
# ax[0].set_title('gKdr = 0.003')
# ax[1].set_title('gKdr = 0.03')
# ax[2].set_title('gKdr= 0.6')
#gHCN
ax[0].set_title('gHCN = 0.0006')
ax[1].set_title('gHCN = 0.006')
ax[2].set_title('gHCN = 0.012')

plt.tight_layout()

# plt.savefig(directory+'g_Navaxon_29097.png')
plt.show()
