import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
DATA = pd.read_excel("10.100.1.xlsx")
import pylab as pl

"""
a=int(input())
b=int(input())
d=int(input())
"""

a=500
b=1250
d=50
#z=(b - a)//d
#DATA.plt(x="Length", y="Number")
#xx=np.linspace(a,b,z+1)
x=DATA["Length"]
x=x*1000
"""
i=0
count=0
c=list()
"""



x.hist()
pl.suptitle("Au(10) / Si(100) структура 1")




"""
#x=DATA.iloc[i:i+50]
for i in range(z+1):
    for j in range(len(x)):
        if x[j]>xx[i] and x[j]<xx[i+1]:
            count+=1
    c.append(count)
    count=0 


with open('Alpha_Particle.txt') as f:
    lines = f.readlines()
    x = [line.split()[0] for line in lines]
    y = [line.split()[1] for line in lines]
"""

#pd.set_option("display.max.columns", None)
#print(DATA.head(10))

"""
for i in range (z+1):
    
    plt.plot(xx[i:i+1],c[i])
"""
