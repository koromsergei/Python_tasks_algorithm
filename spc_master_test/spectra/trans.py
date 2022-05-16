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

file_name = "2022_04_30-ID_79.spc"
file_name_dark = "2022_04_30-ID_71.spc"
file_name_lamp = "2022_04_30-ID_70.spc"

"""
спектр частицы
"""

file = r"C:\Users\lysikova.dv\Documents\GitHub\Python_tasks_algorithm\spc_master_test\spectra\Spectrum_(LS6)-" + file_name
[x_1, y_1] = get_spectra (file)
x1 = x_1.tolist()
y1 = y_1.tolist()


"""
Темновой ток
"""

file = r"C:\Users\lysikova.dv\Documents\GitHub\Python_tasks_algorithm\spc_master_test\spectra\Spectrum_(LS6)-" + file_name_dark
[x_dark, y_dark] = get_spectra (file)
xdark = x_dark.tolist()
ydark = y_dark.tolist()

"""
спектр лампы
"""

file = r"C:\Users\lysikova.dv\Documents\GitHub\Python_tasks_algorithm\spc_master_test\spectra\Spectrum_(LS6)-" + file_name_lamp
[x_lamp , y_lamp ] = get_spectra (file)
xlamp = x_lamp .tolist()
ylamp = y_lamp .tolist()


def transmittion(y):
    yt = (y - y_dark) / (y_lamp - y_dark)
    return yt

y_max = max(transmittion(y1))
np.savetxt('x ' + file_name + ' .txt', x1)
np.savetxt('y ' + file_name + ' .txt', transmittion(y1) / y_max)


plt.plot(x1,  transmittion(y1) / y_max, linewidth = 2)# конечный спектр
plt.show()