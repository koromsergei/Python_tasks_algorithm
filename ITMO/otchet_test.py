import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def transition (x):
    a = 179.22707
    b1 = 0.024
    b2 = -0.0000000598785
    x_new = a + x * b1 + (x**2) * b2
    energ = 1239.85 / x_new
    return x_new, energ

name_x = "5_kV.xlsx"
DATA = pd.read_excel(name_x)
x = DATA["Step"]
y = DATA["Intensity"]
lmbd, E = transition(x)
plt.title(name_x)
plt.xlabel('Energy, eV')
plt.ylabel('Intensity (a.u.)')
plt.plot(E, y)
#plt.savefig('5kV.png')
plt.show()
