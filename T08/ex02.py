from package import redact_ex

from package import solve_explicit_ode

import numpy as np


EXERCISE_02 = """\
Make a program that is able to graphically solve the previous equation
using the following scheme:
(0.5 T_j^(n-1) - 2 T_j^n + 1.5 T_j^(n+1))/\u0394t - \u03B1((T_(j-1)^n - 2 T_j^n + T_(j-1)^n)/\u0394x\u00B2) = 0\
"""

redact_ex(EXERCISE_02, 2)


slices = 20
itern = 1000
plot_frequency = 0.05

deltat = 1e-3
deltax = 1e-1

alpha =  1

s = alpha*deltat/deltax**2


def c3tcs(ngr, grid, s = s):

    slices = len(grid[0])-1

    for vl in range(1, slices):
        ngr[vl] = \
            (s*(1.0*grid[0][vl+1] - 2.0*grid[0][vl] + grid[0][vl-1]) \
        +     2.0*grid[0][vl]   - 0.5*grid[1][vl])  / 1.5
    
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
solve_explicit_ode(c3tcs, initial_conditions, boundary_conditions,
    slices, itern, plot_frequency)
