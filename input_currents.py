import numpy as np
import matplotlib.pyplot as plt

def find_mean_curr(fname):
    DATA = np.loadtxt(fname)

    temp_curr_inh = np.zeros(len(DATA[:, 0]))
    temp_curr_exc = np.zeros(len(DATA[:, 0]))

    for t in range(len(temp_curr_exc)):
        temp_curr_inh[t] = np.sum(DATA[t, 1:3]) + np.sum(
            DATA[t, 4:10])  # find net inh input current at every time point
        temp_curr_exc[t] = DATA[t, 3] + np.sum(DATA[t, 10:])  # find net exc input current at every time point

    mean_current = np.mean(temp_curr_inh - temp_curr_exc)
    std_current = np.std(temp_curr_inh - temp_curr_exc)
    return mean_current, std_current

runs = ['04_SS_', '05_APC_', '08_SS_', '1_SS_', '12_SS_']
# gid = '21310'
gid_list = ['29097', '36884', '44671', '52458']
dir = 'C:/Users/spand/Documents/Skinner_Lab/exc_runs/'

col_names = ['time', 'sca', 'pvb', 'pyr', 'olm', 'ngf', 'ivy', 'cck', 'bis', 'axo', 'ecc', 'ca3']

for run in runs:
    run_curr = np.zeros(2)
    for gid in gid_list:
        filename = dir + 'ca1_1x_exc_' + run + gid + '_Inputs_by_Type.dat'
        run_curr += find_mean_curr(filename)
    run_curr /= len(runs)
    print(run, run_curr)

# fig, axs = plt.subplots(3, sharex = True)

# for i in range(1, 12):
#     axs[i-1].plot(DATA[:,0], DATA[:, i])

# axs[10].set_xlabel('Time (ms)')
# axs[6].set_ylabel('Input Current')

# axs[0].plot(DATA[:,0], temp_curr_exc)
# axs[1].plot(DATA[:,0], temp_curr_inh)
# axs[2].plot(DATA[:,0], temp_curr_inh - temp_curr_exc)
# axs[2].plot(DATA[:,0], mean_current * np.ones_like(DATA[:,0]))

# plt.show()

