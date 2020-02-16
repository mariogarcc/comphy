# Author: Mario García Cajade

# --------------------------------------------------------------------------- #

# program setup
import numpy as np
import matplotlib.pyplot as plt
import _tkinter
TclError = _tkinter.TclError

plt.rc('text', usetex = True)

# computation parameters
slices = 20
itern = 1000
plot_frequency = 0.1

# differentiation parameters
deltat = 0.001
deltax = 0.1

# problem parameters
alpha = 1

# helper variable
s = alpha*deltat/deltax**2

# grid creation with initial conditions
tpprev = np.zeros(slices+1); tprev = np.zeros(slices+1); tnew = np.zeros(slices+1)

tpprev[0] = 5; tprev[0] = 5
tpprev[slices] = 10; tprev[slices] = 10

# computation
for r in range(itern):

    # next row computation
    for j in range(1, slices):
        tnew[j] = (2*s*(tprev[j+1] - 2*tprev[j] + tprev[j-1]) + 4*tprev[j] - tpprev[j])/3

    # apply boundary conditions
    tnew[0] = 5; tnew[slices] = 10

    # reset row assignments
    for i in range(0, slices+1):
        tpprev[i] = tprev[i]
        tprev[i] = tnew[i]

    # plot solution
    if int(r % (1/plot_frequency)) == 0:
        try:
            plt.figure(1)
            plt.title(r"$\frac{\partial T}{\partial t} = \alpha\:\frac{\partial^{2} T}{\partial x^{2}}$", fontsize = 16)
            plt.plot([j*deltax for j in range(slices+1)], tnew)
            plt.pause(0.1)
            plt.show
        except TclError:
            quit()

# await close
input("press ENTER to continue")
plt.close()

    