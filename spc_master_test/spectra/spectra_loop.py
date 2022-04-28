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


"""
спектр частицы
"""
lim = 93
for j in range(33, 37, 1):
    i = str(j)
    file_name = "2022_03_10-ID_" + i +".spc"
    file = r"C:\Users\lysikova.dv\Documents\GitHub\Python_tasks_algorithm\spc_master_test\spectra\Spectrum_(LS6)-" + file_name
    [x_1, y_1] = get_spectra (file)
    x1 = x_1.tolist()
    y1 = y_1.tolist()
    y1new = [i / 2 for i in y1]
    fig = plt.figure()
    np.savetxt('x1 '+  str(i)+ ' .txt', x1)
    np.savetxt('y1 ' + str(i)+ ' .txt', y1)

    plt.plot(x1, y1)# конечный спектр

   # plt.xlim(450, 950)
    #plt.ylim(-250, 250)
    #plt.xlabel("Длина волны, нм")
    #ax.xlabel("Wavelength (nm)", fontsize=12, fontweight="bold")
    #plt.ylabel("Интенсивность, отн.ед.")
    #ax.ylabel("Intensity (a. u.)", fontsize=12, fontweight="bold")
    #plt.legend()
    #ax.axhline(linewidth=3, color="k")
    #ax.axvline(linewidth=1, color="k")

    plt.title(file_name)
    plt.show()
