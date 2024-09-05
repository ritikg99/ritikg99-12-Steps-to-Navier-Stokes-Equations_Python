import ax
import matplotlib

import numpy as np
import inline

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot, cm
import matplotlib.animation as animation

nx = 81
ny = 81
nt = 100
c = 1
dx = 2/(nx-1)
dy = 2/(ny-1)
sigma = 0.2
dt = sigma*dx

x = np.linspace(0,2, nx)
y = np.linspace(0, 2, ny)

u = np.ones((ny,nx))
v = np.ones((ny,nx))
un = np.ones((ny,nx))
vn = np.ones((ny,nx))


u[int(0.5/dy):int(1/dy+1), int(0.5/dx):int(1/dy+1)] = 2
v[int(0.5/dy):int(1/dy+1), int(0.5/dx):int(1/dy+1)] = 2

for n in range(nt+1):
    un = u.copy()
    vn = v.copy()

    u[1:, 1:] = (un[1:, 1:] - (un[1:, 1:] * c * dt / dx * (un[1:, 1:] - un[1:, :-1])) -
                               vn[1:, 1:] * c * dt / dy * (un[1:, 1:] - un[:-1, 1:]))

    v[1:, 1:] = (vn[1:, 1:] - (un[1:, 1:] * c * dt / dx * (vn[1:, 1:] - vn[1:, :-1])) -
                               vn[1:, 1:] * c * dt / dy * (vn[1:, 1:] - vn[:-1, 1:]))

    u[0,:] = 1
    u[-1, :] = 1
    u[:, 0] = 1
    u[:, -1] = 1

    v[0, :] = 1
    v[-1, :] = 1
    v[:, 0] = 1
    v[:, -1] = 1

fig = pyplot.figure(figsize = (11,7), dpi = 100)
ax = fig.add_subplot(projection = "3d")
X, Y = np.meshgrid(x,y)
surf = ax.plot_surface(X,Y,u[:], cmap='viridis', rstride = 2, cstride = 2)
pyplot.show()