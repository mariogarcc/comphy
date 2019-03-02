from package import \
    gauss_reduce, \
    solve_triang_mat, \
    check_sys_sols

# EXERCISE 5: Make a program that is able to solve a system of equations
# by the Gauss elimination method without pivoting and solution computing
# by regressive substitution.

print("""
EXERCISE 5: Make a program that is able to solve a system of equations
by the Gauss elimination method without pivoting and solution computing
by regressive substitution.
""")

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
tmat = gauss_reduce(ab)
print("Triangularized matrix (T):", tmat, sep = '\n\n', end = '\n\n')
sols = solve_triang_mat(tmat)
print("Obtained solutions:", sols, sep = '\n\n', end = '\n\n')
osols = check_sys_sols(sols, ab)
print("Ordered solutions:", osols, sep = '\n\n', end = '\n\n')
print("i.e.:", *("x_{i} = {sol_i}"
    .format(i = i+1, sol_i = osols[i]) for i in range(len(osols))),
    sep = '\n')