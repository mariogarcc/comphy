from package import redact_ex

from package import euler_differentiate

import numpy as np
import warnings
warnings.filterwarnings('ignore')


EXERCISE_00 = """\
Make a program that is able to graphically solve the equation
dx/dt = sin(x) using the Euler method.\
"""

redact_ex(EXERCISE_00, 0)


# dx/dt = sin(x)

def inct(dt, *o):
    return dt

def incx(dt, t, x):
    return dt*np.sin(x)

print("Computing Euler method...", end='\n\n')
euler_differentiate([inct, incx], bounds = [0, 1], delta = 1e-2, itern = 1e4,
    title = r"Euler method for function"
        + r"$\:\:\frac{dx}{dt} = \sin(x)$")