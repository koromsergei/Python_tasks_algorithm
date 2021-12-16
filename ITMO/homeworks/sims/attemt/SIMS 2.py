import pandas as pd
import numpy as np
import pylab as pl
import matplotlib.pyplot as plt
RFS = 2.9830320336689613e+18
"""
ЭТА ПРОГА НАХОДИТ ЗАВИСИМОСТЬ КОНЦЕНТРАЦИИ ПРИМЕСИ 
ОТ ГЛУБИНЫ ЗАЛЕГАНИЯ В ЭТАЛОНЕ
"""

DATA1 = pd.read_excel("data SIMS 1.xlsx")

x_ = DATA1["deep"]
y_ = DATA1["I/I"]
plt.plot(x_, y_*RFS, marker='s', color='black')

plt.xlabel('глубина залегания примеси, нм')
plt.ylabel('концентрация примеси, см^-3')
#plt.savefig("konc_ETALON.png")
plt.yscale('log')


plt.show()