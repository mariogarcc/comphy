print()
"""
Ahora utilizamos los conocimientos de la segunda parte de la asignatura
para resolver el problema. El esquema de Dufort-Frankel es extrapolable de
ejemplos anteriores para la ecuación diferencial sobre "u", con la adición
de la función f(u, v), mientras que la ecuación sobre "v" se resuelve
con la discretización sencilla de la derivada con la función g(u, v).
Cabe la duda de a qué corresponden los valores de "u" y "v" en cada una
de las funciones añadidas, pero mirando la expresión algebraica se puede
deducir que su valor discreto sería nada más que el correspondiente a
"u(t)" y "v(t)", es decir, "u_i^n" y "v_i^n" respectivamente.
Como es un sistema de ecuaciones se ha de calcular cada uno de los nuevos
valores en el mismo intervalo de tiempo, y luego habrá que aplicar la
normalización correspondiente al método de Dufort-Frankel.

Para calcular la velocidad de la onda computacionalmente (de forma aproximada),
encuentro la amplitud de la onda de transporte, que al ser simétrica la mitad
de su distancia entre picos es una aproximación aceptable, y mido cuánto tarda
el centro de la onda en llegar al final del medio desde el punto de comienzo
(un cuarto del medio a la izquierda).
"""

# program setup
import numpy as np
import matplotlib.pyplot as plt
import _tkinter
TclError = _tkinter.TclError

plt.rc('text', usetex = True)

# computation parameters
slices = 200
itern = 1200
plot_frequency = 0.1

# differentiation parameters
deltat = 0.004
deltax = 0.1

# problem parameters
D = 1

epsilon = 10; a = 0.1
def f(u, v, epsilon = epsilon, a = a):
    return epsilon * (u * (a-u) * (u-1) - v)

b = 0.1; gamma = 1
def g(u, v, b = b, gamma = gamma):
    return b*u - gamma*v

# helper variables
s = D*deltat/deltax**2

# grids creation
upprev = np.zeros(slices+1); uprev = np.zeros(slices+1); unew = np.zeros(slices+1)
vpprev = np.zeros(slices+1); vprev = np.zeros(slices+1); vnew = np.zeros(slices+1)

# with initial conditions
u1 = 0; v1 = 0 # already in grid
u3 = 0.8702; v3 = 0.0870
upprev[0:50] = u3; uprev[0:50] = u3; unew[0:50] = u3
vpprev[0:50] = v3; vprev[0:50] = v3; vnew[0:50] = v3

# computation
check = False
for r in range(itern):

    # next row computation
    for j in range(1, slices):
        vnew[j] = vprev[j] + deltat*g(uprev[j], vprev[j])
        unew[j] = (2*s*(uprev[j-1] - upprev[j] + uprev[j+1]) + 2*deltat*f(uprev[j], vprev[j]) + upprev[j])/(1+2*s)

    # dufort-frankel normalization
    unew = (unew+uprev)/2

    # contour conditions
    unew[0] = unew[1]; unew[slices] = unew[slices-1]
    vnew[0] = vnew[1]; vnew[slices] = vnew[slices-1]

    # reset row assignments
    upprev = uprev; uprev = unew
    vpprev = vprev; vprev = vnew

    # approximate speed calculation
    if not check:
        if r == 1000:
            amp = max(unew)/2
        if r >= 1000:
            if unew[slices] > amp:
                # wave looks symmetric, so amp can be (max-low)/2
                print(f"wave amplitude: {amp:.4f} (u) (max = {2*amp:.4f}; low = 0)")
                # average time after goal with time before goal for a correct approximation
                print(f"time elapsed: {((r-1)*deltat+r*deltat)/2:.2f} (t) ({r-1}-{r} iterations)")
                print(f"space traveled: {(slices-50)*deltax:.2f} (x) ({slices-50} pixels)")
                print(f"approximate speed = {(slices-50)*deltax/(r*deltat):.4f} (x/t)")
                check = True

    # plot solution
    if int(r % int(1/plot_frequency)) == 0:
        try:
            plt.figure(1)
            plt.cla()

            plt.title(r"$\frac{\partial u}{\partial t} = f(u, v) + D\,\frac{\partial^{2} u}{\partial x^{2}}$", fontsize = 16)

            plt.ylabel(r"$u$", fontsize = 16)
            plt.xlabel(r"$x\,(pix \times \Delta x)$", fontsize = 16)

            plt.ylim(0, 1)
            plt.xlim(0, 20)
            plt.plot([j*deltax for j in range(slices+1)], unew)

            plt.show
            plt.pause(0.01)
            if r == 700:
                plt.savefig("wave.png")
        except TclError:
            quit()

# await close
input("press ENTER to continue")
plt.close()

    