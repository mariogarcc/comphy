from package import *

# EXERCISE: Find the roots of y(x) = (29.52/(x-0.12)) * e**(-0.686/x) - 11
print("""
EXERCISE: Find the roots of y(x) = (29.52/(x-0.12)) * e**(-0.686/x) - 11
""")

import numpy as np

def f(x):  # given function
    return (29.52/(x-0.12)) * np.exp(-0.686/x) - 11

xmin, xmax = 0.1, 2.2   # interval chosen by inspection
n = 4094  # number of subintervals

xarr = np.linspace(xmin, xmax, n+1)
xlin = np.linspace(xmin, xmax, 4095)

sols = find_sols(f, xarr)

sol_points = []
for sol in sols:
    print("case: solution in {sol}".format(sol=sol))
    sol_point = bisect_solve(f, sol, 63)
    if sol_point is not None:
        sol_points.append(sol_point)
    print("")


# plotting
print("Plotting follows.")
ask_continue()

import matplotlib.pyplot as plt

plt.rc('text', usetex = True)
plt.rc('font', family = 'sans-serif')
plt.title(r'$y(x) = \frac{29.52}{x-0.12}\:e^{\frac{-0.686}{x}} - 11$',
    fontdict = {'fontsize' : 16})

plt.plot(xlin, f(xlin), 'black')
gsize = max(f(xlin)) - min(f(xlin))  # plot vertical size

plt.hlines(0, min(xlin), max(xlin), 'green')

plt.ylim(-5, 10)
gsize = plt.ylim()[1] - plt.ylim()[0]

for sol in sol_points:
    # highlight the solution points
    plt.vlines(sol, f(sol)-gsize/20, f(sol)+gsize/20, color='red')


plt.show()