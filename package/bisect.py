import numpy as np

def bisect(interval):
    """
    Splits number interval (given as a list of two values) in two halves.
    """
    a, b = interval
    h = (a+b)/2
    return [[a, h], [h, b]]


def bis_solve(f, interval, iters = 8, sign_check_func = lambda x, y: x*y < 0,
    verbose = False):
    """
    Approximates a solution to a function *f* that is known to be in a given 
    interval through `iters` number of iterations using the bisection method.
    """
    si = interval # starting interval
    try:
        for _ in range(iters):
            interval = [half for half in bisect(interval) \
                if sign_check_func(f(half[0]), f(half[1]))][0]
    except IndexError:
        if verbose == True:
            print("stopped at {} iterations".format(_))
        if si == interval:
            raise ValueError(
                "solution was non-existent in the given interval")
    else:
        if verbose == True:
            print("successfully completed all iterations")

    sol = (interval[0] + interval[1])/2

    if f(sol) == np.inf:
        # cannot avoid using numpy for this
        if verbose == True:
            print("y = oo (x = {x}) => false solution".format(x = sol))
        return None

    if verbose == True:
        print("solution: x = {sol:.6f} (y = {im:.6e})\niterations: {iters}"
            .format(sol = sol, im = f(sol), iters = iters))
    return sol
