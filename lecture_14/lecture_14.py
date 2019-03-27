from package import redact_ex

from package import range_kutta_differentiate, euler_differentiate, \
    euler_differentiate_mod

import numpy as np


EXERCISE_29 = """\
Make a program that is able to graphically solve the equation
d\u00B2x/dt\u00B2 + b dx/dt + \u03C9_0\u00B2 x = F cos(x) using:
+ the Euler method
+ the Range-Kutta method of order 2
+ the Range-Kutta method of order 4
Comment on the effects of \u0394t over the obtained solutions
(analyze the methods' stability with regards to the \u0394t used).\
"""

redact_ex(EXERCISE_29, 29)


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


EXERCISE_30 = """\
Make a program that is able to graphically solve the equation
dP/dt = rP * (1 - P/k) using:
+ the Euler method
+ the Range-Kutta method of order 2
+ the Range-Kutta method of order 4
Comment on the effects of \u0394t over the obtained solutions
(analyze the methods' stability with regards to the \u0394t used).\
"""

redact_ex(EXERCISE_30, 30)


# dp/dt = r*p * (1-p/k)

r = 1; k = 1
def incp(dt, t, p, r = r, k = k):
    return dt * r*p * (1-p/k)

print("Computing Euler method...", end='\n\n')
euler_differentiate([inct, incp], bounds = [0, 10],
    delta = 1e-3, itern = 3e3,
    title = r"Euler method for function"
        + r"$\:\:\frac{dP}{dt} = r\;P \: \left( 1 - \frac{P}{k} \right)$")

print("Computing Range-Kutta method of order 2...", end='\n\n')
range_kutta_differentiate([inct, incp], bounds = [0, 10], order = 2,
    delta = 1e-3, itern = 3e3,
    title = r"Range-Kutta method of order 2 for function"
        + r"$\:\:\frac{dP}{dt} = r\;P \: \left( 1 - \frac{P}{k} \right)$")

print("Computing Range-Kutta method of order 4...", end='\n\n')
range_kutta_differentiate([inct, incp], bounds = [0, 10], order = 4,
    delta = 1e-3, itern = 3e3,
    title = r"Range-Kutta method of order 4 for function"
        + r"$\:\:\frac{dP}{dt} = r\;P \: \left( 1 - \frac{P}{k} \right)$")


"""
Expanding on the previous comments about the importance of delta:
Take as an example the population exercise (EXERCISE_30) just above:
as prof. said, it describes the size of a population of beings
with some birth rate exposed to a number of resources
and certain environment conditions. For a given (constant)
amount of food and a fixed environment, a population will
stabilize its size on some number of members, after some time
(i.e. the members without food will end up dying).
If this happens very quickly, a deltat chosen too big (e.g. 1e-1 for this case)
will not catch the variation of the population since the start
up until it becomes stabilized, and therefore the program
will only plot a single line, or similar.
"""


EXERCISE_31 = """\
Make a program that is able to graphically solve the set of equations
{
    dx/dt = \u03C3 (y-x)
    dy/dt = r x - y - x z
    dz/dt = x y - b z
}
(Lorenz attractor) using:
+ the Euler method
+ the Range-Kutta method of order 2
+ the Range-Kutta method of order 4
Comment on the effects of \u0394t over the obtained solutions
(analyze the methods' stability with regards to the \u0394t used).\
"""

redact_ex(EXERCISE_31, 31)


# dx/dt
# dy/dt
# dz/dt

sigma = 3; r = 26.5; b = 1
ip = [0, 0, 1, 0] # initial parameters

def inct(dt, *o):   
    return dt

def incx(dt, t, x, y, z, sigma = sigma):
    return dt * sigma*(y-x)

def incy(dt, t, x, y, z, r = r):
    return dt * (r*x - y - x*z)

def incz(dt, t, x, y, z, b = b):
    return dt * (x*y - b*z)


print("Computing Euler method...", end='\n\n')
euler_differentiate([inct, incx, incy, incz], bounds = ip,
    delta = 1e-2, itern = 1e4, graph = [0, 3],
    title = r"Euler method for the Lorenz attractor")

print("Computing Range-Kutta method of order 2...", end='\n\n')
range_kutta_differentiate([inct, incx, incy, incz], bounds = ip, order = 2,
    delta = 1e-2, itern = 1e4, graph = [0, 3],
    title = r"Range-Kutta method of order 2 for the Lorenz attractor")

print("Computing Range-Kutta method of order 4...", end='\n\n')
range_kutta_differentiate([inct, incx, incy, incz], bounds = ip, order = 4,
    delta = 1e-2, itern = 1e4, graph = [0, 3],
    title = r"Range-Kutta method of order 4 for the Lorenz attractor")


EXERCISE_32 = """\
Make a program that is able to graphically solve any of the equations
proposed beforehand using a variable-step integration method.
(Chose the population equation.)\
"""

redact_ex(EXERCISE_32, 32)


# dp/dt = r*p * (1-p/k)

r = 1; k = 1
def incp(dt, t, p, r = r, k = k):
    return dt * r*p * (1-p/k)

print("Computing Euler method with variable-step...", end='\n\n')
euler_differentiate_mod([inct, incp], bounds = [0, 10],
    delta = 1e-2, itern = 1e2,
    step_mults = [0.5, 2], tols = [0.5, 0.1],
    max_delta = 1, min_delta = 1e-6, # verbose = True,
    title = r"Euler method for function"
        + r"$\:\:\frac{dP}{dt} = r\;P \: \left( 1 - \frac{P}{k} \right)\:\:$"
        + r"with variable-step")

# set kwarg `verbose` to True to see how delta varies