import scipy.optimize
import numpy as np
import math as mt
import matplotlib.pyplot as plt
import sympy as sym
def fun (x):
    u_hh = float(0.66)
    k = float(1.38 * 10**(-23))
    T = int(300)
    q = float(1.6 * 10**(-19))
    b = q / (k * T)
    f = u_hh - 1 / b * (mt.log(1 + b * x))
    return f
#x = sym.symbols('x')
x = np.linspace(0, 0.8, 1000)
u_hh = float(0.66)
k = 1.38 * 10**(-23)
T = int(300)
q = 1.6 * 10**(-19)
b = q / (k * T)
y1 = x
y2 = -x + u_hh - (1 / b) * (np.log(1 + b * x))
#.plot_implici(x,-x + u_hh - (1 / b) * (log(1 + b * x)) )
"""
x = Symbol('x')
u_hh = float(0.66)
k = 1.38 * 10**(-23)
T = int(300)
q = 1.6 * 10**(-19)
b = q / (k * T)
s = solve(-x + u_hh - (1 / b) * (log(1 + b * x)), x)
#print(ln(x))
#s = solve(mt.log(1 + b * x), x)
"""
plt.plot(x, y1, x, y2)
#sym.plot_implicit(x, y)
plt.show()