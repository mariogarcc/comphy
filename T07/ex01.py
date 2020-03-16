from package import redact_ex

from package import \
    euler_differentiate, \
    range_kutta_differentiate


EXERCISE_01 = """\
Make a program that is able to graphically solve the equation
d\u00B2x/dt\u00B2 + \u03C9_0\u00B2x = 0 using:
+ the Euler method
+ the Range-Kutta method of order 2
+ the Range-Kutta method of order 4
Comment on the effects of \u0394t over the obtained solutions
(analyze the methods' stability with regards to the \u0394t used).\
"""

redact_ex(EXERCISE_01, 1)


# dx/dt = y
# dy/dt = -omega_0**2*x

omega_0 = 1

def inct(dt, *o):   
    return dt

def incx(dt, t, x, y):
    return dt * y

def incy(dt, t, x, y, omega_0 = omega_0):
    return dt * (-omega_0**2*x)

print("Computing Euler method...", end='\n\n')
euler_differentiate([inct, incx, incy], bounds = [0, 1, -1],
    delta = 1e-2, itern = 1e4, graph = [1, 2],
    title = r"Euler method for function"
        + r"$\:\:\frac{d^2x}{dt^2} + \omega_0^2 x = 0$")

print("Computing Range-Kutta method of order 2...", end='\n\n')
range_kutta_differentiate([inct, incx, incy], bounds = [0, 1, -1],
    delta = 1e-2, order = 2, itern = 1e4, graph = [1, 2],
    title = r"Range-Kutta method of order 2 for function"
        + r"$\:\:\frac{d^2x}{dt^2} + \omega_0^2 x = 0$")

print("Computing Range-Kutta method of order 4...", end='\n\n')
range_kutta_differentiate([inct, incx, incy], bounds = [0, 1, -1],
    delta = 1e-2, order = 4, itern = 1e4, graph = [1, 2],
    title = r"Range-Kutta method of order 4 for function"
        + r"$\:\:\frac{d^2x}{dt^2} + \omega_0^2 x = 0$")