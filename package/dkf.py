from .gauss_reduce import gauss_reduce
from .solve_algebra import solve_triang_mat
from .check import check_sys_sols

import numpy as np


def dkf(f, x0, k, npoints = 5, delta = 0.1):

    assert isinstance(k, int)

    if not npoints >= k+1:
        npoints = k+1

    npoints = int(npoints)
    if npoints % 2 != 1:
        npoints += 1 # npoints must be odd

    b = [n for n in range(int(-(npoints-1)/2), int((npoints+1)/2))]

    cmat = np.array([np.array(b)**k for k in range(npoints)], dtype = float) \
        .reshape(npoints, len(b))
    imat = np.array([[0]]*cmat.shape[0], dtype = float) \
        .reshape(cmat.shape[0], 1)
    smat = np.hstack([cmat, imat])

    tmat = gauss_reduce(smat)

    tmat[k,-1] = np.math.factorial(k)

    sols = solve_triang_mat(tmat)
    a = check_sys_sols(sols, tmat)

    dkfx0 = sum([a[i]*f(x0 + b[i]*delta) for i in range(npoints)])/delta**k

    return dkfx0
