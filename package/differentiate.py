import copy
import numpy as np
import itertools as it
import matplotlib.pyplot as plt


def euler_differentiate(w, bounds = None, delta = 1e-3, itern = 1e3,
    plot = True, title = None,
    shape = 'v', figsize = (10, 6), fontsize = 16,
    names = 'txyz', graph = 'all',
    oneout = False, force = False):

    if bounds is None:
        bounds = [0]*len(w)

    if not force and itern >= 1e9:
        raise OverflowError("number of iterations is too big: {!s}" + "\n" + \
            "you can ignore this error by setting the `force` kwarg to `False`"
            .format(itern))

    itern = int(itern)

    var = { i: v for i, v in enumerate(bounds) }
    vec = { i: [v] for i, v in enumerate(var) } if plot else None

    if plot:
        plt.rc('text', usetex = True)
        plt.rc('axes', labelsize = fontsize)
        plt.rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})

        plt.figure(figsize = figsize)
        plt.title(title)

    for n in range(1, itern+1): # iterate method n times

        pvar = copy.deepcopy(var)

        for i,_ in enumerate(var): # compute new variables
            var[i] += w[i](*[delta]+[pvar[j] for j in range(len(pvar))])

            if plot: vec[i].append(var[i])

        if plot and n % int(np.sqrt(itern)) == 0: # best performance
            plot_differential(vec,
                shape = shape, names = names, graph = graph,
                oneout = oneout)

            for key in list(vec.keys()): # resetting vectors for performance
                vec[key] = [vec[key][-1]]

            oneout = True # first item has already been removed (first plot)

    if plot: plt.tight_layout(rect=[0.05, 0.05, 0.95, 0.95]); plt.show()
    return None




def range_kutta_differentiate(w, order = 4,
    bounds = None, delta = 1e-3, itern = 1e3,
    plot = True, title = None,
    shape = 'v', figsize = (10, 6), fontsize = 16,
    names = 'txyz', graph = 'all',
    oneout = False, force = False):

    if bounds is None:
        bounds = [0]*len(w)

    if not force and itern >= 1e9:
        raise OverflowError("number of iterations is too big: {!s}" + "\n" + \
            "you can ignore this error by setting the `force` kwarg to `False`"
            .format(itern))

    itern = int(itern)
    o = int(order)
    assert o == 2 or o == 4

    var = { i: v for i, v in enumerate(bounds) }
    vec = { i: [v] for i, v in enumerate(var) } if plot else None

    if plot:
        plt.rc('text', usetex = True)
        plt.rc('axes', labelsize = fontsize)
        plt.rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})

        plt.figure(figsize = figsize)
        plt.title(title)

    for n in range(1, itern+1):

        pvar = copy.deepcopy(var)
        k = dict()

        for i,_ in enumerate(var):

            k[i] = dict()
            k[i][0] = w[i](*[delta]+[pvar[j] for j in range(len(pvar))])
            # this was for i != 0
            for o in range(1, order):
                div = (1*(1+(o%3 != 0))) # 1, 2, 2, 1
                tel = delta/div
                kel = k[i][o-1]/div
                k[i][o] = w[i](*[delta+tel]+[pvar[j]+kel \
                    for j in range(1, len(pvar))])

            var[i] += sum(k[i][o]/(3*(1+(o%3 == 0))) \
                for o in range(order)) # k1/6 + k2/3 + k3/3 + k4/6

            if plot: vec[i].append(var[i])

        if plot and (n % int(np.sqrt(itern)) == 0 or n == itern): # performance
            plot_differential(vec,
                shape = shape, names = names, graph = graph,
                oneout = oneout)

            for key in list(vec.keys()): # resetting vectors for performance
                vec[key] = [vec[key][-1]]

            oneout = True # first item has already been removed (first plot)

    if plot: plt.tight_layout(rect=[0.05, 0.05, 0.95, 0.95]); plt.show()
    return None




def plot_differential(vec,
    shape = 'v', names = 'txyz', graph = 'all',
    oneout = False):

    s = 0; ys = 0
    nv = len(list(vec.values())) # var input may be useless
    pp = [[0, i] for i in range(1, nv)] \
                + list(it.combinations(range(1, nv), 2)) # plot keys
    npp = len(pp) # number of plots

    vnames = 'txyz'
    if graph == 'all': graph = range(npp)
    else: npp = len(graph)

    if oneout is False: # fixing plot
        for el in range(nv):
            vec[el] = vec[el][1:]

    for left, right in pp:
        s += 1
        if s-1 not in graph: continue
        ys += 1
        plt.subplot(*(npp, 1, ys) if shape == 'v' else (1, npp, ys))
        plt.xlabel(r'$'+vnames[left]+r'$')
        plt.ylabel(r'$'+vnames[right]+r'$')
        plt.plot(vec[left], vec[right], color = '#3c78f0')

    return None