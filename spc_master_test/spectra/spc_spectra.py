import pandas as pd
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


DATA = pd.read_excel("glass.xlsx")# спектр кюветы
x_gl = DATA["Wavelength nm."]
y_gl = DATA["T%"]
x_glass = x_gl.tolist()
y_glass = y_gl.tolist()
"""
спектр частицы
"""
file_name = "2021_04_18-ID_04.spc"
file = r"C:\Users\lysikova.dv\Documents\GitHub\Python_tasks_algorithm\spc_master_test\spectra\Spectrum_(LS6)-" + file_name
[x_1, y_1] = get_spectra (file)
x1 = x_1.tolist()
y1 = y_1.tolist()

i = 0
n = len(y1)
y1_new = []
x1_new = []

for i in range(n - 1):
    if y1[i] > 0:
        y1_new.append(y1[i])
        x1_new.append(x1[i])


y_1_interp = np.interp(x1, x1_new, y1_new)

#print(y1_new)
y_glass_interp = np.interp(x1_new, x_glass, y_glass)
#plt.plot (x1, y1 / y2, label = 'Au_30нм/Si_180нм rare')# конечный спектр
#plt.plot(x1_new, y1_new)# конечный спектр
plt.plot(x1, y1)# конечный спектр

plt.xlim(450, 950)
#plt.ylim(-250, 250)
#plt.xlabel("Длина волны, нм")
plt.xlabel("Wavelength (nm)")
#plt.ylabel("Интенсивность, отн.ед.")
plt.ylabel("Intensity (a. u.)")
plt.legend()
#plt.title(file_name)
plt.show()


#plt.savefig('DF_30/180_obr2_str2.png')
#plt.savefig('Spectrum_(LS6)-2021_05_04-ID_35')
