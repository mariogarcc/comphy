import numpy as np
import itertools as it
import matplotlib.pyplot as plt


def euler_differentiate(w, bounds = None, delta = 1e-3, itern = 1e3,
    plot = True, title = None,
    shape = 'v', figsize = (10, 6), figshape = None, fontsize = 16,
    names = 'txyz', graph = 'all',
    oneout = False, force = False):

    if bounds is None:
        bounds = [0]*len(w)

    if not force and itern >= 1e9:
        raise OverflowError("number of iterations is too big: {!s}" + "\n" + \
            "you can ignore this error by setting the `force` kwarg to `False`"
            .format(itern))

    itern = int(itern)

    var = bounds
    vec = [[v] for v in var] if plot else None

    if plot:
        plt.rc('text', usetex = True)
        plt.rc('axes', labelsize = fontsize)
        plt.rc('figure', titlesize = fontsize)
        plt.rc('font', family = 'serif')

        if graph == 'all': agraph = range(len(list(
            it.combinations(range(len(vec)), 2))))
        else: agraph = graph

        figshape = figshape or (
            (len(agraph), 1) if shape == 'v' else (1, len(agraph)))
        
        fig, ax = plt.subplots(figshape[0], figshape[1], figsize = figsize)
        fig.suptitle(title, x = 0.525, y = 0.975)

    for n in range(1, itern+1): # iterate method n times

        pvar = [v for v in var]

        for i,_ in enumerate(var): # compute new variables
            var[i] += w[i](*[delta]+[pvar[j] for j in range(len(pvar))])

            if plot: vec[i].append(var[i])

        if plot and n % int(np.sqrt(itern)) == 0: # best performance
            plot_differential(vec, fig, ax,
                shape = shape, names = names, graph = graph,
                oneout = oneout)

            for i in range(len(vec)): # resetting vectors for performance
                vec[i] = [vec[i][-1]]

            oneout = True # first item has already been removed (first plot)

    if plot: plt.tight_layout(rect=[0.05, 0.05, 0.95, 0.95]); plt.show()
    return None




