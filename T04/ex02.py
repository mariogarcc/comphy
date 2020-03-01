from package import redact_ex

from package import simpson_integrate

import numpy as np


EXERCISE_02 = """\
Make a program that computes the integral of a function f(x)
in an interval [a, b] using the rule of Simpson 1/3.
Apply that to the case f(x) = x**3 - 3*x**2 - x + 3 and a = 0, b = 1.35\
"""

redact_ex(EXERCISE_02, 2)


def f(x):
    return x**3 - 3*x**2 - x + 3

interval = [0, 1.35]

integral_ab = simpson_integrate(f, interval, method = '1/3', npoints = 1e5)

print(f"Integrating f(x) in {interval!s} yields (Simpson 1/3):",
    integral_ab, sep = '\n', end = '\n\n')