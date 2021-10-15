import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


name_x = "Kikuchi.xlsx"
DATA = pd.read_excel(name_x)
x = DATA["dB [µm]"]


plt.hist(x, bins=20)
plt.xlabel('Размер частиц, мкм')
plt.ylabel('Количество частиц, шт')
plt.title('AD-1-B ')
#plt.plot(x, y)
#plt.savefig('20kV.png')
plt.show()
