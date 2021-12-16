import pandas as pd
import numpy as np
import pylab as pl
import matplotlib.pyplot as plt
RFS = 2.9830320336689613e+18
"""
ЭТА ПРОГА НАХОДИТ ЗАВИСИМОСТЬ КОНЦЕНТРАЦИИ ПРИМЕСИ 
ОТ ГЛУБИНЫ ЗАЛЕГАНИЯ В ОБРАЗЦЕ
"""

DATA = pd.read_excel("nan 2.xlsx", dtype={'Time[mn] 133Cs 24Mg': float, 'I/I': float})
x = DATA["Time[mn] 133Cs 24Mg"]
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