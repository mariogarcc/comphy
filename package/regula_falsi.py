def regula_falsi(f, interval):
    """
    Splits an interval in two using the regula falsi method.
    """
    a, b = interval
    c = a - f(a) * (b - a)/(f(b) - f(a))
    return [[a, c], [c, b]]


def falsi_solve(f, interval, iters = 8, sign_check_func = lambda x, y: x*y < 0,
    verbose = False):
    """
    Approximates a solution to a function *f* that is known to be in a given 
    interval through `iters` iterations using the regula falsi method.
    """
    si = interval # starting interval
    try:
        for _ in range(iters):
            interval = [half for half in regula_falsi(f, interval)
                        if sign_check_func(f(half[0]), f(half[1]))][0]
    except IndexError:
        psols = regula_falsi(f, interval) # possible solutions
        for psol in psols[0][1], psols[1][0]:
            # because it's either [a, sol] or [sol, b]
            if 0 - f(psol) <= f((interval[0] + interval[1])/2):
                if verbose:
                    print("solution: x = {sol:.6f} "
                          "(y = {im:.6e})\niterations: {iters}"
                          .format(sol=psol, im=f(psol), iters=iters))
                return psol

        if verbose:
            print("stopped at {} iterations".format(_))
        if si == interval:
            raise ValueError(
                "solution was non-existent in the given interval")
        pass

    else:
        if verbose:
            print("successfully completed all iterations")
        pass
    sol = (interval[0] + interval[1])/2
    if verbose:
        print("solution: x = {sol:.6f} (y = {im:.6e})\niterations: {iters}"
            .format(sol=sol, im=f(sol), iters=iters))
    return sol
