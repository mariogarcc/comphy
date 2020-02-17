from package import redact_ex

from package import \
    simpson_integrate, \
    recursive_integrate, \
    romberg_integrate


EXERCISE_17 = """\
Make a program that computes the integral of a function f(x)
in an interval [a, b] using the recursive rule of Simpson 1/3.
Apply that to the case f(x) = (x**2 + x + 1) * cos(x) and a = 0, b = pi/2\
"""

redact_ex(EXERCISE_17, 17)

import numpy as np

def f(x):
    return (x**2 + x + 1) * np.cos(x)

interval = [0, np.pi/2]

integral_ab = recursive_integrate(f, interval, method = 'simpson', prec = 1e-12)

print(f"Integrating f(x) in {interval!s} yields (recursive Simpson 1/3):",
    integral_ab, sep = '\n')
