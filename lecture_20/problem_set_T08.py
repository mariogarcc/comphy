# Author: Mario García Cajade
# Date: 21/03/2019

# Problem set for topic 07: ordinary differential equations


# --------------------------Packages-------------------------- #

import numpy as np
import matplotlib.pyplot as plt
import _tkinter
TclError = _tkinter.TclError

# ------------------------------------------------------------ #

# --------------------Function definitions-------------------- #

def ask_continue():
    response = input("Continue? (y/n)\n")
    if response.lower() not in ('y', 'n'):
        return ask_continue()
    if response.lower() == 'n':
        return quit()





def redact_ex(ex_str, n = '', sep = '\n', end = '\n\n'):
    print('', 'EXERCISE {no:d}:'.format(
        no = int(n) if not isinstance(n, str) else n), ex_str,
        sep = sep, end = end)
    return None





def solve_explicit_ode(
        constructor,
        initial_conditions, boundary_conditions,
        slices, itern, plot_frequency = 1):
    
    grid = initial_conditions
    next_grid_row = initial_conditions[0]

    for lap in range(itern):

        next_grid_row = constructor(next_grid_row, grid)
        next_grid_row, *grid = boundary_conditions(lap, next_grid_row, grid)

        grid = grid[1:] + [next_grid_row]

        if lap == 2: quit()

        if lap % int(1/plot_frequency) == 0:
            try:
                plt.figure(1)
                plt.plot(grid[0])
                plt.pause(0.1)
                plt.show
            except TclError: # catches error by closing tab manually
                return

    input("press ENTER to continue\n")
    plt.close
    return None





def solve_implicit_ode(
        constructor_mat, constructor_helper_mat,
        initial_conditions, boundary_conditions,
        slices, itern, plot_frequency = 1):
    
    grid = initial_conditions
    next_grid_row = initial_conditions[0]

    for lap in range(itern):

        next_grid_row = constructor_mat @ (constructor_helper_mat @ grid[0])
        next_grid_row, *grid = boundary_conditions(lap, next_grid_row, grid)

        grid = grid[1:] + [next_grid_row]

        if lap % int(1/plot_frequency) == 0:
            try:
                plt.figure(1)
                plt.plot(grid[0])
                plt.pause(0.1)
                plt.show
            except TclError:
                return

    input("press ENTER to continue\n")
    plt.close
    return None

# ------------------------------------------------------------ #
print()
# ----------------------- Problem no.1 ----------------------- #

print(f"Exercise {1} follows.")
# ask_continue()

EXERCISE_1 = """\
Make a program that is able to graphically solve the equation
\u2202T/\u2202t = \u03B1 \u2202\u00B2T/\u2202x\u00B2 = 0 using the Forward in Time, Centered in Space (FTCS)
scheme with Dirichlet boundary conditions u_0 = 0 and u_L = 10.
+ Consider different initial conditions.
+ Consider a new boundary condition: u_L = sin(t/2)
+ Consider null flux boundary conditions.\
"""

redact_ex(EXERCISE_1, 1)


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
tprev = tpprev = np.zeros(slices+1)
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
# solve_explicit_ode(ftcs, initial_conditions, boundary_conditions,
#     slices, itern, plot_frequency)


otprev = otpprev = np.zeros(slices+1)
otprev[8:12] = 5; otpprev[8:12] = 5
otprev[0] = 0; otpprev[0] = 0
otprev[slices] = 10; otpprev[slices] = 10

oinitial_conditions = [otprev, otpprev]

print("+ Computing...", end='\n\n')
# solve_explicit_ode(ftcs, oinitial_conditions, boundary_conditions,
#     slices, itern, plot_frequency)


deltat = 1e-2
def oboundary_conditions(lap, ngr, grid, deltat = deltat):

    slices = len(grid[0])-1

    ngr[0] = 0
    ngr[slices] = 10 * np.sin((lap+1)*deltat/2)

    egrid = [ngr] + [r for r in grid]

    return egrid

print("+ Computing...", end='\n\n')
# solve_explicit_ode(ftcs, initial_conditions, oboundary_conditions,
#     slices, itern, plot_frequency)
deltat = 1e-3


def oboundary_conditions(lap, ngr, grid, deltat = deltat):

    slices = len(grid[0])-1

    ngr[0] = ngr[1]
    ngr[slices] = ngr[slices-1]

    egrid = [ngr] + [r for r in grid]

    return egrid

print("+ Computing...", end='\n\n')
# solve_explicit_ode(ftcs, oinitial_conditions, oboundary_conditions,
#     slices, itern, plot_frequency)

# ------------------------------------------------------------ #

# ----------------------- Problem no.2 ----------------------- #

print(f"Exercise {2} follows.")
# ask_continue()

EXERCISE_2 = """\
Make a program that is able to graphically solve the previous equation
using the following scheme:
(0.5 T_j^(n-1) - 2 T_j^n + 1.5 T_j^(n+1))/\u0394t - \u03B1((T_(j-1)^n - 2 T_j^n + T_(j-1)^n)/\u0394x\u00B2) = 0\
"""

