from package import redact_ex

from package import romberg_integrate

import numpy as np


EXERCISE_06 = """\
Make a program that computes the integral of a function f(x)
in an interval [a, b] using the Romberg's rule for integration.
Apply that to the case f(x) = (x**2 + x + 1) * cos(x) and a = 0, b = pi/2\
"""

redact_ex(EXERCISE_06, 6)


def f(x):
    return (x**2 + x + 1) * np.cos(x)

interval = [0, np.pi/2]

integral_ab = romberg_integrate(f, interval, prec = 1e-12)

print(f"Integrating f(x) in {interval!s} yields (Romberg):",
    integral_ab, sep = '\n')