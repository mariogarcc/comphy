from package import redact_ex

from package import solve_explicit_ode

import numpy as np


EXERCISE_01 = """\
Make a program that is able to graphically solve the equation
\u2202T/\u2202t = \u03B1 \u2202\u00B2T/\u2202x\u00B2 = 0 using the Forward in Time, Centered in Space (FTCS)
scheme with Dirichlet boundary conditions u_0 = 0 and u_L = 10.
+ Consider different initial conditions.
+ Consider a new boundary condition: u_L = sin(t/2)
+ Consider null flux boundary conditions.\
"""

redact_ex(EXERCISE_01, 1)


# computation parameters
slices = 20
itern = 1000
plot_frequency = 0.05

# differentiation parameters
deltat = 1e-3
deltax = 1e-1

# problem parameters
alpha =  1

# helper variable
s = alpha*deltat/deltax**2

# grid creation and initial conditions
tprev = np.zeros(slices+1); tpprev = np.zeros(slices+1)
tprev[0] = 0; tpprev[0] = 0
tprev[slices] = 10; tpprev[slices] = 10

initial_conditions = [tprev, tpprev]

# boundary conditions
def boundary_conditions(lap, ngr, grid):

    slices = len(grid[0])-1

    ngr[0] = 0
    ngr[slices] = 10

    egrid = [ngr] + [r for r in grid]

    return egrid

# differentiation scheme
def ftcs(ngr, grid, s = s):

    slices = len(grid[0])-1

    for vl in range(1, slices):
        ngr[vl] = \
            grid[0][vl] + s*(grid[0][vl+1] - 2*grid[0][vl] + grid[0][vl-1])

    return ngr


print("Computing...", end='\n\n')
solve_explicit_ode(ftcs, initial_conditions, boundary_conditions,
    slices, itern, plot_frequency)


otprev = otpprev = np.zeros(slices+1)
otprev[8:12] = 5; otpprev[8:12] = 5
otprev[0] = 0; otpprev[0] = 0
otprev[slices] = 10; otpprev[slices] = 10

oinitial_conditions = [otprev, otpprev]

print("+ Computing...", end='\n\n')
solve_explicit_ode(ftcs, oinitial_conditions, boundary_conditions,
    slices, itern, plot_frequency)


deltat = 1e-2
def oboundary_conditions(lap, ngr, grid, deltat = deltat):

    slices = len(grid[0])-1

    ngr[0] = 0
    ngr[slices] = 10 * abs(np.cos((lap+1)*deltat/2))

    egrid = [ngr] + [r for r in grid]

    return egrid

# need to re-create the initial_conditions arrays
tprev = np.zeros(slices+1); tpprev = np.zeros(slices+1)
tprev[0] = 0; tpprev[0] = 0
tprev[slices] = 10; tpprev[slices] = 10

initial_conditions = [tprev, tpprev]


print("+ Computing...", end='\n\n')
solve_explicit_ode(ftcs, initial_conditions, oboundary_conditions,
    slices, itern, plot_frequency)
deltat = 1e-3


def oboundary_conditions(lap, ngr, grid, deltat = deltat):

    slices = len(grid[0])-1

    ngr[0] = ngr[1]
    ngr[slices] = ngr[slices-1]

    egrid = [ngr] + [r for r in grid]

    return egrid

otprev = otpprev = np.zeros(slices+1)
otprev[8:12] = 5; otpprev[8:12] = 5
otprev[0] = 0; otpprev[0] = 0

oinitial_conditions = [otprev, otpprev]


print("+ Computing...", end='\n\n')
solve_explicit_ode(ftcs, oinitial_conditions, oboundary_conditions,
    slices, itern, plot_frequency)
