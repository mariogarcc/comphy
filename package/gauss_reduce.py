import copy
import numpy as np

from .mat_ops import mat_shift

def gauss_reduce(mat, method = 'g-elim', pivoting = None,
    shift = 0, inplace = False):
    """
    Solves an extended matrix corresponding to a linear system of
    equations.
    """

    # check args
    pivoting = pivoting.lower() if pivoting is not None else None
    method = method.lower()
    try:
        if pivoting not in [None, 'none', 'partial', 'total']:
            raise ValueError("{!r} is not a valid value for `pivoting`"
                .format(pivoting))
        if method not in ['g-elim', 'gj-elim', 'gj-inv']:
            raise ValueError("{!r} is not a valid value for `method`"
                .format(method))
        mat.size
        if any([all([coeff for coeff in mat[:,c] == 0]) \
                for c in range(mat.shape[1]-1)]) == True \
            or mat.shape[1] != mat.shape[0]+1:
            raise ValueError("\n{!r}\nis not a valid matrix".format(mat))
    except AttributeError:
        raise ValueError("\n{!r}\nis not a valid matrix".format(mat))

    if inplace:
        cmat = mat
    else:
        cmat = copy.deepcopy(mat)

    if (method == 'gj-inv' or method == 'gj-elim') and pivoting is None:
        pivoting = 'total'

    # it's a good idea to make paper sketches to figure out the indices needed
    neqs = cmat.shape[0]
    if method == 'gj-inv':
        cmat = cmat[:,:neqs]
        cmat = np.hstack((cmat, np.identity(mat.shape[0])))

    for i in range(neqs-1):

        if pivoting == 'partial':

            rval = None
            for r in range(i+1, neqs):
                rval = r if abs(cmat[r,i]) > abs(cmat[i,i]) else rval
            
            if rval is not None:
                nr = rval

                temp_mat = copy.deepcopy(cmat)
                cmat[i,], cmat[nr,] = temp_mat[nr,], temp_mat[i,]

        if pivoting == 'total':

            # get the indices of the maximum absolute value
            temp_max_loc = np.unravel_index( \
                abs(cmat[i:,i:-1]).argmax(), cmat[i:,i:-1].shape)
            max_loc = (temp_max_loc[0]+i, temp_max_loc[1]+i)

            # make the maximum absolute value the pivoting element
            temp_mat = copy.deepcopy(cmat)
            cmat[i,:], cmat[max_loc[0],:] = temp_mat[max_loc[0],:], temp_mat[i,:]
            temp_mat = copy.deepcopy(cmat)
            cmat[:,i], cmat[:,max_loc[1]] = temp_mat[:,max_loc[1]], temp_mat[:,i]

        for eq in range(i+1, neqs):
            with np.errstate(divide = 'raise', invalid = 'raise'):
                try:
                    cmat[eq,:] -= cmat[i,:] * cmat[eq,i]/cmat[i,i]
                except(ZeroDivisionError, FloatingPointError):
                    if shift > mat.shape[0]-1:
                        raise ValueError("cannot reduce matrix")
                    gauss_reduce(mat_shift(mat), pivoting = pivoting,
                        shift = shift+1)
                    # shifting is only a partial solution
                    # there are neqs! permutations, but that's too many to try

    return cmat