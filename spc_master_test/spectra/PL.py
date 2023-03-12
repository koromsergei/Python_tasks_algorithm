import spc
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import savgol_filter


def get_spectra(path_file):
    path_to_file = path_file
    spectra = spc.File(path_to_file) # Reading .spc file
    x, y = (spectra.x, spectra.sub[0].y) # x-value, y-value
    y = savgol_filter(y, 19, 2)
    return x, y


def pl(y, y_d):
    y_t = (y - y_d)
    return y_t

file_name = "Spectrum_(LS6)-2023_01_27-ID_24.spc"
file_name_d = 'Spectrum_(LS6)-2023_01_27-ID_17.spc'

file = fr"C:\Users\lysikova.dv\Documents\GitHub\Python_tasks_algorithm\spc_master_test\spectra\{file_name}"
[x, y] = get_spectra(file)
file = fr"C:\Users\lysikova.dv\Documents\GitHub\Python_tasks_algorithm\spc_master_test\spectra\{file_name_d}"
[x_d, y_d] = get_spectra(file)


plt.plot(x, pl(y, y_d), label='исходный спектр')
plt.show()

np.savetxt('x ' + file_name + ' .txt', x)
np.savetxt('y ' + file_name + ' .txt', pl(y, y_d))

