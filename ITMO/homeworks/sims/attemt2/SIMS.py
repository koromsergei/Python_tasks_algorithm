import pandas as pd
import numpy as np
import pylab as pl
import matplotlib.pyplot as plt
"""
ЭТА ПРОГА НАХОДИТ ЗАВИСИМОСТЬ ИНТЕНСИВНОСТИ ОТ ВРЕМЕНИ (глубины)
"""

DATA = pd.read_excel("short data mg.xlsx", dtype={'Time[mn]': float, 'I/I': float})
x = DATA["deep"]
y = DATA["I/I"]

xx = x.tolist()
yy = y.tolist()
integr = np.trapz(yy, xx)
print(integr)
D = 10**15
l  = 212.2 * (10**(-9))
#RSF = D / (integr * l)
RSF = D / (integr * 10 ** (-7))

#plt.plot(x_, y_*RSF, marker='s', color='black')
plt.plot(x, y, marker='s', color='black')
plt.xlabel('глубина, нм')
plt.ylabel('In/Im')
#plt.savefig("INITIAL.png")
#plt.yscale('log')
plt.show()
print(RSF)