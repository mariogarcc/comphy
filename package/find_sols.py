def find_sols(f, arr, sign_check_func = lambda x, y: x*y < 0, verbose = False):
    """
    Given an array of section points, checks if function *f* has a solution
    in any of the intervals formed by said points.
    """
    sols = []
    for i in range(len(arr)-1):
        if sign_check_func(f(arr[i]), f(arr[i+1])):
            sols.append([arr[i], arr[i+1]])

    if verbose:
        print("solution(s) in: ", *sols, sep = '\n')
    return sols
