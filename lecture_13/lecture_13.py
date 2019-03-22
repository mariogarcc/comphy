from package import redact_ex

from package import euler_differentiate, range_kutta_differentiate


EXERCISE_26 = """\
Make a program that is able to graphically integrate the equation
dx/dt = sin(x) using the Euler method.\
"""

redact_ex(EXERCISE_26, 26)


import warnings
import numpy as np

warnings.filterwarnings('ignore')

# dx/dt = sin(x)

def inct(dt, *o):
    return dt

def incx(dt, x):
    return dt*np.sin(x)

# euler_differentiate([inct, incx], bounds = [0, 1], delta = 1e-2, itern = 1e4)


EXERCISE_27 = """\
Make a program that is able to graphically integrate the equation
d\u00B2x/dt\u00B2 + \u03C9_0\u00B2x = 0 using:
+ the Euler method
+ the Range-Kutta method of order 2
+ the Range-Kutta method of order 4
Comment on the effects of \u0394t over the obtained solutions
(analyze the methods' stability with regards to the \u0394t used).\
"""

redact_ex(EXERCISE_27, 27)


# dx/dt = y
# dy/dt = -omega**2*x

omega = 1

def inct(dt, *o):   
    return dt

def incx(dt, t, x, y):
    return dt * y

def incy(dt, t, x, y, omega = omega):
    return dt * (-omega**2*x)

# euler_differentiate([inct, incx, incy], bounds = [0, 1, -1],
#     delta = 1e-2, itern = 1e4S)
# range_kutta_differentiate([inct, incx, incy], bounds = [0, 1, -1],
#     delta = 1e-2, order = 4, itern = 1e4)


EXERCISE_28 = """\
Make a program that is able to graphically integrate the equation
d\u00B2x/dt\u00B2 + b dx/dt + \u03C9_0\u00B2 x = 0 using the Euler method.\
"""

redact_ex(EXERCISE_28, 28)


b = 1; omega_0 = 1

def incx(dt, t, x, y):
    return dt * y

def incy(dt, t, x, y, b = b, omega_0 = omega_0):
    return dt * (-b*y - omega_0**2*x)


# euler_differentiate([inct, incx, incy], bounds = [0, 1, -1],
#     delta = 1e-2, itern = 1e4)


EXERCISE_29 = """\
Make a program that is able to graphically integrate the equation
d\u00B2x/dt\u00B2 + b dx/dt + \u03C9_0\u00B2 x = F cos(x) using:
+ the Euler method
+ the Range-Kutta method of order 2
+ the Range-Kutta method of order 4
Comment on the effects of \u0394t over the obtained solutions
(analyze the methods' stability with regards to the \u0394t used).\
"""

redact_ex(EXERCISE_29, 29)


b = 1; omega_0 = 4; f = 1/2; omega = 2

def incx(dt, t, x, y):
    return dt * y

def incy(dt, t, x, y, b = b, omega_0 = omega_0, f = f, omega = omega):
    return dt * (-b*y - omega_0**2*x + f*np.cos(omega*t))


# euler_differentiate([inct, incx, incy], bounds = [0, 0, 1],
#     delta = 1e-2, itern = 1e4, graph = [0, 2])
# range_kutta_differentiate([inct, incx, incy], bounds = [0, 10, -1],
#     delta = 1e-2, order = 2, itern = 1e4)
# range_kutta_differentiate([inct, incx, incy], bounds = [0, 10, -1],
#     delta = 1e-2, order = 4, itern = 1e4)

# when omega_0 == omega, movement is a single sinusoidal wave since the start
# rather than a combination of two, as we can see in the early stages
# of the plots where omega_0 != omega



# overall, all methods have a succesful result dependent on the size of deltat
# this is because a small deltat is required to detect function changes
# "as soon as they happen" to provide an accurate representation
# of the functions

# Take as an example the population exercise (EXERCISE_XX):
# as prof. said, it describes the size of a population of beings
# with some birth rate exposed to a number of resources
# and certain environment conditions. For a given (constant)
# amount of food and a fixed environment, a population will
# stabilize its size on some number of members, after some time
# (i.e. the members without food will end up dying).
# If this happens very quickly, a deltat chosen too big will
# not catch the variation of the population since the start
# up until it becomes stabilized, and therefore the program
# will only plot a single line, or similar.