# Author: Mario García Cajade
# Date: 21/03/2019

# Problem set for topic 07: ordinary differential equations


# --------------------------Packages-------------------------- #

import numpy as np
import itertools as it
import matplotlib.pyplot as plt

# ------------------------------------------------------------ #

# --------------------Function definitions-------------------- #

def redact_ex(ex_str, n = '', sep = '\n', end = '\n\n'):
    print('', 'EXERCISE {no:d}:'.format(
        no = int(n) if not isinstance(n, str) else n), ex_str,
        sep = sep, end = end)
    return None




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
        try:
            ax[ys-1].set_xlabel(r'$'+vnames[left]+r'$')
            ax[ys-1].set_ylabel(r'$'+vnames[right]+r'$')
            ax[ys-1].plot(vec[left], vec[right], color = '#3c78f0')
        except:
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

# ------------------------------------------------------------ #

# ----------------------- Problem no.1 ----------------------- #

EXERCISE_1 = """\
Make a program that is able to graphically solve the equation
d\u00B2x/dt\u00B2 + \u03C9_0\u00B2x = 0 using:
+ the Euler method
+ the Range-Kutta method of order 2
+ the Range-Kutta method of order 4
Comment on the effects of \u0394t over the obtained solutions
(analyze the methods' stability with regards to the \u0394t used).\
"""

redact_ex(EXERCISE_1, 1)


# dx/dt = y
# dy/dt = -omega_0**2*x

omega_0 = 1

def inct(dt, *o):   
    return dt

def incx(dt, t, x, y):
    return dt * y

def incy(dt, t, x, y, omega_0 = omega_0):
    return dt * (-omega_0**2*x)

print("Computing Euler method...", end='\n\n')
euler_differentiate([inct, incx, incy], bounds = [0, 1, -1],
    delta = 1e-2, itern = 1e4, graph = [1, 2],
    title = r"Euler method for function"
        + r"$\:\:\frac{d^2x}{dt^2} + \omega_0^2 x = 0$")

print("Computing Range-Kutta method of order 2...", end='\n\n')
range_kutta_differentiate([inct, incx, incy], bounds = [0, 1, -1],
    delta = 1e-2, order = 2, itern = 1e4, graph = [1, 2],
    title = r"Range-Kutta method of order 2 for function"
        + r"$\:\:\frac{d^2x}{dt^2} + \omega_0^2 x = 0$")

print("Computing Range-Kutta method of order 4...", end='\n\n')
range_kutta_differentiate([inct, incx, incy], bounds = [0, 1, -1],
    delta = 1e-2, order = 4, itern = 1e4, graph = [1, 2],
    title = r"Range-Kutta method of order 4 for function"
        + r"$\:\:\frac{d^2x}{dt^2} + \omega_0^2 x = 0$")

# ------------------------------------------------------------ #

# ----------------------- Problem no.2 ----------------------- #

EXERCISE_2 = """\
Make a program that is able to graphically solve the equation
d\u00B2x/dt\u00B2 + b dx/dt + \u03C9_0\u00B2 x = F cos(x) using:
+ the Euler method
+ the Range-Kutta method of order 2
+ the Range-Kutta method of order 4
Comment on the effects of \u0394t over the obtained solutions
(analyze the methods' stability with regards to the \u0394t used).\
"""

redact_ex(EXERCISE_2, 2)


# dx/dt = y
# dy/dt = -b*y - omega_0**2*x + f*np.cos(omega*t)

b = 1/2; omega_0 = 4; f = 1; omega = 2

def inct(dt, *o):
    return dt

def incx(dt, t, x, y):
    return dt * y

def incy(dt, t, x, y, b = b, omega_0 = omega_0, f = f, omega = omega):
    return dt * (-b*y - omega_0**2*x + f*np.cos(omega*t))

print("Computing Euler method...", end='\n\n')
euler_differentiate([inct, incx, incy], bounds = [0, 0, 1],
    delta = 1e-2, itern = 1e4, graph = [1, 2],
    title = r"Euler method for function"
        + r"$\:\:\frac{d^2x}{dt^2} + b \frac{dx}{dt} + \omega_0^2 x = F \cos(\omega t)$")

print("Computing Range-Kutta method of order 2...", end='\n\n')
range_kutta_differentiate([inct, incx, incy], bounds = [0, 0, 1],
    delta = 1e-2, order = 2, itern = 1e4, graph = [1, 2],
    title = r"Range-Kutta method of order 2 for function"
        + r"$\:\:\frac{d^2x}{dt^2} + b \frac{dx}{dt} + \omega_0^2 x = F \cos(\omega t)$")

print("Computing Range-Kutta method of order 4...", end='\n\n')
range_kutta_differentiate([inct, incx, incy], bounds = [0, 0, 1],
    delta = 1e-2, order = 4, itern = 1e4, graph = [1, 2],
    title = r"Range-Kutta method of order 4 for function"
        + r"$\:\:\frac{d^2x}{dt^2} + b \frac{dx}{dt} + \omega_0^2 x = F \cos(\omega t)$")

omega = omega_0
def incy(dt, t, x, y, b = b, omega_0 = omega_0, f = f, omega = omega):
    return dt * (-b*y - omega_0**2*x + f*np.cos(omega*t))

