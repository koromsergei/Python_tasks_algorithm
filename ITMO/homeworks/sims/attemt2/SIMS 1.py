import pandas as pd
import numpy as np
import pylab as pl
import matplotlib.pyplot as plt
RFS = 2.2973278814682523e+23
"""
ЭТА ПРОГА НАХОДИТ ЗАВИСИМОСТЬ КОНЦЕНТРАЦИИ ПРИМЕСИ 
ОТ ГЛУБИНЫ ЗАЛЕГАНИЯ В ЭТАЛОНЕ
"""

DATA = pd.read_excel("short data mg.xlsx", dtype={'Time[mn]': float, 'I/I': float})
x = DATA["deep"]
y = DATA["I/I"]
y = y * RFS
"""
t = np.polyfit(x, y)
f = np.poly1d(t)
"""


plt.plot(x, y, marker='s', color='black')
plt.xlabel('глубина залегания примеси, нм')
plt.ylabel('концентрация примеси, см^-3')
plt.savefig("konc_obr.png")
plt.yscale('log')


plt.show()