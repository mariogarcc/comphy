"""
Utilizando los conocimientos de la primera parte de la asignatura podemos
encontrar las soluciones numéricas cualquier una función de una variable.
Con un poco de álgebra simple se puede llegar a obtener un polinomio en
función de "u" que verifique las condiciones de solución
f(u, v) = g(u, v) = 0, sobre el cual se aplica el
programa que obtiene sus soluciones numéricas.
"""

# program setup
import numpy as np
import matplotlib.pyplot as plt

plt.rc('text', usetex = True)
plt.rc('font', family = 'serif')


def find_sols(f, arr, sign_check_func = lambda x, y: x*y < 0, verbose = False):
    """
    Given an array of section points, checks if function *f* has a solution
    in any of the intervals formed by said points.
    """
    sols = []
    for i in range(len(arr)-1):
        if sign_check_func(f(arr[i]), f(arr[i+1])):
            sols.append([arr[i], arr[i+1]])

    if verbose:
        print("solution(s) in: ", *sols, sep = '\n')
    return sols


def bisect(interval):
    """
    Splits number interval (given as a list of two values) in two halves.
    """
    a, b = interval
    h = (a+b)/2
    return [[a, h], [h, b]]


def bisect_solve(f, interval, iters = 8, sign_check_func = lambda x, y: x*y < 0,
    verbose = False):
    """
    Approximates a solution to a function *f* that is known to be in a given 
    interval through `iters` number of iterations using the bisection method.
    """
    si = interval # starting interval
    try:
        for _ in range(iters):
            interval = [half for half in bisect(interval) \
                if sign_check_func(f(half[0]), f(half[1]))][0]
    except IndexError:
        if verbose:
            print(f"stopped at {_} iterations")
        if si == interval:
            raise ValueError(
                "solution was non-existent in the given interval")
    else:
        if verbose:
            print("successfully completed all iterations")

    sol = (interval[0] + interval[1])/2

    if f(sol) == np.inf:
        # cannot avoid using numpy for this
        if verbose:
            print(f"solution: x = {sol} -> FALSE SOLUTION (y = oo)")
        return sol

    if verbose:
        print(
            f"solution: x = {sol:.6f} (y = {f(sol):.6e})\niterations: {iters}")
    return sol


# with simple algebra, we find the polinomial associated to the problem
a = 0.1; b = 0.1; gamma = 1
def pol(u, a = a, b = b, gamma = gamma):
    return u * ((a-u) * (u-1) - (b/gamma))

# computation parameters
interval = [-1, 1] # interval chosen by inspection
xmin, xmax = interval
n = 201 # number of subintervals
bisect_iters = 999 # iterations for the bisect method

# helper arrays
xarr = np.linspace(xmin, xmax, n+1)
xlin = np.linspace(xmin, xmax, 1000)

# calculate the intervals where there is a solution
sols = find_sols(pol, xarr)
try:
    assert len(sols) > 0
except(AssertionError, TypeError):
    print("There are no solutions for f(x) in the given interval.")
print("There {} in: "
    .format("is a solution" if len(sols) == 1 else "are solutions"),
    *sols, sep = '\n', end = '\n\n')


bisect_sol_points = []
for sol in sols:
    print(f"case: solution in {sol}")
    bisect_sol_points.append(bisect_solve(pol, sol, iters = bisect_iters))
    print(f"solution: u = {bisect_sol_points[sols.index(sol)]}")
    print(f"iterations: {bisect_iters}", end = '\n\n')


# plotting 
plt.figure(figsize = (9, 6))
plt.title(r"$P(u) = u\,\left[(a-u)\,(u-1) - (b/\gamma)\right]$", fontsize = 16)
plt.xlabel(r"$u$", fontsize = 16)
plt.ylabel(r"$P(u)$", fontsize = 16)

plt.plot(xlin, pol(xlin), 'blue')

# highlight the solution points
plt.hlines(0, min(xlin), max(xlin), 'black')
gsize = max(pol(xlin)) - min(pol(xlin))  # plot vertical size
for sol in bisect_sol_points:
    plt.vlines(sol, pol(sol)-gsize/20, pol(sol)+gsize/20, color='red')
    if bisect_sol_points.index(sol) == 1:
        plt.text(sol, pol(sol)+gsize/16+0.1, f'u = {sol:.5f}, v = {b/gamma*sol:.5f}',
            horizontalalignment = 'center')
    else:
        plt.text(sol, pol(sol)+gsize/16, f'u = {sol:.5f}, v = {b/gamma*sol:.5f}',
            horizontalalignment = 'center')

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig("pol.png")
plt.show()