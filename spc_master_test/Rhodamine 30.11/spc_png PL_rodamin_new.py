import spc
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import savgol_filter
import pandas as pd


DATA = pd.read_excel("3_layers.xlsx")
x_rhod = DATA["Wavelength nm."]
y_rhod = DATA["T%"]

DATA1 = pd.read_excel("glass.xlsx")
x_glass = DATA1["Wavelength nm."]
y_glass = DATA1["T%"]


def get_spectra(path_file):
    path_to_file = path_file
    spectra = spc.File(path_to_file) # Reading .spc file
    x, y = (spectra.x, spectra.sub[0].y) # x-value, y-value
    y = savgol_filter(y, 19, 2)  
    return x, y


file = r"C:\Users\lysikova.dv\Documents\GitHub\Python_tasks_algorithm\spc_master_test\Rhodamine 30.11\Spectrum_(LS6)-2021_11_30-ID_21.spc"
[x1, y1] = get_spectra (file)
q1 = min(y1)
p1 = max(y1 - q1)
plt.plot (x1, (y1 - q1) , label = 'исходный')
#plt.plot (x1, y1 , label = 'исходный')

file = r"C:\Users\lysikova.dv\Documents\GitHub\Python_tasks_algorithm\spc_master_test\Rhodamine 30.11\Spectrum_(LS6)-2021_11_30-ID_24.spc"
[x, y] = get_spectra (file)
q = min(y)
p = max(y - q)
plt.plot (x, (y - q), label = 'с родамином')
#plt.plot (x, y , label = 'с родамином')

t1 = np.interp(x1, x_rhod, y_rhod)  #интерполированный родамин
t2 = np.interp(x1, x_glass, y_glass)  #интерполированное стекло
q3 = min(y1 / t1)
p3 = max((y1 / t1) - q3)
plt.plot (x1, ((y1 / t1) - q3) , label = ' исходный делить родамин')


plt.xlim(450,850)
plt.xlabel("Длина волны, нм")
plt.ylabel("Интенсивность, отн.ед.")
# plt.ylim(75,850)
plt.title(file, fontdict={'fontsize': 6.5})


plt.legend()
plt.show()
#plt.savefig('DF_30/180_obr2_str2.png')
#plt.savefig('Spectrum_(LS6)-2021_05_04-ID_35')
