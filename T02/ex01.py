from package import *


EXERCISE_01 = """\
Make a program that is able to solve a system of equations
by the Gauss elimination method without pivoting and solution computing
by regressive substitution.\
"""

redact_ex(EXERCISE_01, 1)


import numpy as np

a = np.array([[2, -1, 1], [-1, 1, 2], [1, 2, -1]], dtype = float)
b = np.array([[3], [7], [2]], dtype = float)
# given system

a = a.reshape(len(a), len(a))
b = b.reshape(len(b), 1)
ab = np.concatenate((a, b), axis = 1)

print("Matrix of coefficients A (given):", a, sep = '\n\n', end = '\n\n')
print("Vector of independent terms B (given):", b, sep = '\n\n', end = '\n\n')
print("Expanded matrix (AB):", ab, sep = '\n\n', end = '\n\n')
tmat = gauss_reduce(ab, pivoting = 'none')
print("Triangularized matrix (T):", tmat, sep = '\n\n', end = '\n\n')
sols = solve_triang_mat(tmat)
print("Obtained solutions:", sols, sep = '\n\n', end = '\n\n')
sols = deprox_arr(sols)
print("Fixed solutions:", sols, sep = '\n\n', end = '\n\n')
osols = check_sys_sols(sols, ab)
if osols is None:
    print("Obtained solutions were incorrect.")
print("Ordered solutions:", osols, sep = '\n\n', end = '\n\n')
print("i.e.:", *("x_{i} = {sol_i}"
    .format(i = i+1, sol_i = osols[i]) for i in range(len(osols))),
    sep = '\n')