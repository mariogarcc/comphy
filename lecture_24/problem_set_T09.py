# Author: Mario García Cajade
# Date: 08/05/2019

# Problem set for topic 09: convection and transport equation in 1d and 2d


# ------------------------- Packages ------------------------- #

import copy
import numpy as np
import matplotlib.pyplot as plt
import _tkinter
TclError = _tkinter.TclError

# ------------------------------------------------------------ #

# ------------------- Function definitions ------------------- #

def ask_continue():
    response = input("Continue? (y/n)\n")
    if response.lower() not in ('y', 'n'):
        return ask_continue()
    if response.lower() == 'n':
        return quit()

# ------------------ Computation parameters ------------------ #

slices = 20
itern = 1000
plot_frequency = 0.05

# ------------------------------------------------------------ #
print()
# ----------------------- Problem no.1 ----------------------- #

print(f"Exercise {1} follows.")
ask_continue()

deltat = 1e-3
deltax = 1e-1
u = 1
c = u*deltat/deltax

tprev = np.zeros(slices+1)
tprev[4:6] = 1

tnew = np.zeros(slices+1)

for r in range(itern):
    for i in range(1, slices):
        tnew[i] = tprev[i] + c*(tprev[i+1] - tprev[i-1])

    for i in range(0, slices+1):
        tprev[i] = tnew[i]

    if r % int(1/plot_frequency) == 0:
        try:
            plt.figure(1)
            plt.plot(tnew)
            plt.pause(0.001)
            plt.show
        except TclError:
            pass

input('press ENTER to close\n')
plt.close

# ------------------------------------------------------------ #

# ----------------------- Problem no.2 ----------------------- #

print(f"Exercise {2} follows.")
ask_continue()

deltat = 1e-3
deltax = 1e-1
u = 1
c = u*deltat/deltax

tprev = np.zeros(slices+1)
tprev[1:5] = 1

tnew = np.zeros(slices+1)

for r in range(itern):
    for i in range(1, slices):
        tnew[i] = tprev[i] - c*(tprev[i] - tprev[i-1]) # exact with c=1

    for i in range(0, slices+1):
        tprev[i] = tnew[i]

    if r % int(1/plot_frequency) == 0:
        try:
            plt.figure(1)
            plt.plot(tnew)
            plt.pause(0.001)
            plt.show
        except TclError:
            pass

input('press ENTER to close\n')
plt.close

# ------------------------------------------------------------ #

# ----------------------- Problem no.3 ----------------------- #

print(f"Exercise {3} follows.")
ask_continue()

deltat = 1e-3
deltax = 1e-1
u = 1
c = u*deltat/deltax

tprev = tpprev = np.zeros(slices+1)
tprev[4:6] = tpprev[4:6] = 1

tnew = np.zeros(slices+1)

for r in range(itern):
    for i in range(1, slices):
        tnew[i] = tpprev[i] - c*(tprev[i+1] - tprev[i-1])

    tnew = (tnew+tprev)/2

    for i in range(0, slices+1):
        tpprev[i] = tprev[i]
        tprev[i] = tnew[i]

    if r % int(1/plot_frequency) == 0:
        try:
            plt.figure(1)
            plt.plot(tnew)
            plt.pause(0.001)
            plt.show
        except TclError:
            pass

input('press ENTER to close\n')
plt.close

# ------------------------------------------------------------ #

# ----------------------- Problem no.4 ----------------------- #

print(f"Exercise {4} follows.")
ask_continue()

deltat = 1e-3
deltax = 1e-1
u = 1
c = u*deltat/deltax

tprev = np.zeros(slices+1)
tprev[4:6] = 1

tnew = np.zeros(slices+1)

amat = np.diag([1]+[   1]*(slices-1)+[1])         \
     + np.diag([0]+[-c/2]*(slices-1)+[ ], k = 1)  \
     + np.diag([ ]+[+c/2]*(slices-1)+[0], k = -1)

iamat = np.linalg.inv(amat)
iden = np.identity(len(iamat))

for r in range(itern):

    intermediary = iden @ tprev
    tnew = iamat @ intermediary

    for i in range(0, slices+1):
        tprev[i] = tnew[i]

    if r % int(1/plot_frequency) == 0:
        try:
            plt.figure(1)
            plt.plot(tnew)
            plt.pause(0.001)
            plt.show
        except TclError:
            pass

