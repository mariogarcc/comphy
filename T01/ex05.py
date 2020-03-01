from package import redact_ex, ask_continue

from package import \
    find_sols, \
    bisect_solve

import numpy as np

import warnings
warnings.filterwarnings('ignore', category = RuntimeWarning)

EXERCISE_05 = """\
Find the roots of y(x) = (29.52/(x-0.12)) * e**(-0.686/x) - 11\
"""

redact_ex(EXERCISE_05, 5)


def f(x):
    return (29.52/(x-0.12)) * np.exp(-0.686/x) - 11

interval = [0.1, 2.2] # interval chosen by inspection
xmin, xmax = interval
n = 4094

xlin = np.linspace(xmin, xmax, n+1)

sols = find_sols(f, xlin)

sol_points = []
for sol in sols:
    print(f"case: solution in {sol}", end = '\n')
    sol_point = bisect_solve(f, sol, 63, verbose = True)
    sol_points.append(sol_point)
    print()

sol_points = sol_points[1:] # ignore the false solution
"""
The above can be seen as bad code practice at first.
Why not just have the function not return false solutions?
Notice the way we construct the array containing the solutions
is exterior to the function that retrieves the accurate solution points.
Therefore, making it return None would just yield a None value inside
the solution array. This could be then fixed with the line

if sol_point is not None: sol_points.append(sol_point)

but we would not get anything from this operation since this fix is also
(compared to the fix I have written above) exterior to the main function.
One could argue this would be a better implementation, since it would allow
to disregard any number of false solutions indistinctively. However, it could
be a possibility that we wanted to do something with the false solution
points, so returning them regardless is actually a better implementation
since clearing the solutions array from unwanted solution points should
anyway be done in a separate code block, like it is done above.

Would adding a "false" flag to the main function's returns be a good idea?
Maybe. However, if dealing with a large number of solutions, you just doubled
the size of the array with potentially a large percentage of useless data
(false solutions can be expected analitically).
"""

# plotting
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

for i, sol in enumerate(sol_points):
    plt.vlines(sol, f(sol)-gsize/20, f(sol)+gsize/20, color = 'red', zorder = 2)
    plt.text(sol+(0.08 if i != 2 else 0), f(sol)+gsize/(16 if i != 0 else 8),
        f'x = {sol:.5f}',
        horizontalalignment = 'center', zorder = 3+i)

plt.show()