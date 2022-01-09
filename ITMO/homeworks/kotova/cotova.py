import pandas as pd
import numpy as np
import pylab as pl
import matplotlib.pyplot as plt

DATA = pd.read_excel("ZnSe.xlsx", dtype={'L': float, 'I': float})
DATAb = pd.read_excel("back.xlsx", dtype={'L': float, 'I': float})
DATAl = pd.read_excel("lamp.xlsx", dtype={'L': float, 'I': float})
xx = DATA["L"]
yy = DATA["I"]
x = xx.tolist()
y = yy.tolist()

xxb = DATAb["L"]
yyb = DATAb["I"]
xb = xxb.tolist()
yb = yyb.tolist()


xxl = DATAl["L"]
yyl = DATAl["I"]
xl = xxl.tolist()
yl = yyl.tolist()
y_main = []
x_eV = []
for _ in range(len(y)):
    y_main.append((y[_] - yb[_]) / yl[_])
    #y_main.append((y[_]) / 10**6)
    x_eV.append(1237 / x[_])
x_new = x_eV[::-1]
fig, ax1 = plt.subplots()
ax2 = ax1.twiny()
plt.xlim(3.3, 2.4)
#plt.xticks(np.arange(3.3, 2.4, 1))
ax1.plot(x, y_main, 'g-')
#ax2.plot(x_new, y_main, 'b-')
plt.axvline(x = 2.8346, color='r')
plt.axvline(x = 2.855)
ax1.set_xlabel("длина волны нм")
#ax1.set_ylabel("интенсивность *  10\u2076, у.е.")
ax1.set_ylabel("интенсивность, у.е.")
ax2.set_xlabel('E, eV')

plt.show()

"""
plt.plot(x, y_main)
plt.plot(x_eV, y_main)
plt.xlabel('длина волны нм')
plt.ylabel('интенсивность, у.е.')
plt.show()
"""
