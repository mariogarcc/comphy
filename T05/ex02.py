from package import redact_ex

from package import montecarlo_integrate


EXERCISE_20 = """\
Make a program that is able to compute the integral between 0 and infinity
for f(x) = e**(-x)\
"""

redact_ex(EXERCISE_20, 20)


import numpy as np

def f(y):
    return (1/y**2) * np.exp(-1/y+1)

interval = [0, 1]

integral, integral_err = montecarlo_integrate(f, interval)

print(f"Integral between {interval!s} for f(x): {integral}")
print(f"Error for the aboveshown integration: {integral_err:.2e}")