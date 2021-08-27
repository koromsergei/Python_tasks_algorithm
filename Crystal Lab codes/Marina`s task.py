import pandas as pd
import numpy as np
import pylab as pl
import statistics
#sheet_n = input('Введите имя таблицы')
sheet_n = '10sec-20kHz'

DATA = pd.read_excel("results_frequency_10sec.xlsx", sheet_name=sheet_n, dtype={'Length': float})
x = DATA["Length"]
me = statistics.mean(x)#  mean :)
SD = np.std(x) #  Standard Deviation
CV = (SD / me) * 100
#PDI =
print("Mean is: ", me)
print("Standard Deviation is: ", SD)
print("The coefficient of variation is: ", CV, "%")

#y = DATA['Weight']
"""
start = int(input('Введите левую границу интервала'))
stop = int(input('Введите правую границу интервала'))
step = int(input('Введите шаг'))
"""
start = 0
stop = 1100
step = 50

i = start
dec = []  #decomposition (разбиение)
while i < stop:
    dec.append(i)
    i += step

dic = {}  #the dictionary is made
j = 0
weight = []
m = np.zeros((len(x), len(x)))

while j+1 != len(dec):
    count: int = 0
    for i in range(len(x)):
        if dec[j] < x[i] < dec[j + 1]:
            m[i, j] = x[i]
            count += 1
    m[:, j] = count * m[:, j]
    weight.append(count)
    j += 1
print(m)

count: int = 0
for k in range(len(x)):
    if x[k] > dec[len(dec)-1]:
        count += 1
        m[i, j] = x[k]
        i += 1
        j += 1
m[:, j] = count * m[:, j]

weight.append(count)
summa = np.sum(weight)
S: float = 0
for i in range(len(x)):
    for j in range(len(x)):
        S = m[i, j]
        S += S

summa1 = np.sum(m)
s = list(set(weight))
MW = np.dot(s, s) / len(x)  # mean of weight

PDI = S / summa
print("PDI is: ", PDI)


#x.hist(bins=100)
#pl.suptitle("Au(30) / Si(90) структура 3")
#pl.show()
