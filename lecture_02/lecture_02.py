from package import \
    find_sols, \
    bisect_solve, \
    ask_continue


# EXERCISE 5: Find the roots of y(x) = (29.52/(x-0.12)) * e**(-0.686/x) - 11

print("""
EXERCISE 5: Find the roots of y(x) = (29.52/(x-0.12)) * e**(-0.686/x) - 11
""")

import numpy as np
import warnings
warnings.filterwarnings('ignore')

def f(x):  # given function
    return (29.52/(x-0.12)) * np.exp(-0.686/x) - 11

interval = [0.1, 2.2]
xmin, xmax = interval   # interval chosen by inspection
n = 4094  # number of subintervals

xlin = np.linspace(xmin, xmax, n+1)

sols = find_sols(f, xlin)

sol_points = []
for sol in sols:
    print("case: solution in {sol}".format(sol=sol))
    sol_point = bisect_solve(f, sol, 63)
    if sol_point is not None:
        sol_points.append(sol_point)
        print("solution: x = {sol}"
            .format(sol = sol_points[sol_points.index(sol_point)]))
        print("iterations: {iters} (bisection method)"
            .format(iters = 63), end = '\n\n')
    else:
        print("false solution: y = oo", end = '\n\n')


# plotting
print()
print("Plotting follows.")
ask_continue()

import matplotlib.pyplot as plt

plt.rc('text', usetex = True)
plt.rc('font', family = 'sans-serif')

plt.figure()

plt.title(r"$y(x) = \frac{29.52}{x-0.12}\:e^{\frac{-0.686}{x}} - 11$",
    fontdict = {'fontsize' : 16})

plt.plot(xlin, f(xlin), 'blue', zorder = 1)

plt.ylim(-5, 10)
plt.xlim(min(xlin)-0.12, max(xlin))
gsize = plt.ylim()[1] - plt.ylim()[0]

plt.hlines(0, min(xlin)-0.12, max(xlin), 'black', zorder = 0)

for sol in sol_points:
    # highlight the solution points
    plt.vlines(sol, f(sol)-gsize/20, f(sol)+gsize/20, color='red', zorder = 2)


plt.show()