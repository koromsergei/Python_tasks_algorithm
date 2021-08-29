
import spc
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import savgol_filter
import pylab

def get_spectra(path_file):
    path_to_file = path_file
    spectra = spc.File(path_to_file) # Reading .spc file
    x, y = (spectra.x, spectra.sub[0].y) # x-value, y-value
    y = savgol_filter(y, 19, 2)  
    return x, y

from scipy import integrate


I=[12,10,8,6]
array = []




"""
file = "F:\ITMO UNIVERSITY\CRYSTAL LAB\Полезные программы\spc_master_test\Spectrum_(LS6)-2021_05_04-ID_57.spc"
[x,y] = get_spectra (file)

a=x
b=y

v = integrate.trapz(a, b)
print(v)
array.append(v)

"""
file = "F:\ITMO UNIVERSITY\CRYSTAL LAB\Полезные программы\spc_master_test\Spectrum_(LS6)-2021_05_04-ID_58.spc"
[x,y] = get_spectra (file)

a=x
b=y
v = integrate.trapz(a, b)
print(v)
array.append(v)
file = "F:\ITMO UNIVERSITY\CRYSTAL LAB\Полезные программы\spc_master_test\Spectrum_(LS6)-2021_05_04-ID_59.spc"
[x,y] = get_spectra (file)

a=x
b=y
v = integrate.trapz(a, b)
print(v)
array.append(v)
file = "F:\ITMO UNIVERSITY\CRYSTAL LAB\Полезные программы\spc_master_test\Spectrum_(LS6)-2021_05_04-ID_60.spc"
[x,y] = get_spectra (file)

a=x
b=y
v = integrate.trapz(a, b)
print(v)
array.append(v)          
file = "F:\ITMO UNIVERSITY\CRYSTAL LAB\Полезные программы\spc_master_test\Spectrum_(LS6)-2021_05_04-ID_61.spc"
[x,y] = get_spectra (file)

a=x
b=y
v = integrate.trapz(a, b)
print(v)
array.append(v)
pylab.loglog (array,I,'go')# конечный спектр

from scipy import stats

X=np.log(array)
Y=np.log(I)
slope, intercept, r_value, p_value, std_err = stats.linregress(X,Y)
line = slope*X+intercept

plt.plot(line)


"""
p = np.polyfit(array,I, 2)
ya = np.polyval(p, array)
pylab.loglog(ya)
"""
plt.xlabel("Wavelength, nm")
plt.ylabel("Intensity, a.u.")

plt.legend()
plt.show()

#plt.savefig('DF_30/180_obr2_str2.png')
#plt.savefig('Spectrum_(LS6)-2021_05_04-ID_35')
