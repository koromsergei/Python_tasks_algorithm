import pandas as pd
import numpy as np
import pylab as pl
import matplotlib.pyplot as plt

DATA = pd.read_excel("2_layers.xlsx")
x = DATA["Wavelength nm."]
y = DATA["T%"]
plt.plot(x, y)
plt.show()