from package import redact_ex

from package import \
    find_sols, \
    bisect_solve, \
    falsi_solve, \
    newt_raph_solve, \
    ask_continue


EXERCISE_1 = """\
Given the function f(x) = x**2 - 3*x + e**x - 2 = 0 , 
analyze the existence of roots in the interval [-2, 4] 
(by dividing [-2, 4] in 20 subintervals and sign-checking)\
"""

redact_ex(EXERCISE_1, 1)


import numpy as np

def f(x): # given function
    return x**2 - 3*x + np.exp(x) - 2

interval = [-2, 4] # interval
xmin, xmax = interval
n = 20 # number of subintervals

xarr = np.linspace(xmin, xmax, n+1)
xlin = np.linspace(xmin, xmax, 1000)

sols = find_sols(f, xarr)
try:
    assert len(sols) > 0
except(AssertionError, TypeError):
    print("There are no solutions for f(x) in the given interval.")
print("There {} in: "
    .format("is a solution" if len(sols) == 1 else "are solutions"),
    *sols, sep = '\n', end = '\n\n')


EXERCISE_2 = """\
Given an interval where a function has a single root, 
extrapolate a more precise solution using the bisection method.\
"""

redact_ex(EXERCISE_2, 2)


print("Bisection method", end = '\n\n')
bisect_iters = 63
bisect_sol_points = []
for sol in sols:
    print("case: solution in {sol}".format(sol = sol))
    bisect_sol_points.append(bisect_solve(f, sol, iters = bisect_iters))
    print("solution: x = {sol}"
        .format(sol = bisect_sol_points[sols.index(sol)]))
    print("iterations: {iters}".format(iters = bisect_iters), end = '\n\n')


EXERCISE_3 = """\
Calculate the solutions for f(x) using the Regula Falsi method.\
"""

redact_ex(EXERCISE_3, 3)

print("Regula Falsi method", end = '\n\n')
falsi_iters = 63
falsi_sol_points = []
for sol in sols:
    print("case: solution in {sol}".format(sol=sol))
    falsi_sol_points.append(falsi_solve(f, sol, iters = falsi_iters))
    print("solution: x = {sol}"
        .format(sol = falsi_sol_points[sols.index(sol)]))
    print("iterations: {iters}".format(iters = falsi_iters), end = '\n\n')


EXERCISE_4 = """\
Calculate the roots for f(x) using the Newton-Raphson method.\
"""\

redact_ex(EXERCISE_4, 4)

def df(x):
    return 2*x + np.exp(x) - 3
# derivative of function f(x)

print(
    "Newton-Raphson method",
    "using Regula Falsi for an approximate solution",
    sep = '\n', end = '\n\n'
)

falsi_asols = []
falsi_aiters = 7
for sol in sols:
    print("case: solution in {sol}".format(sol=sol))
    falsi_asols.append(falsi_solve(f, sol, iters = falsi_aiters))
    print("approximated solution: x = {asol}"
        .format(asol = falsi_asols[sols.index(sol)]))
    print("iterations: {iters} (regula falsi)"
        .format(iters = falsi_aiters), end = '\n\n')

newt_raph_solve_points = []
newt_raph_iters = 15
for falsi_asol in falsi_asols:
    print("case: approximated solution x = {asol}".format(asol=falsi_asol))
    newt_raph_solve_points.append(newt_raph_solve(f, df, falsi_asol,
        newt_raph_iters))
    print("newton-raphson solution: x = {nrsol}"
        .format(nrsol = newt_raph_solve_points[falsi_asols.index(falsi_asol)]))
    print("iterations: {iters}".format(iters = newt_raph_iters), end = '\n\n')


# plotting 
print() 
print("Plotting follows.")
ask_continue()

import matplotlib.pyplot as plt

plt.rc('text', usetex = True)
plt.rc('font', family = 'serif')

plt.figure(figsize = (9, 6))

plt.suptitle(r"$y(x) = x^2 - 3x + e^x - 2$", fontsize = 16)

plt.subplot(311)

plt.title(r"Bisection", y = 1.03)

plt.plot(xlin, f(xlin), 'blue')

plt.xlim(-1.5, 2.5)
plt.ylim(-5, 10)
gsize = max(f(xlin)) - min(f(xlin))  # plot vertical size

plt.hlines(0, min(xlin), max(xlin), 'black')

for sol in bisect_sol_points:
    # highlight the solution points
    plt.vlines(sol, f(sol)-gsize/20, f(sol)+gsize/20, color = 'red')
    plt.text(sol, f(sol)+gsize/16, 'x = {x:.5f}'.format(x = sol),
        horizontalalignment = 'center')


plt.subplot(312)

plt.title(r"Regula Falsi", y = 1.03)

plt.plot(xlin, f(xlin), 'blue')

plt.xlim(-1.5, 2.5)
plt.ylim(-5, 10)
gsize = max(f(xlin)) - min(f(xlin))  # plot vertical size

plt.hlines(0, min(xlin), max(xlin), 'black')

for sol in falsi_sol_points:
    # highlight the solution points
    plt.vlines(sol, f(sol)-gsize/20, f(sol)+gsize/20, color='red')
    plt.text(sol, f(sol)+gsize/16, 'x = {x:.5f}'.format(x = sol),
        horizontalalignment = 'center')


plt.subplot(313)

plt.title(r"Newton-Raphson", y = 1.03)

plt.plot(xlin, f(xlin), 'blue')

plt.xlim(-1.5, 2.5)
plt.ylim(-5, 10)
gsize = max(f(xlin)) - min(f(xlin))  # plot vertical size

plt.hlines(0, min(xlin), max(xlin), 'black')

for sol in newt_raph_solve_points:
    # highlight the solution points
    plt.vlines(sol, f(sol)-gsize/20, f(sol)+gsize/20, color='red')
    plt.text(sol, f(sol)+gsize/16, 'x = {x:.5f}'.format(x = sol),
        horizontalalignment = 'center')

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