input('press ENTER to close\n')
plt.close

# ------------------------------------------------------------ #

# ----------------------- Problem no.5 ----------------------- #

print(f"Exercise {5} follows.")
ask_continue()

deltat = 1e-3
deltax = 1e-1
u = 1
c = u*deltat/deltax

tprev = np.zeros(slices+1)
tprev[4:6] = 1

tnew = np.zeros(slices+1)

amat = np.diag([1]+[   1]*(slices-1)+[1])         \
     + np.diag([0]+[-c/4]*(slices-1)+[ ], k = 1)  \
     + np.diag([ ]+[+c/4]*(slices-1)+[0], k = -1)

bmat = np.diag([1]+[   1]*(slices-1)+[1])         \
     + np.diag([0]+[+c/4]*(slices-1)+[ ], k = 1)  \
     + np.diag([ ]+[-c/4]*(slices-1)+[0], k = -1)

iamat = np.linalg.inv(amat)

for r in range(itern):

    intermediary = bmat @ tprev
    tnew = iamat @ intermediary

    for i in range(0, slices+1):
        tprev[i] = tnew[i]

    if r % int(1/plot_frequency) == 0:
        try:
            plt.figure(1)
            plt.plot(tnew)
            plt.pause(0.001)
            plt.show
        except TclError:
            pass

input('press ENTER to close\n')
plt.close

# ------------------------------------------------------------ #

# ----------------------- Problem no.6 ----------------------- #

print(f"Exercise {6} follows.")
ask_continue()

deltat = 1e-3
deltax = 1e-1
alpha = 1
u = 1
s = alpha*deltat/deltax**2
c = u*deltat/deltax

tprev = np.zeros(slices+1)
tprev[4:6] = 1

tnew = np.zeros(slices+1)

for r in range(itern):
    for i in range(1, slices):
        tnew[i] = tprev[i] + s*(tprev[i-1] - 2*tprev[i] + tprev[i+1]) - c/2*(tprev[i+1] - tprev[i-1])

    for i in range(0, slices+1):
        tprev[i] = tnew[i]

    if r % int(1/plot_frequency) == 0:
        try:
            plt.figure(1)
            plt.plot(tnew)
            plt.pause(0.001)
            plt.show
        except TclError:
            pass

input('press ENTER to close\n')
plt.close

# ------------------------------------------------------------ #

# ----------------------- Problem no.7 ----------------------- #

print(f"Exercise {7} follows.")
ask_continue()

deltat = 1e-3
deltax = 1e-1
alpha = 1
u = 1
s = alpha*deltat/deltax**2
c = u*deltat/deltax

tprev = np.zeros(slices+1)
tprev[4:6] = 1

tnew = np.zeros(slices+1)

for r in range(itern):
    for i in range(1, slices):
        tnew[i] = tprev[i] + s*(tprev[i-1] - 2*tprev[i] + tprev[i+1]) - c/2*(tprev[i] - tprev[i-1])

    for i in range(0, slices+1):
        tprev[i] = tnew[i]

    if r % int(1/plot_frequency) == 0:
        try:
            plt.figure(1)
            plt.plot(tnew)
            plt.pause(0.001)
            plt.show
        except TclError:
            pass

input('press ENTER to close\n')
plt.close


# ------------------------------------------------------------ #

# ----------------------- Problem no.8 ----------------------- #

print(f"Exercise {8} follows.")
ask_continue()


deltat = 1e-3
deltax = 1e-1
alpha = 1
u = 1
s = alpha*deltat/deltax**2
c = u*deltat/deltax

tprev = tpprev = np.zeros(slices+1)
tprev[4:6] = tpprev[4:6] = 1

tnew = np.zeros(slices+1)

for r in range(itern):
    for i in range(1, slices):
        tnew[i] = (tpprev[i] + 2*s*(tprev[i-1] - tpprev[i] + tprev[i+1]) - 2*c/2*(tprev[i+1] - tprev[i-1]))/(1+2*s)

    tnew = (tnew+tprev)/2

    for i in range(0, slices+1):
        tpprev[i] = tprev[i]
        tprev[i] = tnew[i]

    if r % int(1/plot_frequency) == 0:
        try:
            plt.figure(1)
            plt.plot(tnew)
            plt.pause(0.001)
            plt.show
        except TclError:
            pass

