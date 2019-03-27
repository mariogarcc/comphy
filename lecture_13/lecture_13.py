from package import redact_ex

from package import euler_differentiate, range_kutta_differentiate


EXERCISE_26 = """\
Make a program that is able to graphically solve the equation
dx/dt = sin(x) using the Euler method.\
"""

redact_ex(EXERCISE_26, 26)


import warnings
import numpy as np

warnings.filterwarnings('ignore')

# dx/dt = sin(x)

def inct(dt, *o):
    return dt

def incx(dt, t, x):
    return dt*np.sin(x)

print("Computing Euler method...", end='\n\n')
euler_differentiate([inct, incx], bounds = [0, 1], delta = 1e-2, itern = 1e4,
    title = r"Euler method for function"
        + r"$\:\:\frac{dx}{dt} = \sin(x)$")


EXERCISE_27 = """\
Make a program that is able to graphically solve the equation
d\u00B2x/dt\u00B2 + \u03C9_0\u00B2x = 0 using:
+ the Euler method
+ the Range-Kutta method of order 2
+ the Range-Kutta method of order 4
Comment on the effects of \u0394t over the obtained solutions
(analyze the methods' stability with regards to the \u0394t used).\
"""

redact_ex(EXERCISE_27, 27)


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


EXERCISE_28 = """\
Make a program that is able to graphically solve the equation
d\u00B2x/dt\u00B2 + b dx/dt + \u03C9_0\u00B2 x = 0 using the Euler method.\
"""

redact_ex(EXERCISE_28, 28)


# dx/dt = y
# dy/dt = -b*y - omega

b = 1/2; omega_0 = 2

def incx(dt, t, x, y):
    return dt * y

def incy(dt, t, x, y, b = b, omega_0 = omega_0):
    return dt * (-b*y - omega_0**2*x)

print("Computing Euler method...", end='\n\n')
euler_differentiate([inct, incx, incy], bounds = [0, 1, -1],
    delta = 1e-2, itern = 1e4, graph = [1, 2],
    title = r"Euler method for function"
        + r"$\:\:\frac{d^2x}{dt^2} + b \frac{dx}{dt} + \omega_0^2 x = 0$")


"""
Overall, all methods have a succesful result dependent on the size of deltat,
as one can already expect given the errors' dependencies on
deltat for each of the methods.
This is because a small deltat is required to detect function changes
"as soon as they happen" to provide an accurate representation
of the functions.
You probably noticed how the sinusoidal functions inclease in amplitude,
even though they should not. As explained above, this is because the
"change" in the function, up to when the computer detects it, is delayed
the given delta. There is another thing to this, which is the "phase"
of the method, so to say, which I'll try to explain:
Say the function shape in one of the sinusoidal peaks goes like this, in steps:
 / -> / -> -- -> \ -> \ 
Now imagine the delta is one such that the computer evaluates the function
every 3 steps and, for some reason, we start evaluating at step 2 (or 1 in
computer language). Then, the computer would see this:
 ? -> / -> ? -> ? -> \ 
What is the consequence of this? Well, the computer has been "thinking" that
the function has been increasing in value for 3 consecutive steps, while
in reality it only has been increasing for 1, then stopped, and then started
decreasing. The result is, as we have seen, slightly increasing amplitudes.
You can verify this by changing the value of delta. With a smaller delta,
the effect will be less noticeably, but one could theoretically also find
some delta and some initial conditions that would make this error disappear.
"""