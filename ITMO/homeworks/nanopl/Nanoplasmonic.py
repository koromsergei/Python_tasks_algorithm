import pandas as pd
import numpy as np
import pylab as pl
import matplotlib.pyplot as plt
import statistics
c = 3 * (10**8)
DATA = pd.read_excel("Rakic1.xlsx", dtype={'wavelength': float, 'k': float, 'n': float})
DATA1 = pd.read_excel("GaN1.xlsx", dtype={'wavelength': float, 'k': float, 'n': float})
wf_pd = DATA["wavelength"]
n_pd = DATA["n"]
k_pd = DATA["k"]

wf_Al = wf_pd
wf_Al_list = wf_pd.tolist()
n_Al = n_pd
k_Al = k_pd

wf_GaN_pd = DATA1["wl1"]
n_GaN_pd = DATA1["n1"]
k_GaN_pd = DATA1["k1"]

wf_GaN = wf_GaN_pd
wf_GaN_list = wf_GaN_pd.tolist()
n_GaN = n_GaN_pd
k_GaN = k_GaN_pd

x = np.linspace(0, 0.4, 1000)


def perm(n, k):
    eps1 = (n**2) - (k**2)
    eps2 = 2 * n * k
    return eps1, eps2


eps1_al_pd, eps2_al_pd = perm(n_Al, k_Al)
eps1_gan_pd, eps2_gan_pd = perm(n_GaN, k_GaN)

eps1_al = eps1_al_pd.tolist()
eps2_al = eps2_al_pd.tolist()
eps1_gan = eps1_gan_pd.tolist()
eps2_gan = eps2_gan_pd.tolist()

eps1_al_interp = np.interp(x, wf_Al_list, eps1_al)
eps2_al_interp = np.interp(x, wf_Al_list, eps2_al)

eps1_gan_interp = np.interp(x, wf_GaN_list, eps1_gan)
eps2_gan_interp = np.interp(x, wf_GaN_list, eps2_gan)

eps1 = eps1_al_interp + 1j * eps2_al_interp
eps2 = eps1_gan_interp + 1j * eps2_gan_interp

def dispertion (wf, eps1, eps2):
    k = (np.pi * 2) / wf
    b = k * np.sqrt((eps1 * eps2) / (eps1 + eps2))
    return b

tau = 1.87*10**(-14)
w = c * 2 * np.pi / (x / 1000000)
wp = float(3.626985756036e+15)


"""
хз че
#E1 = 1 - ((wp**2) / (w**2))
#E1 = 1 - (tau * (wp**2) / (1 + w**2  * tau**2))
#E2 = tau * (wp**2) / w * (1 + w**2  * tau**2)
"""

b = dispertion(x /1000000, eps1, eps2)

#b_im = dispertion(wf, eps2, eps2_gan)
"""
# plotting eps1 and eps2 
plt.plot(wf, eps2)
plt.title('imaginary part of permittivity, Al')
plt.xlabel('Wavelength, um')
plt.show()
"""

plt.plot(b.real, w)
#plt.title('Imaginary part of dispertion')
plt.title('Real part of dispertion')
plt.xlabel('Re{β}, 1/m')
plt.ylabel('Frequency, Hz')
plt.ylim(0, 0.1*10**(18))# real
#plt.ylim(0, 0.3*10**(18))# imag
plt.axhline(y = 0.0075*10**(18), linestyle='--', color='r') # real
#plt.axvline(x = 0.578*10**(8), linestyle='--', color='r') # imag
plt.xlim(0, 0.15*10**(9))
plt.show()
#print(max(b_im * c ))