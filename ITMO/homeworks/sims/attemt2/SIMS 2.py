import pandas as pd
import numpy as np
import pylab as pl
import matplotlib.pyplot as plt
RFS = 2.2973278814682523e+23
"""
ЭТА ПРОГА НАХОДИТ ЗАВИСИМОСТЬ КОНЦЕНТРАЦИИ ПРИМЕСИ 
ОТ ГЛУБИНЫ ЗАЛЕГАНИЯ В ОбРАЗЦЕ
"""

DATA1 = pd.read_excel("short data.xlsx", dtype={'Time[mn]': float, 'I/I': float})

x_ = DATA1["deep"]
y_ = DATA1["I Mg"]

x = DATA1["deep 2 corr"]
y = DATA1["I/I cor"]
#plt.plot(x_, y_*RFS, marker='s', color='black')
plt.plot(x, y, marker='s', color='black')

plt.xlabel('глубина залегания примеси, нм')
plt.ylabel('концентрация примеси, см^-3')
#plt.savefig("konc_ETALON.png")
plt.yscale('log')


plt.show()