euler_differentiate([inct, incx, incy], bounds = [0, 0, 1],
    delta = 1e-2, itern = 1e4, graph = [1, 2],
    title = r"Euler method for function"
        + r"$\:\:\frac{d^2x}{dt^2} + b \frac{dx}{dt} + \omega_0^2 x = F \cos(\omega_0 t)$")

# When omega_0 == omega, movement is a single sinusoidal wave since the start
# rather than a combination of two, as we can see in the early stages
# of the plots where omega_0 != omega.

# ------------------------------------------------------------ #

# ----------------------- Problem no.3 ----------------------- #

EXERCISE_3 = """\
Make a program that is able to graphically solve the equation
dP/dt = rP * (1 - P/k) using:
+ the Euler method
+ the Range-Kutta method of order 2
+ the Range-Kutta method of order 4
Comment on the effects of \u0394t over the obtained solutions
(analyze the methods' stability with regards to the \u0394t used).\
"""

redact_ex(EXERCISE_3, 3)


# dp/dt = r*p * (1-p/k)

r = 1; k = 1
def incp(dt, t, p, r = r, k = k):
    return dt * r*p * (1-p/k)

print("Computing Euler method...", end='\n\n')
euler_differentiate([inct, incp], bounds = [0, 10],
    delta = 1e-3, itern = 3e3,
    title = r"Euler method for function"
        + r"$\:\:\frac{dP}{dt} = r\;P \: \left( 1 - \frac{P}{k} \right)$")

print("Computing Range-Kutta method of order 2...", end='\n\n')
range_kutta_differentiate([inct, incp], bounds = [0, 10], order = 2,
    delta = 1e-3, itern = 3e3,
    title = r"Range-Kutta method of order 2 for function"
        + r"$\:\:\frac{dP}{dt} = r\;P \: \left( 1 - \frac{P}{k} \right)$")

print("Computing Range-Kutta method of order 4...", end='\n\n')
range_kutta_differentiate([inct, incp], bounds = [0, 10], order = 4,
    delta = 1e-3, itern = 3e3,
    title = r"Range-Kutta method of order 4 for function"
        + r"$\:\:\frac{dP}{dt} = r\;P \: \left( 1 - \frac{P}{k} \right)$")

# ------------------------------------------------------------ #

# ----------------------- Problem no.4 ----------------------- #

EXERCISE_4 = """\
Make a program that is able to graphically solve the set of equations
{
    dx/dt = \u03C3 (y-x)
    dy/dt = r x - y - x z
    dz/dt = x y - b z
}
(Lorenz attractor) using:
+ the Euler method
+ the Range-Kutta method of order 2
+ the Range-Kutta method of order 4
Comment on the effects of \u0394t over the obtained solutions
(analyze the methods' stability with regards to the \u0394t used).\
"""

redact_ex(EXERCISE_4, 4)


# dx/dt
# dy/dt
# dz/dt

sigma = 3; r = 26.5; b = 1
ip = [0, 0, 1, 0] # initial parameters

def inct(dt, *o):   
    return dt

def incx(dt, t, x, y, z, sigma = sigma):
    return dt * sigma*(y-x)

def incy(dt, t, x, y, z, r = r):
    return dt * (r*x - y - x*z)

def incz(dt, t, x, y, z, b = b):
    return dt * (x*y - b*z)


print("Computing Euler method...", end='\n\n')
euler_differentiate([inct, incx, incy, incz], bounds = ip,
    delta = 1e-2, itern = 1e4, graph = [0, 3],
    title = r"Euler method for the Lorenz attractor")

print("Computing Range-Kutta method of order 2...", end='\n\n')
range_kutta_differentiate([inct, incx, incy, incz], bounds = ip, order = 2,
    delta = 1e-2, itern = 1e4, graph = [0, 3],
    title = r"Range-Kutta method of order 2 for the Lorenz attractor")

print("Computing Range-Kutta method of order 4...", end='\n\n')
range_kutta_differentiate([inct, incx, incy, incz], bounds = ip, order = 4,
    delta = 1e-2, itern = 1e4, graph = [0, 3],
    title = r"Range-Kutta method of order 4 for the Lorenz attractor")

# ------------------------------------------------------------ #

# ----------------------- Problem no.5 ----------------------- #

EXERCISE_5 = """\
Make a program that is able to graphically solve any of the equations
proposed beforehand using a variable-step integration method.
(Chose the population equation.)\
"""

redact_ex(EXERCISE_5, 5)


# dp/dt = r*p * (1-p/k)

r = 1; k = 1
def incp(dt, t, p, r = r, k = k):
    return dt * r*p * (1-p/k)

print("Computing Euler method with variable-step...", end='\n\n')
euler_differentiate_mod([inct, incp], bounds = [0, 10],
    delta = 1e-2, itern = 1e2,
    step_mults = [0.5, 2], tols = [0.5, 0.1],
    max_delta = 1, min_delta = 1e-6, # verbose = True,
    title = r"Euler method for function"
        + r"$\:\:\frac{dP}{dt} = r\;P \: \left( 1 - \frac{P}{k} \right)\:\:$"
        + r"with variable-step")

# set kwarg `verbose` to True to see how delta varies

# ------------------------------------------------------------ #



# Released under CC0