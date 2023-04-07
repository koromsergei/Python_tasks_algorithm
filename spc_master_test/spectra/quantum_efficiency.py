import spc
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
from numpy import trapz
import numpy as np
"""
измерение квантовой эффективности гибридной структуры
"""


def get_spectra(path_file):
    path_to_file = path_file
    spectra = spc.File(path_to_file)  # Reading .spc file
    x, y = (spectra.x, spectra.sub[0].y)  # x-value, y-value
    y = savgol_filter(y, 19, 2)
    return x, y


def photolum(y, y_d):
    # y_t = y - y_d
    y_t = y
    return y_t


# Темновой ток
file_name_dark = "Spectrum_(LS6)-2023_03_04-ID_02.spc"
file = rf"C:\Users\sergej.koromyslov\Python_tasks_algorithm\spc_master_test\spectra\{file_name_dark}"
[xd, y_d] = get_spectra(file)
lim_start = int(len(y_d) / 2)
lim_end = 700
y_d = y_d[::-1]
y_d = y_d[lim_start:lim_end]
laser_power = [27, 24.4, 22.4, 20, 18.4, 16, 14]  # шаг мощности лазера
laser_power_mj = [2.7, 2.44, 2.24, 2.0, 1.84, 1.6, 1.4]  # шаг мощности лазера
laser_power_uj_temp = [i * 1000 for i in laser_power_mj]  # шаг мощности лазера
laser_power_uj = [699, 599, 497, 399, 298, 198, 100, 91, 81, 71, 61, 51]

inegr_intencity = []
# Пропускание частицы
lim_start = 2897
lim_start = 2660
# lim_end = 2990
lim_end = 2740

for i in range(27, 40):
    if i == 102 or i == 93 or i == 94 or i == 98 or i == 92 or i == 114:
        continue
    file_name = f"Spectrum_(LS6)-2023_03_13-ID_{i}.spc"
    file = rf"C:\Users\sergej.koromyslov\Python_tasks_algorithm\spc_master_test\spectra\{file_name}"
    [x, y] = get_spectra(file)
    print(len(x))
    # x = x[::-1]
    x = x[lim_start:lim_end]
    # y = y[::-1]
    y = y[lim_start:lim_end]
    print(len(x))
    inegr_intencity.append(trapz(y, x))
    # inegr_intencity.append(trapz(photolum(y, y_d), x))
    plt.plot(x, y)
    # plt.ylim(0, 7000)
    plt.xlabel("Wavelength, nm")
    plt.ylabel("Intensity, a.u.")
    plt.title(file_name, fontdict={'fontsize': 6.5})
    np.savetxt('x ' + str(i) + ' .txt', x)
    np.savetxt('y ' + str(i) + ' .txt', y)
    # plt.legend()
    plt.show()

print(inegr_intencity)
plt.plot(laser_power_uj, inegr_intencity, "o")
plt.xscale('log')
plt.yscale('log')
# plt.xlabel("Power, mW")
plt.xlabel("Power, mJ / cm ^2")
plt.ylabel("Integrated intensity, a.u.")
plt.show()



