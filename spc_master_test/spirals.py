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


file_name_CCW = "2022_07_07-ID_92.spc"#спектр пропускания
file_name_CW = "2022_07_07-ID_93.spc"#спектр пропускания

file_name_dark = "2022_07_07-ID_09.spc"#темновой ток
file_name_lamp_CW = "2022_07_07-ID_69.spc"#спектр лампы
file_name_lamp_CCW = "2022_07_07-ID_68.spc"#спектр лампы







"""
спектр пропускания CCW
"""

file = r"C:\Users\lysikova.dv\Documents\GitHub\Python_tasks_algorithm\spc_master_test\spectra\Spectrum_(LS6)-" + file_name_CCW
[x_1, y_1] = get_spectra (file)
xCCW = x_1.tolist()
yCCW = y_1.tolist()

"""
спектр пропускания CW
"""

file = r"C:\Users\lysikova.dv\Documents\GitHub\Python_tasks_algorithm\spc_master_test\spectra\Spectrum_(LS6)-" + file_name_CW
[x_2, y_2] = get_spectra (file)
xCW = x_2.tolist()
yCW = y_2.tolist()






"""
Темновой ток
"""

file = r"C:\Users\lysikova.dv\Documents\GitHub\Python_tasks_algorithm\spc_master_test\spectra\Spectrum_(LS6)-" + file_name_dark
[x_dark, y_dark] = get_spectra (file)
xdark = x_dark.tolist()
ydark = y_dark.tolist()

x_lim = 300
y_lim = len(y_dark)
#y_lim = 1700



"""
спектр лампы CW
"""

file = r"C:\Users\lysikova.dv\Documents\GitHub\Python_tasks_algorithm\spc_master_test\spectra\Spectrum_(LS6)-" + file_name_lamp_CW
[x_lamp , y_lamp ] = get_spectra (file)
xlampCW = x_lamp .tolist()
ylampCW = y_lamp .tolist()


"""
спектр лампы CCW
"""

file = r"C:\Users\lysikova.dv\Documents\GitHub\Python_tasks_algorithm\spc_master_test\spectra\Spectrum_(LS6)-" + file_name_lamp_CCW
[x_lamp1, y_lamp1 ] = get_spectra (file)
xlampCCW = x_lamp1 .tolist()
ylampCCW = y_lamp1 .tolist()








def transmittionCW(y):
    #yt = (y - y_dark[x_lim:y_lim]) / ((y_lamp[x_lim:y_lim]  - y_dark[x_lim:y_lim]) * (y_glass[x_lim:y_lim]  - y_dark[x_lim:y_lim] ))# учет стекла
    #yt = (y - y_dark[x_lim:y_lim]) / (y_lamp[x_lim:y_lim]  - y_dark[x_lim:y_lim])
    yt = (y - y_dark[x_lim:y_lim]) / (y_lamp[x_lim:y_lim]  - y_dark[x_lim:y_lim])
    #yt = (y - y_dark) / (y_glass - y_dark)
    return yt

def transmittionCCW(y):
    #yt = (y - y_dark[x_lim:y_lim]) / ((y_lamp[x_lim:y_lim]  - y_dark[x_lim:y_lim]) * (y_glass[x_lim:y_lim]  - y_dark[x_lim:y_lim] ))# учет стекла
    #yt = (y - y_dark[x_lim:y_lim]) / (y_lamp[x_lim:y_lim]  - y_dark[x_lim:y_lim])
    yt = (y - y_dark[x_lim:y_lim]) / (y_lamp1[x_lim:y_lim]  - y_dark[x_lim:y_lim])
    #yt = (y - y_dark) / (y_glass - y_dark)
    return yt


#y_max = max(transmittion(y1[l_lim:r_lim]))
#plt.plot(x1[0:2102], transmittion(y1[0:2102]) / max(transmittion(y1[0:2102])), linewidth = 2)# конечный спектр
#plt.plot(xCW[x_lim:y_lim], transmittion(yCW[x_lim:y_lim]) / max(transmittion(yCW[x_lim:y_lim])), linewidth = 2, label = 'CW')# конечный спектр
plt.plot(xCW[x_lim:y_lim], transmittionCW(yCW[x_lim:y_lim]), linewidth = 2, label = 'CW')# конечный спектр
#plt.plot(xCCW[x_lim:y_lim], transmittion(yCCW[x_lim:y_lim]) / max(transmittion(yCCW[x_lim:y_lim])), linewidth = 2, label = 'CCW')# конечный спектр
plt.plot(xCCW[x_lim:y_lim], transmittionCCW(yCCW[x_lim:y_lim]), linewidth = 2, label = 'CCW')# конечный спектр


np.savetxt('x ' + file_name_CW + ' .txt', xCW)
np.savetxt('y ' + file_name_CW + ' .txt', yCW)
np.savetxt('x ' + file_name_CCW + ' .txt', xCCW)
np.savetxt('y ' + file_name_CCW + ' .txt', yCCW)

plt.xlim(350, 1000)
#plt.ylim(0.8, 1.1)
#plt.xlabel("Длина волны, нм")
plt.xlabel("Wavelength (nm)")
#plt.ylabel("Интенсивность, отн.ед.")
plt.ylabel("Intensity (a. u.)")
plt.legend()
plt.title(file_name_CW)
plt.show()
