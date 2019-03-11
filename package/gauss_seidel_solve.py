import numpy as np

a = np.array([[4, -1, 1], [4, -8, 1], [-2, 1, 5]], dtype = float)
b = np.array([[7], [-21], [15]], dtype = float)

a = a.reshape(len(a), len(a))
b = b.reshape(len(b), 1)
ab = np.concatenate((a, b), axis = 1)

def gauss_seidel_solve(mat, b = False, asol = None, prec = 1e-9, niter = None,
    verbose = False, MAX_ITERATIONS = 1e3):

    MAX_ITERATIONS = int(MAX_ITERATIONS)

    niter = 0 if niter is None else niter

    if b is False and mat.shape[0] == mat.shape[1]:
        raise ValueError()
    elif b is False:
        a = mat[:,:-1]
        b = mat[:,-1]
    else:
        a = mat

    nvars = a.shape[1]

    if asol is None:
        asol = np.array([0.]*nvars, dtype = float)
    assert nvars == len(asol)

    x = np.array([v for v in asol])

    for i in range(nvars):
        if a[i,i] != 0:
            x[i] = (b[i] - sum([a[i,j]*x[j] for j in range(nvars) if j != i]))\
                /a[i,i]
        else:
            continue

    d = sum([abs(x[i] - asol[i]) for i in range(len(x))]) \
        /sum(asol if sum(asol) != 0 else [prec])

    if d < prec and niter != 0:
        if verbose:
            print("completed {niter} iterations".format(niter = niter+1))
        return x
    elif niter != MAX_ITERATIONS:
        return gauss_seidel_solve(a, b, asol = x,
            prec = prec, niter = niter+1, verbose = verbose,
            MAX_ITERATIONS = MAX_ITERATIONS)
    else:
        if verbose:
            print("completed all iterations and failed")
        return None