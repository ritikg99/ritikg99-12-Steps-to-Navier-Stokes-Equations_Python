import numpy
import sympy
from sympy import init_printing
from matplotlib import pyplot as plt
import time, sys

x, nu, t = sympy.symbols('x nu t')
phi = sympy.exp(-(x-4*t)**2/ (4*nu*(t+1))) + sympy.exp(-(x-4*t-2 * sympy.pi)**2/ (4*nu*(t+1)))

phiprime = phi.diff(x)

from sympy.utilities.lambdify import lambdify

u = -2 * nu * (phiprime/phi) + 4

ufunc = lambdify((t,x,nu), u)
print(ufunc(1,4,3))

nx = 101
dx = 2/(nx-1)
nt = 100
nu = 0.07
dt = dx * nu

x = numpy.linspace(0,2*numpy.pi, nx)
un = numpy.empty(nx)
t = 0

u = numpy.asarray([ufunc(t,x0,nu) for x0 in x])

for n in range(nt):
    un = u.copy()
    for i in range(1,nx-1):
        u[i] = un[i] - un[i]* dt/dx * (un[i]-un[i-1]) + nu * dt/dx**2 * (un[i+1] - 2*un[i] + un[i-1])

        u[0] = un[0] - un[0] * dt / dx * (un[0] - un[0 - 1]) + nu * dt / dx ** 2 * (un[1] - 2 * un[0] + un[-2])
        u[-1] = un[0]

u_analytical = numpy.asarray([ufunc(nt*dt, xi, nu) for xi in x])

plt.figure(figsize = (11,7), dpi = 100)
plt.plot(x,u, marker='o', lw=2, label='Computation')
plt.plot(x,u, label='Analytical')
plt.xlim([0,2*numpy.pi])
plt.ylim([0,10])
plt.legend()
plt.show();