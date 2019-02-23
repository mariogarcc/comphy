def newt_raph_solve(f, df, asol, iters = 8,
    sign_check_func = lambda x, y: x*y < 0, verbose = False):
    """
    Further approximates a given solution to a function *f* through `iters`
    iterations of the Newton-Raphson method.
    """
    if iters == 0:
        if verbose:
            print("solution: x = {sol:.6f} (y = {im:.6e})"
                      .format(sol=asol, im=f(asol), iters=iters))
        return asol
    else:
        try:
            asol -= f(asol)/df(asol)
            return newt_raph_solve(f, df, asol, iters-1)
        except:
            if verbose:
                print("stopped at {iters} iterations".format(iters = iters))
            return asol
        else:
            if verbose:
                print("successfully completed all iterations")
