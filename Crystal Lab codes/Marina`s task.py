import pandas as pd
import pylab as pl
#sheet_n = input('Введите имя таблицы')
sheet_n = '10sec-20kHz'

DATA = pd.read_excel("results_frequency_10sec.xlsx", sheet_name=sheet_n, dtype={'Length': float})
x = DATA["Length"]
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

while j+1 != len(dec):
    count = 0
    for i in range (len(x)):
        if x[i] > dec[j] and x[i] < dec[j+1]:
            dic["a"] = x[i]
            count += 1
    j += 1
       #renames the key

for i in range (len(x)):
    if x[i] > dec[len(dec)]:
        dic["a"] = x[i]
        count += 1


x.hist(bins=100)
pl.suptitle("Au(30) / Si(90) структура 3")

pl.show()
