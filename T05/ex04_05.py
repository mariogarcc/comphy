from package import redact_ex

from package import montecarlo_integrate

import numpy as np


EXERCISE_21 = """\
Make a program that computes the area of a circle of radius 1.5 units
using the Monte Carlo method.\
"""

redact_ex(EXERCISE_21, 21)


EXERCISE_22 = """\
Make a program that computes the volume of a sphere of radius 1.5 units
using the Monte Carlo method.\
"""

redact_ex(EXERCISE_22, 22)


print("""
Instead of calculating the values by raw simulation, it is more efficient
and accurate to compute the value of Pi and use it to calculate the desired
unknowns.
""")

import random
# import matplotlib.pyplot as plt

# plt.figure(figsize=(6,6))

npoints = 1e6
n = int(npoints)

o, l, r = [0, 1, 0.5] # checking for a unit radius circle inside a square
x0 = y0 = r

# xp, yp = [], []
inc = 0
for i in range(1, n+1):
    y = random.uniform(o, l)
    x = i/n
    try:
        d = (x-x0)**2+(y-x0)**2
    except OverflowError: # for some reason it sometimes produces numbers +e294
        continue
    if d > r**2 and i != n:
        continue
    inc += 1 # point is in circle
#     xp.append(x)
#     yp.append(y)
#     if i % int(np.sqrt(n)) == 0: # minimize number of arrays & points per array
#         plt.scatter(xp, yp, marker = '.', s = 0.1, color = '#F84210')
#         xp, yp = [], []

# plt.ylim(0, 1)
# plt.xlim(0, 1)
# plt.show()

# if r**2 is area of square and 4*pi*r**2 is area of circle, then pi is
# 4 times the ratio of points inside the circle
api = (inc/n)*4
print(f"Obtained Pi approximation: \u03A0 = {api}")
print("Area of circle: \u03A0r\u00B2 = {area:.4f}"
    .format(area = np.pi*1.5**2))
print("Volume of sphere: 4\u2153\u03A0r\u00B3 = {volume:.4f}"
    .format(volume = 4/3*np.pi*1.5**3))