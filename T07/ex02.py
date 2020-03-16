from package import redact_ex

from package import \
    euler_differentiate, \
    range_kutta_differentiate

import numpy as np


EXERCISE_02i = """\
Make a program that is able to graphically solve the equation
d\u00B2x/dt\u00B2 + b dx/dt + \u03C9_0\u00B2 x = 0 using the Euler method.\
"""

redact_ex(EXERCISE_02i, '2i')


# dx/dt = y
# dy/dt = -b*y - omega

b = 1/2; omega_0 = 2

def inct(dt, *o):
    return dt

def incx(dt, t, x, y):
    return dt * y

def incy(dt, t, x, y, b = b, omega_0 = omega_0):
    return dt * (-b*y - omega_0**2*x)

print("Computing Euler method...", end='\n\n')
euler_differentiate([inct, incx, incy], bounds = [0, 1, -1],
    delta = 1e-2, itern = 1e4, graph = [1, 2],
    title = r"Euler method for function"
        + r"$\:\:\frac{d^2x}{dt^2} + b \frac{dx}{dt} + \omega_0^2 x = 0$")


EXERCISE_02 = """\
Make a program that is able to graphically solve the equation
d\u00B2x/dt\u00B2 + b dx/dt + \u03C9_0\u00B2 x = F cos(x) using:
+ the Euler method
+ the Range-Kutta method of order 2
+ the Range-Kutta method of order 4
Comment on the effects of \u0394t over the obtained solutions
(analyze the methods' stability with regards to the \u0394t used).\
"""

redact_ex(EXERCISE_02, 2)


# dx/dt = y
# dy/dt = -b*y - omega_0**2*x + f*np.cos(omega*t)

b = 1/2; omega_0 = 4; f = 1; omega = 2

def inct(dt, *o):
    return dt

def incx(dt, t, x, y):
    return dt * y

def incy(dt, t, x, y, b = b, omega_0 = omega_0, f = f, omega = omega):
    return dt * (-b*y - omega_0**2*x + f*np.cos(omega*t))

print("Computing Euler method...", end='\n\n')
euler_differentiate([inct, incx, incy], bounds = [0, 0, 1],
    delta = 1e-2, itern = 1e4, graph = [1, 2],
    title = r"Euler method for function"
        + r"$\:\:\frac{d^2x}{dt^2} + b \frac{dx}{dt} + \omega_0^2 x = F \cos(\omega t)$")

print("Computing Range-Kutta method of order 2...", end='\n\n')
range_kutta_differentiate([inct, incx, incy], bounds = [0, 0, 1],
    delta = 1e-2, order = 2, itern = 1e4, graph = [1, 2],
    title = r"Range-Kutta method of order 2 for function"
        + r"$\:\:\frac{d^2x}{dt^2} + b \frac{dx}{dt} + \omega_0^2 x = F \cos(\omega t)$")

print("Computing Range-Kutta method of order 4...", end='\n\n')
range_kutta_differentiate([inct, incx, incy], bounds = [0, 0, 1],
    delta = 1e-2, order = 4, itern = 1e4, graph = [1, 2],
    title = r"Range-Kutta method of order 4 for function"
        + r"$\:\:\frac{d^2x}{dt^2} + b \frac{dx}{dt} + \omega_0^2 x = F \cos(\omega t)$")

omega = omega_0
def incy(dt, t, x, y, b = b, omega_0 = omega_0, f = f, omega = omega):
    return dt * (-b*y - omega_0**2*x + f*np.cos(omega*t))

euler_differentiate([inct, incx, incy], bounds = [0, 0, 1],
    delta = 1e-2, itern = 1e4, graph = [1, 2],
    title = r"Euler method for function"
        + r"$\:\:\frac{d^2x}{dt^2} + b \frac{dx}{dt} + \omega_0^2 x = F \cos(\omega_0 t)$")

# When omega_0 == omega, movement is a single sinusoidal wave since the start
# rather than a combination of two, as we can see in the early stages
# of the plots where omega_0 != omega.