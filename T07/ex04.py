from package import redact_ex

from package import \
    euler_differentiate, \
    range_kutta_differentiate


EXERCISE_04 = """\
Make a program that is able to graphically solve the set of equations
{
    dx/dt = \u03C3 (y-x)
    dy/dt = r x - y - x z
    dz/dt = x y - b z
}
(Lorenz attractor) using:
+ the Euler method
+ the Range-Kutta method of order 2
+ the Range-Kutta method of order 4
Comment on the effects of \u0394t over the obtained solutions
(analyze the methods' stability with regards to the \u0394t used).\
"""

redact_ex(EXERCISE_04, 4)


# dx/dt = sigma*(y-x)
# dy/dt = (r*x - y - x*z)
# dz/dt = (x*y - b*z)

sigma = 3; r = 26.5; b = 1
ip = [0, 0, 1, 0] # initial parameters

def inct(dt, *o):
    return dt

def incx(dt, t, x, y, z, sigma = sigma):
    return dt * sigma*(y-x)

def incy(dt, t, x, y, z, r = r):
    return dt * (r*x - y - x*z)

def incz(dt, t, x, y, z, b = b):
    return dt * (x*y - b*z)


print("Computing Euler method...", end='\n\n')
euler_differentiate([inct, incx, incy, incz], bounds = ip,
    delta = 1e-2, itern = 1e4, graph = [0, 3],
    title = r"Euler method for the Lorenz attractor")

print("Computing Range-Kutta method of order 2...", end='\n\n')
range_kutta_differentiate([inct, incx, incy, incz], bounds = ip, order = 2,
    delta = 1e-2, itern = 1e4, graph = [0, 3],
    title = r"Range-Kutta method of order 2 for the Lorenz attractor")

print("Computing Range-Kutta method of order 4...", end='\n\n')
range_kutta_differentiate([inct, incx, incy, incz], bounds = ip, order = 4,
    delta = 1e-2, itern = 1e4, graph = [0, 3],
    title = r"Range-Kutta method of order 4 for the Lorenz attractor")
