from .solve_algebra import solve_triang_mat

import copy
import numpy as np

def plu_decomp(cmat):

    mat = copy.deepcopy(cmat)

    if mat.shape[0]+1 == mat.shape[1]:
        arg = 'system'
    elif mat.shape[0] == mat.shape[1]:
        arg = 'coeffs'
    else:
        raise ValueError("invalid matrix")

    U = mat if arg == 'coeffs' else mat[:,:-1]
    L = np.zeros((mat.shape[0], mat.shape[0]))
    P = np.identity(mat.shape[0])
    b = mat[:,-1] if arg == 'system' else None

    neqs = mat.shape[0]

    for i in range(neqs-1):

        rval = None
        for r in range(i+1, neqs):
            rval = r if abs(U[r,i]) > abs(U[i,i]) else rval
        
        if rval is not None:
            nr = rval

            temp_mat = copy.deepcopy(U)
            U[i,], U[nr,] = temp_mat[nr,], temp_mat[i,]

            temp_mat = copy.deepcopy(L)
            L[i,], L[nr,] = temp_mat[nr,], temp_mat[i,]

            temp_mat = copy.deepcopy(P)
            P[i,], P[nr,] = temp_mat[nr,], temp_mat[i,]

        for eq in range(i+1, neqs):
            with np.errstate(divide = 'raise', invalid = 'raise'):
                try:
                    pivot = U[eq,i]/U[i,i]
                    U[eq,:] -= U[i,:] * pivot
                    L[eq,i] = pivot
                except(ZeroDivisionError, FloatingPointError):
                    raise ValueError("cannot compute matrix")

    for i in range(L.shape[0]):
        L[i,i] = 1

    if b is not None:
        return P, L, U, b
    else:
        return P, L, U


def plu_solve(P, L, U, b):

    Pb = (P @ b).reshape(len(b), 1)

    Ly = np.hstack([L, Pb])

    y = np.array(solve_triang_mat(Ly, shape = 'lower-left')) \
        .reshape(len(Pb), 1)

    Ux = np.hstack([U, y])

    x = np.array(solve_triang_mat(Ux, shape = 'upper-right'))
    return x[::-1]