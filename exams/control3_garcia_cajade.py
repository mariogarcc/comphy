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
u = 1

# helper variables
s = alpha*deltat/deltax**2
c = u*deltat/deltax

# grid creation
tpprev = np.zeros(slices+1); tprev = np.zeros(slices+1); tnew = np.zeros(slices+1)
# with initial conditions
tpprev[5:10] = 10; tprev[5:10] = 10; tnew[5:10] = 10

"""
Truncation error analysis shows that the
third order derivative term can be negated choosing
deltax**4/deltat**2 = 12*alpha**2
which, simplifying, results in
deltax = sqrt(sqrt(12)*alpha*deltat)
"""
deltax = np.sqrt(np.sqrt(12)*alpha*deltat)

# computation
for r in range(itern):

    # next row computation
    for j in range(1, slices):
        tnew[j] = (2*s*(tprev[j+1] - tpprev[j] + tprev[j-1]) - c*(tprev[j+1] - tprev[j-1]) + tpprev[j])/(1+2*s)
    
    # dufort-frankel normalization
    tnew = (tnew+tprev)/2

    # apply boundary conditions
    tnew[0] = tnew[1]; tnew[slices] = tnew[slices-1]

    # reset row assignments
    for i in range(0, slices+1):
        tpprev[i] = tprev[i]
        tprev[i] = tnew[i]

    # plot solution
    if int(r % int(1/plot_frequency)) == 0:
        try:
            plt.figure(1)
            plt.title(r"$\frac{\partial T}{\partial t} + u\:\frac{\partial T}{\partial x} - \alpha\:\frac{\partial^{2} T}{\partial x^{2}} = 0$", fontsize = 16)
            plt.plot([j*deltax for j in range(slices+1)], tnew)
            plt.pause(0.1)
            plt.show
        except TclError:
            quit()

# await close
input("press ENTER to continue")
plt.close()

    