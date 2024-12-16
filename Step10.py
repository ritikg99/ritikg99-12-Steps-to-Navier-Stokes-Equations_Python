import ax
import matplotlib

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot, cm

nx = 50
ny = 50
nt = 100
dx = 2/(nx-1)
dy = 1/(ny-1)

p = np.zeros((ny,nx))
pd = np.zeros((ny,nx))
b = np.zeros((ny,nx))
x = np.linspace(0,2,nx)
y = np.linspace(0,1,ny)

b[int(ny/4),int(nx/4)] = 100
b[int(3*ny/4),int(3*nx/4)] = -100

x = np.linspace(0,2, nx)
y = np.linspace(0, 1, ny)

for it in range(nt):
    pd = p.copy()

    p[1:-1, 1:-1] = ((pd[1:-1, 2:] + pd[1:-1, :-2])*dy**2 +
                       (pd[2:,1:-1] + pd[:-2, 1:-1]) * dx**2 -
                       b[1:-1, 1:-1] * dx**2 * dy**2) / (2 * (dx**2 + dy**2))

    p[0, :] = 0
    p[ny - 1, :] = 0
    p[:, 0] = 0
    p[:, nx - 1] = 0

def plot2D(x,y,p):
    fig = pyplot.figure()
    ax = fig.add_subplot(projection="3d")
    X,Y = np.meshgrid(x,y)
    surf = ax.plot_surface(X,Y,p[:], rstride=1, cstride=1, cmap=cm.viridis,
            linewidth=0, antialiased=False)
    ax.set_xlim(0, 2)
    ax.set_ylim(0, 1)
    ax.view_init(30, 225)

    pyplot.show()

plot2D(x, y, p)
pyplot.show()
