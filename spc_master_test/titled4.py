#!/usr/bin/env python
# coding: utf-8

# In[2]:


import spc
import matplotlib.pyplot as plt
import numpy as np


def get_spectra(path_file):
    path_to_file = path_file
    spectra = spc.File(path_to_file) # Reading .spc file
    x, y = (spectra.x, spectra.sub[0].y) # x-value, y-value
    return x, y

file = "F:\ITMO UNIVERSITY\CRYSTAL LAB\Спектр\Spectrum_LS6_-2021_03_15-ID_73.spc"

[x,y] = get_spectra (file)
plt.plot (x,y)



file = "F:\ITMO UNIVERSITY\CRYSTAL LAB\Спектр\Spectrum_LS6_-2021_03_15-ID_76.spc"

[x,y] = get_spectra (file)
plt.plot (x,y)
plt.show()