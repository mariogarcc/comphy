import numpy as np

def gen_lineqsys(size = 3, sbound = 5, cbound = 5, ntype = 'int',
    print_res = False):
    """
    Generates a system of linear equations of `size` variables with their
    coefficients being inbetween [`-cbound`, `cbound`], solutions being
    in the range of [`-sbound`, `sbound`]. `ntype` chooses whether
    coefficients should be integers or any rational number.
    """

    assert ntype in ['int', 'half', 'float']

    if ntype == 'int':
        sols = np.array([var - sbound \
            for var in np.random.randint(2*sbound, size = size)])
    elif ntype == 'half':
        sols = np.array([(var - sbound)/2 \
            for var in np.random.randint(2*sbound, size = size)])
    elif ntype == 'float':
        sols = np.array([(var*2*sbound - sbound)/2 \
            for var in np.random.rand(size)])

    mat = np.array([]).reshape(0, size)
    for _ in range(size):
        if ntype == 'int':
            coeffs = np.array([var - cbound \
                for var in np.random.randint(2*cbound, size = size)])
        elif ntype == 'half':
            coeffs = np.array([(var - cbound)/2 \
                for var in np.random.randint(2*cbound, size = size)])
        elif ntype == 'float':
            coeffs = np.array([(var*2*cbound - cbound)/2 \
                for var in np.random.rand(size)])
        try:
            mat.size
        except AttributeError:
            mat = coeffs
        else:
            mat = np.vstack([mat, coeffs])
    
    ind_terms = []
    for r in range(mat.shape[0]):
        ind_terms.append(sum([c*x for c,x in zip(mat[r,:],sols)]))
    ind_terms = np.array(ind_terms).reshape(size, 1)

    emat = np.hstack([mat, ind_terms])

    if print_res == True:
        print("Matrix of coefficients (A):", mat, sep = '\n', end = '\n\n')
        print("Vector of independent terms (B):", ind_terms, sep = '\n', end = '\n\n')
        print("Extended matrix (AB):", emat, sep = '\n', end = '\n\n')
        print("Solutions to the system:", sols, sep = '\n', end = '\n\n')

    return mat, ind_terms, emat, sols