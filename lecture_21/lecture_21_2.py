# def L_xx(arr, i): return (1


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

tprev = tpprev = np.zeros(slices+1)
tprev[1:5] = tpprev[1:5] = 1 # initial conditions
# tprev[0] = 0
# tprev[slices] = 10

tnew = np.zeros(slices+1)

# # ex4
amat = np.diag([1]+[ 1+2*s]*(slices-1)+[1])         \
     + np.diag([0]+[-s-c/2]*(slices-1)+[ ], k = 1)  \
     + np.diag([ ]+[-s+c/2]*(slices-1)+[0], k = -1)

# # ex5
amat = np.diag([1]+[     1+s]*(slices-1)+[1])         \
     + np.diag([0]+[-s/2+c/4]*(slices-1)+[ ], k = 1)  \
     + np.diag([ ]+[-s/2-c/4]*(slices-1)+[0], k = -1)

bmat = np.diag([1]+[     1-s]*(slices-1)+[1])         \
     + np.diag([0]+[+s/2-c/4]*(slices-1)+[ ], k = 1)  \
     + np.diag([ ]+[+s/2+c/4]*(slices-1)+[0], k = -1)

iamat = np.linalg.inv(amat)

iden = np.identity(len(iamat))

for r in range(itern):

    # for i in range(1, slices):
        # ex1
        # tnew[i] = tprev[i] + s*(tprev[i-1] - 2*tprev[i] + tprev[i+1]) - c/2*(tprev[i+1] - tprev[i-1])
        # ex2
        # tnew[i] = tprev[i] + s*(tprev[i-1] - 2*tprev[i] + tprev[i+1]) - c/2*(tprev[i] - tprev[i-1])
        # ex3
        # tnew[i] = (tpprev[i] + 2*s*(tprev[i-1] - tpprev[i] + tprev[i+1]) - 2*c/2*(tprev[i+1] - tprev[i-1]))/(1+2*s)

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