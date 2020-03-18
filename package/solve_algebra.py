import copy
import numpy as np

def solve_ordid(eq):
    """
    Solves a0*x + a1 + ... + aN = b given as a list like `[a0, ..., aN, b]`.
    """
    xloc = np.min(np.argwhere(eq != 0))
    eq = np.array([val for val in eq[xloc:]])
    return (eq[-1] - sum(eq[1:-1]))/eq[0]


def solve_triang_mat(mat, shape = 'upper-right', method = 'g-elim',
    ind_terms = None, check_mat = False):
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
    elif 'lower' in shape: irows = range(0, mat.shape[0], 1)

    sols = []
    for r, rr in zip(irows, reversed(irows)):

        solrow = temp_mat[r,:] if 'right' in shape else \
            np.concatenate((temp_mat[r,:-1][::-1], [temp_mat[r,-1]]))
        sol = solve_ordid(solrow)
        sols.append(sol)

        v = mat.shape[1]-1-(rr+1)

        if method == 'gj-inv':
            temp_mat[r,:] /= temp_mat[r,r]

        sr = range(r) if 'upper' in shape else range(r+1, mat.shape[0])
        for s in sr:
            if method == 'g-elim':
                temp_mat[s,v] *= sol
            elif method == 'gj-elim':
                temp_mat[s,:] -= temp_mat[r,:] * temp_mat[s,v]/temp_mat[r,r]
            elif method == 'gj-inv':
                temp_mat[s,:] -= temp_mat[r,:] * temp_mat[s,r]/temp_mat[r,r]

    if method == 'gj-inv':
        if ind_terms is None:
            raise ValueError("""gauss-jordan inversion method requires \
                the array of independent terms in the input""")
        else:
            return (temp_mat[:,temp_mat.shape[0]:] @ ind_terms) \
                .reshape(1, temp_mat.shape[0])[0]
    return sols