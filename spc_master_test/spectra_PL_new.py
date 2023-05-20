import pandas as pd
import spc
import copy
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import savgol_filter


def get_spectra(path_file):
    path_to_file = path_file
    spectra = spc.File(path_to_file) # Reading .spc file
    x, y = (spectra.x, spectra.sub[0].y) # x-value, y-value
    y = savgol_filter(y, 19, 2)
    return x, y


file_name = "2022_11_01-ID_69.spc"  # спектр частицы
file_name_dark = "2022_11_01-ID_06.spc"  # темновой ток

"""
Спектр частицы
"""
file = r"C:\Users\lysikova.dv\Documents\GitHub\Python_tasks_algorithm\spc_master_test\spectra\Spectrum_(LS6)-" + file_name
[x_1, y_1] = get_spectra(file)
x = x_1.tolist()
y = y_1.tolist()


"""
Темновой ток
"""

file = r"C:\Users\lysikova.dv\Documents\GitHub\Python_tasks_algorithm\spc_master_test\spectra\Spectrum_(LS6)-" + file_name_dark
[x_dark, y_dark] = get_spectra(file)
xdark = x_dark.tolist()
ydark = y_dark.tolist()

x_lim = 0
y_lim = len(y_dark)
#y_lim = 1700


def photolumence(y):
    yt = (y - y_dark[x_lim:y_lim])
    return yt



#y_max = max(transmittion(y1[l_lim:r_lim])) # наибольшее значение
#plt.plot(x1[0:2102], transmittion(y1[0:2102]) / max(transmittion(y1[0:2102])), linewidth = 2)# конечный спектр

#plt.plot(x[x_lim:y_lim], photolumence(y[x_lim:y_lim]) / max(photolumence(y[x_lim:y_lim])), linewidth = 2)# конечный спектр
#plt.plot(x[x_lim:y_lim], photolumence(y[x_lim:y_lim]), linewidth = 2) # конечный спектр
plt.plot(x, y, linewidth = 2) # конечный спектр



np.savetxt('x ' + file_name + ' .txt', x)
np.savetxt('y ' + file_name + ' .txt', y)


#plt.xlim(450, 900)
#plt.ylim(0.8, 1.1)
#plt.xlabel("Длина волны, нм")
plt.xlabel("Wavelength (nm)")
plt.xlabel("Raman shift (1/cm)")
#plt.ylabel("Интенсивность, отн.ед.")
plt.ylabel("Intensity (a. u.)")
#plt.legend()
plt.title(file_name)
plt.show()
