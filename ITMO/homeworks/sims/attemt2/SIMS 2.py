import pandas as pd
import numpy as np
import pylab as pl
import matplotlib.pyplot as plt
RFS = 1.769687560406361e+17
"""
ЭТА ПРОГА НАХОДИТ ЗАВИСИМОСТЬ КОНЦЕНТРАЦИИ ПРИМЕСИ 
ОТ ГЛУБИНЫ ЗАЛЕГАНИЯ В ОбРАЗЦЕ
"""

DATA1 = pd.read_excel("short data.xlsx", dtype={'Time[mn]': float, 'I/I': float})

x_ = DATA1["deep"]
y_ = DATA1["I Mg"]

x = DATA1["deep corrected"]
y = DATA1["I Mg corrected"]
#plt.plot(x_, y_*RFS, marker='s', color='black')
plt.plot(x, y*RFS, marker='s', color='black')

plt.xlabel('глубина залегания примеси, нм')
plt.ylabel('концентрация примеси, см^-3')
#plt.savefig("konc_ETALON.png")
plt.yscale('log')


plt.show()