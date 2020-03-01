from package import redact_ex

from package import find_sols

import numpy as np


EXERCISE_01 = """\
Given the function f(x) = x**2 - 3*x + e**x - 2 = 0 , 
analyze the existence of roots in the interval [-2, 4] 
(by dividing [-2, 4] in 20 subintervals and sign-checking)\
"""

redact_ex(EXERCISE_01, 1)


def f(x):
    return x**2 - 3*x + np.exp(x) - 2

interval = [-2, 4]
xmin, xmax = interval
n = 20 # number of subintervals
xarr = np.linspace(xmin, xmax, n+1)

sols = find_sols(f, xarr)
try:
    assert len(sols) > 0
except(AssertionError, TypeError):
    print("There are no solutions for f(x) in the given interval.")
print("There {} in: "
    .format("is a solution" if len(sols) == 1 else "are solutions"),
    *sols, sep = '\n', end = '\n\n')