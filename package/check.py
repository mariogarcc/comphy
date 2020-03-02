import itertools as it

def check_sys_sols(sols, mat, lim = 1e-3, verbose = False):
    """
    Checks if a set of solutions for a matrix is correct.
    """
    permutations = it.permutations(sols)

    minmaxerr = 1/lim if ((lim < 1) & (lim != 0)) else lim**2
    for permutation in permutations:
        maxerr = 0
        # check if any sum is wrong: sum(a_ij*x_i) =? b_j +- err
        for r in range(mat.shape[0]):

                # err = b_j - sum(a_ij*x_i)
                err = abs(mat[r,-1] - sum([mat[r,c] * permutation[c] \
                        for c in range(mat.shape[1]-1)]))

                # store the maximum value for err
                maxerr = err if err > maxerr else maxerr

        if maxerr == 0: # already found exact match
            return permutation

        # store the best permutation in case of a non-exact match
        if maxerr < minmaxerr:
            minmaxerr = maxerr
            correct_permutation = permutation

    if minmaxerr != 0 and minmaxerr < lim: # valid solution
        if verbose:
            print("solutions are not exact up to approx. {!r} precision"
                .format(minmaxerr))
    elif minmaxerr >= lim: # invalid solution
        return None

    return correct_permutation