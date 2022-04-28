import spc
import matplotlib.pyplot as plt
import numpy as np
import scipy.interpolate as intp
from scipy.signal import savgol_filter
import plotly.express as px
path_to_file = r"C:\Users\lysikova.dv\Documents\GitHub\Python_tasks_algorithm\spc_master_test\maps\array.spc"
y_shape = 30
z_shape = 30


spectra = spc.File(path_to_file) # Reading .spc file
x = spectra.x[::-1] # x-value(usually wavelength)

spectras = []
for i in spectra.sub:
    spectras.append(intp.interp1d(x, i.y[::-1]))
spectras = np.array(spectras)
spec = spectras.reshape(z_shape, y_shape).transpose()

x_label = spectra.xlabel # x label
y_label = spectra.ylabel # y label
y = np.linspace(0, y_shape-1, num=y_shape, dtype=int)
z = np.linspace(0, z_shape-1, num=z_shape, dtype=int)
Lambda = 1360 # nm
res = []
for i in y:
    z_val =[]
    for j in z:
        z_val.append(spec[i, j](Lambda))
    res.append(np.array(z_val))
res = np.array(res)

plt.imshow(np.rot90(res, 1))
plt.colorbar()

#plt.clim(45,100)
plt.show()