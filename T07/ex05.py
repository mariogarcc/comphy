from package import redact_ex

from package import euler_differentiate_mod


EXERCISE_05 = """\
Make a program that is able to graphically solve any of the equations
proposed beforehand using a variable-step integration method.
(Chose the population equation.)\
"""

redact_ex(EXERCISE_05, 5)


# dp/dt = r*p * (1-p/k)

def inct(dt, *o):
    return dt

r = 1; k = 1
def incp(dt, t, p, r = r, k = k):
    return dt * r*p * (1-p/k)

print("Computing Euler method with variable-step...", end='\n\n')
euler_differentiate_mod([inct, incp], bounds = [0, 10],
    delta = 1e-2, itern = 1e2,
    step_mults = [0.5, 2], tols = [0.5, 0.1],
    max_delta = 1, min_delta = 1e-6, # verbose = True,
    title = r"Euler method for function"
        + r"$\:\:\frac{dP}{dt} = r\;P \: \left( 1 - \frac{P}{k} \right)\:\:$"
        + r"with variable-step")

# set kwarg `verbose` to True to see how delta varies
# notice how, even when having a smaller itern to delta ratio,
# the function evaluates much further in time than other methods in this case
