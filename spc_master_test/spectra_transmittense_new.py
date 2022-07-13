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


file_name = "2022_07_10-ID_97.spc"#спектр частицы, прошедшей через Rh
file_name_dark = "2022_07_10-ID_47.spc"#темновой

file_name_lamp = "2022_07_10-ID_01.spc"#спектр частицы без всего
file_name_glass = "2022_07_10-ID_94.spc"#спектр частицы через стекло или чтекло с водой






"""
спектр частицы, прошедшей через Rh
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

x_lim = 100
y_lim = len(y_dark)
#y_lim = 1700



"""
ФЛ частицы без стекла
"""

file = r"C:\Users\lysikova.dv\Documents\GitHub\Python_tasks_algorithm\spc_master_test\spectra\Spectrum_(LS6)-" + file_name_lamp
[x_lamp , y_lamp ] = get_spectra (file)
xlamp = x_lamp .tolist()
ylamp = y_lamp .tolist()

"""
ФЛ частицы со стеклом
"""

file = r"C:\Users\lysikova.dv\Documents\GitHub\Python_tasks_algorithm\spc_master_test\spectra\Spectrum_(LS6)-" + file_name_glass
[x_glass, y_glass ] = get_spectra (file)
xglass = x_glass.tolist()
yglass = y_glass.tolist()



def transmittion(y):
    #yt = (y - y_dark[x_lim:y_lim]) / ((y_lamp[x_lim:y_lim]  - y_dark[x_lim:y_lim]) * (y_glass[x_lim:y_lim]  - y_dark[x_lim:y_lim] ))# учет стекла
    #yt = (y - y_dark[x_lim:y_lim]) / (y_lamp[x_lim:y_lim]  - y_dark[x_lim:y_lim])
    yt = (y - y_dark[x_lim:y_lim]) / (y_glass[x_lim:y_lim]  - y_dark[x_lim:y_lim])
    #yt = (y - y_dark) / (y_glass - y_dark)
    return yt



#y_max = max(transmittion(y1[l_lim:r_lim]))
#plt.plot(x1[0:2102], transmittion(y1[0:2102]) / max(transmittion(y1[0:2102])), linewidth = 2)# конечный спектр
plt.plot(x1[x_lim:y_lim], transmittion(y1[x_lim:y_lim]) / max(transmittion(y1[x_lim:y_lim])), linewidth = 2)# конечный спектр
#plt.plot(x1[x_lim:y_lim], transmittion(y1[x_lim:y_lim]), linewidth = 2)# конечный спектр
#plt.plot(x_2, y_2, linewidth = 3, label = 'Si NP')#
#plt.plot(x_3, y_3, linewidth = 2,  label = 'Au NP')#
#plt.plot(xdye, ydye)# конечный спектр
np.savetxt('x ' + file_name + ' .txt', x1)
np.savetxt('y ' + file_name + ' .txt', y1)


plt.xlim(450, 900)
#plt.ylim(0.8, 1.1)
#plt.xlabel("Длина волны, нм")
plt.xlabel("Wavelength (nm)")
#plt.ylabel("Интенсивность, отн.ед.")
plt.ylabel("Intensity (a. u.)")
#plt.legend()
plt.title(file_name)
plt.show()
