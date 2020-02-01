# 21, 22

import numpy as np
import matplotlib.pyplot as plt
import _tkinter
TclError = _tkinter.TclError

slices = 20
itern = 1000
plot_frequency = 0.05

deltat = 1e-3
deltax = 1e-1

u = 1

c = u*deltat/deltax

tprev = tpprev = np.zeros(slices+1)
tprev[1:5] = tpprev[1:5] = 1 # initial conditions
# tprev[0] = 0
# tprev[slices] = 10

tnew = np.zeros(slices+1)

plt.close('all')
plt.figure(1)
plt.pause(0.1)

# ex4
amat = np.diag([1]+[   1]*(slices-1)+[1])         \
     + np.diag([0]+[-c/2]*(slices-1)+[ ], k = 1)  \
     + np.diag([ ]+[+c/2]*(slices-1)+[0], k = -1)

# ex5
amat = np.diag([1]+[   1]*(slices-1)+[1])         \
     + np.diag([0]+[-c/4]*(slices-1)+[ ], k = 1)  \
     + np.diag([ ]+[+c/4]*(slices-1)+[0], k = -1)

bmat = np.diag([1]+[   1]*(slices-1)+[1])         \
     + np.diag([0]+[+c/4]*(slices-1)+[ ], k = 1)  \
     + np.diag([ ]+[-c/4]*(slices-1)+[0], k = -1)

iamat = np.linalg.inv(amat)

iden = np.identity(len(iamat))

for r in range(itern):
    # for i in range(1, slices):
        # ex1
        # tnew[i] = tprev[i] + c*(tprev[i+1] - tprev[i-1])
        # ex2
        # tnew[i] = tprev[i] - c*(tprev[i] - tprev[i-1]) # exact with c=1
        # ex3
        # tnew[i] = tpprev[i] - c*(tprev[i+1] - tprev[i-1])

    # ex4
    # intermediary = iden @ tprev
    # ex5
    intermediary = bmat @ tprev

    tnew = iamat @ intermediary

    for i in range(0, slices+1):
        tpprev[i] = tprev[i]
        tprev[i] = tnew[i]

    if r % int(1/plot_frequency) == 0:
        try:
        # catch for except closing plots
            plt.figure(1)
            plt.plot(tprev)
            plt.pause(0.001)
            plt.show
        except TclError:
            quit()

input('press ENTER to close\n')
plt.close