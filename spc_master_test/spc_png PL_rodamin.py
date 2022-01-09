
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

"""

file = "F:\ITMO UNIVERSITY\CRYSTAL LAB\Полезные программы\spc_master_test\Spectrum_(LS6)-2021_11_30-ID_46.spc"
[x,y] = get_spectra (file)

q=min(y)
plt.plot (x, y - q)# конечный спектр

file = "F:\ITMO UNIVERSITY\CRYSTAL LAB\Полезные программы\spc_master_test\Spectrum_(LS6)-2021_11_30-ID_47.spc"
[x,y] = get_spectra (file)

q=min(y)
plt.plot (x, y - q)# конечный спектр

"""
file = "F:\ITMO UNIVERSITY\CRYSTAL LAB\Полезные программы\spc_master_test\Spectrum_(LS6)-2021_11_30-ID_48.spc"
[x1, y1] = get_spectra (file)

q1 = min(y1)
#plt.plot (x1, y1 - q1)# конечный спектр


file = "F:\ITMO UNIVERSITY\CRYSTAL LAB\Полезные программы\spc_master_test\Spectrum_(LS6)-2021_11_30-ID_49.spc"
[x, y] = get_spectra (file)

q = min(y)
plt.plot (x, y - y1)# конечный спектр




plt.xlim(450,850)
plt.xlabel("Длина волны, нм")
plt.ylabel("Интенсивность, отн.ед.")
# plt.ylim(75,850)
plt.legend()
plt.show()

#plt.savefig('DF_30/180_obr2_str2.png')
#plt.savefig('Spectrum_(LS6)-2021_05_04-ID_35')
