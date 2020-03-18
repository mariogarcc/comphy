from package import redact_ex

from package import solve_explicit_ode

import numpy as np


EXERCISE_04 = """\
Make a program that is able to graphically solve the previous equation
using the Dufort-Frankel scheme.\
"""

redact_ex(EXERCISE_04, 4)


slices = 20
itern = 1000
plot_frequency = 0.05

deltat = 1e-3
deltax = 1e-1

alpha =  1

s = alpha*deltat/deltax**2


def dufort_frankel(ngr, grid, s = s):

    slices = len(grid[0])-1

    for vl in range(1, slices):
        ngr[vl] = \
            2*s/(1+2*s) * (grid[0][vl-1] + grid[0][vl+1]) + (1-2*s)/(1+2*s) * grid[1][vl]

    return ngr


tprev = np.zeros(slices+1); tpprev = np.zeros(slices+1)
tprev[0] = 0; tpprev[0] = 0
tprev[slices] = 10; tpprev[slices] = 10

initial_conditions = [tprev, tpprev]

def boundary_conditions(lap, ngr, grid):

    slices = len(grid[0])-1

    ngr[0] = 0
    ngr[slices] = 10

    egrid = [ngr] + [r for r in grid]

    return egrid


print("Computing...", end='\n\n')
solve_explicit_ode(dufort_frankel, initial_conditions, boundary_conditions,
    slices, itern, plot_frequency)
