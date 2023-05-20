import numpy as np
import matplotlib.pyplot as plt


def build_path_gl(axes):
    cur_crd = []
    path = []
    trends = [1] * len(axes)
    def build_path_in(axes):
        nonlocal cur_crd
        nonlocal path
        cur_ax = axes[-1]
        if trends[len(axes)-1] == -1:
            cur_ax = np.flip(cur_ax)
        for crd in cur_ax:
            cur_crd.append(crd)
            if len(axes) > 1:
                build_path_in(axes[:-1])
                trends[len(axes)-2] *= -1
            else:
                path.append(np.flip(cur_crd))
            cur_crd.pop(-1)
    build_path_in(axes)
    return path

# X, Y, Z = np.arange(0, 3), np.arange(10, 13), np.arange(20, 25)
X, Y, Z, = np.linspace(1, 1, 1), np.linspace(1, 1, 1), np.linspace(1, 1, 1)
p = build_path_gl([X, X, Z])

ax = plt.figure().add_subplot(projection='3d')
ax.plot(*np.array(p).T)
plt.show()

