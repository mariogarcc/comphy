from package import redact_ex

from package import recursive_integrate

import numpy as np


EXERCISE_04 = """\
Make a program that computes the integral of a function f(x)
in an interval [a, b] using the rule of the recursive trapeze.
Apply that to the case f(x) = (x**2 + x + 1) * cos(x) and a = 0, b = pi/2\
"""

redact_ex(EXERCISE_04, 4)


def f(x):
    return (x**2 + x + 1) * np.cos(x)

interval = [0, np.pi/2]


integral_ab = recursive_integrate(f, interval, method = 'trapeze', prec = 1e-9)

print(f"Integrating f(x) in {interval!s} yields (recursive trapeze):",
    integral_ab, sep = '\n', end = '\n\n')