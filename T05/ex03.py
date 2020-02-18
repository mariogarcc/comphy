from package import *
import random
import numpy as np

EXERCISE_23 = """\
Make a program that is able to compute the center of mass of the figure,
(<figure>) assumed homogeneous, using the Monte Carlo method.\
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
    f"({xg:.6f} \u00B1 {xgerr:.6f}, {yg:.6f} \u00B1 {ygerr:.6f})",
    sep = '\n', end = '\n\n')