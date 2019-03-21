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

print("Integral between {interval!s} for f(x): {result}" \
    .format(interval = interval, result = integral))
print("Error for the aboveshown integration: {error:.2e}" \
    .format(error = integral_err))
print()


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
Instead of calculating the values by raw power, it is more efficient
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
    # xp.append(x)
    # yp.append(y)
    # if i % int(np.sqrt(n)) == 0: # minimize number of arrays & points per array
    #     plt.scatter(xp, yp, marker = '.', s = 0.1, color = '#F84210')
    #     xp, yp = [], []

# plt.ylim(0, 1)
# plt.xlim(0, 1)
# plt.show()

# if r**2 is area of square and 4*pi*r**2 is area of circle, then pi is
# 4 times the ratio of points inside the circle
api = (inc/n)*4
print("Obtained Pi approximation: \u03A0 = {pi}".format(pi = api))
print("Area of circle: \u03A0r\u00B2 = {area:.4f}"
    .format(area = np.pi*1.5**2))
print("Volume of sphere: 4\u2153\u03A0r\u00B3 = {volume:.4f}"
    .format(volume = 4/3*np.pi*1.5**3))
print()


EXERCISE_23 = """\
Make a program that is able to compute the center of mass of the figure,
(<figure>) supposed homogeneous, using the Monte Carlo method.\
"""

redact_ex(EXERCISE_23, 23)


# plt.figure(figsize = (8, 6))

npoints = 1e6
n = int(npoints)

l, h = 8, 6 # rectangle of width 8 and height 6
# empty circle is located at (6, 0) and has radius of 2
xc, yc, rc = 6, 0, 2

xv, yv = 0, 0
xerr, yerr = 0, 0
# xp, yp = [], []
inc = 0
for i in range(n):
    x, y = random.uniform(0, l), random.uniform(0, h)

    if (x-xc)**2 + (y-yc)**2 <= rc**2:
        continue

    inc += 1
    xv += x
    yv += y
    xerr += x**2
    yerr += y**2
    # xp.append(x)
    # yp.append(y)
    # if i % int(np.sqrt(n)) == 0:
    #     plt.scatter(xp, yp, marker = '.', s = 0.1, )
    #     xp, yp = [], []

# plt.ylim(0, 6)
# plt.xlim(0, 8)
# plt.show()

# xg = xv/inc
# yg = yv/inc
# or

v = n/inc

xmf = xv/n; xmf2 = xerr/n
ymf = yv/n; ymf2 = yerr/n

xg = v*xmf
yg = v*ymf

xgerr = v*np.sqrt((xmf2-xmf**2)/n)
ygerr = v*np.sqrt((ymf2-ymf**2)/n)

print("Obtained coordinates for center of mass (x, y):",
    "({:.6f} \u00B1 {:.6f}, {:.6f} \u00B1 {:.6f})"
    .format(xg, xgerr, yg, ygerr), sep = '\n', end = '\n\n')


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