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


file_name = "2022_04_30-ID_11.spc"
file_name2 = "2022_04_30-ID_02.spc"
file_name3 = "2022_04_30-ID_07.spc"
file_name_dark = "2022_04_30-ID_95.spc"
file_name_lamp = "2022_04_30-ID_91.spc"





"""
спектр частицы
"""

file = r"C:\Users\lysikova.dv\Documents\GitHub\Python_tasks_algorithm\spc_master_test\spectra\Spectrum_(LS6)-" + file_name
[x_1, y_1] = get_spectra (file)
x1 = x_1.tolist()
y1 = y_1.tolist()



"""
спектр частицы номер 2
"""

file = r"C:\Users\lysikova.dv\Documents\GitHub\Python_tasks_algorithm\spc_master_test\spectra\Spectrum_(LS6)-" + file_name2
[x_2, y_2] = get_spectra (file)
x2 = x_2.tolist()
y2 = y_2.tolist()

"""
спектр частицы номер 3
"""

file = r"C:\Users\lysikova.dv\Documents\GitHub\Python_tasks_algorithm\spc_master_test\spectra\Spectrum_(LS6)-" + file_name3
[x_3, y_3] = get_spectra (file)
x3 = x_3.tolist()
y3 = y_3.tolist()


DATA = pd.read_excel("glass_1.xlsx")# спектр кюветы
x_gl = DATA["Wavelength nm."]
y_gl = DATA["T%"]
x_glass = x_gl.tolist()
y_glass = y_gl.tolist()


i = 0
n = len(y1)
y1_new = []
x1_new = []

for i in range(n):
    if y1[i] > 0:
        y1_new.append(y1[i])
        x1_new.append(x1[i])


y_1_interp = np.interp(x1, x1_new, y1_new)


#print(y1_new)
y_glass_interp = np.interp(x1_new, x_glass, y_glass)


"""
Темновой ток
"""

file = r"C:\Users\lysikova.dv\Documents\GitHub\Python_tasks_algorithm\spc_master_test\spectra\Spectrum_(LS6)-" + file_name_dark
[x_dark, y_dark] = get_spectra (file)
xdark = x_dark.tolist()
ydark = y_dark.tolist()


"""
ФЛ красителя
"""

file = r"C:\Users\lysikova.dv\Documents\GitHub\Python_tasks_algorithm\spc_master_test\spectra\Spectrum_(LS6)-" + file_name_lamp
[x_lamp , y_lamp ] = get_spectra (file)
xlamp = x_lamp .tolist()
ylamp = y_lamp .tolist()




def transmittion(y):
    y_max = max(y_max - y_dark)


    yt = (y_max - y_dark) / ((y_lamp - y_dark) * y_glass_interp)
    return yt


#plt.plot(x1_new,  transmittion(y_1_interp), linewidth = 2)# конечный спектр
plt.plot(x1_new,  transmittion(y_1_interp), linewidth = 2)# конечный спектр
#plt.plot(x_2, y_2, linewidth = 3, label = 'Si NP')#
#plt.plot(x_3, y_3, linewidth = 2,  label = 'Au NP')#
#plt.plot(xdye, ydye)# конечный спектр
np.savetxt('x ' + file_name + ' .txt', x1_new)
np.savetxt('y ' + file_name + ' .txt', transmittion(y1_new))
plt.xlim(450, 950)
#plt.ylim(-1000, 100)
#plt.xlabel("Длина волны, нм")
plt.xlabel("Wavelength (nm)")
#plt.ylabel("Интенсивность, отн.ед.")
plt.ylabel("Intensity (a. u.)")
#plt.legend()
plt.title(file_name)
plt.show()
