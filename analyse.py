import numpy as np
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
    # finds average isi for each interval
    t1 = np.mean(spike_period[:int((len(spike_period)) / 2)])
    t2 = np.mean(spike_period[int((len(spike_period)) / 2):])

    # finds std dev of spiking rate
    f_sd = np.std(1 / spike_period)
    t_sd = np.std(spike_period)

    f_avg = (f1 + f2) / 2
    t_avg = (t1 + t2) / 2
    # print(f1, f2, f_avg, f_var)
    return [f1, f2, f_avg, f_sd], [t1, t2, t_avg, t_sd]

