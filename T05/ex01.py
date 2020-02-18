from package import redact_ex

from package import montecarlo_integrate


EXERCISE_19 = """\
Make a program able to compute the integral between [0, 1] for
f(x) = (1-x**2)**1.5 using the Monte Carlo method.\
"""

redact_ex(EXERCISE_19, 1)

def f(x):
    return (1-x**2)**1.5

interval = [0, 1] # interval

integral, integral_err = montecarlo_integrate(f, interval)

print(f"Integral between {interval!s} for f(x): {integral}")
print(f"Error for the aboveshown integration: {integral_err:.2e}")