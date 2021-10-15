import pandas as pd
import numpy as np
import pylab as pl
import matplotlib.pyplot as plt
import statistics
# DATA = pd.read_excel("stud1.xlsx", dtype={'Step': int, 'Intensity': float})
DATA = pd.read_excel("stud2.xlsx")
x = DATA["Step"]
y = DATA["Intensity"]
x_s = DATA["Inter_w"].dropna()
y_s = DATA["Inter_step"].dropna()
z_s = DATA["Inter_inten"].dropna()
count = 0
"""
xvals = np.linspace(200, 800, 516)
#f = np.polyval(x_fit, xvals)
"""
"""
xx = x[360:]
yy = y[360:]
x_fit = np.polyfit(x_s, z_s, 1)
p = np.poly1d(x_fit)
x_new = np.linspace(621, 800, 100)
y_new = p(x_new)
plt.plot(x_new, y_new)
"""




x_1 = np.interp(x, y_s, x_s)
plt.plot(x_1, y)
#plt.xlim(200, 800)
plt.xlabel('Wavelength, nm')
plt.ylabel('Intensity Nd, (a.u.)')

plt.savefig('Calibration_2_wavelength.png')
plt.show()