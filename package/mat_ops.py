import copy
import numpy as np

def mat_shift(mat, way = 'down', inplace = False):
    """
    Shifts a matrix's rows by one position
    """
    assert mat.size != None

    if inplace:
        cmat = mat
    else:
        cmat = copy.deepcopy(mat)

    temp_mat = copy.deepcopy(cmat)

    if way.lower() == 'down':
        for r in range(cmat.shape[0]):
            cmat[r,:] = temp_mat[r+1,:] if r+1 != cmat.shape[0] else temp_mat[0,:]
    elif way.lower() == 'up':
        for r in range(cmat.shape[0]):
            cmat[r,:] = temp_mat[r-1,:] if r-1 != -1 else temp_mat[-1,:]
    elif way.lower() == 'right':
        for c in range(cmat.shape[1]):
            cmat[:,c] = temp_mat[:,c+1] if c+1 != cmat.shape[1] else temp_mat[:,0]
    elif way.lower() == 'left':
        for c in range(cmat.shape[1]):
            cmat[:,c] = temp_mat[:,c-1] if c-1 != -1 else temp_mat[:,-1]

    else:
        raise ValueError("{!r} is not a valid value for `way`".format(way))

    return cmat
