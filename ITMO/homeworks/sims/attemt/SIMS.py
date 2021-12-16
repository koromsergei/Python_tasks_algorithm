import pandas as pd
import numpy as np
import pylab as pl
import matplotlib.pyplot as plt
"""
ЭТА ПРОГА НАХОДИТ ЗАВИСИМОСТЬ ИНТЕНСИВНОСТИ ОТ ВРЕМЕНИ
"""

DATA = pd.read_excel("nan.xlsx", dtype={'Time[mn] Mg': float, 'I/I': float})
x = DATA["Time[mn] Mg"]
y = DATA["I/I"]

xx = x.tolist()
yy = y.tolist()
integr = np.trapz(yy, xx)
D = 10**15
l  = 212.2 * (10**(-9))
RSF = D / (integr * l)



#plt.plot(x_, y_*RSF, marker='s', color='black')
plt.plot(x, y, marker='s', color='black')
plt.xlabel('время, мин')
plt.ylabel('In/Im')
#plt.savefig("INITIAL.png")
#plt.yscale('log')
plt.show()
print(RSF)