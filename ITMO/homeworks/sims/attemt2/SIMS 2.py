import pandas as pd
import numpy as np
import pylab as pl
import matplotlib.pyplot as plt
RFS = 8.63590989920847e+21
"""
ЭТА ПРОГА НАХОДИТ ЗАВИСИМОСТЬ КОНЦЕНТРАЦИИ ПРИМЕСИ 
ОТ ГЛУБИНЫ ЗАЛЕГАНИЯ В ОбРАЗЦЕ
"""

DATA1 = pd.read_excel("obrazec.xlsx", dtype={'Time[mn]': float, 'I/I': float})

#x = DATA1["deep c"]
x = DATA1["deep mg"]
y = DATA1["I Mg/ I Ga"]
#y = DATA1["I Mg/ I Ga c"]
#plt.plot(x_, y_*RFS, marker='s', color='black')
plt.plot(x, y * RFS, marker='s', color='black')

plt.xlabel('глубина залегания примеси, нм')
plt.ylabel('концентрация примеси, см^-3')
#plt.savefig("konc_ETALON.png")
plt.yscale('log')


plt.show()