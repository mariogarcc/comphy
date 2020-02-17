from package import redact_ex

from package import jacobi_eigenfind

from package import deprox_num, deprox_arr


EXERCISE_01 = """\
Make a program that is able to compute the eigenvalues and eigenvectors of a
simetrical matrix using the Jacobi method.\
"""

redact_ex(EXERCISE_01, 1)


import numpy as np

mat = np.array([[3, -1, 0], [-1, 2, -1], [0, -1, 3]], dtype = float)
mat = mat.reshape(len(mat), len(mat))

d, v = jacobi_eigenfind(mat)

print("Matrix (M):", mat, sep = '\n', end = '\n\n')
print("Obtained eigencouples (\u03BB, v):",
    *[(deprox_num(d[i,i]), deprox_arr(v[:,i])) \
        for i in range(d.shape[0])], sep = '\n')