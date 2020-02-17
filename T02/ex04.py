from package import *

from package import redact_ex

from package import \
    gauss_reduce, \
    plu_decomp, plu_solve, \
    solve_triang_mat, \
    check_sys_sols

import numpy as np

EXERCISE_09 = """\
Make a program that is able to solve a system of equations
by the Gauss-Jordan elimination method with full pivoting.\
"""

redact_ex(EXERCISE_09, 9)


a = np.array([[1, 2, -1], [2, 4, 5], [3, -1, -2]], dtype = float)
b = np.array([[2], [25], [-5]], dtype = float)

a = a.reshape(len(a), len(a))
b = b.reshape(len(b), 1)
ab = np.concatenate((a, b), axis = 1)

print("Matrix of coefficients A (given):", a, sep = '\n\n', end = '\n\n')
print("Vector of independent terms B (given):", b, sep = '\n\n', end = '\n\n')
print("Expanded matrix (AB):", ab, sep = '\n\n', end = '\n\n')

tmat = gauss_reduce(ab, method = 'gj-elim', pivoting = 'total')
print("Triangularized matrix (T):", tmat, sep = '\n\n', end = '\n\n')
sols = solve_triang_mat(tmat, method = 'gj-elim')
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