from package import redact_ex

from package import \
    gauss_reduce, \
    plu_decomp, plu_solve, \
    solve_triang_mat, \
    check_sys_sols

import numpy as np

a = np.array([[1, 2, -1], [2, 4, 5], [3, -1, -2]], dtype = float)
b = np.array([[2], [25], [-5]], dtype = float)

a = a.reshape(len(a), len(a))
b = b.reshape(len(b), 1)
ab = np.concatenate((a, b), axis = 1)

print()
print("Matrix of coefficients A (given):", a, sep = '\n\n', end = '\n\n')
print("Vector of independent terms B (given):", b, sep = '\n\n', end = '\n\n')
print("Expanded matrix (AB):", ab, sep = '\n\n', end = '\n\n')
print()


EXERCISE_7 = """\
Make a program that is able to solve a system of equations
by the Gauss elimination method with partial pivoting and solution computing
by regressive substitution.\
"""

redact_ex(EXERCISE_7, 7)


tmat = gauss_reduce(ab, pivoting = 'partial')
print("Triangularized matrix (T):", tmat, sep = '\n\n', end = '\n\n')
sols = solve_triang_mat(tmat)
print("Obtained solutions:", sols, sep = '\n\n', end = '\n\n')
osols = check_sys_sols(sols, ab)
if osols is None:
    print("Obtained solutions were incorrect.")
print("Ordered solutions:", osols, sep = '\n\n', end = '\n\n')
print("i.e.:", *("x_{i} = {sol_i}"
    .format(i = i+1, sol_i = osols[i]) for i in range(len(osols))),
    sep = '\n', end = '\n\n\n')


EXERCISE_8 = """\
Make a program that is able to solve a system of equations
by the Gauss elimination method with full pivoting and solution computing
by regressive substitution.\
"""

redact_ex(EXERCISE_8, 8)


tmat = gauss_reduce(ab, pivoting = 'total')
print("Triangularized matrix (T):", tmat, sep = '\n\n', end = '\n\n')
sols = solve_triang_mat(tmat)
print("Obtained solutions:", sols, sep = '\n\n', end = '\n\n')
osols = check_sys_sols(sols, ab)
if osols is None:
    print("Obtained solutions were incorrect.")
print("Ordered solutions:", osols, sep = '\n\n', end = '\n\n')
print("i.e.:", *("x_{i} = {sol_i}"
    .format(i = i+1, sol_i = osols[i]) for i in range(len(osols))),
    sep = '\n', end = '\n\n\n')


EXERCISE_9 = """\
Make a program that is able to solve a system of equations
by the Gauss-Jordan elimination method with full pivoting.\
"""

redact_ex(EXERCISE_9, 9)


tmat = gauss_reduce(ab, method = 'gj-elim', pivoting = 'total')
print("Triangularized matrix (T):", tmat, sep = '\n\n', end = '\n\n')
sols = solve_triang_mat(tmat, method = 'gj-elim')
print("Obtained solutions:", sols, sep = '\n\n', end = '\n\n')
osols = check_sys_sols(sols, ab)
if osols is None:
    print("Obtained solutions were incorrect.")
print("Ordered solutions:", osols, sep = '\n\n', end = '\n\n')
print("i.e.:", *("x_{i} = {sol_i}"
    .format(i = i+1, sol_i = osols[i]) for i in range(len(osols))),
    sep = '\n', end = '\n\n\n')


EXERCISE_10 = """\
Make a program that is able to solve a system of equations
by the Gauss-Jordan inversion method with full pivoting.\
"""

redact_ex(EXERCISE_10, 10)


eimat = gauss_reduce(ab, method = 'gj-inv', pivoting = 'total')
print("Extended inverted matrix (IA^-1):", eimat, sep = '\n\n', end = '\n\n')
sols = solve_triang_mat(eimat, ind_terms = b, method = 'gj-inv')
print("Obtained solutions:", sols, sep = '\n\n', end = '\n\n')
osols = check_sys_sols(sols, ab)
if osols is None:
    print("Obtained solutions were incorrect.")
print("Ordered solutions:", osols, sep = '\n\n', end = '\n\n')
print("i.e.:", *("x_{i} = {sol_i}"
    .format(i = i+1, sol_i = osols[i]) for i in range(len(osols))),
    sep = '\n', end = '\n\n\n')


EXERCISE_11 = """\
Make a program that is able to solve a system of equations using the
PLU decomposition method.\
"""

redact_ex(EXERCISE_11, 11)


p, l, u, b = plu_decomp(ab)
print("Permutation matrix (P):", p, sep = '\n\n', end = '\n\n')
print("Lower triangular matrix (L):", l, sep = '\n\n', end = '\n\n')
print("Upper triangular matrix (U):", u, sep = '\n\n', end = '\n\n')
sols = plu_solve(p, l, u, b)
print("Obtained solutions:", sols, sep = '\n\n', end = '\n\n')
osols = check_sys_sols(sols, ab)
if osols is None:
    print("Obtained solutions were incorrect.")
print("Ordered solutions:", osols, sep = '\n\n', end = '\n\n')
print("i.e.:", *("x_{i} = {sol_i}"
    .format(i = i+1, sol_i = osols[i]) for i in range(len(osols))),
    sep = '\n')

