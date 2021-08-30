import pandas as pd
import numpy as np
import pylab as pl
import matplotlib.pyplot as plt
import statistics
#sheet_n = input('Введите имя таблицы')
sheet_n = '10sec-20kHz'

DATA = pd.read_excel("results_frequency_10sec.xlsx", sheet_name=sheet_n, dtype={'Length': float})
x = DATA["Length"]
me = statistics.mean(x)  #  mean :)
SD = np.std(x)  #  Standard Deviation
CV = (SD / me) * 100

print("Mean is: ", me)
print("Standard Deviation is: ", SD)
print("The coefficient of variation is: ", CV, "%")

"""
start = int(input('Введите левую границу интервала'))
stop = int(input('Введите правую границу интервала'))
step = int(input('Введите шаг'))
"""
start = 0
stop = 1150
step = 50

i = start
dec = []  #decomposition (разбиение)
while i < stop:
    dec.append(i)
    i += step

dic = {}  # the dictionary is made
j: int = 0
i: int = 0
weight = []
m = []
sum_prod: float = 0
temp_var: float = 0
while j+1 != len(dec):
    count: int = 0
    for i in range(len(x)):
        if dec[j] < x[i] < dec[j + 1]:
            m.append(x[i])
            count += 1

    temp_var = np.sum(m) * count
    sum_prod += temp_var
    temp_var = 0
    m.clear()
    weight.append(count)
    j += 1

count: int = 0
m.clear()
for k in range(len(x)):
    if x[k] > dec[len(dec)-1]:
        count += 1
        m.append(x[k])


temp_var = np.sum(m) * count
sum_prod += temp_var
weight.append(count)

summa = np.sum(np.dot(weight, weight))
PDI = sum_prod / me / summa
print("PDI is: ", PDI)
print("Средневзвешанное:", sum_prod / summa)
x1 = np.array(x)
a = np.hstack(x1)
plt.hist(a, bins=100, weights=np.ones(len(x1))*100 / len(x1),width = 100)
#x.hist(width = 1000)

np.histogram(x)
#pl.suptitle("Au(30) / Si(90) структура 3")
plt.xlim([0,1500])

plt.show()