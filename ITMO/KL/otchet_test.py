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


name_x = "YAG Nd.xlsx"
DATA = pd.read_excel(name_x)
x = DATA["Step"]
y = DATA["Intensity"]
#y = {key:val for key, val in y.items() if val != 0}
lmbd, E = transition(x)
#.title('20 kV')
plt.xlabel('Step (a.u.)')
plt.ylabel('Intensity (a.u.)')
plt.plot(x, y)
#plt.savefig('20kV.png')
plt.show()
