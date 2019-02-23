import copy
import numpy as np

from .solve_algebra import solve_triang_mat
from .mat_ops import mat_shift

def gauss_solve(mat, pivoting = 'none', method = 'g-elim', shift = 0):
    """
    Solves an extended matrix corresponding to a linear system of
    equations.
    """
    cmat = copy.deepcopy(mat)

    # check args
    pivoting = pivoting.lower()
    method = method.lower()
    try:
        if pivoting not in ['none', 'partial', 'total']:
            raise ValueError("{!r} is not a valid value for `pivoting`"
                .format(pivoting))
        if method not in ['g-elim', 'gj-elim', 'gj-inv']:
            raise ValueError("{!r} is not a valid value for `method`"
                .format(method))
        mat.size
        if any([all([coeff for coeff in mat[:,c] == 0]) \
                for c in range(mat.shape[1]-1)]) == True \
            or mat.shape[1] != mat.shape[0]+1:
            raise ValueError("{!r} is not a valid matrix".format(mat))
    except AttributeError:
        raise ValueError("{!r} is not a valid matrix".format(mat))

    neqs = mat.shape[0]
    for i in range(neqs-1):
        print(i)

        if pivoting == 'partial':

            for r in range(i+1, neqs):
                rvals = []
                if abs(mat[r,i]) > abs(mat[i,i]):
                    rvals.append([mat[r,i], r])
            if rvals:
                if len(rvals) == 1:
                    nr = rvals[0][1]
                else:
                    try:
                        nr = rvals.index(max([rval[0] for rval in rvals]))[1]
                    except:
                        nr = rvals[0]

                temp_mat = copy.deepcopy(mat)
                mat[i,], mat[nr,] = temp_mat[nr,], temp_mat[i,]
            
        if pivoting == 'total':

            # get the indices of the maximum absolute value
            temp_max_loc = np.unravel_index( \
                abs(mat[i:,i:-1]).argmax(), mat[i:,i:-1].shape)
            max_loc = (temp_max_loc[0]+i, temp_max_loc[1]+i)

            # make the maximum absolute value the pivoting element
            temp_mat = copy.deepcopy(mat)
            mat[i,:], mat[max_loc[0],:] = temp_mat[max_loc[0],:], temp_mat[i,:]
            temp_mat = copy.deepcopy(mat)
            mat[:,i], mat[:,max_loc[1]] = temp_mat[:,max_loc[1]], temp_mat[:,i]

        for eq in range(i+1, neqs):
            print(eq)
            # i = 0 -> eq = 1, 2
            # i = 1 -> eq = 2 ... (for this case, where size = 3)
            with np.errstate(divide = 'raise', invalid = 'raise'):
                try:
                    mat[eq,:] -= mat[i,:] * mat[eq,i]/mat[i,i]
                except(ZeroDivisionError, FloatingPointError):
                    if shift > mat.shape[0]-1:
                        raise ValueError("cannot solve matrix")
                    gauss_solve(mat_shift(cmat), pivoting = pivoting, 
                        shift = shift+1)
                    # shifting is only a partial solution - the system could
                    # still be solved as long as all the coefficients in a col
                    # corresponding to each variable are not zero, but this
                    # method will only allow up to *neqs* permutations instead
                    # of *neqs!*, which would eventually yield the solutions
                    # as long as they're obtainable

                    # someone could also use itertools.permutations()
                    # https://docs.python.org/3.7/library/itertools.html#itertools.permutations

    print(mat)
    return solve_triang_mat(mat)

