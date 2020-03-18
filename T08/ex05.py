from package import redact_ex

from package import solve_implicit_ode

import numpy as np


EXERCISE_05 = """\
Make a program that is able to graphically solve the previous equation
using the fully implicit FTCS scheme.\
"""

redact_ex(EXERCISE_05, 5)


slices = 20
itern = 1000
plot_frequency = 0.05

deltat = 1e-3
deltax = 1e-1

alpha =  1

s = alpha*deltat/deltax**2


amat = np.diag([1]+[1+2*s]*(slices-1)+[1])         \
     + np.diag([0]+[   -s]*(slices-1)+[ ], k = 1)  \
     + np.diag([ ]+[   -s]*(slices-1)+[0], k = -1)

iamat = np.linalg.inv(amat)

iden = np.identity(len(amat))


def iftcs_boundary_conditions(lap, ciarr):

    slices = len(ciarr)-1

    ciarr[0] = 0; ciarr[slices] = 10

    return ciarr


tprev = np.zeros(slices+1); tpprev = np.zeros(slices+1)
tprev[0] = 0; tpprev[0] = 0
tprev[slices] = 10; tpprev[slices] = 10

initial_conditions = [tprev, tpprev]


print("Computing...", end='\n\n')
solve_implicit_ode(iamat, iden, initial_conditions, iftcs_boundary_conditions,
    slices, itern, plot_frequency)
