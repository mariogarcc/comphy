from package import \
    *
# from package import redact_ex

# from package import dkf

EXERCISE_01 = """\
Make a program that is able to compute the numerical k-order derivative
of a given function using the method of undetermined coefficients.
Apply that to the case f(x) = x**3 - 3*x**2 - x + 3 on x0 = 1.2.\
"""

redact_ex(EXERCISE_01, 1)


import numpy as np

def f(x):
    return x**3 - 3*x**2 - x + 3
# df = 3*x**2 - 6*x - 1, on x0 (1.2) = -3.88
# d2f = 6*x - 6, on x0 (1.2) = 1.2
# d3f = 6, on x0 (1.2) = 6

for k in range(1, 6):
    for h in [1/d for d in [10**n for n in range(10)]]:
        v = dkf(f, 1.2, k, delta = h)
        print('f({k}({x0}) = {v} (h = {h})'
            .format(k = k, x0 = 1.2, v = v, h = h), end = '\n\n')

# print(dkf(f, 1.2, 1, delta = 1e-6))
# print(dkf(f, 1.2, 2, delta = 1e-4))
# print(dkf(f, 1.2, 3, delta = 1e-2))