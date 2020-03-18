import numpy as np
import matplotlib.pyplot as plt
import _tkinter
TclError = _tkinter.TclError

def solve_explicit_ode(
        constructor,
        initial_conditions, boundary_conditions,
        slices, itern, plot_frequency = 1):
    
    grid = initial_conditions
    next_grid_row = initial_conditions[0]

    for lap in range(itern):

        next_grid_row = constructor(next_grid_row, grid)
        next_grid_row, *grid = boundary_conditions(lap, next_grid_row, grid)

        grid = [next_grid_row] + grid[:-1]

        if lap % int(1/plot_frequency) == 0:
            try:
                plt.figure(1)
                plt.plot(grid[0])
                plt.pause(0.1)
                plt.show
            except TclError: # catches error by closing tab manually
                print("plot closed manually.", end = '\n\n')
                plt.close('all')
                return

    input("press ENTER to continue\n")
    plt.close('all')
    return None


def solve_implicit_ode(
        constructor_mat, constructor_helper_mat,
        initial_conditions, boundary_conditions,
        slices, itern, plot_frequency = 1):
    
    grid = initial_conditions
    next_grid_row = initial_conditions[0]

    for lap in range(itern):

        constructor_intermediary_arr = constructor_helper_mat @ grid[0]
        constructor_intermediary_arr = boundary_conditions(lap, constructor_intermediary_arr)
        next_grid_row = constructor_mat @ constructor_intermediary_arr

        grid = [next_grid_row] + grid[:-1]

        if lap % int(1/plot_frequency) == 0:
            try:
                plt.figure(1)
                plt.plot(grid[0])
                plt.pause(0.1)
                plt.show
            except TclError:
                print("plot closed manually.")
                plt.close('all')
                return

    input("press ENTER to continue\n")
    plt.close('all')
    return None
