import numpy as np
from scipy.integrate import odeint
from scipy.optimize import fsolve
import matplotlib.pyplot as plt


def ode_func(U, x, alfa):
    Pdrop = -100

    u1, u2 = U
    du1dy = u2
    du2dy = 1.0 / alfa * Pdrop
    return [du1dy, du2dy]


def calc(u2_0, u1_0, x, alfa):
    U = odeint(ode_func, [u1_0, u2_0], x, args=(alfa,))
    u1 = U[:,0]
    return u1[-1]


def shoot_func(alfa):
    d = 0.1
    x = np.linspace(0, d)
    u1_0 = 0

    u2_0, = fsolve(calc, 1.0, args=(u1_0, x, alfa))
    U = odeint(ode_func, [u1_0, u2_0], x, args=(alfa,))

    #plt.plot(x, U[:,0])
    #plt.plot([d],[0], 'ro')
    #plt.xlabel('x')
    #plt.ylabel('u')
    #plt.show()