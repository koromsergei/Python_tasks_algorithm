import numpy as np
from scipy.constants import h, c, k
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

from colour_system import cs_hdtv
cs = cs_hdtv

def plot3Dmap_nonshow(X, Y, Z):
    Z = np.array(Z)
    Nx = len(X)
    Ny = len(Y)
    X, Y = np.meshgrid(X, Y)
    Z = Z.reshape(Ny, Nx)

    # plt.imshow(Z, interpolation='bilinear')
    plt.pcolor(X, Y, Z)
    plt.colorbar()

def planck(lam, T):
    """ Returns the spectral radiance of a black body at temperature T.

    Returns the spectral radiance, B(lam, T), in W.sr-1.m-2 of a black body
    at temperature T (in K) at a wavelength lam (in nm), using Planck's law.

    """

    lam_m = lam / 1.e9
    fac = h*c/lam_m/k/T
    B = 2*h*c**2/lam_m**5 / (np.exp(fac) - 1)
    return B

fig, ax = plt.subplots()
# plt.subplot(1,2,1)
# The grid of visible wavelengths corresponding to the grid of colour-matching
# functions used by the ColourSystem instance.
lam = np.arange(380., 781., 5)



for i in range(24):
    # T = 500 to 12000 K
    T = 500*i + 500

    # Calculate the black body spectrum and the HTML hex RGB colour string
    # it looks like
    spec = planck(lam, T)
    # html_rgb = cs.spec_to_rgb(spec, out_fmt='html')
    #
    # # Place and label a circle with the colour of a black body at temperature T
    # x, y = i % 6, -(i // 6)
    # circle = Circle(xy=(x, y*1.2), radius=0.4, fc=html_rgb)
    # ax.add_patch(circle)
    # ax.annotate('{:4d} K'.format(T), xy=(x, y*1.2-0.5), va='center',
    #             ha='center', color=html_rgb)

    buf = cs.spec_to_xyz(spec)
    plt.plot(buf[0], buf[1], 'kx')

cX = list()
cY = list()

for i in range(len(lam) - 15):
    # T = 500 to 12000 K
    # T = 500*i + 500

    # Calculate the black body spectrum and the HTML hex RGB colour string
    # it looks like
    # spec = planck(lam, T)
    # html_rgb = cs.spec_to_rgb(spec, out_fmt='html')
    #
    # # Place and label a circle with the colour of a black body at temperature T
    # x, y = i % 6, -(i // 6)
    # circle = Circle(xy=(x, y*1.2), radius=0.4, fc=html_rgb)
    # ax.add_patch(circle)
    # ax.annotate('{:4d} K'.format(T), xy=(x, y*1.2-0.5), va='center',
    #             ha='center', color=html_rgb)
    spec = np.zeros(len(lam))
    spec[i] = 1
    buf = cs.spec_to_xyz(spec)
    cX.append(buf[0])
    cY.append(buf[1])

    plt.plot(buf[0], buf[1], 'g.')
cX.append(cX[0])
cY.append(cY[0])


print(np.interp(np.linspace(0,1,5), np.array(cX), np.array(cY)))

ixmax = np.where(cX == np.array(cX).max())
ixmin = np.where(cX == np.array(cX).min())
iymax = np.where(cY == np.array(cY).max())
iymin = np.where(cY == np.array(cY).min())

index = [int(ixmax[0]), int(ixmin[0]),int(iymax[0]),int(iymin[0][1])]




N = 100
for x in range(N):
    for y in range(N):

        rgb = cs.xyz_to_rgb([x / N, y / N, 1 - (x + y) / N], out_fmt='html')
        plt.plot(x / N, y / N, '.', color = rgb)


print(index, len(cX) - 1)

# plt.subplot(1,2,1)
plt.plot(cX, cY, 'k')
# plt.plot(cX[index[0]], cY[index[0]], 'yx')
# plt.plot(cX[index[1]], cY[index[1]], 'gx')
# plt.plot(cX[index[2]], cY[index[2]], 'bx')
# plt.plot(cX[index[3]], cY[index[3]], 'kx')

