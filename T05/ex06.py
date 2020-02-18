from package import redact_ex

import numpy as np
import random

EXERCISE_24 = """\
Make a program that computes the volume of the part of a torus shown
in the figure (<figure>) using the Monte Carlo method.\
"""

redact_ex(EXERCISE_24, 24)


a, b = 1, 3

npoints = 1e6
n = int(npoints)

inc = 0
for i in range(n):
    x, y, z = random.uniform(1, 4), random.uniform(-3, 4), random.uniform(-1, 1)
    if (np.sqrt(x**2 + y**2) - b)**2 + z**2 <= a**2:
        inc += 1

area = 3*7*2
volume = inc*area/n

print("Obtained volume:", volume, sep = '\n', end = '\n\n')