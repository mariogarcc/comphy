# Author: Mario García Cajade

# --------------------------------------------------------------------------- #

import matplotlib.pyplot as plt

# du/dt = u*(1-v)
# dv/dt = alpha*v*(u-1)

alpha = 1

def inct(dt, *o):
    return dt

def incu(dt, t, u, v):
    return dt * u*(1-v)

def incv(dt, t, u, v, alpha = alpha):
    return dt * alpha*v*(u-1)

def runge_kutta_differentiate(w, order = 4, delta = 1e-3,
        bounds = None, itern = 1e3):
    bounds = bounds or [0]*len(w)
    itern = int(itern)

    var = bounds
    vec = [[v] for v in var]

    for n in range(itern):
        pvar = [v for v in var] # copy the old values from the variables
        k = dict()

        for i in range(len(var)): # iterate through every variable
            k[i] = dict()
            k[i][0] = w[i](*[delta]+[pvar[j] for j in range(len(pvar))])
            # make k1

            for o in range(1, order):
                div = (1*(1+(o%3 != 0))) # 1, 2, 2, 1
                tel = delta/div # deltat for each kn
                kel = k[i][o-1]/div # kn uses the previous k/(1, 2, 2, 1)
                k[i][o] = w[i](*[delta+tel]+[pvar[j]+kel \
                    for j in range(len(pvar))]) # compute the new k

            var[i] += sum(k[i][o]/(3*(1+(o%3 == 0))) for o in range(order))
            # sum the k's to the variable to compute the new value
            vec[i].append(var[i])
            # make vector for later plotting

    # ---- Plot u, v ----- #
    plt.figure()
    plt.plot(vec[1], vec[2])
    plt.show()
    # -------------------- #

    return None

runge_kutta_differentiate([inct, incu, incv], delta = 1e-2,
    bounds = [0, 0.5, 0.5], itern = int(1e4))