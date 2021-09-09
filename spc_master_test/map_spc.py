# %%

import spc
import matplotlib.pyplot as plt
import numpy as np
import scipy.interpolate as intp
from scipy.signal import savgol_filter
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# %%
"""
# #dark current file
spc_dark_cur_filename = "D:/Documents/YandexDisk/ITMO/exp_data/2020-12-23/Point_3_3_sec_30x30.spc"
spc_dark_cur_data = spc.File(spc_dark_cur_filename)
print("SPC dark current file is readed")
print("Range", spc_dark_cur_data.x.min(), '...', spc_dark_cur_data.x.max(), spc_dark_cur_data.xlabel)
"""
# %%

spc_filename = r"C:\Users\79218\Git\Python_tasks_algorithm\spc_master_test\30 90 spec 800 obr 1 3x3.spc"
spc_data = spc.File(spc_filename)
x = spc_data.x[::-1]  # wavelength or wavenumber

y_shape, z_shape = int(spc_data.fnsub / spc_data.fwplanes), spc_data.fwplanes  # scan matrix shape

spectras = []
for i in spc_data.sub:
    spectras.append(intp.interp1d(x, i.y[::-1]))
#     spectras.append( intp.interp1d(x, (i.y-spc_dark_cur_data.sub[0].y)[::-1]) )#with dark current
spec = np.array(spectras).reshape(z_shape, y_shape)

x_label = spc_data.xlabel  # x label
val_label = spc_data.ylabel  # y label

y = np.linspace(0, y_shape - 1, num=y_shape, dtype=int)
z = np.linspace(0, z_shape - 1, num=z_shape, dtype=int)

print("SPC data file is readed")
print("Range", x.min(), '...', x.max(), x_label)
print("Scan area:", y_shape, 'x', z_shape, 'points')

# %%

Lambda = 800
# Lambda = np.linspace(1500, 1600, 51)  # nm
title = r"$\lambda$ = " + str(Lambda) + " nm"
res = []
for j in z:
    y_val = []
    for i in y:
        y_val.append(spec[j, i](Lambda).sum())
    res.append(np.array(y_val))
res = np.array(res)

# %%

fig1 = px.imshow((res / res.max()),
                 labels=dict(x=r"$x, \mu m$",
                             y=r"$y, \mu m$",
                             color="Intensity, a.u.",
                             ),

                 x=spc_data.fzinc * y,
                 y=spc_data.fwinc * z,
                 origin='lower',
                 width=640,
                 #                 zmin=0,
                 #                 zmax=1,
                 aspect='equal'
                 #                 color_continuous_scale="Viridis"
                 )

fig1.update_layout(
    title="Real Coordinates",
    font=dict(
        size=24,
        color="RebeccaPurple"
    )

)

fig1.show()

# %%

fig2 = px.imshow((res / res.max()),
                 labels=dict(x="x",
                             y="y",
                             color="Intensity, a.u.",
                             ),

                 x=y,
                 y=z,
                 origin='lower',
                 width=640,
                 #                 zmin=0,
                 #                 zmax=1,
                 aspect='equal'
                 #                 color_continuous_scale="Viridis"
                 )

fig2.update_layout(
    title="Matrix Coordinates",
    font=dict(
        size=24,
        color="RebeccaPurple"
    )

)
fig2.show()

# %%

# For known coordinates(work badly)
# point_data = [1.104741,1.380926]
# point_int = [int(point_data[0]/spc_data.fzinc), int(point_data[1]/spc_data.fwinc)]

# For known coordinates
point_int = [29, 0]
data_point = spec[point_int[1], point_int[0]](x)
data_savgol = savgol_filter(data_point, 11, 1)
real_coord = [spc_data.fzinc * point_int[0], spc_data.fwinc * point_int[1]]
print("Coordinates:", real_coord)

# %%

fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=data_point,
                         mode='lines',
                         name='Measured'))

fig.add_trace(go.Scatter(x=x, y=data_savgol,
                         mode='lines',
                         name='SavGol filtered'))
fig.show()

# %%


# %%

# plt.title(title)
plt.imshow(res, origin='lower',
           #            vmin=0,vmax=1,
           extent=[0, spc_data.fzinc * (y_shape - 1), 0, spc_data.fwinc * (z_shape - 1)])
plt.xlabel(r"$x, \mu m$")
plt.ylabel(r"$y, \mu m$")
cb = plt.colorbar()
cb.ax.set_ylabel("Intensity, a.u.")
plt.show()

# %%

plt.plot(x, data_point, label="Measured")
plt.plot(x, data_savgol, label="SavGol filtered")

plt.xlabel(x_label)
plt.ylabel(val_label)
plt.legend()
plt.show()

# %%


