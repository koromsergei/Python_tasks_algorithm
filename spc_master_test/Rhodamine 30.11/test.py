import spc
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import savgol_filter
import pandas as pd

"""
в этой программе изображается спектр пропускания T = It - Id / I0 - Id 
Id  - темновой ток 
I0 - спектр кюветы
"""
DATA = pd.read_excel("3_layers.xlsx")
x_rh = DATA["Wavelength nm."]
y_rh = DATA["T%"]
x_rhod = x_rh.tolist()
y_rhod = y_rh.tolist()

DATA1 = pd.read_excel("glass.xlsx")# спектр кюветы
x_gl = DATA1["Wavelength nm."]
y_gl = DATA1["T%"]
x_glass = x_gl.tolist()
y_glass = y_gl.tolist()


def get_spectra(path_file):
    path_to_file = path_file
    spectra = spc.File(path_to_file) # Reading .spc file
    x, y = (spectra.x, spectra.sub[0].y) # x-value, y-value
    y = savgol_filter(y, 19, 2)
    return x, y

def transmittion(y):
    y_t = (y - y_d_interp) / (y_glass_interp - y_d_interp)
    return y_t
file = r"C:\Users\lysikova.dv\Documents\GitHub\Python_tasks_algorithm\spc_master_test\Rhodamine 30.11\Spectrum_(LS6)-2022_01_09-ID_72.spc"
[x, y] = get_spectra (file)

file = r"C:\Users\lysikova.dv\Documents\GitHub\Python_tasks_algorithm\spc_master_test\Rhodamine 30.11\Spectrum_(LS6)-2022_01_09-ID_68.spc"
[xn, yn] = get_spectra (file)

file = r"C:\Users\lysikova.dv\Documents\GitHub\Python_tasks_algorithm\spc_master_test\Rhodamine 30.11\Spectrum_(LS6)-2021_11_30-ID_46.spc"
[x1, y1] = get_spectra (file)

file = r"C:\Users\lysikova.dv\Documents\GitHub\Python_tasks_algorithm\spc_master_test\Rhodamine 30.11\Spectrum_(LS6)-2022_01_09-ID_10.spc"
[x_d, y_d] = get_spectra (file)

y_d_interp = np.interp(x, x_d, y_d)# интерполированный темновой ток
y_glass_interp = np.interp(x, x_glass, y_glass)# интерполированное стекло
y_rhod_interp = np.interp(x, x_rhod, y_rhod)  # интерполированный родамин

plt.plot (x, transmittion(y), label = 'Au Power 280')
plt.plot (xn, transmittion(yn), label = 'Au Power 140')
#plt.plot (x, transmittion(y_rhod_interp), label = 'родамин')
#plt.plot (x, transmittion(y / y_rhod_interp), label = 'исходный деленный на родамин')
#plt.plot (x1, transmittion(y1), label = 'спектр снятый с родамином')

plt.xlim(450,850)
plt.xlabel("Длина волны, нм")
plt.ylabel("Интенсивность, отн.ед.")
#plt.ylim(-1, 20)
plt.title(file, fontdict={'fontsize': 6.5})


plt.legend()
plt.show()
#plt.savefig('DF_30/180_obr2_str2.png')
#plt.savefig('Spectrum_(LS6)-2021_05_04-ID_35')
