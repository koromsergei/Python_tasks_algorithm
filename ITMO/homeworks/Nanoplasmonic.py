import pandas as pd
import numpy as np
import pylab as pl
import matplotlib.pyplot as plt
import statistics
c = 3 * (10**8)
DATA = pd.read_excel("Rakic.xlsx", dtype={'wavelength': float, 'k': float, 'n': float})
DATA1 = pd.read_excel("GaN.xlsx", dtype={'wavelength': float, 'k': float, 'n': float})
wf = DATA["wavelength"]
n = DATA["n"]
k = DATA["k"]
wf_GaN = DATA1["wl1"]
n_GaN = DATA1["n1"]
k_GaN = DATA1["k1"]
def perm(n, k):
    eps1 = (n**2) - (k**2)
    eps2 = 2 * n *k
    return eps1, eps2


eps1, eps2 = perm(n, k)
eps1_gan, eps2_gan = perm(n_GaN, k_GaN)

def dispertion (wf, eps1, eps2):
    k = (np.pi * 2) / wf
    b = k * np.sqrt((eps1 * eps2) / (eps1 + eps2))
    return b
tau = 1.87*10**(-14)
w = c * 2 * np.pi / wf_GaN
wp = float(3.626985756036e+15)
b = dispertion(wf, eps1, eps2)
#E1 = 1 - ((wp**2) / (w**2))
#E1 = 1 - (tau * (wp**2) / (1 + w**2  * tau**2))
#E2 = tau * (wp**2) / w * (1 + w**2  * tau**2)
b_re = dispertion(wf, eps1, eps1_gan)
b_im = dispertion(wf, eps2, eps2_gan)
"""
# plotting eps1 and eps2 
plt.plot(wf, eps2)
plt.title('imaginary part of permittivity, Al')
plt.xlabel('Wavelength, um')
plt.show()
"""

plt.plot(b_im * c / wp , w / wp)
plt.title('Imaginary part of dispertion')
plt.xlabel('Wavevector, 1/m')
plt.ylabel('Frequency, w/wp')
plt.show()
print(max(b_im * c ))