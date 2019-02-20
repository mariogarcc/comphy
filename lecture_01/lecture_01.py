from module import *

# EXERCISE 1: Given function f(x) = x**2 - 3*x + e**x - 2 = 0 ,
# analyze the existence of roots in the interval [-2, 4]
print("""
EXERCISE 1: Given the function f(x) = x**2 - 3*x + e**x - 2 = 0 , 
analyze the existence of roots in the interval [-2, 4] 
(by dividing [-2, 4] in 20 subintervals)
""")

import numpy as np

def f(x): # given function
    return x**2 - 3*x + np.exp(x) - 2

xmin, xmax = -2, 4 # interval
n = 20 # number of subintervals

xarr = np.linspace(xmin, xmax, n+1)
xlin = np.linspace(xmin, xmax, 1000)

sols = find_sols(f, xarr)
print("There is (are) solution(s) in: ", *sols, sep = '\n')


# EXERCISE 2: Given an interval where a function has a single root,
# extrapolate a more precise solution using the bisection method.
print("""
EXERCISE 2: Given an interval where a function has a single root, 
extrapolate a more precise solution using the bisection method.
""")

print("Bisection method\n")

bis_sol_points = []
for sol in sols:
    print("case: solution in {sol}".format(sol = sol))
    bis_sol_points.append(bis_solve(f, sol, iters = 63))
    print("")


# EXERCISE 3: Calculate the solutions for f(x) using the regula falsi method.
print("""
EXERCISE 3: Calculate the solutions for f(x) using the regula falsi method.
""")

print("Falsi regula method\n")
falsi_sol_points = []
for sol in sols:
    print("case: solution in {sol}".format(sol=sol))
    falsi_sol_points.append(falsi_solve(f, sol, iters = 63))
    print("")


# EXERCISE 4: Calculate the roots for f(x) using the Newton-Raphson method.
print("""
EXERCISE 4: Calculate the roots for f(x) using the Newton-Raphson method.
""")

def df(x):
    return 2*x + np.exp(x) - 3
# derivative of function f(x)

print("Newton-Raphson method\nvia regula falsi for an approximate solution\n")

falsi_asols = []
for sol in sols:
    print("case: solution in {sol}".format(sol=sol))
    falsi_asols.append(falsi_solve(f, sol, iters = 7))
    print("")

newrap_sol_points = []
iterations = 15
for falsi_asol in falsi_asols:
    print("case: approximated solution x = {asol}".format(asol=falsi_asol))
    newrap_sol_points.append(newrap_sol(f, df, falsi_asol, iterations))
    print("iterations: {iterations}".format(iterations = iterations))
    print("")


# plotting
    
print("Plotting follows.")
ask_continue()

import matplotlib.pyplot as plt

plt.figure()
plt.title('bisection')
plt.plot(xlin, f(xlin), 'black')
gsize = max(f(xlin)) - min(f(xlin)) # plot vertical size

plt.hlines(0, min(xlin), max(xlin), 'green')

for sol in bis_sol_points:
    # highlight the solution points
    plt.vlines(sol, f(sol)-gsize/20, f(sol)+gsize/20, color = 'red')


plt.figure()
plt.title('regula falsi')
plt.plot(xlin, f(xlin), 'black')
gsize = max(f(xlin)) - min(f(xlin))  # plot vertical size

plt.hlines(0, min(xlin), max(xlin), 'green')

for sol in falsi_sol_points:
    # highlight the solution points
    plt.vlines(sol, f(sol)-gsize/20, f(sol)+gsize/20, color='red')


plt.figure()
plt.title('newton-raphson')
plt.plot(xlin, f(xlin), 'black')
gsize = max(f(xlin)) - min(f(xlin))  # plot vertical size

plt.hlines(0, min(xlin), max(xlin), 'green')

for sol in newrap_sol_points:
    # highlight the solution points
    plt.vlines(sol, f(sol)-gsize/20, f(sol)+gsize/20, color='red')


plt.show()