# plt.plot(cX[index[1]:index[0]], np.array(cY[index[1]:index[0]]) + 0.1, 'k')
# plt.plot(cX[0:index[1]], cY[0:index[1]], 'k')
# plt.plot(cX[index[1]:index[3]], cY[index[1]:index[3]], 'k')

plt.xlim([0, 1])
plt.ylim([0, 1])
ax.set_aspect("equal")


# # Set the limits and background colour; remove the ticks
# ax.set_xlim(-0.5,5.5)
# ax.set_ylim(-4.35, 0.5)
# ax.set_xticks([])
# ax.set_yticks([])
# ax.set_facecolor('k')
# # Make sure our circles are circular!
# ax.set_aspect("equal")
# plt.show()



def lerp(x, a, b):
    return a + x * (b-a)

def get_color(x, y, a, b, c, d):
    return np.array([lerp(y, lerp(x, a[i], b[i]),
                             lerp(x, c[i], d[i])) for i in range(3)])

# w = h = 200
# verts = [[255,0,0],[0,255,0],[0,0,255],[255,0,0]]
# verts = [[0,255,0],[0,0,255],[255,0,0],[0,0,0]]
# img = np.empty((h,w,3), np.uint8)
# for y in range(h):
#     for x in range(w):
#         img[y,x] = get_color(x/w, y/h, *verts)
# plt.subplot(1,2,2)
# plt.imshow(img)



file = open('sp1_.txt')

column_0 = list()
column_1 = list()
column_2 = list()
column_3 = list()
column_4 = list()
column_5 = list()
column_6 = list()
column_7 = list()
column_8 = list()
column_9 = list()
column_10 = list()
column_11 = list()


for line in file:
    check = line.split()
    if len(check) == 0:
        continue
    column_0.append(float(check[0]))
    column_1.append(float(check[1]))
    column_2.append(float(check[2]))
    column_3.append(float(check[3]))
    column_4.append(float(check[4]))
    column_5.append(float(check[5]))
    column_6.append(float(check[6]))
    column_7.append(float(check[7]))
    column_8.append(float(check[8]))
    #column_9.append(float(check[9]))
    #column_10.append(float(check[10]))
    #column_11.append(float(check[11]))

file.close()

PL = np.interp(lam, column_0, column_1)
coordinate = cs.spec_to_xyz(PL)
plt.plot(coordinate[0], coordinate[1], 'ko')



PL1 = np.interp(lam, column_0, column_2)
coordinate = cs.spec_to_xyz(PL1)
plt.plot(coordinate[0], coordinate[1], 'ko')


PL2 = np.interp(lam, column_0, column_3)
coordinate = cs.spec_to_xyz(PL2)
plt.plot(coordinate[0], coordinate[1], 'ko')

PL3 = np.interp(lam, column_0, column_4)
coordinate = cs.spec_to_xyz(PL3)
plt.plot(coordinate[0], coordinate[1], 'ko')



PL4 = np.interp(lam, column_0, column_5)
coordinate = cs.spec_to_xyz(PL4)
plt.plot(coordinate[0], coordinate[1], 'ko')



PL5 = np.interp(lam, column_0, column_6)
coordinate = cs.spec_to_xyz(PL5)
plt.plot(coordinate[0], coordinate[1], 'ko')


PL6 = np.interp(lam, column_0, column_7)
coordinate = cs.spec_to_xyz(PL6)
plt.plot(coordinate[0], coordinate[1], 'ko')



PL7 = np.interp(lam, column_0, column_8)
coordinate = cs.spec_to_xyz(PL7)
plt.plot(coordinate[0], coordinate[1], 'ko')

""""


PL8 = np.interp(lam, column_0, column_9)
coordinate = cs.spec_to_xyz(PL8)
plt.plot(coordinate[0], coordinate[1], 'ko')


PL9 = np.interp(lam, column_0, column_11)
coordinate = cs.spec_to_xyz(PL9)
plt.plot(coordinate[0], coordinate[1], 'ko')
coordinate = cs.spec_to_xyz(np.ones(np.size(lam)))
plt.plot(coordinate[0], coordinate[1], 'ko')
"""


plt.show()



# plt.subplot(1,2,2)
# plt.plot(column_0, column_2)
# plt.plot(lam, PL)


