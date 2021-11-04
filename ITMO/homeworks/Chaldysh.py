from scipy import constants as const
import scipy.special as sc
import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate

# GaN
Ga_n = np.genfromtxt('GaN_n.csv', delimiter=',')
Ga_k = np.genfromtxt('GaN_k.csv', delimiter=',')
ImEps_GaN = np.zeros(len(Ga_n[:,1]),dtype='complex')
ReEps_GaN = np.zeros(len(Ga_n[:,1]))
Eps_GaN=np.zeros(len(Ga_n[:,1]),dtype='complex')
for i in range(len(Eps_GaN)):
    Eps_GaN[i]= (Ga_n[i,1]+1j*Ga_k[i,1])**2
    ReEps_GaN[i] = Eps_GaN[i].real
    ImEps_GaN[i] = Eps_GaN[i].imag
# plt.plot(Ga_k[:,0],ReEps_GaN, "g", label='Re(ε_GaN)')
# plt.plot(Ga_k[:,0],ImEps_GaN, "r", label='Im(ε_GaN)')
# plt.xlabel('Wavelength, μm',fontsize=14)
# plt.ylabel('d.u.',fontsize=14)
# plt.grid()
# plt.legend()
# plt.show()

# Pd
# Pd_n = np.genfromtxt('Pd_n.csv', delimiter=',')
# Pd_k = np.genfromtxt('Pd_k.csv', delimiter=',')
# ImEps_Pd = np.zeros(len(Pd_n[:,1]),dtype='complex')
# ReEps_Pd = np.zeros(len(Pd_n[:,1]))
# Eps_Pd=np.zeros(len(Pd_n[:,1]),dtype='complex')
# for i in range(len(Eps_Pd)):
#     Eps_Pd[i]= (Pd_n[i,1]+1j*Pd_k[i,1])**2
#     ReEps_Pd[i] = Eps_Pd[i].real
#     ImEps_Pd[i] = Eps_Pd[i].imag
# #plt.plot(Pd_n[:,0],ReEps_Pd, "g", label='Re(ε_Pd)')
# plt.plot(Pd_k[:,0],ImEps_Pd, "r", label='Im(ε_Pd)')
# plt.xlabel('Wavelength, μm',fontsize=14)
# plt.ylabel('d.u.',fontsize=14)
# plt.grid()
# plt.legend()
# # plt.show()

#Pd_new
Pd_n = np.genfromtxt('Pd_n_new.csv', delimiter=',')
n_Pd =Pd_n[:,1]
Pd_k = np.genfromtxt('Pd_k_new.csv', delimiter=',')
k_Pd =Pd_k[:,1]
ImEps_Pd = np.zeros(len(n_Pd),dtype='complex')
ReEps_Pd = np.zeros(len(n_Pd))
Eps_Pd=np.zeros(len(n_Pd),dtype='complex')
for i in range(len(Eps_Pd)):
    Eps_Pd[i]= (n_Pd[i]+1j*k_Pd[i])**2
    ReEps_Pd[i] = Eps_Pd[i].real
    ImEps_Pd[i] = Eps_Pd[i].imag
#plt.plot(Pd_n[:,0],ReEps_Pd, "g", label='Re(ε_Pd)')
# plt.plot(Pd_k[:,0],ImEps_Pd, "r", label='Im(ε_Pd)')
# plt.xlabel('Wavelength, μm',fontsize=14)
# plt.ylabel('d.u.',fontsize=14)
# plt.grid()
# plt.legend()
# plt.show()
# exit()

# обрезаем
ReGa_new=ReEps_GaN[275:]
ImGa_new=ImEps_GaN[275:]
Eps_GaN =  Eps_GaN[275:]
RePd_new = ReEps_Pd[:473]
ImPd_new = ImEps_Pd[:473]
Eps_Pd = Eps_Pd[:473]
print(len(ImPd_new),len(ReGa_new))
#exit()
RePd=[]
ImPd = []
lam = Pd_n[:473,0]
lamm=[]
Eps_Pd_new = []
for i in range(len(RePd_new)):
    if i%2!=0:
        RePd.append(RePd_new[i])
        ImPd.append(RePd_new[i])
        lamm.append(lam[i])
        Eps_Pd_new.append(Eps_Pd[i])
    else:
        continue
RePd = RePd[:225]
ImPd = ImPd[:225]
lamm =lamm[:225]
Eps_Pd_new = Eps_Pd_new[:225]

k = np.zeros(len(lamm),dtype='complex')
Rek = np.zeros(len(lamm))
Imk=np.zeros(len(lamm))
c= 3*1e8
for i in range(len(k)):
    k[i] =(2*np.pi*c/(lamm[i]*1e-6))/c  * np.sqrt(Eps_Pd_new[i] * Eps_GaN[i] / (Eps_Pd_new[i] + Eps_GaN[i]))
    Rek[i] = k[i].real
    Imk[i] = k[i].imag

lamb = np.zeros(len(lamm))
for i in range(len(lamb)):
    lamb[i]=lamm[i]
print(len(lamb))
plt.plot(Imk,2 * np.pi * c /lamb/1e-6,'.', label='Im(k)')
plt.plot(Imk,2 * np.pi * c /lamb/1e-6,'--', label='approximation of line')
plt.xlabel('Im{k} , 1/m', fontsize=14)
plt.ylabel('frequency, Hz', fontsize=14)
plt.grid()
plt.legend()
plt.show()



