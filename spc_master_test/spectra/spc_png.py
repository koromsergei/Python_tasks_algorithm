
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

def transmittion(y):
    y_t = (y - yd) / (y0 - yd)
    return y_t
"""
I0
спектр от структуры в воде. типа референс
"""
file = r"C:\Users\lysikova.dv\Documents\GitHub\Python_tasks_algorithm\spc_master_test\spectra\Spectrum_(LS6)-2022_03_10-ID_86.spc"
[x0, y0] = get_spectra (file)


"""
Id
темновой ток
"""
file = r"C:\Users\lysikova.dv\Documents\GitHub\Python_tasks_algorithm\spc_master_test\spectra\Spectrum_(LS6)-2022_03_10-ID_64.spc"
[xd, yd] = get_spectra (file)



"""
If
фотолюм родамина rh800 
"""
file = r"C:\Users\lysikova.dv\Documents\GitHub\Python_tasks_algorithm\spc_master_test\spectra\Spectrum_(LS6)-2022_03_15-ID_14.spc"
[xf, yf] = get_spectra (file)


"""
I
сам спектр в красителе
"""
file = r"C:\Users\lysikova.dv\Documents\GitHub\Python_tasks_algorithm\spc_master_test\spectra\Spectrum_(LS6)-2022_03_10-ID_64.spc"
[x, y] = get_spectra (file)
#plt.plot (x1, y1, label = 'Au_30нм/Si_180нм rare')# конечный спектр
#plt.plot (x, transmittion(y))
plt.plot (xf, yf)#
#plt.ylim(0,950)
#plt.xlim(400,950)
plt.xlabel("Длина волны, нм")
plt.ylabel("Интенсивность, отн.ед.")
# plt.ylim(75,1000)
#plt.legend()
plt.show()

#plt.savefig('DF_30/180_obr2_str2.png')
#plt.savefig('Spectrum_(LS6)-2021_05_04-ID_35')
