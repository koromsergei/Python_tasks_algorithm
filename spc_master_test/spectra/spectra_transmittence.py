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


file_name = "2022_03_10-ID_60.spc"
file_name2 = "2022_03_10-ID_02.spc"
file_name3 = "2022_03_10-ID_07.spc"
file_name_dark = "2022_04_11-ID_26.spc"
file_name_dye = "2022_04_11-ID_23.spc"
file_name_water = "2022_04_11-ID_19.spc"

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

file = r"C:\Users\lysikova.dv\Documents\GitHub\Python_tasks_algorithm\spc_master_test\spectra\Spectrum_(LS6)-" + file_name_dye
[x_dye, y_dye] = get_spectra (file)
xdye = x_dye.tolist()
ydye = y_dye.tolist()

"""
интерполяция спектра родамина 


y_dye_interp = np.interp(x1, xdye, ydye)
y_dye = copy.deepcopy(y_dye_interp)
"""
"""
Спектр в воде 
"""

file = r"C:\Users\lysikova.dv\Documents\GitHub\Python_tasks_algorithm\spc_master_test\spectra\Spectrum_(LS6)-" + file_name_water
[x_w, y_w] = get_spectra (file)
xw = x_w.tolist()
yw = y_w.tolist()


def transmittion(y):
    yt = (y - y_dark - y_dark - y_dye ) / (y_w - y_dark)
    return yt


plt.plot(x_1, y_1, linewidth = 2, label = 'Hybrid NP')# конечный спектр
plt.plot(x_2, y_2, linewidth = 3, label = 'Si NP')#
plt.plot(x_3, y_3, linewidth = 2,  label = 'Au NP')#
#plt.plot(xdye, ydye)# конечный спектр

plt.xlim(450, 950)
#plt.ylim(-250, 250)
#plt.xlabel("Длина волны, нм")
plt.xlabel("Wavelength (nm)")
#plt.ylabel("Интенсивность, отн.ед.")
plt.ylabel("Intensity (a. u.)")
plt.legend()
#plt.title(file_name)
plt.show()