redact_ex(EXERCISE_2, 2)


def c3tcs(ngr, grid, s = s):

    slices = len(grid[0])-1

    for vl in range(1, slices):
        ngr[vl] = \
            (s*(1.0*grid[0][vl+1] - 2.0*grid[0][vl] + grid[0][vl-1]) \
        +     2.0*grid[0][vl]   - 0.5*grid[1][vl])  / 1.5
    
    return ngr


print("Computing...", end='\n\n')
# solve_explicit_ode(c3tcs, initial_conditions, boundary_conditions,
#     slices, itern, plot_frequency)

# ------------------------------------------------------------ #

# ----------------------- Problem no.3 ----------------------- #

print(f"Exercise {3} follows.")
# ask_continue()

EXERCISE_3 = """\
Make a program that is able to graphically solve the previous equation
using the following scheme (and appropriate boundary conditions):
(T_j^(n+1) - T_j^n)/\u0394t - \u03B1/\u0394x\u00B2(- 1/12 T_(j-2)^n + 4/3 T_(j-1)^n - 2.5 T_j^n + 4/3 T_(j+1)^n - 1/12 T_(j+2)^n) = 0\
"""

redact_ex(EXERCISE_3, 3)


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

otprev = np.zeros(slices+1)
otprev[8:12] = 5
otprev[0] = 0
otprev[slices] = 10

oinitial_conditions = [otprev]

def oboundary_conditions(lap, ngr, grid, deltat = deltat):

    slices = len(grid[0])-1

    # ngr[0] = ngr[1]
    # ngr[slices] = ngr[slices-1]

    # ngr[0] = 0
    # ngr[slices] = 10

    egrid = [ngr] + [r for r in grid]

    return egrid


print("Computing...", end='\n\n')
solve_explicit_ode(ftc5s, oinitial_conditions, oboundary_conditions,
    slices, itern, plot_frequency)

# ------------------------------------------------------------ #

# ----------------------- Problem no.4 ----------------------- #

print(f"Exercise {4} follows.")
# ask_continue()

EXERCISE_4 = """\
Make a program that is able to graphically solve the previous equation
using the Dufort-Frankel scheme.\
"""

redact_ex(EXERCISE_4, 4)


def dufort_frankel(ngr, grid, s = s):

    slices = len(grid[0])-1

    for vl in range(1, slices):
        ngr[vl] = \
            2*s/(1+2*s) * (grid[0][vl-1] + grid[0][vl+1]) + (1-2*s)/(1+2*s) * grid[1][vl]
    
    return ngr


print("Computing...", end='\n\n')
# solve_explicit_ode(ftcs, initial_conditions, boundary_conditions,
#     slices, itern, plot_frequency)

# ------------------------------------------------------------ #

# ----------------------- Problem no.5 ----------------------- #

print(f"Exercise {5} follows.")
# ask_continue()

EXERCISE_5 = """\
Make a program that is able to graphically solve the previous equation
using the fully implicit FTCS scheme.\
"""

redact_ex(EXERCISE_5, 5)


amat = np.diag([1]+[1+2*s]*(slices-1)+[1])         \
     + np.diag([0]+[   -s]*(slices-1)+[ ], k = 1)  \
     + np.diag([ ]+[   -s]*(slices-1)+[0], k = -1)

iamat = np.linalg.inv(amat)

iden = np.identity(len(amat))

print("Computing...", end='\n\n')
# solve_implicit_ode(iamat, iden, initial_conditions, boundary_conditions,
#     slices, itern, plot_frequency)

# ------------------------------------------------------------ #

# ----------------------- Problem no.6 ----------------------- #

print(f"Exercise {6} follows.")
# ask_continue()

EXERCISE_6 = """\
Make a program that is able to graphically solve the previous equation
using the Crank-Nicolson scheme.\
"""

redact_ex(EXERCISE_6, 6)


amat = np.diag([1]+[ 1+s]*(slices-1)+[1])         \
     + np.diag([0]+[-s/2]*(slices-1)+[ ], k = 1)  \
     + np.diag([ ]+[-s/2]*(slices-1)+[0], k = -1)

iamat = np.linalg.inv(amat)

a = 0; b = 10
bmat = np.diag([a]+[ 1-s]*(slices-1)+[b])         \
     + np.diag([0]+[ s/2]*(slices-1)+[ ], k = 1)  \
     + np.diag([ ]+[ s/2]*(slices-1)+[0], k = -1)

print("Computing...", end='\n\n')
# solve_implicit_ode(iamat, bmat, initial_conditions, boundary_conditions,
#     slices, itern, plot_frequency)

# ------------------------------------------------------------ #

# ------------------------- Comments ------------------------- #

"""
"""

# ------------------------------------------------------------ #



# Released under CC0