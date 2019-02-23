from package import *

# EXERCISE: Make a program that computes the integral of a function f(x)
# in an interval [a, b] using the rule of the trapeze. Apply that to the case
# f(x) = x**3 - 3*x**2 - x + 3 and a = 0, b = 1.35
print("""
EXERCISE: Make a program that computes the integral of a function f(x)
in an interval [a, b] using the rule of the trapeze. Apply that to the case
f(x) = x**3 - 3*x**2 - x + 3 and a = 0, b = 1.35
""")

def f(x):
    return x**3 - 3*x**2 - x + 3

interval = [0, 1.35]
a, b = interval

nk = int(1e6) # number of subintervals
k = (i+1 for i in range(nk+1))
delta = (b-a)/nk
x = (a + delta*(k_i-1) for k_i in k)

integral_ab = (delta/2)*(f(a)+f(b)) + (delta*sum((f(x_k) for x_k in x)))

print("Integrating f(x) in {!s} yields:".format(interval),
    integral_ab, sep = '\n')