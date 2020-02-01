# def L_xx(arr, i): return (1

import copy
import numpy as np
import matplotlib.pyplot as plt
import _tkinter
TclError = _tkinter.TclError

slices = 20
itern = 500
plot_frequency = 0.05

deltat = 1e-3
deltax = 1e-1

alpha = 1
u = 1

s = alpha*deltat/deltax**2
c = u*deltat/deltax

sx = sy = s
deltay = deltax

tprev = np.zeros((slices+1, slices+1))
for r in range(8, 12):
    tprev[r,8:12] = 1 # initial conditions

# tprev[0,:] = np.zeros(slices+1)
# tprev[slices,:] = np.array([1]*(slices+1))

# tprev[:,0] = np.zeros(slices+1)
# tprev[:,slices] = np.array([1]*(slices+1))

tnew = tast = np.zeros((slices+1, slices+1))

#####
camat = np.diag([1]+[ 1+sx]*(slices-1)+[1])         \
      + np.diag([0]+[-sx/2]*(slices-1)+[ ], k = 1)  \
      + np.diag([ ]+[-sx/2]*(slices-1)+[0], k = -1)


ramat = np.diag([1]+[ 1+sy]*(slices-1)+[1])         \
      + np.diag([0]+[-sy/2]*(slices-1)+[ ], k = 1)  \
      + np.diag([ ]+[-sy/2]*(slices-1)+[0], k = -1)

icamat = np.linalg.inv(camat)
iramat = np.linalg.inv(ramat)



for it in range(itern):

    for c in range(1, slices):
        cbarr = np.array(
                [0] \
              + [((+sy/2)*tprev[i,c-1] + (1-sy)*tprev[i,c] + (+sy/2)*tprev[i,c+1]) \
                    for i in range(1, slices)] \
              + [0]
              )

        tast[:,c] = icamat @ cbarr

    for r in range(1, slices):
        rbarr = np.array(
                [0] \
              + [((+sx/2)*tast[r-1,j] + (1-sx)*tast[r,j] + (+sx/2)*tast[r+1,j]) \
                    for j in range(1, slices)] \
              + [0]
              )

        tnew[r,:] = iramat @ rbarr


    # boundary
    # tnew[0,:] = np.zeros(slices+1)
    # tnew[slices,:] = np.array([1]*(slices+1))

    # tnew[:,0] = np.zeros(slices+1)
    # tnew[:,slices] = np.array([1]*(slices+1))

    # copying
    tprev = copy.deepcopy(tnew)

    # plotting
    if it % int(1/plot_frequency) == 0:
        try:
        # catch for except closing plots
            plt.figure(1)
            # plt.pcolor(tnew[1:slices,1:slices])
            plt.pcolor(tnew)
            plt.pause(0.001)
            plt.show
        except TclError:
            quit()

input('press ENTER to close\n')
plt.close

