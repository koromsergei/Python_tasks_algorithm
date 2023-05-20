import spc
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import savgol_filter
import pandas as pd

"""
в этой программе изображается спектр фотолюма I = It - Id 
Id  - темновой ток 
"""


def get_spectra(path_file):
    path_to_file = path_file
    spectra = spc.File(path_to_file)  # Reading .spc file
    x, y = (spectra.x, spectra.sub[0].y)  # x-value, y-value
    y = savgol_filter(y, 19, 2)
    return x, y


def photolum(y, y_d):
    y_t = (y - y_d)
    return y_t


file_name_dark = "Spectrum_(LS6)-2023_01_27-ID_17.spc"

file = rf"C:\Users\sergej.koromyslov\Python_tasks_algorithm\spc_master_test\spectra\{file_name_dark}"
[xd, y_d] = get_spectra(file)

for i in range(10, 25, 1):
    file_name = f"Spectrum_(LS6)-2023_01_27-ID_{i}.spc"
    file = rf"C:\Users\sergej.koromyslov\Python_tasks_algorithm\spc_master_test\spectra\{file_name}"
    [x, y] = get_spectra(file)
    plt.plot(x, photolum(y, y_d))

    # plt.xlim(450,950)
    # plt.ylim(-1, 20)
    plt.xlabel("Wavelength, nm")
    plt.ylabel("Intensity, a.u.")
    plt.title(file_name, fontdict={'fontsize': 6.5})

    np.savetxt('x ' + str(i) + ' .txt', x)
    np.savetxt('y ' + str(i) + ' .txt', photolum(y, y_d))
    # plt.legend()
    plt.show()
    # plt.savefig('DF_30/180_obr2_str2.png')
    # plt.savefig('Spectrum_(LS6)-2021_05_04-ID_35')