def range_kutta_differentiate(w, order = 4,
    bounds = None, delta = 1e-3, itern = 1e3,
    plot = True, title = None,
    shape = 'v', figsize = (10, 6), figshape = None, fontsize = 16,
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

    var = bounds
    vec = [[v] for v in var] if plot else None

    if plot:
        plt.rc('text', usetex = True)
        plt.rc('axes', labelsize = fontsize)
        plt.rc('figure', titlesize = fontsize)
        plt.rc('font', family = 'serif')

        if graph == 'all': agraph = range(len(list(
            it.combinations(range(len(vec)), 2))))
        else: agraph = graph

        figshape = figshape or (
            (len(agraph), 1) if shape == 'v' else (1, len(agraph)))
        
        fig, ax = plt.subplots(figshape[0], figshape[1], figsize = figsize)
        fig.suptitle(title, x = 0.525, y = 0.975)

    for n in range(1, itern+1):

        pvar = [v for v in var]
        k = dict()

        for i,_ in enumerate(var):

            k[i] = dict()
            k[i][0] = w[i](*[delta]+[pvar[j] for j in range(len(pvar))])

            for o in range(1, order):
                div = (1*(1+(o%3 != 0))) # 1, 2, 2, 1
                tel = delta/div
                kel = k[i][o-1]/div
                k[i][o] = w[i](*[delta+tel]+[pvar[j]+kel \
                    for j in range(len(pvar))])

            var[i] += sum(k[i][o]/(3*(1+(o%3 == 0))) \
                for o in range(order)) # k1/6 + k2/3 + k3/3 + k4/6

            if plot: vec[i].append(var[i])

        if plot and (n % int(np.sqrt(itern)) == 0 or n == itern): # performance
            plot_differential(vec, fig, ax,
                shape = shape, names = names, graph = graph,
                oneout = oneout)

            for i in range(len(vec)): # resetting vectors for performance
                vec[i] = [vec[i][-1]]

            oneout = True # first item has already been removed (first plot)

    if plot: plt.tight_layout(rect=[0.00, 0.05, 1.00, 0.95]); plt.show()
    # rect is left, bottom, right, top
    return None




def plot_differential(vec, fig, ax,
    shape = 'v', names = 'txyz', graph = 'all',
    oneout = False):

    s = 0; ys = 0
    nv = len(vec)
    pp = list(it.combinations(range(nv), 2)) # plot keys

    vnames = names
    if graph == 'all': graph = range(len(pp))

    if oneout is False: # fixing plot
        for el in range(nv):
            vec[el] = vec[el][1:]

    for left, right in pp:
        s += 1
        if s-1 not in graph: continue
        ys += 1
        if type(ax) == np.ndarray:
            if type(ax[0]) == np.ndarray:
                print("figshape not yet supported (use None)")
            else:
                ax[ys-1].set_xlabel(r'$'+vnames[left]+r'$')
                ax[ys-1].set_ylabel(r'$'+vnames[right]+r'$')
                ax[ys-1].plot(vec[left], vec[right], color = '#3c78f0')
        else:
            ax.set_xlabel(r'$'+vnames[left]+r'$')
            ax.set_ylabel(r'$'+vnames[right]+r'$')
            ax.plot(vec[left], vec[right], color = '#3c78f0')

    return None




def euler_differentiate_mod(w, bounds = None, delta = 1e-3, itern = 1e3,
    plot = True, title = None,
    shape = 'v', figsize = (10, 6), figshape = None, fontsize = 16,
    names = 'txyz', graph = 'all',
    oneout = False, force = False,
    tols = [10, 0.1], step_mults = [0.1, 10],
    max_delta = 1, min_delta = 1e-9,
    verbose = False):

    if bounds is None:
        bounds = [0]*len(w)

    if not force and itern >= 1e9:
        raise OverflowError("number of iterations is too big: {!s}" + "\n" + \
            "you can ignore this error by setting the `force` kwarg to `False`"
            .format(itern))

    itern = int(itern)

    var = bounds
    vec = [[v] for v in var] if plot else None

    if plot:
        plt.rc('text', usetex = True)
        plt.rc('axes', labelsize = fontsize)
        plt.rc('figure', titlesize = fontsize)
        plt.rc('font', family = 'serif')

        if graph == 'all': agraph = range(len(list(
            it.combinations(range(len(vec)), 2))))
        else: agraph = graph

        figshape = figshape or (
            (len(agraph), 1) if shape == 'v' else (1, len(agraph)))

        fig, ax = plt.subplots(figshape[0], figshape[1], figsize = figsize)
        fig.suptitle(title, x = 0.525, y = 0.975)

    n = 1
    while n < itern:

        pvar = [v for v in var]

        for i,_ in enumerate(var): # compute new variables
            var[i] += w[i](*[delta]+[pvar[j] for j in range(len(pvar))])

            if plot: vec[i].append(var[i])

        if plot and n % int(np.sqrt(itern)) == 0: # best performance
            plot_differential(vec, fig, ax,
                shape = shape, names = names, graph = graph,
                oneout = oneout)

            for i in range(len(vec)): # resetting vectors for performance
                vec[i] = [vec[i][-1]]

            oneout = True # first item has already been removed (first plot)

        fchanges = [abs(var[i]-pvar[i]) for i in range(1, len(var))]
        fd = max(fchanges)

        if verbose: print(f"delta = {delta}")
        try:
            if len(check) > 2:
                n += 1
        except:
            check = []
        if fd > tols[0]:
            check.append(n)
            delta *= step_mults[0] if delta >= min_delta else 1
        elif fd < tols[1]:
            check.append(n)
            delta *= step_mults[1] if delta <= max_delta else 1
        else:
            check = []
            n += 1

    if plot:
        plt.tight_layout(rect=[0.05, 0.05, 0.95, 0.95])
        plt.show()

    return None
