import pandas as pd
import numpy as np
import pylab as pl
import matplotlib.pyplot as plt


#ЭТОТ КОД ДЛЯ ОБЛАСТИ C
DATA = pd.read_excel("data_asm.xlsx")
x = DATA["time C"]
x_ = DATA["time B"]
#y_ = DATA["amplitude B, mV"]
#y = DATA["amplitude C, mV"]
#y = DATA["FWHM C, nm"]
y = DATA["Q C"]
#y_ = DATA["FWHM B, nm"]
y_ = DATA["Q B"]
plt.plot(x, y/(10**21), marker='s', color='black')#для области С
plt.plot(x_, y_/(10**21), marker='s', color='black')#для области С
#plt.savefig("QC.png")
plt.ylim(0, 5.5*10**(-13))
#plt.ylim(0, 150)
#plt.ylim(0, 3500) #FWHF
plt.xlabel('Время, с')
#plt.ylabel('Амплитуда напряжения, мВ')
#plt.ylabel('Ширина на полувысоте, нм')
plt.ylabel('Заряд на поверхности, Кл')
plt.show()


"""


#ЭТОТ КОД ДЛЯ ОБЛАСТИ В 
DATA = pd.read_excel("data_asm.xlsx")
x = DATA["time B"]
#y = DATA["amplitude B, mV"]
y = DATA["FWHM B, nm"]
#y = DATA["Q B"]
plt.plot(x, y, marker='s', color='black')
#plt.plot(x, y/(10**21), marker='s', color='black') #для заряда
#plt.savefig("QC.png")
#plt.ylim(0, 150) # для напряжения
plt.ylim(0, 2500) # для ...
#plt.ylim(0, 4.5*10**(-13)) # для заряда
plt.xlabel('Время, с')
#plt.ylabel('Амплитуда напряжения, мВ')
plt.ylabel('Ширина на полувысоте, нм')
#plt.ylabel('Заряд на поверхности, Кл')
plt.show()
"""

"""
#ЭТОТ КОД ДЛЯ ОБЛАСТИ Амплитуда напряжения области В 
DATA = pd.read_excel("data_asm.xlsx")
x = DATA["time B"]
y = DATA["amplitude B, mV"]
plt.plot(x, y/(10**21), marker='s', color='black')
plt.xlabel('Время, с')
plt.ylabel('Амплитуда напряжения области В, мВ')
plt.show()

"""

"""
#ЭТОТ КОД ИЩЕТ Зависимость среднеквадратичного отклонения от размера области сканирования
sq_side = [1, 3, 10, 30]
rms = [3.56781, 4.43403, 4.50053, 4.45366]
plt.plot(sq_side, rms , 's')
plt.ylim(0, 5)
plt.xlim(0, 31)
plt.xlabel('среднеквадратичноеотклонение, нм')
plt.ylabel('Размер области сканирования, мкм')
plt.show()
"""




