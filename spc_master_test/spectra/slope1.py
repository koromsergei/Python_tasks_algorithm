import pandas as pd
import spc
import copy
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import savgol_filter
import pandas as pd
import spc
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import savgol_filter
"""
программа, позволяющая найти слоп, ну или хотя бы значение интенсивностей 
"""


def get_spectra(path_file):
    path_to_file = path_file
    spectra = spc.File(path_to_file) # Reading .spc file
    x, y = (spectra.x, spectra.sub[0].y) # x-value, y-value
    y = savgol_filter(y, 19, 2)
    return x, y


slope = []
temp = []
power = [10, 15, 20, 30, 43, 55]
limit = 2569


"""
Id
темновой ток
"""
file = r"C:\Users\lysikova.dv\Documents\GitHub\Python_tasks_algorithm\spc_master_test\spectra\Spectrum_(LS6)-2022_03_10-ID_64.spc"
[xd, yd] = get_spectra (file)


for _ in range(limit):
    for i in range(33, 39, 1):
        j = 0
        n = str(i)
        file = r"C:\Users\lysikova.dv\Documents\GitHub\Python_tasks_algorithm\spc_master_test\spectra\Spectrum_(LS6)-2022_03_10-ID_" + n + ".spc"
        [x1, y1] = get_spectra(file)
        x1 = x1 - xd
        y1 = y1 - yd
        x = x1.tolist()
        y = y1.tolist()
        #temp.extend([y[_]])
        #np.polyfit(x, y, 2)
        temp.append(y[_])

        j += 1
    slope.append(np.polyfit(power, temp, 1))
    temp.clear()
    j = 0
    i = 0
    #slope.append(temp)
    #temp.clear()
#print(slope)
plt.plot(x, slope)
plt.yscale('log')
plt.xscale('log')



plt.show()