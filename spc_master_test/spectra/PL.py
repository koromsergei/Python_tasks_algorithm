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


for i in range(122, 125):
    file_name = f"Spectrum_(LS6)-2023_04_13-ID_{i}.spc"
    file_name_d = 'Spectrum_(LS6)-2023_04_13-ID_71.spc'

    # file = fr"C:\Users\lysikova.dv\Documents\GitHub\Python_tasks_algorithm\spc_master_test\spectra\{file_name}"
    file = fr"C:\Users\sergej.koromyslov\Python_tasks_algorithm\spc_master_test\spectra\{file_name}"
    [x, y] = get_spectra(file)

    # file = fr"C:\Users\lysikova.dv\Documents\GitHub\Python_tasks_algorithm\spc_master_test\spectra\{file_name_d}"
    file = fr"C:\Users\sergej.koromyslov\Python_tasks_algorithm\spc_master_test\spectra\{file_name_d}"
    [x_d, y_d] = get_spectra(file)

    plt.plot(x, pl(y, y_d) / max(pl(y, y_d)), label='исходный спектр')
    plt.title(file_name)
    plt.show()

    np.savetxt('x ' + file_name + ' .txt', x)
    np.savetxt('y ' + file_name + ' .txt', pl(y / max(y), y_d))

