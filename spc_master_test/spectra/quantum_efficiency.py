import spc
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
from numpy import trapz

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
    y_t = (y - y_d)
    return y_t


# Темновой ток
file_name_dark = "Spectrum_(LS6)-2023_02_14-ID_118.spc"
file = rf"C:\Users\sergej.koromyslov\Python_tasks_algorithm\spc_master_test\spectra\{file_name_dark}"
[xd, y_d] = get_spectra(file)

laser_power = [27, 24.4, 22.4, 20, 18.4, 16, 14, 12]  # шаг мощности лазера
laser_power_mj = [2.7, 2.44, 2.24, 2.0, 1.84, 1.6, 1.4, 1.2]  # шаг мощности лазера
inegr_intencity = []
# Пропускание частицы
for i in range(69, 77):

    file_name = f"Spectrum_(LS6)-2023_02_14-ID_{i}.spc"
    file = rf"C:\Users\sergej.koromyslov\Python_tasks_algorithm\spc_master_test\spectra\{file_name}"
    [x, y] = get_spectra(file)
    inegr_intencity.append(trapz(y, x))
    plt.plot(x, photolum(y, y_d))
    plt.ylim(0, 7000)
    plt.xlabel("Wavelength, nm")
    plt.ylabel("Intensity, a.u.")
    plt.title(file_name, fontdict={'fontsize': 6.5})
    # plt.legend()
    plt.show()

print(inegr_intencity)
plt.plot(laser_power_mj, inegr_intencity, "o")
plt.xscale('log')
plt.yscale('log')
# plt.xlabel("Power, mW")
plt.xlabel("Power, mJ / cm ^2")
plt.ylabel("Integrated intensity, a.u.")
plt.show()



