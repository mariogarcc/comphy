import numpy as np

def trapeze_integrate(f, interval, npoints = 1e6):
    n = npoints
    n = int(n)

    a, b = interval
    delta = (b-a)/n

    x = (a + delta*(h) for h in range(1, n))

    v = (delta/2)*(f(a)+f(b)) + (delta*sum((f(x_k) for x_k in x)))

    return v


def simpson_integrate(f, interval, method = '1/3', npoints = 1e6):

    npoints = int(npoints)
    n = npoints

    a, b = interval

    if method == '1/3':

        delta = (b-a)/(2*n)
        x = [a + delta*(h) for h in range(1, 2*n)]

        v =   (  delta/3)*   (f(a)+f(b)) \
            + (2*delta/3)*sum(f(x[2*h+1]) for h in range(int(n-1))) \
            + (4*delta/3)*sum(f(x[2*h]) for h in range(int(n)))

    elif method == '3/8':
        # something is not working properly here...
        delta = (b-a)/(3*n)
        x = [a + delta*(h) for h in range(1, 3*n)]

        v =   (3*delta/8)*   (f(a)+f(b)) \
            + (6*delta/8)*sum(f(x[3*h+1]) for h in range(int(n-1))) \
            + (9*delta/8)*sum(f(x[3*h-1])+f(x[3*h]) \
                    for h in range(int(n)))
    
    else:
        raise ValueError("invalid value for method: {!s}".format(method))

    return v


def recursive_integrate(f, interval, method = 'simpson',
    iters = 15, prec = None, verbose = False):
    
    if prec is not None:
        iters = 2

    a, b = interval

    t = (b-a)/2 * (f(a)+f(b))
    s = None
    v = None

    i = 0
    while i < iters:

        pt, ps = t, s
        pv = ps if method in 'simpson' else pt

        n = int(2**i)

        delta = (b-a)/2**(i+1)
        x = [a + delta*h for h in range(1, 2*n)]

        t = pt/2 + delta * sum(f(x[2*i]) for i in range(n))
        s = (4*t-pt)/3

        v = s if method in 'simpson' else t
        
        i += 1
        try:
            if prec is not None and i == iters and abs(v-pv) > prec:
                iters += 1
        except Exception as e:
            try:
                olderr
            except NameError:
                olderr = True
            if olderr:
                raise(e)

    if verbose:
        print(f"result took {iters} iterations")

    return v


def romberg_integrate(f, interval, upgrade = 5, prec = None, showres = False):
    a, b = interval
    u = upgrade

    r = dict()

    t = (b-a)/2 * (f(a)+f(b))
    for j in range(1, u+1):
        try:
            r[j]
        except:
            r[j] = dict()
            r[j][1] = t
        pt = t
        n = int(2**(j-1))
        delta = (b-a)/2**j
        x = [a + delta*(h) for h in range(1, 2*n)]

        t = pt/2 + delta * sum(f(x[2*i]) for i in range(n))

    for j in range(1, u+1):
        for k in range(2, u+1):
            if j >= k:
                r[j][k] = (4**(k-1) * r[j][k-1] - r[j-1][k-1])/(4**(k-1)-1)

    if prec is not None:
        if abs(r[u][u-1] - r[u][u]) > prec:
            return romberg_integrate(f, interval, upgrade = u+1, prec = prec,
                showres = showres)

    if showres:
        return (r[u][u],
              [[r[n][j] for j in r[n].keys()] for n in r.keys()],
               [r[n][len(r[n])] for n in r.keys()])

    return r[u][u]

# if returning r from romberg_integrate:
# print(*[[r[n][j] for j in r[n].keys()] for n in r.keys()], sep = '\n') # matrix
# print(*[r[n][len(r[n])] for n in r.keys()], sep = '\n') # diagonal

import random
def montecarlo_integrate(f, interval, npoints = 1e6):
    n = int(npoints)
    a, b = interval
    v = b-a

    mf, mfsq = 0, 0
    for i in range(n):
        d = random.uniform(a, b)
        mf += f(d)
        mfsq += f(d)**2

    mf /= n
    mfsq /= n

    v, err = v*mf, v*np.sqrt((mfsq - mf**2)/n)
    return v, err