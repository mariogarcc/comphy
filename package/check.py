import itertools as it
import numpy as np

def check_sys_sols(sols, mat, lim = 1e-3, verbose = False):
    """
    Checks if a set of solutions for a matrix is correct.
    """
    permutations = it.permutations(sols)

    minmaxerr = 1/lim if ((lim < 1) & (lim != 0)) else lim**2
    psols = dict()
    for permutation in permutations:
        maxerr = 0
        # check if any sum is wrong: sum(a_ij*x_i) =? b_j +- err
        for r in range(mat.shape[0]):

                # err = b_j - sum(a_ij*x_i)
                err = abs(mat[r,-1] - sum([mat[r,c] * permutation[c] \
                        for c in range(mat.shape[1]-1)]))

                # store the maximum value for err
                maxerr = err if err > maxerr else maxerr

        # store the best permutation
        if maxerr < minmaxerr:
            minmaxerr = maxerr
            correct_permutation = permutation

    if minmaxerr != 0 and minmaxerr < lim:
        if verbose:
            print("solutions are not exact up to approx. {!r} precision"
                .format(minmaxerr))
    elif minmaxerr >= lim:
        return None

    return correct_permutation