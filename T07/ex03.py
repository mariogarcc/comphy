from package import redact_ex

from package import \
    euler_differentiate, \
    range_kutta_differentiate


EXERCISE_03 = """\
Make a program that is able to graphically solve the equation
dP/dt = rP * (1 - P/k) using:
+ the Euler method
+ the Range-Kutta method of order 2
+ the Range-Kutta method of order 4
Comment on the effects of \u0394t over the obtained solutions
(analyze the methods' stability with regards to the \u0394t used).\
"""

redact_ex(EXERCISE_03, 3)


# dp/dt = r*p * (1-p/k)

def inct(dt, *o):
    return dt

r = 1; k = 1
def incp(dt, t, p, r = r, k = k):
    return dt * r*p * (1-p/k)

print("Computing Euler method...", end='\n\n')
euler_differentiate([inct, incp], bounds = [0, 10],
    delta = 1e-3, itern = 3e3,
    title = r"Euler method for function"
        + r"$\:\:\frac{dP}{dt} = r\;P \: \left( 1 - \frac{P}{k} \right)$")

print("Computing Range-Kutta method of order 2...", end='\n\n')
range_kutta_differentiate([inct, incp], bounds = [0, 10], order = 2,
    delta = 1e-3, itern = 3e3,
    title = r"Range-Kutta method of order 2 for function"
        + r"$\:\:\frac{dP}{dt} = r\;P \: \left( 1 - \frac{P}{k} \right)$")

print("Computing Range-Kutta method of order 4...", end='\n\n')
range_kutta_differentiate([inct, incp], bounds = [0, 10], order = 4,
    delta = 1e-3, itern = 3e3,
    title = r"Range-Kutta method of order 4 for function"
        + r"$\:\:\frac{dP}{dt} = r\;P \: \left( 1 - \frac{P}{k} \right)$")