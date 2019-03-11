from package import redact_ex

from package import trapeze_integrate


EXERCISE_13 = """\
Make a program that computes the integral of a function f(x)
in an interval [a, b] using the rule of the trapeze. Apply that to the case
f(x) = x**3 - 3*x**2 - x + 3 and a = 0, b = 1.35"""

redact_ex(EXERCISE_13, 13)


def f(x):
    return x**3 - 3*x**2 - x + 3

interval = [0, 1.35]

integral_ab = trapeze_integrate(f, interval)

print("Integrating f(x) in {!s} yields:".format(interval),
    integral_ab, sep = '\n')

def pf(x): # primitive of f(x)
    return (1/4)*x**4 - x**3 - (1/2)*x**2 + 3*x

print("Correct result:", pf(1.35)-pf(0), sep = '\n', end = '\n\n')