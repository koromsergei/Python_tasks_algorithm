
import spc
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import savgol_filter


def get_spectra(path_file):
    path_to_file = path_file
    spectra = spc.File(path_to_file) # Reading .spc file
    x, y = (spectra.x, spectra.sub[0].y) # x-value, y-value
    y = savgol_filter(y, 20, 2)  
    return x, y



"""
file = "F:\ITMO UNIVERSITY\CRYSTAL LAB\Полезные программы\spc_master_test\Spectrum_(LS6)-2021_05_04-ID_143.spc" #спектр от зеркала
[x1,y1] = get_spectra (file)

file = "F:\ITMO UNIVERSITY\CRYSTAL LAB\Полезные программы\spc_master_test\Spectrum_(LS6)-2021_05_04-ID_140.spc" #темновой спектр 
[x2,y2] = get_spectra (file)
"""
file = "F:\ITMO UNIVERSITY\CRYSTAL LAB\Полезные программы\spc_master_test\Spectrum_(LS6)-2021_05_04-ID_72.spc"
[x,y] = get_spectra (file)
q=min(y)
plt.plot (x,y-q, label = 'Au_30нм/Si_180нм rare')# конечный спектр







plt.xlim(450,950)
plt.xlabel("Длина волны, нм")
plt.ylabel("Интенсивность, отн.ед.")
# plt.ylim(75,1000)
plt.legend()
plt.show()

#plt.savefig('DF_30/180_obr2_str2.png')
#plt.savefig('Spectrum_(LS6)-2021_05_04-ID_35')
