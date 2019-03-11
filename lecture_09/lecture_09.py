from package import redact_ex

from package import montecarlo_integrate


EXERCISE_19 = """\
Make a program able to compute the integral between [0, 1] for
f(x) = (1-x**2)**1.5 using the Monte Carlo method.\
"""

def f(x):
    return (1-x**2)**1.5

interval = [0, 1] # interval

integral, integral_err = montecarlo_integrate(f, interval)

print("Integral between {interval!s} for f(x): {result}" \
    .format(interval = interval, result = integral))
print("Error for the aboveshown integration: {error:.2e}" \
    .format(error = integral_err))