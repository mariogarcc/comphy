import copy
import numpy as np

def solve_ordid(eq):
    """
    Solves a0*x + a1 + ... + aN = b given as a list like `[a0, ..., aN, b]`.
    """
    eq = np.array([val for val in eq if val != 0])
    return (eq[-1] - sum(eq[1:-1]))/eq[0]


def solve_triang_mat(mat, shape = 'upper-right', method = 'g-elim',
    check_mat = False):
    """
    Solves a triangular matrix.
    """
    shape, method = shape.lower(), method.lower()

    if check_mat:
        if (len(np.nonzero(mat)[0]) \
                == mat.size - sum([i for i in range(mat.shape[0])]) \
            and (
                mat[mat.shape[0]-1,0] == 0 \
                or mat[0,mat.shape[1]-1] == 0 \
                or mat[0,0] == 0 \
                or mat[mat.shape[0]-1,mat.shape[1]-1] == 0
                )
        ):
            raise ValueError("matrix is not triangular")
    # triangular matrix

    temp_mat = copy.deepcopy(mat)

    if 'upper' in shape: irows = range(mat.shape[0]-1, -1, -1)
    elif 'lower' in shape: irows = range(-1, mat.shape[0], 1)

    sols = []
    for r, rr in zip(irows, reversed(irows)):

        sol = solve_ordid(temp_mat[r,:])
        sols.append(sol)

        if 'right' in shape:
            v = mat.shape[1]-2-rr
        elif 'left' in shape:
            v = rr+1

        for s in (range(r) if 'upper' in shape else range(1, rr+1)):
            if method == 'g-elim':
                temp_mat[s,v] *= sol
            elif method == 'gj-elim':
                temp_mat[s,:] -= temp_mat[r,:] * temp_mat[s,v]/temp_mat[r,r]

    return sols