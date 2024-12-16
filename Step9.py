import ax
import matplotlib

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot, cm

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


def laplace2D(p,y,dx,dy,tolerance):
    l1norm = 1
    pn = np.empty_like(p)

    while l1norm>tolerance:
        pn = p.copy()

        p[1:-1, 1:-1] = ((dy**2 * (pn[1:-1, 2:] + pn[1:-1, 0:-2]) + dx**2 * (pn[2:, 1:-1] + pn[0:-2, 1:-1])) /
                        (2 * (dx**2 + dy**2)))

        p[:, 0] = 0
        p[:, -1] = y
        p[0, :] = p[1, :]
        p[-1, :] = p[-2, :]
        l1norm = (np.sum(np.abs(p[:]) - np.abs(pn[:])) /
                  np.sum(np.abs(pn[:])))

        return p

nx = 31
ny = 31
dx = 2/(nx-1)
dy = 2/(ny-1)
c = 1

p = np.zeros((ny,nx))

x = np.linspace(0,2, nx)
y = np.linspace(0, 1, ny)

p[:, 0] = 0
p[:, -1] = y
p[0, :] = p[1, :]
p[-1, :] = p[-2, :]


p = laplace2D(p, y, dx, dy, 1e-4)

plot2D(x, y, p)
pyplot.show()
