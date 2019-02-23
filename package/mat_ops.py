import copy
import numpy as np

def mat_shift(mat, way = 'down'):
    """
    Shifts a matrix's rows by one position
    """
    assert mat.size != None
    import copy
    temp_mat = copy.deepcopy(mat)

    if way.lower() == 'down':
        for r in range(mat.shape[0]):
            mat[r,:] = temp_mat[r+1,:] if r+1 != mat.shape[0] else temp_mat[0,:]
    elif way.lower() == 'up':
        for r in range(mat.shape[0]):
            mat[r,:] = temp_mat[r-1,:] if r-1 != -1 else temp_mat[-1,:]
    elif way.lower() == 'right':
        for c in range(mat.shape[1]):
            mat[:,c] = temp_mat[:,c+1] if c+1 != mat.shape[1] else temp_mat[:,0]
    elif way.lower() == 'left':
        for c in range(mat.shape[1]):
            mat[:,c] = temp_mat[:,c-1] if c-1 != -1 else temp_mat[:,-1]

    else:
        raise ValueError("{!r} is not a valid value for `way`".format(way))
    
    return mat