from package import redact_ex

from package import \
    simpson_integrate, \
    recursive_integrate, \
    romberg_integrate


EXERCISE_18 = """\
Make a program that computes the integral of a function f(x)
in an interval [a, b] using the Romberg's rule for integration.
Apply that to the case f(x) = (x**2 + x + 1) * cos(x) and a = 0, b = pi/2\
"""

redact_ex(EXERCISE_18, 18)

import numpy as np

def f(x):
    return (x**2 + x + 1) * np.cos(x)

interval = [0, np.pi/2]

integral_ab = romberg_integrate(f, interval, prec = 1e-12)

print(f"Integrating f(x) in {interval!s} yields (Romberg):",
    integral_ab, sep = '\n')