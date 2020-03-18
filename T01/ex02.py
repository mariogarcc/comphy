from package import redact_ex, ask_continue

from package import \
    find_sols, \
    bisect_solve

import numpy as np


EXERCISE_02 = """\
Given an interval where a function ( f(x) = x**2 - 3*x + np.exp(x) - 2 )
has a single root, extrapolate a more precise solution using
the bisection method.\
"""

redact_ex(EXERCISE_02, 2)


####################################

def f(x):
    return x**2 - 3*x + np.exp(x) - 2

interval = [-2, 4]
xmin, xmax = interval
n = 20
xarr = np.linspace(xmin, xmax, n+1)

sols = find_sols(f, xarr)
try:
    assert len(sols) > 0
except(AssertionError, TypeError):
    print("There are no solutions for f(x) in the given interval.")
print("There {} in: "
    .format("is a solution" if len(sols) == 1 else "are solutions"),
    *sols, sep = '\n', end = '\n\n')

######## ^ Copied from ex01 ########

print("Bisection method", end = '\n\n')
bisect_iters = 63
bisect_sol_points = []
for sol in sols:
    print(f"case: solution in {sol}")
    bisect_sol_points.append(bisect_solve(f, sol, iters = bisect_iters))
    print(f"solution: x = {bisect_sol_points[sols.index(sol)]}")
    print(f"iterations: {bisect_iters}", end = '\n\n')

# plotting
print("Plotting follows.")
ask_continue()

import matplotlib.pyplot as plt

xlin = np.linspace(xmin, xmax, 1000)

plt.rc('text', usetex = True)
plt.rc('font', family = 'serif')

plt.figure(figsize = (9, 6))
plt.suptitle(r"$y(x) = x^2 - 3x + e^x - 2$", fontsize = 16)
plt.title(r"Bisection method", y = 1.03)

plt.plot(xlin, f(xlin), 'blue')

plt.xlim(-1.5, 2.5)
plt.ylim(-5, 10)
gsize = max(f(xlin)) - min(f(xlin))  # plot vertical size

plt.hlines(0, min(xlin), max(xlin), 'black')

# highlight the solution points
for sol in bisect_sol_points:
    plt.vlines(sol, f(sol)-gsize/20, f(sol)+gsize/20, color = 'red')
    plt.text(sol, f(sol)+gsize/16, f'x = {sol:.5f}',
        horizontalalignment = 'center')

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()