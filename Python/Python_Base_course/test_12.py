import time
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

# X, Y, Z, W = np.array([0, 6, 7]), np.array([2]), np.array([0, 2, 3]), np.array([10, 20, 30])

X, Y, Z, W = np.linspace(1, 10, 100), np.linspace(2, 20, 100), np.linspace(3, 30, 100), np.linspace(3, 30, 100)
start = time.time()

p = build_path_gl([X, Y, Z, W])
print(p)
print(time.time() - start)
# ax = plt.figure().add_subplot(projection='3d')
# ax.plot(*np.array(p)[:,:3].T)
# ax.plot(*np.array(p).T)

# plt.show()
