def sign_changes(x, z):
    """
    Checks if two numbers have different sign
    """
    return x*z < 0

def fsign_changes(f, x, z):
    return f(x)*f(z) < 0

def seq_sign_changes(arr, i):
    """
    Checks whether a sequence's i'th element has different sign from the i+1'th
    element
    """
    return arr[i]*arr[i+1] < 0

def fseq_sign_changes(f, arr, i):
    """
    Checks whether a sequence's i'th image through a function f has different 
    sign from the i+1'th element
    """
    return f(arr[i]) * f(arr[i+1]) < 0


# notice how if introducing, as `f`, `lambda x: x` you can simply check for
# array values sign changes

# in other words:
# `fseq_sign_changes(lambda x: x, arr, i = 0)`
# is equivalent to
# `def fseq_sign_changes(arr, i = 0): return arr[i] * arr[i+1] < 0`

# >>> [(i, i+1) for i in range(3) \
# ...     if fseq_sign_changes(lambda x: x, [-2, -1, 1, 2], i))
# [(1, 2)]