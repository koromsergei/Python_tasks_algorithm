import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

DATA = pd.read_excel("YAG Nd.xlsx")
x = DATA["Step"]
y = DATA["Intensity"]
plt.plot(x, y)
plt.show()
x_s = DATA["Inter_w"].dropna()
y_s = DATA["Inter_step"].dropna()
z_s = DATA["Inter_inten"].dropna()

x_1 = np.interp(x, y_s, x_s)
#plt.plot(x_1, y)
plt.show()

x_fit = np.polyfit(x_s, y_s, 1)
print(np.polyval(x_1, 2))
p = np.poly1d(x_fit)
x_new = np.linspace(396, 650, 100)
y_new = p(x_new)
plt.plot(x, p(x))
plt.show()

""""
x_s = DATA["Inter_w"].dropna()
y_s = DATA["Inter_step"].dropna()
z_s = DATA["Inter_inten"].dropna()
f = interpolate.interp2d(x_s, z_s)
x_new = np.linspace(400, 600, 100)
y_new = f(x_new)
"""