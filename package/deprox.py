import re
import numpy as np

# Q: why not just round?
# A: rounding e.g. 1.2345670000004 with a fixed "tolerance" of 4 gives 1.2346
#    instead of 1.234567.

def deprox_num(num, tol = 4, offset = 0):
    """
    """
    numstr = '{:.24f}'.format(num) if num > 1e-24 else str(num)
    tol = int(tol)
    ov = int(offset) # offset value
    
    try:
        dpl = re.search(r'\.', numstr).start()+1 # decimal point location
        seqs = re.search(r'(0{{{tol},}}|9{{{tol},}})'.format(tol = tol), numstr[dpl:]) \
            .start() # sequence start
    except AttributeError: # no regex match
        return num

    # remove the unwanted decimal values from the end
    cn = int(num*10**(seqs+ov+1))/10**(seqs+ov+1) # cut number
    return round(cn, seqs+ov)


def deprox_arr(arr, tol = 4, offset = 0):
    """
    """
    return [deprox_num(val) for val in arr]


def deprox_mat(mat, tol = 4, offset = 0):
    """
    """
    for r in range(mat.shape[0]):
        for c in range(mat.shape[1]):
            mat[r,c] = deprox_num(mat[r,c],
                tol = tol, offset = offset)
                # tol = int(np.log10(lim)), offset = offset)

    return mat

# to do: precision kwarg, e.g. to deprox up to a certain decimal point (round)