input('press ENTER to close\n')
plt.close


# ------------------------------------------------------------ #

# ----------------------- Problem no.9 ----------------------- #

print(f"Exercise {9} follows.")
ask_continue()

deltat = 1e-3
deltax = 1e-1
alpha = 1
u = 1
s = alpha*deltat/deltax**2
c = u*deltat/deltax

tprev = np.zeros(slices+1)
tprev[4:6] = 1

tnew = np.zeros(slices+1)

amat = np.diag([1]+[ 1+2*s]*(slices-1)+[1])         \
     + np.diag([0]+[-s-c/2]*(slices-1)+[ ], k = 1)  \
     + np.diag([ ]+[-s+c/2]*(slices-1)+[0], k = -1)

iamat = np.linalg.inv(amat)
iden = np.identity(len(iamat))

for r in range(itern):

    intermediary = iden @ tprev
    tnew = iamat @ intermediary

    for i in range(0, slices+1):
        tprev[i] = tnew[i]

    if r % int(1/plot_frequency) == 0:
        try:
            plt.figure(1)
            plt.plot(tnew)
            plt.pause(0.001)
            plt.show
        except TclError:
            quit()

input('press ENTER to close\n')
plt.close

# ------------------------------------------------------------ #

# ----------------------- Problem no.10 ----------------------- #

print(f"Exercise {10} follows.")
ask_continue()


deltat = 1e-3
deltax = 1e-1
alpha = 1
u = 1
s = alpha*deltat/deltax**2
c = u*deltat/deltax

tprev = tpprev = np.zeros(slices+1)
tprev[4:6] = tpprev[4:6] = 1

tnew = np.zeros(slices+1)


amat = np.diag([1]+[     1+s]*(slices-1)+[1])         \
     + np.diag([0]+[-s/2+c/4]*(slices-1)+[ ], k = 1)  \
     + np.diag([ ]+[-s/2-c/4]*(slices-1)+[0], k = -1)

bmat = np.diag([1]+[     1-s]*(slices-1)+[1])         \
     + np.diag([0]+[+s/2-c/4]*(slices-1)+[ ], k = 1)  \
     + np.diag([ ]+[+s/2+c/4]*(slices-1)+[0], k = -1)

iamat = np.linalg.inv(amat)

for r in range(itern):

    intermediary = bmat @ tprev
    tnew = iamat @ intermediary

    for i in range(0, slices+1):
        tprev[i] = tnew[i]

    if r % int(1/plot_frequency) == 0:
        try:
            plt.figure(1)
            plt.plot(tnew)
            plt.pause(0.001)
            plt.show
        except TclError:
            quit()

input('press ENTER to close\n')
plt.close

# ------------------------------------------------------------ #

# ----------------------- Problem no.12 ----------------------- #

print(f"Exercise {12} follows.")
ask_continue()

itern = 500

deltat = 1e-3
deltax = 1e-1
alpha = 1
u = 1

s = alpha*deltat/deltax**2
c = u*deltat/deltax
deltay = deltax
sx = sy = s

tprev = tpprev = np.zeros((slices+1, slices+1))

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
            plt.figure(1)
            plt.pcolor(tnew[1:slices,1:slices])
            plt.pause(0.001)
            plt.show
        except TclError:
            quit()

input('press ENTER to close\n')
plt.close


# ------------------------------------------------------------ #

# ----------------------- Problem no.13 ----------------------- #

print(f"Exercise {13} follows.")
ask_continue()

itern = 500

deltat = 1e-3
deltax = 1e-1
alpha = 1
u = 1

s = alpha*deltat/deltax**2
c = u*deltat/deltax
deltay = deltax
sx = sy = s

tprev = np.zeros((slices+1, slices+1))
for r in range(8, 12):
    tprev[r,8:12] = 1

tnew = tast = np.zeros((slices+1, slices+1))

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

    # copying
    tprev = copy.deepcopy(tnew)

    # plotting
    if it % int(1/plot_frequency) == 0:
        try:
            plt.figure(1)
            plt.pcolor(tnew[1:slices,1:slices])
            plt.pause(0.001)
            plt.show
        except TclError:
            quit()

input('press ENTER to close\n')
plt.close



# ------------------------------------------------------------ #



# Released under CC0