import numpy as np

# deprox_num
# deprox_arr

def deprox_mat(mat, lim = 1e-9):
    """
    Tries to remove floating point errors for 0-value approximations in matrix.
    """
    for r in range(mat.shape[0]):
        for c in range(mat.shape[1]):
            if mat[r,c] < lim:
                mat[r,c] = 0
                
    return mat