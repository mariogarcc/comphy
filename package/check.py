import itertools as it
import numpy as np

def check_sys_sols(sols, mat, lim = 1e-3, verbose = False):
    """
    Checks if a set of solutions for a matrix is correct.
    """
    permutations = it.permutations(sols)
    minmaxerr = lim # how to make lim and minmaxerr independent?

    for permutation in permutations:
        maxerr = 0
        # check if any sum is wrong: sum(a_ij*x_i) =? b_j +- err
        for r in range(mat.shape[0]):

                # val = b_j - sum(a_ij*x_i)
                val = abs(mat[r,-1] - sum([mat[r,c] * permutation[c] \
                        for c in range(mat.shape[1]-1)]))

                # store the maximum value for err, the max error
                maxerr = val if val > maxerr else maxerr

        minmaxerr = maxerr if maxerr < minmaxerr else minmaxerr

    if minmaxerr != 0 and minmaxerr < lim:
        if verbose:
            print("solutions are not exact up to approx. {!r} precision"
                .format(minmaxerr))
    elif minmaxerr >= lim:
        return False

    return True