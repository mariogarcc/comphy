from package import redact_ex

from package import \
    simpson_integrate, \
    recursive_integrate, \
    romberg_integrate


EXERCISE_14 = """\
Make a program that computes the integral of a function f(x)
in an interval [a, b] using the rule of Simpson 1/3.
Apply that to the case f(x) = x**3 - 3*x**2 - x + 3 and a = 0, b = 1.35\
"""

redact_ex(EXERCISE_14, 14)


import numpy as np

def f(x):
    return x**3 - 3*x**2 - x + 3

interval = [0, 1.35]

integral_ab = simpson_integrate(f, interval, method = '1/3', npoints = 1e5)

print(f"Integrating f(x) in {interval!s} yields (Simpson 1/3):",
    integral_ab, sep = '\n', end = '\n\n')


EXERCISE_15 = """\
Make a program that computes the integral of a function f(x)
in an interval [a, b] using the rule of Simpson 3/8.
Apply that to the case f(x) = x**3 - 3*x**2 - x + 3 and a = 0, b = 1.35\
"""

redact_ex(EXERCISE_15, 15)


integral_ab = simpson_integrate(f, interval, method = '3/8', npoints = 1e5)

print(f"Integrating f(x) in {interval!s} yields (Simpson 3/8):",
    integral_ab, sep = '\n', end = '\n\n')


EXERCISE_16 = """\
Make a program that computes the integral of a function f(x)
in an interval [a, b] using the rule of the recursive trapeze.
Apply that to the case f(x) = (x**2 + x + 1) * cos(x) and a = 0, b = pi/2\
"""

redact_ex(EXERCISE_16, 16)


def f(x):
    return (x**2 + x + 1) * np.cos(x)

interval = [0, np.pi/2]


integral_ab = recursive_integrate(f, interval, method = 'trapeze', prec = 1e-12)

print(f"Integrating f(x) in {interval!s} yields (recursive trapeze):",
    integral_ab, sep = '\n', end = '\n\n')


EXERCISE_17 = """\
Make a program that computes the integral of a function f(x)
in an interval [a, b] using the recursive rule of Simpson 1/3.
Apply that to the case f(x) = (x**2 + x + 1) * cos(x) and a = 0, b = pi/2\
"""

redact_ex(EXERCISE_17, 17)


integral_ab = recursive_integrate(f, interval, method = 'simpson', prec = 1e-12)

print(f"Integrating f(x) in {interval!s} yields (recursive Simpson 1/3):",
    integral_ab, sep = '\n')


EXERCISE_18 = """\
Make a program that computes the integral of a function f(x)
in an interval [a, b] using the Romberg's rule for integration.
Apply that to the case f(x) = (x**2 + x + 1) * cos(x) and a = 0, b = pi/2\
"""

redact_ex(EXERCISE_18, 18)


integral_ab = romberg_integrate(f, interval, prec = 1e-12)

print(f"Integrating f(x) in {interval!s} yields (Romberg):",
    integral_ab, sep = '\n')