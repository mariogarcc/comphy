import copy
import numpy as np

def jacobi_eigenfind(mat, d = None, v = None, prec = 1e-9,
    itern = 0, MAX_ITERATIONS = int(1e6)):

    if d is None or v is None:
        d = copy.deepcopy(mat)
        v = np.identity(len(mat), dtype = float)

    nimat = copy.deepcopy(d)
    for i in range(len(nimat)):
        nimat[i,i] = 0.

    p, q = np.unravel_index(np.argmax(abs(nimat)), nimat.shape)

    theta = (d[q,q] - d[p,p]) \
        /(2*d[p,q])

    t = (1 if theta >= 0 else -1)/(abs(theta) + np.sqrt(theta**2 + 1))
    c = 1/np.sqrt(t**2 + 1)
    s = c*t

    r = np.identity(len(mat))
    r[p,p], r[p,q], r[q,p], r[q,q] = c, s, -s, c

    old_evals = [d[i,i] for i in range(d.shape[0])]
    old_evecs = [v[:,i] for i in range(v.shape[1])]

    d = np.transpose(r) @ d @ r
    v = v @ r

    new_evals = [d[i,i] for i in range(d.shape[0])]
    new_evecs = [v[:,i] for i in range(v.shape[1])]

    eval_convergence = all(d < prec for d in \
        [abs(nev-oev) for (nev, oev) in zip(new_evals, old_evals)])
    evec_convergence = all(d < prec for d in \
        [sum([abs(x-ox) for (x, ox) in zip(nevec, oevec)]) \
            for (nevec, oevec) in zip(new_evecs, old_evecs)])

    convergence = eval_convergence and evec_convergence

    if not convergence and itern != MAX_ITERATIONS:
        return jacobi_eigenfind(mat, d, v, prec, itern+1)

    return d, v