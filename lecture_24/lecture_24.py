# def L_xx(arr, i): return (1

import copy
import numpy as np
import matplotlib.pyplot as plt
import _tkinter
TclError = _tkinter.TclError

slices = 20
itern = 1000
plot_frequency = 0.05

deltat = 1e-3
deltax = 1e-1

alpha = 1
u = 1

s = alpha*deltat/deltax**2
c = u*deltat/deltax

sx = sy = s
deltay = deltax

tprev = tpprev = np.zeros((slices+1, slices+1))
for r in range(8, 12):
    tprev[r,8:12] = tpprev[r,8:12] = 1 # initial conditions

tprev[0,:] = tpprev[0,:] = np.zeros(slices+1)
tprev[slices,:] = tpprev[slices,:] = np.array([10]*(slices+1))

tprev[:,0] = tpprev[:,0] = np.zeros(slices+1)
tprev[:,slices] = tpprev[:,slices] = np.array([10]*(slices+1))

tnew = np.zeros((slices+1, slices+1))


for i in range(itern):
    for r in range(1, slices):
        for c in range(1, slices):
            tnew[c, r] = tprev[c, r] \
                       + sx*(tprev[c-1, r] - 2*tprev[c, r] + tprev[c+1, r]) \
                       + sy*(tprev[c, r-1] - 2*tprev[c, r] + tprev[c, r+1])

    tnew[0,:] = tprev[0,:] = np.zeros(slices+1)
    tnew[slices,:] = tprev[slices,:] = np.array([10]*(slices+1))

    tnew[:,0] = tprev[:,0] = np.zeros(slices+1)
    tnew[:,slices] = tprev[:,slices] = np.array([10]*(slices+1))

    tprev = copy.deepcopy(tnew)
    tpprev = copy.deepcopy(tprev)

    if i % int(1/plot_frequency) == 0:
        try:
        # catch for except closing plots
            plt.figure(1)
            plt.pcolor(tnew)
            # plt.pcolor(tnew[1:slices,1:slices])
            plt.pause(0.001)
            plt.show
        except TclError:
            quit()

input('press ENTER to close\n')
plt.close

