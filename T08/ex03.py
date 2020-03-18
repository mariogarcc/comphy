from package import redact_ex

from package import solve_explicit_ode

import numpy as np


EXERCISE_03 = """\
Make a program that is able to graphically solve the previous equation
using the following scheme (and appropriate boundary conditions):
(T_j^(n+1) - T_j^n)/\u0394t - \u03B1/\u0394x\u00B2(- 1/12 T_(j-2)^n + 4/3 T_(j-1)^n - 2.5 T_j^n + 4/3 T_(j+1)^n - 1/12 T_(j+2)^n) = 0\
"""

redact_ex(EXERCISE_03, 3)


slices = 20
itern = 1000
plot_frequency = 0.05

deltat = 1e-3
deltax = 1e-1

alpha =  1

s = alpha*deltat/deltax**2


def ftc5s(ngr, grid, s = s):

    slices = len(grid[0])-1

    for vl in range(2, slices-1):
        ngr[vl] = \
            grid[0][vl] + s*( \
                - (1/12)*grid[0][vl-2] - (1/12)*grid[0][vl+2] \
                + (4/3) *grid[0][vl-1] + (4/3) *grid[0][vl+1] \
                - (5/2) *grid[0][vl] )

    return ngr

# this scheme needs additional boundary conditions due to its
# 5-space-neighbour nature

tprev = np.zeros(slices+1)
tprev[8:12] = 5

initial_conditions = [tprev]

def boundary_conditions(lap, ngr, grid, deltat = deltat):

    slices = len(grid[0])-1

    ngr[1] = ngr[2]
    ngr[slices-1] = ngr[slices-2]

    ngr[0] = ngr[1]
    ngr[slices] = ngr[slices-1]

    egrid = [ngr] + [r for r in grid]

    return egrid


print("Computing...", end='\n\n')
solve_explicit_ode(ftc5s, initial_conditions, boundary_conditions,
    slices, itern, plot_frequency)
