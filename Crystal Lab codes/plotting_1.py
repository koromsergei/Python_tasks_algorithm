import math

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pylab as pl
import scipy.optimize as sc

DATA = pd.read_excel("10.100.4.xlsx")
x = DATA["Length"]
x = x * 1000
a = 1
def gauss(a, x):
    return ((1 / a*np.sqrt(2 * np.pi)) * np.exp((-x ** 2) / 2))

y = np.linspace(0, len(x), 1)

f = gauss(a, x)

popt, pcov = sc.curve_fit(f, x, y)
plt.grid(True)
pl.suptitle("Au(30) / Si(90) структура 3")
pl.show()
plt.plot(x, popt)
