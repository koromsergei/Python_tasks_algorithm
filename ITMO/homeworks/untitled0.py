# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 22:02:50 2021

@author: lysikova.dv
"""

import scipy.optimize
import numpy as np
import math as mt
import matplotlib.pyplot as plt
from sympy import *

x = Symbol('x')
u_hh = float(0.66)
k = 1.38 * 10**(-23)
T = int(300)
q = 1.6 * 10**(-19)
b = q / (k * T)
I_f = int(30000)
#s = solve(-x + u_hh - (1 / b) * (log(1 + b * x)), x)
#print(ln(x))
#s = solve(mt.log(1 + b * x), x)
Um = 0.587
s = I_f * (1 - (k * T)/(q * Um))

print(s)