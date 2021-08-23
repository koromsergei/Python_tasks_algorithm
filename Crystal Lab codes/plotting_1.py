import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pylab as pl
DATA = pd.read_excel("30.90.3.xlsx")


x = DATA["Length"]
x = x * 1000
x.hist(bins=15)
pl.suptitle("Au(30) / Si(90) структура 3")

pl.show()
