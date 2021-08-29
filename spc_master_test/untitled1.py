# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 22:54:38 2021

@author: lysikova.dv
"""

#!/usr/bin/env python
# coding: utf-8

# In[2]:


import  spc
#from spc import File
import matplotlib.pyplot as plt


def get_spectra(path_file):
    path_to_file = path_file
    spectra = spc.File(path_to_file) # Reading .spc file
    x, y = (spectra.x, spectra.sub[0].y) # x-value, y-value
    return x, y

file = "F:\ITMO UNIVERSITY\CRYSTAL LAB\Полезные программы\spc_master_test\Spectrum_(LS6)-2021_04_18-ID_77.spc"

[x,y] = get_spectra (file)
plt.plot (x,y)

plt.savefig('Spectrum_(LS6)-2021_04_18-ID_49.png')